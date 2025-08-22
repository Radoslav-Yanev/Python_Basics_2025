yearly_tax_for_basketball = int(input())

basketball_sneakers = yearly_tax_for_basketball - (yearly_tax_for_basketball * 0.40)
basketball_team = basketball_sneakers - (basketball_sneakers * 0.20)
basketball_ball = basketball_team / 4
basketball_accessorise = basketball_ball / 5

total_sum = basketball_sneakers + basketball_team + basketball_ball + basketball_accessorise + yearly_tax_for_basketball

print(f"{total_sum:.2f}")