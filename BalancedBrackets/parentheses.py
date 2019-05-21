#Take a str of parentheses and balance it
#example str = '(()' -> '(())'

def format(string):
  result = ''

  if '(' in string:
    first_open = string.index('(')

    i = 0
    while i < first_open:
      result += '('
      i += 1
    
    for j in range(i):
      result += string[j]
  
  string = string[i:]

  result+= string

  stack = []
  
  for k in string:
    if k == '(':
      stack.append(')')
    if k == (')'):
      stack.pop()

  for l in stack:
    result += l

  
  return result

test = ')))('
print(format(test))









test1 = '((()'
test2 = ')()(('

print(balanceParentheses(test1)) # should be '((()))'
print(balanceParentheses(test2)) # should be '()()(())'

