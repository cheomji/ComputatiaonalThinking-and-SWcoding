#교수님 코드 입니다 ㅋ 저는 능력이 안돼서.. 걍 보고 공부하셈
from stack import *

while True:
	# 입력 부분 처리
	line = input("Enter an RPN expression: ")
	line = line.split()

	# 종료 조건 처리
	if line[0] == 'q':
		break

	# 스택 초기화
	rpn = getStack()

	# 오류 플래그	(초기값: False)
	# (1) =로 끝나지 않을 경우, 즉 =가 식의 마지막 부분이 아닌, 중간에 등장할 경우
	# (2) =가 아예 존재하지 않을 경우
	# (3) 연산자를(+,-,*,/) 마주쳤는데, 스택에서 pop() 연산을 통해 뽑아낼 피연산자(operands)가 2개 미만일 경우
	# (4) 연산을 모두 마쳤는데 (=를 만나서), 스택에 2개 이상의 숫자가 존재할 경우 (결과값을 제외하고도 1개 이상의 숫자가 남아있을 때)
	# (5) 연산을 모두 마쳤는데 (=를 만나서), 스택에 숫자가 아예 존재 하지 않을 경우 (즉, 결과값으로 반환할 값이 없을 경우에)
	# (1)-(4)에 대해서 오류 발생 처리가 필요하다!
	error = False

	if line[-1] != '=':	# 오류 (1)번
		error = True
	if '=' not in line:	# 오류 (2)번
		error = True
	
	if not error:

		for item in line:
			if item == '+' or item == '-' or item == '*' or item == '/':
				# 현재 item이 숫자가 아닌, 연산자들중 하나일 경우:
				# (1) 두 숫자를 pop한다! (피연산자;operands)로 활용해야 함.
				if isEmpty(rpn):	# 오류 (3)번
					error = True
					break
				op2 = pop(rpn)
				if isEmpty(rpn):	# 오류 (3)번
					error = True
					break
				op1 = pop(rpn)
				# (2) pop한 두 숫자를 이용하여, 현재 주어진 연산자로 연산을 수행한다.
				# (3) 그 결과를 다시 스택에 push하여 삽입한다.
				if item == '+':		push(rpn, op1 + op2)
				elif item == '-':	push(rpn, op1 - op2)
				elif item == '*':	push(rpn, op1 * op2)
				elif item == '/':	push(rpn, op1 / op2)
			elif item == '=':
				if isEmpty(rpn):	# 오류 (5)번
					error = True
				result = pop(rpn)
				if not isEmpty(rpn):	#오류 (4)번
					error = True
				break
			else:
				# 숫자이면, 그냥 push() 연산을 통해서 stack에 삽입한다.
				push(rpn, int(item))

	if not error:
		print("Value of expression:", result)
	else:
		print("Evaluation error!")
