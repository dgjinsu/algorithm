import java.io.*;
import java.util.*;

public class Main {

    static class Room {

        int start, end;

        public Room(int start, int end) {
            this.start = start;
            this.end = end;
        }
    }

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        Room[] rooms = new Room[n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            rooms[i] = new Room(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        Arrays.sort(rooms, (r1, r2) -> {
            if (r1.end == r2.end) {
                return r1.start - r2.start;
            }
            return r1.end - r2.end;
        });

        int availableTime = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (availableTime <= rooms[i].start) {
                availableTime = rooms[i].end;
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
