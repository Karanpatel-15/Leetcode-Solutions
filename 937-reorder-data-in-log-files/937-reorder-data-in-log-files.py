class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        dig = []
        let = []
        
        for l in logs:
          splitL = l.split(" ", 1)
          identifier = splitL[0]
          content = splitL[1] 
          
          if content[0].isdigit():
            dig.append(l)
          else:
            let.append(l)
        
        let.sort(key=lambda x:x.split(" ",1)[0])
        let.sort(key=lambda x:x.split(" ",1)[1])
            
        return let + dig