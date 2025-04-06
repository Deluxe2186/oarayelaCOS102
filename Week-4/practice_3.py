def changeme( mylist ):
    #This changes a past list
    mylist = [1,2,3,4]
    print("Valuse inside the function: ", mylist)
    return
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)