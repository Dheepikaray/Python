fruit={"apple","mango","banana","cherry"}
print(fruit)
fruit.add("orange")
print(fruit)
fruit.update({"strawberry","pineapple"})
print(fruit)
print("orange" in fruit)
fruit2={"grapes"}
fruit3=fruit.union(fruit2)
print(fruit3)
fruit.remove("mango")
print(fruit)
fruit.discard("cherry")
print(fruit)