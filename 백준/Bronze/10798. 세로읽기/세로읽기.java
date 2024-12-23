import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        char[][] arr = new char[5][15];
        for (int i = 0; i<5; i++) {
            for (int j = 0; j<15; j++) {
                arr[i][j] = '-';
            }
        }
        String line = "";
        for (int i = 0; i< 5; i++) {
            line = bf.readLine();

            for (int j = 0; j<line.length(); j++) {
                arr[i][j] = line.charAt(j);
            }
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                sb.append(arr[j][i]);
            }
        }
        System.out.println(sb.toString().replaceAll("-", ""));
    }
}