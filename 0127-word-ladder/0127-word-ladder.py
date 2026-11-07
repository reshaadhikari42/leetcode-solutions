class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        visited = set()
        wordList = set(wordList) #so look up is O(1)
        if endWord not in wordList: return 0
        q = deque()
        q.append([beginWord, 1]) #word, distance
        visited.add(beginWord)
        alpha = 'abcdefghijklmnopqrstuvwxyz'

        while q:
            word, distance = q.popleft()
            if word == endWord:
                return distance
            #to get neighbors
            for i in range(len(word)):
                for c in alpha:
                    new_word = word[0:i] + c + word[i+1:] #not including i
                    if new_word in wordList and new_word not in visited:
                        q.append([new_word, distance + 1])
                        visited.add(new_word)
        return 0