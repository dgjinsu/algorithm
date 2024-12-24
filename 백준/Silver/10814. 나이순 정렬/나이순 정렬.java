import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class Main {

    public static class Person {
        int age;
        String name;

        public Person (int age, String name) {
            this.age = age;
            this.name = name;
        }

        @Override
        public String toString () {
            return this.age + " " + this.name;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(bf.readLine());

        Person[] persons = new Person[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(bf.readLine());
            persons[i] = new Person(Integer.parseInt(st.nextToken()), st.nextToken());
        }

        Arrays.sort(persons, (p1, p2) -> {
            if (p1.age == p2.age) {
                return 0;
            }
            return p1.age - p2.age;
        });

        Arrays.stream(persons).forEach(System.out::println);
    }
}