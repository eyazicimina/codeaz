import random

def buyer(p_input:list) -> float:
    if len(p_input) > 2:
        persentage = p_input[-1]/p_input[-3]
        return p_input[-2]*persentage+p_input[-2]
    else:
        return p_input[-1]*0.1

    if p_input[-1] < 0:
        p_input.append(0)
    return p_input

def seller(offered_prices):
    if offered_prices[0] > 100:
        if len(offered_prices) == 2:
            #: If first time
            if offered_prices[len(offered_prices)- 2] * 0.97 < offered_prices[len(offered_prices)- 1]:
                return 0
            else:
                return offered_prices[len(offered_prices)- 2] * 0.97 # if not, decrease it by %3
        else:
            #: If not first time
            if offered_prices[len(offered_prices)- 2] * 0.98 < offered_prices[len(offered_prices)- 1]:
                return 0
            else:
                return offered_prices[len(offered_prices)- 2] * 0.98
    else:
        if len(offered_prices) == 2:
            if offered_prices[len(offered_prices)- 2] * 0.9899 < offered_prices[len(offered_prices)- 1]:
                return 0
            else:
                return offered_prices[len(offered_prices)- 2] * 0.9899
        else:
            if offered_prices[len(offered_prices)- 2] * 0.9999 < offered_prices[len(offered_prices)- 1]:
                return 0
            else:
                return offered_prices[len(offered_prices)- 2] * 0.9999



moves = {
    1: ('divide', 3),
    2: ('minus', 0.30),
    3: (),
    4: (),
    5: (),
    6: ('accept', 0)
}


def run( initialBid: float, realPrice: float ):
    #: Declare variables
    prices = [initialBid]
    counter = 0
    #: Loop until reaches zero
    while counter < 20:
        #: Increment the counter
        counter += 1
        #: Go to buyer
        r = buyer( prices )
        if r == 0: break
        if r < 0: return 'SELLER WINS', prices
        prices.append(r)
        r = seller( prices )
        if r == 0: break
        if r < 0: return 'BUYER WINS', prices
        prices.append(r)
    #: Calculate the penalty
    penalty = counter * 5

    buyergain = realPrice - prices[-1] - penalty
    sellergain = prices[-1] - realPrice - penalty
    if buyergain > sellergain: return 'BUYER WINS', prices
    return 'SELLER WINS', prices


for _ in range(100):
    realPrice = random.randint(0, 200)
    initialBid = realPrice * random.randint( 5, 15 )
    print( realPrice, initialBid, run(  initialBid, realPrice ) )
