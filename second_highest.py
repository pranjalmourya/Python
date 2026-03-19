# name_score = []
# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input()) 
#         name_score.append([name,score]) 
     
# scores = []
# for i in name_score:
#     scores.append(i[1])
# sorted_scores =   sorted(scores) 
# newlist = list(set(sorted_scores))
# second_Score = newlist[1]
# second_Scorer_student = []
# for j in range(len(name_score)):
#    if name_score[j][1] == second_Score:
#        second_Scorer_student.append(name_score[j][0])
# for i in  sorted(second_Scorer_student):
#     print(i)     
       
name_score =  [['Hina',20] , ['Shina' ,20.1] ,['Mina', 20.01], ['Tina',20.001]]
# for _ in range(int(input())):
#         name = input()
#         score = float(input()) 
#         name_score.append([name,score]) 

    
# scores = []
# for i in name_score:
#     scores.append(i[1])
# sorted_scores =   sorted(set(scores))
# # print(sorted_scores)
# second_Score = sorted_scores[1]
# second_Scorer_student = []
# for j in range(len(name_score)):
#     if name_score[j][1] == second_Score:
#         second_Scorer_student.append(name_score[j][0])
# second_Scorer_student_final = sorted(second_Scorer_student)        
# for i in sorted(second_Scorer_student_final):
#     print(i)     


# n = int(input())  
# s = set(map(int, input().split())) 
# print(n)
# print(s)

string = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
max_width = 4

start = 0
end = max_width
empty = []
for i in range((len(string)//4)+1): 
    if len(string[start:end]) == 0:
        break
    empty.append(string[start:end])
    start += max_width
    end += max_width
    count= 0
for j in empty:
    count+=1
    print(j,count)













