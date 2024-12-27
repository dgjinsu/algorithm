import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    static int[][] g;
    static int[][] v;
    static int m;
    static int n;
    static int k;
    static int cnt;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        int t = Integer.parseInt(br.readLine());
        while (t-- > 0) {
            st = getSt();
            m = Integer.parseInt(st.nextToken());
            n = Integer.parseInt(st.nextToken());
            g = new int[m][n];
            v = new int[m][n];
            k = Integer.parseInt(st.nextToken());
            for (int i = 0; i < k; i++) {
                st = getSt();
                g[Integer.parseInt(st.nextToken())][Integer.parseInt(st.nextToken())] = 1;
            }

            cnt = 0;
            for (int i = 0; i < m; i++) {
                for (int j = 0; j < n; j++) {
                    if (g[i][j] == 1 && v[i][j] == 0) {
                        bfs(i, j);
                    }
                }
            }
            System.out.println(cnt);
        }
    }

    static void bfs(int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        v[i][j] = 1;
        q.add(new int[]{i, j});
        while (!q.isEmpty()) {
            int[] now = q.poll();
            for (int k = 0; k < 4; k++) {
                int nx = now[0] + dx[k];
                int ny = now[1] + dy[k];
                if (nx < m && nx >= 0 && ny < n && ny >= 0 && g[nx][ny] == 1 && v[nx][ny] == 0) {
                    v[nx][ny] = 1;
                    q.add(new int[]{nx, ny});
                }
            }
        }
        cnt++;
    }

}