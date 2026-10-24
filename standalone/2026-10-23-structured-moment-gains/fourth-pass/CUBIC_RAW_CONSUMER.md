# The complete first-Poisson consumer for a cubic raw inverse moment

Status: explicit algebraic reduction and conditional consumer. The
rectangular estimate identified below is not proved here. The numerical
boundary in Section 4 is a conditional target.

Scope: Eisenstein primary generators, the cubic character with its zero
extension, the normalized cubic Gauss coefficient of the first-moment
source, fixed angular/ray coefficient data, and a fixed initial set of
omitted primes. No transposition of a structured coefficient vector is
used. This note uses the cubic symbol throughout; the sextic raw inverse
has a different first-Poisson column.

Sources: `openai/math@1581d4cbdd69a0faf34b2089614fe2a814316a6a`, cubic
first-moment `sections/dispersion.tex`, `eq:poisson`, with its primary
coset normalization; its elementary primitive Gauss evaluation and
Gauss multiplicativity. The amplification proof is the cubic version of
`eq:sixth-power-column-identity` and `lem:inverse-amplification` in the
quasi-Riemann paper at the same commit. The accepted scope of the related
structured Gauss theorem is the frozen third-pass packet at
`GettysburgResearch/riemann@f11e86684905c6417683a9f45ac75c223da6a162`.

## 1. Original moment and its genuine diagonal

Let $W$ be a nonnegative smooth radial plane weight in a fixed annulus,
$V$ a smooth norm-annular weight, and
$c_b=\mu(b)\theta(b)V(Nb/D)$, with the fixed omitted-prime mask included.
Define

\[
I_\theta(H,D)=\frac1D\sum_{a\equiv1\ (3)}W(a/\sqrt H)
                   \left|\sum_b c_b\chi_b(a)\right|^2.          \tag{1}
\]

The genuine pair diagonal is exactly

\[
\mathcal D=\frac1D\sum_b|c_b|^2
             \sum_{(a,b)=1}W(a/\sqrt H)\ll H                 \tag{2}
\]

for $H\ge1$, with the primary condition retained in the inner sum.
The rows have no squarefree restriction.

For each unequal pair write $b_i=fp_i$, where $f,p_1,p_2$ are
squarefree, $(p_1,p_2)=1$, and $(p_1p_2,f)=1$. Remove $(a,f)=1$ by
$\sum_{m\mid f}\mu(m)1_{m\mid a}$, and put $F=Nf$, $M=Nm$.
With $\lambda=\sqrt{-3}$ and
$\varepsilon(k)=e(\operatorname{Tr}(k/(3\lambda)))$, the exact
nonzero-frequency expression for $I_\theta-\mathcal D$ is

\[
\frac H{9D}\sum_f\sum_{m\mid f}\frac{\mu(m)}M
\sum_{p_1,p_2}^{\prime}
\frac{c_{fp_1}\overline{c_{fp_2}}G(p_1)\overline{G(p_2)}}
     {\sqrt{Np_1Np_2}}
\sum_{k\ne0}\varepsilon(k)
\widehat W\!\left(\frac{k\sqrt H}{3\lambda\sqrt M\,p_1p_2}\right)
\overline{\chi_{p_1}(k/m)}\chi_{p_2}(k/m).                     \tag{3}
\]

The prime means the stated squarefreeness and coprimalities and excludes
$p_1=p_2=1$. The inverse of $m$ is residue notation on its actual coprime
support. Primitive Fourier evaluation supplies
$G(p_1)\overline{G(p_2)}$; the cross CRT cubic factors cancel by
reciprocity. There is no extra $f$ in the cubic frequency argument in
(3): unlike the frozen structured Gauss theorem, the original columns
in (1) do not contain $G(fp_i)$.

The frequencies in (3) are all nonzero lattice frequencies, including
ramified multiples and nonsquarefree elements. The phase is signed and
cannot be dropped in an identity. For real radial $W$, pairing $k$ with
$-k$ replaces the phase by its real part, which takes the values $1$
and $-1/2$ in the three relevant residue classes. The radial transform
itself need not be nonnegative.

## 2. Exact masks after coprimality inversion

Extend the displayed nonzero-frequency expression formally to all
$p_1,p_2$, insert $\sum_{l\mid(p_1,p_2)}\mu(l)$, and put $p_i=ln_i$,
$L=Nl$. The surviving conditions include $(f,l)=1$ and
$(n_i,fl)=1$. Gauss multiplicativity is
$G(ln)=G(l)G(n)\overline{\chi_n(l)}$. Hence the external weight is
$\mu(m)\mu(l)/(ML)$, the row mask is

\[
|\chi_l(k/m)|^2=1_{(k,l)=1},                                  \tag{4}
\]

and the separated normalized column is

\[
\sum_{(n,fl)=1}\frac{\mu(n)\theta(n)G(n)}{\sqrt{Nn}}
 \overline{\chi_n(lk/m)}V(FLNn/D).                            \tag{5}
\]

The inverse in (5) can be replaced by $m^2$; its generated twist is
$v=lm^2$ and puncture is $Q=fl$. Both can move. Fixed-conductor
constants are therefore insufficient. Fixed omitted primes and their
zero masks remain present in (4)--(5).

Before common Mellin separation, the two-column kernel is precisely

\[
\widehat W\!\left(
\frac{k\sqrt H}{3\lambda\sqrt M\,l^2 n_1n_2}\right).
\]

Set

\[
K=D^2/H,\qquad A_{fm}=KM/F^2,\qquad B_{fl}=D/(FL).             \tag{6}
\]

A frequency dyad $Nk\asymp J$ has arbitrary decay
$(1+J/A_{fm})^{-R}$, with a common rapidly decreasing Mellin majorant
independent of the current row. The external normalization is
$H/(9DML)$. Subunit $A_{fm}$ must retain the same decay rather than
adding a spurious constant row count.

Formal extension adds the artificial pair $p_1=p_2=1$, so one subtracts
exactly

\[
U=\frac H{9D}\sum_{f\ {\mathrm{sf}}}|c_f|^2
  \sum_{m\mid f}\frac{\mu(m)}M
  \sum_{k\ne0}\varepsilon(k)
       \widehat W\!\left(\frac{k\sqrt H}{3\lambda\sqrt M}\right).
                                                                    \tag{7}
\]

Its frequency sum is $O(M/H)$ for every positive $M/H$, by Schwartz
decay and nonzero-lattice counting. Since $Nf\asymp D$, this gives
$U\ll D^\epsilon$; for $H>D$ stronger tail decay is available.
It is separate from the genuine diagonal (2).

## 3. A sufficient complete rectangular input

Let $\mathcal J_{v,Q}(A,B)$ denote the all-row normalized moment of the
column (5), including each generated common test profile and the finite
row masks. A sufficient bound for the complete consumer is

\[
\sum_{f,m\mid f,l}\frac1{ML}
 \mathcal J_{lm^2,fl}(KM/F^2,D/(FL))
 \ll D(HD)^\epsilon\qquad(K\le D),                           \tag{8}
\]

with the frequency-tail interpretation from (6). Positivity is used
only to majorize (3) at this stage. In particular the uniform estimate

\[
\mathcal J_{v,Q}(A,B)\ll (HD)^\epsilon(A+B)                  \tag{9}
\]

for the generated twists, punctures and profiles implies (8), because

\[
\sum_{f,m\mid f,l}\frac{A_{fm}}{ML}\ll K(HD)^\epsilon,
\qquad
\sum_{f,m\mid f,l}\frac{B_{fl}}{ML}\ll D(HD)^\epsilon.
\]

The first has $F^{-2}L^{-1}$ after cancellation of $M$; the second has
$F^{-1}M^{-1}L^{-2}$. The admissible ideal sums and divisor counts cost
only the stated power loss. Primary frequency representatives, units,
and exact powers of the ramified prime can be separated first; the
resulting finite cubic ray twists and their dyadic sums must also be
covered.

Equations (2), (7)--(9) give $I_\theta(H,D)\ll(H+D)(HD)^\epsilon$.
The principal block $f=m=l=1$ alone requires
$\mathcal J_{1,1}(D^2/H,D)\ll D^{1+\epsilon}$ when $H>D$.
Thus the frozen $A\ge B$ theorem does not cover the desired range,
and a fixed saving below its generic cross term is insufficient.

Bound (8) is sufficient, not necessary: exploiting the signs of (3)
before positive majorization is a different possible consumer.

## 4. Cube amplification and an explicit target

Suppose for every $c,\epsilon>0$ the complete raw estimate
$I_\theta(H,D)\ll H(HD)^\epsilon$ holds for $H\ge D^{\alpha+c}$,
uniformly on bounded smooth test families and their logarithmic scale
derivatives. Write
$M_u^V(D)=D^{-1/2}\sum_n\mu(n)\theta(n)\chi_n(u)V(Nn/D)$.
The original zero extensions give the exact identity

\[
M_u^V(D)=\sum_{d\mid\operatorname{rad}a}
 \mu(d)\theta(d)\chi_d(u)(Nd)^{-1/2}M_{ua^3}^V(D/Nd).         \tag{10}
\]

The total divisor weight is $(Na)^\epsilon$. Sobolev on logarithmic
scale intervals upgrades the raw estimate to a common scale supremum.
Averaging (10) for $u=1$ over $\gg H^{1/3}$ primary ideals
$Na\ll H^{1/3}$, and using injectivity of the cube map on these
generators, yields $|M_1^V(D)|^2\ll H^{2/3}(HD)^\epsilon$.
Consequently

\[
\sum_n\mu(n)\theta(n)V(Nn/D)
 \ll D^{1/2+\alpha/3+\epsilon}.                              \tag{11}
\]

The same test uniformity for $V_s(y)=V(y)y^{-s}$ on compact $s$-sets
gives holomorphic reciprocal continuation and zero-freeness to the
right of $1/2+\alpha/3$. For the Riemann zeta function one principal
Eisenstein result suffices by
$\zeta_E(s)=\zeta(s)L(s,\chi_{-3})$.

The explicit target $\alpha=28/25$ would give $131/150$
($0.873333\ldots$). It requires $K=D^{22/25}<D$ and the complete
estimate (8). The companion exponent-obstruction note shows why the
present size-only second-Poisson estimates do not prove this input.
