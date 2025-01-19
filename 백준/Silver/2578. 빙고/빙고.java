import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int[] calledCntAtEachLine = new int[12];
    static int bingoCnt = 0;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    public static class Coordinate {

        private final int x;
        private final int y;

        public Coordinate(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        int callCnt = 1;

        Map<Integer, Coordinate> numberToCoordMap = new HashMap<>();

        for (int x = 0; x < 5; x++) {
            st = getSt();
            for (int y = 0; y < 5; y++) {
                numberToCoordMap.put(Integer.parseInt(st.nextToken()), new Coordinate(x, y));
            }
        }

        while (callCnt / 5 < 5) {
            st = getSt();
            for (int idx = 0; idx < 5; idx++) {
                int calledNumber = Integer.parseInt(st.nextToken());

                Coordinate calledNumberCoordinate = numberToCoordMap.get(calledNumber);
                int calledNumberX = calledNumberCoordinate.x;
                int calledNumberY = calledNumberCoordinate.y;

                processCalledNumber(calledNumberX, calledNumberY);

                checkBingo(calledNumberX, calledNumberY);

                if (bingoCnt >= 3) {
                    System.out.println(callCnt);
                    return;
                }

                callCnt++;
            }
        }
    }

    private static void checkBingo(int calledNumberX, int calledNumberY) {
        if (calledCntAtEachLine[calledNumberX] == 5) {
            bingoCnt++;
        }

        if (calledCntAtEachLine[calledNumberY + 5] == 5) {
            bingoCnt++;
        }

        if (calledNumberX == calledNumberY) {
            if (calledCntAtEachLine[10] == 5) {
                bingoCnt++;
            }
        }
        if (calledNumberX + calledNumberY == 4) {
            if (calledCntAtEachLine[11] == 5) {
                bingoCnt++;
            }
        }
    }

    private static void processCalledNumber(int calledNumberX, int calledNumberY) {
        calledCntAtEachLine[calledNumberX]++;
        calledCntAtEachLine[calledNumberY + 5]++;

        if (calledNumberX == calledNumberY) {
            calledCntAtEachLine[10]++;
        }
        if (calledNumberX + calledNumberY == 4) {
            calledCntAtEachLine[11]++;
        }
    }
}