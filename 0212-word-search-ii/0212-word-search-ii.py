class TrieNode:
    def __init__(self):
        self.children = {}
        self.wordEnd = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.wordEnd = True

    def removeWord(self, word):
        curr = self.root
        for c in word:
            if len(curr.children[c].children) == 0: #look 2 steps forward before deleting.
                del curr.children[c]
                return
            else:
                curr = curr.children[c]


    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        #add words to Trie
        for word in words:
            self.addWord(word)

        #dfs begins
        #removalRoot = self.root
        def dfs(r, c, word,curr):
            if r < 0  or c < 0 or r >= rows or c >= cols or board[r][c] not in curr.children or (r,c) in visit:
                return

            #if it reaches here, the letter exists
            ch = board[r][c]
            word += ch
            curr = curr.children[ch]

            if curr.wordEnd: #removing the word after its found
                res.append(word)
                self.removeWord(word)
                curr.wordEnd = False #don't know if this is needed?

            visit.add((r,c))
            dfs(r+1,c,word,curr)
            dfs(r-1,c,word, curr)
            dfs(r,c+1,word, curr)
            dfs(r,c-1,word, curr)

            visit.remove((r,c))


        #search begins
        curr = self.root
        rows, cols = len(board), len(board[0])
        visit = set()
        res = [] #updated in dfs

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, '',self.root)
        return res