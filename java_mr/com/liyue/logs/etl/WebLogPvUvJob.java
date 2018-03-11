package com.liyue.logs.etl;

import java.io.IOException;

import org.apache.commons.lang.StringUtils;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.jobcontrol.ControlledJob;
import org.apache.hadoop.mapreduce.lib.jobcontrol.JobControl;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class WebLogPvUvJob extends Configured implements Tool {
	private static final String TMP_PATH = "/tmp/pvuvjob";

	public static class KeyCountMapper extends Mapper<LongWritable,Text,Text,LongWritable>{

		private LongWritable one = new LongWritable(1);
		private Text uidKey = new Text();

		@Override
		protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, LongWritable>.Context context)
				throws IOException, InterruptedException {
			String fields[] = StringUtils.split(value.toString(),'\001');
			if(fields.length != 6) {
				return;
			}
			
			String query = fields[4];//parameters
			int startIndex = query.indexOf("uid=");
			int endIndex = query.indexOf('&',startIndex);
			
			String uid = "empty";
			if(startIndex >= 0) {
				uid = endIndex > startIndex ? query.substring(startIndex + 4,endIndex) : query.substring(startIndex + 4);
			}
			
			uidKey.set(uid);
			context.write(uidKey, one);
		}
		
	}
	
	public static class KeyCountReducer extends Reducer<Text,LongWritable,Text,LongWritable>{

		private LongWritable sumValue = new LongWritable();

		@Override
		protected void reduce(Text key, Iterable<LongWritable> value,
				Reducer<Text, LongWritable, Text, LongWritable>.Context context) throws IOException, InterruptedException {
			long sum = 0L;
			
			for(LongWritable v : value) {
				sum += v.get();
			}
			
			sumValue.set(sum);
			context.write(key, sumValue );
		}
		
	}
	
	public static class KeySumMapper extends Mapper<Text,LongWritable,NullWritable,LongWritable>{

		private LongWritable result = new LongWritable();

		//uid \t count
		@Override
		protected void map(Text key, LongWritable value,
				Mapper<Text, LongWritable, NullWritable, LongWritable>.Context context)
				throws IOException, InterruptedException {
			String[] fields = StringUtils.split(value.toString(),'\t');
			
			result.set(Long.parseLong(fields[1]));
			context.write(NullWritable.get(), result );
		}
		
	}

	public static class KeySumReducer extends Reducer<NullWritable,LongWritable,LongWritable,LongWritable>{


		private LongWritable pvKey = new LongWritable();
		private LongWritable uvValue = new LongWritable();

		@Override
		protected void reduce(NullWritable key, Iterable<LongWritable> values,
				Reducer<NullWritable, LongWritable, LongWritable, LongWritable>.Context context)
				throws IOException, InterruptedException {
			Long pv = 0L;
			Long uv = 0L;
			
			for(LongWritable v : values) {
				pv += v.get();
				uv ++;
			}
			
			pvKey.set(pv);
			uvValue.set(uv);
			context.write(pvKey ,uvValue);
		}
		
	}
	
	private Job configureCountJob(String input,String output) throws IOException {
		Job job = Job.getInstance(getConf(),"KeyCountJob");
		
		job.setJarByClass(WebLogPvUvJob.class);
		job.setMapperClass(KeyCountMapper.class);
		job.setReducerClass(KeyCountReducer.class);
		job.setCombinerClass(KeyCountReducer.class);
		
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(LongWritable.class);
		
		FileInputFormat.setInputPaths(job, new Path(input));
		
		Path outputDir = new Path(output);
		FileOutputFormat.setOutputPath(job,outputDir);
		
		deletePath(outputDir);
		
		return job;
	}

	private Job configureSumJob(String input,String output) throws IOException {
		Job job = Job.getInstance(getConf(),"KeySumJob");
		
		job.setJarByClass(WebLogPvUvJob.class);
		job.setMapperClass(KeySumMapper.class);
		job.setReducerClass(KeySumReducer.class);
		
		job.setMapOutputKeyClass(NullWritable.class);
		job.setMapOutputValueClass(LongWritable.class);
		job.setOutputKeyClass(LongWritable.class);
		job.setOutputValueClass(LongWritable.class);
		
		FileInputFormat.setInputPaths(job, new Path(input));
		
		Path outputDir = new Path(output);
		FileOutputFormat.setOutputPath(job,outputDir);
		
		deletePath(outputDir);
		
		return job;
	}
	
	private void deletePath(Path outputDir) throws IOException {
		FileSystem fs = FileSystem.get(getConf());
		if(fs.exists(outputDir)) {
			fs.delete(outputDir,true);
		}
	}
	
	public int run(String[] args) throws Exception {
		if(args.length < 2) {
			System.out.println("<input> <output>");
			return 2;
		}
		Job countJob = configureCountJob(args[0], TMP_PATH);
		Job sumJob = configureSumJob(TMP_PATH, args[1]);
		
		ControlledJob c1 = new ControlledJob(getConf());
		c1.setJob(countJob);
		
		ControlledJob c2 = new ControlledJob(getConf());
		c2.setJob(sumJob);
		c2.addDependingJob(c1);
		
		JobControl jobCtrl = new JobControl("WebLogPvUvJob");
		jobCtrl.addJob(c1);
		jobCtrl.addJob(c2);
		
		Thread t = new Thread(jobCtrl);
		t.start();
		
		while(true) {
			if(jobCtrl.allFinished()) {
				System.out.println(jobCtrl.getSuccessfulJobList());
				jobCtrl.stop();
				return 0;
			}
			if(!jobCtrl.getFailedJobList().isEmpty()) {
				System.out.println(jobCtrl.getFailedJobList());
				jobCtrl.stop();
				return 1;
			}
		}
	}

	public static void main(String[] args) throws Exception {
		int res = ToolRunner.run(new WebLogPvUvJob(), args);
		System.exit(res);
		
	}

}
