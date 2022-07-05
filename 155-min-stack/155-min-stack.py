class MinStack(object):

    def __init__(self):
        self.stack = [] # inside [min till that point, val]
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        if len(self.stack) > 0:       
          self.stack.append([min(val, self.stack[-1][0]),val])
        else:
          self.stack.append([val,val])

    def pop(self):
        """
        :rtype: None
        """
        if len(self.stack) > 0:
          self.stack.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
          return self.stack[-1][1]
      

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) > 0:
          return self.stack[-1][0]
      
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()