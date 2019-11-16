import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.lang.Math;

public class Index{
    public static int hIndex(int start, int end, ArrayList<Integer> c) {
        // System.out.println("Calcualting H-Index start: " +start+ " end: "+ end);
        int mid = (start + end)/2;
        int report = mid+1;
        int check = Math.min(report, c.get(mid).intValue());
        if (start >= end){
            int result;
            if (check == 0)
                result = 0;
            else 
                result = check;
            return result;
        }
        else
            if (c.get(mid)< report)
                return hIndex(start, mid-1, c);
            else if (c.get(mid) >= report)
                return hIndex(mid+1, end, c);
        return 0;
    }

    public static void main(String []args){

        Scanner input = new Scanner(System.in);
        //ArrayList<String> array = new ArrayList<>();
        String line = input.nextLine();

        int i;
        int count =0;

        ArrayList<Authors> authorList = new ArrayList<>();

        while (!line.equals("")){
            
            String[] array = line.split(" ");
            i = 2;

            ArrayList<Integer> citations = new ArrayList<>();

            while (i< array.length) {
                citations.add(Integer.parseInt(array[i]));
                i++;
            }

            Collections.sort(citations);
            Collections.reverse(citations);

            int hIndex = hIndex(0, citations.size()-1,citations);

            Authors newAuthor = new Authors(array[0], array[1], citations, hIndex); 
            
            authorList.add(newAuthor);
            count++;

            line = input.nextLine();
        }

        authorList.sort(Comparator.comparing(Authors::gethIndex).reversed().thenComparing(Authors::getlName));

        for (int y =0; y<count; y++){
            System.out.println("Author: "+ authorList.get(y).lName + " " + authorList.get(y).fName);
            System.out.println("H-Index: "+ authorList.get(y).hIndex);
            System.out.println("");
        }

        input.close();

    }

    public static class Authors{
        public ArrayList<Integer> citations; 
        public String lName, fName; 
        public int hIndex; 

        public Authors(String lName, String fName, ArrayList<Integer> citations, int hIndex){
            this.lName = lName; 
            this.fName = fName; 
            this.hIndex = hIndex; 
            this.citations = citations; 
        }

        public Authors(){
            lName = null; 
            fName = null; 
            hIndex = 0; 
        }

        public String getlName(){
            return this.lName; 
        }

        public String getfName(){
            return this.fName;
        }

        public int gethIndex(){
            return this.hIndex;
        }
    }
}