# Problem: List
# Difficulty: Easy

'''Consider a list (list = []). You can perform the following commands:

1.insert i e: Insert integer e at position i.
2.print: Print the list.
3.remove e: Delete the first occurrence of integer e.
4.append e: Insert integer e at the end of the list.
5.sort: Sort the list.
5.pop: Pop the last element from the list.
7.reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.'''
if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        i=input().split()
        if i[0]=='insert':
            l.insert(int(i[1]),int(i[2]))
        elif i[0]=='print':
            print(l)
        elif i[0]=='remove':
            l.remove(int(i[-1]))
        elif i[0]=='append':
            l.append(int(i[-1]))
        elif i[0]=='sort':
            l.sort()
        elif i[0]=='pop':
            l.pop()
        elif i[0]=='reverse':
            l.reverse()
