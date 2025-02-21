iphones = [
    {
        "price": 3000,
        "name": "iphone13"
    },
    {
        "price": 1000,
        "name": "iphone10"
    },
    {
        "price": 5000,
        "name": "iphone14"
    },
    {
        "price": 2000,
        "name": "iphone11"
    },
    {
        "price": 4000,
        "name": "iphone13"
    },
    {
        "price": 3500,
        "name": "iphone13PM"
    },
    {
        "price": 2500,
        "name": "iphone12PM"
    },
    {
        "price": 4200,
        "name": "iphone14PM"
    }
]

class Node:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, name, price):
        if self.root == None:
            self.root = Node(name, price)
        else:
            self._insert_recursive(self.root, name, price)
        
    def _insert_recursive(self, node, name, price):
        if price < node.price:
            if node.left == None:
                node.left = Node(name, price)
            else:
                self._insert_recursive(node.left, name, price)
        else:
            if price > node.price:
                if node.right == None:
                    node.right = Node(name, price)
                else:
                    self._insert_recursive(node.right, name, price)
                    
    def search(self, min_price, max_price):
        result = []
        self._inorder(self.root, min_price, max_price, result)
        return result
        
    def _inorder(self, node, min_price, max_price, result):
        if not node:
            return
        if node.price > min_price:
            self._inorder(node.left, min_price, max_price, result)
        if min_price <= node.price <= max_price:
            result.append({"name": node.name, "price": node.price})
        if node.price < max_price:
            self._inorder(node.right, min_price, max_price, result)
            
            
ip_bst = BinaryTree()
for item in iphones:
    ip_bst.insert(item["name"], item["price"])
    
sorted_lst = ip_bst.search(3000, 5000)

for iphone in sorted_lst:
    print(f"Name: {iphone["name"]} - Price: {iphone["price"]}")
        