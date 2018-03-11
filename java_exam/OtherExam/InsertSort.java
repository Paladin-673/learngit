package OtherExam;

public class InsertSort {

	public void insertSort(int[] a) {
		int i,j,insertNote;//要插入的数据
		for(i = 1;i < a.length;i++) {
			//从数组的第二个元素开始循环将数组中的元素插入
			insertNote = a[i];//设置数组中的第二个元素为第一次循环要插入的数据
			j = i - 1;
			while(j >= 0 && insertNote < a[j]) {
				a[j + 1] = a[j];//如果要插入的元素小于第j个元素，就将第j个元素向后移动
				j--;
			}
			a[j + 1] = insertNote;//直到要插入的元素不小于第j个元素，将insertNote插入到数组中
		}
		
		for(int x  = 0; x < a.length;x++)
			System.out.print(a[x]+",");
	}
	
	public static void main(String[] args) {
		InsertSort is = new InsertSort();
		int a[] = {38,65,97,76,13,27,89};
		is.insertSort(a);
	}
	
}
