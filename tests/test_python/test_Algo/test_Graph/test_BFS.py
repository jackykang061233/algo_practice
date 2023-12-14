import pytest
from python.Algo.Graph.BFS import bfs

@pytest.fixture
def example_graph():
    return {
        'A': {'B', 'C'},
        'B': {'A', 'D', 'E'},
        'C': {'A', 'F', 'G'},
        'D': {'B'},
        'E': {'B', 'H'},
        'F': {'C'},
        'G': {'C'},
        'H': {'E'}
    }

def test_bfs(example_graph):
    start_node = 'A'
    expected_order = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    result = bfs(example_graph, start_node)
    assert result == expected_order
