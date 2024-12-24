import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        LinkedList<Integer> q = new LinkedList<>();
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            Integer b = null;
            if (st.hasMoreTokens()) {
                b = Integer.parseInt(st.nextToken());
            }

            if (a.equals("push")) {
                q.offer(b);
            } else if (a.equals("pop")) {
                Integer pollNum = q.poll();
                sb.append((pollNum == null) ? "-1" : pollNum).append("\n");
            } else if (a.equals("size")) {
                sb.append(q.size()).append("\n");
            } else if (a.equals("empty")) {
                sb.append(q.isEmpty() ? "1" : "0").append("\n");
            } else if (a.equals("front")) {
                sb.append(q.isEmpty() ? "-1" : q.peek()).append("\n");
            } else if (a.equals("back")) {
                sb.append(q.isEmpty() ? "-1" : q.peekLast()).append("\n");
            }
        }

        System.out.print(sb);
    }
}