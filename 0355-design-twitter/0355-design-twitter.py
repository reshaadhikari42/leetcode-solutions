class Twitter:
    def __init__(self):
        self.tweetList = defaultdict(list)
        self.following = defaultdict(set)
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetList[userId].append([self.time, tweetId])
        self.time -= 1        

    def getNewsFeed(self, userId: int) -> list[int]:
        heap = []
        for following in self.following[userId] | {userId}:
            tweets = self.tweetList[following]
            index = len(tweets) - 1
            if index >= 0: #you need to check for users with no tweets as well apparently.
                time, tweet = tweets[index]
                heap.append([time, tweet, following, index])
                
        heapify(heap)
        res = []
        while heap and len(res) < 10:
            time, tweet, following, index = heapq.heappop(heap)
            res.append(tweet)
            index -= 1
            if index >= 0:
                tweets = self.tweetList[following]
                time, tweet = tweets[index]
                heapq.heappush(heap,[time, tweet, following, index])
        return res       
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None: 
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)