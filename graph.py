# coding=gbk
import re
import numpy
import networkx as nx
import matplotlib.pyplot as plt

def main(my_ip=""):
    list = []
    with open('result.txt', 'r') as f:
        for line in f:
             separate= line.split(" ")
             if separate[0] == "通过最多":
                 list.append(my_ip)
             print(separate)
             if len(separate) > 1 and separate[-1] == '\n':
                 tail = separate[-2]
                 find=re.match(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",
                               tail)
                 if find:
                     list.append(tail)

    print("list", list)

    new_set = set(list)

    new_list = []
    for i in new_set:
        new_list.append(i)
    print("new_list",new_list)

    my_map = [[0 for j in range(len(new_list))] for i in range(len(new_list))]

    for i in range(len(list)-1):
        if list[i+1] != my_ip:
            my_map[new_list.index(list[i])][new_list.index(list[i+1])] = 1
            my_map[new_list.index(list[i+1])][new_list.index(list[i])] = 1

    for i in range(len(new_list)):
        my_map[i][i] = 1

    my_map = numpy.array(my_map)

    print("my_map", my_map)

    nodes = new_list
    edges = []
    for i in range(len(new_list)):
        for j in range(i+1, len(new_list)):
            if my_map[i][j] == 1:
                edges.append((new_list[i], new_list[j]))

    g = nx.Graph()
    g.add_nodes_from(nodes)
    g.add_edges_from(edges)

    #输出图的点数与变数
    print(g.number_of_nodes(), g.number_of_edges())

    nx.draw(g, with_labels=True)

    plt.show()
if __name__ == '__main__':
    main("192.168.137.1")
