import java.util.*;
class Solution3 {               //스택을 사용
    public int solution(String s)
    {
        char carr[] = s.toCharArray();
        Stack<Character> stack = new Stack<>();

        for(int i = 0;i < carr.length;i++) {
            char a = carr[i];
            if(stack.isEmpty()){
                stack.push(a);
            }
            else {
                if (stack.peek() == a) {
                    stack.pop();
                }
                else {
                    stack.push(a);
                }
            }
        }
        if(stack.isEmpty()) {
            return 1;

        }
        else {
            return 0;
        }
    }
}


public class level2_짝지어제거하기 {
    Solution3 solution3 = new Solution3();
}
