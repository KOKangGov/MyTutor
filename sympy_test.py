# sympy_test.py

from fractions import Fraction
import sympy

# 가지고 있던 돈 x
x = sympy.symbols("x")

# 가지고 있던 돈의 2/5가 1760이므로, 방정식 = x*(2/5) = 1760
f = sympy.Eq(x*Fraction('2/5'), 1760)

# 방정식을 만족하는 값(result)을 구한다
result = sympy.solve(f)

# 남은 돈은 가지고 있던 돈에서 1760원 빼면 된다
remains = result[0] - 1760

print(f'남은 돈은 {remains}원 입니다.')
