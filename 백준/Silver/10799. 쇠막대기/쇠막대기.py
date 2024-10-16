import sys
input = sys.stdin.readline

def raser(pipe):
   stack = []
   result = 0
   
   for i in range(len(pipe)):
       if pipe[i] == '(':
           stack.append(i)
       else:
           stack.pop()
           
           if pipe[i-1] == '(':
               result += len(stack)
           else:
               result += 1 
   return result

pipe = input().strip()
print(raser(pipe))