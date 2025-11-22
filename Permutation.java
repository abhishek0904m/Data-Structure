import java.util.*;

public class Permutation {
    TreeSet<Integer> ts = new TreeSet();

    void generatePermutation(char ch[], int start, int end) {
        if (start == end) {
            ts.add(Integer.parseInt(String.valueOf(ch)));
        } else {
            for (int i = start; i <= end; i++) {
                swap(ch, start, i);
                generatePermutation(ch, start + 1, end);
                swap(ch, start, i);
            }
        }
    }

    void swap(char ch[], int i, int j) {
        char temp = ch[i];
        ch[i] = ch[j];
        ch[j] = temp;
    }

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        Permutation p = new Permutation();
        int n = sc.nextInt();
        String num = n + "";
        p.generatePermutation(num.toCharArray(), 0, num.length() - 1);

        for (int ele : p.ts) {
            if (ele > n) {
                System.out.println(ele);
                break;
            }
        }
    }
}
