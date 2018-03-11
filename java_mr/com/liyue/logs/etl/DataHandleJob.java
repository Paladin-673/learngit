package com.liyue.logs.etl;


import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.util.Tool;
import org.apache.hadoop.util.ToolRunner;

public class DataHandleJob extends Configured implements Tool {

	public int run(String[] args) throws Exception {
		if(args.length < 2) {
			System.out.println("input output dir");
			return 2;
		}
		Job job = Job.getInstance(getConf(), "DataHandleJob");
		job.setJarByClass(DataHandleJob.class);
		job.setMapperClass(DataHandleMapper.class);
		job.setMapOutputKeyClass(NullWritable.class);
		job.setMapOutputValueClass(Text.class);
		
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

