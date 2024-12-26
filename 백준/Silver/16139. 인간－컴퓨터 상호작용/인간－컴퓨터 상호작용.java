import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int[][] arr;
    public static void main(String[] args) throws IOException {
        String line = br.readLine();
        arr = new int[line.length() + 1][26];

        for (int i = 1; i <= line.length(); i++) {
            copyBefore(i);
            char alphabet = line.charAt(i - 1);
            int tmp = alphabet - 'a';
            arr[i][tmp]++;
        }

        int q = Integer.parseInt(br.readLine());

        for (int i = 0; i < q; i++) {
            st = new StringTokenizer(br.readLine());
            char alphabet = st.nextToken().charAt(0);
            int start  = Integer.parseInt(st.nextToken());
            int end  = Integer.parseInt(st.nextToken());
            sb.append(arr[end + 1][alphabet - 'a'] - arr[start][alphabet - 'a']).append('\n');
        }

        System.out.println(sb);
    }


    private static void copyBefore(int now) {
        for (int i = 0; i<26; i++) {
            arr[now][i] = arr[now-1][i];
        }
    }
}