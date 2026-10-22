# R-26802 — The positive-inverse primitive is not the RH-sensitive prime normal signal

Claim ID: `R-26802`  
Title: The `a_omega log` specialization of the annular split frame cancels every reciprocal-zeta pole and cannot close RH by itself  
Status: **EXACT SCOPE CORRECTION / FORMER SOURCE IDENTIFICATION WITHDRAWN**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: `L-26802`, `L-26804`; PR #269 `L-26903`; elementary Laplace and Dirichlet-convolution algebra  
Scope: corrects the source used in the physical/carry annular map; does not refute the annular isometry

## 1. The exact annular geometry survives

For any finite coefficient sequence `x=(x_m)`, the compact window

\[
 h_\omega(t)
 =e^{-t/2}
 \left[
 \mathbf1_{[0,\log2)}(t)
 -\frac12\mathbf1_{[\log2,\log4)}(t)
 \right]
\]

and the atomic source

\[
 \alpha_x=\sum_m\frac{x_m}{\sqrt m}\delta_{\log m}
\]

produce the exact integer potential and weighted carry-split identities of
`L-26802`. The polynomial-filtered identities of `L-26804` are also valid for
every `x`.

The error corrected here concerns only which coefficient sequence is the
RH-sensitive physical source.

## 2. The compact window is the counting primitive of `omega_2`

Let

\[
 C(t)=e^{-t/2}\lfloor e^t\rfloor\mathbf1_{t\ge0}.
\]

Its Laplace transform is

\[
 \widehat C(z)
 =\frac{\zeta(z+1/2)}{z+1/2}.
\]

Since

\[
 \mathbf1*\omega_2
 =\varepsilon-\frac32\delta_2+\frac12\delta_4,
\]

a direct coefficient calculation gives

\[
 \boxed{
 h_\omega=C*\alpha_{\omega_2}.
 }
\tag{R-26802.1}
\]

Thus

\[
 \widehat h_\omega(z)
 =rac{(1-2^{-s})(1-2^{-s-1})}{s},
 \qquad s=z+\frac12.
\tag{R-26802.2}
\]

The compact wavelet is an elementary Euler numerator divided by `s`; it does
not itself contain `1/zeta`.

## 3. Why `x_m=a_omega(m) log m` is pole blind

Let

\[
 A_\omega(s)
 =\sum_{m\ge1}\frac{a_\omega(m)}{m^s}
 =\frac{\zeta(s)}{E(s)},
 \qquad
 E(s)=(1-2^{-s})(1-2^{-s-1}).
\]

For

\[
 x_m=a_\omega(m)\log m,
\]

the physical signal has Laplace transform

\[
 -\widehat h_\omega(z)A_\omega'(s)
 =-rac{E(s)}s\left(\frac{\zeta(s)}{E(s)}\right)'.
\]

Expanding gives

\[
 \boxed{
 \widehat Q_{a\log}(z)
 =\frac{-\zeta'(s)+\zeta(s)E'(s)/E(s)}s.
 }
\tag{R-26802.3}
\]

At every zero of `zeta`, both terms are holomorphic: `zeta'` is entire and the
second term vanishes. Therefore this physical primitive has no reciprocal-zeta
pole at a hypothetical off-line zero.

Equivalently, using Dirichlet convolution,

\[
 h_\omega*\alpha_{a_\omega\log}
 =C*\alpha_{\omega_2*a_\omega\log}
 =C*\alpha_{\Lambda_\omega}.
\tag{R-26802.4}
\]

This is a generalized-prime counting primitive. It is useful algebraically, but
it is not an RH detector.

## 4. The RH-sensitive physical specialization

The correct physical coefficient sequence is

\[
 \boxed{x_m=\Lambda_\omega(m).}
\tag{R-26802.5}
\]

Then

\[
 \widehat Q_\Lambda(z)
 =\widehat h_\omega(z)
 \left[-\frac{A_\omega'}{A_\omega}(s)\right].
\tag{R-26802.6}
\]

Because

\[
 -\frac{A_\omega'}{A_\omega}(s)
 =-rac{\zeta'}{\zeta}(s)+\frac{E'}E(s),
\]

every hypothetical off-line zeta zero remains a pole. The elementary window
multiplier has no matching zero there.

Its exact carry image is

\[
 \boxed{
 W_n(j)
 :=\sum_m\Lambda_\omega(m)Z_{n,m}(j)
 =\sum_q(\omega_2*\Lambda_\omega)(q)\chi_{n,q}(j).
 }
\tag{R-26802.7}
\]

This is the RH-sensitive annular carry feature.

## 5. Relation to the carry profile already controlled on PR #269

PR #269 establishes a strict carry reserve for

\[
 P_n(j)
 =\sum_q\Lambda_\omega(q)\chi_{n,q}(j)
 =\sum_m a_\omega(m)\log m\,Z_{n,m}(j).
\tag{R-26802.8}
\]

The two features are not equal. They satisfy the exact source-change identity

\[
 \boxed{
 a_\omega*(\omega_2*\Lambda_\omega)
 =\Lambda_\omega,
 }
\tag{R-26802.9}
\]

or schematically

\[
 a_\omega*W=P.
\]

The convolution kernel `a_omega` is positive but infinite and not a strict
contraction. Therefore the reserve for `P` does not automatically transfer to
`W`.

This source-change is the actual remaining arithmetic theorem in the annular
physical/carry programme.

## 6. Corrected status

The following claims survive:

```text
annular physical/carry isometry for arbitrary x     EXACT
critical polynomial-filtered isometry                EXACT
positive proper-divisor Selberg defect               EXACT
carry reserve for P=lambda_omega                     PROPOSED COMPLETE
```

The following former statement is withdrawn:

```text
x=a_omega log is the RH-sensitive physical prime source.
```

The corrected proof frontier is:

```text
RH-sensitive physical source x=lambda_omega
-> exact annular carry feature W=omega_2*lambda_omega
-> source-change / direct reserve for W
-> strict annular recurrence
-> RH.
```

## 7. Review firewall

Reject any completion that:

- uses (R-26802.3) as though it contained `1/zeta` poles;
- silently replaces `W` by `P`;
- treats positivity of `a_omega` as invertibility with a bounded positive inverse;
- quotes the PR #269 Schur reserve without proving its transfer to the
  RH-sensitive feature;
- loses the exact reciprocal-zeta pole in the source map.

RH remains unproved.
