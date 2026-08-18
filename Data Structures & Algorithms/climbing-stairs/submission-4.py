class Solution:
    def climbStairs(self, n: int) -> int:
        #here we basically did was only remembered the last 2 steps ka ways no 
        #need to remeber rest all , its a fibonacci
        one,two = 1,1

        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one