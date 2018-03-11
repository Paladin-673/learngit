package com.liyue.logs.etl;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Hello world!
 *
 */
public class App 
{
    public static void main( String[] args )
    {
    	String s = "127.0.0.1 - - [23/Feb/2017:09:58:37 +0800] \"GET /?dd=ss&dsd=899&uid=4d09eeac8ed65 HTTP/1.1\" 200 555 \"-\" \"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36\" \"-\"";
        
    	Pattern pattern = Pattern.compile("(\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}) - \\S+ \\[(.+)\\] \"\\S+ (\\S+)\\?(\\S+) \\S+\" \\d+ \\d+ \"\\S+\" \"(.+)\"");
    	
    	Matcher r = pattern.matcher(s);
    	if(r.find()) {
    		for(int i=1; i<=r.groupCount(); i++) {
    			System.out.println(r.group(i));
    		}
    	}else {
    		System.out.println("not found");
    	}
    }
}

