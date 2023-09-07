# Modify delete method in class BinarySearchTreeNode class to use min element from left subtree. You will
# remove lines marked with # elow and use max value from left subtree




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

    def delete(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else :
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            # min_val = self.right.find_min()
            # self.data = min_val
            # self.right=self.right.delete(min_val)
            max_val = self.left.find_max()
            self.data = max_val
            self.left=self.left.delete(max_val)
        return self
    
def build_tree(elements):
    root = Binary_search_Tree(elements[0])
    for i in range(1,len(elements)):
        root.add_elements(elements[i])
    return root


if __name__ == "__main__":
    numbers = [15,12,27,88,20,14,7,23]
    root = build_tree(numbers)
    root.delete(20)
    print(root.inorder_elements())

