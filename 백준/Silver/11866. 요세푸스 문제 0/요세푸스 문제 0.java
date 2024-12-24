import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        LinkedList<Integer> q = new LinkedList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        for (int i = 1; i <= n; i++) {
            q.add(i);
        }

        List<Integer> results = new ArrayList<>();
        while (!q.isEmpty()) {
            for (int i = 0; i < k - 1; i++) {
                q.add(q.poll());
            }
            results.add(q.poll());
        }

        if (results.size() == 1) {
            System.out.println("<" + results.get(0) + ">");
            return;
        }

        for (int i = 0; i < results.size(); i++) {
            if (i == 0) {
                System.out.print("<" + results.get(i) + ", ");
            } else if (i == results.size() - 1) {
                System.out.println(results.get(i) + ">");
            } else {
                System.out.print(results.get(i) + ", ");
            }
        }
    }
}