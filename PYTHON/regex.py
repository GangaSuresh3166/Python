# Regular Expression:

# 1 //  match = 

# import re
# a="hello world"
# b=re.match("hello",a)
# print(b)


# 2 //  search = 

# import re
# a="my favourite number is 5,number"
# b=re.search("number",a)
# print(b)


# 3 //  findall = 

# import re
# a="my favourite number is 5,number"
# b=re.findall("e",a)
# print(b)


# 4 // split = 

# import re
# a="my name is anu"
# b=re.split("name",a)
# print(b)


# 5 // sub = 

import re
a="my name is anu,my age is 20"
b=re.sub("anu","ammu",a)
print(b)