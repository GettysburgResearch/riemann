# Joint continuation by exchanging the two physical axes

**Status:** proposed source-conditional analytic theorems. Keeping the
actual divisor phases inside their completed polynomial, and resolving
the one-sided cube mask before exchanging the raw axes, enlarges the
holomorphic tube of the literal canonical and reunited three-cusp
functions. It also gives new square-root row means. The strongest
displayed balanced scalar is \(73/120\), approached from the interior.
It is not a zero-free exponent, an estimate for the original signed
moment remainder, or a proof of a generalized moment.

**Authorship:** /root/joint_spectral_attack, with the axis-exchange
direction suggested by root. Independent review must bind the final
source bytes. All inequalities below have analytic proofs; exploratory
linear programming is not used as a proof or as an imported hypothesis.

## 0. Exact inputs and scope

We retain the Eisenstein field, primary generators, fixed bad set \(S\),
fixed finite ray-character families, Gauss normalization, and literal
residue-symbol zeros of the following sources.

| Input | Exact source and role |
|---|---|
| Exact canonical divisor function | PR #925 mathematical source 5ad900ff27d34f1a8f94d28e19c47a3b37de6e39, standalone/2026-10-10-joint-divisor-covariance/JOINT_DIVISOR_MEAN.md, Sections 1–4 |
| Moving completed and raw norms | The same source, MOVING_AUXILIARY_ADAPTER.md, Theorems 2.1 and 3.1 and its separate fixed-ray-twist paragraph |
| Reunited three-cusp identity | PR #922 mathematical source 8f2acaacddc10bd8fb053a66070a1d06d25aa922, standalone/2026-10-10-signed-covariance-descent/FULL_CUSP_DESCENT.md, equations (1.2), (2.5), (2.6), and FINITE_RAY_REUNION.md, equation (4.3) |
| Classical squarefree sextic sieve | Blomer–Goldmakher–Louvel, Theorem 1.3, in the convention explicitly fixed by PR #925's joint-divisor note |
| Additional optimal fixed-order sieve | Alexandre de Faveri, [arXiv:2610.04045v1](https://arxiv.org/html/2610.04045v1), Theorem 1.1; its fixed-family adapter at PR #924 source 725b2d25ab47e57500049d93985560098c7ef3fa, standalone/2026-10-10-sextic-moving-labels/OPTIMAL_SIEVE_SPECTRAL_EXTENSION.md, Section 1 |

The imported theta foundation is OpenAI/math
adc7f1241b42e322a6451854ab7e4b4c146bf78a, October 5 paper2.tex,
including Proposition R and the exact cube inverse. This note does not
reprove that foundation, either large sieve, or the inherited cusp
transforms. All native claims here are deductions from those stated
inputs.

Let \(1/2<\beta\le1\), and write

\[
c=2\beta-1,\qquad \kappa_0=1-\frac c2=\frac32-\beta,
\qquad \delta=\frac{2\beta-2}{3}.
\tag{0.1}
\]

The value \(\beta=1\) uses counting in the scalar step and does not use
the angular reciprocal input. The value \(\beta=11/12\) retains exactly
the source-qualified angular premise of the moving adapter; it is not
an endpoint reciprocal theorem. The holomorphic continuation and the
classical \(5/8\) mean below require only \(\beta=1\). The two stronger
means explicitly state when they also use de Faveri or \(\beta=11/12\).

Rows remain squarefree primary \(k\), prime to \(S\), with
\(Q\le Nk<2Q\), \(Q\ge2\). Any subset of this row set is allowed.
The exact reflected-function identity is not asserted here for
nonsquarefree rows. Its positive-norm inputs may be restricted from
their larger all-row sets.

## 1. The exact function and its coherent blocks

Use the notation of the joint-divisor source:

\[
t=1-s,\qquad u=v-s,\qquad a=\Re u,\qquad b=\Re t,
\]
\[
\xi_1=\varrho,\qquad \xi_2=\kappa\varrho,\qquad
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n).
\tag{1.1}
\]

Here \(\kappa\) is the fixed ray character from that source and is
different from the real number \(\kappa_0\) in (0.1). At a permitted
good prime \(p\), of norm \(q\), put

\[
\begin{aligned}
c_k(p)&=\overline{\alpha(p)}^{\,3}\xi_1(p)^3\chi_k(p)^3,\\
\widetilde c_k(p)&=\kappa(p)^3c_k(p),\\
z_p&=\widetilde c_k(p)q^{1/2-3u},\\
A_p&=\kappa(p)c_k(p)q^{1/2-2t-u},\\
\Theta_k(d;u,t)&=\prod_{p\mid d}\frac{1-A_p}{1-z_p}.
\end{aligned}
\tag{1.2}
\]

Prime products omit \(kS\); the outer \(d\)-summand vanishes when
\((d,kS)\ne1\). Let \(\mathcal T_{k,d}(u)\) be the source's exact
canonical Gauss series multiplied by its cube Euler factor omitting
\(kdS\). The exact representation, initially in \(\Re u>1,\Re t>\Re u\),
is

\[
\boxed{
\mathcal Z_k(u,t)=
\frac{L_{S,k}(3t-\tfrac12,c_k)}
     {L_{S,k}(3u-\tfrac12,\widetilde c_k)}
\sum_d^*
\frac{a_{\xi_1}(d)\chi_k(d)\Theta_k(d;u,t)}{(Nd)^t}
\mathcal T_{k,d}(u).
}
\tag{1.3}
\]

The exterior ratio and its reciprocal are bounded uniformly in \(k\)
on compact real substrips \(a,b>1/2\). These are absolute Euler
half-planes, not assertions about zero-free regions.

For fixed smooth compact positive-norm tests \(V,W\), define

\[
\mathfrak B_{F,X}(k;u,t)=F^{-1/2}
\sum_d^* a_{\xi_1}(d)\chi_k(d)\Theta_k(d;u,t)
V(Nd/F)\,T_W(X;k,d).
\tag{1.4}
\]

Here \(F,X\ge1\), and the normalized physical inner completion is

\[
\begin{aligned}
T_W(X;k,d)=X^{-1/2}
\sum_m^*\sum_{(b_0,dS)=1}
&a_{\xi_2}(m)\chi_k(m)\chi_m(d)^4
\overline{\alpha(b_0)}^{\,3}\xi_2(b_0)^3
\chi_k(b_0)^3\sqrt{Nb_0}\\
&\times W\!\left(\frac{Nm(Nb_0)^3}{X}\right).
\end{aligned}
\tag{1.5}
\]

The ideal \(b_0\) is arbitrary. There is no condition
\((m,b_0)=1\). The masks \((m,d)=1\) and the row masks are
the literal character zeros. The mask \((b_0,d)=1\) is present.

Every block is finite and is holomorphic in \(u,t\) on \(a,b>1/2\).
The new completed estimates require smooth \(V\). We do not carry
forward PR #925's arbitrary-bounded-divisor-coefficient quantifier
through the angular scalar argument.

### 1.1 The exact correction does not become an arbitrary row weight

Write \(z_p=z_{0,p}\varepsilon_k(p)\),
\(A_p=A_{0,p}\varepsilon_k(p)\), with
\(\varepsilon_k(p)=\chi_k(p)^3\). At permitted primes,

\[
e_1(p)=\frac{z_{0,p}-A_{0,p}}{1-z_{0,p}^2},
\qquad e_0(p)=z_{0,p}e_1(p),
\]
\[
\Theta_k(d)=
\sum_{\substack{r_0r_1\mid d\\(r_0,r_1)=1}}
e_0(r_0)e_1(r_1)\chi_k(r_1)^3.
\tag{1.6}
\]

On any compact real substrip \(a,b>1/2\),

\[
\sum_{r_0,r_1}^{*}
\mathbf1_{(r_0,r_1)=1}|e_0(r_0)e_1(r_1)|
(Nr_0Nr_1)^\eta<\infty
\tag{1.7}
\]

for a sufficiently small fixed \(\eta>0\). This is the exact
quadratic rationalization proved in the source. It is used only at
units; at a common \(d,k\) prime the surrounding character is zero.
No identity \(\varepsilon_k(p)^2=1\) is used at such a nonunit.

Fix \(r=r_0r_1\) and put \(R=Nr\). Writing \(d=rj\), Gauss CRT gives

\[
a_{\xi_1}(rj)a_{\xi_2}(m)\chi_m(rj)^4
=a_{\xi_1}(r)\,a_{\xi_1}(jm)\kappa(m)\chi_{jm}(r)^4.
\tag{1.8}
\]

The surviving \(j,m,b_0\) all avoid \(r\). Thus this component of
(1.4), apart from its displayed \(e\)-coefficient, is exactly

\[
R^{-1/2}a_{\xi_1}(r)\chi_k(r)\chi_k(r_1)^3\,
\mathcal C^{(1,\kappa)}_{1,1}(F/R,X;k,r).
\tag{1.9}
\]

The notation \((1,\kappa)\) records the separate fixed ray characters:
the raw squarefree coefficient is \(a_{\xi_1}(jm)\kappa(m)\),
and the physical cube coefficient uses \(\xi_2^3=\xi_1^3\kappa^3\).
This is exactly the separate-ray extension of the moving adapter.
Its auxiliary is \(r\), on both surviving squarefree axes, with its
cube exclusion retained. The factor outside \(\mathcal C\) is a row
contraction. Nonempty \(F/R\) below one lies in a fixed compact positive
interval determined by the support of \(V\); the source's bounded-scale
convention applies.

## 2. Three bounds for the same completed joint block

### Theorem 2.1

Uniformly on compact real substrips \(a,b>1/2\), the block (1.4)
satisfies

\[
\|\mathfrak B_{F,X}\|_2^2
\ll (QFX)^\epsilon\,\mathcal N_J(V,W)^2
\min\{P_{\rm cl},C_\beta,S_1\},
\tag{2.1}
\]

where \(\mathcal N_J\) is a product of fixed finite smooth seminorms,

\[
P_{\rm cl}=Q+FX+(QFX)^{2/3},
\tag{2.2}
\]
\[
\boxed{
C_\beta=
QF+\frac{Q^2F}{X}\min(F,\sqrt X)^c
+Q^{4/3}F^{4/3}X^{-2/3},
}
\tag{2.3}
\]
\[
\boxed{S_1=QX+Q^2X+Q^{4/3}X^{4/3}.}
\tag{2.4}
\]

The \(C_\beta\) estimate uses the scalar premise at \(\beta\).
The exchanged-axis bound \(S_1\) uses only its counting choice
\(\beta=1\). With de Faveri's additional theorem, \(P_{\rm cl}\)
may also be replaced by

\[
\boxed{
P_{\rm opt}=
Q+FX+Q^{5/6}(FX)^{1/3}+Q^{1/3}(FX)^{5/6}.
}
\tag{2.5}
\]

All bounds include the exact \(\Theta\), its moving masks, and the
physical cubes. They are bounds for the same finite block.

### 2.1 The forward completed bound

Apply the inherited moving completed theorem to (1.9), with outer
scale \(F/R\), inner scale \(X\), exclusion \(q=1\), and auxiliary
\(f=r\). Its label costs are \(L=R\), \(M=R^{2/3}\).
After the squared normalization \(R^{-1}\), its three monomials are

\[
QF R^{-2},\qquad
\frac{Q^2F}{RX}\min(F/R,\sqrt X)^c,\qquad
Q^{4/3}F^{4/3}X^{-2/3}R^{-5/3}.
\tag{2.6}
\]

They are bounded by their \(R=1\) counterparts. Minkowski over the
absolutely summable coefficients (1.7) gives (2.3).
The smooth seminorm dependence follows by keeping the finite orders
of the two source test seminorms throughout that proof. In particular,
substituting \(y^{-t}V(y)\) or \(y^{-u}W(y)\) costs only a fixed
polynomial in the imaginary parts.

### 2.2 The polynomial bounds

For completeness, fixing \(b_0\) in (1.5) leaves the factor
\((Nb_0)^{-1}\) times a squarefree product polynomial in \(dm\),
at product scale \(FX/(Nb_0)^3\). Equation (1.8), or its \(r=1\)
case, combines the Gauss phases before the row norm is taken.
The resulting divisor coefficient has norm bounded by a divisor
function times the two smooth suprema. Its normalized squared
coefficient mass is \((FX)^\epsilon\).

Applying the classical squarefree sextic sieve and summing the
physical \(b_0\)-terms with weight \(1/Nb_0\) gives (2.2), exactly
as in PR #925. For (2.5), use the sixth-power-free operator of
de Faveri on its squarefree subfamily. Its four monomials are
precisely those in (2.5). Fixed reciprocity and \(S\)-unit classes
are partitioned before the sieve, as in PR #924's adapter; they do
not vary with the conductor.

For each energy term \(Q^\rho L^\sigma\) with \(\sigma>0\), the
Minkowski cube sum is bounded by
\(\sum_{b_0}(Nb_0)^{-1-3\sigma/2}\).
The \(Q\)-term has only a harmonic logarithm. Fixing a correction
\(r\) changes the product scale by \(R^{-1}\), in addition to the
outside norm factor \(R^{-1/2}\); all correction sums converge by
(1.7). This proves both polynomial assertions. There is no
sixth-power-copy row term here because the actual row set is
squarefree.

### 2.3 Exchanging the raw axes without deleting the cube mask

This is the additional arithmetic step. First consider
\(\mathcal C_{q,1}(A,B;k,f)\) with arbitrary squarefree \(q,f\),
including overlap, and fixed separate ray characters. Freeze its
physical cube ideal \(b_0\), which avoids \(qfS\), and put

\[
z=\operatorname{rad}(b_0),\qquad Z=Nz,\qquad B_0=Nb_0.
\]

In this auxiliary assertion, let
\(D=2+Q+A+B+Nq+Nf\) be the ambient size parameter. Every nonempty
physical cube term has \(B_0^3\ll B\), with a constant determined
by the fixed test support. Thus the cube and divisor labels and all
nonempty child scales below are bounded by fixed powers of \(D\),
as required by the moving adapter. After substitution of (1.9),
\(2+QFX\) serves as the ambient size parameter since \(R\ll F\).

The original outer squarefree variable \(d\) avoids \(b_0\), while
the inner squarefree variable \(m\) may meet it. Split it uniquely:

\[
\ell=(m,z),\qquad m=\ell m_0,\qquad \ell\mid z.
\tag{2.7}
\]

Then \(m_0\) avoids \(z\), and \(d,m_0\) are coprime and both
avoid \(z\). Conversely, these conditions with \(\ell\mid z\)
recover every original \(m\) once. The original factor \(d\)
already avoids \(\ell\), and \(m_0\) does too.

Gauss CRT gives

\[
a_\xi(d\ell m_0)
=a_\xi(\ell)a_\xi(dm_0)\chi_{dm_0}(\ell)^4.
\tag{2.8}
\]

The fixed ray factors at \(\ell\), and its row and original
\(f\)-characters, are kept as outside phases of modulus at most one.
Thus the raw child has global exclusion and common auxiliary

\[
q'=qz,\qquad f'=f\ell,
\tag{2.9}
\]

and, after exchanging its two raw axes, lengths

\[
A'=\frac{B}{B_0^3N\ell},\qquad B'=A.
\tag{2.10}
\]

This is a legitimate symmetric raw polynomial with global masks.
It is not a claim that an unhandled inner-only exclusion can be
treated as an outer exclusion. The split (2.7) resolves that issue
before the exchange. The two fixed ray characters are exchanged
with their axes.

Set \(L=N\operatorname{lcm}(q,f)\) and
\(M=N(q/(q,f))^{1/3}(Nf)^{2/3}\), as in the source.
Since \(b_0\) avoids \(qf\), the child label costs are exactly

\[
L'=LZ,\qquad M'=MZ^{1/3}(N\ell)^{1/3}.
\tag{2.11}
\]

The squarefree factor split contributes \((N\ell)^{-1/2}\)
to normalization, in addition to the original cube factor
\(B_0^{-1}\).

Use the source raw theorem at \(\beta=1\), hence \(\delta=0\),
on this child:

\[
\|\mathcal P_{q'}(A',B';\cdot,f')\|_2^2
\ll D^\epsilon
\left[QA'+L'Q^2A'+M'Q^{4/3}(A')^{4/3}\right].
\tag{2.12}
\]

Since \(Z\le B_0\), after square roots and multiplication by
\(B_0^{-1}(N\ell)^{-1/2}\), the three norm weights are bounded by

\[
\sqrt{QB}\,B_0^{-5/2}(N\ell)^{-1},
\]
\[
\sqrt{LQ^2B}\,B_0^{-2}(N\ell)^{-1},
\]
\[
\sqrt{MQ^{4/3}B^{4/3}}\,
B_0^{-17/6}(N\ell)^{-1}.
\tag{2.13}
\]

Each sum over \(\ell\mid z\) is bounded by a divisor function,
and all three \(b_0\)-sums converge absolutely after an arbitrarily
small power loss. This proves the uniform exchanged estimate

\[
\boxed{
\|\mathcal C_{q,1}(A,B;\cdot,f)\|_2^2
\ll D^\epsilon
\left[QB+LQ^2B+MQ^{4/3}B^{4/3}\right].
}
\tag{2.14}
\]

All physical sums were finite before the positive norm accounting.
No condition \((m,b_0)=1\) was inserted.

Finally apply (2.14) to (1.9). Here \(B=X,L=R,M=R^{2/3}\).
After the outside squared factor \(R^{-1}\), its terms are

\[
QX/R,\qquad Q^2X,\qquad Q^{4/3}X^{4/3}R^{-1/3}.
\tag{2.15}
\]

The exact correction sum (1.7) is therefore still absolutely
summable. This proves (2.4), and finishes Theorem 2.1.

## 3. A larger holomorphic tube for the literal function

Choose fixed smooth dyadic partitions on positive norms, including
a separate bounded first block when needed. In the absolute
chamber (1.3) becomes exactly

\[
\mathcal Z_k(u,t)=
\frac{L_{S,k}(3t-\tfrac12,c_k)}
     {L_{S,k}(3u-\tfrac12,\widetilde c_k)}
\sum_{F,X}F^{1/2-t}X^{1/2-u}
\mathfrak B_{F,X}[V_t,W_u](k),
\tag{3.1}
\]

where \(V_t(y)=y^{-t}V_0(y)\) and \(W_u(y)=y^{-u}W_0(y)\).
This reconstructs both original norm powers and the physical cube
power \(3u-1/2\) term by term. Every fixed test seminorm is bounded
by a fixed polynomial in \(|\Im u|+|\Im t|\).

### Theorem 3.1. Normal convergence of coherent blocks

The right side of (3.1) is locally normally convergent in the finite
row Hilbert space throughout

\[
\boxed{\mathcal D_{\rm exch}=
\{(u,t): a>\tfrac12,\ b>\tfrac12,\ 6a+8b>11\}.}
\tag{3.2}
\]

It gives a holomorphic continuation of the exact function (1.3).
On every bounded closed real subregion with strict margins,

\[
\boxed{
\|\mathcal Z_{\cdot}(u,t)\|_{\ell^2(k\asymp Q)}
\ll Q^{1+\epsilon}
(2+|\Im u|+|\Im t|)^M.
}
\tag{3.3}
\]

The continued function is independent of the chosen admissible smooth
dyadic partitions. No claim of convergence under arbitrary sharp
divisor truncation or arbitrary bounded \(d\)-weights is made.

**Proof.** Use only \(\beta=1\) in Theorem 2.1. For \(F,X,Q\ge1\),

\[
C_1\ll Q^2\left[F+F^{4/3}X^{-2/3}\right],
\qquad S_1\ll Q^2X^{4/3}.
\tag{3.4}
\]

The middle term in \(C_1\) is bounded by \(Q^2F/\sqrt X\le Q^2F\).
Consequently

\[
\min(C_1,S_1)\ll Q^2
\left[
\min(X^{4/3},F)+
\min(X^{4/3},F^{4/3}X^{-2/3})
\right].
\tag{3.5}
\]

Take square roots and multiply by \(F^{1/2-b}X^{1/2-a}\).
The two crossovers are \(X=F^{3/4}\) and \(X=F^{2/3}\).
For \(1/2<a<7/6\), their dyadic \(X\)-sums are bounded respectively by

\[
QF^{11/8-b-3a/4},\qquad
QF^{23/18-b-2a/3}.
\tag{3.6}
\]

For example the first lower summand is
\(QF^{1/2-b}X^{7/6-a}\), and its upper summand is
\(QF^{1-b}X^{1/2-a}\). Both geometric sums have the first size
in (3.6). The other upper summand is
\(QF^{7/6-b}X^{1/6-a}\), which gives the second size.

The difference between the two displayed \(F\)-exponents is
\((7-6a)/72>0\), so the first controls the second in this range.
For \(a>7/6\), both lower sums start with a bounded first block;
their total is \(O(QF^{1/2-b})\). At \(a=7/6\) there is only
a logarithm. Uniformly across that transition, a sufficient bound is
the sum of these three expressions times \(1+\log(2F)\).

These majorants give a convergent \(F\)-sum under the sufficient
strict conditions in (3.2). Choose preliminary losses below the compact
strip margins before either dyadic summation. This also proves (3.3)
with arbitrary final \(\epsilon\). Each block is holomorphic; normal
convergence gives holomorphy. The tube is convex and intersects the
initial absolute chamber. Equality there proves that this is the
continuation of the same function. The identity theorem similarly
proves independence of the smooth partitions. \(\square\)

For instance \(a=b=4/5\) lies strictly inside (3.2).
The previous sufficient divisor plane \(2b+a>3\) fails at that
point. This is a genuine continuation of the original exact object,
not a replacement obtained by setting \(\Theta=1\).

## 4. Square-root row means near the best spectral line

We first record a region preserving de Faveri's \(4/7\) spectral
threshold. It uses the forward joint completion and the exact support
minimum; it does not need the exchanged bound.

### Theorem 4.1

On strict bounded real subregions with \(a<1\), the estimate

\[
\boxed{
\|\mathcal Z_{\cdot}(u,t)\|_2
\ll Q^{1/2+\epsilon}
(2+|\Im u|+|\Im t|)^M
}
\tag{4.1}
\]

holds in each of these explicitly qualified regions:

| Inputs beyond the fixed theta foundation | Sufficient region |
|---|---|
| Classical sextic sieve, \(\beta=1\) | \(a>5/8,\quad b>(6-a)/5\) |
| De Faveri sieve, \(\beta=1\) | \(a>7/12,\quad b>(6-a)/5\) |
| De Faveri sieve, \(\beta=11/12\) | \(a>4/7,\quad b>(6-a)/5\) |

The first region will be enlarged further in Section 5.

### 4.1 An explicit weighted-geometric-mean lemma

Let \(A_{r,s}=Q^r(FX)^s\), with \(0\le r<1\), \(0<s\le1\).
The middle term of \(C_\beta\) is the exact minimum

\[
B_-=\frac{Q^2F^{1+c}}{X},\qquad
B_+=Q^2F X^{-\kappa_0}.
\tag{4.2}
\]

Put \(\alpha=1/(2-r)\) and \(\lambda=1-\alpha\). A weighted
geometric mean with weights \((\alpha,z,\lambda-z)\) gives

\[
F^{1-2b}X^{1-2a}\min(A_{r,s},B_-,B_+)\le Q
\tag{4.3}
\]

provided

\[
a\ge\frac{1+s}{2(2-r)},\qquad
b\ge\frac{3+s-2r}{2(2-r)},
\]
\[
2a+b\ge
\frac12\left[3+\frac{3s+(c-1)(1-r)}{2-r}\right].
\tag{4.4}
\]

Indeed the row power of the product is
\(\alpha r+2\lambda=1\). Its \(F\)- and \(X\)-powers after the
outside weight are nonpositive exactly when

\[
\max\!\left(0,
\frac{\alpha s-\kappa_0\lambda+1-2a}{1-\kappa_0}\right)
\le z\le
\min\!\left(\lambda,
\frac{2b-1-\alpha s-\lambda}{c}\right).
\tag{4.5}
\]

The three conditions (4.4) are precisely the three comparisons
that make this interval nonempty. This proves the lemma using
ordinary weighted geometric means.

For the last term \(B_2=Q^{4/3}F^{4/3}X^{-2/3}\), use weights
\((\theta,1-\theta)\) on \(A_{r,s},B_2\), where

\[
\theta=\min\!\left(1,\frac{2a-1/3}{s+2/3}\right).
\tag{4.6}
\]

If \(\theta<1\), the \(X\)-power cancels. The required lower
\(a\)-bounds for the row power to be at most one, and the required
\(b\)-bounds for a nonpositive \(F\)-power, are:

| \((r,s)\) | Required \(a\) | Required \(b\) |
|---|---:|---:|
| \((0,1)\) | \(3/8\) | \(6/5-a/5\) |
| \((2/3,2/3)\) | \(1/2\) | \(5/4-a/2\) |
| \((5/6,1/3)\) | \(1/2\) | \(4/3-a\) |
| \((1/3,5/6)\) | \(5/12\) | \(11/9-a/3\) |

If \(\theta=1\), the bound follows directly from \(A_{r,s}\),
since \(2a\ge1+s\), \(b>1\), and \(r<1\).
Thus all these comparisons hold under \(a>1/2\) and
\(b>(6-a)/5\), \(a<1\).

### 4.2 Checking the spectral thresholds

For the optimal polynomial's three nonconstant terms, the three
conditions in (4.4) read:

| \((r,s)\) | Lower bound for \(a\) | Lower bound for \(b\) | Lower bound for \(2a+b\) |
|---|---:|---:|---:|
| \((0,1)\) | \(1/2\) | \(1\) | \(2+c/4\) |
| \((5/6,1/3)\) | \(4/7\) | \(5/7\) | \((26+c)/14\) |
| \((1/3,5/6)\) | \(11/20\) | \(19/20\) | \((41+4c)/20\) |

For \(0<c\le1\), the largest final-column entry is
\((41+4c)/20\). The condition \(b>(6-a)/5\) gives
\(2a+b>(9a+6)/5\). Hence it is sufficient that

\[
a>\max\!\left(\frac47,\frac{17+4c}{36}\right)
=\max\!\left(\frac47,\frac{13+8\beta}{36}\right).
\tag{4.7}
\]

This is \(7/12\) at \(\beta=1\), and \(4/7\) at
\(\beta=11/12\). At the latter limiting point
\((a,b)=(4/7,38/35)\), the margins in the first and third
final-column inequalities are respectively \(17/840\) and \(1/84\).
The \(d=1\) spectral comparison still supplies the limiting \(4/7\)
condition; it has not been bypassed by taking the divisor sum.

For the classical pair \((r,s)=(2/3,2/3)\), (4.4) instead gives
\(a\ge5/8,\ b\ge7/8,\ 2a+b\ge(17+c)/8\).
Together with the linear pair, these hold throughout the first
region of Theorem 4.1, including \(c=1\).

### 4.3 Completing the dyadic proof

For nonnegative quantities,
\(\min(\sum_i x_i,y)\le\sum_i\min(x_i,y)\).
Applying this successively to the polynomial and the three completed
terms reduces their minimum to the finite comparisons above, the
base term \(Q\), and the term \(QF\). The latter two satisfy the
required weighted bound because \(a>1/2,b>1\).

Inside any strict region in the theorem, choose \(a'<a,b'<b\)
uniformly close enough that all the stated comparisons still hold.
Applying the weighted inequalities at \(a',b'\) proves

\[
F^{1-2b}X^{1-2a}\min(P,C_\beta)
\ll QF^{-2(b-b')}X^{-2(a-a')}.
\tag{4.8}
\]

The square-root double dyadic sum is geometric. Absorb the
preliminary \((QFX)^\epsilon\) losses below these strict margins.
Equation (3.1) and the bounded exterior Euler ratio prove (4.1).
This completes the proof of Theorem 4.1.

## 5. Stronger row means using the exchanged bound

### Theorem 5.1

The same square-root row estimate (4.1) holds in the larger rectangles

\[
\boxed{a>\frac58,\qquad b>1}
\tag{5.1}
\]

using the classical sextic sieve and \(\beta=1\), and

\[
\boxed{a>\frac{73}{120},\qquad b>1}
\tag{5.2}
\]

using de Faveri's sieve and \(\beta=11/12\) in the forward completed
bound. The exchanged estimate in (5.2) still uses only \(\beta=1\).
All statements are on bounded closed real subregions with positive
margins. The \(a\)-coordinate need not be kept below one here.

### 5.1 The counting proof

At the limiting point \(a=5/8,b=1\), set
\(T=QF X^{1/4}\). We prove pointwise

\[
\min(P_{\rm cl},C_1,S_1)\ll T.
\tag{5.3}
\]

The \(Q\)-term of \(P_{\rm cl}\) and the \(QF\)-term of \(C_1\)
are always at most \(T\).

If \(X\le Q^{4/3}\), the linear polynomial term \(FX\) is at most
\(T\). If also \(F\ge X^{5/4}/Q\), its mixed term is at most
\(T\), so use \(P_{\rm cl}\). Otherwise use the outer-support
middle term \(Q^2F^2/X\) of \(C_1\): its ratio to \(T\) is
\(QF X^{-5/4}<1\). The last completed term is also bounded,
because \(QF<X^{5/4}\le X^{11/4}\).

If \(X\ge Q^{4/3}\), the other middle term \(Q^2F/\sqrt X\)
has ratio \(QX^{-3/4}\le1\). If \(F\le X^{11/4}/Q\), the last
completed term is at most \(T\), so use \(C_1\). In the remaining
case, \(F>X^{11/4}/Q\), use \(S_1\). Its two nonredundant
ratios are

\[
\frac{Q^2X}{T}=\frac{QX^{3/4}}F
<Q^2X^{-2}\le1,
\]
\[
\frac{Q^{4/3}X^{4/3}}T
=\frac{Q^{1/3}X^{13/12}}F
<Q^{4/3}X^{-5/3}\le1.
\tag{5.4}
\]

This proves (5.3). Moving strictly right in both real coordinates
adds the summable factors
\(F^{-(b-1)}X^{-(a-5/8)}\) to the norm in (3.1).
The preliminary small losses are absorbed in those margins.
This proves (5.1).

### 5.2 The optimal-sieve and angular proof

At the limiting point \(a=73/120,b=1\), let

\[
T=QF X^{13/60}.
\tag{5.5}
\]

We prove
\[
\min(P_{\rm opt},C_{11/12},S_1)\ll T.
\tag{5.6}
\]

First suppose \(X\le Q^{5/4}\). The polynomial terms \(Q\)
and \(FX\) are at most \(T\). For the first mixed term,

\[
\frac{Q^{5/6}(FX)^{1/3}}T
=Q^{-1/6}F^{-2/3}X^{7/60}
\le Q^{-1/48}\le1.
\tag{5.7}
\]

The last mixed term is bounded if
\[
F\ge Q^{-4}X^{37/10}.
\tag{5.8}
\]

If (5.8) holds, use \(P_{\rm opt}\). Otherwise, the two requirements
for the nontrivial completed terms are

\[
F\le Q^{-6/5}X^{73/50},
\qquad F\le Q^{-1}X^{53/20}.
\tag{5.9}
\]

They follow from the failure of (5.8), since on the present
\(X\)-range

\[
\frac{Q^{-4}X^{37/10}}{Q^{-6/5}X^{73/50}}
=Q^{-14/5}X^{56/25}\le1,
\]
\[
\frac{Q^{-4}X^{37/10}}{Q^{-1}X^{53/20}}
=Q^{-3}X^{21/20}\le1.
\tag{5.10}
\]

The first inequality in (5.9) uses the exact support branch
\(Q^2F^{11/6}/X\). The second controls
\(Q^{4/3}F^{4/3}X^{-2/3}\). Thus \(C_{11/12}\ll T\).

Next suppose \(X\ge Q^{5/4}\). The other middle branch has
the bound

\[
\frac{Q^2F X^{-7/12}}T=QX^{-4/5}\le1.
\tag{5.11}
\]

If \(F\le Q^{-1}X^{53/20}\), use \(C_{11/12}\). Otherwise use
the exchanged counting bound \(S_1\), since

\[
\frac{Q^2X}{T}
=\frac{QX^{47/60}}F
<Q^2X^{-28/15}\le Q^{-1/3}\le1,
\]
\[
\frac{Q^{4/3}X^{4/3}}T
=\frac{Q^{1/3}X^{67/60}}F
<Q^{4/3}X^{-23/15}\le Q^{-7/12}\le1.
\tag{5.12}
\]

The \(QX\)-term is smaller than \(Q^2X\).
All cases are exhausted. This proves (5.6).
Strictly increasing \(a,b\) from the limiting point again supplies
two geometric margins for (3.1), and proves (5.2).
No endpoint row-mean estimate is asserted.

## 6. The actual reunited three-cusp function inherits these results

The source identity, with every ramified and bad-prime label present,
is

\[
\mathcal Y_k(s,v)=\sum_\lambda B_\lambda(s,k)
\mathcal Z_k(u,t;\varrho_\lambda),
\qquad u=v-s,\quad t=1-s.
\tag{6.1}
\]

The index \(\lambda\) here denotes the full source label list, not
only a cusp representative. Its fixed finite good-ray family obeys
\(\varrho_\lambda^3=\overline\rho^{\,3}\).
The exact source bound for its coefficient mass is

\[
|B_\lambda(s,k)|
\ll 3^{-j(b-1/6)}(Nb_0)^{-(3b-1/2)}.
\tag{6.2}
\]

The \(j\)-sum and every \(S\)-supported \(b_0\)-sum converge
absolutely already for \(b>1/6\), uniformly in \(k\) and the
imaginary coordinates. Every domain proved above has \(b>1/2\).
Thus (6.1) converges normally, and its total coefficient norm
is uniformly bounded, throughout the new domain (3.2).
It agrees with the original reunited function on the initial
absolute overlap and therefore continues that same function.

### Corollary 6.1

The complete reunited function is holomorphic on

\[
\boxed{
a=\Re(v-s)>\frac12,\qquad
\tau=\Re v<
\min\!\left(a+\frac12,\frac{14a-3}{8}\right).
}
\tag{6.3}
\]

It has the row norm \(O(Q^{1+\epsilon})\), up to a fixed vertical
polynomial, there. On the regions of Theorems 4.1 and 5.1 it has
the sharper norm \(O(Q^{1/2+\epsilon})\), with all cusp cross terms
retained by Minkowski. No orthogonality between those sectors is
claimed.

The source reflected function satisfies
\[
\mathscr R_k(w,s)=H_\Gamma(s)(Nk)^{1-2s}\mathcal Y_k(s,v).
\tag{6.4}
\]

Its explicit common gamma factor is
\[
H_\Gamma(s)=\frac{i}{3^{5/2}}27^{-s}(2\pi)^{4s-2}
\frac{\Gamma(4/3-s)\Gamma(5/3-s)}
     {\Gamma(s+1/3)\Gamma(s+2/3)}.
\tag{6.5}
\]

The new domain has \(\Re s=1-b<1/2\), so its numerator gamma
factors have no poles; the reciprocal denominator factors are
entire. Therefore (6.4) is also holomorphic on (6.3).
Its fixed-strip vertical growth is polynomial by Stirling.
This conclusion uses the actual coefficient identity (6.1),
not an assumed second Weyl functional equation.

## 7. Quantitative meaning and the remaining moment obstruction

The balanced Mellin scalar, after the inherited row conductor
cancels, has size

\[
D^{\Re(v-2s)}=D^{a+b-1}.
\tag{7.1}
\]

Theorem 4.1 gives limiting scalar exponents \(7/10\), \(2/3\),
and \(23/35\), respectively, in its three rows. The stronger
rectangles in Theorem 5.1 give

\[
\boxed{\frac58\quad\text{with the classical counting inputs},\qquad
\frac{73}{120}\quad\text{with the optimal sieve and angular input}.}
\tag{7.2}
\]

These are infima, approached strictly from inside the proved
regions. At the latter corner, \(s\to0^-\), \(u,v\to73/120\).
The original signed covariance and every physical Mellin kernel
must still be present before such a scalar can be used in an
estimate for a moment.

There is a sharp practical limitation of this gain. Even if the
remaining physical contour composition yields the candidate
squarefree-row energy

\[
QD^{73/60+\epsilon},
\tag{7.3}
\]

it does not improve the available positive envelope for the same
physical one-axis completion. The forward completed theorem at
\(A=B=D,\ q=f=1,\ \beta=11/12\) gives

\[
QD+Q^2D^{5/12}+Q^{4/3}D^{2/3},
\tag{7.4}
\]

and the classical product polynomial gives
\[
Q+D^2+(QD^2)^{2/3}.
\tag{7.5}
\]

For \(Q\le D^{19/24}\), every term of (7.4) is at most
\(QD^{29/24}\). For \(Q\ge D^{19/24}\), every term of (7.5)
is at most that same quantity. Thus the existing minimum is
uniformly

\[
\ll QD^{29/24+\epsilon}.
\tag{7.6}
\]

Since \(73/60-29/24=1/120>0\), the new scalar route remains
weaker as a universal positive physical estimate. With counting
alone, the analogous split at \(Q=D^{3/4}\) already gives
\(QD^{5/4+\epsilon}\), matching the counting scalar in (7.2).
The comparison concerns exactly the physical completion; it is
not a comparison with the original Möbius moment.

The new mathematical information is the larger holomorphic tube
of the exact reunited object, the square-root means in genuinely
larger joint regions, and the explicit axis-exchange identity
resolving its one-sided cube masks. The unsolved target remains
the signed two-column covariance at the original long dual
heights, with its actual moving auxiliaries and strict product
diagonal. No fourth moment, \(17/24\) zero-free boundary,
generalized \(2k\)-th moment, or RH conclusion follows here.

## 8. Review and finite-verification boundary

The new load-bearing arithmetic assertion is the exact split
(2.7)–(2.11). The new analytic deductions are the simultaneous
block bounds (2.1), normal convergence (3.2), and the pointwise
envelope inequalities (5.3), (5.6). Their failure would invalidate
the corresponding continuation or row-mean claims.

Exact rational checks can reproduce the conductor powers, norm
weights, two crossovers, weighted-geometric-mean conditions,
and every monomial comparison in Section 5. Such checks do not
reprove the theta foundation or either sieve, do not supply
uniformity beyond the stated masks, and do not turn a finite
calculation into a proof of the generalized moment.
