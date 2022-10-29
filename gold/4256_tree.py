def get_tree(preorder, inorder):
    root = preorder[0]
    n = inorder.index(root)
    left_in = inorder[:n]
    right_in  = inorder[n+1:]
    left_pre = preorder[1:1+n]
    right_pre = preorder[1+n:]
    if len(left_in) > 0:
        trees[root][0] = left_pre[0]
        get_tree(left_pre, left_in)
    if len(right_in) > 0:
        trees[root][1] = right_pre[0]
        get_tree(right_pre, right_in)

def postorder(n):
    if trees[n][0] != 0:
        postorder(trees[n][0])
    if trees[n][1] != 0:
        postorder(trees[n][1])
    print(n, end=" ")

T = int(input())
for t in range(T):
    N = int(input())
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    trees = [[0, 0] for n in range(N+1)]

    get_tree(preorder[:], inorder[:])
    postorder(preorder[0])
    print()

      
        

    
    