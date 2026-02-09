# Problem: Tuples
# Difficulty: Easy
#Given an integer,n, and n space-separated integers as input, create a tuple,t, of those n integers. Then compute and print the result of hash(t) .

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = tuple(map(int, raw_input().split()))
    print(hash(integer_list))
