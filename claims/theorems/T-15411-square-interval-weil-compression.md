# T-15411 — Square interval indicators already carry the complete RH obstruction

Claim ID: `T-15411`  
Title: The square-screw scalar is exactly the normalized Weil energy of one centered interval indicator and the constant D-0001 coordinate  
Status: `PROPOSED — EXACT COMPOSITION THEOREM; SQUARE-SAMPLING/LANDAU AND D-0001 NORMALIZATIONS INHERITED`  
Authoring agent: `gpt56-05-l`  
Created: 2026-08-07  
Dependencies: Nakamura–Suzuki’s centered screw/zero-sum identities; `L-19801`, `L-19802`, `L-20704`; the accepted centered Weil-form normalization  
Scope: global rank-one compression of the scalar, finite-matrix, and localized Weil programmes  
Related counterexample candidates: none

## 1. Centered Weil form and interval vectors

Write

\[
\Xi(z)=\xi\!\left(\frac12+iz\right)
\]

and let \(\Gamma_\Xi\) be its multiset of zeros, with multiplicities
\(m_\gamma\). Use the Fourier convention

\[
\widehat f(z)=\int_{\mathbb R}f(x)e^{-izx}\,dx
\]

and the centered polarized Weil form

\[
Q_W(f,g)
=
\sum_{\gamma\in\Gamma_\Xi}
 m_\gamma\widehat f(\gamma)
 \overline{\widehat g(\overline\gamma)}.
\tag{T-15411.1}
\]

Let

\[
\Psi(t)=-g_\zeta(t)
\]

be the nonnegative-under-RH screw sign convention of `L-19801`. The exact zero
expansion is

\[
\boxed{
\Psi(t)
=
\sum_{\gamma\in\Gamma_\Xi}
 m_\gamma\frac{1-e^{-i\gamma t}}{\gamma^2}.}
\tag{T-15411.2}
\]

For \(t\ge0\), define

\[
v_t=\mathbf1_{[0,t]},
\qquad
w_t=\mathbf1_{[-t/2,t/2]}.
\tag{T-15411.3}
\]

Their transforms satisfy

\[
\widehat v_t(z)=\frac{1-e^{-izt}}{iz}.
\tag{T-15411.4}
\]

Because every centered zeta zero has bounded imaginary part and

\[
\sum_\gamma \frac{m_\gamma}{|\gamma|^2}<\infty,
\]

the series defining \(Q_W(v_s,v_t)\) is absolutely convergent for fixed
\(s,t\). Thus interval indicators lie in the closed Weil form domain. They may
also be obtained by smooth compactly supported approximation without changing
the identities below.

## 2. Exact polarized interval identity

For every \(s,t\ge0\),

\[
\boxed{
Q_W(v_s,v_t)
=
\Psi(s)+\Psi(t)-\Psi(s-t),}
\tag{T-15411.5}
\]

where \(\Psi\) is even.

### Proof

Insert (T-15411.4) into (T-15411.1). One summand is

\[
\frac{1-e^{-i\gamma s}}{i\gamma}
\overline{
\frac{1-e^{-i\overline\gamma t}}{i\overline\gamma}}
=
\frac{1-e^{i\gamma t}+e^{-i\gamma(s-t)}-e^{-i\gamma s}}
{\gamma^2}.
\]

The zero multiset is invariant under \(\gamma\mapsto-\gamma\), so after summing
one may replace \(e^{i\gamma t}\) by \(e^{-i\gamma t}\). Equation
(T-15411.2) then gives (T-15411.5). Absolute convergence justifies the
reindexing. QED.

Taking \(s=t\) and using \(\Psi(0)=0\) gives

\[
\boxed{
Q_W(v_t,v_t)=2\Psi(t).}
\tag{T-15411.6}
\]

Translation invariance of the centered form gives the same identity for the
centered interval:

\[
\boxed{
Q_W(w_t,w_t)=2\Psi(t),
\qquad
\|w_t\|_2^2=t.}
\tag{T-15411.7}
\]

Hence

\[
\boxed{
\frac{Q_W(w_t,w_t)}{\|w_t\|_2^2}
=
\frac{2\Psi(t)}t.}
\tag{T-15411.8}
\]

## 3. Exact square-support identification

For an integer \(M\ge2\), put

\[
t_M=2\log M.
\]

Let \(A_{N,M^2}\) be any even D-0001 matrix containing its constant coordinate
\(e_0\), in the normalization of `L-20704`, and put

\[
a_M=e_0^{\mathsf T}A_{N,M^2}e_0.
\tag{T-15411.9}
\]

`L-20704` proves term by term that

\[
\Psi(2\log M)=\log M\,a_M.
\tag{T-15411.10}
\]

Combining (T-15411.7)--(T-15411.10) yields the three-way identity

\[
\boxed{
 a_M
 =
 \frac{\Psi(2\log M)}{\log M}
 =
 \frac{Q_W(w_{2\log M},w_{2\log M})}
      {\|w_{2\log M}\|_2^2}.}
\tag{T-15411.11}
\]

Thus the following objects are literally the same scalar:

1. the square-cutoff screw statistic divided by \(\log M\);
2. the normalized complete Weil energy of one centered interval indicator;
3. the constant principal coordinate of every square-support D-0001 packet.

No frame choice, Schur complement, selected-zero packet, or asymptotic
approximation enters (T-15411.11).

## 4. Complete rank-one RH criterion

The square-sampling theorem `L-19801` gives

\[
\boxed{
\mathrm{RH}
\iff
Q_W(w_{2\log M},w_{2\log M})\ge0
\text{ for every sufficiently large integer }M.}
\tag{T-15411.12}
\]

Equivalently,

\[
\boxed{
\mathrm{RH}
\iff
a_M\ge0
\text{ for every sufficiently large integer }M.}
\tag{T-15411.13}
\]

The weaker negative-part condition

\[
\boxed{
\bigl(-Q_W(w_{2\log M},w_{2\log M})\bigr)_+
=M^{o(1)} }
\tag{T-15411.14}
\]

already implies RH. In D-0001 coordinates this is

\[
\boxed{
\log M\,(-a_M)_+=M^{o(1)}.}
\tag{T-15411.15}
\]

This is a global criterion on one explicitly given rank-one family. It is not a
claim that positivity on arbitrary interval indicators would imply positivity
of an arbitrary translation-invariant form; the converse uses the zeta-specific
square-mesh derivative bound and Landau one-sign theorem from `L-19801`.

## 5. Exact false-RH alternative

Let

\[
\Theta_\zeta
=
\sup_{\xi(\rho)=0}
\left(\Re\rho-\frac12\right).
\]

`L-19802` and (T-15411.11) give

\[
\boxed{
\Theta_\zeta
=
\limsup_{M\to\infty}
\frac{
 \log\!\left(1+
 \bigl(-Q_W(w_{2\log M},w_{2\log M})\bigr)_+
 \right)}
{2\log M}.}
\tag{T-15411.16}
\]

Equivalently,

\[
\boxed{
\Theta_\zeta
=
\limsup_{M\to\infty}
\frac{
 \log\!\left(1+
 \log M\,(-a_M)_+
 \right)}
{2\log M}.}
\tag{T-15411.17}
\]

Therefore, if RH is false, then for every \(\theta<\Theta_\zeta\),

\[
\boxed{
\frac{
 \bigl(-Q_W(w_{2\log M},w_{2\log M})\bigr)_+
}{M^{2\theta}}
\text{ is unbounded on every integer tail},}
\tag{T-15411.18}
\]

or equivalently

\[
\boxed{
\frac{
 \log M\,(-a_M)_+
}{M^{2\theta}}
\text{ is unbounded on every integer tail}.}
\tag{T-15411.19}
\]

This is stronger than the statement that a complicated complete packet must
contain a hidden negative direction. Under false RH, polynomially deep
negativity is forced into the single constant interval ray itself.

## 6. Consequences for the repository-wide proof architecture

### Finite matrix route

Any lower bound for the full square-support D-0001 matrix immediately bounds
\(a_M\). Hence every cofinal matrix programme must already prove
(T-15411.15) in its constant coordinate. Better zero frames, Leja conditioning,
or Schur bookkeeping cannot bypass the scalar arithmetic obstruction.

### Complete-kernel route

The canonical augmentation, Xi-cardinal, Möbius-tail, and conditional-frame
stack remains useful for producing or excluding general negative directions.
But (T-15411.18) shows that a false-RH direction cannot remain visible only in
that sophisticated packet: it must ultimately project onto this explicit
rank-one interval family along a cofinal square schedule.

### Original-kernel / Loewner route

A proof of positivity of the original \(K_0\) or complete Loewner kernel proves
all Weil energies positive and therefore closes (T-15411.12). Conversely, any
putative positive factorization should be tested first on the interval ray,
where its scalar output must reproduce the exact prime-power formula
\(\Psi(2\log M)\).

## 7. Proof-producing interface

At one level \(M\), an arithmetic certificate needs only:

1. every prime power \(q\le M^2\), exactly once, with weight
   \(\Lambda(q)/\sqrt q\);
2. directed logarithms and square roots;
3. the complete pole and archimedean terms in the square-screw formula;
4. one interval enclosing \(\Psi(2\log M)\), equivalently \(a_M\);
5. the exact overlap check (T-15411.11) against an independent D-0001 producer.

A strictly negative upper endpoint would disprove RH. Positive finite levels do
not prove the eventual statement.

## 8. Proof boundary

- The interval polarization and Rayleigh identities are exact consequences of
  the centered zero-sum formula.
- The square-support D-0001 identity is inherited from `L-20704` and must share
  its normalization audit.
- The eventual and growth equivalences are inherited from `L-19801/L-19802` and
  therefore share their Landau/screw review status.
- This theorem is a global compression and witness-extraction result. It does
  not establish the required cofinal sign and does not claim RH.
