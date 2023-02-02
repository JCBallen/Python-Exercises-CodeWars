import os
os.system("cls")


class Node:
    def __init__(self, next=None):
        self.next = next


node1 = Node()
node2 = Node()
node3 = Node()
node4 = Node()
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2


def loop_size(node):
    node_list=[node]
    aux=node
    while True:
        if aux.next not in node_list:
            node_list.append(aux.next)
            aux=aux.next
        else:
            initial_loop_node=aux.next
            break
    node_index=node_list.index(initial_loop_node)
    return len(node_list)-node_index


print(loop_size(node1))
