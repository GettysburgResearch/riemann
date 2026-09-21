# STC26: control of the transport-matched negative sector

**Proposed component proofs, pending independent review. No upper bound for
all of PET26's negative part, no full Newton covariance estimate, and no RH
proof is asserted.** Additive continuation of #903 at
`862f93aad76d0768b08bd9a12f6764d15e2cad63`.

This imports PET26's observable, not merely its name. It adapts RCB26's rough
parity partition to that observable and proves the needed estimate directly
in its actual kernel. It does NOT identify the physical kernel below with
RCB26's centered-harmonic kernel. Finite Euler algebra, squarefree counting,
character orthogonality and the elementary prime estimates are classical;
no field-wide priority claim is made.

## 1. Same observable, an exactly specified sector

Let b>=2 be an integer, X=b^2, N=X-1, and M(x)=sum_{n<=x} mu(n), zero for
x<1. All integrals use Lebesgue measure; integer jump values do not change
an integral. PET26 defines

$$\mathcal P_b=\sum_{p<X}\log p\int_b^X M(x)M(x/p)\frac{dx}{x^2}.$$

Every sum over p is over primes. Put

$$W_b(u,v)=\left(\frac1{\max(b,u,v)}-\frac1X\right)_+.$$

Then, with no tails omitted,

$$\mathcal P_b=\sum_{p<X}\sum_{m<X}\sum_{n<X/p}
 \mu(m)\mu(n)\log p\,W_b(m,pn).\tag{1}$$

Both m and n are squarefree whenever the coefficient is nonzero. Their
product pn need not be squarefree. For a finite prime bank S define

$$c_S(k)=\prod_{q\notin S,\ v_q(k)\text{ odd}}q.$$

This is the parity core, NOT the radical: c_empty(4)=1 and c_empty(12)=3.
Define the **transport-matched** sector T_{b,S} by restricting (1) to

$$c_S(m)=c_S(pn).\tag{2}$$

The remaining triples define R_{b,S}; thus P_b=T_{b,S}+R_{b,S} exactly.
The absolute matched envelope B_{b,S} is the same restricted sum with
|mu(m)mu(n)| in place of mu(m)mu(n). In particular

$$(-\mathcal P_b)_+\le B_{b,S}+(-R_{b,S})_+.\tag{3}$$

Unlike PET26's one-sided bound on (P_b)_+, a bound on B_{b,S} controls BOTH
signs of an explicitly identified piece of the previously unbounded side.
It does not control the remaining term in (3).

## 2. Complete classification of the matched triples

Write P_S=product_{q in S}q. Each a,c below is a squarefree divisor of P_S.
The integer r is squarefree and coprime to P_S. The following list is
exhaustive and disjoint:

| Case | m | n | Further condition | mu(m)mu(n) | max(m,pn) |
|---|---|---|---|---|---|
| p outside S, p does not divide n | p r a | r c | p does not divide r | -mu(a)mu(c) | p r max(a,c) |
| p outside S, p divides n | r a | p r c | p does not divide r | -mu(a)mu(c) | r max(a,p^2 c) |
| p in S | r a | r c | none | mu(a)mu(c) | r max(a,p c) |

Only rows with max(m,pn)<X enter. These restrictions imply m,n<X.

Proof. For p outside S, multiplying the squarefree n by p toggles exactly
the p-bit of its outside-S parity core. If p does not divide n, the core
of m must acquire p; if p divides n, it must lose p. All other outside-S
primes agree. For p in S there is no outside-S toggle. Unique factorization
then gives exactly the three rows and their displayed signs. QED.

This classification retains the reverse orientation m=r a,n=p r c. Its
transported product is p^2 r c. Deleting it as a nonsquarefree artifact is
incorrect; it is responsible for the second term in Section 4.

## 3. Uniform absolute budget, including arbitrarily large transport primes

Put

$$Z_S=\prod_{q\in S}(1+q^{-1/2}),\quad
 \Theta_N=\sum_{p\le N}\frac{\log p}{p},\quad
 \beta_S=\sum_{p\in S}\frac{\log p}{\sqrt p},\quad
 H_N=\sum_{n=1}^N\frac1n.$$

**STC26-1.** For every b and every finite S,

$$\boxed{B_{b,S}\le H_N Z_S^2(2\Theta_N+\beta_S).}\tag{4}$$

Proof. For the two outside-bank rows of the classification,

$$W_b(m,pn)\le\frac1{\sqrt{mpn}}=\frac1{pr\sqrt{ac}}.$$

For the inside-bank row the corresponding majorant is
1/(sqrt(p) r sqrt(ac)). Drop the coprimality, support and squarefreeness
restrictions on r, bounding its harmonic sum by H_N. Extend the a,c sums
to every divisor of P_S; their product sum is Z_S^2. The two outside-bank
orientations give at most 2 Theta_N and the inside-bank row gives beta_S.
Every extension enlarges a nonnegative majorant. This proves (4). QED.

The envelope proof also holds for ANY source supported on squarefree
integers with coefficients of modulus at most one. Its exact identification
with the native signs, and the sign formula in Section 4, use mu. Thus this
is not advertised as a theorem using every native divisor equation.

### A polylogarithmically growing bank still costs subpower

For t=log X>=exp(8), take any S contained in the primes up to t^2. Then

$$\boxed{B_{b,S}\le10t(1+t)\exp\!\left(\frac{14t}{\log t}\right)
 =X^{o(1)}.}\tag{5}$$

Here are all inputs to this conservative explicit bound. First,
log(N!)=sum_{p^j<=N}log(p)floor(N/p^j), and floor(N/p)>=N/(2p), so
Theta_N<=2 log N. The elementary central-binomial Chebyshev estimate
vartheta(z)<3z implies by partial summation
sum_{p<=z}log(p)/sqrt(p)<6sqrt(z). Also, for z>=exp(16), splitting primes
at sqrt(z) gives

$$\sum_{p\le z}p^{-1/2}\le 2z^{1/4}+12\sqrt z/\log z
 \le14\sqrt z/\log z.$$

These are the elementary bounds already used in PPD26/RCB26. Hence
log Z_S^2<=2 sum p^{-1/2}<=14t/log t, beta_S<=6t, and H_N<=1+t.
Insert them in (4). No PNT or RH hypothesis enters (4)-(5).

The estimate includes transport primes as large as X. Only the parity
mismatch is restricted to a small-prime bank. It is NOT just a bound for
the small-p terms in P_b.

## 4. Empty bank: an exactly negative sector and a sharper logarithmic budget

Let w_b(n)=(1/max(b,n)-1/X)_+. The classification now has a=c=1. Thus

$$\boxed{T_{b,\varnothing}=-D_b-J_b,}\tag{6}$$

where

$$D_b=\sum_{n<X}\mu(n)^2\log n\,w_b(n),$$
$$J_b=\sum_{p^2r<X,\ p\nmid r}\mu(r)^2\log p\,w_b(p^2r).$$

To prove the first equality, write the first orientation as n'=pr. Each
squarefree n' occurs with total weight sum_{p|n'}log p=log n'. The reverse
orientation gives J_b, not another copy of D_b. Every contribution is
nonpositive. In particular,

$$\boxed{0\le-T_{b,\varnothing}\le\tfrac32(\log b)^2+2\log b.}\tag{7}$$

Indeed, D_b=integral_b^X sum_{n<=x}mu(n)^2log(n) dx/x^2, whose numerator is
at most x log x. For J_b the numerator is at most
x sum_p log(p)/p^2<2x. The last bound follows from log n<=sqrt n and
sum_{n>=2}n^{-3/2}<2. Integrating gives (7), with every lower-cutoff term
retained.

There is also a sharp leading growth rate:

$$\boxed{-T_{b,\varnothing}=\frac9{\pi^2}(\log b)^2+O(\log b).}\tag{8}$$

This needs no PNT. The elementary identity mu(n)^2=sum_{d^2|n}mu(d) gives
Q(x)=sum_{n<=x}mu(n)^2=(6/pi^2)x+O(sqrt x). Partial summation yields
sum_{n<=x}mu(n)^2log n=(6/pi^2)(x log x-x)+O(sqrt x log x).
Integrating from b to b^2 gives the leading term in (8); J_b=O(log b).
Thus this negative sector is NOT negligible, even though it is subpower.

## 5. Exact family interpretation, and why it is not an individual bound

Let chi be a completely multiplicative sign character, free at primes
outside S up to N and equal to one on S. Put a_chi(n)=mu(n)chi(n),
A_chi(x)=sum_{n<=x}a_chi(n), and define the consistently twisted observable

$$\mathcal P_b^\chi=\sum_{p<X}\chi(p)\log p
 \int_b^X A_\chi(x)A_\chi(x/p)\frac{dx}{x^2}.$$

Finite sign orthogonality proves

$$\boxed{\mathbb E_\chi\mathcal P_b^\chi=T_{b,S}.}\tag{9}$$

The prime weight chi(p) is ESSENTIAL: the character in a summand is
chi(mpn), not chi(mn). Its average is one exactly under (2). This is a
finite algebraic identity; no random model for mu is assumed.

Do not infer the same bound for each signature. For S empty and chi(p)=-1
at every relevant prime, a_chi=mu^2 and

$$\mathcal P_b^\chi=-\sum_p\log p\int_b^X Q(x)Q(x/p)\frac{dx}{x^2}.$$

Keep just p=2. Since Q(x)=(6/pi^2)x+O(sqrt x), uniformly on this annulus,

$$-\mathcal P_b^\chi\ge
 \left(\frac{18\log2}{\pi^4}+o(1)\right)(X-b).\tag{10}$$

The matched sector remains (6), because all matched m p n are squares.
The unmatched remainder for this multiplicative signature is consequently
negative of order X, not subpower. This is an all-scale counterexample to
UNIFORM individualization of (9), not a counterexample on native mu.
PPD26's inexpensive small-bank signature comparison does not justify
changing all the rough prime signs in (9).

## 6. Exact consumer; the unresolved negative part has not disappeared

Let E=integral_1^b M(x)^2 dx/x^2 and I=integral_b^X M(x)^2 dx/x^2.
PET26's proved component inequality, with its finite d_b,h_b, implies

$$d_b I\le h_b\sqrt{EI}+(-\mathcal P_b)_+\quad(d_b>0).$$

Combine it with (3) to obtain

$$I\le\frac{h_b^2}{d_b^2}E+
 \frac2{d_b}\{B_{b,S}+(-R_{b,S})_+\}.\tag{11}$$

This uses h_b sqrt(EI)<=d_b I/2+h_b^2 E/(2d_b). The new theorem supplies
B_{b,S}, NOT the second term. For a bank as in (5), a genuinely new
subpower bound for (-R_{b,S})_+ would yield subpower physical energy along
the square ladder, hence RH by the existing Mellin argument. That native
remainder bound is not proved here.

For completeness, the conditional recursion has no hidden endpoint step:
d_b~(3/4)log b and h_b~(1/2)log b by PET26, so (11) would give
E(b^2)<=K E(b)+b^{o(1)}. Iteration on b_j=b_0^(2^j) gives E(b_j)=b_j^{o(1)};
monotonicity, with the exponent halved before interpolation, gives the same
for all b. Cauchy--Schwarz on dyadic intervals then makes
integral_1^infinity M(x)x^{-s-1}dx holomorphic for Re(s)>1/2, continuing
1/(s zeta(s)) from Re(s)>1. This conditional ending is inherited in substance,
not claimed as a new easier criterion.

For a FIXED bank S there is a sharper conditional statement: (4) is
O((log b)^2), so a bound (-R_{b,S})_+=O((log b)^2) would imply
E(b^2)<=(13/9+o(1))E(b)+O(log b). Since 13/9<2 and log(b^2)=2 log b,
iteration gives E(x)=O(log x). This stronger arithmetic input is also
unproved; finite positive remainders are not substituted for it.

The reported COMPLETE two-moment state remains

$$\mathcal A_{X-1}=E+I+2X(u_0+u_1)^2,\qquad
 u_0=\int_1^bM(x)\frac{dx}{x^2},\quad
 u_1=\int_b^XM(x)\frac{dx}{x^2}.$$

No claim that (4) alone controls that state is made. The finite calculations
retain both means and reconstruct the state exactly with directed intervals.

## 7. What changed relative to PET26 and RCB26

PET26 bounded the positive part of the full P_b. This packet controls the
absolute size of a specified matched sector, including its negative part,
and explains it as an average with an exact individualization obstruction.
RCB26 controlled within-squareclass blocks of a DIFFERENT harmonic kernel.
Its parity idea transfers; its numerical covariances and constants do not.

At Y=255, the empty-bank sector is approximately -25.95436, the unmatched
remainder +24.29287, and the full P_b -1.66149. For S={2,3} the corresponding
values are -9.10317 and +7.44169. Even these finite decompositions must be
kept signed. Positivity of these seven native remainders is reconnaissance,
not an all-scale theorem. The next task is native control of the remainder,
not another use of family averaging without an individualization estimate.
