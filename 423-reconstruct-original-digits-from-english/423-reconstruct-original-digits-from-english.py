from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        
        
        * zero  -> z 
        one   -> o - 0 - 2 - 4 
        * two   -> w
        * three -> h - 8
        * four  -> u
        * five  -> v - 7
        * six   -> x
        * seven -> s - 6
        * eight -> g
        nine  -> i - 5 - 6 - 8 
        
        """
        
        cnt = Counter(s)
        res = {}
        
        res[0] = cnt["z"]
        res[2] = cnt["w"]
        res[4] = cnt["u"]
        res[6] = cnt["x"]
        res[8] = cnt["g"]
        
        res[3] = cnt["h"] - res[8]
        res[7] = cnt["s"] - res[6]
        res[5] = cnt["v"] - res[7]
        res[9] = cnt["i"] - res[5] - res[6] - res[8]
        res[1] = cnt["o"] - res[0] - res[2] - res[4]
        
        string = ""
        for i in range(10):
          string += str(i) * res[i]
          
        return string



        
        

        
        