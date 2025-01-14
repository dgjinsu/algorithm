import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int[] nums = new int[5];
        for (int i = 0; i < 5; i++) {
            nums[i] = Integer.parseInt(bf.readLine());
        }

        Arrays.stream(nums).average().ifPresent(avg -> System.out.println((int) avg));
        Arrays.sort(nums);
        System.out.println(nums[(int) (nums.length / 2)]);
    }
}