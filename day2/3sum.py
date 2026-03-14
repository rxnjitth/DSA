def threeSum(self, nums):
       result = []
       for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(i+2, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    triple = sorted([nums[i], nums[j], nums[k]])
                    if triple not in result:
                        result.append(triple)
        return result
            
