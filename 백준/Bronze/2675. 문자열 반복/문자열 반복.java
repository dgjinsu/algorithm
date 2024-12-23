import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(bf.readLine());

        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            int repeat = Integer.parseInt(st.nextToken());
            String sentence = st.nextToken();
            repeatSentence(repeat, sentence);
        }
    }

    private static void repeatSentence(int repeat, String sentence) {
        for (int i = 0; i < sentence.length(); i++) {
            char c = sentence.charAt(i);
            for (int j = 0; j < repeat; j++) {
                System.out.print(c);
            }
        }
        System.out.println();
    }
}