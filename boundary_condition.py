from matrix_h import *
from jacobian2D import *

shape_functions_bc = [
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 - eta),
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 - eta),
        lambda eta, ksi: 0,
        lambda eta, ksi: 0
    ]


def add_boundary_condtion(element, matrix):
    mes_input = read_file()

    nH = int(mes_input[0])
    nL = int(mes_input[1])
    node_height = mes_input[2]
    node_length = mes_input[3]

    det_h = float(node_height)/2
    det_l = float(node_length)/2

    if element.element_id in range(1, nH*(nL-1)+1+1, nH):
        matrix = add_side_12(matrix, det_l)
    if element.element_id in range(nH*(nL-1)+1, nH*nL + 1, 1):
        matrix = add_side_23(matrix, det_h)
    if element.element_id in range(nH, nH*nL+nL, nL):
        matrix = add_side_34(matrix, det_l)
    if element.element_id in range(1, nH + 1, 1):
        matrix = add_side_41(matrix, det_h)
    return matrix


def add_side_12(matrix, det_l):
    local_eta = -1
    local_ksi = [-sqrt3, sqrt3, 0, 0]
    #print("side 12")
    shape_functions_bc = [
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 - eta),
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 - eta),
        lambda eta, ksi: 0,
        lambda eta, ksi: 0
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta, local_ksi[integration_point - 1])

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            matrix[i][j] += alfa * det_l * float(shape_fun_bc(i, 1)) * float(shape_fun_bc(j, 1))
            matrix[i][j] += alfa * det_l * shape_fun_bc(i, 2) * shape_fun_bc(j, 2)

    return matrix


def add_side_23(matrix, det_h):
    local_ksi = 1
    local_eta = [-sqrt3, sqrt3, 0, 0]
    #print("side 23")
    shape_functions_bc = [
        lambda eta, ksi: 0,
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 - eta),
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 + eta),
        lambda eta, ksi: 0
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta[integration_point - 1], local_ksi)

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            # x = alfa * det_h * shape_fun_bc(i, 1) * shape_fun_bc(j, 1)
            # #print("x" + str(x))
            # matrix[i][j] += "a"
            #
            # y = alfa * det_h * shape_fun_bc(i, 2) * shape_fun_bc(j, 2)
            # print("x + y" + str(x+y))
            # matrix[i][j] += "b"
            # matrix[i][j] += x + y
            matrix[i][j] += alfa * det_h * shape_fun_bc(i, 1) * shape_fun_bc(j, 1)
            matrix[i][j] += alfa * det_h * shape_fun_bc(i, 2) * shape_fun_bc(j, 2)

    return matrix


def add_side_34(matrix, det_l):
    local_eta = 1
    local_ksi = [sqrt3, -sqrt3, 0, 0]
    #print("side 34")
    shape_functions_bc = [
        lambda eta, ksi: 0,
        lambda eta, ksi: 0,
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 + eta),
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 + eta)
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta, local_ksi[integration_point - 1])

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            matrix[i][j] +=(alfa * det_l * shape_fun_bc(i, 1) * shape_fun_bc(j, 1))
            matrix[i][j] += alfa * det_l * shape_fun_bc(i, 2) * shape_fun_bc(j, 2)

    return matrix


def add_side_41(matrix, det_h):
    local_ksi = -1
    local_eta = [sqrt3, -sqrt3, 0, 0]
    #print("side 41")
    shape_functions_bc = [
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 - eta),
        lambda eta, ksi: 0,
        lambda eta, ksi: 0,
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 + eta)
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta[integration_point - 1], local_ksi)

    for i in range(0, 4, 1):
        for j in range(0, 4, 1):
            matrix[i][j] += (alfa * det_h * shape_fun_bc(i, 1) * shape_fun_bc(j, 1))
            matrix[i][j] += alfa * det_h * shape_fun_bc(i, 2) * shape_fun_bc(j, 2)

    return matrix


def main():

    matrix = []
    for i in range(0, 4, 1):
        matrix.append([])
        for j in range(0, 4, 1):
            matrix[i].append(0)
    add_side_12(matrix, 0.0125)
    add_side_23(matrix, 0.0125)
    add_side_34(matrix, 0.0125)
    add_side_41(matrix, 0.0125)
    for i in range(len(matrix)):
        print(matrix[i])

if __name__ == "__main__":
    main()