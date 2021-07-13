import re

txt = "The rain in Germany"
x = re.search("^The.*Germany$", txt)

print(x.start())
print(x.endpos)
print(x.span())
print(x.group())