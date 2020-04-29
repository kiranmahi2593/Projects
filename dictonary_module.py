def Add(x):
    
    Udict = dict()
    for i in range(x):
        DKey = input("Enter the Key:")
        DValue = input("Enter the Value:")
        
        Udict[DKey] = DValue
    print("Dictionary",Udict)
    return Udict
    



def Remove(x):
    
    val = input("enter the key name to remove dict:")
    x.pop(val)
    print("Dictionary after removing values:",x)
    return x

def Remove_last(x):
    
    
    n=list(x.keys())[-1]
    x.pop(n)
    print("Dictionary after removing values:",x)
    return x

def Get_keys(x):
    Lkeys = x.keys()
    print("Keys are:",Lkeys)
    return Lkeys

def Get_Values(x):
    Lval = x.values()
    print("values are:",Lval)
    return Lval

def Replace(x):
    val=input("Enter the key value to replace:")
    new_var = x[val]
    print("new replace value:",new_var)
    
