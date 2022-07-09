# code to check win conditions

sol1 = [[0,0],[0,1],[0,2]]
sol2 = [[1,0],[1,1],[1,2]]
sol3 = [[2,0],[2,1],[2,2]]
sol4 = [[0,0],[1,0],[2,0]]
sol5 = [[0,1],[1,1],[2,1]]
sol6 = [[0,2],[1,2],[2,2]]
sol7 = [[0,0],[1,1],[2,2]]
sol8 = [[0,2],[1,1],[2,0]]

soln = [sol1, sol2, sol3, sol4, sol5, sol6, sol7, sol8]

moves = [[0, 0], [0,2], [1, 1], [1,2], [2,2]]

for x in soln:
	if all(i in moves for i in x):
		result = "True"
		break
	else:
		result = "False"

print(result)
