import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Integer> s = new Stack<>();
        Queue<Integer> q = new LinkedList<>();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            q.offer(Integer.parseInt(st.nextToken()));
        }

        int next = 1;
        s.push(q.poll());
        while (!q.isEmpty()) {
            if (s.isEmpty() || (!s.isEmpty() && s.peek() != next)) {
                s.push(q.poll());
            }

            if (!s.isEmpty() && s.peek() == next) {
                s.pop();
                next++;
            }
        }

        while (!s.isEmpty()) {
            if (s.peek() == next) {
                s.pop();
                next++;
            } else {
                break;
            }
        }

        System.out.println((next == n + 1) ? "Nice" : "Sad");
    }
}
