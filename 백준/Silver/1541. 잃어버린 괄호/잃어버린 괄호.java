import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine(), "-");
        int[] partSums = new int[st.countTokens()];
        for (int i = 0; st.countTokens() != 0; i++) {
            StringTokenizer st2 = new StringTokenizer(st.nextToken(), "+");
            int[] tmp = new int[st2.countTokens()];

            for (int j = 0; st2.countTokens() != 0; j++) {
                tmp[j] = Integer.parseInt(st2.nextToken());
            }

            partSums[i] = Arrays.stream(tmp).sum();
        }

        int sum = Arrays.stream(partSums).sum();
        System.out.println(2 * partSums[0] - sum);
    }
}
