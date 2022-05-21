
#Function to output the first node of a reversed linked list

def reverse(root):
    prev_node, curr_node = None, root
    while(curr_node != None):
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node, curr_node = curr_node, next_node
    return prev_node
