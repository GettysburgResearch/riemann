# L-34009 — Critical-Haar reflected product and individual blocks are an exact two-state ledger

Claim ID: `L-34009`  
Title: Root-of-unity averaging of the complete Q=4 critical-Haar reflected identity gives exactly the base Q=4 product/individual block plus one unit-delay copy with explicit current--bare corrections  
Status: **PROPOSED COMPLETE EXACT INDEPENDENT-FREQUENCY LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Dependencies: `L-34007`; PR #302 `L-28013`; PR #241 `L-9518`  
Scope: complete product/individual/current block algebra; no dissipative inequality or RH conclusion

## 1. Base reflected block

For the Q=4 source write

\[
 B=B_4,\qquad q=B',\qquad t=BC_4.
\]

On one physical Hilbert block `I`, define

\[
\boxed{
 \mathfrak P_B(I)
 =2\|\mathcal P_q\|_I^2
  +2\operatorname{Re}\langle\mathcal P_t,\mathcal P_B\rangle_I,
}
\tag{L-34009.1}
\]

and

\[
\boxed{
 \mathfrak I_B(I)
 =2\operatorname{Re}\langle\mathcal P_t,\mathcal P_B\rangle_I.
}
\tag{L-34009.2}
\]

Then the source-convolved reflected identity is simply

\[
\boxed{
 \mathfrak P_B(I)-\mathfrak I_B(I)
 =2\|\mathcal P_q\|_I^2.
}
\tag{L-34009.3}
\]

This is `L-28013/L-32710` in physical notation.

## 2. Critical-Haar detail state

Put

\[
 u=\sqrt2\,2^{-s},\qquad \ell=\log2,
\]

and let

\[
 B_\omega=(1-\omega u)B.
\]

The nonzero DFT modes of the source/current pair are

\[
 B_0=B,\qquad q_0=q,\qquad t_0=t,
\]

and, after removing the common unitary delay `u`,

\[
\boxed{
 \widetilde B=-B,
 \qquad
 \widetilde q=\ell B-q,
 \qquad
 \widetilde t=-t+2\ell q+\ell^2B.
}
\tag{L-34009.4}

Every higher second-current DFT mode is pure bare source and is killed exactly by the bare leg in the reflected individual term, by `L-34007`.

## 3. Product block of the detail state

The reflected product block attached to the detail state is

\[
 \mathfrak P_{\rm det}
 =2\|\widetilde q\|^2
  +2\operatorname{Re}\langle\widetilde t,\widetilde B\rangle.
\]

Substitution of (L-34009.4) gives

\[
\begin{aligned}
 \mathfrak P_{\rm det}
={}&2\|q\|^2
 +2\operatorname{Re}\langle t,B\rangle
 -8\ell\operatorname{Re}\langle q,B\rangle.
\end{aligned}
\]

Hence

\[
\boxed{
 \mathfrak P_{\rm det}(I)
 =\mathfrak P_B(I)
 -8(\log2)\operatorname{Re}
   \langle\mathcal P_q,\mathcal P_B\rangle_I.
}
\tag{L-34009.5}

All `ell^2 ||B||^2` terms cancel from the complete product block.

## 4. Individual block of the detail state

Likewise

\[
 \mathfrak I_{\rm det}
 =2\operatorname{Re}\langle\widetilde t,\widetilde B\rangle
\]

gives

\[
\boxed{
\begin{aligned}
 \mathfrak I_{\rm det}(I)
 ={}&\mathfrak I_B(I)
 -4(\log2)\operatorname{Re}
   \langle\mathcal P_q,\mathcal P_B\rangle_I\\
 &-2(\log2)^2\|\mathcal P_B\|_I^2.
\end{aligned}}
\tag{L-34009.6}

Subtracting (L-34009.6) from (L-34009.5) gives exactly

\[
\boxed{
 \mathfrak P_{\rm det}-\mathfrak I_{\rm det}
 =2\|\mathcal P_q-(\log2)\mathcal P_B\|^2.
}
\tag{L-34009.7}

Thus the detail reflected identity is itself an exact Hermitian square.

## 5. Channel average

Choose `M` beyond twice the active dyadic depth and use conjugate root-of-unity channels on the two independent-frequency legs. Parseval and `L-34007` imply that only modes zero and one survive.

Multiplication by `u` is one unit-amplitude translation by `log2` in the critical physical coordinate. Consequently

\[
\boxed{
 {1\over M}\sum_{\omega^M=1}
 \mathfrak P_{B_\omega}(I)
 =\mathfrak P_B(I)
  +\mathfrak P_{\rm det}(I-\log2),
}
\tag{L-34009.8}

\[
\boxed{
 {1\over M}\sum_{\omega^M=1}
 \mathfrak I_{B_\omega}(I)
 =\mathfrak I_B(I)
  +\mathfrak I_{\rm det}(I-\log2),
}
\tag{L-34009.9}

and therefore

\[
\boxed{
\begin{aligned}
 {1\over M}\sum_\omega
 2\|\mathcal P_{q_\omega}\|_I^2
={}&2\|\mathcal P_q\|_I^2\\
 &+2\|\mathcal P_q-(\log2)\mathcal P_B\|_{I-\log2}^2.
\end{aligned}}
\tag{L-34009.10}

This is the complete source-convolved independent-frequency identity, not only a current-side DFT calculation.

## 6. Consequence for the remaining proof problem

The adaptive root-of-unity bank can have arbitrarily many generalized-prime modes, but its complete reflected product and individual terms remain a fixed two-state system:

```text
state 0 at I:
    base Q4 product / individual block;

state 1 at I-log2:
    the same base block
    plus explicit current--bare and bare-square corrections.
```

Since the bare Q4 physical field is deterministic/polylogarithmic, all corrections in (L-34009.5)--(L-34009.6) are linear or quadratic in a closed forcing channel. There is no hidden channel-dependent product source left in RDP.

This exact reduction still does **not** put the separated generalized-prime reserve on the dissipative side of the ledger; that sign/orientation remains the RH-bearing step.

## 7. Proof boundary

Closed exactly, subject to review:

1. detail product block identity;
2. detail individual block identity;
3. exact Hermitian-square subtraction;
4. full root-of-unity channel average of product and individual terms;
5. fixed two-state reflected ledger independent of channel count.

Still open:

1. dissipative insertion of the separated generalized-prime reserve;
2. coefficient-one recurrence;
3. RH.
