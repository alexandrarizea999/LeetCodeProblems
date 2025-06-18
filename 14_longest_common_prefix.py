strs = ["Alex", "Alin", "Alexandra", "Alice"]

if not strs:
    print("")
else:
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                print("")
                break
    else:
        print(prefix)