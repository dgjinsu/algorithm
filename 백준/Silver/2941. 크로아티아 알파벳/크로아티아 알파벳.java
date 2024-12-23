import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String sentence = bf.readLine();

        String[] chroatia = {"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="};
        for (int i = 0; i < chroatia.length; i++) {
            if (sentence.contains(chroatia[i])) {
                sentence = sentence.replaceAll(chroatia[i], "@");
            }
        }
        System.out.println(sentence.length());
    }
}