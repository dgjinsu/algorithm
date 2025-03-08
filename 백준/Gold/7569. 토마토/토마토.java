import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int[] dx = {-1, 1, 0, 0, 0, 0};
    static int[] dy = {0, 0, -1, 1, 0, 0};
    static int[] dz = {0, 0, 0, 0, -1, 1};
    static int width;
    static int depth;
    static int height;

    static StringTokenizer getSt() throws IOException {
        return new StringTokenizer(br.readLine());
    }

    static class Coord {
        int x;
        int y;
        int z;

        public Coord(int x, int y, int z) {
            this.x = x;
            this.y = y;
            this.z = z;
        }
    }

    public static void main(String[] args) throws IOException {
        Queue<Coord> ripeTomatoCoord = new LinkedList<>();

        st = getSt();
        width = Integer.parseInt(st.nextToken());
        depth = Integer.parseInt(st.nextToken());
        height = Integer.parseInt(st.nextToken());

        int [][][] boxes = new int[width][depth][height];
        int [][][] ripedIndex = new int[width][depth][height];

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < depth; j++) {
                st = getSt();
                for (int k = 0; k < width; k++) {
                    boxes[k][j][i] = Integer.parseInt(st.nextToken());
                    if (boxes[k][j][i] == 1) {
                        ripeTomatoCoord.add(new Coord(k, j, i));
                        ripedIndex[k][j][i] = 1;
                    }
                    if (boxes[k][j][i] == -1) {
                        ripedIndex[k][j][i] = -1;
                    }
                }
            }
        }

        if (checkAllTomatoRiped(boxes)) {
            System.out.println(0);
            return;
        }

        while(!ripeTomatoCoord.isEmpty()) {
            Coord coord = ripeTomatoCoord.poll();

            for (int i = 0; i < 6; i++) {
                int nextX = coord.x + dx[i];
                int nextY = coord.y + dy[i];
                int nextZ = coord.z + dz[i];

                if (nextX >= 0 && nextY >= 0 && nextZ >= 0 && nextX < width && nextY < depth && nextZ < height) {
                    if (boxes[nextX][nextY][nextZ] == 0 && ripedIndex[nextX][nextY][nextZ] == 0) {
                        ripeTomatoCoord.add(new Coord(nextX, nextY, nextZ));
                        ripedIndex[nextX][nextY][nextZ] = ripedIndex[coord.x][coord.y][coord.z] + 1;
                    }
                }
            }

//            for (int i = 0; i < height; i++) {
//                for (int j = 0; j < depth; j++) {
//                    for (int k = 0; k < width; k++) {
//                        System.out.print(ripedIndex[k][j][i] + " ");
//                    }
//                    System.out.println();
//                }
//            }
//            System.out.println();
        }

        for (int i = 0; i < height; i++) {
            for (int j = 0; j < depth; j++) {
                for (int k = 0; k < width; k++) {
                    if (ripedIndex[k][j][i] == 0) {
                        System.out.println(-1);
                        return;
                    }
                }
            }
        }

        System.out.println(findMaxValue(ripedIndex) - 1);
    }

    private static boolean checkAllTomatoRiped(int[][][] boxes) {
        boolean flag = true;
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < depth; j++) {
                for (int k = 0; k < width; k++) {
                    if (boxes[k][j][i] == 0) {
                        flag = false;
                    }
                }
            }
        }
        return flag;
    }

    public static int findMaxValue(int[][][] ripedIndex) {
        int maxValue = Integer.MIN_VALUE;

        for (int i = 0; i < ripedIndex.length; i++) { // width
            for (int j = 0; j < ripedIndex[i].length; j++) { // depth
                for (int k = 0; k < ripedIndex[i][j].length; k++) { // height
                    if (ripedIndex[i][j][k] > maxValue) {
                        maxValue = ripedIndex[i][j][k];
                    }
                }
            }
        }
        return maxValue;
    }
}