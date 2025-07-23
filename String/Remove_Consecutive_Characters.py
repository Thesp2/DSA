def remove_consecutive(s:str)->str:
    if not s:
        return ''
    
    result=[s[0]]

    for c in s[1:]:
        if c != result[-1]:
            result.append(c)
    return ''.join(result) 

input_str = "aaabbcddddee"
output_str = remove_consecutive(input_str)
print(output_str)
