# L-32314 — Eventual one-sign of the shifted bottom tail already implies RH

Claim ID: `L-32314`

Status: **PROPOSED COMPLETE CONDITIONAL FIREWALL — INDEPENDENT REVIEW REQUESTED**

Created: 2026-08-09

Dependencies: `L-32313`; Landau's one-sign theorem; standard real-axis facts for zeta

Scope: corrects the strength classification of the global bottom-tail sign.  It does not prove that sign and does not prove RH unconditionally.

## 1. Bottom-tail transform

Retain

\[
\mathcal C(x)
=\sum_{n\le x}\mu(n)
\left(\frac1{\sqrt n}-\frac1{\sqrt x}\right)^2
\]

from `L-32313`.  Its Mellin transform is

\[
\boxed{
F(s)
:=\int_1^\infty \mathcal C(x)x^{-s-1}\,dx
=\frac1{s(s+1)(2s+1)\zeta(s+1)}.
}
\tag{L-32314.1}
\]

Initially this is an absolute-convergence identity for `Re s>0`, followed by the displayed meromorphic continuation.

`L-32313` correctly notes that the apparent singularity at `s=0` is removable.

## 2. There is a positive real anchor pole at s=-1/2

At

\[
s=-\frac12,
\]

one has `s+1=1/2`, and `zeta(1/2)` is finite and nonzero.  Thus the factor `2s+1` gives a genuine simple pole:

\[
\boxed{
\operatorname*{Res}_{s=-1/2}F(s)
=-\frac2{\zeta(1/2)}.
}
\tag{L-32314.2}
\]

Moreover

\[
\zeta(1/2)<0,
\]

so this residue is strictly positive.

For completeness, the sign follows from

\[
\zeta(\sigma)
=\frac{\eta(\sigma)}{1-2^{1-\sigma}},
\qquad0<\sigma<1,
\]

where the alternating Dirichlet eta series is positive and the denominator is negative.

Thus the shifted-zeta tail has a canonical real singularity at exactly the RH scale `-1/2`.

## 3. No other real singularity lies to its right

On the real interval

\[
-\frac12<s<0,
\]

one has

\[
\frac12<s+1<1.
\]

The eta representation above shows that `zeta(s+1)` is finite and nonzero there.  The elementary factors

\[
s,\qquad s+1,\qquad2s+1
\]

are also nonzero on the open interval.

At `s=0` the zeta pole cancels the explicit factor `s`, as already proved in `L-32313`.

Consequently

\[
\boxed{
F(s)\text{ has no real singularity on }(-1/2,\infty).
}
\tag{L-32314.3}

## 4. Eventual one-sign excludes every off-line zero

Put

\[
f(t)=\mathcal C(e^t),
\qquad t\ge0.
\]

Then `F(s)` is the Laplace transform

\[
F(s)=\int_0^\infty f(t)e^{-st}\,dt.
\tag{L-32314.4}
\]

Assume that `C(x)` is eventually of one sign.  Multiplying by `-1` if necessary, assume

\[
f(t)\ge0
\]

for all sufficiently large `t`.

Let `sigma_c` be the abscissa of convergence of the tail Laplace transform after removing a fixed compact initial interval.  Landau's one-sign theorem says that if `sigma_c` is finite, then the continued transform must have a singularity at the **real point** `s=sigma_c`.

Suppose now that zeta has a nontrivial zero

\[
\rho=\beta+i\gamma,
\qquad\beta>\frac12.
\]

Equation (L-32314.1) has an uncancelled pole at

\[
s_\rho=\rho-1,
\qquad
\Re s_\rho=\beta-1>-\frac12.
\tag{L-32314.5}
\]

Therefore the Laplace transform cannot be analytic on the whole half-plane

\[
\Re s>\beta-1,
\]

and in particular

\[
\boxed{\sigma_c\ge\beta-1>-\frac12.}
\tag{L-32314.6}
\]

Landau then forces a real singularity at `s=sigma_c`, strictly to the right of `-1/2`.  This contradicts (L-32314.3).

Hence no nontrivial zeta zero can satisfy `Re rho>1/2`.  Functional-equation symmetry gives

\[
\boxed{\mathrm{RH}.}
\tag{L-32314.7}

Thus

\[
\boxed{
\mathcal C(x)\text{ eventually one-signed}
\Longrightarrow\mathrm{RH}.
}
\tag{L-32314.8}

The same implication holds for either eventual sign.

## 5. Correction to the previous scope classification

`L-32313` correctly identified the shifted denominator `zeta(s+1)` and correctly warned that a global sign theorem is nontrivial.  Its Section 6, however, classified eventual one-sign only as implying some unspecified fixed zero-free strip.

The real anchor pole at `s=-1/2` sharpens that argument completely:

```text
real pole at -1/2
+
no real singularity to its right
+
Landau one-sign theorem
=> no nonreal pole to its right
=> Re rho <= 1/2
=> RH.
```

Accordingly the global sign of the bottom tail is **not a soft shifted-zeta theorem**.  It is another RH-bearing one-sign criterion.

This does not invalidate the use of finite-depth numerical/lower bounds for `C_R` inside the outer SHARP theorems.  It only blocks the strategy of proving one universal eventual sign as an allegedly easier continuation.

## 6. Proof boundary

Closed here, subject to independent review:

1. the genuine real pole at `s=-1/2`;
2. positivity of its residue;
3. absence of any real singularity in `(-1/2,infinity)`;
4. Landau contradiction from any off-line zeta zero;
5. the corrected implication `eventual one-sign of C -> RH`.

Open:

1. any eventual sign theorem for `C`;
2. the all-depth tail-vs-threshold estimate of SHARP;
3. RH itself.
