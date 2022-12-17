# Write a function that takes in a string and returns the first character that does not repeat in the string. 
# For example, if the input is "total", the function should return "o" 
# because "o" is the first character that does not repeat in the string.

# solution 

from collections import Counter
def noReturnStr():
  word = input("문자열을 입력하세요 : ")
  word = word.replace(' ','')
  if word.isalpha() == False :
    return "입력한 내용이 적절하지 않습니다"
  text = list(word)
  cnt = Counter(text)
  lst = list(cnt.items())
  for i, j in lst:
    if j == 1:
      return i
