"""Check the algebraic unramified cancellation in README; does not verify source identities."""
import sympy as s

v, V, W, D, R = s.symbols('v V W D R', nonzero=True)
E = (R*((1-v)/(1-V)+W-D)-D*(1/v-1)*W*V/(1-V))/(1-R)
P = 1/(1-V)+W/(1-W)-D+E
lhs = s.cancel((1/D-W)*(1-V)*(1-W)*(-D+E)-W*(1-V*W)+(1-V)*(1-W)*P)
rhs = V*(1-W)**2 + E*(1-V)*(1-W)*(1+1/D-W) - D*(1-V)*(1-W)*(1-W)
assert s.cancel(lhs-rhs) == 0
print('unramified local cancellation: exact')
