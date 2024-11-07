class Node:
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            self._insert(self.root,key)
    def _insert(self,root,key):
        if key < root.key:
            if root.left is None:
                root.left=Node(key)
            else:
                self._insert(root.left,key)
        else:
            if root.right is None:
                root.right=Node(key)
            else:
                self._insert(root.right,key)
    def delete(self,key):
        self.root=self._delete(self.root,key)
    def _delete(self,root,key):
        if root is None:
            return root
        if key<root.key:
            root.left=self._delete(root.left,key)
        elif key>root.key:
            root.right=self._delete(root.right,key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            temp=self._min_value_node(root.right)
            root.key=temp.key
            root.right=self._delete(root.right,temp.key)
        return root    
    def _min_value_node(self,node):
       current=node
       while current.left is not None:
           current=current.left
       return current
    def search(self,key):
       return self._search(self.root,key)
    def _search(self,root,key):
        if root is None or root.key==key:
            return root
        if key<root.key:
            return self._search(root.left,key)
        return self._search(root.right,key)
    def display(self):
        lines,*_=self._display_aux(self.root)
        for line in lines:
            print(line)
    def _display_aux(self,node):
        if node.right is None and node.left is None:
            line=f'{node.key}'
            width=len(line)
            hight=1
            middle=width//2
            return [line],width,hight,middle
        if node.right is None:
            lines,n,p,x=self._display_aux(node.left)
            s=f'{node.key}'
            u=len(s)
            first_line=(x+1)*''+(n-x-1)*'_'+s
            second_line=x*''+'/'+(n-x-1+u)*''
            shifted_lines=[line+u*'' for line in lines]
            return [first_line,second_line,]+shifted_lines,n+u,p+2,n+u//2
        if node.left is None:
            lines,n,p,x=self._display_aux(node.right)
            s=f'{node.key}'
            u=len(s)
            first_line=s+x*'_'+(n-x)*''
            second_line=(u+x)*''+'\\'+(n-x-1)*''
            shifted_lines=[u*''+line for line in lines]
            return [first_line,second_line]+shifted_lines,n+u,p+2,u//2
        left,n,p,x=self._display_aux(node.left)
        right,m,q,y=self._display_aux(node.right)
        s=f'{node.key}'
        u=len(s)
        first_line=(x+1)*''+(n-x-1)*'_'+s+y*'_'+(m-y)*''
        second_line=x*''+'/'+(n-x-1+u+y)*''+'\\'+(m-y-1)*''
        if p<q:
            left+=[n*'']*(q-p)
        elif q<p:
            right=[m*'']*(p-q)
        zipped_lines=zip(left,right)
        lines=[first+u*''+second for first,second in zipped_lines]
        return [first_line,second_line]+lines,n+m+u,max(p,q)+2,n+u//2
def menu():
    bst=BST()
    while True:
        print("\n BINARY SEARCH TREEEEEE")
        print("1.insert\n2.delete\n3.search\n4.display\n5.exit")
        choice=int(input("enter a choice:"))
        if choice==1:
            key=int(input("enter key to insert"))
            bst.insert(key)
        elif choice==2:
            key=int(input("enter key to delete:"))
            bst.delete(key)
        elif choice==3:
             key=int(input("enter key to search"))
             result=bst.search(key)
             if result:
                 print(f"key{key} found in bst")
             else:
                 print("nothing to show")
        
        elif choice==4:
            bst.display()
        elif choice==5:
           break 
        else:
            print("invalid")
if __name__=="__main__":
    menu()
            
            
                 
             
        
            
            
            
       