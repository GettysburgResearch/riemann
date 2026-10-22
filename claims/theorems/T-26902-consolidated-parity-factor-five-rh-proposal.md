# T-26902 — Consolidated parity-paired factor-five proposal for RH

Claim ID: `T-26902`  
Title: A complete source-bound physical transition certificate for the parity-paired factor-five block implies the Riemann Hypothesis  
Status: **CONSOLIDATED FULL CONDITIONAL PROPOSAL — ONE EXPLICIT PHYSICAL TRANSFERENCE THEOREM OPEN**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Scope: sole review front door for the corrected reflected/carry route; RH is not claimed proved

## 1. Frozen dependency packet

Review this proposal against the following immutable inputs:

```text
PR #241  3a227e7595e1fe9e38956048297aa97531c80e4e
  corrected independent-frequency physical block L-9518

PR #263  73e24368b62f32f31e10691ebbaf3764b544f2a3
  parity-paired critical Euler fiber, sharp closed-strip reserve,
  positive finite Bezout reconstruction, finite map to omega_2,
  complete odd-core half-pole-null fibers

PR #268  b67f3ee4e5c20fdd23ad0923641d452c4a89da83
  compact omega_2 source, positive inverse/digital/Selberg faces,
  exact bottom-two carry charge and one-sign RH consumer

PR #236  a0d5a627bd2d4e799eddf7c795df77083a3618ff
  all-ratio shell transfer, positive p-adic combs,
  exact dyadic Green block, digital Sobolev tail

PR #229  2fc74c11b9929f694d8c13d060c9d55b99dc9621
  exact first-cell Mertens decoder and fixed-ratio RH equivalence

PR #158  b4896de93983231d0efbf5ffb7899c7703bbe5ef
  exact fixed-logarithm Mobius core and higher Euler closure boundary
```

The source/carry continuation on this PR is reviewed at its final frozen head after this packet is complete.

No rejected one-frequency, bounded-rank, bounded-contact, generic Hankel, or monotone-cover theorem is a dependency.

## 2. Correct physical block

Let \(H\) be a fixed real compact safe window and let

\[
Q(x)=\sum_n\frac{c(n)}{\sqrt n}H(x-\log n).
\]

A physical unit block is

\[
\mathcal B_{J,H}(c)=\int_J^{J+1}|Q(x)|^2dx.
\]

PR #241 proves the exact independent-frequency representation

\[
\boxed{
\mathcal B_{J,H}(c)
=\frac1{(2\pi)^2}
\iint F_\alpha(t)\overline{F_\alpha(s)}
\Phi_{J,\alpha}(t-s)\,dt\,ds,
}
\tag{T-26902.1}
\]

and the equivalent arithmetic normal Gram

\[
\boxed{
\mathcal B_{J,H}(c)
=\sum_{m,n}\frac{c(m)c(n)}{\sqrt{mn}}
K_J^H(\log m,\log n).
}
\tag{T-26902.2}
\]

Independent frequencies and every translate cross term are mandatory.

## 3. Fixed RH-bearing source

Use

\[
\boxed{
\omega_2(n)
=\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
+\frac12\mathbf1_{4\mid n}\mu(n/4).
}
\tag{T-26902.3}
\]

Its Dirichlet series is

\[
\Omega_2(s)
=\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)}.
\tag{T-26902.4}
\]

The two finite Euler factors have no zero in the open critical strip. Hence a subexponential compact-window block bound for this source excludes every zeta zero with real part greater than \(1/2\).

The source has the positive inverse

\[
a_\omega(n)=2v_2(n)+2^{-v_2(n)}>0
\tag{T-26902.5}
\]

and nonnegative generalized von Mangoldt sequence

\[
\Lambda_\omega(q)
=\Lambda(q)+(\log2)(1+2^{-r})\mathbf1_{q=2^r}\ge0.
\tag{T-26902.6}
\]

## 4. Exact source trace into the physical normal Gram

The fixed-\(q_0=2\) Mobius source first gives

\[
b_2(n)=\mu(n)-\mathbf1_{2\mid n}\mu(n/2).
\]

In physical coordinates,

\[
Q_{b_2}(x)
=Q_\mu(x)-2^{-1/2}Q_\mu(x-\log2).
\]

Thus its complete local matrix is

\[
\boxed{
\begin{pmatrix}
1&-2^{-1/2}\\
-2^{-1/2}&1/2
\end{pmatrix}
\succeq0,
}
\tag{T-26902.7}
\]

with all four channels

```text
(m,n), (2m,n), (m,2n), (2m,2n).
```

The extra factor \(I-\tfrac12\tau_{\log2}\) produces \(\omega_2\). The source filter has a stable causal inverse, so the \(b_2\), \(\omega_2\), dyadic-shell, and fixed-ratio first-cell exponents agree.

## 5. Exact carry source

For the carry indicator

\[
\chi_{n,q}(j)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor,
\]

put

\[
Z_{n,m}(j)
=\sum_{k\le n/m}\omega_2(k)\chi_{n,mk}(j).
\]

`L-26901` proves the pointwise formula

\[
\boxed{
Z_{n,m}(j)
=g_m(n)-g_m(j)-g_m(n-j),
}
\tag{T-26902.8}
\]

where

\[
g_m(x)=\mathbf1_{m\le x<2m}
-\frac12\mathbf1_{2m\le x<4m}.
\]

This is an exact source identity before norms or packet estimates.

## 6. Exact factor-five localization

Let

\[
F_n(j)=\log\binom nj
\]

and

\[
\mathcal K(n,m)
=\frac1{n+1}\sum_{j=0}^nZ_{n,m}(j)F_n(j).
\]

The source is pointwise nonnegative for \(m\le n<2m\), pointwise nonpositive for \(2m\le n<4m\), and its far-field Kummer coupling is nonnegative from \(n=5m\) onward. Therefore

\[
\boxed{
(\mathcal K(n,m))_-\ne0
\Longrightarrow
2m\le n<5m.
}
\tag{T-26902.9}
\]

Every potentially negative logarithmic row is confined to quotient cells \(2,3,4\). There is no unbounded quotient tail.

## 7. Exact carry reserve

For every \(n\ge210\), every \(m\), and every scalar \(a\),

\[
\boxed{
\sum_{j=0}^n(F_n(j)-aZ_{n,m}(j))^2
\ge\frac1{60\,000\,000}
\sum_{j=0}^nF_n(j)^2.
}
\tag{T-26902.10}
\]

The proof uses a central interval where \(F_n\) rises by at least \(\log2\), while \(Z_{n,m}\) has at most six jumps. It is uniform through all transition cells.

The actual generalized-prime carry profile is the complete positive synthesis

\[
\boxed{
P_n
=\sum_{m\le n}a_\omega(m)\log m\,Z_{n,m},
}
\tag{T-26902.11}
\]

and differs from ordinary Kummer by a nonnegative digital correction whose relative row norm is \(O(\log n/n)\). Hence the strict reserve survives for the actual generalized-prime source after a finite threshold.

## 8. Parity-paired source frame

PR #263 supplies the critical local polynomial

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2
\]

and its parity mate \(p(-z)\). On the full closed counterexample annulus,

\[
\boxed{
|p(z)|^2+|p(-z)|^2\ge\frac{45}{4}.
}
\tag{T-26902.12}
\]

It also supplies a strictly positive-coefficient polynomial \(U\) satisfying

\[
\boxed{
U(z)p(z)+U(-z)p(-z)=1.
}
\tag{T-26902.13}
\]

Thus the original inverse-zeta source is reconstructed from two analysis channels using only four dyadic delays. The \(\omega_2\) source is itself a finite degree-six synthesis of this parity pair.

These are exact source-frame statements. They do not replace the physical transition theorem below.

## 9. Exact Selberg–carry moment tower

`L-26904` proves, pointwise in every carry row and split,

\[
\boxed{
\sum_m a_\omega(m)Z_{n,m}(j)=0,
}
\tag{T-26902.14}
\]

\[
\boxed{
\sum_m a_\omega(m)\log m\,Z_{n,m}(j)
=P_n(j)\ge0,
}
\tag{T-26902.15}
\]

and

\[
\boxed{
\sum_m a_\omega(m)(\log m)^2Z_{n,m}(j)
=S_n(j)\ge0,
}
\tag{T-26902.16}
\]

where \(S_n\) is the carry image of

\[
\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
\]

The unit source \(m=1\) is absent from the positive first and second moments because \(\log1=0\). Therefore the unweighted boundary coordinate must remain explicit in the physical certificate.

## 10. Bottom-charge consumer

Let \(c_X\) be the unique triangular inverse of

\[
w_X(q)=q^{-1/2}\log(X/q).
\]

The compact source has carry image only on rows \(2,3\):

\[
\sum_q\omega_2(q)\beta_{nq}
=
\begin{cases}
-5/6,&n=2,\\
-1/2,&n=3,\\
0,&n\ge4.
\end{cases}
\]

Hence

\[
\boxed{
5c_X(2)+3c_X(3)
=-6\mathcal R_\omega(X),
}
\tag{T-26902.17}
\]

where

\[
\mathcal R_\omega(X)
=\sum_{q=2}^{X}\frac{\omega_2(q)}{\sqrt q}\log(X/q).
\]

Either an eventual sign for (T-26902.17), a subpower bound for the dyadic signed slack, or a subexponential physical shell bound yields RH through the exact Mellin/Landau consumer.

## 11. Sole remaining theorem — `F5TC`

A **Factor-Five Transition Certificate** is the following explicit production object.

For every sufficiently large physical block, construct the duplicate-free source manifest and the independent-frequency transition matrices for all rows

\[
2m\le n<5m.
\]

The certificate must provide an exact linear source map

\[
\mathsf S_{J,\tau}:\mathcal H_{\rm phys}\to\mathcal H_{\rm car}
\]

and prove, on the licensed parity-paired source subspace,

\[
\boxed{
\mathsf S^*G^{\rm car}\mathsf S
\preceq C_{J,\tau}G^{\rm phys},
}
\tag{T-26902.18}
\]

plus a reverse retained-coordinate inequality

\[
\boxed{
G^{\rm phys}_{\rm source}
\preceq C'_{J,\tau}
\mathsf S^*G^{\rm car}_{\rm source}\mathsf S
+G^{\rm lower}_{J,\tau}.
}
\tag{T-26902.19}
\]

The map must preserve:

1. all parity and dyadic translate cross terms;
2. the \(m=1\) boundary coordinate;
3. the complete positive inverse synthesis;
4. the strict carry Schur reserve;
5. the finite \(n<210\) boundary table;
6. every cutoff, endpoint, and noncoprime row;
7. the fixed-ratio \(2/3\) Mertens mutation.

The condition numbers must fit one of the two accepted recurrence budgets below. A fixed power \(X^c\) is not acceptable.

## 12. Accepted closing recurrences

### Physical shell form

\[
\boxed{
E_\omega(J)
\le C(1+J)^A
+\theta\max_{u\le J-\delta}E_\omega(u),
\qquad0\le\theta<1.
}
\tag{T-26902.20}
\]

### Bottom-charge / DSS form

\[
\boxed{
|\Pi_2(X)|
\le C\log^A(2X)
+\sum_\beta\theta_\beta|\Pi_2(Y_\beta)|,
}
\tag{T-26902.21}
\]

with

\[
Y_\beta\le X^{1-\delta},
\qquad
\sum_\beta\theta_\beta\le1.
\]

Either recurrence gives a subexponential or subpower bound by scale induction.

## 13. Conditional deduction to RH

Assume `F5TC` and either (T-26902.20) or (T-26902.21).

The scale recurrence gives

\[
E_\omega(J)=e^{o(J)}
\]

or

\[
\mathcal R_\omega(X)=O_\varepsilon(X^\varepsilon).
\]

The Mellin transform contains

\[
\frac{(1-2^{-s})(1-2^{-s-1})}{\zeta(s)},
\]

whose numerator has no zero at a zeta zero in \(1/2<\Re s<1\). Therefore no nontrivial zeta zero lies to the right of the critical line. Functional-equation symmetry excludes zeros to its left.

Hence

\[
\boxed{\mathrm{F5TC}\Longrightarrow\mathrm{RH}.}
\tag{T-26902.22}
\]

## 14. What is and is not complete

Complete, subject to independent review:

```text
correct physical source localization
finite parity-paired reconstruction
pointwise omega_2 carry wavelet
factor-five localization of every negative Kummer row
positive inverse and generalized-prime source
uniform carry-space Schur reserve
zero/first/second Selberg-carry moment tower
bottom-charge and Mellin consumers
conditional scale induction to RH
```

Not complete:

```text
physical quotient-cell matrices for the final transition object
exact physical-to-carry map S
physical preservation of the carry reserve and m=1 boundary
consumer recurrence emitted by that map
```

Accordingly this is a full, sharply falsifiable proposal for adversarial review, not an unconditional proof of RH.
