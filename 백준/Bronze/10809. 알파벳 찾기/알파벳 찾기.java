import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        String word = bf.readLine();

        for(char i = 'a'; i <= 'z'; i++) {
            int result = word.indexOf(i);
            System.out.print(result + " ");
        }
    }
}