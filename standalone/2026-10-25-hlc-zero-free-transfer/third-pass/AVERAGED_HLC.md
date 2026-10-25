# Long shift averages: a two-sign Type II power bound and the Type I residue

Status: the Type II estimate, smooth Vaughan decomposition, and homogeneous
mode calculation below are proved from the explicitly stated Mertens bound.
They do not prove a bound of smaller exponent for the full prime correlation.
The reason is calculated: the Type I part retains a coefficient tending to
one on every detectable Mellin mode.

Scope: ordinary rational integers, additive shifts of size comparable to X,
and common smooth profiles. This is not a theorem for arbitrary Eisenstein
angular profiles or native row kernels. The all-family statements needed
for those objects are not silently inferred from ordinary Mertens control.

Dependencies: only the displayed summatory premise, elementary summation by
parts, Poisson summation for smooth compact functions, the exact Vaughan
convolution identity, and the simple residue of zeta at one. The contrast
with the HLC source refers to arXiv:2610.20242v1, equations (4.2)-(4.5):
that fixed-shift proof discards the second Möbius sign before its determinant
estimate. The supplied PDF and digest are identified in the parent sources.

## 1. A power estimate retaining both Möbius signs

Fix 0<beta<1 and assume

\[
 |M(y)|=\left|\sum_{n\le y}\mu(n)\right|
                      \le C_\beta(1+y)^\beta.             \tag{1}
\]

Let X=MN with M,N>=2. Let A and W be smooth functions supported in fixed
compact subintervals of (0,infinity), with their supports bounded away
from zero, and let K be smooth and compactly supported. Take 1<=H<=X.
For coefficients b_n supported on N<n<=2N, put B_N=sum_n |b_n| and

\[
 T_H=\sum_n b_n\sum_m\mu(m)A(m/M)
       \sum_v\mu(v)W(v/X)K((v-mn)/H).                     \tag{2}
\]

The cutoff supports may be enlarged by fixed factors without changing the
claim. Assume they restrict v and mn to fixed multiples of X; this is
automatic for the standard positive-shift annuli used below.

**Theorem 1.** Under (1),

\[
 |T_H|\ll C_\beta^2 B_N M^\beta X^\beta(1+X/H),
 \qquad
 \frac{|T_H|}{H}\ll
 C_\beta^2 B_N M^\beta X^\beta(H^{-1}+XH^{-2}).           \tag{3}
\]

The implicit constant depends on fixed supports and a fixed finite number
of profile derivatives. In particular, if B_N<<N(log X)^C and H=cX for
fixed c>0, then

\[
 \boxed{T_H/H\ll X^\beta M^{\beta-1}(\log X)^C.}          \tag{4}
\]

For M=X^m this has exponent beta-m(1-beta), strictly smaller than beta
when m>0. At beta=7/8 and M>=X^{1/5}, it is at most 17/20. These are
conditional exponent examples under (1), not a claimed new zero-free
half-plane. With an epsilon-version of (1), enlarge the output exponent
by an arbitrarily small epsilon.

### Proof

For each n put

\[
 F_n(u,v)=A(u/M)W(v/X)K((v-un)/H).
\]

Twice integrating against dM gives the exact identity

\[
 \sum_{m,v}\mu(m)\mu(v)F_n(m,v)
 =\int_0^\infty\!\int_0^\infty M(u)M(v)
                           \partial_u\partial_vF_n(u,v)\,du\,dv.
 \tag{5}
\]

The two integrations each contribute a minus sign, so the final sign is
positive. All boundary terms vanish by compact support. Directly,

\[
\begin{split}
 \partial_u\partial_vF_n
 ={}&\frac{A'(u/M)}M
   \left[\frac{W'(v/X)}XK+\frac{W(v/X)}H K'\right]\\
 &-\frac{nA(u/M)}H
   \left[\frac{W'(v/X)}XK'+\frac{W(v/X)}H K''\right],
\end{split}                                                \tag{6}
\]

where K and its derivatives have argument (v-un)/H. The support has
u-length O(M) and, for each u, v-length O(H). Also nM is comparable to X.
The four derivative terms therefore have total L1 norm bounded by
O(H/X+1+1+X/H)=O(1+X/H). On this support |M(u)M(v)| is at most a fixed
multiple of C_beta^2 M^beta X^beta. This proves (3); substitute
B_N<<N(log X)^C and N=X/M to get (4). QED.

Smooth factors depending on mn/X can be included in A(u/M), with n as a
parameter, provided their scaled derivatives are uniformly bounded. A
factor m^{it} costs only a fixed power of 1+|t| in those seminorms; it is
not a new character-uniform Mertens theorem.

For H=X^theta the displayed exponent is
beta+2-m(1-beta)-2theta. Beating beta uniformly for m>=m_0 consequently
requires theta>1-m_0(1-beta)/2. This condition, and the factor H^-2, must
not be omitted when applying the result to shorter shifts.

## 2. Smooth Vaughan decomposition with an exact continuum term

Now fix 0<c<=1/4, H=cX, W supported in (1,2), and K supported in (1,2).
Write kappa=integral K, and define the smooth real-variable function

\[
 F_X(t)=\sum_v\mu(v)W(v/X)K((v-t)/H).                      \tag{7}
\]

It is supported in [X/2,2X]. The full prime correlation of the first-pass
bridge is exactly

\[
 S_H=\sum_{n\ge1}\Lambda(n)F_X(n).
\]

Let w be a fixed smooth cutoff on [0,infinity), equal to one on [0,1],
equal to zero on [2,infinity), and between zero and one. For U,V>=2 set

\[
 \mu_1(d)=\mu(d)w(d/U),\quad \mu_2=\mu-\mu_1,
 \quad \Lambda_1(\ell)=\Lambda(\ell)w(\ell/V),
 \quad \Lambda_2=\Lambda-\Lambda_1.
\]

Dirichlet convolution gives the **exact** identity

\[
 \Lambda=\Lambda_1+\mu_1*\log
                   -\mu_1*\Lambda_1*1+\mu_2*\Lambda_2*1.
 \tag{8}
\]

Indeed log=Lambda*1 and mu*1 is the convolution unit. If 2V<X/2, the
first term vanishes against F_X. Denote the remaining terms by T_1-T_2+T_3.
Define the exact finite sums

\[
 A_U=\sum_d\frac{\mu(d)w(d/U)}d,\qquad
 B_U=\sum_d\frac{\mu(d)w(d/U)\log d}d,\qquad
 L_V=\sum_\ell\frac{\Lambda(\ell)w(\ell/V)}\ell.           \tag{9}
\]

For any fixed integer J>=2 and UV<=X^{1-epsilon_0}, with fixed epsilon_0>0,
Poisson summation in the final free factor of T_1 and T_2 gives

\[
 \frac{T_1-T_2}{H}
 =\frac1H\int_0^\infty F_X(t)
       [A_U(\log t-L_V)-B_U]\,dt
 +O_J\left(X^\beta(UV/X)^J\log X\right).                 \tag{10}
\]

To verify the error, (1) and one summation by parts in v give
||F_X^{(j)}||_infinity<<_j X^{beta-j}, uniformly for every fixed j.
For smooth g supported on t comparable to X,

\[
 \sum_k g(qk)-q^{-1}\int g
       \ll_J q^{J-1}\|g^{(J)}\|_1.
\]

Apply this with q=d and g(t)=log(t/d)F_X(t), or q=d ell and g=F_X.
The sums of d^{J-1} and Lambda(ell)ell^{J-1} over the cutoff ranges are
O(U^J) and O(V^J log V), respectively. Division by H=cX proves the
displayed error. This argument retains the whole continuum term; it does
not classify it as a removable resonance.

For T_3 the coefficient of its second factor is
b_r=(Lambda_2*1)(r), with 0<=b_r<=log r and b_r=0 for r<=V. Smooth dyadic
partition in d, followed by Theorem 1, gives

\[
 \boxed{T_3/H\ll X^\beta U^{\beta-1}\log X.}              \tag{11}
\]

For each d-block M>=U the relevant r-block has N comparable to X/M.
Its contribution is O(X^beta M^{beta-1}log X). The sum over M is a
convergent geometric sum because beta<1, with largest term at M comparable
to U. The cutoff 1-w(d/U) has uniformly bounded scaled derivatives on
these blocks. No smoothness of b_r and no new estimate for it is assumed.

## 3. The Type I residue is exactly the Mertens signal

Under (1), the conditionally convergent series at s=1 and its derivative
may be evaluated from 1/zeta(s), because both series converge locally
uniformly in Re s>beta after summation by parts. Zeta has residue one at
its simple pole. Therefore

\[
 \sum_d\mu(d)/d=0,\qquad
 \sum_d\mu(d)\log d/d=-1.
\]

Summation by parts on the omitted tails, including the smooth transition,
gives

\[
 A_U=O(U^{\beta-1}),\qquad
 B_U=-1+O(U^{\beta-1}\log U).                             \tag{12}
\]

Let

\[
 L_c(u)=\int K(y)\log(u-cy)\,dy.
\]

The logarithm is smooth here: u is in (1,2), y in (1,2), and c<=1/4.
Changing variables t=v-Hy gives the exact identities

\[
 \int F_X(t)\,dt=\kappa H M_W(X),
\]

\[
 \int F_X(t)\log t\,dt
 =H[\kappa(\log X)M_W(X)+M_{W L_c}(X)].                  \tag{13}
\]

Thus the continuum term in (10) is exactly

\[
 \kappa[-B_U+A_U(\log X-L_V)]M_W(X)
                      +A_U M_{W L_c}(X).                \tag{14}
\]

It is kappa M_W(X), plus an error of size
O(X^beta U^{beta-1}log^2 X); the weaker elementary estimate
L_V=O(log^2 V) suffices. Combining (10)-(14) reconstructs

\[
 S_H/H=\kappa M_W(X)
 +O\left(X^\beta U^{\beta-1}\log^2X
        +X^\beta(UV/X)^J\log X\right).                  \tag{15}
\]

This proves a true power-saving estimate for the entire Type II part,
but it also proves why that component gain does not imply a bound of
smaller exponent for S_H itself. The Type I part contains the target.

For example U=V=X^{1/5} gives a Type II exponent at most 17/20 when
beta=7/8, while the continuum Type I term remains M_W at exponent beta.
More generally U=X^{1-epsilon_0-epsilon_1}, V=X^{epsilon_1} makes the
centered remainder exponent arbitrarily close to 2beta-1, after choosing
J large. That is a centered estimate, not a new Mertens exponent.

## 4. Exact multiplier on a hypothetical Mellin mode

This checks whether the Type I continuum term could provide a contracting
dilation equation. Use the test measure dM_rho(v)=rho v^{rho-1}dv, with
0<Re rho<1, in place of the v-Möbius measure in (7), while keeping the
actual finite coefficients A_U,B_U,L_V. Whenever kappa W_hat(rho) is
nonzero, the continuum Type I expression divided by the corresponding
kappa M_{rho,W}(X) has exact multiplier

\[
 \boxed{\mathcal L_{U,V,X}(\rho)
 =-B_U+A_U\left[
 \log X-L_V+
 \frac{\widehat{W L_c}(\rho)}{\kappa\widehat W(\rho)}
 \right].}                                               \tag{16}
\]

For polynomially growing U,V, (12) shows that this tends to one. This is
not an assumption that the actual Mertens function has a single-zero
asymptotic: it is an exact linear-mode calculation for the operator.
For a zero detector use W_tau(u)=W_0(u)u^{-i tau}, where W_0 is
nonnegative and tau=Im rho. Then W_hat_tau(rho)=W_hat_0(Re rho)>0, so
the denominator does not hide that mode. The limiting multiplier is
still one.

Changing the fixed additive kernel or this Mellin modulation changes
the finite ratio in (16), not its limiting unit coefficient. If kappa=0,
the leading Mertens signal is deleted; dividing by the remaining A_U
would require an all-scale lower bound that is not available and would
erase the putative gain. No contracting Type I multiplier has been proved.

## 5. Complete affine averaging really does give a power contraction

The following finite theorem tests the proposed averaging mechanism without
making assumptions about primes. It is an exact calculation, not a heuristic
about the Möbius signs.

Let p be prime, let f,g be complex functions on F_p, and use normalized
averages and norms. Put

\[
 C_{q,h}=p^{-1}\sum_{x\in\mathbb F_p}
                         f(x)\overline{g(qx+h)},
 \quad q\in\mathbb F_p^*,\quad h\in\mathbb F_p.
\]

Write m_f=E f and Var(f)=E|f|^2-|m_f|^2, and likewise for g.
Then the exact identity is

\[
 \boxed{\mathbb E_{q\ne0,h}|C_{q,h}|^2
 =|m_f|^2|m_g|^2+
             \frac{\operatorname{Var}(f)\operatorname{Var}(g)}{p-1}.}
 \tag{17}
\]

For x=y, the average of g(qx+h)conj(g(qy+h)) is E|g|^2. For x!=y,
the affine maps range exactly once through each ordered distinct pair,
so that average is |m_g|^2-Var(g)/(p-1). Expanding |C|^2 gives (17).
It yields the genuine p^-1/2 root-mean-square contraction for the centered
parts, while the constant component survives exactly.

This cannot yet be substituted into the HLC argument. Its averaging is
over a complete affine group, whereas the source uses products of selected
primes and an exact integer determinant equation with archimedean cutoffs.
Reducing that equation modulo p admits additional integer carries; choosing
p larger than the full integer range prevents a complete short-shift
average. Uniformity of a congruence model does not bound the exact equation.
Nor may the first term of (17) be omitted: it is the same mean component
whose full integer version is calculated in (14)-(16).

Thus (17) proves that nonconstant affine modes can contract at a fixed
power, but it does not supply the missing transfer from the source's
incomplete arithmetic average, and it does not eliminate the Mertens mode.

## 6. What a global family cap supplies for polynomial moduli

For this section only, assume explicitly that **every primitive Dirichlet
L-function** is zero-free in Re s>beta, with fixed beta<1, and retain the
usual uniform conductor/height growth on fixed strips. This is an
all-family premise. A bound for ordinary zeta alone does not imply it.
An applicable Eisenstein finite-order cap can supply it through the
quadratic base-change factorization, with all local factors retained;
that source implication must be kept separate from premise (1).

For a smooth compact annular W and every fixed epsilon>0, the Euler-log
disk argument used in `second-pass/CAPPED_NATIVE_MOMENT.md`, followed by
a smooth Mellin contour, gives

\[
 \sum_n\mu(n)\chi(n)W(n/X)
                    \ll_\epsilon X^{\beta+\epsilon}q^\epsilon p_J(W),
\]

\[
 \sum_n\Lambda(n)\chi(n)W(n/X)
  =1_{\chi=\chi_0}X\int W
       +O_\epsilon(X^{\beta+\epsilon}q^\epsilon p_J(W)).   \tag{18}
\]

The derivative and profile orders are fixed. To see the uniformity, on a fixed strip to the right
of beta, Borel--Caratheodory and three-circles bound log L by
O((log(q(2+|t|)))^theta), theta<1. Exponentiation controls 1/L with any
fixed subpower conductor/height loss; Cauchy controls L'/L. For the
principal function take the logarithm of ((s-1)/(s+1))L(s). This removes
the pole while keeping the Euler-disk logarithm uniformly bounded at
large heights; the extra pole at -1 lies outside the working half-plane.
Restore the known residue at one in the prime contour. Natural imprimitive
Euler factors have no zeros in Re s>0, have polynomial conductor growth,
and a uniformly bounded Euler logarithm on Re s>=2. They are covered by
the same argument. Smooth Mellin decay makes the vertical integrals
converge uniformly. This proves (18) from the all-family premise.

Orthogonality consequently gives, for reduced residue classes,

\[
 \sum_{q\le Q}\max_{(a,q)=1}
 \left|\sum_{n\equiv a\ (q)}\Lambda(n)W(n/X)
                 -\frac{X}{\varphi(q)}\int W\right|
 \ll_\epsilon Q^{1+\epsilon}X^{\beta+\epsilon}p_J(W).
 \tag{19}
\]

The analogous Möbius formula has zero main term. In particular
Q<=X^{1-beta-delta}, with fixed delta>0 and epsilon chosen sufficiently
small, gives a fixed power saving in the total modulus sum. This is a
valid resource, but its modulus budget is about X^{1-beta}, not X^{1/2}.

It does not directly repair the source's polynomial-prime substitution.
If selected primes have size X^eta with fixed eta>0, the number of selected
prime divisors of n comparable to X is bounded, but exact expansion of a
mark can still produce divisors d as large as X. Applying (18) at the
remaining length X/d and summing absolute coefficients produces
X^beta sum_d |c_d|d^-beta. At the longest allowed divisors this need only
have size X times a logarithmic saving. A fixed low-degree truncation does
not have a power-small remainder. Therefore the new polynomial-modulus
budget is useful, but it neither controls every marked divisor nor removes
the source's separate dirty-edge problem.

## 7. Factoring inert primes from a path: an exact identity and its limit

A different attempt was to enlarge the source's auxiliary list length J
to a power of X, while avoiding its enormous apparent root modulus.
For a fixed 2R-edge path, at most 2R entries per band can depart from the
initial list. All other initial primes are inert: they remain active at
every vertex. Let I be their squarefree product.

For a path vertex P_j=(u_j,v_j), I divides u_j. Define
P'_j=(u_j/I,v_j). If each actual shared product is D_j=I D'_j, then

\[
 \frac{\det(P_j,P_{j+1})}{D_j}
               =\frac{\det(P'_j,P'_{j+1})}{D'_j}.         \tag{20}
\]

At primes outside I the diagonal coordinate change is invertible, so
the corresponding projective-line incidences are preserved. Primitivity
becomes gcd(u'_j,v_j)=1 together with gcd(I,v_j)=1. For the damping
factor define the reduced prime count by
omega_rem(u'_j)=sum_(p not dividing I) 1_(p divides u'_j). Then
omega(u_j)=omega(I)+omega_rem(u'_j), with the same band restriction on
each count. Subtracting the inert list entries cancels omega(I) from the
damping exponent. Using the original omega(u'_j) instead would be wrong
when an inert prime still divides u'_j. These assertions are exact for
the **unprojected** path kernel, with this reduced counting convention.

There are two remaining failures in the attempted power estimate.

First, the source's good-state projector tests every hypothetical omitted
list entry, not just the entries departing along the chosen path. Such a
hypothetical shared product may omit a prime in I, so it is not divisible
by I. The fixed good-state test therefore still depends on the full initial
list. Replacing it by a test only along the realized path changes the
operator and invalidates the existing Schur/moment argument. Equation (20)
alone does not reduce the modulus of that projected operator.

Second, even if that projection problem were solved, the current
trace-to-pairing estimate retains an active-list dimension factor. If all
auxiliary primes are between X^eta and X^{2eta}, removing the inert part
leaves at most 2KR active initial primes. The crude bound for the remaining
shared-product factor, together with Y, is X^{2eta(2KR+K)}. Its 2R-th
root costs X^{2eta K+eta K/R}. Harmonic list collisions require J^2/p_min
small. Using only p_min>=X^eta gives the uniform lower-endpoint budget
nu<eta/2 for J=X^nu, while the dirty-edge gain is
only J^{-K/2}=X^{-nu K/2}. Combining these available bounds gives no net
power saving. This is a failure of that upper-bound calculation, not a
lower bound on the true operator norm.
A stronger estimate conditioned on the actual endpoint list might change
this comparison, but none is proved here.

Iterating a constant contraction does not evade these issues: a moment
bound ||A^R||<=lambda^R gives ||A||<=lambda after the R-th root, not
X^{-c}. To use repeated blocks without taking that root would require an
exact scale-recursion identity for the original correlation and a controlled
remainder. The Type I calculation (16) shows that the direct Vaughan
recursion retains a unit multiplier on its target mode.

## 8. Power-small coverage by a different prime selector

There is an exact way to replace the source's large rough remainder by a
power-small smooth remainder. It changes the selected-prime family and
does not license the existing determinant estimate for that new family.

For fixed A>0 put y=(log X)^A and let omega_y(n) count the distinct prime
divisors of n exceeding y. For every n,

\[
 \mu(n)1_{P^+(n)>y}
  =-\sum_{\substack{ap=n\\p>y\ {\rm prime}\\(a,p)=1}}
                    \frac{\mu(a)}{1+\omega_y(a)}.         \tag{21}
\]

For squarefree n, each eligible p contributes -mu(n) on the right before
the initial minus sign, and 1+omega_y(a)=omega_y(n). For nonsquarefree n,
either the coprimality condition fails or mu(a)=0. This proves (21) exactly.

Rankin's inequality gives, for every epsilon>0,

\[
 \Psi(2X,y)\ll_{A,\epsilon}
                  X^{\max(0,1-1/A)+\epsilon}.             \tag{22}
\]

Indeed choose a fixed positive sigma slightly larger than
max(0,1-1/A). Then
Psi(2X,y)<=(2X)^sigma product_{p<=y}(1-p^-sigma)^-1, and the logarithm
of the finite product is O_sigma(y^{1-sigma}+log y)=o(log X).
Taking the preliminary sigma loss smaller than epsilon proves (22).

For the full shifted prime correlation with n in (X,2X), the contribution
from P+(n)<=y is therefore, after averaging the shifts and dividing by H,

\[
 O_{W,K,A,\epsilon}
            (X^{\max(0,1-1/A)+\epsilon}).                \tag{23}
\]

The logarithmic von Mangoldt factor is absorbed into epsilon, and
sum_h |K(h/H)|=O_K(H). At A=4 this is X^{3/4+epsilon}, a genuine fixed
power bound for the discarded part. It does not rely on the independent
CRT approximation used by the source's narrow-band marks.

The retained coefficient in (21), however, cannot simply be treated as
another copy of the original Möbius coefficient. For Re s>1 define

\[
 F_{\rho,y}(s)=\sum_n\frac{\mu(n)\rho^{\omega_y(n)}}{n^s}
 =\prod_{p\le y}(1-p^{-s})\prod_{p>y}(1-\rho p^{-s}),
                    \qquad0\le\rho\le1.                 \tag{24}
\]

Since (1+omega_y(a))^-1=integral_0^1 rho^{omega_y(a)}d rho, the new
coefficient averages the family (24). For 0<rho<1 it factors as

\[
 F_{\rho,y}(s)=\zeta(s)^{-\rho}\mathcal H_\rho(s)
       \prod_{p\le y}\frac{1-p^{-s}}{1-\rho p^{-s}},       \tag{25}
\]

where H_rho is an absolutely convergent, nonzero Euler product on
Re s>1/2, uniformly on compact strips and 0<=rho<=1. For each fixed y,
the nonzero factor in (25) leaves the principal branch (s-1)^rho at one.
Consequently a below-one power estimate for these intermediate coefficients
would be false even under a global zero-free half-plane, unless its
principal contribution were included. Moving y does not justify ignoring
this principal contribution.

The cancellation is coherent only in the full prime-factor expression:

\[
 -\partial_\rho F_{\rho,y}(s)
 =F_{\rho,y}(s)\sum_{p>y}\frac{p^{-s}}{1-\rho p^{-s}},
\]

\[
 F_{1,y}(s)-F_{0,y}(s)
 =-\int_0^1F_{\rho,y}(s)
                  \sum_{p>y}\frac{p^{-s}}{1-\rho p^{-s}}\,d\rho.
 \tag{26}
\]

Here F_{1,y}=1/zeta and F_{0,y} is the finite small-prime Euler product.
Equation (26) is the Dirichlet-series form of (21); it retains the local
coprimality condition through the factor (1-rho p^-s)^-1.

**Coherent Type II consequence.** In (2), replace the v-coefficient by
g_y(v)=mu(v)1_{P+(v)>y}, equivalently by the complete right side of (21)
or its finite rho integral. Put gamma=max(0,1-1/A)+epsilon. Its cumulative
sum on v comparable to X is bounded by C X^beta+O(X^gamma), since it is
M(v) minus the smooth-number Möbius prefix. Applying (5) with this prefix
in place of the second M gives, when H=cX and B_N<<N(log X)^C,

\[
 T_H^{>y}/H\ll (X^\beta+X^\gamma)M^{\beta-1}(\log X)^C.
 \tag{27}
\]

The smooth complement separately satisfies the same bound with X^gamma
alone. Thus at A=4 and beta=7/8, the **entire** broad-selector Type II
expression has the contraction (4). This bound is justified by integrating
the coherent prime-factor expression before taking absolute values; no
false Mertens estimate is imposed on an intermediate rho coefficient.
All sums and the rho integral are finite at a fixed X, so this recombination
does not require interchanging an uncontrolled analytic limit.

After this recombination the full Vaughan Type I term is still (14).
Cancelling the intermediate fractional branch at s=1 therefore does not
cancel the limiting unit coefficient on the target Mellin mode in (16).

The source's fixed-rho narrow-band determinant estimate itself neither covers
the selected primes all the way up to X nor the integration to rho=1.
Near rho=1 its current Fock damping constants lose uniformity. Taking
absolute values in rho or estimating the a-coefficient separately also
loses the exact principal-term cancellation in (26). Thus (21)-(23)
solve the coverage problem at a fixed power, but do not solve the retained
arithmetic correlation. They give a specific alternative to merely adding
more narrow bands, with the remaining analytic problem displayed.

## 9. An oscillatory-prime input and the scale of the retained signal

I inspected the primary source Yangbo Ye, *Zero density in short strips and
short-interval bounds toward Hypothesis S*, arXiv:2610.15989v2, Theorem 1.3,
at <https://arxiv.org/html/2610.15989v2>. Its prime phases are e(alpha n^b)
on intervals of length X^delta, with delta>1-b and fixed nonzero alpha.
This is a height-density and oscillatory-prime input, not a conductor-family
bound for the native inverse. No such uniformity is inferred here.

The following applicability calculation is independent of that source.
For v comparable to X, b in (0,1), and a smooth K supported in (1,2), put

\[
 A_X(v)=\int e(\alpha p^b)K((v-p)/H)\,dp,\qquad H=X^\delta.
\]

Suppose H<=X/4. On changing variables p=v-Hy, the y-phase derivative has
magnitude comparable to H X^{b-1}=X^{b+delta-1}, with no stationary point.
Higher normalized derivatives are uniformly bounded because H/X<=1/4.
Repeated integration by parts therefore proves

\[
 A_X(v)\ll_J H X^{-J(b+\delta-1)}\qquad(J\text{ fixed}). \tag{28}
\]

In the strict regime delta>1-b this eliminates the continuous prime-density
term to arbitrary power precision. Multiplying the outer Möbius factor by
e(-alpha v^b) does not change that magnitude. At the critical scale
delta=1-b a nonzero continuous signal may remain, but that scale is outside
the stated strict oscillatory regime. Fully compensating the phase inside
the kernel would simply restore the original nonoscillatory correlation.

Thus this direct insertion can produce oscillatory correlation estimates,
but it does not preserve the ordinary Mertens signal used by the present
zero detector. This is a scoped application check, not a general obstruction
to every use of short-strip density or oscillatory prime sums.

## 10. Conclusion of this pass and verification scope

The new all-scale estimate is (3)-(4), with the full Type II bound (11).
For example choosing U=X^{3/5}, V=X^{1/5} in the long-average decomposition
gives T_3/H<<X^{4/5+epsilon} under Mertens exponent 7/8+epsilon. This
closes the Type II component at the first-pass 4/5 target. Its Type I
component, however, is exactly the Mertens main term plus smaller errors;
the full correlation target remains unproved.

The other rigorous components are the complete affine second-moment
identity (17), the conductor-uniform estimate (18)-(19) under its explicit
global family cap, the unprojected inert-factor identity (20), and the
power-small smooth remainder (21)-(23).
Their missing transfers are stated above, rather than counted as achieved
power estimates for the source's full projected operator.

`check_averaged_hlc.py` checks the mixed summation-by-parts identity using
actual Möbius values and exact rational compact profiles, the smooth
Vaughan identity with formal prime logarithms, and the complete affine
average with exact rational complex arithmetic. It also verifies the broad
prime-selector identity (21), including nonsquarefree inputs. These finite checks verify
the algebraic identities; they do not verify premise (1), the all-family
cap in Section 6, or a new zero-free region.
