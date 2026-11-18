"""Bound the lower end of the deterministic midpoint proxy, using real Arb balls."""
from flint import arb, ctx

ctx.prec = 128
log2 = arb(2).log()
b = lambda v: -(1-1/v).log()
a = lambda v: v.li()-arb(2).li()
# The positive integral in c has terms E1(m log 2)/(m+1).
c_upper = arb.const_euler() + log2.log()
for m in range(1, 13):
    c_upper += (-m*log2).ei() / (m+1)
assert c_upper < arb('-.034')

right_lo, right_hi = arb('2.8724'), arb('2.8726')
mid_hi = arb('2.3909')
assert a(right_lo) < 1 < a(right_hi)
assert a(mid_hi) > arb(1)/2
# b(v)/log(v) decreases, so this is an upper Darboux bound for the first cell.
step = (right_hi - 2)/2048
first_integral = sum(step*b(2+j*step)/(2+j*step).log() for j in range(2048))
first_error_lower = b(mid_hi) - first_integral
# |d/dy b(v(y))| decreases for v>=2, giving the midpoint Peano tail.
tail_error = right_lo.log()/(8*right_lo*(right_lo-1))
d_upper = c_upper - first_error_lower + tail_error
assert d_upper < arb('-.003')
print(f'Upper bound for d: {d_upper}')
