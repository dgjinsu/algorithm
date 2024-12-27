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
        st = getSt();
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        Map<String, Integer> map = new HashMap<>();
        Map<Integer, String> map2 = new HashMap<>();
        for (int i = 0; i<n; i++) {
            String line = br.readLine();
            map.put(line, i + 1);
            map2.put(i + 1, line);
        }

        for (int i = 0; i < m; i++) {
            String command = br.readLine();
            try {
                int num = Integer.parseInt(command);
                sb.append(map2.get(num)).append("\n");
            } catch (Exception e) {
                sb.append(map.get(command)).append("\n");
            }
        }

        System.out.println(sb);
    }
}