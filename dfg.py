name_score = [['pranjal', 85.0], ['Anju',85.0],['krant', 76.0], ['saurabh', 95.0],['nisha', 95.0]]
# for _ in range(int(input())):
#      name = input()
#      score = float(input())
#      name_score.append([name,score]) 
     
scores = []
for i in name_score:
    scores.append(i[1])
sorted_scores =   sorted(scores) 
newlist = list(set(sorted_scores))
second_Score = newlist[1]
second_Scorer_student = []
for j in range(len(name_score)):
   if name_score[j][1] == second_Score:
       second_Scorer_student.append(name_score[j][0])
for i in  sorted(second_Scorer_student):
    print(i)     
       
      