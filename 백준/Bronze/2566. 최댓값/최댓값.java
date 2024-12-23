import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int[][] nums = new int[9][9];

        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());

            for (int j = 0; j < 9; j++) {
                nums[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int max = -1;
        int maxX = -1;
        int maxY = -1;
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (max < nums[i][j]) {
                    max = nums[i][j];
                    maxX = i;
                    maxY = j;
                }
            }
        }

        System.out.println(max);
        System.out.println((maxX + 1) + " " + (maxY + 1));

    }
}