import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static final int CHESS_BOARD_SIZE = 6;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    static class Player {

        private Knight knight;
        private List<String> visitSequence;
        private Set<String> visitRecord;

        public Player(List<String> visitSequence) {
            this.visitSequence = visitSequence;
            this.knight = new Knight(
                visitSequence.get(0).charAt(0) - 'A' + 1,
                visitSequence.get(0).charAt(1) - '0'
            );
            this.visitRecord = new HashSet<>();
            visitRecord.add(visitSequence.get(0));
        }

        // 이동 명령 실행
        public void executeVisitSequence() {
            boolean isValid = true;

            try {
                for (int i = 1; i < visitSequence.size(); i++) {
                    String visitCoordinate = visitSequence.get(i);

                    // 방문 기록 검사
                    isVisitedCoordinate(visitCoordinate);

                    // 이동
                    int x = visitCoordinate.charAt(0) - 'A' + 1;
                    int y = visitCoordinate.charAt(1) - '0';
                    knight.move(x, y);
                    
                    // 방문 기록 업데이트
                    updateVisitRecord(visitCoordinate);
                }

                // 원점 돌아오기
                String firstVisit = visitSequence.get(0);
                int firstX = firstVisit.charAt(0) - 'A' + 1;
                int firstY = firstVisit.charAt(1) - '0';
                knight.move(firstX, firstY);
            } catch (IllegalArgumentException e) {
                System.out.println("Invalid");
                isValid = false;
            }

            if (isValid) {
                System.out.println("Valid");
            }
        }

        private void isVisitedCoordinate(String visitCoordinate) {
            if (visitRecord.contains(visitCoordinate)) {
                throw new IllegalArgumentException("already visited");
            }
        }

        private void updateVisitRecord(String visitCoordinate) {
            this.visitRecord.add(visitCoordinate);
        }
    }

    static class Knight {

        private int prevVisitX;
        private int prevVisitY;
        private int currentVisitX;
        private int currentVisitY;

        public Knight(int currentVisitX, int currentVisitY) {
            this.currentVisitX = currentVisitX;
            this.currentVisitY = currentVisitY;
        }

        public void move(int x, int y) {
            this.prevVisitX = this.currentVisitX;
            this.prevVisitY = this.currentVisitY;
            this.currentVisitX = x;
            this.currentVisitY = y;

            validateKnightMove(
                this.prevVisitX,
                this.prevVisitY,
                this.currentVisitX,
                this.currentVisitY
            );
        }

        private void validateKnightMove(int x1, int y1, int x2, int y2) {
            if (!((Math.abs(x1 - x2) == 2 && Math.abs(y1 - y2) == 1) ||
                (Math.abs(x1 - x2) == 1 && Math.abs(y1 - y2) == 2))) {
                throw new IllegalArgumentException("Invalid knight move");
            }
        }
    }

    public static void main(String[] args) throws IOException {
        List<String> tmpSequence = new ArrayList<>();
        int chessBoardSize = CHESS_BOARD_SIZE * CHESS_BOARD_SIZE;

        while (chessBoardSize-- > 0) {
            tmpSequence.add(br.readLine());
        }

        Player player = new Player(tmpSequence);

        player.executeVisitSequence();
    }
}