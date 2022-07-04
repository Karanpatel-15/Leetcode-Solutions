class TrieNode():
    
    def __init__(self):
        self.children = {}
        self.completed = False

class WordDictionary(object):

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.head
        for l in word:
          if l not in curr.children:
            curr.children[l] = TrieNode()            
          curr = curr.children[l]
        curr.completed = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        def dfs(curr, i):
          
          for i in range(i, len(word)):
            letter = word[i]
            if word[i] == ".":
              for c in curr.children.values():
                if dfs(c, i+1):
                  return True
              return False
            elif letter not in curr.children:
              return False
            curr = curr.children[letter]
          return curr.completed
        return dfs(self.head, 0)
            
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)