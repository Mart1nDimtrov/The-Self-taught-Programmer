import this
import re

zen = "".join([this.d.get(c, c) for c in this.s])
matchObj = re.findall("[A-Za-z]+[y]\\b", zen)
print(matchObj)