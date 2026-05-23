class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_frequency = {}
        

        for i in nums:
            if i in nums_frequency:
                nums_frequency[i] = nums_frequency[i] + 1
            else:
                nums_frequency[i] = 1
        
        sorted_nums_frequency = dict(sorted(nums_frequency.items(), key=lambda item: item[1], reverse=True))
        
        returned_list = list(sorted_nums_frequency)
        return returned_list[:k]
