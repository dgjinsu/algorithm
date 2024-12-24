import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Character[][] chess = new Character[n][m];

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < line.length(); j++) {
                chess[i][j] = line.charAt(j);
            }
        }

        int cntMin = Integer.MAX_VALUE;
        for (int i = 0; i <= n - 8; i++) {
            for (int j = 0; j <= m - 8; j++) {
                int cnt = 0;
                int cnt2 = 0;
                char startColor = (chess[i][j] == 'B') ? 'B' : 'W';

                int tmp = find(i, j, chess, startColor, cnt, cnt2);
                if (tmp < cntMin) cntMin = tmp;
            }
        }

        System.out.println(cntMin);
    }

    private static int find(int i, int j, Character[][] chess, char startColor, int cnt, int cnt2) {
        for (int x = i; x < i + 8; x++) {
            for (int y = j; y < j + 8; y++) {
                if ((x - i) % 2 == 0) {
                    if ((y - j) % 2 == 0) {
                        if (chess[x][y] != startColor) cnt++;
                        else cnt2++;
                    } else {
                        if (chess[x][y] == startColor) cnt++;
                        else cnt2++;
                    }
                } else {
                    if ((y - j) % 2 == 0) {
                        if (chess[x][y] == startColor) cnt++;
                        else cnt2++;
                    } else {
                        if (chess[x][y] != startColor) cnt++;
                        else cnt2++;
                    }
                }
            }
        }
        int tmp = Math.min(cnt, cnt2);
        return tmp;
    }
}