class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
                        #[12,3,7,1]
        '''
        s = distance/time
        t = distance/ speed = (target - position[i]) / speed[i] 
        stack = [1,7,3,12]
        [2,7,1]
        '''
        pair = []
        for i in range(len(position)):
            pair.append([position[i],speed[i]])

        sorted_pair = sorted(pair, key = lambda x:x[0], reverse = True)

        stack = []
        for pos, speed in sorted_pair:
            time = (target - pos) / speed

            if stack and stack[-1][1] >= time:  #if its a fleet
                #stack.pop() don't pop
                continue  #do nothing don't add
            else:
                stack.append([pos, time])
        
        return len(stack)

        
            
