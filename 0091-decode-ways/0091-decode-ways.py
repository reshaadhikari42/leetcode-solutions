class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+1) #we have one longer index so that we don't have to have base case for second element as it follows the same case
        '''
        if you wanted to set dp to len(s) you would have to do this. this ocmplicates dp[1]. instead we just increase the dp length by 1 and follow the loop rule.
        dp[0] = 1, dp[1] = 1 if s[0] != '0' version, the loop could start from i = 2 the same way.
        '''
        dp[0] = 1
        if s[0] == '0':
            return 0
        else:
            dp[1] = 1

        for i in range(2,len(s)+1): #make sure to run till len(s)+1 bc dp is one length longer than s
            #since size of dp and s is diff, s[i-1] is current element and dp[i] is current dp pos
            if s[i-1] == '0':
                if s[i-2] == '1' or s[i-2] == '2': #we can use 10 or 20
                    dp[i] = dp[i-2]  #no additional combination. whatever combination we have before 10/20 we just append 10 or 20 in the end
                else: #eg 30 is an invalid string
                    return 0

            else: #its a valid number
                if (s[i-2] == '1') or (s[i-2] == '2' and int(s[i-1]) < 7):  #can be a double digit. if 1 is prev, curr can be anything but if 2 is prev, curr can't be more than 26 to be valid
                    dp[i] = dp[i-1] + dp[i-2]
                else: #eg 48 where s[i-1] = curr = 8
                    dp[i] = dp[i-1]  #we have no cominations, we add this one digit to whatever we had. for eg: 48 is just 4,8. 4 was already there we just add 8- cannont make new comb

        return dp[len(s)]