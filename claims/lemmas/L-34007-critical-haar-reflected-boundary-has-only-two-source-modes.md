# L-34007 — Adaptive critical-Haar reflected boundary has only two source modes

Claim ID: `L-34007`  
Title: After root-of-unity separation of the Q=4 critical-Haar bank, the complete source-convolved reflected individual terms couple only the principal source mode and one unit-delay predecessor mode  
Status: **PROPOSED COMPLETE EXACT FINITE-ENDPOINT / DIRICHLET LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-09  
Dependencies: PR #325 `L-32424`; PR #302 `L-28013`; elementary logarithmic differentiation  
Scope: exact channel DFT and independent-frequency source-boundary reduction; no dissipative sign or RH conclusion

## 1. Critical-Haar Q=4 bank

Retain the Q=4 Euler--Blaschke inverse source

\[
 B(s)=B_4(s),\qquad q(s)=B'(s),\qquad
 t(s)=B(s)C_4(s),
\]

and put

\[
 u(s)=\sqrt2\,2^{-s},\qquad \ell=\log2.
\]

For an integer `M>=2` and an `M`th root of unity `omega`, define

\[
 h_\omega(s)=1-\omega u(s),\qquad
 B_\omega=h_\omega B.
\]

The separate Dirichlet system has inverse `A_omega=B_omega^{-1}`, logarithmic current

\[
 q_\omega=B_\omega',
\]

and source-convolved second current

\[
 t_\omega=B_\omega C_\omega,
\qquad
 C_\omega=L_\omega^2-L_\omega',
\qquad
 L_\omega=B_\omega'/B_\omega.
\]

At a finite arithmetic endpoint `N`, assume

\[
 M>2\lfloor\log_2N\rfloor.
\tag{L-34007.1}
\]

Then no active dyadic mode can wrap modulo `M`.

## 2. Bare source and first-current modes

Since `u'=-ell u`,

\[
 q_\omega
 =(1-\omega u)q+\ell\omega uB
 =q+\omega u(\ell B-q).
\tag{L-34007.2}
\]

Thus the normalized channel DFT has exactly

\[
 \widehat B_0=B,
 \qquad
 \widehat B_1=-uB,
 \qquad
 \widehat B_k=0\quad(k\ge2),
\tag{L-34007.3}
\]

and

\[
 \widehat q_0=q,
 \qquad
 \widehat q_1=u(\ell B-q),
 \qquad
 \widehat q_k=0\quad(k\ge2).
\tag{L-34007.4}
\]

This recovers the two-mode theorem of `L-32424`.

## 3. Exact second-current expansion

Put

\[
 x=\omega u.
\]

Because

\[
 L_\omega=L_4+\ell\frac{x}{1-x}
\]

and

\[
 \left(\ell\frac{x}{1-x}\right)'
 =-\ell^2\frac{x}{(1-x)^2},
\]

direct substitution into `C_omega=L_omega^2-L_omega'` gives

\[
\boxed{
 t_\omega
 =(1-x)t
 +2\ell xq
 +\ell^2B\frac{x(1+x)}{1-x}.
}
\tag{L-34007.5}
\]

The last factor has the formal expansion

\[
 \frac{x(1+x)}{1-x}=x+2x^2+2x^3+\cdots.
\]

At a fixed endpoint `N` only powers `u^k` with `2^k<=N` can enter the finite arithmetic block. Under (L-34007.1) there is therefore no DFT aliasing, and

\[
\boxed{
 \widehat t_0=t,
}
\tag{L-34007.6}
\]

\[
\boxed{
 \widehat t_1
 =u\bigl(-t+2\ell q+\ell^2B\bigr),
}
\tag{L-34007.7}
\]

while for every active `k>=2`,

\[
\boxed{
 \widehat t_k=2\ell^2u^kB.
}
\tag{L-34007.8}
\]

Thus higher source second-current modes exist, but they are pure bare-source modes.

## 4. Higher modes disappear from every reflected individual term

Use the conjugate channel on the second independent-frequency leg. Root-of-unity Parseval gives

\[
 \frac1M\sum_{\omega^M=1}
 t_{\omega,t}\,B_{\bar\omega,-v}
 =\sum_k \widehat t_{k,t}\widehat B_{k,-v}.
\tag{L-34007.9}
\]

But (L-34007.3) has support only in modes zero and one. Hence every `k>=2` term in (L-34007.8) disappears **exactly**, before any norm or estimate.

Substituting (L-34007.3), (L-34007.6), and (L-34007.7),

\[
\boxed{
\begin{aligned}
 {1\over M}\sum_\omega
 t_{\omega,t}B_{\bar\omega,-v}
 ={}&t_tB_{-v}\\
 &-u_tu_{-v}
   \bigl(-t_t+2\ell q_t+\ell^2B_t\bigr)B_{-v}.
\end{aligned}}
\tag{L-34007.10}
\]

The reflected conjugate individual term is the same identity with the two frequency legs interchanged.

Therefore the complete channel-averaged individual contribution is carried by exactly two source states:

```text
mode 0:
    current-scale (t,B) Q=4 source pair;

mode 1:
    one log(2)-delayed pair
    ( -t+2 log(2) q+log^2(2) B , -B ).
```

No higher adaptive channel survives the source-convolved boundary.

## 5. Current product also has only two modes

The same Parseval calculation using (L-34007.4) gives

\[
\boxed{
 {1\over M}\sum_\omega
 q_{\omega,t}q_{\bar\omega,-v}
 =q_tq_{-v}
 +u_tu_{-v}
  (\ell B_t-q_t)(\ell B_{-v}-q_{-v}).
}
\tag{L-34007.11}
\]

After the atomized critical physical localization, multiplication by `u` is a translation by exactly `log 2` with unit amplitude. Thus the averaged Hermitian current block is exactly

```text
current Q=4 pole-current block
+
one unit-amplitude predecessor block of
    (log(2) * bare Q=4 field - Q=4 pole current).
```

The bare Q=4 field is deterministic/polylogarithmic after the common zeta carry factor.

## 6. Channelized reflected identity

Apply the general source-convolved reflected identity `L-28013` to the pair of systems `(A_omega,t,A_baromega,-v)` and average over `omega`. Equations (L-34007.10)--(L-34007.11) show that, after exact finite-endpoint Fourier/carry localization, the entire adaptive bank reduces to a **two-state reflected ledger**.

The arbitrarily many nonnegative generalized-prime Fourier channels of `L-32424` are needed only to diagonalize the Selberg forcing. They do not create additional inverse-source current or individual-boundary states.

Hence endpoint-adaptive forcing separation and the coefficient-one principal recurrence are compatible at fixed state dimension.

## 7. What this closes

The following possible obstruction is eliminated:

> increasing the root-of-unity channel count to separate every active local Selberg level might create an equally large source-convolved boundary state.

It does not. The exact boundary dimension is two, independently of `M`.

This strengthens `L-32423/L-32424` from a current-only statement to the **complete reflected individual-term source ledger**.

## 8. Proof boundary

Closed exactly, subject to review:

1. complete formula (L-34007.5) for the separate-system source second current;
2. its finite-endpoint DFT through every active mode;
3. exact annihilation of every mode `k>=2` in the source-convolved reflected individual terms;
4. exact two-mode current product;
5. reduction of the adaptive independent-frequency reflected boundary to one current-scale state plus one unit-delay predecessor state.

Still open:

1. the sign/no-double-spend inequality placing the separated Selberg reserve dissipatively in this two-state ledger;
2. the resulting coefficient-one block recurrence;
3. RH.
