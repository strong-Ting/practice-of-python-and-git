def is_palindrome(input_str):
    ans = True if input_str == input_str[::-1] else False
    return ans

input_str = input("str:")
print(is_palindrome(input_str))
