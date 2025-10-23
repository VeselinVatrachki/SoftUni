from collections import deque

expr = deque(input())
open_parentheses = '([{'
close_parentheses = ')]}'
index = open_parentheses.index(expr[0]) # 2
print(index, "Print index")
print(expr[0])                         #  {
print(open_parentheses.index(expr[0])) #  2
print(expr[1])                         #  [
print(close_parentheses[index])        #  }
print(expr.popleft())                  #  {
print(expr.popleft())                  #  [