class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        first = 0 #first pointer will be in the first index
        zero = 0 #zero pointer will be in the first index
        second = len(nums)-1 #second poimnter will be in the last index
        
        
        while(first<=second):  #iterate through the list, if the first pointer crosses the second pointer the loop will break
            
            if nums[first] == 1:  #if my num is 1 im just moving the first pointer to the next index
                first+=1
                
            elif nums[first] == 0:  #if the num is 0 we gonna move the 0 to the left side where we have zero pointer, if we 0 we gonna swap t to the zero index 
                nums[first],nums[zero] = nums[zero],nums[first]
                zero+=1  #after swapping we are incermenting zero pointer
                first+=1 #after swapping we are incermenting first pointer
                    
            else: #if the num is 2 we are swapping the first pointer and the second pointer, we are moving the val 2 to the right most where we have second pointer 
                nums[first],nums[second] = nums[second],nums[first]
                second-=1  #after swapping we are decrementing the second pointer
            
        