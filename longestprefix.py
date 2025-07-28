def longest_common_prefix(strings):
    if not strings:
        return "-1"
    min_length=min(len(s)for s in strings)

    for i in range(min_length):
        currentchar=strings[0][i]

        for s in strings:
            if s[i]!=currentchar:
                return strings[0][ :i] if i>0 else "-1"
        
    return strings[0][ :min_length]

strings=["flow","flower","floor"]
print(longest_common_prefix(strings))