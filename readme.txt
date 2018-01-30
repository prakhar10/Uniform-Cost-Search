--------------------------------------------------------------------------------------------------------------------------------------------

Name : Prakhar Shankar Sapre

--------------------------------------------------------------------------------------------------------------------------------------------

UTA ID : XXXXXXXXXX

--------------------------------------------------------------------------------------------------------------------------------------------

Language : Python 2.7

--------------------------------------------------------------------------------------------------------------------------------------------
Code Structure :

The file find_route.py finds the shortest path between the source and destination given a weighted graph in the specific format.
Uniform cost search algorithm is implemented using Python. The different methods and their usage is explained below:

def get_data_dict(file_name) : This method takes file_name as the input and puts data in a dictionary. The key being the locations
and the value being list of all the nodes which are connected to the key location.

def expand_nodes(dictionary,fringe,visited_nodes,destination) - This method will take the fringe and extract its element one by one.
Simultaneously it will check if the location is visted or not. If the location is not visited then it will be expanded so all the locations
that are connected to it will be added to the fringe. The fringe is sorted according to the cost of each state. Recursively we will keep
expanding the nodes until we find the goal(destination). Once we find the goal state we will backtrack from the goal state to the source
location to find the optimized path.

def main(arg) - This is the main method which will get the command line arguments like the input file name, source and the destination name.

A list called visited_nodes is used to store the visited cities so that it is not repeated while storing the child details in the hashmap to
avoid overlap.

The file node.py is used as a entity class for storing data about each node. It has variables like - 
1. State - To store the state of the node.
2. Depth - To store the depth os the node.
3. Cost - To store the cumulative cost of the node.
4. Node - To store the parent node of the node being referenced.

---------------------------------------------------------------------------------------------------------------------------------------------
How to run the program:

If you are running it on command line then use the below command and keep all the files in the same directory:

python find_route.py input_file.txt source destination

---------------------------------------------------------------------------------------------------------------------------------------------