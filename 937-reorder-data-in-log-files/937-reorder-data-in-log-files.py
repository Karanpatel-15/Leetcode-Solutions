class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        dig = []
        let = []
        
        for l in logs:
          
          if l[-1].isdigit():
            dig.append(l)
          else:
            let.append(l)
        
        let.sort(key=lambda x:x.split(" ",1)[0])
        let.sort(key=lambda x:x.split(" ",1)[1])
            
        return let + dig