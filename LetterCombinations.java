import java.util.*;

public class LetterCombinations {

    static String keypad[] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};

    static List<String> letterCombination(String num) {
        if (num == null || num.length() == 0) return new ArrayList<>();
        List<String> ans = new ArrayList<>();
        dfs(num, 0, new StringBuilder(), ans);
        return ans;
    }

    static void dfs(String num, int i, StringBuilder sb, List<String> ans) {
        if (i == num.length()) {
            ans.add(sb.toString());
            return;
        }

        int digit = num.charAt(i) - '0';

        if (digit < 0 || digit > 9 || keypad[digit].isEmpty()) {
            dfs(num, i + 1, sb, ans);
            return;
        }

        for (char ch : keypad[digit].toCharArray()) {
            sb.append(ch);
            dfs(num, i + 1, sb, ans);
            sb.deleteCharAt(sb.length() - 1);
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String num = sc.nextLine().trim();
        System.out.println(letterCombination(num));
        sc.close();
    }
}
