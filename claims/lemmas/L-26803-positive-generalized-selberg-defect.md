# L-26803 — Positive proper-divisor defect in the generalized Selberg source

Claim ID: `L-26803`  
Title: The opposite-parity generalized Selberg forcing has an exact nonnegative strict-lower-scale defect  
Status: **PROPOSED COMPLETE EXACT LEMMA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro-source-specific`  
Created: 2026-08-08  
Dependencies: PR #268 `L-26202`; PR #269 `L-26903`; generalized Selberg coefficient identity  
Scope: coefficientwise reserve and lower-scale routing; no block contraction or RH conclusion

## 1. General setup

Let \(a\) be a Dirichlet series with \(a(1)=1\), and let \(\omega\) be its
Dirichlet inverse:

\[
 \omega*a=\varepsilon.
 \tag{L-26803.1}
\]

Define the generalized von Mangoldt sequence

\[
 \Lambda=\omega*(a\log).
 \tag{L-26803.2}
\]

The generalized Selberg identity is

\[
 \boxed{
 \omega*(a\log^2)
 =\Lambda\log+\Lambda*\Lambda.
 }
 \tag{L-26803.3}
\]

For the opposite-parity source of PR #268,

\[
 a=a_\omega>0,
 \qquad
 \Lambda=\Lambda_\omega\ge0
\]

coefficientwise.

Put

\[
 \mathcal F
 =\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
 \tag{L-26803.4}
\]

Every coefficient of \(\mathcal F\) is nonnegative.

## 2. Positive defect identity

Convolving (L-26803.3) by \(a_\omega\) gives

\[
 \boxed{
 a_\omega\log^2=a_\omega*\mathcal F.
 }
 \tag{L-26803.5}
\]

At an integer \(n\), the divisor \(d=n\) on the right contributes exactly
\(\mathcal F(n)\), because \(a_\omega(1)=1\). Therefore

\[
 \boxed{
 \mathcal D_\omega(n)
 :=
 a_\omega(n)\log^2n-\mathcal F(n)
 =
 \sum_{\substack{d\mid n\\d<n}}
 a_\omega(n/d)\mathcal F(d).
 }
 \tag{L-26803.6}
\]

Since both factors in every summand are nonnegative,

\[
 \boxed{
 \mathcal D_\omega(n)\ge0
 \qquad(n\ge1).
 }
 \tag{L-26803.7}
\]

Equivalently,

\[
 \boxed{
 \mathcal D_\omega
 =(\varepsilon-\omega_2)*(a_\omega\log^2).
 }
 \tag{L-26803.8}
\]

This is an exact source-specific reserve. It is not inferred from a positive
Hankel representation or from a generic operator inequality.

## 3. Every defect term is strictly lower scale

Every proper divisor \(d<n\) satisfies

\[
 d\le\frac n2.
\]

Thus (L-26803.6) routes the complete defect to strict half scale:

\[
 \boxed{
 \mathcal D_\omega(n)
 =
 \sum_{\substack{k\mid n\\k\ge2}}
 a_\omega(k)\mathcal F(n/k),
 \qquad
 n/k\le n/2.
 }
 \tag{L-26803.9}
\]

On a logarithmic block near \(J=\log n\), every term on the right lies at or
below

\[
 J-\log2.
\]

The defect therefore belongs in the lower-block ledger of a reflected
recurrence. It may not be charged as an undeclared same-scale error.

## 4. Exact positive synthesis in carry coordinates

For a carry row \(N\), let

\[
 P_N(j)
 =\sum_{q\le N}\Lambda_\omega(q)\chi_{N,q}(j)
\]

be the generalized-prime Kummer profile. PR #269 proves the positive wavelet
synthesis

\[
 P_N
 =\sum_m a_\omega(m)\log m\,Z_{N,m}.
 \tag{L-26803.10}
\]

The quadratic source \(\Lambda_\omega*\Lambda_\omega\) therefore retains all
cross terms between the annular wavelets. The defect (L-26803.9) is the
proper-divisor part left after the current coefficient \(\mathcal F(n)\) is
separated.

A production recurrence must perform this separation before taking absolute
values.

## 5. Consequence for the physical/carry programme

Together, `L-26802` and this lemma supply:

```text
current annular generalized-prime forcing
    -> exact weighted carry split Gram;

all proper-divisor Selberg defect
    -> explicit nonnegative half-scale ledger.
```

Thus the missing theorem is no longer an unspecified physical-to-carry map or
an unidentified Selberg remainder. It is the quantitative comparison between:

1. the current inverse-zeta source energy in the reflected equation;
2. the strict annular carry reserve;
3. the total declared lower-block charge from (L-26803.9) and the finite digital
   boundary.

That comparison is stated in `T-26802`.

## 6. Firewalls

The following inferences are invalid:

- \(\mathcal D_\omega\ge0\) does not imply \(\omega_2\ge0\);
- positive coefficients \(a_\omega,\Lambda_\omega\) do not imply
  Bottom-Charge Positivity;
- dropping \(\mathcal D_\omega\) from an equality changes the source equation;
- estimating the divisor sum before signed source recombination can restore the
  same balanced Möbius obstruction in unsigned form.

## 7. Proof boundary

Closed exactly:

1. the generalized Selberg identity;
2. the positive proper-divisor formula;
3. strict half-scale routing of every defect term;
4. compatibility with the positive wavelet synthesis.

Open:

1. the reflected annular reserve inequality;
2. summability of the complete lower-block charge relative to that reserve;
3. the inverse-zeta block recurrence;
4. RH.
