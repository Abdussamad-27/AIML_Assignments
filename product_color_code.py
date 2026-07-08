#Product Colour Code Lookup

#creating list where key is  rgb colors as tuple and value as stock 

paint_dict={
    (254,0,0):7,(0,254,0):9,(0,0,254):19
}
#taking rgb values from users

r=int(input("Enter rgb value for R(Red):"))
g=int(input("Enter rgb value for G(Green):"))
b=int(input("Enter rgb value for B(Blue):"))

#creating a tuple

color=(r,g,b)

#checking whether stock is available 

if color in paint_dict :
    print("Stock is available")
else:
    print("Stock is not  available")
