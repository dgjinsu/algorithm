import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        String[] words = new String[n];

        for (int i = 0; i < n; i++) {
            words[i] = bf.readLine();
        }

        String[] newWords = new HashSet<>(Arrays.asList(words)).toArray(new String[0]);

        Arrays.sort(newWords, (w1, w2) -> {
            if (w1.length() == w2.length()) {
                return w1.compareTo(w2);
            }
            return w1.length() - w2.length();
        });

        Arrays.stream(newWords).forEach(System.out::println);
    }

}