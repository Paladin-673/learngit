package OtherExam;

public class Mr_StringCut {
	public static void main(String[] args) {
		String str1,str2,str3;
		String str = "123[liyue]de /?2013-2017id=4788";
		str1 = str.substring(str.indexOf("[")+1,str.indexOf("]"));
		str2 = str.substring(str.indexOf("?")+1,str.indexOf("id="));
		str3 = str.substring(str.indexOf("=")+1);
		
		System.out.println("username: " + str1);
		System.out.println("time: " + str2);
		System.out.println("userid: " + str3);
	}

}
