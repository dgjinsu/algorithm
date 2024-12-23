import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        HashMap<String, Float> gradeMap = new HashMap<>();
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        createGradeMap(gradeMap);
        float sum = 0F;
        float totalA = 0F;
        for (int i = 0; i < 20; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            st.nextToken();
            Float a = Float.parseFloat(st.nextToken());
            String grade = st.nextToken();
            if (grade.equals("P")) continue;
            totalA += a;
            sum += gradeMap.get(grade) * a;
        }

        System.out.println(sum / totalA);
    }

    private static void createGradeMap(HashMap<String, Float> gradeMap) {
        gradeMap.put("A+", 4.5F);
        gradeMap.put("A0", 4.0F);
        gradeMap.put("B+", 3.5F);
        gradeMap.put("B0", 3.0F);
        gradeMap.put("C+", 2.5F);
        gradeMap.put("C0", 2.0F);
        gradeMap.put("D+", 1.5F);
        gradeMap.put("D0", 1.0F);
        gradeMap.put("F", 0.0F);
        gradeMap.put("P", 0.0F);
    }
}