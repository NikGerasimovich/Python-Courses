### Task 1.7
'''Write a program which makes a pretty print of a part of the multiplication table.
Examples:
Input:
a = 2
b = 4
c = 3
d = 7
Output:
	3	4	5	6	7
2	6	8	10	12	14
3	9	12	15	18	21
4	12	16	20	24	28
'''

inp_range1 = int(input())
answer = list()
a = list(range(inp_range1))
for i in range(10):
    for j in a:
        inp_range2 = j * a
        answer.append(inp_range2)

print(answer)
