import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            Stack<Character> s = new Stack<>();
            String line = br.readLine();
            boolean flag = true;

            for (int j = 0; j < line.length(); j++) {
                char c = line.charAt(j);
                if (c == '(') {
                    s.push(c);
                } else if (c == ')' && !s.isEmpty()) {
                    s.pop();
                } else {
                    System.out.println("NO");
                    flag = false;
                    break;
                }
            }
            if (flag) {
                System.out.println((s.isEmpty()) ? "YES" : "NO");
            }
        }
    }
}