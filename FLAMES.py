print("*****************welcome to FLAMES calculator********************")

name1=input("enter a name1 :")
name2=input("enter a name2 :")
name1=name1.replace(" ","")
name2=name2.replace(" ","")


for i in name1:           
    for j in name2: #here it compares "a"(name1) with "x"and"y"(name2)and "b"(name1) with "x"and"y"(name2)
        if i==j:
            name1=name1.replace(i,'',1) #replace(i,'',1) - "1" is used as it will replace only once.
            name2=name2.replace(j,'',1)
            break

#"break" is ued so that it goes back to the 1st for loop.if break is not used, then the changes made in the if statement
#will not be reflectdback. (eg):with name1 as "nisha" and naemw "nishaan" with will replace 1st leter "n" in both
#but the o/p will be updated only in 2nd for loop as "ishaan" and in 1st for loop as still "nisha"

count=len(name1+name2)

list1 = ["Friends","Lovers","Affection","Marriage","Enemies","Sister"]


while len(list1)>1:
    c=count%len(list1)
    index=c-1     #since index starts wth 0 in list, we are reducing the valu to match with the index of list
    if index>=0:
        left_flames=list1[:index]
        right_lames=list1[index+1:]
        list1=(left_flames+right_lames)
    else:
        list1=list1[:len(list1)-1]
        
print("relationhip status of name1 and name2 is:",list1 )

        



        
