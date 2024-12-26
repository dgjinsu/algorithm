import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] temperatures = new int[n + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            temperatures[i] = Integer.parseInt(st.nextToken()) + temperatures[i - 1];
        }

        List<Integer> results = new ArrayList<>();

        for (int i = k; i <= n; i++) {
            results.add(temperatures[i] - temperatures[i - k]);
        }

        System.out.println(results.stream().max(Integer::compareTo).get());
    }
}