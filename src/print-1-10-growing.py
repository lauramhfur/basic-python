# Print the numbers described in the exercise
n = 10
for i in range(1, n+1):
    for j in range(1, i+1):
        if i != j:
            print(j, end = " ")
    print(i)