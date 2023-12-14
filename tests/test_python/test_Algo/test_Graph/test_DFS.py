import pytest
from python.Algo.Graph.DFS import dfs
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

def test_dfs(example_graph):
    start_node = 'A'
    expected_order = ['A', 'B', 'D', 'E', 'H', 'C', 'F', 'G']
    result = dfs(example_graph, start_node)
    assert result == expected_order