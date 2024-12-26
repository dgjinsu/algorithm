import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        ArrayDeque<Integer> d = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());

        int a, b = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            a = Integer.parseInt(st.nextToken());
            if (st.hasMoreTokens()) {
                b = Integer.parseInt(st.nextToken());
            }
            if (a == 1) {
                d.addFirst(b);
            } else if (a == 2) {
                d.addLast(b);
            } else if (a == 3) {
                System.out.println(d.isEmpty() ? -1 : d.pollFirst());
            } else if (a == 4) {
                System.out.println(d.isEmpty() ? -1 : d.pollLast());
            } else if (a == 5) {
                System.out.println(d.size());
            } else if (a == 6) {
                System.out.println(d.isEmpty() ? 1 : 0);
            } else if (a == 7) {
                System.out.println(d.isEmpty() ? -1 : d.peekFirst());
            } else if (a==8) {
                System.out.println(d.isEmpty() ? -1 : d.peekLast());
            }
        }
    }
}