import unittest
from matrix_h import *


class TestMartixH(unittest.TestCase):

    def test_dn1_dksi_ip1(self):
        self.assertAlmostEqual(-0.394337, dn1_dksi(1), None, None, 0.000001)

    def test_dn2_dksi_ip2(self):
        self.assertAlmostEqual(-0.394337, dn2_dksi(2), None, None, 0.000001)

    def test_dn3_dksi_ip3(self):
        self.assertAlmostEqual(0.394337, dn3_dksi(3), None, None, 0.000001)

    def test_dn4_dksi_ip4(self):
        self.assertAlmostEqual(0.394337, dn4_dksi(4), None, None, 0.000001)

    def test_dn1_deta_ip3(self):
        self.assertAlmostEqual(-0.105662, dn1_deta(3), None, None, 0.000001)

    def test_dn2_deta_ip3(self):
        self.assertAlmostEqual(0.105662, dn2_deta(3), None, None, 0.000001)

    def test_dn3_deta_ip3(self):
        self.assertAlmostEqual(0.394337, dn3_deta(3), None, None, 0.000001)

    def test_dn4_deta_ip3(self):
        self.assertAlmostEqual(-0.394337, dn4_deta(3), None, None, 0.000001)

    def test_dn1_dx_ip1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(-31.55, dn1_dx(element_to_test[0], 1), None, None, 0.01)

    def test_dn1_dx_ip3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(-8.45, dn1_dx(element_to_test[0], 3), None, None, 0.01)

    def test_dn2_dx_ip1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(31.55, dn2_dx(element_to_test[0], 1), None, None, 0.01)

    def test_dn3_dx_ip1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(8.45, dn3_dx(element_to_test[0], 1), None, None, 0.01)

    def test_dn4_dx_ip4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(-31.55, dn4_dx(element_to_test[0], 4), None, None, 0.01)

    def test_dn1_dy_ip3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(-8.45, dn1_dy(element_to_test[0], 3), None, None, 0.01)

    def test_dn2_dy_ip1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(-8.45, dn2_dy(element_to_test[0], 1), None, None, 0.01)

    def test_dn3_dy_ip1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(8.45, dn3_dy(element_to_test[0], 1), None, None, 0.01)

    def test_dn4_dy_ip4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(31.55, dn4_dy(element_to_test[0], 4), None, None, 0.01)

    def test_dn_dx_dn_dx_00(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(995.21, dn_dx_dn_dx(element_to_test[0], 1)[0][0], None, None, 0.1)

    def test_dn_dx_dn_dx_33(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(71.5, dn_dx_dn_dx(element_to_test[0], 1)[3][3], None, None, 0.1)

    def test_dn_dy_dn_dy_00(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(995.21, dn_dy_dn_dy(element_to_test[0], 1)[0][0], None, None, 0.1)

    def test_dn_dy_dn_dy_01(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(266.667, dn_dy_dn_dy(element_to_test[0], 1)[0][1], None, None, 0.1)

    def test_dn_dy_dn_dy_33(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(995.21, dn_dy_dn_dy(element_to_test[0], 1)[3][3], None, None, 0.1)

    def test_dn_dx_dn_dx_detj_00(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.1555, dn_dx_dn_dx_detj(element_to_test[0], 1)[0][0], None, None, 0.1)

    def test_dn_dx_dn_dx_detj_03(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.0417, dn_dx_dn_dx_detj(element_to_test[0], 1)[0][3], None, None, 0.0001)

    def test_dn_dy_dn_dy_detj_00(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.1555, dn_dy_dn_dy_detj(element_to_test[0], 1)[0][0], None, None, 0.1)

    def test_dn_dy_dn_dy_detj_03(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(-0.0112, dn_dy_dn_dy_detj(element_to_test[0], 2)[0][3], None, None, 0.0001)

    def test_k_dndx_dndy_00(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(9.33, k_dndx_dndy(element_to_test[0], 1)[0][0], None, None, 0.001)

    def test_k_dndx_dndy_33(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(5, k_dndx_dndy(element_to_test[0], 1)[3][3], None, None, 0.001)

    def test_k_dndx_dndy_10(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(-3.42, k_dndx_dndy(element_to_test[0], 1)[1][0], None, None, 0.01)

    def test_create_matrix_h_00(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(20, create_matrix_h(element_to_test[0])[0][0], None, None, 0.01)

    def test_create_matrix_main(self):
        self.assertAlmostEqual(20, create_matrix_h_main()[0][0], None, None, 0.01)


if __name__ == '__main__':
    unittest.main()
