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
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        st = getSt();
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        g = new int[n][m];
        v = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                g[i][j] = line.charAt(j) - '0';
            }
        }

        bfs();
    }

    static void bfs() {
        Queue<int[]> q = new LinkedList<>();
        v[0][0] = 1;
        q.add(new int[]{0, 0});
        while (!q.isEmpty()) {
            int[] now = q.poll();
            if (now[0] == n - 1 && now[1] == m - 1) {
                System.out.println(v[now[0]][now[1]]);
            }
            for (int i = 0; i<4; i++) {
                int nx = now[0] + dx[i];
                int ny = now[1] + dy[i];
                if (nx < n && nx >= 0 && ny < m && ny >= 0 && g[nx][ny] == 1 && v[nx][ny] == 0) {
                    v[nx][ny] = v[now[0]][now[1]] + 1;
                    q.add(new int[]{nx, ny});
                }
            }
        }
    }
}