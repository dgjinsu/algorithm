import java.io.*;
import java.util.*;

public class Main {

    static class Balloon {
        int num, idx;

        public Balloon(int num, int idx) {
            this.num = num;
            this.idx = idx;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        ArrayDeque<Balloon> d = new ArrayDeque<>();

        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            d.addLast(new Balloon(Integer.parseInt(st.nextToken()), i + 1));
        }

        while (d.size() > 1) {
            Balloon choice = d.pollFirst();
            sb.append(choice.idx).append(" ");
            if (choice.num > 0) {
                for (int i = 0; i < choice.num - 1; i++) {
                    d.addLast(d.pollFirst());
                }
            } else {
                for (int i = 0; i < Math.abs(choice.num); i++) {
                    d.addFirst(d.pollLast());
                }
            }
        } 

        System.out.println(sb.toString() + d.peekFirst().idx);
    }
}