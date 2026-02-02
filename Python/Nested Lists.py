# Problem: Nested Lists
# Difficulty: Easy
#Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
if __name__ == '__main__':
    h=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        l=[name,score]
        h.append(l)
    s=[]
    us=[]
    n=[]
    for i in h :
       s.append(i[1]) 
    for i in s:
        if i not in us:
            us.append(i)
    us.sort()
    for i in h:
        if i[1]==us[1]:
            n.append(i[0])
    if len(n)>1:
        n.sort()
    for i in n:
        print(i)
        
