class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort(key = lambda x : x[0])
        prev_start = intervals[0][0]
        prev_end = intervals[0][1]
        res = []
        res.append([intervals[0][0], intervals[0][1]])
        for i in range(1, len(intervals)):
            print(intervals[i][0], prev_end)
            if intervals[i][0] <= prev_end:
                end = intervals[i][1]
                prev_end = max(prev_end, end)
                res[-1][1] = prev_end
            elif intervals[i][0] > prev_end:
                res.append([intervals[i][0], intervals[i][1]])
            
            # res.append([prev_start, prev_end])
            prev_start, prev_end = res[-1][0], res[-1][1]
        
        return res