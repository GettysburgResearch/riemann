# Finite-height verification gives a trillion-order E–Widder cone

Status: **PROPOSED EXACT THEOREM USING AN IMPORTED RIGOROUS ZERO-VERIFICATION INPUT; THE ALL-ORDER E–WIDDER INEQUALITY AND RH REMAIN UNPROVED.**

This note proves a large unconditional part of the E–Widder source inequality.  The mechanism is not numerical sampling of the Widder functionals.  It is an exact angular theorem for every invariant zero atom, combined with the published rigorous verification of RH through height `3*10^12`.

The result is:

\[
 \boxed{
 \mathcal W_k(u)>0
 \quad\text{for every }u>0
 \text{ and every integer }
 1\le k\le 4{,}710{,}000{,}000{,}000.
 }
 \tag{0.1}
\]

Equivalently, the E–Widder source inequality

\[
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 <\mathcal G_k(u)
 \tag{0.2}
\]

holds throughout the same complete range of `u` and `k`.

More generally, the proof gives a height–order theorem for the full two-parameter Widder cone, not only its diagonal.

## 1. The full Widder quantities

Retain

\[
 q(u)=2\frac{\mathfrak X'(u)}{\mathfrak X(u)},
 \qquad
 \mathfrak X(s(s-1))=\xi_{\rm R}(s).
\]

For integers `n,k>=0`, define

\[
 \boxed{
 F_{n,k}(u)
 =(-1)^nD_u^{n+k}\bigl[u^kq(u)\bigr].
 }
 \tag{1.1}
\]

The diagonal E–Widder functional is

\[
 \mathcal W_k=F_{k-1,k}
 \qquad(k\ge1).
 \tag{1.2}
\]

For a Stieltjes function all `F_{n,k}` are nonnegative.  The point here is that a very large finite portion of this cone can be proved directly from finite-height RH verification and the geometry of the critical strip.

## 2. Invariant zero product without assuming RH

Let `rho=beta+i gamma` be a nontrivial zero of `zeta`.  The functional-equation pair `rho,1-rho` has the common invariant coordinate

\[
 \rho(\rho-1).
\]

Put

\[
 \boxed{
 a_\rho=-\rho(\rho-1).
 }
 \tag{2.1}
\]

Choose one `a` for each functional-equation orbit, with multiplicity.  Conjugation closes the resulting multiset.  Since `mathfrak X` has order at most `1/2`, its genus-zero product gives locally uniformly on the complement of its zeros

\[
 q(u)=2\sum_a\frac1{u+a}.
 \tag{2.2}
\]

No RH assumption enters (2.2).

For one atom, the exact identity

\[
 \boxed{
 (-1)^nD_u^{n+k}\left[\frac{u^k}{u+a}\right]
 =(n+k)!\frac{a^k}{(u+a)^{n+k+1}}
 }
 \tag{2.3}
\]

follows either by polynomial division or from the standard Widder kernel calculation.  Therefore

\[
 \boxed{
 F_{n,k}(u)
 =2(n+k)!\sum_a
 \frac{a^k}{(u+a)^{n+k+1}}.
 }
 \tag{2.4}
\]

The series is absolutely and locally uniformly convergent.  For `k>=1` its terms are `O(|a|^{-n-1})`; for `k=0` the differentiated logarithmic-derivative series has the same standard local convergence after functional-equation-orbit grouping.

On the critical line, `beta=1/2`,

\[
 a_\rho=\gamma^2+\frac14>0,
\]

so every critical invariant atom contributes strictly positively to every `F_{n,k}`.

## 3. Exact phase bound for one off-line orbit

Write

\[
 \rho=\beta+i\gamma,
 \qquad 0<\beta<1,
 \qquad \gamma\ne0.
\]

Then

\[
 a=a_\rho=A+iB
\]

with

\[
 A=\gamma^2+\beta(1-\beta)>\gamma^2,
 \qquad
 B=-\gamma(2\beta-1).
 \tag{3.1}
\]

Consequently

\[
 \boxed{
 \frac{|B|}{A}<\frac1{|\gamma|},
 \qquad
 |\arg a|<\arctan\frac1{|\gamma|}.
 }
 \tag{3.2}
\]

Fix `u>0`.  Let

\[
 \theta=\arg a,
 \qquad
 \phi=\arg(u+a).
\]

Because `A>0`, adding the positive real number `u` preserves the sign of the argument and decreases its magnitude.  Hence, for `theta>=0`,

\[
 0\le\phi\le\theta,
\]

and the inequalities reverse symmetrically when `theta<0`.

The phase of the atom in (2.4) is

\[
 \Psi_{n,k}
 =k\theta-(n+k+1)\phi.
 \tag{3.3}
\]

As `phi` ranges between `0` and `theta`, this phase lies between

\[
 k\theta
 \quad\text{and}\quad
 -(n+1)\theta.
\]

Therefore

\[
 \boxed{
 |\Psi_{n,k}|
 \le
 \max\{k,n+1\}\,|\theta|
 <
 \max\{k,n+1\}
 \arctan\frac1{|\gamma|}.
 }
 \tag{3.4}
\]

The conjugate invariant zero contributes the conjugate atom.  Their combined contribution is

\[
 4(n+k)!\Re\left[
 \frac{a^k}{(u+a)^{n+k+1}}
 \right].
 \tag{3.5}
\]

It is strictly positive whenever

\[
 \max\{k,n+1\}
 \arctan\frac1{|\gamma|}<\frac\pi2.
 \tag{3.6}
\]

This is uniform in `u>0`.

### Algebraic form of the same angular lemma

For the diagonal atom, put

\[
 z(u,a)=\frac{a}{(u+a)^2}.
\]

A direct expansion gives

\[
 \Re z
 =\frac{A(u+A)^2+B^2(2u+A)}{|u+a|^4}>0,
\]

\[
 \Im z
 =\frac{B(u^2-|a|^2)}{|u+a|^4}.
\]

Cross multiplication yields

\[
 |\arg z(u,a)|\le|\arg a|.
\]

Thus the diagonal pair is positive whenever `k|arg a|<pi/2`.  Section 3.3 is the corresponding full-`F_(n,k)` statement.

## 4. Finite-height-to-finite-order theorem

### Theorem FHWC

Assume that every nontrivial zeta zero with

\[
 0<|\gamma|\le H
\]

lies on the critical line.  Let `M` be a positive integer satisfying

\[
 \boxed{
 M\arctan(1/H)<\frac\pi2.
 }
 \tag{4.1}
\]

Then, for every `u>0`,

\[
 \boxed{
 F_{n,k}(u)>0
 \quad\text{whenever}\quad
 n,k\ge0,
 \quad
 \max\{k,n+1\}\le M.
 }
 \tag{4.2}
\]

In particular,

\[
 \boxed{
 \mathcal W_j(u)>0
 \quad(1\le j\le M,\ u>0).
 }
 \tag{4.3}
\]

#### Proof

Every zero at height at most `H` is critical by hypothesis, so its invariant atom is positive real and contributes positively.

Every off-line zero has `|gamma|>H`.  By (3.4), for `max{k,n+1}<=M`,

\[
 |\Psi_{n,k}|
 <M\arctan(1/H)<\frac\pi2.
\]

Therefore every off-line conjugate pair also contributes positively.  The orbit-grouped series (2.4) is absolutely convergent, so summing preserves positivity.  At least one critical zero exists, hence the result is strict.  This proves (4.2), and (4.3) follows from `W_j=F_(j-1,j)`.  `square`

No simplicity assumption is used.

## 5. Published numerical corollary

Platt and Trudgian rigorously proved, using interval arithmetic and a Turing-method count, that every nontrivial zero with

\[
 0<\gamma\le3\cdot10^{12}
\]

lies on the critical line.  The repository already carries the exact external source lock

```text
EXT.XI.PLATT_TRUDGIAN.2021
```

for this theorem.  The external computation is imported; it was not rerun in this pass.

Take

\[
 H=3{,}000{,}000{,}000{,}000,
 \qquad
 M=4{,}710{,}000{,}000{,}000.
\]

Then

\[
 \frac MH=\frac{157}{100}.
\]

Using the elementary inequalities

\[
 \arctan y<y\quad(y>0),
 \qquad
 \pi>3.14,
\]

we obtain

\[
 M\arctan(1/H)
 <\frac MH
 =1.57
 <\frac\pi2.
\]

Theorem FHWC therefore yields

\[
 \boxed{
 F_{n,k}(u)>0
 \quad
 \left(
 \max\{k,n+1\}\le
 4{,}710{,}000{,}000{,}000
 \right)
 }
 \tag{5.1}
\]

for every `u>0`, and in particular the diagonal theorem (0.1).

## 6. Source-side consequence

The Euler-safe identity in the parent dossier is

\[
 \mathcal W_k(u)
 =\mathcal G_k(u)
 -\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n).
\]

Combining it with (0.1) proves

\[
 \boxed{
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \mathcal L_k(u,\log n)
 <\mathcal G_k(u)
 }
 \tag{6.1}
\]

for every `u>0` and every integer

\[
 1\le k\le4{,}710{,}000{,}000{,}000.
\]

This is an actual proof of the E–Widder source inequality through more than four trillion complete derivative orders, not a finite `u` panel.

## 7. Failure-localization corollary

Let

\[
 R=\max\{k,n+1\}\ge1.
\]

If

\[
 F_{n,k}(u)<0
\]

at some `u>0`, then there must exist an off-line zero `beta+i gamma` satisfying

\[
 \boxed{
 |\gamma|<\cot\left(\frac\pi{2R}\right).
 }
 \tag{7.1}
\]

Indeed, if every off-line zero had height at least the right side, then every conjugate pair would obey (3.6) and every term in (2.4) would be nonnegative.

For the diagonal hierarchy this reads

\[
 \boxed{
 \mathcal W_k(u)<0
 \Longrightarrow
 \text{an off-line zero exists below height }
 \cot\left(\frac\pi{2k}\right).
 }
 \tag{7.2}
\]

As `k` grows,

\[
 \cot\left(\frac\pi{2k}\right)
 =\frac{2k}{\pi}+O(k^{-1}).
\]

Thus Widder order is a quantitative zero-height microscope: an order-`k` failure cannot be caused solely by off-line zeros far above height approximately `2k/pi`.

The converse is not asserted.  An off-line zero below that height need not by itself force the complete sum negative at that same order.

## 8. What this closes and what remains

The previous front door called `W_2>=0` the first new theorem-sized target.  Theorem FHWC supersedes that statement:

```text
W_k(u)>0 for every u>0 and 1<=k<=4.71*10^12  PROVED FROM IMPORTED VERIFIED HEIGHT
full F_(n,k) cone with max(k,n+1)<=4.71*10^12 PROVED FROM IMPORTED VERIFIED HEIGHT
all k with no upper bound                              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                     UNPROVED
```

The first unresolved diagonal order relative to the imported height theorem is

\[
 k=4{,}710{,}000{,}000{,}001.
\]

That integer is not intrinsically special.  It is simply where the present finite-height angular budget ends.  A proof of all orders must add a height-free mechanism that rules out, cancels or positively absorbs the phase rotation of hypothetical off-line invariant atoms above the verified range.

## 9. Review points

Independent review should check:

1. orbit multiplicity in the invariant genus-zero product;
2. the atom formula (2.3);
3. absolute/local uniform convergence in (2.4);
4. the exact interval for the phase in (3.3);
5. the critical-strip bound `|arg a|<arctan(1/|gamma|)`;
6. use of the external verified-height theorem without silently rerunning or strengthening it;
7. the rational `M/H=157/100` corollary;
8. the strict source inequality (6.1);
9. the one-way nature of the failure-localization corollary.
