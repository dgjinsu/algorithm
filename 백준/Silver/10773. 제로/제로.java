import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Stack<Integer> s = new Stack<>();

        int n = Integer.parseInt(br.readLine());

        for(int i = 0 ; i < n ; i++) {
            int input = Integer.parseInt(br.readLine());
            if (input == 0) {
                s.pop();
            } else {
                s.push(input);
            }
        }
        int sum = 0;
        for (Integer x : s) {
            sum += x;
        }
        System.out.println(sum);
    }
}