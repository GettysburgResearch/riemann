# A coefficient-faithful Gauss inverse decomposition and a stronger ordinary component

Status: exact finite algebra, and a source-dependent analytic estimate for
an ordinary-character component. No estimate for the complete native
Möbius inverse and no smaller zero-free half-plane is proved here.

Scope: the original Eisenstein sextic symbol, natural nonunit zeros,
squarefree columns, a common smooth profile, and all nonzero frequency
rows. The positive estimate in Section 5 refines an intermediate bound;
the complete divisor ledger has the same worst-case exponent as
`MOVING_TWIST_MOMENT.md`. The finite inverse decomposition is an attempted
route from that theorem to the actual post-Poisson coefficient, not a
claim that changing the coefficient is harmless.

Exact sources: PR1020 at
`c690f96fe6876f945398b3e2779810c563a64743`, its fifth-pass
`SEXTIC_ROW_PHASE_CANCELLATION.md` (blob
`3a5d7adcc24ec8907be5c8fd6879d81736d44788`),
`PR1019_COEFFICIENT_TRANSFER_AUDIT.md` (blob
`945847ee7d1bc1ba0836f916dfabb01b9ae56a9b`), and the exact arithmetic
source `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`,
`preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`
(blob `268c4e3206d460c617d3d2129742a72b831b3def`). Section 5 additionally
uses that source's `eq:cubic-large-sieve`, stated there as
Heath--Brown's Theorem 2, and `lem:sextic-large-sieve`. Neither source
input nor its full global application is independently certified here.

What was run: `check_native_gain.py`, an exact synthetic algebra control
over the quadratic number field Q(zeta_6). It checks 3,000 inverse
coefficients, 632 finite Heath--Brown coefficients, and 72 complete row
transport identities. It is not a native Gauss-sum implementation or
evidence for an asymptotic estimate.

## 1. The exact twist in cubic Gauss multiplication

All ideals are outside the same fixed omitted set S containing the
primes above 6; use their primary generators and the additive character
of the pinned source. Extend

\[
             g(n)=\gamma_2(n)
\]

by zero off squarefree ideals, and put g(1)=1. For coprime squarefree
d,e, the Chinese remainder parametrization x=e y+d z in the Gauss sum
gives

\[
 \gamma_2(de)=\gamma_2(d)\gamma_2(e)
                  \chi_d(e)^2\chi_e(d)^2.
\]

The fixed sextic reciprocity sign has square one. Consequently

\[
        g(de)=g(d)g(e)t(d,e),\qquad
        t(d,e)=\chi_e(d)^4=\chi_d(e)^4.                 \tag{1}
\]

No ordinary multiplicativity of g is being asserted. For pairwise
coprime d,e,h, symbol multiplicativity gives the cocycle identity

\[
             t(d,e)t(de,h)=t(e,h)t(d,eh).              \tag{2}
\]

Define, on functions supported on squarefree ideals,

\[
 (a\star b)(n)=
       \sum_{\substack{de=n\\(d,e)=1}}a(d)b(e)t(d,e).
                                                            \tag{3}
\]

Set it to zero for nonsquarefree n. Equations (1)--(2) prove that this
is a commutative associative convolution with identity delta_1.
It is a unitary, twisted convolution; its coprimality is essential.
The identity follows from finite sums, without an Euler product
convergence question.

Let f=mu g. For squarefree n,

\[
 (g\star f)(n)=g(n)\sum_{e\mid n}\mu(e)=\delta_1(n),
 \qquad\boxed{g\star f=\delta_1.}                       \tag{4}
\]

Multiplying g and f by a common completely multiplicative unitary
ray/angular character preserves (1)--(4); a common natural zero mask
is also permitted. The fixed ray function G in the actual first-Poisson
formula is dealt with by its source's fixed finite character expansion.
It is not silently assumed to be completely multiplicative.

## 2. A finite Heath--Brown identity in this algebra

For y>=1 write g_y(n)=g(n)1_(Nn<=y), and take an integer k>=1. Then

\[
 \boxed{
 g(n)=\sum_{j=1}^k(-1)^{j+1}\binom kj
             (g_y^{\star j}\star f^{\star(j-1)})(n),
             \qquad Nn\le y^k.}                        \tag{5}
\]

**Proof.** Put r=delta_1-f star g_y=f star(g-g_y).
Its support has norm greater than y. Thus r^(star k), and also
g star r^(star k), vanish at norms at most y^k. Expand the latter
using the binomial formula and g star f=delta_1. This is (5).
The proof also specifies why no assertion beyond y^k follows. All
coefficient sums are finite. No claim of novelty for the usual
Heath--Brown algebraic mechanism is intended; its exact Gauss cocycle
and induced row twist are the relevant features here.

At k=2,

\[
                  g=2g_y-g_y\star g_y\star f.
                                                            \tag{6}
\]

For squarefree r define

\[
 d_y(r)=\#\{(a,b):ab=r,\ Na\le y,\ Nb\le y\}.
\]

The two factors are automatically coprime, and (1) gives
g_y star g_y(r)=d_y(r)g(r). Hence, whenever y<Nn<=y^2,

\[
       g(n)=-\sum_{\substack{rc=n\\(r,c)=1}}
                        d_y(r)g(r)\mu(c)g(c)t(r,c).
                                                            \tag{7}
\]

This really does expose the coefficient mu gamma_2 to which the new
moment theorem applies. It also exposes all of the outer factors and
their moving conductor; they cannot be omitted.

## 3. The complete row identity and the exact moving twist

Let D>=2, y=sqrt(2D), and V be a common smooth profile supported in
(1,2). Take a completely multiplicative fixed ray/angular factor
theta. With all the original masks retained, put

\[
 G_u(D)=D^{-1/2}\sum_n g(n)\theta(n)\chi_n(u)V(Nn/D).
\]

Every n in this sum lies between y and y^2. For each squarefree r put

\[
 F_{u;r}(X)=X^{-1/2}
 \sum_{(c,r)=1}\mu(c)g(c)\theta(c)
               \chi_c(u r^4)V(Nc/X).
\]

Then (7), multiplicativity, and
R^(-1/2)(D/R)^(-1/2)=D^(-1/2) give the exact identity

\[
 \boxed{
 G_u(D)=-\sum_r\frac{d_y(r)g(r)\theta(r)\chi_r(u)}{\sqrt{Nr}}
                        F_{u;r}(D/Nr).}                \tag{8}
\]

There is no row-dependent choice of a new column profile: the same V
appears at its explicitly shifted scale. The new character is
chi_c(u)chi_c(r)^4, including zero at any prime shared by c and r.
The coprimality in the definition of F is retained even though that
zero already enforces it. A prior puncture (n,Q_0)=1 appears separately
in r and c, and every fixed omitted prime remains omitted.

Thus the meaningful conductor is rad(r), as in the moving-twist
theorem. Bounding (8) by allowing an arbitrary row of norm
Nu (Nr)^4 incurs an unnecessary and much larger cost.

## 4. What the new moment proves for each block, and the remaining loss

Let the physical u rows have norm about A and a common nonnegative
weight. Write G_(u,R) for the norm-R dyad of the exact outer r sum in
(8). Apply `MOVING_TWIST_MOMENT.md` to each fixed r, with
X=D/R and Q=Nr (an upper bound for its radical). There are
O_epsilon(R^(1+epsilon)) such ideals and d_y(r)<<_epsilon R^epsilon.
Minkowski in the weighted row Hilbert space gives

\[
 \begin{split}
 \sum_u w(u)|G_{u,R}|^2\ll (AD)^\epsilon\{&
 AR+D R^{1/3}+A^{1/4}D^{1/2}R\\
 &+\mathbf1_{\ell=-1}A^{5/6}D^{1/3}R^{2/3}\}.
 \end{split}                                               \tag{9}
\]

Here theta has fixed angular order ell, and the other smooth/height
conventions are those of the moving-twist theorem. Bounded subunit X
can be treated directly. Equation (9) is a bound for a genuine piece
of the exact Gauss decomposition, not a bound for an altered coefficient.
It improves the former separate-twist cost D sqrt(R) to D R^(1/3).

It does not close the full inverse. The identity includes R comparable
to D, where (9) can cost AD and the trivial bound is already that size.
Such terms are algebraically present: for a squarefree semiprime n=pq
with Np,Nq<=y and Nn>y, the branch r=n,c=1 in (7) has d_y(n)=2.
There is no norm-power saving obtained by deleting that branch.
Higher fixed k in (5) replaces it by more coherently coupled inverse
factors, not by a theorem for a single common coefficient.

There is another quantitative loss before (8) can help the native
consumer. In the common-divisor-free native first-Poisson block, the
dual row width is K=D^2/U and the external factor is U/D. Even an
ideal estimate of row-volume size K for the separated dual square
costs

\[
                         (U/D)K=D.                       \tag{10}
\]

For U<D this is larger than the inherited nonvolume scale
D^(5/6)U^(1/6). The signed Fourier-frequency phase, which the positive
dual mean has discarded, must therefore also be used in a successful
return to the raw native inverse. Formula (10) is a budget for this
specific positive-majorant route, not an impossibility theorem for
the exact signed sum.

## 5. Optional stronger ordinary estimate using both cubic and sextic rows

The powerful-frequency proof in `MOVING_TWIST_MOMENT.md` gives
K+K^(3/4)(FQ)^(1/2)+K(FQ)^(1/3). The ordinary-character component
admits the sharper source-dependent bound

\[
 \boxed{
 \mathcal O(K,X;F,Q)\ll(KX FQ)^\epsilon
           \{K+K^{2/3}(FQ)^{1/2}+K(FQ)^{1/3}\}.}       \tag{11}
\]

The notation, nonprincipal restriction, original natural character,
common profiles, and permitted extra punctures are exactly those of
that note's Section 2. This claim additionally imports the pinned
squarefree cubic large sieve. No zero-free hypothesis is used.

### A unique decomposition with two useful row variables

Write the good part of a nonzero frequency uniquely as

\[
                    k=r s^2 t,                          \tag{12}
\]

where r consists of the primes of valuation one, s consists of the
primes of valuation two, and every prime of t has valuation at least
three. Thus r,s are squarefree and r,s,t are pairwise coprime.
Let Nr~R, Ns~S, Nt~L, so R S^2 L~K. Put

\[
                       C=N\operatorname{rad}(t)FQ.
\]

For each fixed s,t the variable r occurs through a sextic character.
For each fixed r,t the variable s occurs through the cubic character
chi_n(s)^2. Both ordinary inducing characters have conductor times
redundant radical at most a constant times R S C. This counts every
natural zero once; it does not erase the phase at a repeated prime.

The squarefree cubic and sextic large sieves both give, at row scale
H and arbitrary common divisor-bounded full columns of scale X,
the normalized estimate H+X+(HX)^(2/3), up to small powers. The full
column extension follows from the same powerful-column decomposition
as the parent note, with the relevant character order unchanged.

Remove principally induced rows before reflection. On a fixed s,t
slice, reflection returns a common polynomial with variable sextic
row r and scale at most R S C/X; on a fixed r,t slice it returns one
with variable cubic row s and the same scale budget. The original
masks at the other fixed factors are common column coefficients.
The coprimality of the variable row to those fixed factors is a
row restriction; after exact nonprincipal reflection its positive
mean may be enlarged. There is no arbitrary pair-dependent mask
inside either sieve.

Taking the better of a sum and its reflection makes the effective
column scale at most sqrt(R S C). Consequently summing over the fixed
s variable after the sextic estimate gives

\[
           RS+R^{1/2}S^{3/2}C^{1/2}+RS^{4/3}C^{1/3},
                                                            \tag{13}
\]

whereas summing over fixed r after the cubic estimate gives

\[
           RS+R^{3/2}S^{1/2}C^{1/2}+R^{4/3}SC^{1/3}.
                                                            \tag{14}
\]

Use (13) when R>=S, and (14) when R<=S. With Z=RS^2,
both cases are at most

\[
                   Z+Z^{2/3}C^{1/2}+Z C^{1/3}.          \tag{15}
\]

For example, if R>=S then S<=Z^(1/3), giving
R^(1/2)S^(3/2)=Z^(1/2)S^(1/2)<=Z^(2/3).
If R<=S, then S>=Z^(1/3), giving
R^(3/2)S^(1/2)=Z^(3/2)S^(-5/2)<=Z^(2/3).
The third terms satisfy the stated Z bound directly; all norms in
these nonempty dyads are at least a fixed positive constant.

### Sum the cubefull and omitted-prime parts

There are O_epsilon(L^(1/3+epsilon)) cubefull ideals t in a norm-L
dyad and Nrad(t)<=L^(1/3). For completeness, write
t=a^3 b^4 c^5 with b,c squarefree and coprime, assigning exponents
modulo three. Ideal counting, followed by the convergent sums of
(Nb)^(-4/3)(Nc)^(-5/3), proves this count; allowing the irrelevant
additional overlaps only increases its upper bound.

Since Z~K/L, the three contributions of (15), summed over this t
dyad, are at most

\[
 (KX FQ)^\epsilon\{
 K L^{-2/3}+K^{2/3}(FQ)^{1/2}L^{-1/6}
                          +K(FQ)^{1/3}L^{-5/9}\}.       \tag{16}
\]

All three dyadic L sums converge. The R,S dyads contribute only
logarithmically. Units and S-supported parts are separated into the
fixed finite character classes and summed with the convergent norm
powers 1 or 2/3. The squarefree-column and common-puncture identities
of the parent note then apply with their external bounded row
scalars, logarithmic d mass, and subpower puncture mass. This proves
(11), with every nonzero frequency retained.

### Its stronger small-common-divisor contribution and global limit

Insert (11) into the exact Poisson ledger with
K_0=B^2/A, K_fm=K_0 M/F^2 and weight A/(B M L).
For f=m=1, the middle term now costs

\[
                  (ABQ)^\epsilon A^{1/3}B^{1/3}Q^{1/2},
                                                            \tag{17}
\]

instead of A^(1/4)B^(1/2)Q^(1/2). More generally, before summing f,m,
the corresponding absolute contribution is

\[
 (ABQ)^\epsilon A^{1/3}B^{1/3}Q^{1/2}
               F^{-5/6}M^{-1/3}L^{-1}.                 \tag{18}
\]

There is no improved complete exponent obtained by summing (18)
without its support. For K_0>=1 retain the Fourier tail more sharply:
its dyadic frequency sum is at most
H^(2/3) min(1,H^(1/3)), H=K_0 M/F^2.
For F<=sqrt(K_0), summing the F^(-5/6) part costs K_0^(1/12).
For F>sqrt(K_0), use

\[
 M^{-1/3}\min(1,(K_0M/F^2)^{1/3})
                         \le (K_0/F^2)^{1/3},
\]

so that the remaining f sum is bounded by
K_0^(1/3) sum_(F>sqrt(K_0)) F^(-3/2)
<<K_0^(1/12), up to divisor losses. Thus both ranges restore
A^(1/4)B^(1/2)Q^(1/2), the parent theorem's global term.
When K_0<1, its original simpler proof remains a valid global bound.

This is why (11) is retained as an actual component improvement,
especially for small fixed f, while (17) is not promoted to a bound
for the whole native sum.

## 6. Verification and remaining analytic work

The checker constructs a symmetric bilinear sextic-symbol model with
natural gcd zeros and defines its Gauss coefficients by the cocycle
(1). Arithmetic in Q(zeta_6) is exact. It verifies (4)--(8), detects
70 incorrect fourth-to-third row-twist substitutions, and rejects
43 instances of ordinary multiplication in place of the cocycle.
It also checks that (5) fails somewhere beyond its licensed support
in both retained test cases. These are meaningful algebra controls,
but not checks of actual Eisenstein Gauss values or infinite sums.

The remaining problem is a coherent estimate for (8) that keeps the
outer short-factor signs and, on returning to the inverse, the signed
Fourier-frequency kernel. The new estimates price those exact
constituents more efficiently. They do not provide the cancellation
across constituents that would improve the zero-free boundary.
