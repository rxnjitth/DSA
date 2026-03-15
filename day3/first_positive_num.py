def firstMissingPositive(self, nums):
    
        nums.sort()
        expected = 1
        
        for num in nums:
            if num == expected:
                expected += 1
        
        return expected
            

        

            

            
            
            
       
            