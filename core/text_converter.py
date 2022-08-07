
def converter(text_name):
  f = open(text_name, "r")
  text_string = ''
  for line in f:
    text_string += line
  return text_string