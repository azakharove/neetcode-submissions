class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for number in nums:
            if number in count:
                count[number] += 1
            else:
                count[number] = 1
        topk = []
        while k > 0:
            max_key = max(count, key=count.get)
            topk.append(max_key)
            count.pop(max_key)
            k -= 1
        return topk

