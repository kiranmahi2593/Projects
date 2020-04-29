def create_tuple(x):
    
    tup = []
    
    for i in range(x):
        
        tinput = input("Enter the elements:")
        tup.append(tinput)
        tup1 = tuple(tup)
    
    return tup1

def Length(x):
    Length = len(x)
    return Length

def count(x):
    ele = input("Enter the element to be counted:")
    ecount = x.count(ele)
    print("Count of the element is:",ecount)
    #return ecount

def indexing(x):
    ival = input("Enter the index value to checked:")
    ival1 = x.index(ival)
    print("Index of given input:",ival1)
    #return ival1

def slicing(x):
    a = int(input("enter the index value from where the slicing would start:"))
    b = int(input("enter the index value the slicing should end:"))
    return x[a:b]
