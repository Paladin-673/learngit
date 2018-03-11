package com.liyue.logs.etl;

import java.io.IOException;
import java.net.URLDecoder;
import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Locale;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.NullWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class DataHandleMapper extends Mapper<LongWritable, Text, NullWritable, Text> {
	private static final String SEP = "\t";

	private Pattern pattern = Pattern.compile("(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}) - \\S+ \\[(.+)\\] \"\\S+ (\\S+)\\?(\\S+) \\S+\" \\d+ \\d+ \"\\S+\" \"(.+)\"");
	
	private SimpleDateFormat dataTimeFormat = new SimpleDateFormat("dd/MMM/yyyy:HH:mm:ss Z", Locale.US);
	private SimpleDateFormat recordTimeFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
	
	private StringBuilder buffer = new StringBuilder(1024);

	private Text result = new Text();
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, NullWritable, Text>.Context context)
			throws IOException, InterruptedException {

		Matcher r = pattern.matcher(value.toString());
		if(!r.find()) {
			context.getCounter("MY COUNTERS", "error-lines").increment(1);
			return;
		}
		
		buffer.delete(0, buffer.length());
		buffer.append(r.group(1)).append(SEP);//IP
		
		try {
			Date date = dataTimeFormat.parse(r.group(2));//datetime
			buffer.append(date.getTime()).append(SEP);//timestamp
			buffer.append(recordTimeFormat.format(date)).append(SEP);//datetime
			
		} catch (ParseException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		
		buffer.append(r.group(3)).append(SEP);//url
		buffer.append(URLDecoder.decode(r.group(4), "utf-8")).append(SEP);//parameters
		buffer.append(r.group(5));//user-agent
		
		result.set(buffer.toString());
		context.write(NullWritable.get(), result );
		
	}

}

