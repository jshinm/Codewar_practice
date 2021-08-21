# Given an integer x, return true if x is palindrome integer.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

class Solution:
    #string solution
    def isPalindrome_int(self, x: int) -> bool:
        
        if x >= -2**31 and x <= 2**31 - 1:
        
            temp = str(x)

            if temp == temp[::-1]:
                return True
        
        return False

    #integer solution - search the half
    def isPalindrome(self, x: int) -> bool:
        
        if x >= -2**31 and x <= 2**31 - 1:
                        
            if x < 10:
                if x < 0:
                    return False
                else:
                    return True
                
            if x % 10 == 0: #the last digit can't be zero
                return False
            
            newSeq = 0
            
            while (x >= newSeq):                

                if newSeq == x:
                    return True
                                
                newSeq *= 10
                newSeq += x % 10
                x = int(x / 10)
                
                if x == 0:
                    return False
                
                # print(newSeq, x)
                
            if x == int(newSeq / 10):
                return True
            
        return False   

# public boolean isPalindrome(int num){
#    if(num < 0) return  false; 
#    int reversed = 0, remainder, original = num;
#    while(num != 0) {
#         remainder = num % 10; // reversed integer is stored in variable
#         reversed = reversed * 10 + remainder; //multiply reversed by 10 then add the remainder so it gets stored at next decimal place.
#         num  /= 10;  //the last digit is removed from num after division by 10.
#     }
#     // palindrome if original and reversed are equal
#     return original == reversed;
# }