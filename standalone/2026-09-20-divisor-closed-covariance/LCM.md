# Full least-common-multiple cancellation and an exact boundary kernel

**Proposed elementary component proof for independent review. This is an exact
source-faithful identity, not an upper bound for the full covariance.**
It strengthens the divisor-closure interpretation in PROOF.md and uses the
same physical prime observable. It is not a theorem about the harmonic
Newton Gram without a separate adapter.

Let h be supported on primes, h(1)=0, and set A=h*mu. The weights of h need
not be positive for the identity below. Define

$$C(n)=\sum_{\operatorname{lcm}(m,t)=n}\mu(m)A(t).$$

Every sum at a fixed n is finite. Then

$$\boxed{C(n)=0\quad\text{for every }n.}\tag{1}$$

Indeed,

$$\sum_{d\mid n}C(d)=
 \left(\sum_{m\mid n}\mu(m)\right)
 \left(\sum_{t\mid n}A(t)\right)
 =\delta(n)h(n)=0.$$

Möbius inversion gives (1). This uses the actual divisor-inverse equation;
it is not orthogonality assigned to unrelated prime shifts.

Now b>=2, X=b^2, N=X-1, and w(n)=(1/max(b,n)-1/X)_+. Because w(n)=0
for n>=X, (1) gives

$$\sum_{m,t\le N}\mu(m)A(t)w(\operatorname{lcm}(m,t))=0.$$

Therefore the ENTIRE physical covariance has the exact representation

$$\boxed{P_b=\sum_{m,t\le N}\mu(m)A(t)\,
 \left[w(\max(m,t))-w(\operatorname{lcm}(m,t))\right].}\tag{2}$$

The new nonnegative kernel is

$$\Delta_b(m,t)=\int_b^X
 \mathbf1_{\max(m,t)\le x<\operatorname{lcm}(m,t)}\frac{dx}{x^2}.\tag{3}$$

It vanishes whenever m and t are divisor-comparable, and whenever their
lcm is at most b. At every observation point x, only the incomplete
LCM fibres, with max(m,t)<=x<lcm(m,t), remain. Thus the old STC26 empty-bank
matched sector, which has m=sf(t) dividing t, vanishes IDENTICALLY in this
representation. Its negative mass has been canceled by actual arithmetic
companions, not dropped or bounded by zero on its own.

The kernel correction is not constant on all incomparable pairs. In the
region b<=max(m,t)<=lcm(m,t)<X it is

$$\Delta_b(m,t)=\frac{\min(m,t)-\gcd(m,t)}{mt}.$$

When lcm(m,t)>=X, no lcm correction is present and the original kernel
remains. Thus high-lcm, nearly coprime pairs remain a serious unresolved
sector. Nonnegativity of Delta does NOT imply a favorable sign of the
signed coefficient sum. Formula (2) is not a proof of RH.

## Safe relation to the separate comparable sign theorem

PROOF.md's P_div is positive for nonnegative prime weights. Removing only
that set from the ORIGINAL kernel leaves P_b-P_div, not P_b. Formula (2)
also subtracts a precisely specified contribution from the incomparable
pairs; the sum of all those corrections is zero. The two representations
are compatible, but their remainders cannot be interchanged term by term.
The stored transport tables use the original-kernel, positive-sector
partition. The tests independently check the full LCM identity and boundary
kernel for small complete domains.

## General inverse coefficients retain an explicit correction

For a general real source a, A=h*a and d=1*a, the LCM fibre sum is

$$C=\mu*[d\,(h*d)],$$

where the product inside brackets is POINTWISE. It need not vanish.
Accordingly the missing term in a would-be use of (2) is
sum_n C(n)w(n). This is another exact expression of the source mismatch
identified in LFAMILY.md. The E_17 single-prime example has C(7)=-20 in
units of log 7, so this correction cannot be deleted in the CM family.
