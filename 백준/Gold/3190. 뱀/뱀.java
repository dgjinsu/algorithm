import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n; // 보드 크기
    static int k; // 사과 개수
    static int l; // 변환 정보 개수
    static int[][] board;
    static int direction = 1; // 위:0 오른쪽:1 아래:2 왼쪽:3
    static char commandDirection;
    static int time = 0;
    static int turnTime;
    static Queue<int[]> snake = new LinkedList<>();
    static Map<Integer, Character> commands = new HashMap<>();
    static int headX = 0;
    static int headY = 0;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        board = new int[n][n];
        snake.add(new int[]{0, 0});
        for (int i = 0; i < k; i++) {
            st = getSt();
            board[Integer.parseInt(st.nextToken()) - 1][Integer.parseInt(st.nextToken()) - 1] = -1;
        }
        l = Integer.parseInt(br.readLine());

        for (int i = 0; i < l; i++) {
            st = getSt();
            turnTime = Integer.parseInt(st.nextToken());
            commandDirection = st.nextToken().charAt(0);
            commands.put(turnTime, commandDirection);
        }

        while (true) {
            time++;

            // 전진
            go();

            // 헤드가 벽, 몸통에 박지 않았는지 확인
            if (isEndOfBoard()) {
                break;
            }
            if (isCrashBody()) {
                break;
            }

            // 사과 있는지 확인 후 꼬리 따라오기
            if (board[headX][headY] != -1) {
                snake.poll();
            } else {
                board[headX][headY] = 0;
            }

            // 명령 있는지 확인 후 방향 전환
            if (commands.containsKey(time)) {
                setDirection(commands.get(time));
            }
        }

        System.out.println(time);
    }


    private static boolean isCrashBody() {
        int tmp = snake.size();
        for (int i = 0; i < tmp - 1; i++) {
            int[] body = snake.poll();
            if (body[0] == headX && body[1] == headY) {
                return true;
            }
            snake.add(body);
        }
        snake.add(snake.poll());
        return false;
    }

    private static void go() {
        if (direction == 0) {
            headX--;
        } else if (direction == 1) {
            headY++;
        } else if (direction == 2) {
            headX++;
        } else if (direction == 3) {
            headY--;
        }

        snake.add(new int[]{headX, headY});
    }

    private static boolean isEndOfBoard() {
        return !(headX >= 0 && headY >= 0 && headX < n && headY < n);
    }

    private static void setDirection(char c) {
        if (c == 'D') {
            direction = (direction + 1) % 4;
        } else {
            direction = (direction + 4 - 1) % 4;
        }
    }
}