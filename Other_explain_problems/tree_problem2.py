# modify print_tree method to take tree level as input. 
# And that should print tree only upto that level


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level =0
        p = self.parent
        while p:
            level +=1
            p=p.parent
        return level

    def print_tree(self,level): 
        if self.get_level() > level:
            return
        spaces = self.get_level()*" "*3
        prefix = spaces+"!__" if self.parent else ""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

def build_product_tree(x):
    root = TreeNode(x[0])

    cto = TreeNode(x[1])

    inf = TreeNode(x[2])
    inf.add_child(TreeNode(x[3]))
    inf.add_child(TreeNode(x[4]))

    app = TreeNode(x[5])
    cto.add_child(inf)
    cto.add_child(app)

    get = TreeNode(x[6])
    get.add_child(TreeNode(x[7]))
    get.add_child(TreeNode(x[8]))

    root.add_child(cto)
    root.add_child(get)

    return root



if __name__ == "__main__":
    x=["Nilupul", "Chinmay", "Vishwa","Dhaval","Abhijit","Aamir","Gels","Peter","Waqas"]
    y=["(CEO)","(CTO)","(Infrastructure Head)","(Cloud Manager)","(App Manager)","(Application Head)","(HR Head)","(Recruitment Manager)","(Policy Manager)"]
    k =[]
    for i in range(len(x)):
        k.append(x[i]+" "+y[i])
    print("Are you want only 1. name, 2. Designation or 3. Both")
    p = int(input())
    n = int(input("Enter the no. of level you want \n"))
    if p==1:
        root = build_product_tree(x)
    elif p==2:
        root = build_product_tree(y)
    elif p==3:
        root=build_product_tree(k)

    
    root.print_tree(n)