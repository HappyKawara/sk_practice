import re
xs = ["-","..","'","00"]
print([re.sub("-|\.|'","",x) for x in xs if re.match("\D",x)])

