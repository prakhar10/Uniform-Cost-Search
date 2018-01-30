import sys
import node


def get_data_dict(file_name):
    dictionary = {}
    data_file = open(file_name,'r')

    for line in data_file:
        if line.strip() == "END OF INPUT":
            break
        input_array = line.split(" ")
        node_list = dictionary.get(input_array[0], [])
        node_list.append(node.Node(input_array[1], 0, input_array[2], None))
        dictionary[input_array[0]] = node_list

    data_file.close()
    data_file = open(file_name,'r')
    for line in data_file:
        if line.strip() == "END OF INPUT":
            break
        input_array = line.split(" ")
        node_list = dictionary.get(input_array[1], [])
        node_list.append(node.Node(input_array[0], 0, input_array[2], None))
        dictionary[input_array[1]] = node_list

    data_file.close()
    return dictionary


def get_node_cost(node):
    return node.get_cost


def expand_nodes(data_dictionary,fringe,visited_nodes,destination):

    if len(fringe) is not 0:
        node = fringe[0]
        fringe.remove(node)
        if node.get_state() not in visited_nodes:
            node_list = data_dictionary.get(node.get_state())

            #If we find the goal state then we backtrack to the source and print the path and distance
            if node.get_state() == destination:
                backtrack = []
                backtrack.append(node)
                while node.get_node() is not None:
                    node = node.get_node()
                    backtrack.append(node)

                backtrack.reverse()
                total_distance_node = backtrack[-1]
                count = 0
                print("Distance:" + str(total_distance_node.get_cost()) +" km")
                print("Route:")
                for child in backtrack:
                    if count < len(backtrack)-1:
                        count = count + 1
                        print(child.get_state() + " to " + backtrack[count].get_state() + " , " + str(backtrack[count].get_cost() - child.get_cost()) + " km")

                return

            #If the current node is not the goal then we expand the node that we took out from fringe and update the values in the child_nodes
            if node.get_state() != destination:

                for child_node in node_list:
                    child_node.set_depth(node.get_depth()+1)
                    child_node.set_cost(int(child_node.get_cost()) + node.get_cost())
                    child_node.set_node(node)
                    fringe.append(child_node)

                fringe = sorted(fringe, key=lambda nodes: nodes.cost)

            visited_nodes.append(node.get_state())
        expand_nodes(data_dictionary,fringe,visited_nodes,destination)
    else:
        print("Distance: Infinity")
        print("Route: None")


def main(arg):
    fringe = []
    visited_nodes = []
    data_dictionary = get_data_dict(arg[1])
    fringe.append(node.Node(arg[2]))
    expand_nodes(data_dictionary,fringe,visited_nodes,arg[3])


main(sys.argv)

