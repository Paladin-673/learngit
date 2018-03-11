package Library;

import java.util.*;

public class Library {
	Map map=new HashMap();
	public void add(Book book) {
		//book是形似参数，只要保证传值时传的是对象即可，对象名随意
		map.put(book.getName(), book);//形式参数，要与book同名
	}
}
