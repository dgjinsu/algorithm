import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int m;
    static int targetNum;
    static int[] num;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        num = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            num[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(num);

        m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            targetNum = Integer.parseInt(st.nextToken());

            if (findNum()) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }

    }

    private static boolean findNum() {
        int start = 0, end = n - 1;

        while (start <= end) {
            int mid = (start + end) / 2;

            if (num[mid] == targetNum) {
                return true;
            } else if (num[mid] > targetNum) {
                end = mid - 1;
            } else if (num[mid] < targetNum) {
                start = mid + 1;
            }
        }
        return false;
    }
}