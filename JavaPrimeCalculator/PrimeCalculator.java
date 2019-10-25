/**
 * Class for calculating primes & associated algorithms
 * @author paul.gatto
 */
public class PrimeCalculator {

    /**
     * Finds smallest prime factor of a number if that number is a prime
     * @param number integer to be evaluated for smallest divisor
     * @return smallest divisor as integer
     */
    private static int getSmallestDivisor(int number) {
        if (number == 0 || number == 1) {
            return 1;
        } else {
            for (int x = 2; x <= (number/2); x++) {
                if (number % x == 0) {
                    return x;
                }
            }
        }
        return 1;
    }

    /**
     * Returns true if the input parameter is a prime integer. Uses the number divided by two as an upper limit when evaluating.
     * @param number number to be evaluated
     * @return true if prime, false otherwise
     */
    public static boolean isPrime(int number) {
        if (number == 0 || number == 1) {
            return false;
        } else {
            for (int x = 2; x <= (number/2); x++) {
                if (number % x == 0) {
                    return false;
                }
            }
            return true;
        }
    }

    /**
     * Returns true if the input parameter is a prime integer, but uses the square root of the input for an upper limit.
     * @param number number to be evaluated
     * @return true if prime, false otherwise
     */
    public static boolean isPrimeSqrt(int number) {
        if (number == 0 || number == 1) {
            return false;
        } else {
            for (int x = 2; x <= Math.sqrt(number); x++) {
                if (number % x == 0) {
                    return false;
                }
            }
            return true;
        }
    }

    /**
     * Gets products of a number broken down into primes
     * @param number number to be evaluated
     * @return string representing breakdown of number into its prime products
     */

    public static String getProductOfPrimes(int number) {
        int currentValue = number;
        String productList = "";

        if (currentValue < 2) {
            return "ERROR";
        } else if (isPrime(number)) {
            //just return 1 * that number
            //return String.valueOf(number) + " = " + String.valueOf(number) + "*1";
            return String.valueOf(number) + " is a prime, therefore its only divisors are 1 and itself";
        } else {
            while (isPrime(currentValue) == false && currentValue > 2) {
                int newPrime = getSmallestDivisor(currentValue);
                currentValue = currentValue / newPrime;
                productList += String.valueOf(newPrime);
                productList += "*";
            }
            //currentvalue is now last prime once this loop has finished
            if (currentValue != 1) {
                productList += String.valueOf(currentValue);
            }
            return productList;
        }
    }
}
