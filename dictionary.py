# books={"book1":"white","book2":"black","price":30} #key-value pair
# print(books)
# print(books["book2"])
#  books

pizza={"small pizza": 150,"Medium pizza": 200,"Large pizza": 250,"pepperoni small":20,"pepperoni large or medium":30,"cheeses":10}
smallPizza= int(input("enter small pizza:"))
largePizza= int(input("enter large pizza:"))
mediumPizza= int(input("enter medium pizza:"))
pepperoniSmall= int(input("enter pepperoni small:"))
pepperoniLarge=int(input("enter pepperoni large:"))
cheese=int(input("enter cheese:"))
cost=smallPizza*pizza["small pizza"]+largePizza*pizza["Large pizza"]+mediumPizza*pizza["Medium pizza"]+pepperoniSmall*pizza["pepperoni small"]+pepperoniLarge*pizza["pepperoni large or medium"]+cheese*pizza["cheeses"]
print("Total amount=",cost)

