import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Set<String> s1 = new HashSet<>();
        Set<String> s2 = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            s1.add(br.readLine());
        }
        for (int i = 0; i < m; i++) {
            s2.add(br.readLine());
        }
        String[] s1Array = s1.toArray(new String[0]);
        List<String> result = new ArrayList<>();
        for (String name : s1Array) {
            if (s2.contains(name)) {
                result.add(name);
            }
        }
        Collections.sort(result);
        System.out.println(result.size());
        result.forEach(System.out::println);
    }
}
