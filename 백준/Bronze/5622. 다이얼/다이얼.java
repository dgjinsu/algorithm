import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Character, Integer> matchNum = new HashMap<Character, Integer>();
        matchNum.put('A', 2);
        matchNum.put('B', 2);
        matchNum.put('C', 2);
        matchNum.put('D', 3);
        matchNum.put('E', 3);
        matchNum.put('F', 3);
        matchNum.put('G', 4);
        matchNum.put('H', 4);
        matchNum.put('I', 4);
        matchNum.put('J', 5);
        matchNum.put('K', 5);
        matchNum.put('L', 5);
        matchNum.put('M', 6);
        matchNum.put('N', 6);
        matchNum.put('O', 6);
        matchNum.put('P', 7);
        matchNum.put('Q', 7);
        matchNum.put('R', 7);
        matchNum.put('S', 7);
        matchNum.put('T', 8);
        matchNum.put('U', 8);
        matchNum.put('V', 8);
        matchNum.put('W', 9);
        matchNum.put('X', 9);
        matchNum.put('Y', 9);
        matchNum.put('Z', 9);

        String s = bf.readLine();

        int result = 0;
        for (int i = 0; i<s.length(); i++) {
            result += matchNum.get(s.charAt(i)) + 1;
        }
        System.out.println(result);
    }
}
