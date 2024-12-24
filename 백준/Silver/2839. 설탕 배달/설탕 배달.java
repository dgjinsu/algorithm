import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        int maxThree = (int) n / 3;
        int maxFive = (int) n / 5;

        List<Integer> resultList = new ArrayList<>();
        for (int i = 0; i <= maxThree; i++) {
            for (int j = 0; j <= maxFive; j++) {
                if ((3 * i) + (5 * j) == n) {
                    resultList.add(i + j);
                }
            }
        }

        if (resultList.isEmpty()) {
            System.out.println(-1);
        } else {
            System.out.println(Collections.min(resultList));
        }
    }
}