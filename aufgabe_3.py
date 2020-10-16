
def decode(input_string):
  columns = input_string.split(' ')
  key = len(columns[0])
  output = ''
  for i in range(key):
    for col in columns:
      output = output + col[i]
  output = output.rstrip('-').replace('-', ' ')
  return output

string = 'H-VCG EIEOS L--D- LLEI- OONN-'

print(
  decode(string)
)