import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] pool;
    static boolean[][][] visit;
    static int n;
    static int m;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int result = 0;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        StringTokenizer st = getSt();
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visit = new boolean[n][m][10];

        pool = new int[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                pool[i][j] = line.charAt(j) - '0';
            }
        }

        fillWaterIntoPool();

        System.out.println(result);
    }

    private static void printPool() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(pool[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private static boolean fillWaterIntoPool() {
        boolean flag = true;
        for (int h = 1; h <= 9; h++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < m; j++) {
                    if (pool[i][j] == h && !visit[i][j][h]) {
                        visit[i][j][h] = true;
                        bfs(i, j, h);
                    }
                }
            }
        }

        return flag;
    }

    private static void bfs(int a, int b, int h) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{a, b});
        boolean isFlood = false;
        List<int[]> sameHeightCoord = new ArrayList<>();
        sameHeightCoord.add(new int[]{a, b});
        List<Integer> higherHeight = new ArrayList<>();

        // 둘러싸져 있는지 검사
        while (!q.isEmpty()) {
            int[] now = q.poll();
            int x = now[0];
            int y = now[1];
            // 테두리 체크
            if (x == 0 || y == 0 || x == n - 1 || y == m - 1) {
                isFlood = true;
            }
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    // 같은 높이라면 웅덩이
                    if (pool[nx][ny] == h && !visit[nx][ny][h]) {
                        q.add(new int[]{nx, ny});
                        visit[nx][ny][h] = true;
                        sameHeightCoord.add(new int[]{nx, ny});
                    }

                    // 낮다면 흘러넘침
                    if (pool[nx][ny] < h) {
                        isFlood = true;
                    }

                    if (pool[nx][ny] > h) {
                        higherHeight.add(pool[nx][ny]);
                    }
                }
            }
        }

        if (!isFlood) {
            Integer minHeight = higherHeight.stream().min(Integer::compare).get();
            result += sameHeightCoord.size() * (minHeight - h);
            for (int i = 0; i < sameHeightCoord.size(); i++) {
                pool[sameHeightCoord.get(i)[0]][sameHeightCoord.get(i)[1]] += (minHeight - h);

            }
        }
    }
}