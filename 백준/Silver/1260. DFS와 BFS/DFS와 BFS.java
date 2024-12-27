import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    static ArrayList<ArrayList<Integer>> g = new ArrayList<>();
    static int[] v;
    static int n;
    static int m;
    static int start;

    public static void main(String[] args) throws IOException {
        st = getSt();
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        start = Integer.parseInt(st.nextToken());
        v = new int[n + 1];

        for (int i = 0; i <= n; i++) {
            g.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = getSt();
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            g.get(a).add(b);
            g.get(b).add(a);
        }

        for (int i = 0; i <= n; i++) {
            Collections.sort(g.get(i));
        }

        dfs(start);
        sb.append('\n');
        v = new int[n + 1];
        bfs(start);

        System.out.println(sb);
    }

    static void bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        v[start]++;
        while (!q.isEmpty()) {
            int now = q.poll();
            sb.append(now).append(" ");
            for (int next : g.get(now)) {
                if (v[next] == 0) {
                    v[next]++;
                    q.add(next);
                }
            }
        }
    }

    static void dfs(int node) {
        v[node]++;
        sb.append(node).append(" ");
        for (int next : g.get(node)) {
            if (v[next] == 0) {
                v[next]++;
                dfs(next);
            }
        }
    }
}