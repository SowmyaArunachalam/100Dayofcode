import random
rock ='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''
#Write your code below this line 👇
game_symbol=[rock,paper,scissors]
your_choice=int(input("What do you choose? Tye 0 for rock, 1 for paper,2 for scissors: "))
print(game_symbol[your_choice])
computer_choice=random.randint(0,2)
print(f"computer choice: {computer_choice}")
print(game_symbol[computer_choice])

if your_choice>=3 or your_choice<0:
  print("invaild number")
elif your_choice==0 and computer_choice==2:
  print("you win")
elif computer_choice==0 and your_choice==2:
  print("you loose")
elif your_choice==1 and computer_choice==0:
  print("you win")
elif computer_choice==1 and your_choice==0:
  print("you loose")
elif your_choice==2 and computer_choice==1 :
  print("you win")
elif computer_choice==2 and your_choice==1:
  print("you loose")
  
elif your_choice==computer_choice:
  print("its a draw")