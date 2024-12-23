import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        Integer[] scores = new Integer[n];
        st = new StringTokenizer(bf.readLine());
        for (int i = 0; i < n; i++) {
            scores[i] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(scores, Collections.reverseOrder());

        System.out.println(scores[k - 1]);
    }
}