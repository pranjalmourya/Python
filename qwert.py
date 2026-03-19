string = 'AABCAAADA'
k = m = 3

start = 0
end = k
p = []
i = 0
while i < m:
    i += 1
    p.append(string[start:end])
    start += k
    end += k

for er in [[q for q in a] for a in p ]:
    print(''.join(list(set(er))))
   
       
    
    

  