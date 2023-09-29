cgpa = int(input("enter cgpa="))
if(cgpa>=9 and cgpa<=10):
    print("grade=A")
elif(cgpa>=7 and cgpa<9):
    print("grade=B")
elif(cgpa>=5 and cgpa<7):
    print("grade=C")
else:
    print("fail")