def RLE(s):
    if not s.isalpha():
        return ValueError("Невалидная строка")
    if not s:
        return ""
    result = ""
    count = 1
    prev_char = s[0]
    for char in s[1:]:
        if char != prev_char:
            result += prev_char + str(count)
            count = 1
            prev_char = char
        else:
            count += 1
    result += prev_char + str(count)
    return result


print(RLE("AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB"))
