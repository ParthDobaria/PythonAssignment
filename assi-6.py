#name: 20CE026-PARTH DOBARIA
#github-link : https://github.com/ParthDobaria/PythonAssignment.git

# You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.
# Sample Input
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# Sample Output
# 3
# 2 1 1
# Explanation: There are 3 distinct words. Here, "bcdef" appears twice in the input at the first and last positions. The other words appear once each. The order of the first appearances are "bcdef", "abcdefg" and "bcde" which corresponds to the output.

n= int(input())
c= {}
l = []
for i in range(n):
  word = input()
  l.append(word)
  if word in c:
    c[word] += 1
  else:
    c[word] = 1 
print(len(c))
print(' '.join([str(c[word]) for word in c]))