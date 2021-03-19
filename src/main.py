import os
#import numpy as np
#from numpy import random as r
from tools import helpers as h
from tools import tournament as t
import Player as P

#START_ELOS = r.normal(loc=0, scale=0.1, size=10)
#START_ELOS[:] = [3000*h.normal(x) for x in START_ELOS]
START_ELOS = []
NUM_PlAYERS = 16

tournament_order = []
players = []

players_final_result = []
winner_id = 0


def main():
    if(os.path.exists("player.log")):
        os.remove("player.log")
    #START_ELOS[:] = [3000*h.normal(x) for x in START_ELOS]
    # START_ELOS.sort()
    START_ELOS = h.gen_elos(NUM_PlAYERS)
    START_ELOS.sort()
    print(START_ELOS)
    tournament_order = create_all(NUM_PlAYERS)
    print(tournament_order)

    i = 1
    for elo in START_ELOS:
        players.append(P.Player(i, elo))
        i += 1
    del i

    for player in players:
        f = open("player.log", "a")
        text = str(player.id) + " -> " + str(player.rating)
        print(text)
        f.write("Player " + str(text) + "\n")
        f.close()
    del f
    #p1 = P.Player(1, 1200)
    # print(p1.id)
    # print(p1.rating)
    #p1.rating = 1040
    # print(p1.rating)
    # h.test()
    # play_test_game()
    play_tournament(tournament_order, players)
    print(winner_id)
    print(players[winner_id - 1].rating)


def play_test_game():
    result = h.play_game(players[0].rating, players[1].rating)
    print(str(result) + "\nPlayer " +
          str(players[0].id) + " played player " + str(players[1].id))
    if(result[1] == -1):
        print("and lost")
    else:
        print("and won")
    print("New player " + str(players[0].id) +
          "\'s rating: " + str(result[0][0]))
    print("New player " + str(players[1].id) +
          "\'s rating: " + str(result[0][1]))


def play_tournament(order, player_list):
    """Must be multidimensional array for order."""
    new_list = []
    b = True
    if(len(order) == 1):
        print("The winner is player " + str(player_list[0].id) + " with a rating of " + str(player_list[0].rating) + ".")
        b = False
        global winner_id
        winner_id = player_list[0].id
    if(b):
        j = 0
        while(j < len(order[0]) - 1):
            s = ""
            old_ratings = (player_list[order[0][j] - 1].rating, player_list[order[0][j + 1] - 1].rating)
            new_ratings = h.play_game(player_list[order[0][j] - 1].rating, player_list[order[0][j + 1] - 1].rating)
            player_list[order[0][j] - 1].rating = new_ratings[0][0]
            player_list[order[0][j + 1] - 1].rating = new_ratings[0][1]
            if(new_ratings[1] == -1):
                new_list.append(player_list[order[0][j + 1] - 1])
                s = " Result: Loss."
            else:
                new_list.append(player_list[order[0][j] - 1])
                s = " Result: Win."
            print(old_ratings)
            print(new_ratings)
            print(order[0][j])
            print(order[0][j + 1])
            f = open("player.log", "a")
            #f.write("Player " + str(player_list[order[0][j] - 1].id) + " (" + str(old_ratings[0]) + ") " + "played " + str(player_list[order[0][j + 1] - 1].id) + " (" + str(old_ratings[1]) + ") " + s)
            try:
                f.write("Player " + str(player_list[order[0][j] - 1].id) + " (" + str(round(old_ratings[0])) + ") " + "played player " + str(player_list[order[0][j + 1] - 1].id) + " (" + str(round(old_ratings[1])) + ") " + s + "\n")
                f.write(str(player_list[order[0][j] - 1].id) + "\'s new rank is " + str(round(new_ratings[0][0])) + "\n")
                f.write(str(player_list[order[0][j + 1] - 1].id) + "\'s new rank is " + str(round(new_ratings[0][1])) + "\n")
            except IndexError:
                print("INDEX ERROR: ")
                print(j)
                print(" or ")
                print(j + 1)
                print("END ERROR")
            f.close()
            j += 2
            del f
        for k in new_list:
            print(k.rating)
        order.pop(0)
        play_tournament(order, new_list)


def create_all(length):
    temp = []
    while True:
        temp.append(t.generate_tournament(length))
        length //= 2
        if (length < 1):
            break
    return temp


if __name__ == '__main__':
    main()
