import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            HashSet<Character> blackList = new HashSet<>();
            boolean flag = true;
            String sentence = bf.readLine();
            char prevCharacter = sentence.charAt(0);
            for (int j = 1; j < sentence.length(); j++) {
                char nowCharacter = sentence.charAt(j);

                if (blackList.contains(nowCharacter)) {
                    flag = false;
                }

                if (nowCharacter != prevCharacter) {
                    blackList.add(prevCharacter);
                }
                prevCharacter = nowCharacter;
            }
            if (flag) cnt++;
        }

        System.out.println(cnt);

    }
}