package shortest_reach;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class solution {

    // Complete the fibonacciModified function below.
    static BigInteger fibonacciModified(int t1, int t2, int n) {
    	BigInteger bigNumber1 = new BigInteger(Integer.toString(t1));
    	BigInteger bigNumber2 = new BigInteger(Integer.toString(t2));
    	BigInteger bigNumber3  = new BigInteger(Integer.toString(0));
    	
    	int a = 0;
    	for (int i = 0; i < n-2 ; i++ ) {
    		
    		bigNumber3 = bigNumber2.multiply(bigNumber2).add(bigNumber1);
    		bigNumber1 = bigNumber2;
    		bigNumber2 = bigNumber3;
    		
    		
    	}
    	
    	return bigNumber3 ;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/jeong-wonlyeol/Desktop/test.txt"));

        String[] t1T2n = scanner.nextLine().split(" ");

        int t1 = Integer.parseInt(t1T2n[0]);

        int t2 = Integer.parseInt(t1T2n[1]);

        int n = Integer.parseInt(t1T2n[2]);

        BigInteger result = fibonacciModified(t1, t2, n);

        bufferedWriter.write(result.toString());
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
