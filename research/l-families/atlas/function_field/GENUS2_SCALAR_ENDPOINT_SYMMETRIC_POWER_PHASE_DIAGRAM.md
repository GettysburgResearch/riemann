# The scalar-endpoint symmetric-power phase diagram

Status: **exact for every symmetric-power rank and every positive integer
moment on the tower \(q=3^{4k}\), \(k\geq1\)**. The geometric input is
source-locked to the exact scalar endpoint packet at commit
77c6a1b31d6d2b475df0d87e187f32d9a09479e5. The replay uses only small
exact integer and rational checks. It enumerates no finite field, curve,
group element, representation, L-function, or zero set.

## 1. Locked geometric input

Let

\[
 \mathcal H_5(q)=
 \{D\in\mathbf F_q[T]:D\text{ monic squarefree},\ \deg D=5\}.
\]

The locked scalar packet proves that, for \(q=3^{4k}\), the affine orbit of
\(D_0=T^5+1\) is the disjoint union of two square-affine orbits
\(\mathcal O_+\) and \(\mathcal O_-\). Put

\[
 s=(-1)^k.
\]

Their normalized Frobenius classes and sizes are

\[
 U_D=sI_4\quad(D\in\mathcal O_+),\qquad
 U_D=-sI_4\quad(D\in\mathcal O_-),                         \tag{1}
\]

\[
 |\mathcal O_+|=|\mathcal O_-|={q(q-1)\over10},\qquad
 |\mathcal H_5(q)|=q^4(q-1).                               \tag{2}
\]

Thus each constructed orbit has member-uniform density \(1/(10q^3)\).
This is an exact density for the constructed orbit, and only a lower bound
for the density of all members having that scalar endpoint.

The source lock is transitive: the scalar packet itself pins the marked-stack
action and the Sym10 rare-event normalization. No second rare-event input is
needed here.

## 2. Every symmetric power

Let \(\chi_r\) be the character of
\(\operatorname{Sym}^r(\mathbf C^4)\), restricted to \(\operatorname{USp}(4)\),
and put

\[
 d_r=\dim\operatorname{Sym}^r(\mathbf C^4)
     ={r+3\choose3}
     ={(r+1)(r+2)(r+3)\over6}.                              \tag{3}
\]

Indeed, the standard monomial basis is indexed by the weak compositions of
\(r\) into four parts, of which there are \({r+3\choose3}\).

If \(P_D(u)^{-1}=\sum_{r\geq0}r_D(r)u^r\), the standard symmetric-power
identity gives

\[
 r_D(r)=q^{r/2}\chi_r(U_D).                                 \tag{4}
\]

For a scalar \(tI_4\), the representation
\(\operatorname{Sym}^r(tI_4)\) is \(t^rI_{d_r}\). Hence (1) gives

\[
 \boxed{
 \chi_r(sI_4)=s^r d_r,
 \qquad
 \chi_r(-sI_4)=(-s)^r d_r.}                                \tag{5}
\]

This includes the old specialization \(d_{10}={13\choose3}=286\).

## 3. Exact absolute and signed subtotals

For an integer \(m\geq1\), define the full normalized absolute and signed
moments

\[
 A_{r,m}(q)={1\over|\mathcal H_5(q)|}
 \sum_D|\chi_r(U_D)|^m,
 \qquad
 S_{r,m}(q)={1\over|\mathcal H_5(q)|}
 \sum_D\chi_r(U_D)^m.                                      \tag{6}
\]

Equations (2)--(5) show that the two-orbit union contributes exactly

\[
 \boxed{
 A^{\rm end}_{r,m}(q)={d_r^m\over5q^3}}                    \tag{7}
\]

to the absolute moment. Its signed subtotal is

\[
 S^{\rm end}_{r,m}(q)
 ={d_r^m\over10q^3}
 \left(s^{rm}+(-s)^{rm}\right)
 =\boxed{
 \begin{cases}
 0,&rm\text{ odd},\\[2mm]
 d_r^m/(5q^3),&rm\text{ even}.
 \end{cases}}                                               \tag{8}
\]

The positive row in (8) is independent of \(k\): if \(rm\) is even then
\(s^{rm}=1\). When \(rm\) is odd, cancellation occurs between the two
constructed twist orbits. It says nothing about cancellation or bias in the
remaining family.

## 4. The full absolute-moment spectral-radius limit

Every eigenvalue of a unitary representation has absolute value one, so

\[
 |\chi_r(U)|\leq d_r\qquad
 (U\in\operatorname{USp}(4)).                              \tag{9}
\]

The constructed positive-density endpoints give the lower bound in (7),
while (9) gives the upper bound. Therefore

\[
 {d_r^m\over5q^3}\leq A_{r,m}(q)\leq d_r^m                 \tag{10}
\]

and

\[
 \boxed{
 d_r(5q^3)^{-1/m}
 \leq A_{r,m}(q)^{1/m}
 \leq d_r.}                                                 \tag{11}
\]

At fixed \(q=3^{4k}\) and fixed \(r\), the two bounds converge to the same
number. Thus

\[
 \boxed{
 \lim_{m\to\infty}A_{r,m}(q)^{1/m}=d_r.}                   \tag{12}
\]

Unlike the phase statements below, (12) is a theorem about the **full**
absolute family moment. It is the usual \(L^m\)-to-\(L^\infty\) mechanism,
made exact here by an explicitly realized positive-mass endpoint.

## 5. Exact critical surface

Write the constructed absolute subtotal as

\[
 C(r,m,q)={d_r^m\over5q^3}.                                 \tag{13}
\]

It is equal to one precisely on

\[
 \boxed{
 m\log d_r=3\log q+\log5.}                                 \tag{14}
\]

The choice of logarithm base is irrelevant. For \(r=0\), \(d_0=1\), so
\(C(0,m,q)=1/(5q^3)\) and there is no moment-order crossover. The following
statements assume \(r\geq1\).

### 5.1 Fixed rank: logarithmic moment order

The continuous crossover is

\[
 m_*(q,r)={3\log q+\log5\over\log d_r}.                     \tag{15}
\]

On the tower \(q=3^{4k}\), this is

\[
 m_*(3^{4k},r)={12k\log3+\log5\over\log d_r},               \tag{16}
\]

so the critical moment grows linearly in \(k\), equivalently logarithmically
in \(q\).

There is an exact discrete version requiring no logarithms. Put

\[
 M(q,r)=\max\{m\geq0:d_r^m\leq5q^3\}.
\]

Then \(M\) is the last subcritical integer and \(M+1\) is the first
supercritical integer, with

\[
 \boxed{
 {1\over d_r}<C(r,M,q)\leq1
 <C(r,M+1,q)\leq d_r.}                                     \tag{17}
\]

The producer computes the declared controls by repeated exact integer
multiplication, not floating logarithms.

### 5.2 Fixed moment: cubic rank scale

For fixed \(m\), put

\[
 R(q,m)=
 \max\left\{r\geq0:{r+3\choose3}^{m}\leq5q^3\right\}.       \tag{18}
\]

Then \(R\) is the last subcritical rank and \(R+1\) is the first
supercritical rank. Since

\[
 {(r+1)^3\over6}\leq d_r\leq{(r+3)^3\over6},               \tag{19}
\]

putting

\[
 X=6^{1/3}5^{1/(3m)}q^{1/m}
\]

gives the exact width-two integer window

\[
 \boxed{
 \lfloor X\rfloor-3\leq R(q,m)\leq\lfloor X\rfloor-1.}      \tag{20}
\]

In particular,

\[
 \boxed{
 R(q,m)=6^{1/3}5^{1/(3m)}q^{1/m}+O(1),}                    \tag{21}
\]

which is the requested \(r\asymp q^{1/m}\) crossover. The replay computes
\(\lfloor X\rfloor\) as the exact integer \(3m\)-th root of \(6^m5q^3\).

## 6. Interpretation firewall

Proved:

- the all-\(r\) dimension, reciprocal normalization, and scalar-character
  formulas;
- the exact absolute and parity-sensitive signed subtotals of the two
  constructed twist orbits;
- the full absolute-moment squeeze and fixed-\((q,r)\) \(m\)-th-root limit;
- the exact critical surface, fixed-rank discrete moment crossover, and
  fixed-moment discrete rank crossover;
- the width-two control (20) and hence the asymptotic scale (21).

Not proved:

- that the two constructed orbits exhaust the scalar endpoints;
- an asymptotic formula for the full moment at fixed or growing \(r,m,q\);
- that the subtotal crossing in (14) is a phase transition for the rest of
  the family;
- a sign law for the full signed moment;
- equidistribution, monodromy, a motive classification, a zero theorem, RH,
  GRH, or average-to-individual amplification.

## 7. Reproduction

    python -B research/l-families/atlas/function_field/genus2_scalar_endpoint_symmetric_power_phase_diagram.py --write
    python -B research/l-families/atlas/function_field/genus2_scalar_endpoint_symmetric_power_phase_diagram.py --check
    python -O -B research/l-families/atlas/function_field/genus2_scalar_endpoint_symmetric_power_phase_diagram.py --check
    python -m pytest -q tests/test_genus2_scalar_endpoint_symmetric_power_phase_diagram.py
    python -O -m pytest -q tests/test_genus2_scalar_endpoint_symmetric_power_phase_diagram.py
    python -m ruff check research/l-families/atlas/function_field/genus2_scalar_endpoint_symmetric_power_phase_diagram.py tests/test_genus2_scalar_endpoint_symmetric_power_phase_diagram.py

The canonical payload is
genus2_scalar_endpoint_symmetric_power_phase_diagram.json.
