class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        ArrayList<int[]> list = new ArrayList<>();

        for(Map.Entry<Integer,Integer> entry : map.entrySet()) {
            list.add(new int[]{entry.getKey(), entry.getValue()});
        }
        Collections.sort(list, (a, b) -> Integer.compare(b[1], a[1]));
        int ans[] = new int[k];
        for(int i = 0; i < k; i++) {
            ans[i] = list.get(i)[0];
        }

        return ans;
    }
}
