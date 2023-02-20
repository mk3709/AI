
Source Code:

  
A = dict()
B = dict()
Y = dict()
X = dict()
A = {&quot;a&quot;: 0.2, &quot;b&quot;: 0.3, &quot;c&quot;: 0.6, &quot;d&quot;: 0.6}
B = {&quot;a&quot;: 0.9, &quot;b&quot;: 0.9, &quot;c&quot;: 0.4, &quot;d&quot;: 0.5}
print(&#39;The First Fuzzy Set is :&#39;, A)
print(&#39;The Second Fuzzy Set is :&#39;, B)
for A_key, B_key in zip(A, B):
A_value = A[A_key]
B_value = B[B_key]
if A_value &gt; B_value:
Y[A_key] = A_value
else:
Y[B_key] = B_value
print(&#39;Fuzzy Set Union is :&#39;, Y)
# Difference Between Two Fuzzy Sets
for A_key in A:
X[A_key]= 1-A[A_key]
print(&#39;Fuzzy Set Complement is :&#39;, X)
