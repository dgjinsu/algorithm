import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        int[] persons = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            persons[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(persons);
        int finishTime = 0;
        int sum = 0;
        for (int i = 0; i < n; i++) {
            finishTime += persons[i];
            sum += finishTime;
        }
        System.out.println(sum);
    }
}
