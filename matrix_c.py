from jacobian2D import *
from matrix_h import *


def n_by_nt(element, integration_point):
    array_to_return = []
    det = jacobian_matrix_determinant(element, integration_point)
    for i in range(0, 4, 1):
        array_to_return.append([])
        for j in range(0, 4, 1):
            array_to_return[i].append(c * ro * det * shape_fun(j, integration_point) * shape_fun(i, integration_point))

    return array_to_return


def shape_fun(shape_function_number, integration_point):
    return shape_functions[shape_function_number](tab_eta[integration_point - 1], tab_ksi[integration_point - 1])


def create_matrix_c(element):
    point_1 = n_by_nt(element, 1)
    point_2 = n_by_nt(element, 2)
    point_3 = n_by_nt(element, 3)
    point_4 = n_by_nt(element, 4)
    matrix = []
    for i in range(0, 4, 1):
        matrix.append([])
        for j in range(0, 4, 1):
            matrix[i].append(point_1[i][j] + point_2[i][j] + point_3[i][j] + point_4[i][j])
    return matrix


def create_matrix_c_main():
    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    node = create_nodes(nH, nL, node_height, node_length, 20)
    element = create_elements(1, 1, node)
    matrix = create_matrix_c(element[0])
    return matrix

def main():

    matrix = create_matrix_c_main()
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    main()