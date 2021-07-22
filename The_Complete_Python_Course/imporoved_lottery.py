import random

# This line creates a set with 6 random numbers
lottery_numbers = set(random.sample(range(22), 6))

# winner_found = False
# Here are your players; find out who has the most numbers matching lottery_numbers!

players = [
    {'name': 'Rolf', 'numbers': {1, 3, 5, 7, 9, 11}},
    {'name': 'Charlie', 'numbers': {2, 7, 9, 22, 10, 5}},
    {'name': 'Anna', 'numbers': {13, 14, 15, 16, 17, 18}},
    {'name': 'Jen', 'numbers': {19, 20, 12, 7, 3, 5}}
]

# Then, print out a line such as "Jen won 1000.".
# The winnings are calculated with the formula:
# 100 ** len(numbers_matched)

matched_players = players[0]
# print(matched_players)

for player in players: 
    # print(player)
    players_matched_numbers = (len(player["numbers"].intersection(lottery_numbers))) #trying to get length of the players numbers that match the lotter numbers 
    # print(players_matched_numbers)
    if players_matched_numbers > len(matched_players["numbers"].intersection(lottery_numbers)):
        # print(players_matched_numbers)
        matched_players = player # players who match the player that has most numbers
        winning = 100 ** len(matched_players["numbers"].intersection(lottery_numbers))
       
        # print(f"{matched_players['name']} matched {players_matched_numbers}")
        # print(f"{matched_players['name']} won {winning}.")
        print("{} won {}".format(player.get('name'), winning))
    
    # if not winner_found:
    #     print("NO WINNER, EVERYONE IS SAD")