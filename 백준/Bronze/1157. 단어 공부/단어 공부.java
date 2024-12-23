import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String sentence = bf.readLine();
        int[] alphabet = new int[26];
        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            if (c >= 'a') {
                c -= 32;
            }
            alphabet[c - 'A']++;
        }
        int max_alpha = Arrays.stream(alphabet).max().orElseThrow();
        int result = 'a';
        int max_alpha_cnt = 0;
        for (int i = 0; i < alphabet.length; i++) {
            if (alphabet[i] == max_alpha) {
                result = (char) i;
                max_alpha_cnt++;
            }
        }
        if (max_alpha_cnt > 1) {
            System.out.println('?');
            return;
        }

        System.out.println((char) (result + 65));
    }
}