# L-32407 — The Q=4 physical field is controlled by its balanced Selberg reserve

Claim ID: `L-32407`  
Title: The source-convolved `Q=4` atomized physical current has an explicit sparse coefficient law and is pointwise bounded by an absolute multiple of the complete balanced Selberg–Kummer reserve  
Status: **PROPOSED COMPLETE SOURCE-BOUND TRANSFERENCE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: `L-32404`, `L-32405`; exact interval replay `X-32402`  
Scope: fixed balanced carry rows; no independent-frequency reflected recurrence or RH conclusion

## 1. Physical source coefficient

Let

\[
 e_4(1)=1,
 \qquad
 e_4(4^r)=-3\quad(r\ge1),
\]

with all other local coefficients zero. This is the source comb of `L-32404`.

Define

\[
 \boxed{c_4=e_4*\Lambda_4.}
 \tag{L-32407.1}
\]

At an integer carry row the source-convolved physical field is exactly

\[
 \boxed{
 Q_4(n,j)=\sum_{q\le n}c_4(q)\chi_{n,q}(j).
 }
 \tag{L-32407.2}
\]

This is the finite specialization of the pole-preserving current `E_4 L_4`.

## 2. Exact coefficient collapse

Write `ell=log 2`. Direct convolution of (L-32404.8) with `e_4` gives the complete support.

For every odd prime `p` and every `a>=1`,

\[
 \boxed{c_4(p^a)=\log p,}
 \tag{L-32407.3}
\]

\[
 \boxed{c_4(4^r p^a)=-3\log p\qquad(r\ge1),}
 \tag{L-32407.4}
\]

and

\[
 \boxed{c_4(2\cdot4^r p^a)=0\qquad(r\ge0).}
 \tag{L-32407.5}
\]

No integer containing two distinct odd prime factors occurs.

On the pure dyadic tower,

\[
 \boxed{
 c_4(2^{2r})=(3r+4)\ell\qquad(r\ge1),
 }
 \tag{L-32407.6}
\]

and

\[
 \boxed{
 c_4(2^{2r+1})=(1-3r)\ell\qquad(r\ge0).
 }
 \tag{L-32407.7}
\]

For (L-32407.6), use

\[
 \Lambda_4(2^{2r})=(2\cdot4^r-1)\ell
\]

and subtract the previous `4`-dilates. The geometric sum reduces exactly to `3r+4`. For odd dyadic exponent, every generalized-prime coefficient is simply `ell`, and the `r` previous `4`-dilates give `1-3r`.

Thus the huge positive generalized-prime spike at `4^r` has disappeared from the physical current. The current has only a linear dyadic coefficient and one fixed `-3` copy of each odd prime-power source at every `4`-adic dilation.

## 3. Absolute coefficient mass is linear

Let

\[
 M_4(x)=\sum_{q\le x}|c_4(q)|.
\]

The odd-prime-power part satisfies, by the elementary Chebyshev bound of `L-32405`,

\[
\begin{aligned}
 M_{\rm odd}(x)
 &\le\psi(x)
  +3\sum_{r\ge1}\psi(x/4^r)\\
 &\le2x\ell
   +6x\ell\sum_{r\ge1}4^{-r}\\
 &=4x\ell\\
 &<\frac{20}{7}x.
\end{aligned}
 \tag{L-32407.8}
\]

For the pure dyadic tower let

\[
 K=\lfloor\log_2x\rfloor.
\]

Equations (L-32407.6)--(L-32407.7) imply the crude bound

\[
 \sum_{2^k\le x}|c_4(2^k)|
 \le\ell\left(\frac34K^2+\frac{19}{4}K\right).
 \tag{L-32407.9}
\]

Using `ell<5/7`, the right side is at most

\[
 \frac{15K^2+95K}{28}.
\]

For `K>=6` this is at most `2^K` (check `K=6`; the difference then increases by elementary induction). Therefore, for every `x>=64`,

\[
 \sum_{2^k\le x}|c_4(2^k)|\le x.
 \tag{L-32407.10}
\]

Combining (L-32407.8)--(L-32407.10),

\[
 \boxed{
 M_4(x)<\frac{27}{7}x<4x
 \qquad(x\ge64).
 }
 \tag{L-32407.11}
\]

## 4. Large balanced rows

For every row,

\[
 |Q_4(n,j)|
 \le\sum_{q\le n}|c_4(q)|\chi_{n,q}(j)
 \le M_4(n).
\]

Hence for `n>=4735`,

\[
 \boxed{|Q_4(n,j)|<4n.}
 \tag{L-32407.12}
\]

On the balanced cone, `L-32405` gives

\[
 \mathcal R_4(n,j)
 >\frac1{20}P_4(n,j)^2
 \ge\frac{n^2(\log2)^2}{320}.
 \tag{L-32407.13}
\]

Therefore

\[
 \frac{|Q_4(n,j)|^2}{\mathcal R_4(n,j)}
 <\frac{5120}{(\log2)^2}.
\]

Using `log2>69/100`,

\[
 \frac{5120}{(\log2)^2}
 <\frac{51200000}{4761}
 <11000.
\]

Thus

\[
 \boxed{
 |Q_4(n,j)|^2<11000\,\mathcal R_4(n,j)
 }
 \tag{L-32407.14}
\]

for every balanced row with `n>=4735`.

## 5. Exact finite range is much stronger

The extended `X-32402` exact interval replay constructs `c_4=e_4*Lambda_4` with directed fixed-point intervals and verifies, simultaneously with the reserve theorem,

\[
 \boxed{
 |Q_4(n,j)|^2<4\,\mathcal R_4(n,j)
 }
 \tag{L-32407.15}
\]

for all

\[
 4\le n\le4734,
 \qquad
 \lceil n/4\rceil\le j\le\lfloor n/2\rfloor.
\]

The worst finite row is

\[
 \boxed{(n,j)=(6,2),}
\]

where the rigorous interval ratio is still strictly below four. The exact upper interval stored by the replay is

```text
7333535891689720380539921101689744150614259864289
----------------------------------------------------------------
2013296516059285484657555115280091244531092056049
```

which is approximately `3.64255132475`.

By symmetry the same statement holds on the other half of the balanced cone.

Combining finite and infinite ranges yields the all-row source-bound estimate

\[
 \boxed{
 |Q_4(n,j)|^2
 <11000\,\mathcal R_4(n,j)
 \quad
 (n\ge4,\ n/4\le j\le3n/4).
 }
 \tag{L-32407.16}
\]

## 6. Consequence

This closes the fixed-row physical-to-transverse estimate for the main-pole-killing Euler–Blaschke source:

```text
Q=4 physical current
    -> exact sparse source coefficient c_4
    -> complete source-matched Selberg reserve R_4
    -> absolute pointwise domination on every balanced row.
```

No inverse singular value, generic frame theorem, source-amplitude rescaling, or generalized-prime pointwise guess is used.

The remaining RH-bearing work is now specifically the independent-frequency reflected assembly: prove that the same reserve is available with the correct sign and without double spending after all source cross terms are retained, and route the unitary scattering state of `L-32406` as the sole coefficient-one principal return.

## 7. Proof boundary

Closed here:

1. exact physical source coefficients;
2. linear absolute coefficient mass;
3. large-row pointwise transference;
4. rigorous finite transference;
5. one all-`n` balanced physical-to-reserve theorem.

Open:

1. the complete independent-frequency source congruence;
2. the reflected block recurrence with the scattering state retained;
3. RH.
