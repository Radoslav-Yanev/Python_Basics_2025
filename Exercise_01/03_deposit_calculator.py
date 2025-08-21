# 1.	Депозирана сума – реално число в интервала [100.00 … 10000.00]                                                                      
# 2.	Срок на депозита (в месеци) – цяло число в интервала [1…12]
# 3.	Годишен лихвен процент – реално число в интервала [0.00 …100.00]

deposit_sum = float(input())
deposit_expire = int(input())
annual_interest_rate = float(input()) / 100

amount = deposit_sum + deposit_expire * ((deposit_sum * annual_interest_rate) / 12)

print(amount)

