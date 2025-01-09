import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static Bucket[] buckets;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static class Bucket {

        private int ballNumber;

        public Bucket(int ballNumber) {
            this.ballNumber = ballNumber;
        }

        public void exchangeBallNumber(Bucket targetBucket) {
            int tmp = ballNumber;
            ballNumber = targetBucket.ballNumber;
            targetBucket.ballNumber = tmp;
        }

        @Override
        public String toString() {
            return String.valueOf(ballNumber);
        }
    }

    public static void main(String[] args) throws IOException {
        st = getSt();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        buckets = new Bucket[n + 1];

        for (int i = 1; i <= n; i++) {
            buckets[i] = new Bucket(i);
        }

        while (m-- > 0) {
            st = getSt();

            Bucket sourceBucket = buckets[Integer.parseInt(st.nextToken())];
            Bucket targeBucket = buckets[Integer.parseInt(st.nextToken())];

            sourceBucket.exchangeBallNumber(targeBucket);
        }

        Arrays.stream(buckets)
                .skip(1)
                .forEach(bucket -> sb.append(bucket.toString()).append(" "));

        System.out.println(sb);
    }
}