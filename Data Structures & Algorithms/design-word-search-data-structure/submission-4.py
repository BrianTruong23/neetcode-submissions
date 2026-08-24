

class TrieNode:

    def __init__(self):
        self.children = {}
        self.endOfWord = False 

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

        
    def addWord(self, word: str) -> None:
        cur = self.root 
        for c in word: 

            if c not in cur.children:  
                cur.children[c] = TrieNode()
            
            cur = cur.children[c]
        
        cur.endOfWord = True 


    def search(self, word: str) -> bool:

        cur = self.root 

        return self.search_letter(cur, 0, word)
  

    def search_letter(self, cur, start, word):

        for u in range(start, len(word)):
            c = word[u]
            # print(start, c, u,, cur.children, word)
            if c == ".":
                
                for x in cur.children:
                    if self.search_letter(cur.children[x], u + 1, word):
                        return True 
                
                return False 
       
            else:
                if c not in cur.children:
                    return False 
                else:
                    cur = cur.children[c]
                
        return cur.endOfWord
    
        
