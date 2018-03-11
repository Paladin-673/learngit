package Library;

import java.util.*;
import java.util.Scanner;

public class LibraryManager {
	Scanner sc=new Scanner(System.in);
	//替换前代码
	//Library library=new Library();
	//替换后代码
	Library library=null;
	public LibraryManager(Library library) {
		super();
		this.library=library;
	}
	
	//得到数量
	public void getBookNumber() {
		System.out.println("请从OOP、JAVA、C++、python、JSP中选择输入书籍的名称：");
		String str=sc.next();
		Book book=(Book) library.map.get(str);
		if(library.map.containsKey(str)) {
			System.out.println("当前输入的书名是："+str);
			System.out.println("当前选中书的单价是："+book.getPrice());
			System.out.println("当前书在图书馆的数量是:"+book.getNumber());
		}else {
			System.out.println("您的图书馆中没有这本书！");
		}
	}
}
