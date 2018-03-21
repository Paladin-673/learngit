package com.liyue.logs.etl;

import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.util.regex.Pattern;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.conf.Configured;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
import org.apache.hadoop.mapreduce.lib.output.MultipleOutputs;
import org.apache.hadoop.mapreduce.lib.output.TextOutputFormat;

public class WordCountMutiExport extends Configured {
	
	public static class mutiMapper extends Mapper<LongWritable,Text,Text,IntWritable>{

		private static final Pattern PATTERN = Pattern.compile(" ");
		Text K = new Text();
		IntWritable V = new IntWritable(1);

		@Override
		protected void map(LongWritable key, Text value, Context context)
				throws IOException, InterruptedException {
			
			String[] words = PATTERN.split(value.toString());
			System.out.println("**********" + value.toString());
			for(String word : words) {
				K.set(word);
				context.write(K, V);
			}
		}
		
	}

	/**
	 * 对单词做词频统计
	 * @author liyue
	 *
	 */
	public static class mutiReducer extends Reducer<Text, IntWritable, Text, IntWritable>{
		//将结果输出到多个文件或多个文件夹
		private MultipleOutputs<Text, IntWritable> mos;
		//创建MutipleOutputs对象
		protected void setup(Context context) throws IOException, InterruptedException {
			mos = new MultipleOutputs<Text,IntWritable>(context);
		}
		@Override
		protected void reduce(Text key, Iterable<IntWritable> values,
				Context context) throws IOException, InterruptedException {
			IntWritable V = new IntWritable();
			int sum = 0;
			for(IntWritable value : values) {
				sum = sum + value.get();
			}
			System.out.println("word:" + key.toString() + "    sum = " + sum);
			V.set(sum);
			
			//使用MutipleOutputs对象输出数据
			if(key.toString().equals("hello")) {
				mos.write("hello", key, V);
			}else if(key.toString().equals("world")) {
				mos.write("world", key, V);
			}else if(key.toString().equals("hadoop")) {
				//输出到hadoop/hadoopfile-r-00000文件
				mos.write("hadoopfile", key, V, "hadoop/");
			}
		}
		
		
		//关闭MultipleOutputs对象
		protected void cleanup(Context context)
				throws IOException, InterruptedException {
			mos.close();
		}
		
	}
	public static void main(String[] args) {
		String in = "/home/badou/Desktop/test/word/";
		String out = "hdfs://localhost:9000/hdfs/test/wordcount/output/";
		
		Job job;
		try {
			//删除hdfs目录
			WordCountMutiExport wcme = new WordCountMutiExport();
			
			wcme.removeDir(out);
			
			job = new Job(new Configuration(),"wordcountmultiExport");
			job.setOutputKeyClass(Text.class);
			job.setOutputValueClass(IntWritable.class);
			job.setMapperClass(mutiMapper.class);
			job.setCombinerClass(mutiReducer.class);
			job.setReducerClass(mutiReducer.class);
			
			//定义附加的输出文件
			MultipleOutputs.addNamedOutput(job, "hello", TextOutputFormat.class, Text.class, IntWritable.class);
			MultipleOutputs.addNamedOutput(job, "world", TextOutputFormat.class, Text.class, IntWritable.class);
			MultipleOutputs.addNamedOutput(job, "hadoopfile", TextOutputFormat.class, Text.class, IntWritable.class);
			
			FileInputFormat.addInputPath(job, new Path(in));
			FileOutputFormat.setOutputPath(job, new Path(out));
			
			job.waitForCompletion(true);
			
		}catch(IOException e) {
			e.printStackTrace();
		}catch(URISyntaxException e) {
			e.printStackTrace();
		}catch(ClassNotFoundException e) {
			e.printStackTrace();
		}catch(InterruptedException e) {
			e.printStackTrace();
		}

	}
	
	
	@SuppressWarnings("deprecation")
	private void removeDir(String filePath) throws IOException, URISyntaxException {
		String url = "hdfs://localhost:9000";
		FileSystem fs = FileSystem.get(new URI(url), new Configuration());
		fs.delete(new Path(filePath));
	}

}
