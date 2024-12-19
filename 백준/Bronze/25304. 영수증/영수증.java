import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int totalPrice = Integer.parseInt(bf.readLine());

        int n = Integer.parseInt(bf.readLine());
        int sum = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            sum += Integer.parseInt(st.nextToken()) * Integer.parseInt(st.nextToken());
        }
        String answer = "";
        answer = (totalPrice == sum) ? "Yes" : "No";
        System.out.println(answer);
    }
}
