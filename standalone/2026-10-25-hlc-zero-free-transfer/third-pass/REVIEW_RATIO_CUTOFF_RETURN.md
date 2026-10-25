# Independent internal review: the exact ratio-cutoff return

Reviewer: root research agent. Author: native_gain agent.

**Verdict: pass for the exact coefficient identities and the stated
source-dependent scalar bound.** The note correctly withholds any lower
bound for a signed polynomial or family moment. It does not rule out a
new cancellation estimate for the remaining middle expression.

Reviewed mathematical file: `RATIO_CUTOFF_RETURN.md`, SHA256
`0c1abc65e71d0300ecac44234337be6b0ebc797db055b3f51a68a3dd91adc02a`, Git blob `1b58867a7d611b18f24a8470679638f57efb6e17`.
Reviewed checker: `check_ratio_cutoff_return.py`, SHA256
`97306a93cc7b2f6a94f1044bf5195b9aa9f5c7bf3331a5687ee59d9693a40687`,
Git blob `406b08c6d0fbf76acc89bc28f35f0b12d40b7ae1`.

I independently derived the return formula while the author was working
on the synthesis problem, then read the complete final note. The root
checker replay under `python -O` passed 6,247 inversion predicates,
120 masked reflected returns, and 50 squarefree/exponent predicates.
Negative controls caught the false support inference and deletion of
the natural k mask. These checks are finite algebra, not analytic
certification of the imported scalar cap or a functional equation.

## 1. The correct transformed coefficient

Starting from the complete gcd identity, expand the remaining
coprimality by `sum_(k|a,b) mu(k)` and substitute `a=km`, `b=kn`.
The character factors in k cancel only on the actual unit support,
leaving `1_((k,P_u)=1)`. The kernel depends on n/m, so k disappears
from its argument but retains the scalar weight `1/Nk`.

The original e sum is untouched. It has the primitive value at e,
not the naturally zero-extended value, and no false puncture restriction
is inserted in the remaining dual n. Thus reversing the exact ordinary
functional equation restores the same natural ordinary block and gives

`D_(F,P)(m)=sum_(k,P)=1 mu(k) C_(km)(P) F(Nk Nm/B_0)/Nk`.

There is no extra e factor in this coefficient. The primitive conductor,
original row, common profile and norm height are unchanged.

Substitute the finite definition of C and set v=kd. This gives

`D_(F,P)(m)=sum_(v,P)=1 A(mv)/Nv sum_(k|v) mu(k) F(Nk Nm/B_0)`.

At F=1, Mobius inversion leaves only v=1 and returns A(m) exactly.
At F=1-chi it returns A(m)-H_(chi,P)(m). In particular a lower
cutoff on the ratio numerator km does not become a lower cutoff on m.
The author's one-prime example correctly gives a nonzero returned
coefficient at m=1 and provides a direct finite negative control.

## 2. The small error estimate uses only its stated scalar input

On the natural support, the companion coefficient theorem gives

`|C_(km)(P)| << Z^epsilon (Nk Nm/D)^(1-beta)`.

The smooth low selector restricts `Nk<=2B_0/Nm`. Consequently

`|H_(chi,P)(m)| << Z^epsilon (Nm/D)^(1-beta)`

`                          times sum_(Nk<=2B_0/Nm) (Nk)^(-beta)`.

Ideal counting and partial summation bound the last sum by a constant
times `(B_0/Nm)^(1-beta)`. This gives the claimed uniform
`Z^epsilon(B_0/D)^(1-beta)` bound. When Nm is at least 2B_0 the low
coefficient is zero directly. No moving coefficient is inserted into
a family moment or sieve in this argument.

For B_0=U^(7/9), the smallest value of r-7/9 on the consumer interval
is 86/225. Taking beta=22/25 gives the bare exponent -86/1875.
Its margin over -1/25 is 11/1875, so the prescribed polynomial
puncture and bounded length ranges allow a sufficiently small epsilon
to obtain the stated U^(-1/25) error. Constants may depend on the
chosen scalar line and the fixed cutoff/profile data.

## 3. The critical original coefficients really remain

For squarefree m of norm at most y_2, every divisor factorization is
coprime and its second cutoff is one. Thus

`A(m)=mu(m) sum_(a|m) w_0(Na/y_1)`.

The sum is real, nonnegative and at least one, because a=1 occurs.
The ratio high component therefore retains this coefficient up to
the uniform small error. Subtracting the original-product far piece
as well leaves exactly

`chi_0(Nm/U) A(m)-H_(chi,P_u)(m)`.

This formula is a difference of three signed identities, with no claim
that the two subtracted selectors are disjoint. At the previously
critical product exponent b_* between .74 and .75, the first selector
is one; b_* is also below both 7/9-2/125 and r_c-2/125. Those strict
inequalities follow from the authenticated rational placement in the
asymmetric-tail review, not from a need to assume existence of special
rows. The original-product head has already vanished at this scale.
The supposed new lower support threshold therefore does not follow.

The conclusion is appropriately narrow. Coefficients of substantial
size can still cancel after the character sum and row average. This
note does not establish an actual moment lower bound, forbid a joint
estimate for the remaining signed sum, or disprove the open middle
hypothesis. It authenticates why the two separately proved component
norms do not, on their own, complete the zero-free argument.

The only root edit before binding was the status line naming this
completed review; the mathematical content was unchanged.
