import java.util.Arrays;
import java.util.HashSet;

class Solution {
    public int distributeCandies(int[] candies) {
        // remove repititions //
        HashSet < Integer > set = new HashSet < > ();
        for (int candy: candies) {
            set.add(candy);
        }
        // count n/2 times //
        return Math.min(candies.length / 2, set.size());
    }

    public static void main(String[] args) {
      int[] candies = {6,2,1,2,3,4,5,6};
      int ret = new Solution().distributeCandies(candies);
      String out = String.valueOf(ret);
      System.out.println(out);
    }
}

