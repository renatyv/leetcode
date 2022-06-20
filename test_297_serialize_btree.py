from typing import Optional


class TreeNode(object):
    def __init__(self, x: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = x
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        format:
        nhlr
        n = size of left tree in symbols
        h = head value
        l = left tree
        r = right tree
        """
        if root is None:
            return ''
        else:
            left_subtree_str = self.serialize(root.left)
            right_subtree_str = self.serialize(root.right)
            val_str = chr(root.val + 1000)
            left_len_str = chr(len(left_subtree_str))
            return left_len_str + val_str + left_subtree_str + right_subtree_str

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        left_len = ord(data[0])
        root = TreeNode(ord(data[1]) - 1000)
        if left_len > 0:
            root.left = self.deserialize(data[2:2 + left_len])
        if len(data) - 2 - left_len > 0:
            root.right = self.deserialize(data[2 + left_len:])
        return root


def test_examples():
    codec = Codec()
    assert codec.deserialize(codec.serialize(None)) == None
    serizlied = codec.serialize(TreeNode(0))
    head = codec.deserialize(serizlied)
    assert head.val == 0 and head.left is None and head.right is None
    serizlied = codec.serialize(TreeNode(0,
                                         TreeNode(1),
                                         TreeNode(2,
                                                  TreeNode(3))))
    head = codec.deserialize(serizlied)
    assert head.val == 0 and head.left.val == 1 and head.right.val == 2
