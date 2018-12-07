import unittest
from grid import *
from jacobian2D import *


class TestJakobian2D(unittest.TestCase):

    # TEST: test shape function
    '''
    def test_shape_function_1(self):
        self.assertAlmostEqual(0.622008, shape_function(1, tab_eta[0], tab_ksi[0]), None, None, 0.00001)

    def test_shape_function_2(self):
        self.assertAlmostEqual(0.166666, shape_function(2, tab_eta[0], tab_ksi[0]), None, None, 0.00001)

    def test_shape_function_3(self):
        self.assertAlmostEqual(0.044658, shape_function(3, tab_eta[0], tab_ksi[0]), None, None, 0.00001)

    def test_shape_function_4(self):
        self.assertAlmostEqual(0.166666, shape_function(4,tab_eta[0], tab_ksi[0]), None, None, 0.00001)
    '''
    # TEST: test interpolation for x

    def test_x_interpolation_for_node1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, x_interpolation(element_to_test[0], 1), None, None, 0.00001)

    def test_x_interpolation_for_node2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, x_interpolation(element_to_test[0], 2), None, None, 0.00001)

    def test_x_interpolation_for_node3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, x_interpolation(element_to_test[0], 3), None, None, 0.00001)

    def test_x_interpolation_for_node4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, x_interpolation(element_to_test[0], 4), None, None, 0.00001)

    # TEST: test interpolation for y

    def test_y_interpolation_for_node1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, y_interpolation(element_to_test[0], 1), None, None, 0.00001)

    def test_y_interpolation_for_node2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, y_interpolation(element_to_test[0], 2), None, None, 0.00001)

    def test_y_interpolation_for_node3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, y_interpolation(element_to_test[0], 3), None, None, 0.00001)

    def test_y_interpolation_for_node4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, y_interpolation(element_to_test[0], 4), None, None, 0.00001)

    # TEST: test derivative n derivative eta

    def test_derivative_n_derivative_eta_shape_function_1_integration_point_1(self):
        self.assertAlmostEqual(-0.394337, derivative_n_derivative_eta(1, 1), None, None, 0.00001)

    def test_derivative_n_derivative_eta_shape_function_1_integration_point_2(self):
        self.assertAlmostEqual(-0.105662, derivative_n_derivative_eta(1, 2), None, None, 0.00001)

    def test_derivative_n_derivative_eta_shape_function_1_integration_point_3(self):
        self.assertAlmostEqual(-0.105662, derivative_n_derivative_eta(1, 3), None, None, 0.00001)

    def test_derivative_n_derivative_eta_shape_function_1_integration_point_4(self):
        self.assertAlmostEqual(-0.394337, derivative_n_derivative_eta(1, 4), None, None, 0.00001)

    def test_derivative_n_derivative_eta_shape_function_3_integration_point_1(self):
        self.assertAlmostEqual(0.105662, derivative_n_derivative_eta(3, 1), None, None, 0.00001)

    def test_derivative_n_derivative_eta_shape_function_4_integration_point_4(self):
        self.assertAlmostEqual(0.394337, derivative_n_derivative_eta(4, 4), None, None, 0.00001)

    # TEST: test derivative n derivative ksi

    def test_derivative_n_derivative_ksi_shape_function_1_integration_point_1(self):
        self.assertAlmostEqual(-0.394337, derivative_n_derivative_ksi(1, 1), None, None, 0.00001)

    def test_derivative_n_derivative_ksi_shape_function_1_integration_point_2(self):
        self.assertAlmostEqual(-0.394337, derivative_n_derivative_ksi(1, 2), None, None, 0.00001)

    def test_derivative_n_derivative_ksi_shape_function_1_integration_point_3(self):
        self.assertAlmostEqual(-0.105662, derivative_n_derivative_ksi(1, 3), None, None, 0.00001)

    def test_derivative_n_derivative_ksi_shape_function_1_integration_point_4(self):
        self.assertAlmostEqual(-0.105662, derivative_n_derivative_ksi(1, 4), None, None, 0.00001)

    def test_derivative_n_derivative_ksi_shape_function_2_integration_point_2(self):
        self.assertAlmostEqual(0.394337, derivative_n_derivative_ksi(2, 2), None, None, 0.00001)

    def test_derivative_n_derivative_ksi_shape_function_4_integration_point_4(self):
        self.assertAlmostEqual(-0.394337, derivative_n_derivative_ksi(4, 4), None, None, 0.00001)

    # TEST: test derivative shape functions that are used to build of Jacoby matrix

    def test_derivative_x_derivative_ksi_integration_point_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.0125, derivative_x_derivative_ksi(element_to_test[0], 1), None, None, 0.00001)

    def test_derivative_y_derivative_ksi_integration_point_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0, derivative_y_derivative_ksi(element_to_test[0], 1), None, None, 0.00001)

    def est_derivative_x_derivative_eta_integration_point_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0, derivative_x_derivative_eta(element_to_test[0], 1), None, None, 0.00001)

    def test_derivative_y_derivative_eta_integration_point_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.0125, derivative_y_derivative_eta(element_to_test[0], 1), None, None, 0.00001)

    # TEST: test Jacobian matrix determinant

    def test_jacobian_matrix_determinant_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, jacobian_matrix_determinant(element_to_test[0], 1), None, None, 0.00000001)

    def test_jacobian_matrix_determinant_2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, jacobian_matrix_determinant(element_to_test[0], 2), None, None, 0.00000001)

    def test_jacobian_matrix_determinant_3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, jacobian_matrix_determinant(element_to_test[0], 3), None, None, 0.00000001)

    def test_jacobian_matrix_determinant_4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, jacobian_matrix_determinant(element_to_test[0], 4), None, None, 0.00000001)
    
    # TEST: test jacobi transformation matrix

    def test_jacobi_transformation_matrix_el_0_0(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(80, jacobi_transformation_matrix(element_to_test[0])[0][0])

    def test_jacobi_transformation_matrix_el_0_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0, jacobi_transformation_matrix(element_to_test[0])[0][1])

    def test_jacobi_transformation_matrix_el_3_3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(80, jacobi_transformation_matrix(element_to_test[0])[3][3])



if __name__ == '__main__':
    unittest.main()
