package hackerrank_string;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;



class Result {


    public static int kruskals(int gNodes, List<Integer> gFrom, List<Integer> gTo, List<Integer> gWeight) {
    
        boolean[] boo = new boolean[gNodes];
        int[] Union = new int[gNodes];
        
        int[][] lst = new int[gFrom.size()][3] ;
        for(int i = 0 ; i < gFrom.size() ; i++){
            lst[i][0] =  gFrom.get(i);
            lst[i][1] =  gTo.get(i);
            lst[i][2] =  gWeight.get(i);
          
        }
        for(int i = 0 ; i < gNodes ; i ++) {
        	  Union[i] = -1 ; 
              //System.out.print(Union[i]);
        }
        //System.out.print("\n");
        
        
        Arrays.sort(lst,Comparator.comparingInt(o1->o1[2]));
        int weight = 0 ;
        
        for(int i = 0 ; i < lst.length ; i++) {
        	//System.out.println("weight"+lst[i][2]);
        	int num = findUnion(Union,lst[i][1]-1);
        	int num_1 = findUnion(Union,lst[i][0]-1);
            if(num!=num_1) {
            	
            	
            	
            	//System.out.println("from"+(lst[i][0]));
            	//System.out.println("to"+(lst[i][1]));
            	
            	
            	Union[findUnion(Union,lst[i][1]-1)] = findUnion(Union,lst[i][0]-1);
            	
            	
            	//System.out.println(lst[i][1] +" "+Union[lst[i][1]-1]);
            	
            	
            	weight = weight + lst[i][2];
            	
            	
            }
        }
        

        return weight;
    }
    
    public static int findUnion(int[] para,int parx) {
    	if (para[parx] == -1){
    		return parx;
    		
    	}
    	else {
    		return findUnion(para,para[parx]); 
    	}
    }
    
    
    
    
    
    

}



public class kruskal_really_special {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        //BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("/Users/jeong-wonlyeol/Desktop/text.txt")));

        String[] gNodesEdges = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

        int gNodes = Integer.parseInt(gNodesEdges[0]);
        int gEdges = Integer.parseInt(gNodesEdges[1]);

        List<Integer> gFrom = new ArrayList<>();
        List<Integer> gTo = new ArrayList<>();
        List<Integer> gWeight = new ArrayList<>();

        IntStream.range(0, gEdges).forEach(i -> {
            try {
                String[] gFromToWeight = bufferedReader.readLine().replaceAll("\\s+$", "").split(" ");

                gFrom.add(Integer.parseInt(gFromToWeight[0]));
                gTo.add(Integer.parseInt(gFromToWeight[1]));
                gWeight.add(Integer.parseInt(gFromToWeight[2]));
            } catch (IOException ex) {
                throw new RuntimeException(ex);
            }
        });

        int res = Result.kruskals(gNodes, gFrom, gTo, gWeight);
        System.out.println(res);
        // Write your code here.

        bufferedReader.close();
        //bufferedWriter.close();
    }
}

