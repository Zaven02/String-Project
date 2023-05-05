import java.util.*;

public class SpringArray {

    String springs="";

    Spring s_tmp = new Spring();
    int[] check = new int[springs.length()];
    int n = 0;
    int m = 0;
    int sum = 0;

    // We assume that there are no typos or wrong usage of parentheses.
    SpringArray(){
        String springs = "[{}{}[{}{}]{}]";
    }

    public int getParallelBraces(String[] springs, int k, int[] check){
        for (int i = 1; i == springs.length; i++){
            if(springs[i].equals("[") || springs[i].equals("]")){
                check[n] = i;
                n++;
            }
        }
        return k;
    }

    public Spring equivalentSpring(String springExpr, Spring[] springs){
        double k = 0;
        if (springs.equals("")) {
            return null;
        }
        for (int i = 0; i < check.length / 2; i++){
            sum += (check[check.length / 2 + 1 + i] - check[check.length / 2 - i] - 1) / 2;
        }

        k = s_tmp.getSpring();
        Spring s = new Spring(k);
        return s;
    }
}