from const import *
from grid import *


shape_functions = [
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 - eta),
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 - eta),
        lambda eta, ksi: 0.25 * (1 + ksi) * (1 + eta),
        lambda eta, ksi: 0.25 * (1 - ksi) * (1 + eta)
    ]


def x_interpolation(element, node_id):
    x_interpolated = 0.0
    node_index = node_id - 1

    for zip_value in zip(shape_functions, element.nodes):
            x_interpolated += float(zip_value[0](tab_eta[node_index], tab_ksi[node_index])) * \
                              float(zip_value[1].x)

    return x_interpolated


def y_interpolation(element, node_id):
    y_interpolated = 0.0
    node_index = node_id - 1

    for zip_value in zip(shape_functions, element.nodes):
            y_interpolated += float(zip_value[0](tab_eta[node_index], tab_ksi[node_index])) * \
                              float(zip_value[1].y)

    return y_interpolated


n_derivatives_by_ksi = [
        lambda integration_point_index: - 0.25 * (1 - tab_eta[integration_point_index]),
        lambda integration_point_index: 0.25 * (1 - tab_eta[integration_point_index]),
        lambda integration_point_index: 0.25 * (1 + tab_eta[integration_point_index]),
        lambda integration_point_index: - 0.25 * (1 + tab_eta[integration_point_index])
]


n_derivatives_by_eta = [
        lambda integration_point_index: - 0.25 * (1 - tab_ksi[integration_point_index]),
        lambda integration_point_index: - 0.25 * (1 + tab_ksi[integration_point_index]),
        lambda integration_point_index: 0.25 * (1 + tab_ksi[integration_point_index]),
        lambda integration_point_index: 0.25 * (1 - tab_ksi[integration_point_index])
]


def derivative_n_derivative_ksi(shape_function_number, integration_point):
    # d N/ d ksi
    return n_derivatives_by_ksi[shape_function_number - 1](integration_point - 1)


def derivative_n_derivative_eta(shape_function_number, integration_point):
    # d N/ d eta
    return n_derivatives_by_eta[shape_function_number - 1](integration_point - 1)


def derivative_x_derivative_ksi(element, integration_point):
    # element [0,0] in Jacoby matrix
    derivative_value = 0.0
    for i in range(0, 4, 1):
        derivative_value += derivative_n_derivative_ksi(i + 1, integration_point) * element.nodes[i].x

    return derivative_value


def derivative_y_derivative_ksi(element, integration_point):
    # element [0,1] in Jacoby matrix
    derivative_value = 0.0
    for i in range(0, 4, 1):
        derivative_value += derivative_n_derivative_ksi(i + 1, integration_point) * element.nodes[i].y

    return derivative_value


def derivative_x_derivative_eta(element, integration_point):
    # element [1,0] in Jacoby matrix
    derivative_value = 0.0
    for i in range(0, 4, 1):
        derivative_value += derivative_n_derivative_eta(i + 1, integration_point) * element.nodes[i].x

    return derivative_value


def derivative_y_derivative_eta(element, integration_point):
    # element [1,1] in Jacoby matrix
    derivative_value = 0.0
    for i in range(0, 4, 1):
        derivative_value += derivative_n_derivative_eta(i + 1, integration_point) * element.nodes[i].y

    return derivative_value


def jacobian_matrix_determinant(element, integration_point):
    det_value = 0.0
    det_value += derivative_x_derivative_ksi(element, integration_point) * derivative_y_derivative_eta(element, integration_point)
    det_value -= derivative_x_derivative_eta(element, integration_point) * derivative_x_derivative_eta(element, integration_point)
    mes_input = read_file()
    #return det_value

    node_height = float(mes_input[2])
    node_length = float(mes_input[3])
    return (node_length*node_height)/4


def det_j():
    mes_input = read_file()

    node_height = float(mes_input[2])
    node_length = float(mes_input[3])
    return (node_length * node_height)/4


def jacobi_transformation_matrix(element):
    transformation_matrix = []
    for i in range(0, 4, 1):
        transformation_matrix.append([])
        detj = jacobian_matrix_determinant(element, i + 1)
        shape_function_number = i + 1

        transformation_matrix[i].append(derivative_y_derivative_eta(element, shape_function_number) / detj)
        transformation_matrix[i].append((- derivative_y_derivative_ksi(element, shape_function_number)) / detj)
        transformation_matrix[i].append((- derivative_x_derivative_eta(element, shape_function_number)) / detj)
        transformation_matrix[i].append(derivative_x_derivative_ksi(element, shape_function_number) / detj)
    return transformation_matrix


def jacobian_2d_main():
    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    node = create_nodes(nH, nL, node_height, node_length, 20)
    element = create_elements(1, 1, node)
    jacobian_2D = jacobi_transformation_matrix(element[0])
    return jacobian_2D


def main():

    jacobian_2d = jacobian_2d_main()

    for i in range(len(jacobian_2d)):
        print(jacobian_2d[i])


if __name__ == "__main__":
    main()
