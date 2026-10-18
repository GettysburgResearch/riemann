# An exact parameter corollary with boundary 0.87488666

**Claim ID:** `AMPLIFIED-BOUNDARY-87488666-20261018`  
**Status:** proved parameter corollary of the explicitly imported analytic framework below; proposed repository contribution.  
**Scope:** a fixed half-plane at every height and conductor, conditional on those analytic imports.  
**New work:** a rational parameter choice, its complete exact admissibility certificate, and independent reconstruction.  
**Not established here:** the upstream analytic inputs, a substantially stronger boundary, or RH.

## 1. Statement and exact dependencies

Let \(F=\mathbb Q(\sqrt{-3})\). Assume the analytic hypotheses in Section 2 of Yuanda Xu and Hejian Sang, *Amplified moments and a refinement of the quasi-Riemann hypothesis*, [arXiv:2610.15291v2, October 15, 2026](https://arxiv.org/html/2610.15291v2). In particular, the family-wide \(7/8\) conclusion and the specified reflection, detector, and moment inputs from the September 30, 2026 OpenAI manuscript are hypotheses, not independently verified results of this packet.

**Theorem.** Under those hypotheses, every finite-order Hecke \(L\)-function over \(F\), and every Dirichlet \(L\)-function, is nonzero in

\[
 \boxed{\operatorname{Re}s>B_\dagger
   :=\frac{43744333}{50000000}=0.87488666.}
\]

Principal poles at \(s=1\) are allowed. In particular the conclusion applies to ordinary \(\zeta(s)\). No height cutoff is imposed. The claim is an import-dependent theorem; the exact computation below does not authenticate the imported analytic proofs.

The proof uses Xu--Sang's general closure criterion (Lemma 8.1), its admissibility definition (Section 6.2), and its first-stage family conclusion from Sections 7--8. The analytic probe and its estimates are theirs. The new boundary is smaller than their stated final boundary by exactly

\[
 \frac{8748867}{10000000}-B_\dagger
      =\frac1{25000000}=4\cdot10^{-8}.
\]

This is the scale of the improvement claimed here. No literature-wide priority claim is made for this decimal.

## 2. The parameter choice and its license

Choose

\[
 \begin{gathered}
 b=\frac{173}{2000},\qquad
 \ell=\frac{6267001}{37500000},\qquad
 \kappa=\frac{29991}{40000},\\
 g=\frac1{100000000},\qquad
 r=\frac1{10000000000},\qquad
 g_*=\frac1{200000000}.
 \end{gathered}
\]

Here \(r\) denotes the row-range extension called \(\zeta\) in the source and in the JSON certificate; it is unrelated to the Riemann zeta function. Set

\[
 \begin{split}
 l_x&=(1-b-\ell)/2=\frac{27989249}{75000000},\\
 l_y&=(1+b-\ell)/2=\frac{34476749}{75000000},\\
 h&=(1+b+3\ell)/2=\frac{19848251}{25000000},\\
 C_0&=-1/4+b/6+5\ell/4=-\frac{266833}{10000000}.
 \end{split}
\]

Two exact identities are essential:

\[
 B(\ell)=\frac{11}{12}-\frac\ell4=B_\dagger,
 \qquad \frac{1+\kappa}{2}=\frac{69991}{80000}.
\]

The second number is the *previously established first-stage family bound* of Xu--Sang. Thus the moment parameter is licensed before this new choice is used. There is no inference from the proposed conclusion back into its own moment hypothesis. We keep the full family required by that hypothesis; replacing it with only the zeros of ordinary zeta would not license this proof.

For \(C_b(s)=s-(4+b)/6\), also

\[
 l_x/2+b/12=C_b(B_\dagger).
\]

This matches the direct estimate to the candidate boundary in the unchanged probe normalization.

## 3. A proof over the whole continuous rectangle

We now prove the only non-scalar admissibility condition. Use the source's row exponent, with

\[
 \begin{gathered}
 \alpha=5/6,\quad c=(3\kappa)^{-1}=\frac{40000}{89973},\\
 D=3-(1+2c)x,\qquad P=(2-2cx)(1-x),\\
 J=(\alpha-\delta)D+\delta P,\qquad
 R=1-\delta+\frac{(\alpha-\delta)\delta P}{2J}.
 \end{gathered}
\]

The endpoint to be controlled is

\[
 E=C_0+\frac\delta2
   +\delta x\left\{\ell+c\left(\frac h4-\frac{l_y}2\right)\right\}
   -\frac{3h}{4}(1-R).
\]

We will show \(E<-g\) for \(0\le\delta\le5/6\), \(0\le x\le1/2\), which contains the source's required rectangle.

On that rectangle,

\[
 D\ge\frac52-c=\frac{369865}{179946}>0,
 \qquad
 P\ge\frac{2-c}{2}=\frac{69973}{89973}>0.
\]

Consequently \(J>0\), including at both endpoints in \(\delta\). Put \(y=1/2-x\ge0\). Clearing this positive denominator gives the identity

\[
 Q:=-8J(E+g)=A(y)\delta^2+B_q(y)\delta+C(y).
\]

This identity is checked by independent symbolic expansion over rational numbers. To make its construction reproducible without a symbolic algebra package, define

\[
 T(y)=\frac12-\frac{3h}{4}
          +x\left\{\ell+c\left(\frac h4-\frac{l_y}2\right)\right\}.
\]

Then the coefficient polynomials are exactly

\[
 \begin{split}
 A&=-8\{T(P-D)-3hP/8\},\\
 B_q&=-8\{(C_0+g)(P-D)+\alpha TD+3h\alpha P/8\},\\
 C&=-8\alpha(C_0+g)D.
 \end{split}
\]

Their full rational coefficients are in [certificate.json](certificate.json). For a human-readable positive certificate, the coefficients of \(A\), in ascending powers of \(y\), are

\[
 \left(
 \frac{503792967617747563}{303567777337500000},
 \frac{162640300396334993}{50594629556250000},
 \frac{30201978010901243}{12648657389062500},
 \frac{16538148991136}{15178388866875}
 \right).
\]

The coefficients of \(4AC-B_q^2\), again in ascending powers, are

\[
 \begin{split}
 &\frac{6859827102685708103245732680491}
 {3317522235754679229200625000000000000},\\
 &\frac{1590124257100755878943504353066767283}
 {829380558938669807300156250000000000},\\
 &\frac{1748977444202728230363766666937535013}
 {276460186312889935766718750000000000},\\
 &\frac{123231782221401249592372215732930161}
 {20734513973466745182503906250000000},\\
 &\frac{2776840561372205854616252535910559}
 {2073451397346674518250390625000000}.
 \end{split}
\]

Every displayed numerator and denominator is positive. Hence \(A(y)>0\) and \(4A(y)C(y)-B_q(y)^2>0\) for every \(y\ge0\). Completing the square gives

\[
 4A Q=(2A\delta+B_q)^2+(4AC-B_q^2)>0.
\]

Thus \(Q>0\) for all real \(\delta\) and \(y\ge0\). On the original rectangle \(J>0\), so \(E+g=-Q/(8J)<0\), as required. This is a finite exact polynomial proof of a continuum assertion. Sampling a grid, fitting a maximum, or locating finitely many zeros plays no role in its acceptance.

## 4. All remaining numerical conditions

The scalar conditions are checked directly as rational inequalities. For completeness, the checker covers all of the following groups:

| Purpose | Predicates checked |
|---|---|
| Geometry and allowed source region | \(b>0\), \(1/6\le\ell\le1/5\), \(29991/40000\le\kappa\le3/4\), \(B_\dagger>87/100\), \(l_x>\ell\), \(l_y-\ell>11b/6\) |
| Prime supply and numerator displacement | \(6\kappa\ell>3/4\), \(\ell/h<1/(6\kappa)\), \(\ell/(h+r)>21/100\), \(h/2<l_y<1/2\) |
| Retained positive margins | \(0<g_*<1/1000\), \(0<2r<1/1000\), \(g-2r>g_*\) |
| Other row ranges | The three inequalities below, including both endpoints of the first maximum |
| License and comparison | The exact preceding-stage licensing equality and \(8748867/10^7>B_\dagger\) |

Define \(A_{\rm sm}=1/2+(\ell/2)(1/2+2\ell/h)-h/2\), \(z_0=17/50\), and \(d_{\min}=1/100\). The three remaining bounds are

\[
 \begin{gathered}
 \max\{C_0,C_0+A_{\rm sm}/8\}<-1/250,\\
 C_0+(1/2+3\ell/2)/50<-1/100,\\
 h(z_0-1/6)-l_y/2+2d_{\min}<-1/20.
 \end{gathered}
\]

For example, exact retained gaps are

\[
 \begin{split}
 \ell/(h+r)-21/100&=\frac{1184154737}{2381790120300},\\
 -1/250-C_0-A_{\rm sm}/8
   &=\frac{1644686354141}{8931712950000000},\\
 -1/100-C_0-(1/2+3\ell/2)/50&=\frac{521781}{312500000},\\
 -1/20-h(z_0-1/6)+l_y/2-2d_{\min}
   &=\frac{83364199}{3750000000},\\
 g-2r-g_*&=\frac3{625000000}.
 \end{split}
\]

All are positive. The receipt contains 21 strict scalar margins and three inclusive margins, including the two licensing/range equalities. The continuum endpoint and denominator checks are additional. The criterion therefore handles the other row scales and complete remainders through its stated analytic consumer; it does not discard them on the basis of the endpoint alone.

## 5. Why the conclusion is global

Write \(\beta_*\) for the supremum of real parts of nontrivial zeros in the complete finite-order Hecke family over \(F\), adjoining \(1/2\) to the set as in the source. The imported first stage gives

\[
 \beta_*\le\frac{69991}{80000}=\frac{1+\kappa}{2}.
\]

Sections 3--4 prove every numerical hypothesis of Xu--Sang's general Lemma 8.1 for this licensed tuple. Applying that lemma yields \(\beta_*\le B_\dagger\). Its scope is a supremum over the whole family, with a common positive exponent saving; no assumption that the supremum is attained is needed. The source's proof compares the two estimates of one normalized probe and continues the reciprocal target \(L\)-function by Mellin inversion. The nonvanishing principal multiplier is part of that imported interface. The vanishing of the reciprocal at a principal pole causes no exception.

The Dirichlet conclusion uses the same norm-pullback transfer specified in Xu--Sang's theorem. For ordinary zeta, it also follows immediately from

\[
 \zeta_F(s)=\zeta(s)L(s,\chi_{-3}).
\]

The nonprincipal factor on the right is entire. At a nontrivial zero of \(\zeta\), it cannot cancel that zero. Thus the established Hecke-family conclusion includes the claimed ordinary-zeta half-plane. This specialization needs one auxiliary number field. Removing the family of auxiliary characters from the licensing step would require a different argument.

## 6. Reproduction and authentication boundary

From this directory:

```sh
python certify_boundary.py --check certificate.json
python -O certify_boundary.py --check certificate.json
```

Only the Python standard library is required. All acceptance comparisons use exact integers and `fractions.Fraction`; no floating-point number participates in the proof. Required checks raise explicit exceptions and remain active under `python -O`.

The independent checker in the packet's `review/` directory reconstructs \(Q\) directly in a separate bivariate rational polynomial ring. It imports neither this checker nor its coefficient data. With `--b 173/2000`, it reproduces every parameter, all 24 scalar margins, and all coefficients of \(A,B_q,C,4AC-B_q^2\). The independent report binds the reviewed files by SHA-256.

The primitive mathematical input to these computations is the explicit endpoint and admissibility interface of the cited source. They authenticate the new rational algebra against that interface. They do not replay cubic-theta reflection, Hecke moment estimates, Euler corrections, or the upstream family \(7/8\) argument. The smallest load-bearing external statement for the final implication is Xu--Sang's general licensed-parameter closure lemma together with its stipulated hypotheses.

The gain is fixed but very small, so the source's loss parameters can be placed inside the positive margins. This argument does not calculate an effective numerical height threshold or useful uniform numerical constants. Those are not needed for the quantified half-plane consequence.
