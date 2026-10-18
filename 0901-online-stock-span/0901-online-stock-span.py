class StockSpanner:
    def __init__(self):
        self.stack = []
    '''
seems like we need to check the stack[-1-length] until we find stack[-1-i] > price, and then return i+1 as length should start from 1 apprarently.
and then we also append the price as it is necessary for next comparison..

to make time comp better, we just compare with the top of the stack. if we can save [price, length] on stack together. we don't ahve to check all.
because [60,70, 60,75,85] will look like stack = [[60,1], [70,2],[60,1],[75,2],[85,3]]

that works... but we got TLE
to make solution better: we can store [index, price] in stack.
and we don't need to store smaller values. we only store the bigger values. that way stack will be smaller.
this is because we don't care about smaller prices. [60,70,80]
for 80 we don't need 60s price if that is added to 70s price. we can also pop 70 after we add 70's high to 80s
stack will be like = [[60,1]] first and then in another loop:
[[70,2]] this will determine that we had something before 70 that was smaller than 70
then it becomes [[80,3]] this shows that whatever comes after 80 if its bigger than 80 can just use its price +1
if anything comes over 80 that is smaller than 80, then it will just return 1 and don't need to look at 60,70 anymore
'''

    def next(self, price: int) -> int:
        span = 0
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append([price, span + 1])
        return span + 1



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)