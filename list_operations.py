list1=[8,0,8,9,9,9,4,6]
#finding length of list using len()
print(len(list1))

#repeatation of list 

list=list1*3
print(list)
#finding first index of item using index()
print(list1.index(8))

#finding total number of occurance of a item using count()
print(list1.count(9))

#copying a list into another list using copy()

new_list=list1.copy()
print("mm",new_list)

#reversing a list
x=new_list.reverse()
print("reversed list:",x)

# [x*2 for x in nums]

nums=[9,8,7,6,5,4]
print(nums)
for x in nums:
   print(x*2)
