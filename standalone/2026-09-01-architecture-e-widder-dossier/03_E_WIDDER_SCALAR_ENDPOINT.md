# The E–Widder scalar endpoint

Status: **PROPOSED EXACT RH-EQUIVALENCE; INDEPENDENT REVIEW REQUIRED.  THE SOURCE INEQUALITY IS PROVED THROUGH ORDER `4.71*10^12`; ITS ALL-ORDER FORM AND RH REMAIN OPEN.**

This note compresses the all-order source/Hermite/Stieltjes positivity problem to one scalar derivative hierarchy evaluated entirely on the Euler-safe half-plane `Re(s)>1`.

The external real-analysis input is Widder's characterization of Stieltjes functions.  A convenient modern source is A. D. Sokal, *Real-variables characterization of generalized Stieltjes functions*, arXiv:0902.0065, Theorem 1.  In the notation below, Widder's reduced condition is exactly

\[
 f(u)\ge0,
 \qquad
 (-1)^{k-1}D_u^{2k-1}[u^kf(u)]\ge0
 \quad(k\ge1).
\]

The finite-order theorem proved after the initial version of this note is recorded in [`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md).

## 1. Functional-equation invariant coordinate

The functional equation

\[
 \xi_{\rm R}(s)=\xi_{\rm R}(1-s)
\]

shows that

\[
 Y(x)=\xi_{\rm R}(1/2+x)
\]

is an even entire function.  Its power series has only even terms,

\[
 Y(x)=\sum_{m\ge0}a_mx^{2m}.
\]

Therefore there is a unique entire function `mathfrak X` such that

\[
 \boxed{
 \mathfrak X(s(s-1))=\xi_{\rm R}(s).
 }
 \tag{1.1}
\]

Indeed, with `u=s(s-1)=x^2-1/4`, define

\[
 \mathfrak X(u)=\sum_{m\ge0}a_m(u+1/4)^m.
\]

Since `Y` has order one in `x`, `mathfrak X` has order at most one half in `u`.  In particular its canonical product has genus zero.

For `u>0`, put

\[
 x=x(u)=\sqrt{u+1/4},
 \qquad
 s=s(u)=1/2+x>1.
\]

Define

\[
 \boxed{
 q(u)=2\frac{\mathfrak X'(u)}{\mathfrak X(u)}
 =\frac1{x}
 \frac{\xi_{\rm R}'}{\xi_{\rm R}}(s).
 }
 \tag{1.2}
\]

The second identity follows from `du/dx=2x`.

## 2. Unconditional positivity of `q`

The actual full-line theta representation gives

\[
 Y(x)=2\int_0^\infty\Phi(v)\cosh(xv)\,dv>0
\]

for `x>0`, and

\[
 Y'(x)=2\int_0^\infty v\Phi(v)\sinh(xv)\,dv>0.
\]

Consequently

\[
 \boxed{q(u)>0\qquad(u>0).}
 \tag{2.1}
\]

This pays the separate `F_(0,0)>=0` condition in Widder's theorem.

Stirling's formula and the absolute convergence of `zeta'/zeta` at `s>1` give

\[
 q(u)=O\left(\frac{\log u}{\sqrt u}\right),
 \qquad
 q(u)\longrightarrow0
 \quad(u\to\infty).
 \tag{2.2}
\]

Thus any Stieltjes representation of `q` has zero constant term.

## 3. Widder hierarchy

For every integer `k>=1`, define

\[
 \boxed{
 \mathcal W_k(u)=
 (-1)^{k-1}
 D_u^{2k-1}\bigl[u^kq(u)\bigr].
 }
 \tag{3.1}
\]

The endpoint theorem is

\[
 \boxed{
 \mathrm{RH}
 \iff
 \mathcal W_k(u)\ge0
 \quad\text{for every }u>0\text{ and every }k\ge1.
 }
 \tag{3.2}
\]

Sections 4–6 prove the equivalence.

## 4. RH implies the hierarchy

Assume RH.  Write the nontrivial zeros as

\[
 \rho=1/2\pm i\gamma,
 \qquad \gamma>0,
\]

with multiplicity `m_gamma`.  Their invariant coordinate is

\[
 \rho(\rho-1)=-(\gamma^2+1/4).
\]

Put

\[
 a_\gamma=\gamma^2+1/4>0.
\]

Because `mathfrak X` has genus zero and

\[
 \sum_{\gamma>0}\frac{m_\gamma}{a_\gamma}<\infty,
\]

its logarithmic derivative is

\[
 \frac{\mathfrak X'(u)}{\mathfrak X(u)}
 =\sum_{\gamma>0}
 \frac{m_\gamma}{u+a_\gamma}.
\]

Therefore

\[
 \boxed{
 q(u)=2\sum_{\gamma>0}
 \frac{m_\gamma}{u+a_\gamma}.
 }
 \tag{4.1}
\]

This is a positive Stieltjes transform.

For one atom, polynomial division gives

\[
 \frac{u^k}{u+a}
 =Q_{k-1}(u)+\frac{(-a)^k}{u+a},
\]

where `Q_(k-1)` has degree at most `k-1`.  Hence

\[
 \boxed{
 (-1)^{k-1}D_u^{2k-1}
 \left[\frac{u^k}{u+a}\right]
 =(2k-1)!\frac{a^k}{(u+a)^{2k}}.
 }
 \tag{4.2}
\]

Termwise differentiation in (4.1) is justified locally uniformly, and thus

\[
 \boxed{
 \mathcal W_k(u)
 =2(2k-1)!
 \sum_{\gamma>0}m_\gamma
 \frac{a_\gamma^k}{(u+a_\gamma)^{2k}}>0.
 }
 \tag{4.3}
\]

This proves the forward implication.

## 5. The hierarchy makes `q` Stieltjes

Assume

\[
 \mathcal W_k(u)\ge0
 \qquad(u>0,\ k\ge1).
\]

Together with (2.1), Widder's theorem implies that `q` is a Stieltjes function:

\[
 q(u)=C+\int_{[0,\infty)}\frac{d\mu(r)}{u+r},
 \qquad C\ge0,
 \quad \mu\ge0.
 \tag{5.1}
\]

By (2.2), `C=0`.  Thus `q` extends holomorphically to

\[
 \Omega=\mathbb C\setminus(-\infty,0].
\]

## 6. Stieltjes continuation forces RH

On the positive real axis,

\[
 q(u)=2\frac{\mathfrak X'(u)}{\mathfrak X(u)}.
\]

The left side has the holomorphic continuation (5.1) to `Omega`; the right side is meromorphic there.  By the meromorphic identity theorem the two continuations agree wherever both are defined.  A zero of `mathfrak X` at any point of `Omega` would create a nonremovable pole of its logarithmic derivative, contradicting the holomorphy of `q`.  Hence

\[
 Z(\mathfrak X)\subset(-\infty,0].
 \tag{6.1}
\]

Let `rho=beta+i gamma` be a nontrivial zero of `xi_R`.  Its invariant coordinate is

\[
 \rho(\rho-1)
 =\beta(\beta-1)-\gamma^2
 +i\gamma(2\beta-1).
 \tag{6.2}
\]

By (6.1), this number is real.  Therefore

\[
 \gamma(2\beta-1)=0.
\]

There are no real nontrivial zeros in `0<s<1`: for real `0<s<1`, the alternating eta series is positive and `1-2^{1-s}<0`, so `zeta(s)<0`.  Thus `gamma\ne0`, and

\[
 \beta=1/2.
\]

Every nontrivial zero lies on the critical line.  This proves RH and completes the proof of (3.2), subject to review of the imported theorem and analytic details.

## 7. Euler-safe arithmetic expansion

For `s>1`,

\[
 \frac{\xi_{\rm R}'}{\xi_{\rm R}}(s)
 =\frac1s+\frac1{s-1}
 -\frac12\log\pi
 +\frac12\psi(s/2)
 -\sum_{n\ge2}\frac{\Lambda(n)}{n^s}.
 \tag{7.1}
\]

Since `2s-1=2x` and `s(s-1)=u`,

\[
 \frac1x\left(\frac1s+\frac1{s-1}\right)=\frac2u.
\]

Also

\[
 n^{-s}=n^{-1/2}e^{-x\log n}.
\]

Therefore

\[
 \boxed{
 q(u)=
 \frac2u
 +\frac{\psi(s/2)-\log\pi}{2x}
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \frac{e^{-x\log n}}x.
 }
 \tag{7.2}
\]

## 8. The pole term disappears at every Widder order

Multiplication by `u^k` changes `2/u` into `2u^(k-1)`.  Since

\[
 2k-1>k-1,
\]

we have

\[
 D_u^{2k-1}[2u^{k-1}]=0.
\]

Define the archimedean reserve

\[
 \boxed{
 \mathcal G_k(u)=
 (-1)^{k-1}D_u^{2k-1}
 \left[
  \frac{u^k}{2x}
  \bigl(\psi(s/2)-\log\pi\bigr)
 \right]
 }
 \tag{8.1}
\]

and the prime-power filter

\[
 \boxed{
 \mathcal L_k(u,\ell)=
 (-1)^{k-1}D_u^{2k-1}
 \left[
  \frac{u^k}{x}e^{-\ell x}
 \right].
 }
 \tag{8.2}
\]

Then

\[
 \boxed{
 \mathcal W_k(u)=
 \mathcal G_k(u)
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
  \mathcal L_k(u,\log n).
 }
 \tag{8.3}
\]

Every derivative of the summand is `e^(-x log n)` times a finite polynomial in `log n` and rational functions of `x`.  Hence, for each fixed `u>0`, the series in (8.3) is absolutely convergent because

\[
 \sum_{n\ge2}\Lambda(n)(\log n)^M n^{-s}<\infty
 \qquad(s>1)
\]

for every fixed `M`.

## 9. The E–Widder source inequality

The all-order Architecture-E burden is

\[
 \boxed{
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 \le
 \mathcal G_k(u)
 \qquad
 (u>0,\ k\ge1).
 }
 \tag{EW}
\]

The statement contains:

- no zero sum;
- no analytic continuation of the Euler series;
- no quotient, gauge or inverse observation;
- no limiting finite panel;
- no unsigned prime envelope;
- no hidden choice of test function.

It is one scalar inequality for an absolutely convergent prime-power series.

## 10. Finite-height theorem: `(EW)` through `4.71*10^12` orders

The initial version of this note left every order above the inherited first rung open.  The angular theorem in [`08_FINITE_HEIGHT_WIDDER_CONE.md`](08_FINITE_HEIGHT_WIDDER_CONE.md) supersedes that frontier.

Without assuming RH, choose one invariant atom

\[
 a=-\rho(\rho-1)
\]

for each functional-equation orbit.  If `rho=beta+i gamma`, then

\[
 \Re a=\gamma^2+\beta(1-\beta)>\gamma^2,
 \qquad
 |\Im a|<|\gamma|,
\]

so

\[
 |\arg a|<\arctan(1/|\gamma|).
\]

For the full Widder quantities

\[
 F_{n,k}(u)=(-1)^nD_u^{n+k}[u^kq(u)],
\]

the exact zero-atom formula is

\[
 F_{n,k}(u)
 =2(n+k)!\sum_a\frac{a^k}{(u+a)^{n+k+1}}.
\]

For an off-line conjugate pair, the phase of one summand has absolute value at most

\[
 \max\{k,n+1\}|\arg a|.
\]

Therefore finite-height RH verification through `H` proves the entire cone

\[
 F_{n,k}(u)>0
\]

whenever

\[
 \max\{k,n+1\}\arctan(1/H)<\pi/2.
\]

Using the published Platt–Trudgian height

\[
 H=3\cdot10^{12}
\]

and the rational budget

\[
 M/H=157/100<\pi/2,
\]

we obtain

\[
 \boxed{
 \mathcal W_k(u)>0
 \quad
 (u>0,\ 1\le k\le4{,}710{,}000{,}000{,}000).
 }
 \tag{10.1}
\]

Combining (10.1) with (8.3) proves strict `(EW)` throughout that range.

No simplicity assumption is used, and the external zero computation was not rerun.

The same argument gives

\[
 \boxed{
 \mathcal W_k(u)<0
 \Longrightarrow
 \text{an off-line zero below height }
 \cot\left(\frac\pi{2k}\right).
 }
 \tag{10.2}
\]

The converse is not claimed.

## 11. Remaining all-order frontier

The first diagonal order not paid by the imported finite-height theorem is

\[
 4{,}710{,}000{,}000{,}001.
\]

This number is merely the current height-to-angle cutoff.  The unresolved task is not to manipulate a derivative of that literal order.  It is to prove a height-free mechanism controlling the phase rotation of hypothetical off-line invariant atoms.

A full proof must establish `(EW)` for unbounded `k`, which by Sections 3–6 is equivalent to RH.

## 12. False-RH finite witnesses

Because `q(u)>0` unconditionally, failure of RH means that `q` is not Stieltjes.  By Widder's theorem there exist an integer `k>=1` and a real `u>0` such that

\[
 \mathcal W_k(u)<0.
\]

By continuity, a rational `u` can be chosen with the same strict sign.  At that rational point the prime series in (8.3) is absolutely convergent, so a sufficiently large outward-rounded finite prime cutoff certifies the strict violation.

The finite-height theorem now adds that any such witness must satisfy

\[
 k>4{,}710{,}000{,}000{,}000.
\]

Thus false RH has a countable family of finite, Euler-safe certificate types, but no witness can occur in the first `4.71*10^12` complete orders.

No Riemann-data witness is claimed here.

## 13. Relation to the earlier Stieltjes coordinate

The source–Hermite closure uses

\[
 p(t)=\frac{F(\sqrt t)}{\sqrt t},
 \qquad t>1/4.
\]

The invariant function is simply the translated coordinate

\[
 q(u)=p(u+1/4).
\]

The translation moves the RH spectral support from `gamma^2` to

\[
 a_\gamma=\gamma^2+1/4,
\]

which is exactly `-rho(rho-1)`.  This makes the converse transparent: Stieltjes support on the negative real `u` axis is literally critical-line support under the functional-equation quotient.

## 14. Main review points

Independent review should check, in this order:

1. the entire descent `xi_R(s)=mathfrak X(s(s-1))` and order-one-half claim;
2. the factor two in `q=2 mathfrak X'/mathfrak X`;
3. the genus-zero product and orbit multiplicities;
4. the exact Widder indexing `F_(k-1,k)=(-1)^(k-1)D^(2k-1)u^kq`;
5. the meromorphic identity-theorem argument in Section 6;
6. exclusion of real nontrivial zeros;
7. the pole-term cancellation in Section 8;
8. absolute convergence after arbitrary fixed-order differentiation;
9. the angular proof and use of the imported height theorem in Section 10.

## 15. Exact status

```text
functional-equation invariant descent              PROPOSED COMPLETE / REVIEW
RH -> positive Stieltjes representation             PROPOSED COMPLETE / REVIEW
Widder hierarchy <-> Stieltjes                      CLASSICAL IMPORT
Stieltjes continuation -> RH                        PROPOSED COMPLETE / REVIEW
Euler-safe prime-power formula                      PROPOSED COMPLETE / REVIEW
finite-height full cone through 4.71*10^12          PROPOSED COMPLETE / REVIEW
E-Widder source inequality through 4.71*10^12       PROPOSED COMPLETE / REVIEW
all-order E-Widder source inequality                OPEN / RH-EQUIVALENT
Riemann Hypothesis                                  UNPROVED
```
