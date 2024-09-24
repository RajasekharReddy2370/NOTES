import re

r = " Raj@2370 chen"

print(re.findall("[a-m]",r))
print(re.findall("\d",r))
print(re.findall("Ra.",r))
print(re.findall("^ Raj",r))
print(re.findall("chen$",r))
print(re.findall(" Ra.*n",r))
print(re.findall(" R.+@2370 chen",r))
print(re.findall(" Raj.?@2370 chen",r))
print(re.findall(" R.{2}@2370 chen",r))

print(re.findall("\A Raj",r))
print(re.findall(r"\bche",r))
print(re.findall(r"hen\b",r))
print(re.findall(r"\BRaj",r))
print(re.findall(r"Raj\B",r))
print(re.findall("\d",r))
print(re.findall("\D",r))
print(re.findall("\s",r))
print(re.findall("\S",r))

print("<b> raja sekhar </b>")

['a', 'j', 'c', 'h', 'e']
['2', '3', '7', '0']
['Raj']
[' Raj']
['chen']
[' Raj@2370 chen']
[' Raj@2370 chen']
[' Raj@2370 chen']
[' Raj@2370 chen']
[' Raj']
['che']
['hen']
[]
[]
['2', '3', '7', '0']
[' ', 'R', 'a', 'j', '@', ' ', 'c', 'h', 'e', 'n']
[' ', ' ']
['R', 'a', 'j', '@', '2', '3', '7', '0', 'c', 'h', 'e', 'n']

