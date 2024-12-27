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
    static int n;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static List<Integer> results = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        g = new int[n][n];
        v = new int[n][n];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                g[i][j] = line.charAt(j) - '0';
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (g[i][j] == 1 && v[i][j] == 0) {
                    bfs(i, j);
                }
            }
        }

        Collections.sort(results);
        System.out.println(results.size());
        results.forEach(System.out::println);
    }

    static void bfs(int i, int j) {
        int cnt = 1;
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{i, j});
        v[i][j] = 1;
        while (!q.isEmpty()) {
            int[] now = q.poll();
            for (int k = 0; k < 4; k++) {
                int nextI = now[0] + dx[k];
                int nextJ = now[1] + dy[k];
                if (nextI < n && nextI >= 0 && nextJ < n && nextJ >= 0
                    && g[nextI][nextJ] == 1 & v[nextI][nextJ] == 0) {
                    v[nextI][nextJ] = 1;
                    cnt++;
                    q.add(new int[]{nextI, nextJ});
                }
            }
        }
        results.add(cnt);
    }
}