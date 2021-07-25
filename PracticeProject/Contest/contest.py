'''
Created on 25-Jul-2021

@author: nikhil
'''
def maxCompatibilitySum(students, mentors):
    total_score = 0
    for student in students:
        max_score = 0
        for mentor in mentors:
            score = 0
            for i in range(len(student)):
                if student[i] == mentor[i]:
                    score +=1
            if max_score < score:
                max_score = score
        for mentor in mentors:
            score = 0
            for i in range(len(student)):
                if student[i] == mentor[i]:
                    score +=1
            if max_score == score:
                mentors.remove(mentor)
                break
            
        total_score += max_score
        print(total_score)
    return total_score
        
students = [[1,1,1],[0,0,1],[0,0,1],[0,1,0]]
mentors = [[1,0,1],[0,1,1],[0,1,0],[1,1,0]]
print(maxCompatibilitySum(students, mentors))