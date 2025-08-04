from NodeStack import NodeStack

def revert_text(text):
  stack = NodeStack()

  for char in text:
    stack.push(char)

  reversed_text = ''
  while not stack.is_empty():
    reversed_text += stack.pop()

  return reversed_text


def revert_text_by_words(text: str):
  stack = NodeStack()
  words = text.split(' ')

  for word in words:
    stack.push(word)

  reversed_text = []
  while not stack.is_empty():
    reversed_text.append(stack.pop())

  return ' '.join(reversed_text)


print(revert_text('David'))
print(revert_text_by_words('David, Shelton Sales de Faria'))
