package shortest_reach;
import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class solution {

		
	
    // Complete the bfs function below.
    static int[] bfs(int n, int m, int[][] edges, int s) {
    	
    	int start = s-1;
    	int[] way = new int[n];
    	
    	boolean[] boo = new boolean[n];
    	Queue<Integer> queue = new LinkedList<Integer>();
    	int[][] ed = new int[n][n];
    	for( int i = 0 ; i < edges.length ; i ++) {
    		int f = edges[i][0] -1;
    		int z = edges[i][1] -1;
    		
    		ed[f][z] = 1;
    		ed[z][f] = 1;
    	}
    	
    	
    	s = s-1;
    	
    	queue.add(s);
    	boo[s] = true;
		
    	
    	while(!queue.isEmpty()) {
    		s = queue.poll();
        	for (int i = 0 ; i < ed[s].length ; i ++) {
	    		if (ed[s][i] == 1 & boo[i] == false) {
	    			
	    			way[i] = way[s]+1;
	    			boo[i] = true;
	    			queue.add(i);
	    		}	
	    	}
    	}
    	LinkedList<Integer> way_linked = new LinkedList<Integer>();
    	for(int i = 0 ; i <n ; i ++ ) {
    		if (way[i] == 0) {
    			way_linked.add(-1);
    		}
    		else {
    		way_linked.add(way[i]*6);
    		}
    	}
    	way_linked.remove(start);
    	
    	int[] a = new int[way_linked.size()];
    	
    	Iterator<Integer> iter = way_linked.iterator();
    	int cnt = 0 ;
    	while(iter.hasNext()){//다음값이 있는지 체크
    		int k = iter.next();
    		a[cnt] = k;
    	
    		cnt = cnt+1;
    	}
    
	
    	return a;
    	
    }

    private  static Scanner scanner = new Scanner(System.in);

    public  static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter("/Users/jeong-wonlyeol/Desktop/test1.txt"));

        int q = scanner.nextInt();
        scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

        for (int qItr = 0; qItr < q; qItr++) {
            String[] nm = scanner.nextLine().split(" ");

            int n = Integer.parseInt(nm[0]);

            int m = Integer.parseInt(nm[1]);

            int[][] edges = new int[m][2];

            for (int i = 0; i < m; i++) {
                String[] edgesRowItems = scanner.nextLine().split(" ");
                
                scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");
                
                
                
                for (int j = 0; j < 2; j++) {
                    int edgesItem = Integer.parseInt(edgesRowItems[j]);
                    edges[i][j] = edgesItem;
                    
                }
                
            }

            int s = scanner.nextInt();
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            int[] result = bfs(n, m, edges, s);

            for (int i = 0; i < result.length; i++) {
                bufferedWriter.write(String.valueOf(result[i]));

                if (i != result.length - 1) {
                    bufferedWriter.write(" ");
                }
            }

            bufferedWriter.newLine();
        }

        bufferedWriter.close();

        scanner.close();
    }
}



