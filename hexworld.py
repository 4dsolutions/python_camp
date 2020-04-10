#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 15:59:02 2020

The Game class gives the players turns to play,
based on options derived from the Map class.
"""

class Winner(Exception):
    pass

class Loser(Exception):
    pass

class Quitter(Exception):
    pass

class Map:
    """
    Six hexagonal rooms around a central hexagonal room define
    the map.  Doors take the player to a neighboring room.
    Rooms contain points.
    """

    rooms = {0: "Control Room",
             1: "Fountain",
             2: "Deck",
             3: "Lookout",
             4: "Sanctuary",
             5: "Lounge",
             6: "Garage"}
    
    points_by_room = {0: 0,
                      1: 30,
                      2: 20,
                      3: 5,
                      4: 50,
                      5: 40,
                      6: 30}
    
    # reverse dictionary
    rooms_by_name = dict(zip(rooms.values(), rooms.keys()))
    
    connections = {0: [1,2,3,4,5,6],
                   1: [2,0,6],
                   2: [1,0,3],
                   3: [2,0,4],
                   4: [5,0,3],
                   5: [6,0,4],
                   6: [5,0,1]}

class Player:

    def __init__(self, nm):
        self.name = nm
        self.points = 0
    
class Game:
    """
    Will the player score more than 100 points before the 
    allowed number of turns, max_turns, runs out?
    
    Designed for use in a try block with a while True loop.
    The only way to escape the loop is by means of an 
    exception.  However Quitter is handled by __exit__
    whereas Winner and Loser propagate outside the context.
    """
    
    def __init__(self, player):
        self.player = player
        self.the_map = Map()
        self.room    = 0  # starting position
        self.turns   = 0
        self.max_turns = 8
        
    def turn_to_play(self):
        
        self.turns += 1
        
        # here is how we escape from the while True loop below
        if self.player.points > 100:
            raise Winner
        if self.turns > self.max_turns:
            raise Loser
            
        print("You are in the", self.the_map.rooms[self.room])
        print("You now have {} points".format(self.player.points))
        print("Turn number: {} of {}".format(self.turns, self.max_turns))
        print("You may move to:")
        
        # make a menu
        choices = dict(enumerate(
                self.the_map.connections[self.room],
                start=1))

        while True:
            # print the menu
            for num, next_room in choices.items():
                print(num, self.the_map.rooms[next_room])
                
            pick = input("Your move: > ")
            if pick.lower() == "q":
                raise Quitter
            if not pick.isdigit():
                print("Not an option")
                continue
            pick = int(pick) # this is safe to do now
            if not pick in choices.keys():
                print("Not an option")
                continue
            
            break  # answer is OK
        
        # go from menu to room name
        room_name = self.the_map.rooms[choices[pick]]
        # go from room name to room number
        self.room = self.the_map.rooms_by_name[room_name]
        # add any points from this room
        self.player.points += self.the_map.points_by_room[self.room]
        # the room no longer has points
        self.the_map.points_by_room[self.room] = 0
        
    def __enter__(self):
        """
        As you enter a context, you must go through here
        """
        print("Welcome to Hex World")
        # with X() as x: what __enter__ returns will be x
        return self  
    
    def __exit__(self, *oops): # *oops collects 3 pieces of info
        """
        As you leave a context, you must go through here
        """
        print("You are leaving Hex World")
        if oops[0] in (Winner, Loser):  # exception raised
            return False  # exception not yet handled
        return True       # in case of Quitter

def main():
    try:
        with Game(Player("Kirby")) as the_cage:
            # any Exception (Winner, Loser or Quitter) 
            # will abort the loop
            while True:
                the_cage.turn_to_play()
    except Winner:
        print("You win!")
        print("You have {} points!".format(the_cage.player.points))
    except Loser:
        print("You lose!")
    else:  # no exception, everything handled
        print("You quit the game.")   
        
if __name__ == "__main__":
    main()

