# R-32401 — The extra zeta-power row reserve cancels in standard reflected polarization

Claim ID: `R-32401`  
Title: Uniformly powering the reflected zeta factors does not strengthen the normalized Hermitian cross identity, because the additional linear Selberg reserve cancels exactly  
Status: **PROPOSED COMPLETE EXACT SCOPE REFUTATION — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-32402`; PR #241 reflected independent-frequency identity  
Scope: refutes one proposed use of the power reserve; does not refute asymmetric or nonstandard polarizations

## 1. Generalized reflected sources

Let

\[
 A_+(s)=\zeta(s+it),
 \qquad
 A_-(s)=\zeta(s-iu)
\]

and write their generalized von Mangoldt sequences as

\[
 \Lambda_+,
 \qquad
 \Lambda_-.
\]

For the product

\[
 A_\times=A_+A_-,
\]

one has

\[
 \Lambda_\times=\Lambda_++\Lambda_-.
\]

The ordinary generalized Selberg subtraction therefore gives

\[
\boxed{
 \mathcal C_\times-\mathcal C_+-\mathcal C_-
 =2\Lambda_+*\Lambda_-.
}
\tag{R-32401.1}
\]

## 2. Power every factor by the same integer `M`

For an integer `M>=1`, put

\[
 A_{+,M}=A_+^M,
 \qquad
 A_{-,M}=A_-^M,
 \qquad
 A_{\times,M}=(A_+A_-)^M.
\]

Then

\[
 \Lambda_{+,M}=M\Lambda_+,
 \qquad
 \Lambda_{-,M}=M\Lambda_-,
 \qquad
 \Lambda_{\times,M}=M(\Lambda_++\Lambda_-).
\]

Consequently

\[
\begin{aligned}
 \mathcal C_{\times,M}
 &=M(\Lambda_++\Lambda_-)\log
   +M^2(\Lambda_++\Lambda_-)*(\Lambda_++\Lambda_-),\\
 \mathcal C_{+,M}
 &=M\Lambda_+\log+M^2\Lambda_+*\Lambda_+,\\
 \mathcal C_{-,M}
 &=M\Lambda_-\log+M^2\Lambda_-*\Lambda_-.
\end{aligned}
\]

Subtracting gives

\[
\boxed{
 \mathcal C_{\times,M}
 -\mathcal C_{+,M}
 -\mathcal C_{-,M}
 =2M^2\Lambda_+*\Lambda_-.
}
\tag{R-32401.2}
\]

After the natural normalization by `M^2`,

\[
\boxed{
 {1\over M^2}
 (\mathcal C_{\times,M}-\mathcal C_{+,M}-\mathcal C_{-,M})
 =2\Lambda_+*\Lambda_-.
}
\tag{R-32401.3}
\]

This is exactly the `M=1` reflected identity.

## 3. Where the strict row reserve went

`L-32402` proves on one carry row

\[
 F_M^2-S_M=M^2Q+M(M-1)A,
\]

with the new strict term

\[
 M(M-1)A.
\]

But that term belongs to the **linear** generalized Selberg forcing

\[
 M\Lambda\log.
\]

In the product identity the linear forcing is additive:

\[
 M(\Lambda_++\Lambda_-)\log
 =M\Lambda_+\log+M\Lambda_-\log.
\]

It therefore cancels identically in (R-32401.2). The Hermitian cross term scales only by the trivial factor `M^2`.

Hence the following proposed inference is false:

```text
strict endpoint reserve for zeta^M rows
    =>
strictly stronger standard reflected Hermitian identity.
```

The standard product-minus-two-individuals polarization has exactly the same normalized cross identity for every `M`.

## 4. Surviving possibility

This refutation is deliberately narrow. It does **not** exclude an asymmetric polarization using different powers or additional quotient/product identities. Such a construction would have to display explicitly:

1. the surviving linear term;
2. its sign after the independent-frequency physical localization;
3. every self-square coefficient;
4. the exact source manifest;
5. why no off-line pole is canceled.

Until such an identity is produced, `L-32402` is a strict row theorem rather than a completed reflected proof.

## 5. Proof boundary

Proved exactly:

- (R-32401.2)--(R-32401.3);
- cancellation of the additional linear power reserve in standard reflection.

Not refuted:

- asymmetric power polarization;
- a different physical consumer of the strict row reserve;
- RH.
