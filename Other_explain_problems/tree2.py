# Add following methods to BinarySearchTreeNode class
# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree






class Binary_search_Tree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_elements(self, data):
        if data == self.data:
            return
        if data <self.data:
            if self.left:
                self.left.add_elements(data)
            else:
                self.left = Binary_search_Tree(data)
        if data > self.data:
            if self.right:
                self.right.add_elements(data)
            else:
                self.right = Binary_search_Tree(data)

    def inorder_elements(self):
        elements = []
        if self.left:
            elements += self.left.inorder_elements()

        elements.append(self.data)

        if self.right:
            elements+=self.right.inorder_elements()

        return elements
    
    def preorder_elements(self):
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder_elements()     
        if self.right:
            elements+=self.right.preorder_elements()

        return elements
    
    def postorder_elements(self):
        elements = []        
        if self.left:
            elements += self.left.postorder_elements()     
        if self.right:
            elements+=self.right.postorder_elements()
        elements.append(self.data)
        return elements
    
    def search(self,val):
        if val ==self.data:
            return True
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data :
            if self.right:
                return self.right.search(val)
            else :
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        return self.data
    
    def calculate_sum(self):
        sum=0
        if self.left:
            sum+=self.left.calculate_sum()
        sum += self.data
        if self.right:
            sum+=self.right.calculate_sum()
        return sum
    

def build_tree(elements):
    root = Binary_search_Tree(elements[0])
    for i in range(1,len(elements)):
        root.add_elements(elements[i])
    return root


if __name__ == "__main__":

    countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
    country_tree = build_tree(countries)

    print(country_tree.inorder_elements())
    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))

    numbers = [15,12,27,88,20,14,7,23]
    root = build_tree(numbers)
    print(root.inorder_elements())
    print(root.search(0))
    print(root.find_min())
    print(root.find_max())
    print(root.calculate_sum())
    print(root.preorder_elements())
    print(root.postorder_elements())

