import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Integer> s = new Stack<>();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            Integer b = null;
            if (st.hasMoreTokens()) {
                b = Integer.parseInt(st.nextToken());
            }
            if (a == 1) {
                s.push(b);
            }
            if (a == 2) {
                System.out.println((s.isEmpty()) ? "-1" : s.pop());
            }
            if (a == 3) {
                System.out.println(s.size());
            }
            if (a == 4) {
                System.out.println((s.isEmpty()) ? "1" : "0");
            }
            if (a == 5) {
                System.out.println((s.isEmpty()) ? "-1" : s.peek());
            }
        }
    }
}