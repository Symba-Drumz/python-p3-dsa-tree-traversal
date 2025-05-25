import pytest
from lib.tree import Tree

def make_node(id, children=None):
    if children is None:
        children = []
    return {
        'tag_name': 'div',
        'id': id,
        'text_content': '',
        'children': children
    }

@pytest.fixture
def sample_tree():
    # Construct a sample tree:
    #       root
    #      /    \
    #   child1  child2
    #           /    \
    #      grand1   grand2
    grand1 = make_node('grand1')
    grand2 = make_node('grand2')
    child1 = make_node('child1')
    child2 = make_node('child2', [grand1, grand2])
    root = make_node('root', [child1, child2])
    return Tree(root)

def test_depth_first_found(sample_tree):
    tree = sample_tree
    node = tree.get_element_by_id('grand1', method='depth')
    assert node is not None
    assert node['id'] == 'grand1'

def test_depth_first_not_found(sample_tree):
    tree = sample_tree
    node = tree.get_element_by_id('nonexistent', method='depth')
    assert node is None

def test_breadth_first_found(sample_tree):
    tree = sample_tree
    node = tree.get_element_by_id('grand2', method='breadth')
    assert node is not None
    assert node['id'] == 'grand2'

def test_breadth_first_not_found(sample_tree):
    tree = sample_tree
    node = tree.get_element_by_id('nonexistent', method='breadth')
    assert node is None

def test_empty_tree():
    tree = Tree(None)
    assert tree.get_element_by_id('anyid', method='depth') is None
    assert tree.get_element_by_id('anyid', method='breadth') is None

def test_invalid_method(sample_tree):
    tree = sample_tree
    with pytest.raises(ValueError):
        tree.get_element_by_id('root', method='invalid')
