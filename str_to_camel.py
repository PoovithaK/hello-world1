def camel(x):
    final = ''
    for item in x:
        if item.isupper():
            final += "_"+item.lower()
        else:
            final += item
    if final[0] == "_":
        final = final[1:]
    print(final)

camel("StringToCamelCase")
