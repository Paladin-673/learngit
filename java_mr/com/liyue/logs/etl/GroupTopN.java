package com.liyue.logs.etl;

import java.io.IOException;
import java.util.TreeSet;

import org.apache.hadoop.conf.Configuration;
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
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.GenericOptionsParser;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class GroupTopN extends Configured implements Tool{
	
	public static class GroupTopNMapper extends Mapper<LongWritable,Text,Text,LongWritable>{

		private Text outKey = new Text();
		private LongWritable outValue = new LongWritable();
		String[] valArr = null;
		

		@Override
		protected void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {
			valArr = value.toString().split("\t");
			outKey.set(valArr[1]);
			outValue.set(Long.parseLong(valArr[2])); //城市
			context.write(outKey, outValue ); //人口数
		}
		
	}
	
	public static class GroupTopNReducer extends Reducer<Text,LongWritable,Text,LongWritable>{

		private LongWritable outValue = new LongWritable();

		@Override
		protected void reduce(Text key, Iterable<LongWritable> values,
				Context context) throws IOException, InterruptedException {
			TreeSet<Long> numberTreeSet = new TreeSet<Long>(); //调用util库中的有序数组，用来存储人数number
			for (LongWritable v : values) {
				numberTreeSet.add(v.get());
				if(numberTreeSet.size() > 3) {
					numberTreeSet.remove(numberTreeSet.first()); //当Set中的数量大于3时，把最小的移除
				}
			}
			
			for(Long number : numberTreeSet) {
				outValue.set(number);
				context.write(key, outValue);
			}
		}
		
	}
//原来
	/*
	public static void main(String[] args) throws IOException, ClassNotFoundException, InterruptedException {
		Configuration conf = new Configuration();
		String[] otherArgs = new GenericOptionsParser(conf,args).getRemainingArgs();
		
		System.out.println(otherArgs.length);
		System.out.println(otherArgs[0]);
		System.out.println(otherArgs[1]);
		
		if(otherArgs.length != 3) {
			System.err.println("Usage:GroupTopN <in> <out>");
			System.exit(2);
		}
		
		Job job = new Job(conf,"GroupTopK");
		job.setJarByClass(GroupTopN.class);
		job.setMapperClass(GroupTopNMapper.class);
		job.setReducerClass(GroupTopNReducer.class);
		
		job.setNumReduceTasks(1);
		job.setOutputKeyClass(LongWritable.class);
		job.setOutputValueClass(LongWritable.class);
		
		FileInputFormat.addInputPath(job, new Path(otherArgs[1]));
		FileOutputFormat.setOutputPath(job, new Path(otherArgs[2]));
		System.exit(job.waitForCompletion(true) ? 0 : 1);

	}
	*/
//按job的修改
	public int run(String[] args) throws Exception {
		if(args.length < 2) {
			System.out.println("input output dir");
			return 2;
		}
		Job job = Job.getInstance(getConf(), "GroupTopN");
		job.setJarByClass(GroupTopN.class);
		job.setMapperClass(GroupTopNMapper.class);
		job.setReducerClass(GroupTopNReducer.class);
		
		job.setNumReduceTasks(1);
		job.setOutputKeyClass(LongWritable.class);
		job.setOutputValueClass(LongWritable.class);
		
		Path outputDir = new Path(args[1]);
		
		FileSystem fs = FileSystem.get(getConf());
		if(fs.exists(outputDir)) {
			fs.delete(outputDir,true);
		}
		
		
		FileInputFormat.setInputPaths(job, new Path(args[0]));		
		FileOutputFormat.setOutputPath(job, outputDir);

		return job.waitForCompletion(true) ? 0 : 1;
	}

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub

		int res = ToolRunner.run(new DataHandleJob(), args);
		System.exit(res);
	}
}
