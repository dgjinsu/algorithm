import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        int[] arr = new int[n];
        double[] scores = new double[n];
        StringTokenizer st = new StringTokenizer(bf.readLine());

        for (int i = 0; i<n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int maxScore = Arrays.stream(arr).max().orElseThrow();

        for (int i = 0; i<n; i++) {
            scores[i] = (double) arr[i] / maxScore * 100;
        }

        System.out.println(Arrays.stream(scores).average().orElseThrow());
    }
}
