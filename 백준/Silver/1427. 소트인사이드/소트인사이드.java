import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String line = bf.readLine();
        Integer[] arr = new Integer[line.length()];
        for (int i = 0; i < line.length(); i++) {
            arr[i] = line.charAt(i) - '0';
        }
        Arrays.sort(arr, Collections.reverseOrder());

        StringBuilder sb = new StringBuilder();
        for (int a : arr) {
            sb.append(a);
        }

        System.out.println(sb.toString());
    }
}