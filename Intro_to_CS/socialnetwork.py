# --------------------------- #
# Intro to CS Final Project   #
# Gaming Social Network       #
# --------------------------- #
#
# For students who have subscribed to the course,
# please read the submission instructions in the Instructor Notes below.
# ----------------------------------------------------------------------------- 

# Background
# ==========
# You and your friend have decided to start a company that hosts a gaming
# social network site. Your friend will handle the website creation (they know 
# what they are doing, having taken our web development class). However, it is 
# up to you to create a data structure that manages the game-network information 
# and to define several procedures that operate on the network. 
#
# In a website, the data is stored in a database. In our case, however, all the 
# information comes in a big string of text. Each pair of sentences in the text 
# is formatted as follows: 
# 
# <user> is connected to <user1>, ..., <userM>.<user> likes to play <game1>, ..., <gameN>.
#
# For example:
# 
# John is connected to Bryant, Debra, Walter.John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.
# 
# Note that each sentence will be separated from the next by only a period. There will 
# not be whitespace or new lines between sentences.
# 
# Your friend records the information in that string based on user activity on 
# the website and gives it to you to manage. You can think of every pair of
# sentences as defining a user's profile.
#
# Consider the data structures that we have used in class - lists, dictionaries,
# and combinations of the two (e.g. lists of dictionaries). Pick one that
# will allow you to manage the data above and implement the procedures below. 
# 
# You may assume that <user> is a unique identifier for a user. For example, there
# can be at most one 'John' in the network. Furthermore, connections are not 
# symmetric - if 'Bob' is connected to 'Alice', it does not mean that 'Alice' is
# connected to 'Bob'.
#
# Project Description
# ====================
# Your task is to complete the procedures according to the specifications below
# as well as to implement a Make-Your-Own procedure (MYOP). You are encouraged 
# to define any additional helper procedures that can assist you in accomplishing 
# a task. You are encouraged to test your code by using print statements and the 
# Test Run button. 
# ----------------------------------------------------------------------------- 

# Example string input. Use it to test your code.
example_input="John is connected to Bryant, Debra, Walter.\
John likes to play The Movie: The Game, The Legend of Corgi, Dinosaur Diner.\
Bryant is connected to Olive, Ollie, Freda, Mercedes.\
Bryant likes to play City Comptroller: The Fiscal Dilemma, Super Mushroom Man.\
Mercedes is connected to Walter, Robin, Bryant.\
Mercedes likes to play The Legend of Corgi, Pirates in Java Island, Seahorse Adventures.\
Olive is connected to John, Ollie.\
Olive likes to play The Legend of Corgi, Starfleet Commander.\
Debra is connected to Walter, Levi, Jennie, Robin.\
Debra likes to play Seven Schemers, Pirates in Java Island, Dwarves and Swords.\
Walter is connected to John, Levi, Bryant.\
Walter likes to play Seahorse Adventures, Ninja Hamsters, Super Mushroom Man.\
Levi is connected to Ollie, John, Walter.\
Levi likes to play The Legend of Corgi, Seven Schemers, City Comptroller: The Fiscal Dilemma.\
Ollie is connected to Mercedes, Freda, Bryant.\
Ollie likes to play Call of Arms, Dwarves and Swords, The Movie: The Game.\
Jennie is connected to Levi, John, Freda, Robin.\
Jennie likes to play Super Mushroom Man, Dinosaur Diner, Call of Arms.\
Robin is connected to Ollie.\
Robin likes to play Call of Arms, Dwarves and Swords.\
Freda is connected to Olive, John, Debra.\
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures."



def to_list(string_input):
    """
    Converts string_input to sentences seperated with ",".

    Keyword Arguments:
    string_input -- Block of text where each line of block is separated by ".".

    Returns:
    Returns list with each sentences seperated by ",".
    """
    
    output = []
    start_point = 0
    end_point = string_input.find(".")
    while end_point != -1:
         string = string_input[start_point:end_point]
         output.append(string)
         start_point = end_point + 1
         end_point = string_input.find(".",start_point)

    return output




def get_name(string_input):
    """
    Gets the name of the user from input string.

    Keywork Arguments:
    string_input -- string with keywords like "is connected" or "likes to play" in it.

    Returns:
    Returns name of the user as a string from string_input.
    """
    get_is =  string_input.find("is")
    get_likes =  string_input.find("likes")

    if "is connected" in string_input:
        return string_input[:get_is-1]
    elif "likes to play" in string_input:
        return string_input[:get_likes-1]
    else:
        return None


    
def connection(string_input):
    """
    Gets the name of connections from input string.

    Keyword Arguments:
    string_input -- string with keyword "connection" in it.

    Returns:
    Returns dictionary with user's connections as a list.   
    """
    output = {}
    if "is connected" in string_input:
        find_connected = string_input.find("to")
        value = string_input[find_connected+3:].split(", ")
        if value == [''] or find_connected == -1:
            output["Connections"] = []
            return output
        else:
          output["Connections"] = value
          return output


   
         
def get_games(string_input):
    """
    Gets the name of the games from input string.

    Keyword Argument:
    string_input -- string with keyword "likes to play" in it.

    Returns:
    Returns dictionary with games of the user as list.
    """
    output = {}
    if "likes to play" in string_input:
        get_play = string_input.find("play")
        value = string_input[get_play+5:].split(", ")
        if value == [''] or get_play == -1:
             output["Games"] = []
             return output
        else:
            output["Games"] = value
            return output


# ----------------------------------------------------------------------------- 
# create_data_structure(string_input): 
#   Parses a block of text (such as the one above) and stores relevant 
#   information into a data structure. You are free to choose and design any 
#   data structure you would like to use to manage the information.
# 
# Arguments: 
#   string_input: block of text containing the network information
#
#   You may assume that for all the test cases we will use, you will be given the 
#   connections and games liked for all users listed on the right-hand side of an
#   'is connected to' statement. For example, we will not use the string 
#   "A is connected to B.A likes to play X, Y, Z.C is connected to A.C likes to play X."
#   as a test case for create_data_structure because the string does not 
#   list B's connections or liked games.
#   
#   The procedure should be able to handle an empty string (the string '') as input, in
#   which case it should return a network with no users.
# 
# Return:
#   The newly created network data structure

def create_data_structure(string_input):
    """
    Cretes data structure from block of text.
    
    Keyword Argument:
    string_input -- block of text with name of users, connections and games.
    
    Returns:
    Returns dictionary with each username with their connection
    and games as a list.
    """
    network = {}
    str_to_sen = to_list(string_input)
    for i in str_to_sen:
        name = get_name(i)
        if name not in network:
            network[name] = {}
        if "likes to play" in i:
             network[name].update(get_games(i))
        if "is connected" in i:
            network[name].update(connection(i))
            
    return network

# ----------------------------------------------------------------------------- # 
# Note that the first argument to all procedures below is 'network' This is the #
# data structure that you created with your create_data_structure procedure,    #
# though it may be modified as you add new users or new connections. Each       #
# procedure below will then modify or extract information from 'network'        # 
# ----------------------------------------------------------------------------- #

# ----------------------------------------------------------------------------- 
# get_connections(network, user): 
#   Returns a list of all the connections that user has
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all connections the user has.
#   - If the user has no connections, return an empty list.
#   - If the user is not in network, return None.

def get_connections(network, user):
    """
    Looks for connection in network for user.
    
    Keyword Argument:
    network -- Data Structure created by create_data_structure
    user -- name of the user whose connection needs to be returned.
    
    Returns:
    Returns the list of connections of given user if exists.
    """
    if user in network:
        return network[user]["Connections"]
   

# ----------------------------------------------------------------------------- 
# get_games_liked(network, user): 
#   Returns a list of all the games a user likes
#
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
# 
# Return: 
#   A list of all games the user likes.
#   - If the user likes no games, return an empty list.
#   - If the user is not in network, return None.
def get_games_liked(network,user):
    """
    Looks for games liked by the user in the network.
        
    Keyword Argument:
    network -- Data Structure created by create_data_structure.
    user -- name of the user whose games needs to be returned. 

    Returns:
    Returns list of game for given user if exists.
    """
    if user in network:
        return network[user]["Games"]
      

# ----------------------------------------------------------------------------- 
# add_connection(network, user_A, user_B): 
#   Adds a connection from user_A to user_B. Make sure to check that both users 
#   exist in network.
# 
# Arguments: 
#   network: the gamer network data structure 
#   user_A:  a string with the name of the user the connection is from
#   user_B:  a string with the name of the user the connection is to
#
# Return: 
#   The updated network with the new connection added.
#   - If a connection already exists from user_A to user_B, return network unchanged.
#   - If user_A or user_B is not in network, return False.


def add_connection(network, user_A, user_B):
    """
    Adds user_B to the connections of user_A if user_B is not there.
    
    Keyword Argument:
    network -- Data Structure created by create_data_structure.
    user_A -- name of the user whose connections needs to be modified
    user_B -- name of the user that needs to be added to connection list of user_A.
    
    Returns:
    Updated list of connections of user_A and returns
    gamer data structure.
    """
    

    if user_A in network and user_B in network:
        connections = network[user_A]["Connections"]
        if user_B not in connections:
            connections.append(user_B)
    else:
        return False

    return network 

# ----------------------------------------------------------------------------- 
# add_new_user(network, user, games): 
#   Creates a new user profile and adds that user to the network, along with
#   any game preferences specified in games. Assume that the user has no 
#   connections to begin with.
# 
# Arguments:
#   network: the gamer network data structure
#   user:    a string containing the name of the user to be added to the network
#   games:   a list of strings containing the user's favorite games, e.g.:
#		     ['Ninja Hamsters', 'Super Mushroom Man', 'Dinosaur Diner']
#
# Return: 
#   The updated network with the new user and game preferences added. The new user 
#   should have no connections.
#   - If the user already exists in network, return network *UNCHANGED* (do not change
#     the user's game preferences)



def add_new_user(network, user, games):
    """
    Adds new user to the games network data structure.

    Keyword Argument:
    network -- the gamer network data structure.
    user --  a string containing the name of the user to be added to the network.
    games --   a list of strings containing the user's favorite games.
    
    Returns:
    Returns updated network with new user added with associated games.
    """
      
    all_games = {}
    all_connections = {}
    if user not in network:
        network[user] = {}
        all_games["Games"] = games
        all_connections["Connections"] = []
        network[user].update(all_games)
        network[user].update(all_connections)
    
    return network
		
# ----------------------------------------------------------------------------- 
# get_secondary_connections(network, user): 
#   Finds all the secondary connections (i.e. connections of connections) of a 
#   given user.
# 
# Arguments: 
#   network: the gamer network data structure
#   user:    a string containing the name of the user
#
# Return: 
#   A list containing the secondary connections (connections of connections).
#   - If the user is not in the network, return None.
#   - If a user has no primary connections to begin with, return an empty list.
# 
# NOTE: 
#   It is OK if a user's list of secondary connections includes the user 
#   himself/herself. It is also OK if the list contains a user's primary 
#   connection that is a secondary connection as well.




def get_secondary_connections(network, user):
    """
    Searches for all the connections of connections for user.

    Keyword Argument:
    network -- the gamer network data structure.
    user -- a string containing the name of the user.
    
    Returns:
    Returns all the secondary connections of the user if exists
    else empty list.
    """
       

    if user not in network:
        return None
    primary_connections = get_connections(network,user)
    secondary_connections = []

    if primary_connections != []:
        for i in primary_connections:
            connections = get_connections(network,i)
            for i in connections:
                if i not in secondary_connections:
                    secondary_connections.append(i)
        return secondary_connections
    else:
        return []

# ----------------------------------------------------------------------------- 	
# connections_in_common(network, user_A, user_B): 
#   Finds the number of people that user_A and user_B have in common.
#  
# Arguments: 
#   network: the gamer network data structure
#   user_A:  a string containing the name of user_A
#   user_B:  a string containing the name of user_B
#
# Return: 
#   The number of connections in common (as an integer).
#   - If user_A or user_B is not in network, return False.



def connections_in_common(network, user_A, user_B):
    """
    Finds the common connection between user_A and user_B.

    Keyword Argument:
    network -- the gamer network data structure
    user_A --  a string containing the name of user_A
    user_B --  a string containing the name of user_B

    Returns:
    Returns integer value of the common connection between
    user_A and user_B if user_A and user_B are in network.
    """
    count = 0
    if user_A not in network or user_B not in network:
        return False
    connection_A = network[user_A]["Connections"]
    connection_B = network[user_B]["Connections"]
    for i in connection_A:
        if i in connection_B:
            count = count + 1
    return count

# ----------------------------------------------------------------------------- 
# path_to_friend(network, user_A, user_B): 
#   Finds a connections path from user_A to user_B. It has to be an existing 
#   path but it DOES NOT have to be the shortest path.
#   
# Arguments:
#   network: The network you created with create_data_structure. 
#   user_A:  String holding the starting username ("Abe")
#   user_B:  String holding the ending username ("Zed")
# 
# Return:
#   A list showing the path from user_A to user_B.
#   - If such a path does not exist, return None.
#   - If user_A or user_B is not in network, return None.
#
# Sample output:
#   >>> print path_to_friend(network, "Abe", "Zed")
#   >>> ['Abe', 'Gel', 'Sam', 'Zed']
#   This implies that Abe is connected with Gel, who is connected with Sam, 
#   who is connected with Zed.
# 
# NOTE:
#   You must solve this problem using recursion!
# 
# Hints: 
# - Be careful how you handle connection loops, for example, A is connected to B. 
#   B is connected to C. C is connected to B. Make sure your code terminates in 
#   that case.
# - If you are comfortable with default parameters, you might consider using one 
#   in this procedure to keep track of nodes already visited in your search. You 
#   may safely add default parameters since all calls used in the grading script 
#   will only include the arguments network, user_A, and user_B.




def path_to_friend(network, user_A, user_B,tracked = None):
    """
    Finds path to user_B from user_A's connections.
    
    Keyword Argument:
    network -- the gamer network data structure
    user_A -- name of the user_A
    user_B -- name of the user_B
    
    Returns:
    Returns list of user in path from user_A to user_B
    if user_A and user_B are in network and user_B is in
    the path of user_B. It will return None if no path is
    found.
    """
    if tracked is None:
        tracked = []
    if user_A not in network or user_B not in network:
        return None
  
    path = [user_A]
    connections = get_connections(network,user_A)

    if user_B in connections:
        path.append(user_B)
        return path
    else:
        tracked = tracked + [user_A]
        for i in connections:
            if i not in tracked:
                to_path = path_to_friend(network,i,user_B,tracked)
                if to_path != None:
                    path = path + to_path
                    return path
    return None       

# Make-Your-Own-Procedure (MYOP)
# ----------------------------------------------------------------------------- 
# Your MYOP should either perform some manipulation of your network data 
# structure (like add_new_user) or it should perform some valuable analysis of 
# your network (like path_to_friend). Don't forget to comment your MYOP. You 
# may give this procedure any name you want.



def remove_connection(network,user_A,user_B):
    """
    Removes user_B from connections of user_A if exists if both exists.

    Keyword Argument:
    network -- the gamer network data structure
    user_A -- name of the user_A
    user_B -- name of the user_B
    
    Returns:
    Following procedure doesn't remove anything.
    It will update the gamers network data structure
    by removing user_B from user_A's connections if
    it exists.
    """
    connections = get_connections(network,user_A)
    if user_B in connections:
        connections.remove(user_B)

   
def remove_game(network,user_A,game):
    """
    Removes the game from user_A's list of games if both exists.
    
    Keyword Argument:
    network -- the gamer network data structure
    user_A -- name of the user_A
    
    Returns:
    Following procedure will not return anything.
    It will remove game from the user_A's list
    of games if it exists.
    """
    games = get_games_liked(network,user_A)
    if game in games:
        games.remove(game)    
    

net = create_data_structure(example_input)
print net
print path_to_friend(net, "John", "Ollie")
print get_connections(net, "Debra")
print add_new_user(net, "Debra", []) 
print add_new_user(net, "Nick", ["Seven Schemers", "The Movie: The Game"]) # True
print get_connections(net, "Mercedes")
print get_games_liked(net, "John")
print add_connection(net, "John", "Freda")
print get_secondary_connections(net, "Mercedes")
print connections_in_common(net, "Mercedes", "John")
