class GCD {
    /* better solution in best cases
    
    public static void main(String[] args) {
        int n1 = 20, n2 = 15;
    
        int gcd = 1;
    
        for (int i = Math.min(n1, n2); i > 1; i--) {
            if ((n1 % i == 0) && (n2 % i == 0)) {
                gcd = i;
                break;
            }
        }
    
        System.out.println("GCD " + gcd);
    }
    */

    // optimal approach - Euclidean Algorithm
    public static void main(String[] args) {
        int a = 20, b = 15;

        while (a > 0 && b > 0) {
            if (a > b)
                a = a % b;
            else
                b = b % a;
        }

        if (a == 0)
            System.out.println(b);
        else System.out.println(a);
    }

}