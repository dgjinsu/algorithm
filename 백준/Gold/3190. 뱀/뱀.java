import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n; // 보드 크기
    static int k; // 사과 개수
    static int l; // 변환 정보 개수

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    enum Direction {
        UP(-1, 0), RIGHT(0, 1), DOWN(1, 0), LEFT(0, -1);

        private int dx;
        private int dy;

        Direction(int dx, int dy) {
            this.dx = dx;
            this.dy = dy;
        }

        public int dx() {
            return dx;
        }

        public int dy() {
            return dy;
        }

        public Direction getNextDirection(char directionCommand) {
            if (directionCommand == 'D') {
                return values()[(this.ordinal() + 1) % 4];
            } else if (directionCommand == 'L') {
                return values()[(this.ordinal() + 3) % 4];
            }
            return this;
        }
    }

    static class Coord {
        private int x;
        private int y;

        public Coord(int x, int y) {
            this.x = x;
            this.y = y;
        }

        @Override
        public boolean equals(Object obj) {
            if (this == obj) return true;
            if (!(obj instanceof Coord)) return false;
            Coord other = (Coord) obj;
            return this.x == other.x && this.y == other.y;
        }

        @Override
        public int hashCode() {
            return Objects.hash(x, y);
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }
    }

    static class Board {
        private Set<Coord> appleCoords;
        private int size;

        public Board(Set<Coord> appleCoords, int size) {
            this.appleCoords = appleCoords;
            this.size = size;
        }
    }

    static class Snake {
        private Coord headCoord = new Coord(1, 1);
        private Queue<Coord> body = new LinkedList<>();
        private Direction direction = Direction.RIGHT;
        private Board board;

        public Snake() {
            body.add(headCoord);
        }

        public void registerBoardInfo(Board board) {
            this.board = board;
        }

        public void turn(Direction direction) {
            this.direction = direction;
        }

        private boolean move() {
            int headX = headCoord.getX() + direction.dx();
            int headY = headCoord.getY() + direction.dy();

            this.headCoord = new Coord(headX, headY);
            body.add(headCoord);

            if (isCollisionWall() || isCollisionBody()) {
                return true;
            }

            moveTail();

            return false;
        }

        private boolean isCollisionWall() {
            return !(headCoord.getX() >= 1 &&
                headCoord.getY() >= 1 &&
                headCoord.getX() <= board.size &&
                headCoord.getY() <= board.size);
        }

        private boolean isCollisionBody() {
            List<Coord> bodyCoordList = new ArrayList<>(body);
            for (int i = 0; i < bodyCoordList.size() - 1; i++) {
                Coord c = bodyCoordList.get(i);
                if (headCoord.equals(c)) return true;
            }
            return false;
        }

        private void moveTail() {
            if (!board.appleCoords.contains(headCoord)) {
                body.poll();
            } else {
                board.appleCoords.remove(headCoord);
            }
        }
    }

    static class GameServer {
        private final Map<Integer, Character> commands;
        private int time = 0;
        private final Board board;
        private final Snake snake;

        public GameServer(Map<Integer, Character> commands, Set<Coord> appleCoords, int boardSize) {
            this.commands = commands;
            this.board = new Board(appleCoords, boardSize);
            this.snake = new Snake();
        }

        public void gameStart() {
            snake.registerBoardInfo(board);

            while (true) {
                time++;

                boolean isCollision = snake.move();

                if (isCollision) {
                    break;
                }

                if (commands.containsKey(time)) {
                    char directionCommand = commands.get(time);
                    snake.turn(snake.direction.getNextDirection(directionCommand));
                }
            }

            System.out.println(time);
        }
    }

    public static void main(String[] args) throws IOException {
        Set<Coord> appleCoord = new HashSet<>();
        Map<Integer, Character> commands = new HashMap<>();

        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        for (int i = 0; i < k; i++) {
            st = getSt();
            appleCoord.add(new Coord(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken())));
        }

        l = Integer.parseInt(br.readLine());

        for (int i = 0; i < l; i++) {
            st = getSt();
            commands.put(Integer.parseInt(st.nextToken()), st.nextToken().charAt(0));
        }

        new GameServer(commands, appleCoord, n).gameStart();
    }
}
