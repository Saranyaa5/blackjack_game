############### Blackjack Project #####################
def play():
  def won():
    print(f"your final hand{user_cards},final Score:{user_score(user_cards)}")
    print(f"computer's final hand:{computer_cards},final Score:{computer_score(computer_cards)}")
    print("you win the game")
  def lost():
    print(f"your final hand{user_cards},final Score:{user_score(user_cards)}")
    print(f"computer's final hand:{computer_cards},final Score:{computer_score(computer_cards)}")
    print("you lose")
  def draw():
    print(f"your final hand{user_cards},final Score:{user_score(user_cards)}")
    print(f"computer's final hand:{computer_cards},final Score:{computer_score(computer_cards)}")
    print("the match is draw")
  def extra_user_card(extra_card):
    #yes
    if(extra_card=='y'):
      user_cards.append(random.choice(cards))
      if(user_score(user_cards)>21):
        if(11 in user_cards):
          user_cards.remove(11)
          user_cards.append(1)
          if(user_score(user_cards)<21):
            print(f"Your cards: {user_cards}, current score: {user_score(user_cards)}")
            print(f"computer's first card: {computer_cards[0]}")
            extra_user_card(input("want extra card for user? y or n: "))
        print(f"Your cards: {user_cards}, current score: {user_score(user_cards)}")
        print(f"computer's first card: {computer_cards[0]}")
        lost()
      else:
       print(f"Your cards: {user_cards}, current score: {user_score(user_cards)}")
       print(f"computer's first card: {computer_cards[0]}")
       extra_user_card(input("want extra card for user? y or n: "))
    #no
    else:
      if(computer_score(computer_cards)< user_score(user_cards) and user_score(user_cards)<=21 and computer_score(computer_cards)<=21):
        won()
      elif(computer_score(computer_cards)>21 and user_score(user_cards)<=21):
        won()
      elif computer_score(computer_cards)==user_score(user_cards):
        draw()
      elif(computer_score(computer_cards)>user_score(user_cards) and user_score(user_cards)<=21 and computer_score(computer_cards)<=21):
        lost()

  def user_score(user_cards):
    ans=0
    for user_card in user_cards:
      ans+=user_card
    return ans
  def computer_score(computer_cards):
    ans=0
    for computer_card in computer_cards:
      ans+=computer_card
    return ans
  from art import logo
  import random
  do=input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
  if(do=='y'):
   print(logo)
   cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
   user_cards=[]
   while(len(user_cards)<2):
       user_cards.append(random.choice(cards))
   print(f"Your cards: {user_cards}, current score: {user_score(user_cards)}")
   #computer 
   computer_cards=[]
   while(computer_score(computer_cards)<17):
       computer_cards.append(random.choice(cards))
   print(f"computer's first card: {computer_cards[0]}")
   extra_user_card(input("want extra card for user? y or n: "))
   play()
play()