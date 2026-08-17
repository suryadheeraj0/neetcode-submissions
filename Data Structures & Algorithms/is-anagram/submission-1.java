class Solution {
    public boolean isAnagram(String s, String t) {
        int[] s_freq = new int[26];
        int[] t_freq = new int[26];
        for(int i=0;i<s.length();i++){
            s_freq[s.charAt(i)-'a']++;
        }
        for(int j=0;j<t.length();j++){
            t_freq[t.charAt(j)-'a']++;
        }
        System.out.println(Arrays.toString(s_freq));
        System.out.println(Arrays.toString(t_freq));
        for(int k=0;k<s_freq.length;k++){
            if(s_freq[k]!=t_freq[k]){
                return false;
            }
        }
        return true;
    }
}
