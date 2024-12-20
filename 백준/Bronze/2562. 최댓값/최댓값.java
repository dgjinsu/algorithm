import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[9];
        for (int i = 0; i < 9; i++) {
            arr[i] = Integer.parseInt(bf.readLine());
        }

        int max = Arrays.stream(arr).max().orElseThrow();
        System.out.println(max);

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == max) {
                System.out.println(i + 1);
                break;
            }
        }
    }
}
