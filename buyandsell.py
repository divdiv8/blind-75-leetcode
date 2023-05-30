#bruteforce
def maxProfit_brute(self, prices) -> int:
    pro =[0]
    for i in range(0,len(prices)):
        for j in range(0,len(prices)):
            if i<j:
                pro.append(prices[j]-prices[i])
    print(pro)
    profit = max(pro)
    if profit<0:
        return 0
    return max(pro)

def maxProfit_deq(prices):
    pro=[0]
    left = 0
    for i in range(0,len(prices)):
        right = min(prices)
        
    