import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            Stack<Character> s = new Stack<>();
            String line = br.readLine();
            if (line.length() == 1 && line.charAt(0) == '.') {
                break;
            }
            System.out.println(find(s, line) ? "yes" : "no");
        }
    }


    private static boolean find(Stack<Character> s, String line) {
        for (int i = 0; i < line.length(); i++) {
            char c = line.charAt(i);
            if (c == '(' || c == '[') {
                s.push(c);
            }
            if (c == ')') {
                if (s.isEmpty()) {
                    return false;
                }
                if (s.peek() != ('(')) {
                    return false;
                }
                s.pop();
            }
            if (c == ']') {
                if (s.isEmpty()) {
                    return false;
                }
                if (s.peek() != ('[')) {
                    return false;
                }
                s.pop();
            }
        }
        return s.isEmpty();
    }
}