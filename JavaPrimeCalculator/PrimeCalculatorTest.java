import java.util.Scanner;
import java.lang.Math;

/**
 * Simple console tester for primecalculator methods
 * @author paul.gatto
 */
public class PrimeCalculatorTest {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {

        int inputNumber;

        String inputString;

        PrimeCalculator primeCalculator = new PrimeCalculator();


        System.out.println("Enter a number to find out if it's prime:");
        inputNumber = sc.nextInt();
        System.out.printf("%b\n\n", primeCalculator.isPrime(inputNumber));

        System.out.println("Enter a number to find all primes lower than it:");
        inputNumber = sc.nextInt();
        for (int i=2; i<inputNumber; i++) {
            if (primeCalculator.isPrime(i)) {
                System.out.printf("%d\n", i);
            }
        }

        System.out.println("\n\nEnter two numbers find all primes between the two:");
        System.out.println("First number:");
        int lowerBound = sc.nextInt();
        System.out.println("Second number:");
        int upperBound = sc.nextInt();
        System.out.printf("\nPrime numbers between %d and %d:\n", lowerBound, upperBound);
        for (int i=lowerBound; i<=upperBound; i++) {
            if (primeCalculator.isPrime(i)) {
                System.out.printf("%d\n", i);
            }
        }


        System.out.println("\n\nEnter a number to get a list of its prime divisors:");
        inputNumber = sc.nextInt();
        System.out.printf("%s\n\n", primeCalculator.getProductOfPrimes(inputNumber));
    }
}