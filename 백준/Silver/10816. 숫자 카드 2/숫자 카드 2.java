import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Map<Integer, Integer> map = new HashMap<>();
        int n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        for(int i = 0; i < n; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (map.containsKey(num)) {
                map.put(num, map.get(num) + 1);
            } else {
                map.put(num, 1);
            }
        }
        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            Integer tmp = map.get(Integer.parseInt(st.nextToken()));
            if (tmp == null) tmp = 0;
            sb.append(tmp).append(" ");
        }
        System.out.println(sb);
    }
}
