import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int result = 0;

        for (int i = 1; i <= n; i++) {
            int sum = 0;
            int tmp = i;
            while (tmp != 0) {
                sum += (tmp % 10);
                tmp = (int) tmp / 10;
            }
            sum += i;
            if (sum == n) {
                result = i;
                break;
            }
        }
        System.out.println(result);
    }
}