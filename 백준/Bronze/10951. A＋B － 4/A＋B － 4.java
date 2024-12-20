import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int a, b;
        String tmp;
        while (true) {
            tmp = bf.readLine();
            if (tmp == null) break;
            StringTokenizer st = new StringTokenizer(tmp);
            if (!st.hasMoreTokens()) break;

            a = Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            System.out.println(a + b);
        }
    }
}
