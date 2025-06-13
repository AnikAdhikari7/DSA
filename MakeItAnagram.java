// Make It Anagram - check two string and count how many chars need to be removed to make the two string anagram.
// print the removed chars and the number of chars

public class MakeItAnagram {
    public static void main(String[] args) {

        String str1 = "abc", str2 = "dec", str3 = "a";

        for (int i = 0; i < str1.length(); i++) {
            String ch = Character.toString(str1.charAt(i));

            if (str2.contains(ch)) {
                str2 = str2.replaceFirst(ch, "");
            } else {
                str3 += ch;
            }
        }

        int count = str2.length() + str3.length();

        System.out.println(str3);
        System.out.println(str2);
        System.out.println(count);
    }
}

