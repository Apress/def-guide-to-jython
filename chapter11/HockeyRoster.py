# HockeyRoster.py
#
# Implemenatation logic for the HockeyRoster application

# Import Player class from the Player module

from Player import Player
import shelve

# Define shelve for storage to disk
player_data = shelve.open("players")

def make_selection():
    '''
    Creates a selector for our application.  The function prints output to the
    command line.  It then takes a parameter as keyboard input at the command
    line in order to choose our application option.
    '''
    options_dict = {1:add_player,
                    2:print_roster,
                    3:search_roster,
                    4:remove_player}
    print "Please chose an option\n"

    selection = raw_input('''Press 1 to add a player, 2 to print the roster,
                          3 to search for a player on the team,
                          4 to remove player, 5 to quit: ''')
    if int(selection) not in options_dict.keys():
        if int(selection) == 5:
            print "Thanks for using the HockeyRoster application."
        else:
            print "Not a valid option, please try again\n"
            make_selection()
    else:
        func = options_dict[int(selection)]
        if func:
            func()
        else:
            print "Thanks for using the HockeyRoster application."

def add_player():
    '''
    Accepts keyboard input to add a player object to the roster list.
    This function creates a new player object each time it is invoked
    and appends it to the list.
    '''
    add_new = 'Y'
    print "Add a player to the roster by providing the following information\n"
    while add_new.upper() == 'Y':
        first = raw_input("First Name: ")
        last = raw_input("Last Name: ")
        position = raw_input("Position: ")

        id = return_player_count() + 1
        print id
        #set player and shelve
        player = Player(id, first, last, position)
        player_data[str(id)] = player


        print "Player successfully added to the roster\n"
        add_new = raw_input("Add another? (Y or N)")
    make_selection()

def print_roster():
    '''
    Prints the contents of the list to the command line as a report
    '''
    print "====================\n"
    print "Complete Team Roster\n"
    print "======================\n\n"
    player_list = return_player_list()
    for player in player_list:
        print "%s %s - %s" % (player_list[player].first,
                player_list[player].last, player_list[player].position)
    print "\n"
    print "=== End of Roster ===\n"
    make_selection()

def search_roster():
    '''
    Takes input from the command line for a player's name to search within the
    roster list.  If the player is found in the list then an affirmative message
    is printed.  If not found, then a negative message is printed.
    '''
    index = 0
    found = False
    print "Enter a player name below to search the team\n"
    first = raw_input("First Name: ")
    last = raw_input("Last Name: ")
    position = None
    player_list = return_player_list()
    for player_key in player_list:
        player = player_list[player_key]
        if player.first.upper() == first.upper() and player.last.upper() == last.upper():
            position = player.position
    if position:
        print '%s %s is in the roster as %s' % (first, last, position)
    else:
        print '%s %s is not in the roster.' % (first, last)
    make_selection()

def remove_player():
    '''
    Removes a player from the list
    '''
    index = 0
    found = False
    print "Enter a player name below to remove them from the team roster\n"
    first = raw_input("First Name: ")
    last = raw_input("Last Name: ")
    position = None
    player_list = return_player_list()
    found_player = None
    for player_key in player_list:
        player = player_list[player_key]
        if player.first.upper() == first.upper() and player.last.upper() == last.upper():
            found_player = player
            break
    if found_player:
        print '''%s %s is in the roster as %s,
                 are you sure you wish to remove?''' % (found_player.first,
                                                        found_player.last,
                                                        found_player.position)
        yesno = raw_input("Y or N")
        if yesno.upper() == 'Y':
                # remove player from shelve
                print 'The player has been removed from the roster',
                found_player.id
                del(player_data[str(found_player.id)])
        else:
            print 'The player will not be removed'
    else:
        print '%s %s is not in the roster.' % (first, last)
    make_selection()

def return_player_list():
    return player_data

def return_player_count():
    return len(player_data.keys())
    
# main
#
# This is the application entry point.  It simply prints the applicaion title
# to the command line and then invokes the makeSelection() function.
if __name__ == "__main__":
    print "Hockey Roster Application\n\n"
    make_selection()