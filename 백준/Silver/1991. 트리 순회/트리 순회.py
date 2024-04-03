import sys

input = sys.stdin.readline

tree = {}

n = int(input())

for _ in range(n):
    root, left, right = map(str, input().strip().split())
    tree[root] = [left,right]

def pre(root):
    if root != ".":
        print(root, end = "")
        pre(tree[root][0])
        pre(tree[root][1]) 

def ino(root):
    if root != ".":
        ino(tree[root][0])
        print(root, end = "")
        ino(tree[root][1])

def pos(root):
    if root != ".":
        pos(tree[root][0])
        pos(tree[root][1])  
        print(root, end = "")

pre("A")
print()
ino("A")
print()
pos("A")