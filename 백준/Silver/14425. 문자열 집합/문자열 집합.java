import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        HashSet<String> s = new HashSet<>();
        for (int i = 0; i < n; i++) {
            s.add(br.readLine());
        }
        int cnt = 0;
        for (int i = 0; i < m; i++) {
            if (s.contains(br.readLine())) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
