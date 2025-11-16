class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        # approch : using stack and savign elemenst in the stakc and if a higher number comes and if k i snot zero i would rathe pop out this higher number rather than any potential smaller number elemenst later 
        # its also possibel that by the end the number could be greater than this earkie higer numbers like in thsi test case 1432219, 9 > 4 but still taking the 4 intially will make the whole valiue smaller than taking the 9 number in the end
        # tc : O(n), sc : O(n)

        if len(num) <= k:
            return "0"

        stack = []

        for digit in num:
            while k>0 and stack and stack[-1] > digit:
                stack.pop()
                k-=1
            
            stack.append(digit)
        
        # all numbers are equal 
        while k>0:
            stack.pop()
            k-=1
        
        output = "".join(stack).lstrip("0") 

        if output != "":
            return output
        else: 
            return "0"
        