
def decode(input_string):
  # check if input is string
  if type(input_string) != str:
    return "Wrong input type"
  
  # split input into columns
  columns = input_string.split(' ')

  # get key of string
  key = len(columns[0])
  
  # for keynumber iterate over columns
  output = ''
  for i in range(key):
    for col in columns:
      output = output + col[i]

  # remove dashes at the end and convert them to spaces
  output = output.rstrip('-').replace('-', ' ')
  return output

string = 'H-VCG EIEOS L--D- LLEI- OONN-'

print(
  decode(string)
)

from nose.tools import assert_equal
assert_equal(decode("H-VCG EIEOS L--D- LLEI- OONN-"), 'HELLO I LOVE ENCODINGS')
assert_equal(decode("T-A-I HA-SN ELHE- RWICD EADRA -YDET ISETA S-N--"), 'THERE IS ALWAYS A HIDDEN SECRET IN DATA')
assert_equal(decode("NHRHA OA-IG BLRSE OLE-- D-AM- YEDE- -V-S- SETS-"), 'NOBODY SHALL EVER READ THIS MESSAGE')
assert_equal(type(decode("ts et")), str)
assert_equal(len(decode("T- HS IE SN -T WE IN LC LE -- BI E- -G AU -E LS OS N- G-")), 36)
assert_equal(decode(""), "")
assert_equal(decode([]), "Wrong input type")
