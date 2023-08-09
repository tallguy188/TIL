import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2]; // 배열 선언 및 초기화
        List<String> list = new ArrayList<String>();
        boolean flag = true;

        for (int i = 0; i < words.length; i++) {
            if (list.contains(words[i])) {
                answer[0] = (i % n) + 1; // 걸린사람의 번호
                answer[1] = (i / n) + 1; // 걸린사람의 차례
                flag = false;
                break;
            }

            list.add(words[i]);

            //이전 끝단어와 현재 첫단어가 다른 경우
            if (i > 0 && words[i - 1].charAt(words[i - 1].length() - 1) != words[i].charAt(0)) {

                answer[0] = (i % n) + 1;
                answer[1] = (i / n) + 1;
                flag = false;
                break;
            }
        }
        if (flag) return new int[]{0, 0};
        return answer;

    }
}

public class level2_끝말잇기 {
    public static void main(String[] args) {
        Solution solution = new Solution();
    }
}
