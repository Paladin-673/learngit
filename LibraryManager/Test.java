package Library;

public class Test {
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Library library=new Library();
		library.add(new Book(132,98,"OOP"));
		library.add(new Book(12,12.5,"JAVA"));
		library.add(new Book(22,45,"JSP"));
		library.add(new Book(200,33,"python"));
		library.add(new Book(42,18,"C++"));
		//替换前
		//LibraryManager librarymanager=new LibraryManager();
		//替换后
		LibraryManager librarymanager=new LibraryManager(library);
		
		librarymanager.getBookNumber();
	}
}
