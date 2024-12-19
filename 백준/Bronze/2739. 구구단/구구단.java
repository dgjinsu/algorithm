import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        String n = new BufferedReader(new InputStreamReader(System.in)).readLine();

        for (int i = 1; i < 10; i++) {
            System.out.println(n + " * " + i + " = " + Integer.parseInt(n) * i);
        }
    }
}
