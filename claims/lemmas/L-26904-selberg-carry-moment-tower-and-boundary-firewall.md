# L-26904 — Exact Selberg–carry moment tower and the surviving boundary coordinate

Claim ID: `L-26904`  
Title: The complete opposite-parity source has zero carry mass, nonnegative first and second logarithmic moments, and an unavoidable unweighted boundary mode  
Status: **PROPOSED COMPLETE EXACT ALGEBRA PENDING INDEPENDENT REVIEW**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-26901`, `L-26903`; the generalized Selberg coefficient identity  
Scope: exact source/carry algebra and proof-boundary identification; no physical transference estimate or RH conclusion

## 1. Source and inverse

Retain the opposite-parity source

\[
\omega_2(n)
=\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
+\frac12\mathbf1_{4\mid n}\mu(n/4)
\tag{L-26904.1}
\]

and its positive inverse

\[
a_\omega(n)=2v_2(n)+2^{-v_2(n)}>0.
\tag{L-26904.2}
\]

They satisfy

\[
\boxed{\omega_2*a_\omega=\varepsilon.}
\tag{L-26904.3}
\]

Define the generalized von Mangoldt sequence

\[
\boxed{
\Lambda_\omega
=\omega_2*(a_\omega\log),
}
\tag{L-26904.4}
\]

and the second Selberg coefficient sequence

\[
\boxed{
C_\omega
=\omega_2*(a_\omega\log^2)
=\Lambda_\omega\log+\Lambda_\omega*\Lambda_\omega.
}
\tag{L-26904.5}
\]

`L-26903` gives explicitly

\[
\Lambda_\omega(q)
=\Lambda(q)+(\log2)(1+2^{-r})\mathbf1_{q=2^r}\ge0.
\tag{L-26904.6}
\]

Consequently

\[
\boxed{C_\omega(q)\ge0\qquad(q\ge1).}
\tag{L-26904.7}
\]

## 2. Scaled carry wavelets

For integers

\[
n\ge1,\qquad 0\le j\le n,\qquad m\ge1,
\]

put

\[
\chi_{n,q}(j)
=\left\lfloor\frac nq\right\rfloor
-\left\lfloor\frac jq\right\rfloor
-\left\lfloor\frac{n-j}{q}\right\rfloor
\in\{0,1\},
\tag{L-26904.8}
\]

with \(\chi_{n,1}(j)=0\), and define

\[
\boxed{
Z_{n,m}(j)
=\sum_{k\le n/m}\omega_2(k)\chi_{n,mk}(j).
}
\tag{L-26904.9}
\]

`L-26901` identifies this pointwise as

\[
Z_{n,m}(j)=g_m(n)-g_m(j)-g_m(n-j),
\tag{L-26904.10}
\]

where

\[
g_m(x)=\mathbf1_{m\le x<2m}
-\frac12\mathbf1_{2m\le x<4m}.
\]

## 3. General logarithmic-moment identity

For an integer \(r\ge0\), define

\[
M_r(n,j)
=\sum_{m\le n}a_\omega(m)(\log m)^r Z_{n,m}(j).
\tag{L-26904.11}
\]

All sums are finite. Substituting (L-26904.9), writing \(q=mk\), and interchanging the finite sums gives

\[
\begin{aligned}
M_r(n,j)
&=\sum_{m,k:\,mk\le n}
 a_\omega(m)(\log m)^r\omega_2(k)\chi_{n,mk}(j)\\
&=\sum_{q\le n}
 [\omega_2*(a_\omega\log^r)](q)\chi_{n,q}(j).
\end{aligned}
\]

Hence

\[
\boxed{
M_r(n,j)
=\sum_{q\le n}
 [\omega_2*(a_\omega\log^r)](q)\chi_{n,q}(j).
}
\tag{L-26904.12}
\]

This identity retains every source sibling and every carry cross channel before any estimate.

## 4. The exact zero/first/second moment tower

### Zeroth moment

Using (L-26904.3),

\[
M_0(n,j)
=\sum_{q\le n}\varepsilon(q)\chi_{n,q}(j)
=\chi_{n,1}(j)=0.
\]

Thus

\[
\boxed{
\sum_{m\le n}a_\omega(m)Z_{n,m}(j)=0.
}
\tag{L-26904.13}
\]

The positive inverse weights therefore synthesize the complete source wavelets as a literal zero-mass carry measure.

### First logarithmic moment

Using (L-26904.4),

\[
\boxed{
M_1(n,j)
=\sum_{q\le n}\Lambda_\omega(q)\chi_{n,q}(j)
=:P_n(j)\ge0.
}
\tag{L-26904.14}
\]

This is the actual generalized-prime carry profile of `L-26903`.

### Second logarithmic moment

Using (L-26904.5),

\[
\boxed{
M_2(n,j)
=\sum_{q\le n}C_\omega(q)\chi_{n,q}(j)
=:S_n(j)\ge0.
}
\tag{L-26904.15}
\]

Equivalently,

\[
\boxed{
S_n(j)
=\sum_{m\le n}a_\omega(m)(\log m)^2Z_{n,m}(j).
}
\tag{L-26904.16}
\]

The second logarithmic moment is not postulated positive: it is the carry image of the exact generalized Selberg forcing.

## 5. Averaged Hermitian forms

Let

\[
\langle f,g\rangle_n
=\frac1{n+1}\sum_{j=0}^nf(j)\overline{g(j)}.
\tag{L-26904.17}
\]

Averaging (L-26904.13)--(L-26904.16) gives

\[
\sum_{m\le n}a_\omega(m)\langle Z_{n,m},1\rangle_n=0,
\tag{L-26904.18}
\]

\[
\sum_{m\le n}a_\omega(m)\log m\,\langle Z_{n,m},1\rangle_n
=\langle P_n,1\rangle_n\ge0,
\tag{L-26904.19}
\]

and

\[
\sum_{m\le n}a_\omega(m)(\log m)^2\langle Z_{n,m},1\rangle_n
=\langle S_n,1\rangle_n\ge0.
\tag{L-26904.20}
\]

More generally, every pointwise identity may be paired with any nonnegative test on the carry position \(j\).

These formulas are compatible with, but stronger in source bookkeeping than, a rowwise use of the individual-wavelet Schur reserve: they retain the complete positive inverse synthesis and the second Selberg moment simultaneously.

## 6. Exact boundary firewall

The logarithmic factors vanish at the unit coordinate:

\[
\log1=(\log1)^2=0.
\tag{L-26904.21}
\]

Therefore the base source wavelet \(Z_{n,1}\) contributes to the zeroth identity (L-26904.13), but is absent from both positive moment identities (L-26904.14) and (L-26904.15).

This is load bearing. The compact RH-bearing source has the averaged carry image

\[
\sum_{q=2}^{n}\omega_2(q)\beta_{nq}
=
\begin{cases}
-5/6,&n=2,\\
-1/2,&n=3,\\
0,&n\ge4,
\end{cases}
\tag{L-26904.22}
\]

and hence the bottom-charge consumer

\[
5c_X(2)+3c_X(3)=-6\mathcal R_\omega(X).
\tag{L-26904.23}
\]

Equations (L-26904.14)--(L-26904.16) do not by themselves control this unweighted \(m=1\) boundary coordinate. A proof which quotes generalized-prime positivity or the carry Schur reserve while omitting the unit-source boundary has not proved Bottom-Charge Positivity, DSS, or a physical shell estimate.

The missing physical transition theorem must therefore export one of the following explicitly:

1. a boundary/collar term carrying \(Z_{n,1}\) into the final recurrence;
2. a source reconstruction in which the unit coordinate is retained through all two-frequency cross terms;
3. a direct lower-scale telescope for the bottom charge.

## 7. Consequence for the factor-five programme

The source-side transition data are now closed at four compatible levels:

```text
pointwise wavelet                    L-26901
uniform carry Schur reserve          L-26902
positive inverse / prime synthesis   L-26903
zero/first/second moment tower       L-26904
```

The remaining `F5TC` theorem is not another coefficient identity. It is precisely the physical source-image theorem which must preserve the unweighted boundary coordinate while transferring the first/second-moment reserve to the independent-frequency normal block.

## 8. Review mutations

A checker or symbolic proof should reject at least the following mutations:

```text
replace chi_(n,1)=0 by an artificial unit carry;
drop the r=0 identity;
remove the m=1 source from the source manifest;
claim that M1>=0 or M2>=0 signs the bottom charge;
replace C_omega by Lambda_omega log alone;
drop the Lambda_omega*Lambda_omega term;
take absolute values before the m,k recombination;
use only diagonal Z_(n,m) energies and omit synthesis cross terms.
```

## 9. Proof boundary

Closed exactly:

- the general logarithmic-moment identity;
- zero total carry mass under the positive inverse synthesis;
- nonnegative first generalized-prime moment;
- nonnegative second Selberg moment;
- the exact exclusion of the unit-source boundary from the positive moments;
- the resulting review firewall.

Open:

- the independent-frequency physical-to-carry transference;
- a boundary-preserving physical Schur reserve;
- a DSS, bottom-charge, or shell-energy recurrence;
- RH.
