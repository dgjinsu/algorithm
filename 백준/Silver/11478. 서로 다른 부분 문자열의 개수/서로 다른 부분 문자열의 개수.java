import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Set<String> s = new HashSet<>();

        String line = br.readLine();

        for (int i = 0; i < line.length(); i++) {
            for (int j = i + 1; j <= line.length(); j++) {
                s.add(line.substring(i, j));
            }
        }
        System.out.println(s.size());
    }
}
