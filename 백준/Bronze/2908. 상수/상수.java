import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        String first = st.nextToken();
        String second = st.nextToken();

        StringBuilder sbFirst = new StringBuilder();
        StringBuilder sbSecond = new StringBuilder();

        for (int i = first.length() - 1; i >= 0; i--) {
            sbFirst.append(first.charAt(i));
        }
        for (int i = second.length() - 1; i >= 0; i--) {
            sbSecond.append(second.charAt(i));
        }

        int firstInt = Integer.parseInt(sbFirst.toString());
        int secondInt = Integer.parseInt(sbSecond.toString());

        System.out.println(Math.max(firstInt, secondInt));
    }
}
