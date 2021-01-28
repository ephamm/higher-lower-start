# Higher Lower Game

# import Art and Game_data
import random
from game_data import data
from art import logo 
from art import vs
from replit import clear

def get_random_account():
  """Get random data from accounts"""
  return random.choice(data)

# format data to be used in game.
def format_data(account):
  account_name  = account['name']
  account_descr = account['description']
  account_country = account['country']

  return f"{account_name} a {account_descr} from the {account_country}."

# Check user's guess.
def check_answer(guess, a_followers, b_followers):
  """ takes the acccount data and returns the printable fomrat. """
  if a_followers > b_followers:
    return guess == "a"
  else :
    return guess == "b"

# combining everything into function to easily call and repeat game

def game():
  # display art
  print(logo)

  # keep score
  score = 0
  game_should_continue = True
  # generate accounts from random data
  account_a = random.choice(data)
  account_b = random.choice(data)
  
  while game_should_continue:
    account_a = get_random_account()
    account_b = get_random_account()
  
  
    while account_a == account_b:
      account_b = get_random_account()

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("who has more follower either 'a' or 'b'?").lower()

    # check if user is correct
    ## compare a vs b
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # give user feedback on their guess
    # score keeping
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      print(f"sorry, that's wrong. Final score = {score}")

game()