MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resource_sufficient(order_incredients):
  for item in order_incredients:
    if order_incredients[item] >= resources[item]:
      print(f"sorry,not enough {item}")
      return False
  return True

def coins():
  print("please insert coins")
  total = int(input("how many quarters: ")) * 0.25
  total+=int(input("how many dimes: " ))*0.10
  total+=int(input("how many nickles: " ))*0.05
  total+=int(input("how many pennies: " ))*0.01
  return total

def transaction_successful(money_recieved,drink_cost):
  if money_recieved >= drink_cost:
     change = round(money_recieved - drink_cost,2)
     print(f"change amount {change}")
     global profit
     profit+=drink_cost
     return True
  else:
     print("sorry,not enough money")
     return False
    
def  coffee(drink_item,order_ingredients):
  for item in order_ingredients:
    resources[item]-=order_ingredients[item]
  print(f"Here,is your drink {choice},enjoy")
  
  
  
on=True
while on:
  choice=input("What would you like? (espresso/latte/cappuccino): ")
  if choice=='off':
    on=False
  elif choice=='report':
    print(f"water :{resources['water']} ml")
    print(f"milk :{resources['milk']} ml")
    print(f"coffee :{resources['coffee']} ml")
    print(f"profit : ${profit} ")
  else: 
    drink = MENU[choice]
    if resource_sufficient(drink['ingredients']):
      payment=coins()
      if transaction_successful(payment,drink['cost']):
        coffee(choice,drink['ingredients'])




    



    