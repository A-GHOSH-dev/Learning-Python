# A program to construct Binary  
# Tree from preorder traversal  
  
# Utility function to create a 
# new Binary Tree node  
class newNode: 
    def __init__(self, data): 
        self.data = data  
        self.left = None
        self.right = None
  
# A recursive function to create a 
# Binary Tree from given pre[] preLN[]  
# arrays. The function returns root of   
# tree. index_ptr is used to update  
# index values in recursive calls. index  
# must be initially passed as 0  
def constructTreeUtil(pre, preLN, index_ptr, n): 
      
    index = index_ptr[0] # store the current value  
                         # of index in pre[]  
  
    # Base Case: All nodes are constructed  
    if index == n:  
        return None
  
    # Allocate memory for this node and  
    # increment index for subsequent  
    # recursive calls  
    temp = newNode(pre[index])  
    index_ptr[0] += 1
  
    # If this is an internal node, construct left 
    # and right subtrees and link the subtrees  
    if preLN[index] == 'N': 
        temp.left = constructTreeUtil(pre, preLN,  
                                      index_ptr, n)  
        temp.right = constructTreeUtil(pre, preLN,  
                                       index_ptr, n)  
  
    return temp 
  
# A wrapper over constructTreeUtil()  
def constructTree(pre, preLN, n): 
      
    # Initialize index as 0. Value of index is 
    # used in recursion to maintain the current  
    # index in pre[] and preLN[] arrays.  
    index = [0] 
  
    return constructTreeUtil(pre, preLN, index, n) 
  
# This function is used only for testing  
def printInorder (node): 
    if node == None: 
        return
  
    # first recur on left child 
    printInorder (node.left)  
  
    # then print the data of node 
    print(node.data,end=" ")  
  
    # now recur on right child  
    printInorder (node.right) 
      
# Driver Code 
if __name__ == '__main__': 
    root = None
  
    # Constructing tree given in 
    # the above figure  
    #     10  
    #     / \  
    # 30 15  
    # / \  
    # 20 5  
    pre = [10, 30, 20, 5, 15] 
    preLN = ['N', 'N', 'L', 'L', 'L']  
    n = len(pre)  
  
    # construct the above tree  
    root = constructTree (pre, preLN, n)  
  
    # Test the constructed tree  
    print("Following is Inorder Traversal of", 
          "the Constructed Binary Tree:")  
    printInorder (root) 