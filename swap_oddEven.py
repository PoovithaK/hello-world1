def swapem (s):
    if len(s) < 2: return s
    return "%s%s%s"%(s[1], s[0], swapem (s[2:]))

for str in ("string", "value"):
    print "[%s] -> [%s]"%(str, swapem (str))
