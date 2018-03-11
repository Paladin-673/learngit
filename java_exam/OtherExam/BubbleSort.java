package OtherExam;

public class BubbleSort {

	public void bubbleSortbig(int[] a) {
		int temp = 0;
		for(int i=0;i<a.length-1;i++) {
			for(int j=0;j<a.length-1-i;j++) {
				if(a[j]>a[j+1]) {
					temp = a[j];
					a[j] = a[j+1];
					a[j+1] = temp;
				}
			}
		}
		for(int i=0;i<a.length;i++)
			System.out.print(a[i]+",");
		
	}
	
	public void bubbleSortsmall(int[] a) {
		int temp = 0;
		for(int i=0;i<a.length-1;i++) {
			for(int j=a.length-1;j>i;j--) {
				if(a[j]<a[j-1]) {
					temp = a[j];
					a[j] = a[j-1];
					a[j-1] = temp;
				}
			}
		}
		for(int i=0;i<a.length;i++)
			System.out.print(a[i]+",");
	}
	
	public static void main(String[] args) {
		int a[] = {38,65,97,76,13,27,89};
		BubbleSort bs = new BubbleSort();
		bs.bubbleSortbig(a);
		System.out.println("");
		int b[] = {38,65,97,76,13,27,89};
		bs.bubbleSortsmall(b);
	}
	
}
