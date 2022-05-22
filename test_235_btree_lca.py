class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root.val == q.val or root.val == p.val:
        return root
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)
    elif p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    else:
        return root


def test_examples():
    root = TreeNode(4,
                    TreeNode(2,
                             TreeNode(1),
                             TreeNode(3)),
                    TreeNode(7,
                             TreeNode(6),
                             TreeNode(9)))
    lca = lowestCommonAncestor(root, TreeNode(1), TreeNode(2))
    assert lca.val == 2
    assert lowestCommonAncestor(root, TreeNode(6), TreeNode(9)).val == 7
    assert lowestCommonAncestor(root, TreeNode(7), TreeNode(9)).val == 7
    assert lowestCommonAncestor(root, TreeNode(1), TreeNode(6)).val == 4
