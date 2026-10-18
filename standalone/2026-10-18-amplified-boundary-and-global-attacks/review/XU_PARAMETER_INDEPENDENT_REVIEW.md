# Independent review of the new Xu--Sang parameter choice

**Verdict: PASS for the exact numerical hypotheses and their use through the
stated imported analytic interface.** This is a source-qualified global
zero-free consequence, not a verification of all analytic inputs imported
by Xu--Sang from OpenAI. No unconditional RH claim is made.

The candidate reviewed here is

\[
 \begin{gathered}
 B=\frac{43744333}{50000000}=0.87488666,\qquad
 b=\frac{173}{2000},\qquad
 \ell=\frac{6267001}{37500000},\qquad
 \kappa=\frac{29991}{40000},\\
 g=10^{-8},\qquad \zeta=10^{-10},\qquad g_*=5\cdot10^{-9}.
 \end{gathered}
\]

The independent checker was written directly from the formulas in
Xu--Sang, arXiv:2610.15291v2. It imports no polynomial, coefficient list,
or code from the parent agent's checker.

## 1. Analytic interface and dependency check

Primary source inspected directly:

Yuanda Xu and Hejian Sang, *Amplified moments and a refinement of the
quasi-Riemann hypothesis*, arXiv:2610.15291v2, October 15, 2026:
<https://arxiv.org/html/2610.15291v2>.

The relevant source statements have the following roles:

- Proposition 3.1 supplies the same compensated probe, direct estimate,
  and principal term for admissible \(b,\ell\).
- Proposition 4.1 and equation (21) give the row-count exponent
  \(R_\kappa(\delta,x)\).
- Proposition 5.1 supplies the amplified numerator moment under the
  separately licensed family bound.
- Section 6.2 lists **all** numerical admissibility hypotheses;
  Proposition 6.1 then gives a common positive saving for every target,
  assuming those hypotheses and the imported analytic inputs.
- Lemma 8.1 converts any licensed admissible choice into the global family
  bound \(\beta_*\le B(\ell)\), where
  \(B(\ell)=11/12-\ell/4\).

The current parameters stay within the exact Section 6.2 ranges. In
particular \(\kappa\) is not decreased below the source's lower endpoint,
and \(B>87/100\), so no new moment-range or contour extension is required.

The source's established first-stage conclusion licenses this choice:

\[
 \frac{1+\kappa}{2}=\frac{69991}{80000}=0.8748875.
\]

It is the family-wide conclusion of Xu--Sang, not a statement about a
single target. This distinction preserves the auxiliary denominator
family and the supremum argument in Lemma 8.1. The final implication
concerns all finite-order Hecke targets over the same Eisenstein field,
and the source's norm-pullback transfer gives every Dirichlet target,
including ordinary zeta. The target constants and thresholds may vary;
the positive exponent saving is common, exactly as required by the source.

The resulting new boundary differs from the source's stated final
boundary by

\[
 \frac{8748867}{10000000}-\frac{43744333}{50000000}
      =\frac1{25000000}=4\cdot10^{-8}>0.
\]

The novelty asserted is this parameter choice and its exact certificate.
The endpoint criterion, analytic argument, and zero-free transfer are
Xu--Sang's imported framework.

## 2. Endpoint reconstructed over the entire rectangle

The independent checker sets

\[
 \begin{split}
 \alpha&=5/6,\quad c=(3\kappa)^{-1},\quad x=1/2-y,\\
 D&=3-(1+2c)x,\quad P=(2-2cx)(1-x),\\
 J&=(\alpha-\delta)D+\delta P,\\
 R&=1-\delta+(\alpha-\delta)\delta P/(2J),\\
 E&=C_0+\delta/2+\delta x\{\ell+c(h/4-l_y/2)\}
                              -(3h/4)(1-R).
 \end{split}
\]

Here \(h=(1+b+3\ell)/2\), \(l_y=(1+b-\ell)/2\), and
\(C_0=-1/4+b/6+5\ell/4\), as in the source. Clearing the denominator
directly gives

\[
 Q=-8J(E+g)=A(y)\delta^2+B_q(y)\delta+C(y).
\]

All coefficients of \(A\) and of \(4AC-B_q^2\) are strictly positive
rational numbers. Their complete values are recorded in the receipt;
in particular the latter polynomial's constant coefficient is exactly

\[
 \frac{6859827102685708103245732680491}
      {3317522235754679229200625000000000000}>0.
\]

The exact polynomial identity

\[
 4A Q=(2A\delta+B_q)^2+(4AC-B_q^2)
\]

was also checked coefficientwise. Hence \(Q>0\) for every real \(\delta\)
and every \(y\ge0\). On the relevant rectangle
\(0\le\delta\le5/6\), \(0\le x\le1/2\), both \(D,P\) are positive,
and \(J>0\). Therefore \(E<-g\) on the full rectangle, including the
smaller rectangle required in Section 6.2. There is no grid-to-continuum
inference.

## 3. Scalar conditions and error margins

Every other Section 6.2 condition was checked by exact rational
comparison. These include the direct geometry, both prime-supply
constraints, the supply at \(h+\zeta\), the numerator contour range,
the three estimates for remaining row classes, and the order of the
positive error margins.

Some of the smaller retained margins are

\[
 \begin{split}
 \ell/(h+\zeta)-21/100
    &=\frac{1184154737}{2381790120300}>0,\\
 -1/250-(C_0+A_{\rm sm}/8)
    &=\frac{1644686354141}{8931712950000000}>0,\\
 g-2\zeta-g_*&=\frac{3}{625000000}>0.
 \end{split}
\]

The full receipt records every margin, including the inclusive equality
at the moment-range endpoint and the exact licensing equality.

The small numerical size of the gain does not change the quantifiers:
the source's analytic losses can be chosen within a fixed positive
margin. It may make effective constants or thresholds very large; no
numerical effective threshold is claimed by this review.

## 4. Reproduction and frozen identities

From the directory containing this review:

```sh
python check_xu_candidate_independent.py --b 173/2000 --output replay.json
python -O check_xu_candidate_independent.py --b 173/2000 --output replay_optimized.json
```

Both executions completed successfully and produced byte-identical
receipts. Required checks use explicit exceptions, so Python optimization
does not disable them.

SHA-256 identities:

| File | SHA-256 |
|---|---|
| `check_xu_candidate_independent.py` | `3073b30e1d5e0223b424d95789d107b1ff59e810aa6f824fddcf5061da23fdbb` |
| `xu_candidate_independent_root_params.json` | `c4e7acaeaaa0f3e35725509631549ebfcd53f27a16f2bfa28337794a1171e4e3` |

The checker also found a passing nearby choice \(b=86457/10^6\), but that
choice is not needed for the reviewed result. The commands above specify
the parent candidate explicitly.

This review does not bind a parent proof or certificate that has not yet
been frozen. It independently establishes the claimed numerical
admissibility and the applicability of the stated source-qualified
consumer. Any subsequent parent changes require a separate hash check.
