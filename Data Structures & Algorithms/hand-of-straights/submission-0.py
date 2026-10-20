class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        d = Counter(hand)
        for i in hand:
            if d[i]!=0:
                d[i]-=1
                for j in range(1,groupSize):
                    if j+i in d:
                        d[j+i]-=1
                    else:
                        return False
        return True