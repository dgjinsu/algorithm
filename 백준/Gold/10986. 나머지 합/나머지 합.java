import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static StringTokenizer input() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        long[] nums = new long[n + 1];
        long[] cnt = new long[m];
        long result = 0;

        st = input();
        for (int i = 1; i <= n; i++) {
            nums[i] = Long.parseLong(st.nextToken()) + nums[i - 1];
        }
        for (int i = 1; i <= n; i++) {
            nums[i] = nums[i] % m;
            cnt[(int) nums[i]]++;
        }

        for (int i = 0; i < m; i++) {
            result += comb(cnt[i]);
        }

        System.out.println(result + cnt[0]);
    }

    private static long comb(long n) {
        if (n < 2) {
            return 0;
        }
        return n * (n - 1) / 2;
    }
}