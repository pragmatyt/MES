from matrix_h import *


def global_h():
    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]
    global_h = []
    nodes_ammount = (int(nL) + 1) * (int(nH) + 1)
    for i in range(nodes_ammount):
        global_h.append([])
        for j in range(nodes_ammount):
            global_h[i].append(0)
    return global_h


def create_global_matrix_h():

    global_martix_h = global_h()

    mes_input = read_file()
    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    nodes = create_nodes(nH, nL, node_height, node_length, 20)
    elements = create_elements(nH, nL, nodes)

    for i in range(len(elements)):
        element = elements[i]
        matrix = create_matrix_h(elements[i])
        for row in range(len(matrix)):
            for j in range(len(matrix)):
                #print("row: " + str(row) + " j: " + str(j))
                #print("row: " + str(element.nodes[row].node_id - 1) + " j: " + str(element.nodes[j].node_id - 1))
                global_martix_h[element.nodes[row].node_id - 1][element.nodes[j].node_id - 1] += matrix[row][j]*0.82

    return global_martix_h


def main():

    matrix = create_global_matrix_h()
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    main()