# L-34008 — Critical-Haar source curvature splits into current and predecessor Q=4 states

Claim ID: `L-34008`  
Title: The complete inverse-source imaginary Jordan curvature of the adaptive critical-Haar bank is exactly one current-scale Q=4 source curvature plus one unit-delay copy and a positive deterministic bare-source square  
Status: **PROPOSED COMPLETE EXACT HILBERT/DFT LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Dependencies: `L-34007`; PR #325 `L-32424`; PR #337 imaginary-Jordan orientation  
Scope: source-curvature state reduction; generalized-prime reserve is inserted separately; no global dissipation or RH conclusion

## 1. Source curvature

Retain

\[
 B=B_4,\qquad q=B',\qquad t=B C_4,
\]

and for any physical Hilbert block define the Q=4 inverse-source imaginary curvature

\[
\boxed{
 \mathfrak C_B
 =\|\mathcal P_q\|^2
  -\operatorname{Re}\langle\mathcal P_B,\mathcal P_t\rangle.
}
\tag{L-34008.1}
\]

This is the source half of the augmented Hermitian curvature of PR #337.

For the critical-Haar channels

\[
 B_\omega=(1-\omega u)B,
 \qquad
 u=\sqrt2\,2^{-s},
 \qquad \ell=\log2,
\]

write the analogous curvature as `C_(B_omega)`.

As in `L-34007`, use conjugate root-of-unity channels on the two independent-frequency legs and choose the channel count larger than twice the active dyadic depth, so no finite-endpoint aliasing occurs.

## 2. Mode-zero curvature

The zero DFT modes are

\[
 \widehat B_0=B,
 \qquad
 \widehat q_0=q,
 \qquad
 \widehat t_0=t.
\]

Hence their contribution is exactly

\[
\boxed{\mathfrak C_0=\mathfrak C_B.}
\tag{L-34008.2}
\]

## 3. Mode-one curvature

`L-34007` gives

\[
 \widehat B_1=-uB,
\]

\[
 \widehat q_1=u(\ell B-q),
\]

and

\[
 \widehat t_1=u(-t+2\ell q+\ell^2B).
\]

Multiplication by `u` is unitary translation by `log 2` in the critically normalized physical coordinate. Dropping the common unitary delay while computing one predecessor block, the mode-one source curvature is therefore

\[
\begin{aligned}
 \mathfrak C_1
 ={}&\|\ell B-q\|^2\\
 &-\operatorname{Re}
 \langle -B,-t+2\ell q+\ell^2B\rangle.
\end{aligned}
\tag{L-34008.3}
\]

Expanding the two lines, the mixed `B,q` terms cancel exactly:

\[
\begin{aligned}
 \mathfrak C_1
 ={}&\|q\|^2
 -\operatorname{Re}\langle B,t\rangle
 +2\ell^2\|B\|^2.
\end{aligned}
\]

Thus

\[
\boxed{
 \mathfrak C_1
 =\mathfrak C_B+2(\log2)^2\|\mathcal P_B\|^2.
}
\tag{L-34008.4}
\]

The second term is nonnegative and deterministic/polylogarithmic for Q=4 after the common atomized carry factor cancels zeta against `B_4`.

## 4. No higher source-curvature modes

Although `t_omega` has pure-bare DFT modes `k>=2`, the bare source `B_omega` itself has only modes zero and one. Therefore root-of-unity Parseval in the bilinear term

\[
 \operatorname{Re}\langle B_\omega,t_\omega\rangle
\]

kills every higher mode exactly. The current has only modes zero and one as well.

Consequently

\[
\boxed{
 {1\over M}\sum_{\omega^M=1}
 \mathfrak C_{B_\omega}(I)
 =\mathfrak C_B(I)
  +\mathfrak C_B(I-\log2)
  +2(\log2)^2\|\mathcal P_B\|_{I-\log2}^2,
}
\tag{L-34008.5}
\]

up to the explicit fixed finite endpoint collar when a block is cut rather than aligned. The identity is exact on aligned blocks and in the finite arithmetic Gram after the predecessor-row adapter.

## 5. Add the generalized-prime reserve

Let `R_Haar(I)` denote the channel-averaged generalized-prime imaginary curvature of `L-32424`. At a finite endpoint with separated active modes it is

\[
 \mathcal R_{\rm Haar}
 =\mathcal R_4
  +\sum_{2^r\le n}(\log2)^2 2^r\chi_{n,2^r}(j)
 \ge\mathcal R_4.
\tag{L-34008.6}
\]

Therefore the complete channel-averaged augmented curvature has the exact two-state form

\[
\boxed{
\begin{aligned}
 \mathfrak A_{\rm Haar}(I)
 ={}&\mathcal R_{\rm Haar}(I)
   +\mathfrak C_B(I)
   +\mathfrak C_B(I-\log2)\\
 &+2(\log2)^2\|\mathcal P_B\|_{I-\log2}^2,
\end{aligned}}
\tag{L-34008.7}
\]

with the understood exact row/carry realization at finite endpoints.

Thus the adaptive channel count diagonalizes arbitrarily many Selberg forcing levels **without increasing the dynamic source-curvature state dimension**.

## 6. Significance for RDP

The remaining reflected dissipative placement theorem can now be formulated on a fixed two-state storage space:

```text
current source curvature C_B(I)
+
one unit-delay predecessor C_B(I-log2)
+positive separated Selberg reserve
+deterministic bare square.
```

There is no hidden tower of channel-dependent source curvatures to propagate. Any successful coefficient-one recurrence only has to orient this two-state ledger; increasing `M` is harmless.

This does not itself orient the positive reserve dissipatively and therefore does not prove RH.

## 7. Proof boundary

Closed exactly, subject to review:

1. mode-zero source curvature;
2. exact mode-one source-curvature identity;
3. cancellation of the two mixed `B,q` terms;
4. elimination of every higher source-curvature mode;
5. exact two-state adaptive curvature decomposition (L-34008.7).

Still open:

1. reflected dissipative orientation/no-double-spend for `R_Haar`;
2. the coefficient-one block recurrence;
3. RH.
