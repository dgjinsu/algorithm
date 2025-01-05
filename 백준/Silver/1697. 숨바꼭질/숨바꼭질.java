import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int[] g = new int[1000001];
    static int[] v = new int[1000001];
    static int[] dx = {1, -1, 2};
    static int k;
    static int n;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        st = getSt();
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        bfs(n);
    }

    private static void bfs(int n) {
        Queue<Integer> q = new LinkedList<>();
        q.add(n);
        while (!q.isEmpty()) {
            Integer x = q.poll();
            if (x == k) {
                System.out.println(v[x]);
                break;
            }
            for (int i = 0; i<3; i++) {
                int nx = x + dx[i];
                if (dx[i] == 2) {
                    nx = x * 2;
                }
                if (nx <= 100000 && nx >= 0 && v[nx] == 0) {
                    v[nx] = v[x] + 1;
                    q.add(nx);
                }
            }
        }
    }
}
