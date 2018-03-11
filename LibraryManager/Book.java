package Library;

public class Book {
	private int number;
	private double price;
	private String name;
	public Book(int number,double price,String name) {
		super();
		this.number=number;
		this.price=price;
		this.name=name;
	}
	public Book(int number,double price) {
		super();
		this.number=number;
		this.price=price;
	}
	public Book() {
		super();
	}
	public String getName() {
		return name;
	}
	public void setName(String name) {
		this.name=name;
	}
	public int getNumber() {
		return number;
	}
	public void setNumber(int number) {
		this.number=number;
	}
	public double getPrice() {
		return price;
	}
	public void setPrice(double price) {
		this.price=price;
	}
}
