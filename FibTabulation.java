public class FibTabulation {
    int fib(int n)
    {
        int f[] = new int[n+1];
        f[0] = 0;
        f[1] = 1;
        for (int i = 2; i<= n; i++)
        //the value you're looking for are the previously computed values 
            f[i] = f[i-1] + f[i-2];
        return f[n];
    }

    public static void main(String[] args){
        FibTabulation f = new FibTabulation();
        int n = 9; 
        System.out.println("Fibonacci number is "+ f.fib(n));
    }
}