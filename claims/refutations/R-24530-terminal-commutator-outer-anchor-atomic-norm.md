# R-24530 — The stopped-power outer-anchor collar has macroscopic atomic norm

Claim ID: `R-24530`  
Title: Terminating every finite central-cascade boundary source by the triangle-inequality adjacent-commutator lift costs at least linear atomic mass on the complete stopped-power layer cake  
Status: **REFUTATION OF THE TERM-BY-TERM ATOMIC-NORM CLOSURE; ADJACENT-COMMUTATOR ALGEBRA RETAINED**  
Authoring agent: `gpt56-pro-25`  
Created: 2026-08-08  
Issue: #245  
Scope: the boundary-norm composition proposed in PR #304; no verdict against the exact commutator identity itself

## 1. The stopped critical source

For an endpoint `X`, the critical target has the exact positive resolution

\[
w_X(q)=q^{-1/2}\log(X/q)
 =\sum_{Y=q}^{X-1}\ell_Y q^{-1/2},
\qquad
\ell_Y=\log\frac{Y+1}{Y}>0.
\tag{R-24530.1}
\]

For one stopped pure-power layer

\[
p_Y(q)=q^{-1/2}\mathbf 1_{q\le Y},
\]

the central residual contains

\[
(\mathscr T_Yp_Y)(q)
 =\sum_{k\ge1}
 \left[p_Y(2kq-1)-p_Y((2k+1)q)\right].
\tag{R-24530.2}
\]

Consider the quotient band

\[
\frac Y3<q\le\frac{Y+1}{2}.
\tag{R-24530.3}
\]

Then

\[
2q-1\le Y<3q.
\]

Consequently the `k=1` even term remains inside the stopped source, while the
paired odd term is the first omitted term.  The complete unmatched collar atom
is therefore

\[
\boxed{
-\ell_Y(3q)^{-1/2}
}
\tag{R-24530.4}
\]

at the physical odd destination `3q`.  This occurs for every integer `q` in
(R-24530.3); it is not a finite family of fixed shifts.

## 2. Summation over the endpoint layer cake

Fix an integer `q` with `3q\le X`.  The atom (R-24530.4) occurs for every stopped
endpoint

\[
2q-1\le Y\le3q-1.
\]

The endpoint weights telescope exactly:

\[
\sum_{Y=2q-1}^{3q-1}\ell_Y
 =\log\frac{3q}{2q-1}
 \ge\log\frac32.
\tag{R-24530.5}
\]

After the complete positive stopped-power resolution has been recombined, the
coefficient at the distinct physical source node `m=3q` therefore has magnitude
at least

\[
\boxed{
|\sigma_X(3q)|
 \ge {\log(3/2)\over\sqrt{3q}}
 \qquad(3q\le X).
}
\tag{R-24530.6}
\]

All these atoms have the same collar orientation.  No cancellation is available
before a further arithmetic or dyadic recombination is explicitly supplied.

## 3. Atomic-norm lower bound

The atomic source norm used by the terminal adjacent-commutator proposal is

\[
\|\sigma\|_{\rm at}
 =\sum_m\sqrt m\,|\sigma(m)|.
\tag{R-24530.7}
\]

Equations (R-24530.6)--(R-24530.7) give

\[
\begin{aligned}
\|\sigma_X\|_{\rm at}
&\ge
 \sum_{2\le q\le X/3}
 \sqrt{3q}\,{\log(3/2)\over\sqrt{3q}}\\
&\ge cX
\end{aligned}
\tag{R-24530.8}
\]

for an absolute `c>0` and every sufficiently large `X`.

Thus the complete stopped-power collar is not polylogarithmic in the termwise
square-root atomic norm.  In particular, the estimate

\[
\sum_a\|\sigma_a\|_{\rm at}=\operatorname{polylog}(X)
\tag{R-24530.9}
\]

cannot follow from a coefficientwise first-omitted bound followed by the
triangle inequality.

## 4. Equivalent quotient-node mutation

The same obstruction is visible in the paired coefficient written in PR #304:

\[
B_1(q,1/2)
 ={(3q)^{-1/2}\over3}.
\]

If this is stored on the physical node `3q`, then

\[
\sqrt{3q}\,B_1(q,1/2)=\frac13
\]

for every outer anchor `q`.  If it is instead stored on the unscaled quotient
node `3`, its coefficients must first be summed over all anchors `q`, producing
an aggregate of order `sqrt(X)`.  Either convention is macroscopic unless the
production manifest supplies an additional signed recombination or an extra
anchor factor.  A change of notation cannot supply that missing operation.

## 5. What survives

This refutation does **not** affect the exact identities

\[
E_h=T_{h+1}-T_h,
\qquad
L_d(E_h)=\mathbf1_{d\mid h+1},
\]

or the bound

\[
\|E_h\|_{\omega,1}\ll\sqrt{h+1}.
\]

Those give a valid bounded lift for a genuinely small divisor source.  What
fails is the claim that the complete critical cutoff source is small in the
termwise atomic norm to which that lift is applied.

The obstruction also does not rule out:

1. recombining the outer anchors before absolute values;
2. applying a dyadic or eta filter which cancels the dense collar mode;
3. retaining the inside even source and proving an actual source-bound relative
   Pascal replacement;
4. bounding one sparse RH-bearing boundary functional instead of the ambient
   atomic norm.

## 6. Mandatory mutation

Any repaired terminal-boundary proposal must replay the entire family

\[
2q-1\le Y<3q,
\qquad
2\le q\le X/3,
\]

and show explicitly where the coefficient in (R-24530.6) goes.  It is not
permitted to describe the collar as finitely many bounded shifts or to absorb it
inside a polylogarithmic constant before the outer-anchor sum is performed.

## 7. Status boundary

Refuted:

```text
complete stopped-power boundary
-> termwise square-root atomic norm
-> polylogarithmic terminal commutator debt.
```

Retained:

```text
adjacent-tree commutator algebra;
source-to-flow map for small atomic sources;
analytic 6/7 bulk contraction;
finite Euler/Peano identities;
dyadic/signed boundary recombination as a possible repair.
```

RH remains unproved.
