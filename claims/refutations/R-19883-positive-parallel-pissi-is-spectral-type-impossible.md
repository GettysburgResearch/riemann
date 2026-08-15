# R-19883 — A positive parallel PSSI cannot contain a nonzero diffuse native-defect string

Claim ID: `R-19883`  
Status: **PROVED EXACT REFUTATION OF THE PSSI FORMULATION IN T-19819**  
Authoring agent: `gpt56-pro-09-y`  
Created: 2026-08-15  
Depends on: uniqueness of Stieltjes measures; `L-92100`; `L-19884`; strict factor-67 reserve `L-91724`  
RH status: **unproved; the contradiction is internal to the proposed PSSI**

## 1. The proposed positive parallel identity

`T-19819` asks for

\[
 p_\Xi(q)
 =p_{\rm row,a}(q)
  +\mathscr S_a(q)
  +p_{\rm arch,a}(q),
\tag{R-19883.1}
\]

where every term on the right is Stieltjes and

\[
 \mathscr S_a(q)
 =\int_0^\infty
  \frac{e^{-ax}\Delta(e^x)}{q+x}dx.
\tag{R-19883.2}
\]

Its representing measure is the absolutely continuous positive measure

\[
 d\nu_a(x)=e^{-ax}\Delta(e^x)dx.
\tag{R-19883.3}
\]

## 2. PSSI itself forces a pure-point left-hand measure

If (R-19883.1) holds with positive Stieltjes terms, then `p_Xi` is Stieltjes. The analytic equivalence in `L-92100` then forces RH. Under RH,

\[
\boxed{
 p_\Xi(q)
 =2\sum_{\gamma>0}
   \frac{m_\gamma}{q+\gamma^2},
}
\tag{R-19883.4}
\]

so its unique Stieltjes measure is

\[
\boxed{
 \mu_\Xi
 =2\sum_{\gamma>0}m_\gamma\delta_{\gamma^2},
}
\tag{R-19883.5}
\]

which is purely atomic.

## 3. Measure uniqueness forbids the diffuse summand

Let `mu_row` and `mu_arch` be the positive representing measures of the other two terms in (R-19883.1). Uniqueness of the Stieltjes transform gives

\[
\boxed{
 \mu_\Xi=\mu_{\rm row}+\nu_a+\mu_{\rm arch}.
}
\tag{R-19883.6}
\]

Hence `nu_a<=mu_Xi` as positive measures. But a measure absolutely continuous with respect to Lebesgue measure cannot be a nonzero submeasure of the countable pure-point measure (R-19883.5). Therefore

\[
\boxed{\nu_a=0,}
\tag{R-19883.7}
\]

or equivalently

\[
 \Delta(e^x)=0
 \quad\text{for almost every }x.
\tag{R-19883.8}
\]

Thus positive parallel PSSI is possible only when the native-defect string is identically absent.

## 4. The repaired factor-67 packet has strictly positive native defect

The all-column/knot-collar reserve gives, for sufficiently large `X`,

\[
 s_X(2)>
 \frac{\Omega_X(2)}{2(\sqrt K+130)}.
\tag{R-19883.9}
\]

For `X>=8`,

\[
 \Omega_X(2)
 =\frac{\log4}{\sqrt2},
 \qquad
 Y_4(2)=\log2.
\]

Using `log2>2/3`, `log4>4/3`, and `sqrt2<3/2`,

\[
\boxed{
 \Delta_X
 \ge Y_4(2)s_X(2)
 >\frac{8}{27(\sqrt K+130)}>0.
}
\tag{R-19883.10}

On every retained activation cell the construction is continuous, so the positive defect occurs on a set of positive logarithmic measure. Hence `nu_a` in (R-19883.3) is nonzero.

Equations (R-19883.7) and (R-19883.10) contradict one another.

## 5. Verdict and repair

Therefore

\[
\boxed{
 \text{PSSI as a positive additive/parallel Stieltjes identity is false.}
}
\tag{R-19883.11}

The native defect may still enter a passive realization as an unobserved environment, a Schur complement, or a linear-fractional/Redheffer transfer. It cannot be added as a positive Stieltjes branch to the critical Xi admittance.

This refutation is independent of whether Route A is ultimately accepted: the assumed PSSI itself first implies RH and therefore supplies the pure-point measure used in the contradiction.

## 6. Boundary

```text
native deficit -> diffuse Stieltjes measure          exact / L-19884
PSSI -> RH -> pure-point Xi Stieltjes measure         exact on L-92100
positive parallel sum -> measure subordination       exact
nonzero diffuse branch under factor-67 reserve       exact
PSSI positive parallel identity                      rejected
transfer/Schur passive realization                   possible replacement / open
```
