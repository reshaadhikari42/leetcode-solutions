class Solution:
    #we can use recursion backtrack dfs but this is the shortest path qn and bfs is a better soln
    #we solve it as a graph where the word is node and its neighbor is another word with one letter difference
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordList = set(wordList) #for O(1) seach
        visit = set()
        q = deque()
        q.append([beginWord, 1]) #1 is the distance 
        visit.add(beginWord)
        alpha = 'abcdefghijklmnopqrstuvwxyz'
        if endWord not in wordList: return 0
        #bfs
        while q: #O(n)
            word, dist = q.popleft()
            if word == endWord:
                return dist
            #now look for neighbors
            for i in range(len(word)): #O(m)
                for c in alpha: #O(26)
                    new_word = word[0:i] + c + word[i+1:] #exclude i
                    #this takes O(m) time and space where m is letter of word
                    #concat creates a new str everytime
                    if new_word in wordList and new_word not in visit:
                        q.append([new_word, dist+1])
                        visit.add(new_word)
        return 0

        #time is O(n*m*m) 
        #space is O(nm) for q and visit