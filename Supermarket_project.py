from datetime import datetime
Name=input("Enter your name : ")
items='''
Rice    Rs 20/kg
Sugar   Rs 30/kg
Salt    Rs 20/kg
Oil     Rs 110/liter
Colgate Rs 85/each
Dal     Rs 30/kg
'''

price=0
totalprice=0
finalprice=0
pricelist=[]
ilist=[]
qlist=[]
plist=[]

# Rates for items
list_of_items={'Rice':20,'Sugar':30,'Salt':20,'Oil':110,'Colgate':85,'Dal':30}

option=int(input("For list of items press 1 and 2 for exit "))
if option==1:
    print(items)
for i in range(len(list_of_items)):
    info1=int(input("If you want to buy press 1 and 2 for exit"))
    if info1==2:
        break
    if info1==1:
        item=input("Enter the item ")
        quantity=int(input("Enter the quantity"))
        if item in list_of_items.keys():
            price=quantity*(list_of_items[item])
            pricelist.append((item,quantity,items,price))
            totalprice=totalprice+price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalprice=totalprice+gst
        else:
            print("Sorry you entered item is not available")
    else:
        print("You have entered wrong number")
    inf=input("Do you want bill yes or no :")
    if inf=='yes':
        pass
        if finalprice!=0:
            print(25*"=", "Hiral Supermarket",25*'=')
            print(25*"=","Anakapalli",30*"=")
            print("Name: ",Name,25*" ","Date: ",datetime.now())
            print(75*"-")
            print("SNo.",8*" ","Items",8*" ","Quantity",4*" ","price")
            for i in range(len(pricelist)):
                print(i,12*" ",ilist[i],12*" ",qlist[i],8*" ",plist[i])
            print(75*"-")
            print(50*" ","Total Amount ","Rs",totalprice)
            print(50*" ", "GST Amount","Rs",gst)
            print(75*"-")
            print(50*" ","Final Amount ","Rs",finalprice)
            print(75*"-")
            print(50*" ","Thanks for visiting")
            print(75*"-")
