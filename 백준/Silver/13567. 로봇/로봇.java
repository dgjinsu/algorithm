import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        st = getSt();
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int x = 0;
        int y = 0;

        int direction = 1;
        // 북: 0
        // 동: 1
        // 남: 2
        // 서: 3

        for (int i = 0; i < n; i++) {
            st = getSt();
            String command = st.nextToken();
            int tmp = Integer.parseInt(st.nextToken());

            if (command.equals("MOVE")) {
                if (direction == 0) {
                    if (y + tmp > m) {
                        System.out.println(-1);
                        return;
                    } else {
                        y += tmp;
                    }
                } else if (direction == 1) {
                    if (x + tmp > m) {
                        System.out.println(-1);
                        return;
                    } else {
                        x += tmp;
                    }
                } else if (direction == 2) {
                    if (y - tmp < 0) {
                        System.out.println(-1);
                        return;
                    } else {
                        y -= tmp;
                    }
                } else if (direction == 3) {
                    if (x - tmp < 0) {
                        System.out.println(-1);
                        return;
                    } else {
                        x -= tmp;
                    }
                }
            } else if (command.equals("TURN")) {
                direction = setDirection(tmp, direction);
            }
        }
        System.out.println(x + " " + y);
    }

    private static int setDirection(int tmp, int direction) {
        if (tmp == 1) {
            direction = (direction + 1) % 4;
        } else if (tmp == 0) {
            direction = direction - 1;
            if (direction == -1) {
                direction = 3;
            }
        }
        return direction;
    }
}