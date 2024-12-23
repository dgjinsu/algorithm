import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;

public class Main {

    public static class Point {

        int x;
        int y;

        public Point(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());

        Point[] points = new Point[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            points[i] = new Point(
                Integer.parseInt(st.nextToken()),
                Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(points, new Comparator<Point>() {
            @Override
            public int compare(Point o1, Point o2) {
                if (o1.x == o2.x) {
                    return o1.y - o2.y;
                }
                return o1.x - o2.x;
            }
        });

        for (int i = 0; i < n; i++) {
            System.out.println(points[i].x + " " + points[i].y);
        }
    }
}