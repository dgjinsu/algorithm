import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Set<String> s = new HashSet<>();
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            String name = st.nextToken();
            if (st.nextToken().equals("enter")) {
                s.add(name);
            } else {
                s.remove(name);
            }
        }
        String[] names = s.toArray(new String[0]);
        Arrays.sort(names, Collections.reverseOrder());
        Arrays.stream(names).forEach(name -> sb.append(name).append('\n'));
        System.out.println(sb);
    }
}
