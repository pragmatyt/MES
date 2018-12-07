import csv


def read_file():
    mes_input = []
    with open('fem_input.csv') as xfile:
        my_reader = csv.reader(xfile)
        for row in my_reader:
            mes_input.append(row[0])
    return mes_input


class Node:
    def __init__(self, node_id, x, y, temp):
        self.node_id = node_id
        self.x = x
        self.y = y
        self.temp = temp


class Element:
    element_id = 0
    nodes = []

    def __init__(self, element_id):
        self.element_id = element_id
        self.nodes = []


def create_nodes(nH, nL, node_height, node_length, temp):
    node_id = 1
    node_array = []

    for i in range(int(nL) + 1):
        for j in range(int(nH) + 1):
            node_array.append(Node(node_id, i * float(node_length), j * float(node_height), temp))
            node_id += 1

    return node_array


def create_element_1x1(node_array):
    element_id = 1
    element_array = []

    element_array.append(Element(element_id=element_id))
    element_array[0].nodes.append(node_array[0])
    element_array[0].nodes.append(node_array[2])
    element_array[0].nodes.append(node_array[3])
    element_array[0].nodes.append(node_array[1])

    return element_array


def create_elements(nH, nL, node_array):
    element_id = 1
    element_array = []

    if nH == 1 and nL == 1:
        element_array = create_element_1x1(node_array)
        return element_array

    for i in range(int(nL)):
        for j in range(int(nH)):
            el_index = element_id - 1
            element_array.append(Element(element_id=element_id))

            element_array[el_index].nodes.append(node_array[el_index + int(i)])
            element_array[el_index].nodes.append(node_array[el_index + int(nH) + int(i) + 1])
            element_array[el_index].nodes.append(node_array[el_index + int(nH) + int(i) + 2])
            element_array[el_index].nodes.append(node_array[el_index + int(i) + 1])

            element_id += 1

    return element_array


def main():

    mes_input = read_file()
    print("mes input from file:")
    for i in range(len(mes_input)):
        print(mes_input[i])

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    node_array = create_nodes(nH, nL, node_height, node_length, 20)
    element_array = create_elements(nH, nL, node_array)

    print("Nodes:")
    for i in range(len(node_array)):
        print(node_array[i].node_id, node_array[i].x, node_array[i].y)

    print("Elements")
    for i in range(len(element_array)):
        print(element_array[i].element_id)
        nodes = "Nodes id: "
        for j in range(0, 4, 1):
            nodes += str((element_array[i].nodes[j].node_id)) + " "
        print(nodes)

    pass


if __name__ == "__main__":
    main()
