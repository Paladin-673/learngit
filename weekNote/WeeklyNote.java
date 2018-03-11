package note;
/*
 * 作者：李月
 * 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 */


import java.util.List;
import java.util.ArrayList;

public class WeeklyNote {

	public static void main(String args[]) {
		//List<String> strList = new ArrayList<String>();
		for (int i = 0; i < 50; i++) {
			String centos = getWorkWordsList();
			System.out.println(centos);
			//strList.add(centos);
		}
		//int suijishu = (int) (0 + Math.random() * (49 - 0 + 1));
	}

	public void WeeklyNote() {

	}

	//自定义的语句片段，用来拼接，可自行增加
	public static final String logs[] = { "修正目前已知BUG", "更改后端错误代码", "增加新的后台与前台功能", "对所写代码进行一定量的自测", "修改前端代码", "修改数据库文档", "整理数据库SQL文件", "整理项目文档", "整合已修改功能以及部分代码", "修正自测未发现BUG", "与测试进行深度联调", "对未备份数据库、代码以及项目文件进行备份", "调整开发环境" };

	//public static List<String> workWordsList = new ArrayList<String>();

	// 最大数
	public static final int MAX_MUN = logs.length - 1;
	// 最小数
	public static final int MIN_MUN = 0;
	// 最大拼接条数
	public static final int TIME_MAX = 6;
	// 最小拼接条数
	public static final int TIME_MIN = 4;

	// int allTimes = (int)(TIME_MIN+Math.random()*(TIME_MAX-TIME_MIN+1));
	// 循环拼接的次数 4——6条为佳

	/*
	 * 获取当前随机生成的工作日志，并输出
	 */
	public static String getWorkWordsList() {
		String cents = "今天";
		// allTimes指的是循环拼接的次数
		int allTimes = (int) (TIME_MIN + Math.random() * (TIME_MAX - TIME_MIN + 1));
		int suijishuInt[] = new int[MAX_MUN + 1];
		for (int i = 0; i < allTimes; i++) {
			boolean readyForCont = false;
			int times = (int) (MIN_MUN + Math.random() * (MAX_MUN-MIN_MUN + 1));
				for (int j = 0; j < suijishuInt.length; j++) {
					if (times == suijishuInt[j]) {
						readyForCont = true;
						break;
					}
				}
			if (readyForCont) {
				i--;
				continue;
			}
			cents = cents + logs[times];
			if (i != allTimes - 1) {
				cents = cents + "，";
				suijishuInt[i] = times;
			} else {
				cents = cents + "。";
			}
		}
		return cents;
	}

	/*
	 * public void setWorkWordsList(){ for(int i=0 ; i<logs.length ; i++){ workWordsList.add(logs[i]); } }
	 */
}
