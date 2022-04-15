from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)
print('Welcome to the auction')
bid_start = True
bid_list = []
highest_bidder=None

while bid_start:
  bidder_name = input('What is your name')
  bid_value = int(input('How much will you bid : $'))
  bid_list.append({
    'name' : bidder_name,
    'amount' : bid_value
  })
    
  bid_play = input('Are there any other bidders? yes or no : ')
  
  if bid_play == 'yes':
    clear()
    continue
  elif bid_play == 'no':
    max_amount = 0
    for i,x in enumerate(bid_list):
      if x['amount'] > max_amount:
        max_amount = x['amount']
        highest_bidder=i
    break
print('The highest bidder is : {} with amount: {}'.format(bid_list[highest_bidder]['name'],bid_list[highest_bidder]['amount']))
  