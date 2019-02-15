from jacobian2D import *


def create_vector_p(element):
    mes_input = read_file()

    nH = int(mes_input[0])
    nL = int(mes_input[1])

    node_height = mes_input[2]
    node_length = mes_input[3]

    det_h = float(node_height) / 2
    det_l = float(node_length) / 2

    vector = []
    for i in range(0, 4, 1):
        vector.append(0)

    if element.element_id in range(1, nH * (nL - 1) + 1 + 1, nH):
        vector = add_side_12(vector, det_l)
    if element.element_id in range(nH * (nL - 1) + 1, nH * nL + 1, 1):
        vector = add_side_23(vector, det_h)
    if element.element_id in range(nH, nH * nL + nL, nL):
        vector = add_side_34(vector, det_l)
    if element.element_id in range(1, nH + 1, 1):
        vector = add_side_41(vector, det_h)
    return vector


def add_side_12(vector, det_l):
    local_eta = -1
    local_ksi = [-sqrt3, sqrt3, 0, 0]

    shape_functions_bc = [
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 - eta),
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 - eta),
        lambda eta, ksi: 0,
        lambda eta, ksi: 0
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta, local_ksi[integration_point - 1])

    for i in range(0, 4, 1):
        vector[i] += alfa * det_l * shape_fun_bc(i, 1) * t_alfa
        vector[i] += alfa * det_l * shape_fun_bc(i, 2) * t_alfa

    return vector


def add_side_23(vector, det_h):
    local_ksi = 1
    local_eta = [-sqrt3, sqrt3, 0, 0]

    shape_functions_bc = [
        lambda eta, ksi: 0,
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 - eta),
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 + eta),
        lambda eta, ksi: 0
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta[integration_point - 1], local_ksi)

    for i in range(0, 4, 1):
        vector[i] += alfa * det_h * shape_fun_bc(i, 1) * t_alfa
        vector[i] += alfa * det_h * shape_fun_bc(i, 2) * t_alfa

    return vector


def add_side_34(vector, det_l):
    local_eta = 1
    local_ksi = [sqrt3, -sqrt3, 0, 0]

    shape_functions_bc = [
        lambda eta, ksi: 0,
        lambda eta, ksi: 0,
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 + eta),
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 + eta)
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta, local_ksi[integration_point - 1])

    for i in range(0, 4, 1):
        vector[i] += alfa * det_l * shape_fun_bc(i, 1) * t_alfa
        vector[i] += alfa * det_l * shape_fun_bc(i, 2) * t_alfa

    return vector


def add_side_41(vector, det_h):
    local_ksi = -1
    local_eta = [sqrt3, -sqrt3, 0, 0]

    shape_functions_bc = [
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 - eta),
        lambda eta, ksi: 0,
        lambda eta, ksi: 0,
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 + eta)
    ]

    def shape_fun_bc(shape_function_number, integration_point):
        return shape_functions_bc[shape_function_number](local_eta[integration_point - 1], local_ksi)

    for i in range(0, 4, 1):
        vector[i] += alfa * det_h * shape_fun_bc(i, 1) * t_alfa
        vector[i] += alfa * det_h * shape_fun_bc(i, 2) * t_alfa

    return vector


def create_vector_p_main():
    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    node = create_nodes(nH, nL, node_height, node_length, 20)
    element = create_elements(nH, nL, node)
    vector = create_vector_p(element[3])
    return vector


def main():

    vector = create_vector_p_main()
    for i in range(len(vector)):
        print(vector[i])


if __name__ == "__main__":
    main()