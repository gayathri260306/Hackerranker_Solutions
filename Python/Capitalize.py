# Problem: Capitalize
# Difficulty: Easy
#You are asked to ensure that the first and last names of people begin with a capital letter in their passports.

def solve(s):
    word=s.split(' ')
    li=[]
    for i in word:
        a=i.capitalize()
        li.append(a)
        
    result=' '.join(li)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
