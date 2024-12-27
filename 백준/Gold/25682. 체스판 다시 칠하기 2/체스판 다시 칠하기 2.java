import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        st = getSt();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        char[][] chess = new char[n][m];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                chess[i][j] = line.charAt(j);
            }
        }
        int[][] sum = new int[n + 1][m + 1];
        int[][] sum2 = new int[n + 1][m + 1];
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++) {
                char now = chess[i - 1][j - 1];
                int tmp = 0;
                int tmp2 = 0;
                if (((i + j) % 2 == 0 && now == 'W') || ((i + j) % 2 == 1 && now == 'B')) {
                    tmp = 1;
                }
                if (((i + j) % 2 == 1 && now == 'W') || ((i + j) % 2 == 0 && now == 'B')) {
                    tmp2 = 1;
                }
                sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + tmp;
                sum2[i][j] = sum2[i - 1][j] + sum2[i][j - 1] - sum2[i - 1][j - 1] + tmp2;
            }
        }

        List<Integer> results = new ArrayList<>();

        int x1, y1, x2, y2;
        for (int i = 1; i <= n - k + 1; i++) {
            for (int j = 1; j <= m - k + 1; j++) {
                x1 = i;
                y1 = j;
                x2 = i + k - 1;
                y2 = j + k - 1;
                int result = sum[x2][y2] - sum[x2][y1 - 1] - sum[x1 - 1][y2] + sum[x1 - 1][y1 - 1];
                int result2 = sum2[x2][y2] - sum2[x2][y1 - 1] - sum2[x1 - 1][y2] + sum2[x1 - 1][y1 - 1];
                results.add(Math.min(result, result2));
            }
        }

        System.out.println(results.stream().min(Integer::compareTo).get());
    }
}