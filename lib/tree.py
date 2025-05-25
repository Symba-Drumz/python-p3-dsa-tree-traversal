class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id, method='depth'):
    if not self.root:
      return None

    if method == 'depth':
      # Depth-first traversal to find node by id
      def dfs(node):
        if node['id'] == id:
          return node
        for child in node['children']:
          found = dfs(child)
          if found:
            return found
        return None
      return dfs(self.root)

    elif method == 'breadth':
      # Breadth-first traversal to find node by id
      nodes_to_visit = [self.root]
      while nodes_to_visit:
        node = nodes_to_visit.pop(0)
        if node['id'] == id:
          return node
        nodes_to_visit.extend(node['children'])
      return None

    else:
      raise ValueError("Invalid method. Use 'depth' or 'breadth'.")
