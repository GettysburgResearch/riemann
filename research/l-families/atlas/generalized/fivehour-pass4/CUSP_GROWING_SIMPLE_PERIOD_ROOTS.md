# Growing simple roots of the full native cusp-period determinant

Status: PROPOSED ANALYTIC THEOREM; independent review required.
Scope: the full level-one completed period determinant, in a growing but
sub-cube-root endpoint range. This does not assert scalar flag-quotient
noncancellation or an RH mechanism.

## 1. Statement

Let `P_k(s)` be the Petersson form operator of the completed Eisenstein
period on `V_k=S_k(SL_2(Z))`, with the normalization of the accepted parent
and of the preceding K, P, G, and L packets. Let `T_k` be its finite-part
operator at `s=1`, with decreasing eigenvalues `lambda_j(k)`.

Let `J_k` be any positive integer sequence satisfying

\[
 J_k^3\log k=o(k).                                      \tag{R1}
\]

**Theorem R.** For all sufficiently large even `k`, and for every
`1<=j<=J_k`, there is a conjugation-invariant domain `Omega_(k,j)` in the
complex epsilon plane such that:

1. the domains are pairwise disjoint and lie in `0<|epsilon|<1/4`;
2. `det P_k(1-epsilon)` has exactly one zero in `Omega_(k,j)`, counting
   multiplicity;
3. that zero `epsilon_(k,j)` is real, positive and simple; and
4. uniformly over the declared range,

\[
 \left|-{1\over2\epsilon_{k,j}}+\lambda_j(k)\right|
       =O(j\log k),                                    \tag{R2}
\]

and consequently

\[
 \boxed{\epsilon_{k,j}={12j\over k}(1+o(1)).}          \tag{R3}
\]

Thus the fixed-depth full-determinant ladder extends simultaneously through
every range (R1). The theorem concerns the full native determinant. It does
not prove that these zeros remain uncancelled in any particular quotient of
nested scalar determinants.

## 2. A growing-coordinate operator remainder

The fixed-compact estimate in Theorem G can be made uniform in a slowly
growing endpoint coordinate. The exact form needed here is the following.

**Lemma R1.** There are absolute constants `C` and `eta_0>0` such that, for
all large even `k` and all complex `epsilon` with

\[
 0<|\epsilon|\le\eta_0,qquad |\epsilon|\log k\le\eta_0,
\]

one has, in the original Petersson norm,

\[
 \left\|P_k(1-\epsilon)+{1\over2\epsilon}I-T_k\right\|_{op}
 \le C|\epsilon|k\log k.                               \tag{R4}
\]

Proof. The Laurent expansion is formed before estimating its terms. The
constant term of the completed Eisenstein series gives, on `y>=1`,

\[
 \left|E^*(z,1-\epsilon)+{1\over2\epsilon}-E_0(z)\right|
 \le C_0|\epsilon|\{1+y^{1+|\epsilon|}(1+\log y)
                  +y^{|\epsilon|}(1+\log^2y)\}.        \tag{R5}
\]

On the compact part it is `O(|epsilon|)`. The bound is uniform in a fixed
disk about zero. It follows by Taylor expanding both completed-zeta
coefficients and the exponentials only after the polar exponential has had
its constant and linear terms removed. The nonconstant Fourier series is
uniformly analytic in the same disk: its Bessel functions are bounded by a
fixed `K_1`, followed by an exponentially convergent divisor sum. These are
the full-domain estimates used in G; no inequality is continued from only
one side of the pole.

For `0<=theta<=eta_0`, the coefficientwise incomplete-Gamma recurrence on
the full cusp gives

\[
 \mathbb E_f[y^{r+\theta}]
 \le C_r k^{r+\theta},\qquad r=0,1,2,                 \tag{R6}
\]

uniformly over every Petersson-unit cusp form. One may first prove (R6) for
integer moments by integration by parts and then use log-convexity between
adjacent moments. The compact contribution is bounded. Also

\[
 \mathbb E_f[y^{1+\theta}\log y]
 \le C k^{1+\theta}\log k,                            \tag{R7}
\]

by splitting at `y=k` (or differentiating the Gamma ratio), while
`log^2 y<=y` for `y>=1`. Under the hypothesis of the lemma,
`k^|epsilon|` is bounded. Taking expectations in (R5), and using weighted
Cauchy--Schwarz for a mixed pair of cusp forms, proves (R4). The argument is
valid for complex `epsilon` because only absolute values entered. This also
proves holomorphy of the matrix remainder. QED.

The restriction `|epsilon| log k<=eta_0` is essential to this proof. The
lemma is not an operator estimate at a fixed positive distance from the
endpoint.

## 3. Separation of the native finite-part eigenvalues

The logarithmic spectral theorem gives, uniformly for `j=o(k)`,

\[
 m_{k,j}+o(1)\le\lambda_j(k)\le m_{k,j}+R_1+o(1),
\]

where

\[
 m_{k,j}={k-1\over24j}-{1\over2}\log {k-1\over4\pi j}+c_0.
\]

Therefore

\[
 m_{k,j}-m_{k,j+1}
 ={k-1\over24j(j+1)}-{1\over2}\log{j+1\over j}.       \tag{R8}
\]

For every `J=o(sqrt(k))`, (R8) and the fixed-width brackets imply, uniformly
for `1<=j<=J`,

\[
 \lambda_j(k)-\lambda_{j+1}(k)
 \ge c{k\over(j+1)^2}                                 \tag{R9}

with one absolute `c>0` and all sufficiently large `k`. In particular the
first `J` eigenvalues are positive and simple. The sequential formulation
of the L theorem is uniform here: failure of the displayed uniform claim
would supply a contradicting sequence of legal indices.

Condition (R1) is stronger than the separation range and also gives

\[
 j\log k=o(k/j^2)                                     \tag{R10}

uniformly for `j<=J_k`.

## 4. Disjoint matrix-Rouche domains

Write

\[
 a(\epsilon)=-{1\over2\epsilon},\qquad
 A_k(\epsilon)=a(\epsilon)I+T_k,
\]

and let the analytic remainder in (R4) be `R_k(epsilon)`. Choose a fixed
constant `D>0`, larger than four times the constant in (R4) after the
harmless comparison `|epsilon|<=C_1j/k` below, and put

\[
 q_{k,j}=Dj\log k,
 \qquad
 \Omega_{k,j}=\{\epsilon:
       |a(\epsilon)+\lambda_j(k)|<q_{k,j}\}.           \tag{R11}

The component in (R11) is the Mobius image of a disk and contains
`1/(2lambda_j)`. Equations (R9)--(R10) imply

\[
 q_{k,j}+q_{k,j+1}<\lambda_j-lambda_{j+1}.            \tag{R12}

Thus the domains are disjoint. On their closures,
`|epsilon|` is comparable to `j/k`; in particular they lie in the domain of
Lemma R1 and avoid zero for all large `k`.

On `partial Omega_(k,j)`, the singular values of the normal matrix `A_k`
are the moduli

\[
 |a(\epsilon)+\lambda_l(k)|.
\]

The `l=j` value is `q_(k,j)`, and (R9),(R12) put every other value above a
fixed positive multiple of `q_(k,j)`. Increasing `D` once if necessary,
Lemma R1 gives

\[
 \|A_k(\epsilon)^{-1}R_k(\epsilon)\|<1
 \quad(\epsilon\in\partial\Omega_{k,j}).              \tag{R13}

For completeness, no black-box scalar Rouche theorem is being applied to
individual matrix entries. Along the homotopy
`A_k+uR_k`, `0<=u<=1`, (R13) prevents a boundary singularity. The argument
principle for the finite determinant therefore preserves the number of
zeros inside, counting multiplicity. The diagonal comparison determinant
has exactly one: only the factor `a(epsilon)+lambda_j` vanishes there, and
its zero is simple. Hence the exact period determinant also has exactly one
zero in each domain.

The exact family is Hermitian for real `epsilon` and obeys conjugation
symmetry. Every domain (R11) is invariant under conjugation. Its single zero,
counting multiplicity, must therefore be real and simple. It is positive
because the entire domain lies near the positive center
`1/(2lambda_j)`.

Finally the zero condition and (R11) give (R2). Since
`lambda_j~k/(24j)` and `j^2 log k/k=o(1)` under (R1), inversion gives (R3).

## 5. Exact boundaries

The cube-root range is produced by comparing an `O(j log k)` analytic
remainder with the adjacent finite-part gap `asymp k/j^2`. It is a proved
range for this method, not a claim that the true ladder stops there.

The theorem counts full determinant zeros with multiplicity and proves the
ones in its domains simple. It does not establish interlacing of nested
coefficient-flag quotients, the exponentially smaller separation between
their numerator and denominator roots, or noncancellation after a scalar
Schur complement. It also does not continue the reciprocal-Gamma limit to
moving compact sets; its proof uses the direct exact-period operator
remainder instead.

The imported tools are the completed Eisenstein Fourier expansion,
incomplete-Gamma moments, min--max, finite-dimensional determinant argument
principle, and the previously stated K/L spectral theorems. No finite
certificate is used to infer (R1)--(R3).
