# sympy_외부라이브러리

from fractions import Fraction
import sympy

x = sympy.symbols("x")
f = sympy.Eq(x*Fraction('2/5'), 1760) # 원래 갖고 있던 돈 계산
result = sympy.solve(f)
print(result)

remains = result[0] - 1760 # 남은 돈 계산
print(remains)