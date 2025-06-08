# def square_digits(num):
#     return int(''.join(str(int(d) ** 2) for d in str(num)))
#
# print(square_digits(555))

# def solution(text, ending):
#   return text.endswith(ending)
#
# print(solution("abcd","cd"))

# def is_isogram(string):
#     return len(string) == len(set(string.lower()))
#
# print(is_isogram('Mike'))

# def is_pangram(string):
#     return len(set(s for s in string.lower() if s.isalpha())) == 26

# def is_uppercase(s):
#     return s.isupper()
#
# print(is_uppercase("TIMMY"))
#
# def all_positive(nums):
#     return all(n > 0 for n in nums)

#print(all_positive([89]))
#
# def contains_uppercase(s):
#     return any(c.isupper() for c in s)
#
# print(contains_uppercase('heLlo'))

def is_all_vowels(s):
    return all(c.lower() in "aeiou" for c in s)