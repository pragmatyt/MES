from vector_p import *


def global_vector_p():
    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]
    global_p = []
    nodes_ammount = (int(nL) + 1) * (int(nH) + 1)
    for i in range(nodes_ammount):
        global_p.append([0])
    return global_p


def create_global_p():
    global_p = global_vector_p()

    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    node = create_nodes(nH, nL, node_height, node_length, 20)
    elements = create_elements(nH, nL, node)

    for i in range(len(elements)):
        element = elements[i]
        #print(i)
        vector = create_vector_p(elements[i])
        for j in range(len(vector)):
            #print(vector[j])
            print("i " + str(i))

            global_p[element.nodes[j].node_id - 1] = global_p[element.nodes[j].node_id - 1] + vector[j]
            #global_p[x] += vector[j]

    #vector = create_vector_p(elements[0])
    return global_p


def main():

    matrix = create_global_p()
    #matrix = global_vector_p()
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    main()