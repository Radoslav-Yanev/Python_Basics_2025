annual_tax = int(input())

# •	Баскетболни кецове – цената им е 40% по-малка от таксата за една година
# •	Баскетболен екип – цената му е 20% по-евтина от тази на кецовете
# •	Баскетболна топка – цената ѝ е 1 / 4 от цената на баскетболния екип
# •	Баскетболни аксесоари – цената им е 1 / 5 от цената на баскетболната топка

basketball_sneakers = annual_tax * 0.60
basketball_team = basketball_sneakers * 0.80
basketball_ball = basketball_team * 0.25
basketball_accessories = basketball_ball * 0.20

total_sum = annual_tax + basketball_sneakers + basketball_team + basketball_ball + basketball_accessories

print(total_sum)