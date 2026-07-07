#GPS Location Logger

#creaataed tuples storing lattitude and lagnitude
location1=(10,12)
location2=(34,9)
location3=(78,78)
location4=(3,9)

#storing tuples into list

list=[location1,location2,location3,location4]
print("Lacations are : ",list)


#accessing individual lattitude and lognitude value
print(f"LOcation 1 : {location1[0]} - {location1[1]} ")
print(f"LOcation 2 : {location2[0]} - {location2[1]} ")

print(f"LOcation 3 : {location3[0]} - {location3[1]} ")
print(f"LOcation 4 : {location4[0]} - {location4[1]} ")
#checking whether tuple is mutable or not 
try:
    location4[0]=9
except TypeError as e:
    print(e)

