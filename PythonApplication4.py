

print("welcome to Python Pizza Deliveries!")
size=input("What size pizza do you want? S, M, or L ")
add_pepperoni= input("Do you want pepperoni? Y or N ")
extra_chesse=input("Do you want extra chesse? Y or N ")
if size =='S':
    cost=15
elif size=='M':
    cost=20
elif size=='L':
    cost=25
else:
    print("try to enter size again")
if add_pepperoni=='Y':
    if size=='S':
        cost_pep=2
    else:
       cost_pep=3
if extra_chesse=='Y':
    ex_chesse=1
else:
    ex_chesse=0
total_bill=cost+cost_pep+ex_chesse
print(f"Your final bill is: ${total_bill}")
    
