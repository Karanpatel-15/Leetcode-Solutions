class TrieNode(object):
  
    def __init__(self):
      self.word = False
      self.children = {}

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for l in word:
          if l not in curr.children:
            curr.children[l] = TrieNode()
          curr = curr.children[l]
        curr.word = True
        return
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for l in word:
          if l not in curr.children:
            return False
          curr = curr.children[l]
        return curr.word == True
        

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for l in prefix:
          if l not in curr.children:
            return False
          curr = curr.children[l]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)