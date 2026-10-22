# R-32402 — The asymmetric linear reserve is an initial-scale source and vanishes on large physical blocks

Claim ID: `R-32402`  
Title: The surviving `Lambda log` term of asymmetric power reflection pairs with the unit-source window in the two-frequency localization and is identically zero on every sufficiently large compact physical block  
Status: **PROPOSED COMPLETE EXACT SCOPE REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32404`; PR #241 `L-9518`  
Scope: refutes the use of the asymmetric linear term as a cofinal local-block reserve; does not refute other nonlocal consumers of `L-32404`

## 1. The linear term in the two-frequency adapter

Let `H` be a real compactly supported physical window and use the notation of `L-9518`. Put

\[
 \sigma={1\over2}+\alpha
\]

and define the logarithmically weighted prime field

\[
\boxed{
 Q_{H,\log}(x)
 =\sum_{n\ge2}{\Lambda(n)\log n\over\sqrt n}
   H(x-\log n).
}
\tag{R-32402.1}
\]

Its exponentially weighted Fourier transform is

\[
 \widehat H(\alpha+it)
 \sum_{n\ge2}{\Lambda(n)\log n\over n^{\sigma+it}}.
\tag{R-32402.2}
\]

The second bare window factor

\[
 \widehat H(\alpha-is)
\]

is the conjugate Fourier transform of the fixed physical function `H(x)` itself.

## 2. Exact localization of one surviving leg

Consider the `Lambda_+ log` contribution in `L-32404.4` inserted into the exact `L-9518` block kernel:

\[
\begin{aligned}
 I_+(J)
 ={1\over(2\pi)^2}\iint
 &\widehat H(\alpha+it)
 \widehat H(\alpha-is)
 \Phi_{J,\alpha}(t-s)\\
 &\times
 \left[
 \sum_n{\Lambda(n)\log n\over n^{\sigma+it}}
 \right]dt\,ds.
\end{aligned}
\tag{R-32402.3}
\]

Apply the same double-Fourier calculation as `L-9518.9`, but with the first physical field equal to `Q_(H,log)` and the second equal to the bare window `H`. One obtains exactly

\[
\boxed{
 I_+(J)
 =\int_J^{J+1}Q_{H,\log}(x)H(x)\,dx.
}
\tag{R-32402.4}
\]

The reflected `Lambda_- log` leg gives the conjugate expression, and for real `H` the complete surviving linear term is

\[
\boxed{
 I_{\rm lin}(J)
 =2\int_J^{J+1}Q_{H,\log}(x)H(x)\,dx.
}
\tag{R-32402.5}
\]

No estimate is used: this is an exact source-typing identity.

## 3. Compact support kills the term cofinally

Let

\[
 \operatorname{supp}H\subset[A,B].
\]

If

\[
 J>B,
\]

then

\[
 H(x)=0
 \qquad(J\le x\le J+1).
\]

Therefore

\[
\boxed{
 I_{\rm lin}(J)=0
 \qquad(J>B).
}
\tag{R-32402.6}
\]

Thus the extra coefficient-level forcing retained by `L-32404` is a cross term between the arithmetic source and the **unit source at physical scale zero**. It is not a cofinal large-scale reserve.

On every sufficiently large localized block, `L-32404` reduces physically to the same Hermitian cross energy as the ordinary reflected identity.

## 4. Why the untwisted row reserve was misleading

At a single finite carry row, `L-32404` gives the strict defect

\[
 Q+{A\over M}>0.
\]

That statement is correct. But the linear `A` term has only one arithmetic leg. The physical normal block is a two-leg object. The missing second leg is the unit coefficient, whose translated window remains at the origin rather than following the output block.

Consequently the row reserve and the large-scale physical Gram have different source typing:

```text
untwisted finite row:        strict A/M reserve;
large physical normal block: unit-source leg disjoint -> zero.
```

This is exactly the source/geometry firewall emphasized by PR #241.

## 5. Disposition

Retain:

- the exact asymmetric coefficient identity of `L-32404`;
- its strict untwisted carry-row inequality.

Reject as a cofinal RH mechanism:

```text
asymmetric linear row reserve
  -> positive large-scale physical Schur reserve.
```

A successful reflected proof must retain **two arithmetic legs** in the term that pays the RH-bearing root mode, or use a genuinely nonlocal consumer in which the unit-source leg is not compactly separated.

## 6. Proof boundary

Proved exactly:

- (R-32402.4)--(R-32402.6);
- physical large-block disappearance of the surviving linear term.

Not refuted:

- a nonlocal/global weighted-energy use of `L-32404`;
- a higher-order polarization with two arithmetic legs in every reserve term;
- RH.
