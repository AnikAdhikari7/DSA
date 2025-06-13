public class PrimeNumber {
    public static void main(String[] args) {
        int n = 1, count = 0;

        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                System.out.print(i + " ");
                count++;

                if (n / i != i) {
                    System.out.print(n / i + " ");
                    count++;
                }

            }
        }

        if (count == 2)
            System.out.println(true);
        else
            System.out.println(false);
    }
}

// time complexity = O(sqrt(N))
