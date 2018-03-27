public int maxSpan(int[] nums) {
  int left = 0,
      right = nums.length,
      longestSpan = 0;
  
  Map<Integer, Integer> map = new HashMap<Integer, Integer>();
  
  for (int num: nums){
    int count = (map.containsKey(num)) ? map.get(num) : 0;
    map.put(num, ++count);
  }
  
  for (int num : map.keySet()){
    if (map.get(num) >= 2){
      int i;
      
      for(i = 0; nums[i] != num; i++);
      left = i;
      
      for(i = nums.length - 1; nums[i] != num; i--);
      right = i;
      
      longestSpan = Math.max(right - left + 1, longestSpan);
    }
    if (!map.isEmpty()){
      longestSpan = Math.max(longestSpan, 1);
    }
  }
  
  return longestSpan;
}
