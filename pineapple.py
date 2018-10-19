from scipy.special import comb, perm

def drawOutsComb(iOuts,iHit,iDeck,iDraw):
    answer = 0;
    while iHit<= iOuts:
        answer = answer + comb(iOuts,iHit)*comb(iDeck - iOuts,iDraw - iHit)
        iHit = iHit + 1
    return answer

def drawProbability(iOuts,iHit,iDeck,iDraw):
    return drawOutsComb(iOuts,iHit,iDeck,iDraw)/comb(iDeck,iDraw)

def DeckLeft(iPosition,iRound):
    #iPositon EP 0 MP 1 BT 2
    if iRound == 1:
        return 54-iPosition*5
    else:
        return 54-15-3-(iPosition-1)*2-(iRound-2)*7

def DrawLeft(iRound):
    return 12 - (iRound-1)*3
    #iPositon EP 1 MP 2 BT 3

########aab
gDraw = 12
gHIt = 2
gOutsNoJoker = 5
gOutsWithJoker = 7

print 'EP aab no joker:'
print drawProbability(gOutsNoJoker,gHIt,DeckLeft(1,1),gDraw)

print 'MP aab no joker:'
print drawProbability(gOutsNoJoker,gHIt,DeckLeft(2,1),gDraw)

print 'BT aab no joker:'
print drawProbability(gOutsNoJoker,gHIt,DeckLeft(3,1),gDraw)

print 'EP aab joker:'
print drawProbability(gOutsWithJoker,gHIt,DeckLeft(1,1),gDraw)

print 'MP aab joker:'
print drawProbability(gOutsWithJoker,gHIt,DeckLeft(2,1),gDraw)

print 'BT aab joker:'
print drawProbability(gOutsWithJoker,gHIt,DeckLeft(3,1),gDraw)

a = comb(5,1)*comb(5,1)*comb(DeckLeft(2,4),1) + comb(5,2)*comb(5,1) + comb(5,2)*comb(5,1)
b = comb(4,1)*comb(6,1)*comb(DeckLeft(2,4),1) + comb(4,2)*comb(6,1) + comb(4,1)*comb(6,2)
c = comb(3,1)*comb(7,1)*comb(DeckLeft(2,4),1) + comb(3,2)*comb(7,1) + comb(3,1)*comb(7,2)
d = comb(2,1)*comb(8,1)*comb(DeckLeft(2,4),1) + comb(2,2)*comb(8,1) + comb(2,1)*comb(8,2)

A = comb(DeckLeft(2,4),3)
print '5  5:'
print a/A
print '4  6:'
print b/A
print '3  7:'
print c/A
print '2  8:'
print d/A

gOutsWithJoker = 6
for i in range(1,4):
    for j in range(0,5):
        if i == 1:
            strTemp = 'EP Round'
        if i == 2:
            strTemp = 'MP Round'
        if i == 3:
            strTemp = 'BT Round'
        strTemp = strTemp + str(j)
        print strTemp
        print DrawLeft(j)
        print drawProbability(gOutsWithJoker,3,DeckLeft(i, j),DrawLeft(j))


