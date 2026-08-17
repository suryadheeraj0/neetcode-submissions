class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> map = new HashMap<>();
        for(int i=0;i<strs.length;i++){
            int[] char_freq = new int[26];
            String curr_str = strs[i];
            for(int j=0;j<curr_str.length();j++){
                char_freq[curr_str.charAt(j)-'a']++;
            }
            String key = Arrays.toString(char_freq);
            if(!map.containsKey(key)){
                map.put(key, new ArrayList<>());
            }
            map.get(key).add(curr_str);
        }
        return new ArrayList<>(map.values());
    }
}
