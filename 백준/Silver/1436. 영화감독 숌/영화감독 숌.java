import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int cnt = 0;
        for (int i = 0; ; i++) {
            String s = String.valueOf(i);
            if (s.contains("666")) {
                cnt++;
            }
            if (cnt == n) {
                System.out.println(s);
                return;
            }
        }
    }
}