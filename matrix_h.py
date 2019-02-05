from jacobian2D import *


def dn1_dksi(integration_point):
    return -0.25 * (1 - tab_ksi[integration_point - 1])


def dn2_dksi(integration_point):
    return -0.25 * (1 + tab_ksi[integration_point - 1])


def dn3_dksi(integration_point):
    return 0.25 * (1 + tab_ksi[integration_point - 1])


def dn4_dksi(integration_point):
    return 0.25 * (1 - tab_ksi[integration_point - 1])


def dn1_deta(integration_point):
    return -0.25 * (1 - tab_eta[integration_point - 1])


def dn2_deta(integration_point):
    return 0.25 * (1 - tab_eta[integration_point - 1])


def dn3_deta(integration_point):
    return 0.25 * (1 + tab_eta[integration_point - 1])


def dn4_deta(integration_point):
    return -0.25 * (1 + tab_eta[integration_point - 1])


def dn1_dx(element, integration_point):
    value_to_return = derivative_y_derivative_eta(element, integration_point) * dn1_dksi(integration_point)
    value_to_return += derivative_y_derivative_ksi(element, integration_point) * dn1_deta(integration_point)
    return value_to_return


def dn2_dx(element, integration_point):
    value_to_return = derivative_y_derivative_eta(element, integration_point) * dn2_dksi(integration_point)
    value_to_return += derivative_y_derivative_ksi(element, integration_point) * dn2_deta(integration_point)
    return value_to_return


def dn3_dx(element, integration_point):
    value_to_return = derivative_y_derivative_eta(element, integration_point) * dn3_dksi(integration_point)
    value_to_return += derivative_y_derivative_ksi(element, integration_point) * dn3_deta(integration_point)
    return value_to_return


def dn4_dx(element, integration_point):
    value_to_return = derivative_y_derivative_eta(element, integration_point) * dn4_dksi(integration_point)
    value_to_return += derivative_y_derivative_ksi(element, integration_point) * dn4_deta(integration_point)
    return value_to_return


def dn1_dy(element, integration_point):
    value_to_return = derivative_x_derivative_ksi(element, integration_point) * dn1_deta(integration_point)
    value_to_return += derivative_x_derivative_eta(element, integration_point) * dn1_dksi(integration_point)
    return value_to_return


def dn2_dy(element, integration_point):
    value_to_return = derivative_x_derivative_ksi(element, integration_point) * dn2_deta(integration_point)
    value_to_return += derivative_x_derivative_eta(element, integration_point) * dn2_dksi(integration_point)
    return value_to_return


def dn3_dy(element, integration_point):
    value_to_return = derivative_x_derivative_ksi(element, integration_point) * dn3_deta(integration_point)
    value_to_return += derivative_x_derivative_eta(element, integration_point) * dn3_dksi(integration_point)
    return value_to_return


def dn4_dy(element, integration_point):
    value_to_return = derivative_x_derivative_ksi(element, integration_point) * dn4_deta(integration_point)
    value_to_return += derivative_x_derivative_eta(element, integration_point) * dn4_dksi(integration_point)
    return value_to_return


def dn_dx_dn_dx(element, integration_point):
    dn_array = []
    dn_array.append(dn1_dx(element, integration_point))
    dn_array.append(dn2_dx(element, integration_point))
    dn_array.append(dn3_dx(element, integration_point))
    dn_array.append(dn4_dx(element, integration_point))
    array_to_return = []
    for i in range(0, 4, 1):
        array_to_return.append([])
        for j in range(0, 4, 1):
            array_to_return[i].append(dn_array[i]*dn_array[j])

    return array_to_return


def dn_dy_dn_dy(element, integration_point):
    dn_array = []
    dn_array.append(dn1_dy(element, integration_point))
    dn_array.append(dn2_dy(element, integration_point))
    dn_array.append(dn3_dy(element, integration_point))
    dn_array.append(dn4_dy(element, integration_point))
    array_to_return = []
    for i in range(0, 4, 1):
        array_to_return.append([])
        for j in range(0, 4, 1):
            array_to_return[i].append(dn_array[i]*dn_array[j])

    return array_to_return


def dn_dx_dn_dx_detj(element, integration_point):
    array_to_return = dn_dx_dn_dx(element, integration_point)
    det = jacobian_matrix_determinant(element, integration_point)

    for i in range(len(array_to_return)):
        for j in range(len(array_to_return)):
            array_to_return[i][j] *= 1/det
    return array_to_return


def dn_dy_dn_dy_detj(element, integration_point):
    array_to_return = dn_dy_dn_dy(element, integration_point)
    det = jacobian_matrix_determinant(element, integration_point)

    for i in range(len(array_to_return)):
        for j in range(len(array_to_return)):
            array_to_return[i][j] *= 1/det
    return array_to_return


def k_dndx_dndy(element, integration_point):
    dn_dx = dn_dx_dn_dx_detj(element, integration_point)
    dn_dy = dn_dy_dn_dy_detj(element, integration_point)
    array_to_return = []
    for i in range(0, 4, 1):
        array_to_return.append([])
        for j in range(0, 4, 1):
            array_to_return[i].append(k*(dn_dx[i][j] + dn_dy[i][j]))

    return array_to_return


def create_matrix_h(element):
    point_1 = k_dndx_dndy(element, 1)
    point_2 = k_dndx_dndy(element, 2)
    point_3 = k_dndx_dndy(element, 3)
    point_4 = k_dndx_dndy(element, 4)
    matrix = []
    for i in range(0, 4, 1):
        matrix.append([])
        for j in range(0, 4, 1):
            matrix[i].append(point_1[i][j] + point_2[i][j] + point_3[i][j] + point_4[i][j])
    return matrix


def create_matrix_h_main():
    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    node = create_nodes(nH, nL, node_height, node_length, 20)
    element = create_elements(1, 1, node)
    matrix = create_matrix_h(element[0])
    return  matrix



def main():

    matrix = create_matrix_h_main()
    for i in range(len(matrix)):
        print(matrix[i])


if __name__ == "__main__":
    main()
