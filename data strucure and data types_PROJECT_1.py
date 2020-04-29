#data structure and data types : PROJECT1

print("\n*********************Welcome To DS-DT Calulator*****************")
print("\nBelow are available functons")

available_functions ={1:'list',2:'Numbers',3:'set',4:'tuple',5:'string',6:"dictonary"}
for values,keys in available_functions.items():
    print(values,keys)
    
print("\n****************")
user_input=int(input("Select any of the  above available functions :"))
print("****************")

n=1
###########################################################

def string11():
    #global n
    #while n==1:
    string_input= str(input("Enter the required string :" ))
    if user_input==5:
        string_operations ={1:"Length",2:"Reverse",3:"Split",4:"Palindrome",5:"Add two String",6:"Starts with",7:"Ends with",8:"Replace"}
        for values,keys in string_operations.items():
                print(values,keys)
    #n=n+1
    
    selected_string =int(input("\nEnter any of the above string_operations :"))

    if selected_string ==1:
        l=len(string_input)
        print("Length of the string is :",l)           
    elif selected_string ==2:
        r=string_input[::-1]
        print("reverse output is :",r)
    elif selected_string ==3:
        s=string_input.split()
        print("split op is ",s)
    elif selected_string ==4:
        n=string_input[::-1]
        if n==string_input:        
            print ("string_input is a palindrome")
        else:
            print ("string_input is not a palindrome")
    elif selected_string ==5:
        y=str(input("enter the second string to add : "))
        x=(string_input+y)
        print(x)
    elif selected_string ==6:
        n=string_input[0]
        print("Start_char is ",n)
    elif selected_string ==7:
        n=string_input[0]
        print("End_char is ",n)
    elif selected_string ==8:
        y=str(input("enter the string2:"))
        z=int(input("enter the index no to be replaced:" ))
        r=x.replace(x[z],y)
        print("replace output is :",r)
    else:
        print("\ninvalid input , please enter a valid input value\n")
        #break
    
###########################################################

def list11():
    global n
    while n<=13:
        
        n=n+1
        #import list_function
        
        list_input =int(input("\nmx length of the list needed"))
        UserList=[]
        for i in range (0,list_input):
            UserListInput=int(input("enter the list value"))
            UserList.append(UserListInput)
        lil=UserList
        print("\nselected userlist is :",lil)

        if user_input==1:            
            list_operations = {1:'COUNT',2:'INSERT',3:'REMOVE',4:'POP',5:'CLEAR',6:'EXTEND',7:'INDEX',8:'APPEND',9:'SORT',10:'MIN',11:'MAX',12:'REVERSE'}
            for values,keys in list_operations.items():
                print('\n',values,keys)
                
        selected_list = int(input("\nselect any one of above list operation :"))
       
        if selected_list ==1:  
            x=lil.count(4)
            print("count output is ",x ,'\n')
                    
        elif selected_list ==2:
            lil.insert(1, "orange")
            print("\ninsert output is ",lil ,'\n')

        elif selected_list ==3:
            lil.remove(1)
            print("\nremove output is ",lil ,'\n')

        elif selected_list ==4:
            x=lil.pop(1)
            print("\npop output is",x ,'\n')

        elif selected_list ==5:
            lil.clear()
            print("\nclear output is",lil ,'\n')
                    
        elif selected_list ==6:
            lil.extend("one")
            print("\nextend output is",lil ,'\n')
            
        elif selected_list ==7:
            x=lil.index(1)
            print("\nindex output is",x ,'\n')
            
        elif selected_list ==8:
            lil.append("name")
            print("\nappend output is",lil ,'\n')
            
        elif selected_list ==9:
            lil.sort()
            print("\nsort output is",lil ,'\n')
            
        elif selected_list ==10:
            a=min(lil)
            print("\nmin output is",a ,'\n')

        elif selected_list ==11:
            a=max(lil)
            print("\nmin output is",a,'\n')
            
        elif selected_list ==12:
            lil.reverse()
            print("\nreverse output is",lil ,'\n')
            
        else:
            print("\ninvalid input , please enter a valid input value\n")
            break
###########################################################

def numbers11():
    global n
    while n<=13:
        if user_input==2:               
            num_operations = {1:'ADD',2:'SUB',3:'MUL',4:'DIVIDE',5:'FLOOR DIVISION',6:'POWER',7:'MOD',8:'SQUARE',9:'SQUARE ROOT',10:'CUBE ROOT',11:'CUBE',12:'PRIME',13:"Factorial"}
            for values,keys in num_operations.items():
                print(values,keys)
        n=n+1
        selected_num = int(input("\nselect any one of above numbers operation :"))
        x = int(input("\nenter a number for x:"))
        y = int(input("enter a number for y:"))    
        
        c={}
        fact=1
                
        import math
        if selected_num==1:
            add=x+y
            print("\noutput of add :", add)            
        elif selected_num==2:
            sub=x-y
            print("\noutput of sub :",sub)
        elif selected_num==3:
            mul=x*y
            print("\noutput of mul :",mul)            
        elif selected_num==4:
            div=x/y
            print("\noutput of div :",div)
        elif selected_num==5:
            fd=x//y
            print("\noutput of fd :",fd)
        elif selected_num==6:
            power_of_x=x**x
            power_of_y=y**y
            print("\noutput of power x:",power_of_x)
            print("output of power y:",power_of_y)
        elif selected_num==7:
            mod=x%y
            print("\noutput of mod :",mod)
        elif selected_num==8:
            square=x**2
            print("\nsquare of square :",square)
        elif selected_num==9:
            square_root=x**2
            print("\nsquare of squareroot :",square_root)
        elif selected_num==11:
            cube=x**3
            print("\nsquare of fd :",cube)
        elif selected_num==10:
            cube_root=x**3
            print("\square of fd :",(x**(1/3)))
                  
        elif selected_num==12:
            for c in range(x,y+1):
                for i in range(2,c):
                    if c%i==0:           
                        print(c,"it is not a prime")            
                        break           
            else:
                print(c," is not a prime")

        
        elif selected_num==13:
            for i in range(1,x+1):    
                fact=fact*i
                print("factorial",fact)
                break
        else:
            
            print("\ninvalid input , please enter a valid input value\n")
            break

###########################################################
def set11():
    global n
    while n<=13:
        if user_input==3:            
            set_operations = {1:'UPDATE',2:'DISCARD',3:'REMOVE',4:'UNION',5:'INTERSECTION',6:'DIFFRENCE',7:'SYMMETRIC',8:"superset",9:'subset',10:'disjoint',11:'add'}
            for values,keys in set_operations.items():
                print(values,keys)
        n=n+1
        set_input =int(input("\nmx length of the set needed"))
        UserSet=[]
        for i in range (0,set_input):
            UserSetInput=int(input("enter the set value"))
            UserSet.append(UserSetInput)
        
        print("\nselected userlist is :",UserSet)
        a=UserSet
        set1=set(a)
        print("set1 is :",set1)

       
        set2_input =int(input("\nmx length of the set needed"))
        UserSet2=[]
        for i in range (0,set2_input):
            UserSet2Input=int(input("enter the set value"))
            UserSet2.append(UserSet2Input)
        
        print("\nselected userlist is :",UserSet2)
        a=UserSet2
        set2=set(a)
        print("set2 is :",set2)

        selected_set = int(input("select any one of above set operation :"))
        
        if selected_set==1:
            set1.update(set2)
            print("update output is ",set1)
        elif selected_set ==2:
            set1.discard(11)
            print("discard output is",set1)
        elif selected_set ==3:
            set1.remove(2)
            print("remove output is",set1)
        elif selected_set ==4:
            set1.union(set2)
            print("union output is",set1)
        elif selected_set ==5:
            set1.intersection(set2)
            print("intersection output is",set1)
        elif selected_set ==6:
            x=set1.difference(set2)
            print("difference output is",x)
        elif selected_set ==7:
            x=set1.symmetric(set2)
            print("symmetric output is",x)
        elif selected_set ==8:
            x=set2.issuperset(set1)
            print("superset output is",x)
        elif selected_set ==9:
            x=set1.issubset(set2)
            print("subset output is",x)
        elif selected_set ==10:
            z = set1.isdisjoint(set2) 
            print("isdisjoint is :",z)
        elif selected_set ==11:
            set1.add(6)
            print(set1)
        else:
            print("\ninvalid input , please enter a valid input value\n")

            break

###########################################################
def Tuple11():
    global n
    while n<=4:
        if user_input==4:
            Tuple_ops = { 1:"length","2":"count","3":"index","4":"slicing"}
            for values,keys in Tuple_ops.items():
                     print(values,keys)
        n=n+1
        
        tuple_func=int(input("Enter the tuple function for above options:"))

        import tuple_module
        tuple1 = int(input("Enter the Length of Tuple to be created:"))
        utup = tuple_module.create_tuple(tuple1)

        if tuple_func == 1:
            print("The length of the Tuple is :",tuple_module.Length(utup))
            
        elif tuple_func == 2:
            print("count output is :",tuple_module.count(utup))
            
        elif tuple_func == 3:
            tuple_module.indexing(utup)
            
        elif tuple_func == 4:
            print("The finalized tuple after slicing :",tuple_module.slicing(utup))
                 
        else:
            print("\ninvalid input , please enter a valid input value\n")

            break
###########################################################

def Dictionary11():
    global n
    while n<=9:
        if user_input==6:
            Dictn_ops = { 1:"Add",2:"Remove",3:"Remove last element",4:"Get Keys",5:"Get Values",6:"Items",7:"Replace"}
            for values,keys in Dictn_ops.items():
                     print(values,keys)
        n=n+1
        
        Dictn_function=int(input("Enter the Dictionary function to be performed from above options:"))
        import dictonary_module
        input_dictonary = int(input("Enter the length of dictionary:"))

        if Dictn_function==1:            
            input_dictonary = dictonary_module.Add(input_dictonary)

        elif Dictn_function==2:
            input_dictonary = dictonary_module.Add(input_dictonary)
            dictonary_module.Remove(input_dictonary)

        elif Dictn_function==3:
            input_dictonary1 = dictonary_module.Add(input_dictonary)
            dictonary_module.Remove_last(input_dictonary1)
            
        elif Dictn_function==4:
            input_dictonary1 = dictonary_module.Add(input_dictonary)
            dictonary_module.Get_keys(input_dictonary1)

        elif Dictn_function==5:
            input_dictonary1 = dictonary_module.Add(input_dictonary)
            dictonary_module.Get_Values(input_dictonary1)

        elif Dictn_function==6:
            input_dictonary1 = dictonary_module.Add(input_dictonary)

        elif Dictn_function==7:
            input_dictonary1 = dictonary_module.Add(input_dictonary)
            dictonary_module.Replace(input_dictonary1)
        else:
            print("\ninvalid input , please enter a valid input value\n")

            break
               
if user_input==1:
    list11()
   
elif user_input==2:
     numbers11()

elif user_input==3:
     set11()

elif user_input==5:
     string11()

elif user_input==4:
    Tuple11()
        
elif user_input==6:
    Dictionary11()

   
 

