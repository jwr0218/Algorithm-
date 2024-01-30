package Largest_Permutation;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;




public class Solution {

	
    // Complete the largestPermutation function below.
    static int[] largestPermutation(int k, int[] arr) {
    	HashMap<Integer,Integer> map = new HashMap<>();
    	PriorityQueue<Integer> find = new PriorityQueue<Integer>(Collections.reverseOrder());
    	for(int i = 0 ; i <arr.length ; i ++) {
    		find.add(arr[i]);	
    		map.put(arr[i], i);
    	
    	}
    	int i = 0;
    	
		
    	while (!find.isEmpty()) {
			int val = find.poll();
			
			if (map.get(val) == i) {
				
				continue;
			}
			if (i == k) {
				break;
			}
			
			
			else {
				
				int data = arr[i];
				int index = map.get(val);
				
				arr[i] = val;
				arr[index] = data;	
				map.put(arr[i], i);
				map.put(data, index);
				
				i ++;
			}
			
		}
    	/*
    	
    	for( int i = 0 ;i < arr.length; i ++) {
    		System.out.print(Integer.toString(arr[i])+"\t");
    	}
    	
    	System.out.println("---------------------");
    	

		Iterator<Integer> keys = map.keySet().iterator();
        while( keys.hasNext() ){
            int key = keys.next();
            int value = map.get(key);
            System.out.println("키 : "+key+", 값 : "+value);
        }
    	*/
    	
    	return arr;
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        String[] nk = scanner.nextLine().split(" ");

        int n = Integer.parseInt(nk[0]);

        int k = Integer.parseInt(nk[1]);

        int[] arr = new int[n];

        String[] arrItems = scanner.nextLine().split(" ");
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int i = 0; i < n; i++) {
            int arrItem = Integer.parseInt(arrItems[i]);
            arr[i] = arrItem;
        }

        int[] result = largestPermutation(k, arr);

        

        scanner.close();
    }
}

