import re
solved = False
def solve(letters, values, visited, words):
global solved
if len(set) == len(values):
map = {}
for letter, val in zip(letters,values):
map[letter] = val
if map[words[0][0]] == 0 or map[words[1][0]] == 0 or map[words[2][0]] == 0:
return
word1, word2, res = "", "", ""
for c in words[0]:
word1 += str(map[c])
for c in words[1]:
word2 += str(map[c])
for c in words[2]:
res += str(map[c])
if int(word1) + int(word2) == int(res):
print("{} + {} = {}\t{}".format(word1, word2, res, map))
solved = True
return
for i in range(10):
if not visited[i]:
visited[i] = True
values.append(i)
solve(letters, values, visited, words)
values.pop()
visited[i] = False
print("\nCRYPTARITHMETIC PUZZLE SOLVER")
print("WORD1 + WORD2 = RESULT")
word1 = input("Enter WORD1: ").upper()
word2 = input("Enter WORD2: ").upper()
result = input("Enter RESULT: ").upper()
if len(result) > (max(len(word1), len(word2)) + 1):
print("\n0 Solutions!")
else:
set = []
for c in word1:
if c not in set:
set.append(c)
for c in word2:
if c not in set:
set.append(c)
for c in result:
if c not in set:
set.append(c)
if len(set) > 10:
print("\nNo solutions!")
exit()
print("Solutions:")
solve(set, [], [False for _ in range(10)], [word1, word2, result])
if not solved:
print("\n0 solutions!")
