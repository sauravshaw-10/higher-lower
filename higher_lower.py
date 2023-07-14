from game_data import data
import random
from art import logo, vs
from replit import clear



def get_account():
  random_key = random.randint(0,len(data)-1)
  f_data = data[random_key]

def format_account():  
  name1 = f_data["name"]
  follower_count1 = f_data["follower_count"]
  description1 = f_data["description"]
  country1 = f_data["country"]
  
  random_key2 = random.randint(0,len(data)-1)
  l_data = data[random_key2]
  name2 = l_data["name"]
  follower_count2 = l_data["follower_count"]
  description2 = l_data["description"]
  country2 = l_data["country"]
  
  if f_data == l_data:
    get_data()
  else:
    print(f"Compare A: {name1}, a {description1}, from {country1}")
    print(vs)
    print(f"Against B: {name2}, a {description2}, from {country2}")

    

  # Check follower count
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()
  score = 0
  if guess == 'A'.lower():
    if follower_count1 > follower_count2:
      score += 1
      print(f"You are correct. Current Score: {score}")
    else:
      clear()
      print(f"Sorry, that's incorrect. Final Score: {score}")

  elif guess == 'B'.lower():
    if follower_count2 > follower_count1:
      score += 1
      print(f"You are correct. Current score: {score}")
    else:
      clear()
      print(f"Sorry, that's incorrect. Final Score: {score}")

  return 


    

get_data()
    
  
