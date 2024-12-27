import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        int[] distance = new int[n - 1];
        int[] cost = new int[n];
        int minCost = Integer.MAX_VALUE;
        int result = 0;

        st = getSt();
        for (int i = 0; i < distance.length; i++) {
            distance[i] = Integer.parseInt(st.nextToken());
        }

        st = getSt();
        for (int i = 0; i < n; i++) {
            cost[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 0; i < n - 1; i++) {
            minCost = Math.min(minCost, cost[i]);
            result += minCost * distance[i];
        }

        System.out.println(result);
    }
}