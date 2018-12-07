import unittest
from grid import *


class TestMes1(unittest.TestCase):

    def test_init_node(self):
        self.assertIsNotNone(Node(1, 1, 1, 1))

    def test_init_element(self):
        self.assertIsNotNone(Element(1))

    # TESTS: create_nodes() amount of nodes

    def test_create_4_nodes(self):
        self.assertEqual(4, len(create_nodes(1, 1, 1, 1, 20)))

    def test_create_nodes_for_2_elements_2x1(self):
        self.assertEqual(6, len(create_nodes(2, 1, 1, 1, 20)))

    def test_create_nodes_for_nH2_nL2(self):
        self.assertEqual(9, len(create_nodes(2, 2, 1, 1, 20)))

    def test_create_nodes_for_nH3_nL3(self):
        self.assertEqual(16, len(create_nodes(3, 3, 1, 1, 20)))

    def test_create_nodes_for_nH7_nL3(self):
        self.assertEqual(32, len(create_nodes(7, 3, 1, 1, 20)))

    # TESTS: create_nodes() grid 2x2 nodes id

    def test_create_nodes_2x2_node1_id(self):
        node_to_test = create_nodes(2, 2, 1, 1, 20)
        self.assertEqual(1, node_to_test[0].node_id)

    def test_create_nodes_2x2_node2_id(self):
        node_to_test = create_nodes(2, 2, 1, 1, 20)
        self.assertEqual(2, node_to_test[1].node_id)

    def test_create_nodes_2x2_node3_id(self):
        node_to_test = create_nodes(2, 2, 1, 1, 20)
        self.assertEqual(3, node_to_test[2].node_id)

    def test_create_nodes_2x2_node4_id(self):
        node_to_test = create_nodes(2, 2, 1, 1, 20)
        self.assertEqual(4, node_to_test[3].node_id)

    def test_create_nodes_2x2_node5_id(self):
        node_to_test = create_nodes(2, 2, 1, 1, 20)
        self.assertEqual(5, node_to_test[4].node_id)

    # TESTS: create_nodes() grid 3x3 nodes id

    def test_create_nodes_3x3_node4_id(self):
        node_to_test = create_nodes(3, 3, 1, 1, 20)
        self.assertEqual(4, node_to_test[3].node_id)

    def test_create_nodes_3x3_node6_id(self):
        node_to_test = create_nodes(3, 3, 1, 1, 20)
        self.assertEqual(6, node_to_test[5].node_id)

    def test_create_nodes_3x3_node16_id(self):
        node_to_test = create_nodes(3, 3, 1, 1, 20)
        self.assertEqual(16, node_to_test[15].node_id)

    # TESTS: create_nodes() grid 2x2 nodes x,y coordinates

    def test_create_nodes_2x2_height_025_length_025_node1_x(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0, node_to_test[0].x)

    def test_create_nodes_2x2_height_025_length_025_node1_y(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0, node_to_test[0].y)

    def test_create_nodes_2x2_height_025_length_025_node2_x(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0, node_to_test[1].x)

    def test_create_nodes_2x2_height_025_length_025_node2_y(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.25, node_to_test[1].y)

    def test_create_nodes_2x2_height_025_length_025_node3_x(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0, node_to_test[2].x)

    def test_create_nodes_2x2_height_025_length_025_node3_y(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.5, node_to_test[2].y)

    def test_create_nodes_2x2_height_025_length_025_node4_x(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.25, node_to_test[3].x)

    def test_create_nodes_2x2_height_025_length_025_node5_y(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.25, node_to_test[4].y)

    def test_create_nodes_2x2_height_025_length_025_node6_x(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.25, node_to_test[5].x)

    def test_create_nodes_2x2_height_025_length_025_node7_x(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.5, node_to_test[6].x)

    def test_create_nodes_2x2_height_025_length_025_node9_x(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.5, node_to_test[8].x)

    def test_create_nodes_2x2_height_025_length_025_node9_y(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        self.assertEqual(0.5, node_to_test[8].y)

    # TESTS: create_elements()

    def test_create_one_element(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        self.assertIsNotNone(create_elements(1, 1, node_to_test))

    # TESTS: create_elements() grid 1x1 nodes id

    def test_create_elements_1x1_node1_id(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(1, element_to_test[0].nodes[0].node_id)

    def test_create_elements_1x1_node2_id(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(3, element_to_test[0].nodes[1].node_id)

    def test_create_elements_1x1_node3_id(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(4, element_to_test[0].nodes[2].node_id)

    def test_create_elements_1x1_node4_id(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(2, element_to_test[0].nodes[3].node_id)

    # TESTS: create_elements() grid 2x2 element 1 nodes id

    def test_create_elements_2x2_el1_node1_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(1, element_to_test[0].nodes[0].node_id)

    def test_create_elements_2x2_el1_node2_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(4, element_to_test[0].nodes[1].node_id)

    def test_create_elements_2x2_el1_node3_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(5, element_to_test[0].nodes[2].node_id)

    def test_create_elements_2x2_el1_node4_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(2, element_to_test[0].nodes[3].node_id)

    # TESTS: create_elements() grid 2x2 element 2 nodes id

    def test_create_elements_2x2_el2_node1_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(2, element_to_test[1].nodes[0].node_id)

    def test_create_elements_2x2_el2_node2_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(5, element_to_test[1].nodes[1].node_id)

    def test_create_elements_2x2_el2_node3_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(6, element_to_test[1].nodes[2].node_id)

    def test_create_elements_2x2_el2_node4_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(3, element_to_test[1].nodes[3].node_id)

    # TESTS: create_elements() grid 2x2 element 3 nodes id

    def test_create_elements_2x2_el3_node1_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(4, element_to_test[2].nodes[0].node_id)

    def test_create_elements_2x2_el3_node2_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(7, element_to_test[2].nodes[1].node_id)

    def test_create_elements_2x2_el3_node3_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(8, element_to_test[2].nodes[2].node_id)

    def test_create_elements_2x2_el3_node4_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(5, element_to_test[2].nodes[3].node_id)

    # TESTS: create_elements() grid 2x2 element 4 nodes id

    def test_create_elements_2x2_el4_node1_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(5, element_to_test[3].nodes[0].node_id)

    def test_create_elements_2x2_el4_node3_id(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(9, element_to_test[3].nodes[2].node_id)

    # TESTS: create_elements() grid 3x3 element 3 nodes id

    def test_create_elements_3x3_el3_node1_id(self):
        node_to_test = create_nodes(3, 3, 0.25, 0.25, 20)
        element_to_test = create_elements(3, 3, node_to_test)
        self.assertEqual(3, element_to_test[2].nodes[0].node_id)

    def test_create_elements_3x3_el3_node2_id(self):
        node_to_test = create_nodes(3, 3, 0.25, 0.25, 20)
        element_to_test = create_elements(3, 3, node_to_test)
        self.assertEqual(7, element_to_test[2].nodes[1].node_id)

    # TESTS: create_elements() grid 3x3 element 4 nodes id

    def test_create_elements_3x3_el4_node3_id(self):
        node_to_test = create_nodes(3, 3, 0.25, 0.25, 20)
        element_to_test = create_elements(3, 3, node_to_test)
        self.assertEqual(10, element_to_test[3].nodes[2].node_id)

    def test_create_elements_3x3_el4_node4_id(self):
        node_to_test = create_nodes(3, 3, 0.25, 0.25, 20)
        element_to_test = create_elements(3, 3, node_to_test)
        self.assertEqual(6, element_to_test[3].nodes[3].node_id)

    # TESTS: create_elements() grid 3x3 element 5 nodes id

    def test_create_elements_3x3_el5_node4_id(self):
        node_to_test = create_nodes(3, 3, 0.25, 0.25, 20)
        element_to_test = create_elements(3, 3, node_to_test)
        self.assertEqual(7, element_to_test[4].nodes[3].node_id)


if __name__ == '__main__':
    unittest.main()
