import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int k, n;
    static int[] lan;
    static List<Long> results = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        // 길이 x일 때 랜선 개수 y를 구함
        // y가 필요 개수보다 큰 경우 result[] 에 저장
        // result 최대값
        StringTokenizer st = new StringTokenizer(br.readLine());
        k = Integer.parseInt(st.nextToken());
        n = Integer.parseInt(st.nextToken());

        lan = new int[k];
        for (int i = 0; i < k; i++) {
            lan[i] = Integer.parseInt(br.readLine());
        }

        long left = 0;
        long right = Integer.MAX_VALUE;

        while (left <= right) {
            long mid = (left + right) / 2;
            int lanCnt = getLanCnt(mid);
            if (lanCnt > n) {
                left = mid + 1;
                results.add(mid);
            } else if (lanCnt < n) {
                right = mid - 1;
            } else if (lanCnt == n) {
                left = mid + 1;
                results.add(mid);
            }
        }
        System.out.println(results.stream().max(Long::compareTo).get());
    }

    private static int getLanCnt(Long mid) {
        int tmp = 0;
        for (int i = 0; i < k; i++) {
            tmp += lan[i] / mid;
        }
        return tmp;
    }
}