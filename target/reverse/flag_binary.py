# simple obfuscated flag string for reverse engineering
def f():
    nums = [102,108,97,103,123,114,101,118,95,114,101,118,95,49,50,51,125]
    return ''.join(chr(n) for n in nums)

if __name__ == '__main__':
    # intentionally not printing; student should inspect the file
    pass
