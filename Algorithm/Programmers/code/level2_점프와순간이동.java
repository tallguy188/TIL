import java.util.*;
class Solution2 {
    public int solution(int n) {
        int result = 0;
        int num = 0;
        while(n != 0) {

            if (n % 2 == 0) {
                n = n / 2;
            }

            else {
                n = n-1;
                result +=1;
            }
        }
        return result;
    }
}