#To Support the Gaming Network


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
Freda likes to play Starfleet Commander, Ninja Hamsters, Seahorse Adventures.\
Tom likes to play. "


# ----------------------------------------------------------------------------- 
# to_list (string_input): 
#   to_list takes a string as its input and returns the list with each sentenses seperated
# with a (,) commma. to_list uses a (".") to seperate the string from one line to another
# line. This procedure is used in creating a data structure as a helper procedure to
# create_data_structure.
#   
# Arguments: 
#   string_input: block of text containing the network information
#
# Return:
#   to_list returns input string converted to the list elements.

def to_list(string_input):
    output = []
    start_point = 0
    end_point = string_input.find(".")
    while end_point != -1:
         string = string_input[start_point:end_point]
         output.append(string)
         start_point = end_point + 1
         end_point = string_input.find(".",start_point)

    return output


# ----------------------------------------------------------------------------- 
# get_name (string_input): 
#   get_name finds the name from the string_input and returns it. This is used as a
# helper procedure in create_data_structure procedure.
#
# Arguments: 
#   string_input: block of text containing the network information
#
# Return:
#   get_name gets name of the user and returns None if no name is available.



def get_name(string_input):
  get_is =  string_input.find("is")
  get_likes =  string_input.find("likes")

  if "is connected" in string_input:
        return string_input[:get_is-1]
  elif "likes to play" in string_input:
        return string_input[:get_likes-1]
  else:
      return None


# ----------------------------------------------------------------------------- 
# get_name (string_input): 
#   get_name finds the name from the string_input and returns it. This is used as a
# helper procedure in create_data_structure procedure.
#
# Arguments: 
#   string_input: block of text containing the network information
#
# Return:
#   get_name gets name of the user and returns None if no name is available.


    
def connection(string_input):
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
    
def create_data_structure(string_input):
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
 
        

network  = create_data_structure(example_input)


def get_connections(network, user):
    if user in network:
       return network[user]["Connections"]
    else:
       return None


def add_connection(network, user_A, user_B):
    if user_A in network and user_B in network:
        connections = network[user_A]["Connections"]
        if user_B not in connections:
              connections.append(user_B)
    else:
        return False

    return network

def update_games(network,user,games):
    current_games = network[user]["Games"]
    for i in games:
        if i not in current_games:
            current_games.append(i)
    

def add_new_user(network, user, games = None):
    if games == None:
        games = []
        
    all_games = {}
    all_connections = {}
    if user not in network:
        network[user] = {}
        all_games["Games"] = []
        all_connections["Connections"] = []
        network[user].update(all_games)
        network[user].update(all_connections)
    else:
        update_games(network,user,games)
        
    return network


def get_secondary_connections(network,user):
    if user not in network:
        return None
    primary_connections = network[user]["Connections"]
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



def get_games_liked(network,user):
    if user in network:
        return network[user]["Games"]


    
def connections_in_common(network, user_A, user_B):
    count = 0
    if user_A not in network or user_B not in network:
        return False
    connection_A = network[user_A]["Connections"]
    connection_B = network[user_B]["Connections"]
    for i in connection_A:
        if i in connection_B:
            count = count + 1
    return count


def in_network(network, A):
    if A not in network:
        return False
    else:
        return True
    


def path_to_friend(network, user_A, user_B,tracked = None):
	# your RECURSIVE solution here!

  if tracked is None:
      tracked = []

  if not (in_network(network,user_A) and in_network(network,user_B)):
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
               # print to_path
                if to_path != None:
                    path = path + to_path
                    
                    return path
    
        
        return None
           
        
                    
                
        
	

    
