#Monthly Report Card Extract

yearly_revenue=[82000,56000,89000,8900,34000,23000,22000,16000,7800,78000,65000,79000]

print("12 Months revenue figure is :",yearly_revenue)

#creating first quarter using indexing

first_quarter=yearly_revenue[0:3]
print("first_quarter revenue :",first_quarter)

#creating fourth quarter using indexing
fourth_quarter=yearly_revenue[9:12]
print("fourth_quarter revenue :",fourth_quarter)

#creating  peak season earning list  using indexing
peak_season=first_quarter+fourth_quarter

print("peak season revenue :",peak_season)








