# K-D TREE
def insert(self, point):
    if not self.root:
        self.root = Node(point)
    else:
        current = self.root
        while current:
            if point[0] < current.point[0]:
                if not current.left:
                    current.left = Node(point)
                    break
                current = current.left
            elif point[0] > current.point[0] or (point[0] == current.point[0] and point[1] < current.point[1]):
                if not current.right:
                    current.right = Node(point)
                    break
                current = current.right


def range(self, low, high):
    points = []
    def search(node):
        if not node:
            return
        if low[0] <= node.point[0] <= high[0] and low[1] <= node.point[1] <= high[1]:
            points.append(node.point)
        if low[0] <= node.point[0]:
            search(node.left)
        if high[0] >= node.point[0]:
            search(node.right)
    search(self.root)
return points


def nearest_neighbor(self, point):
    nearest = None
    def search(node):
        nonlocal nearest
        if not node:
            return
        distance = self.distance(point, node.point)
        if not nearest or distance < self.distance(point, nearest):
            nearest = node.point
        if point[0] < node.point[0]:
            search(node.left)
        else:
            search(node.right)
    search(self.root)
    return nearest
