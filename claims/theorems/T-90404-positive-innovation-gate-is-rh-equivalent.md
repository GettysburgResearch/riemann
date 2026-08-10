# T-90404 — The positive innovation gate is an RH-equivalent filtered Chebyshev mean square

Claim ID: `T-90404`  
Title: RH gives a pointwise `O(log^4 n)` bound for the normalized Q4 compact innovation, hence PIG; combined with `T-90302`, PIG is exactly RH-equivalent within the corrected Q4 assembly  
Status: **PROPOSED COMPLETE CONDITIONAL EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-10  
Dependencies: PR #345 `L-34401`; `T-90302`; the classical von Koch consequence `RH => psi(x)=x+O(sqrt(x) log^2(2x))`  
Scope: exact Q4 compact innovation and the block energy of `T-90302`; no proof of PIG or RH

## 1. The compact innovation

Retain the Q4 source notation of `L-34401`:

\[
B_4(s)=\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)},
\qquad b_4\leftrightarrow B_4,
\]

\[
b_\circ=(\varepsilon-\delta_4)*b_4,
\qquad q_\circ=-b_\circ\log,
\]

and, with `ell_4=log 4`,

\[
\boxed{i_\circ=q_\circ-\ell_4\,\delta_4*b_4.}
\tag{T-90404.1}
\]

For an aligned balanced row `n=j+k`, the actual compact innovation is

\[
\boxed{
I_\circ(n,j)=\mathcal L_{4n,4j}(i_\circ).
}
\tag{T-90404.2}
\]

The own-current prefix is exactly

\[
G_\circ(X)=\psi(X)-4\psi(\lfloor X/4\rfloor)
+4\ell_4\mathbf1_{X\ge4},
\tag{T-90404.3}
\]

where

\[
\psi(X)=\sum_{m\le X}\Lambda(m).
\]

## 2. Exact filtered Chebyshev formula on aligned rows

For positive integers `n,j,k` with `n=j+k`, equation (T-90404.3) gives

\[
\begin{aligned}
\mathcal L_{4n,4j}(q_\circ)
={}&G_\circ(4n)-G_\circ(4j)-G_\circ(4k)\\
={}&\psi(4n)-\psi(4j)-\psi(4k)\\
&-4\bigl(\psi(n)-\psi(j)-\psi(k)\bigr)-4\ell_4.
\end{aligned}
\tag{T-90404.4}
\]

Put

\[
E(x)=\psi(x)-x.
\]

The linear main terms cancel because `n=j+k`, so

\[
\boxed{
\begin{aligned}
\mathcal L_{4n,4j}(q_\circ)
={}&E(4n)-E(4j)-E(4k)\\
&-4\bigl(E(n)-E(j)-E(k)\bigr)-4\ell_4.
\end{aligned}}
\tag{T-90404.5]

(The closing bracket in the tag is typographical only.)

Thus the hard innovation is a compact radix-four finite difference of the ordinary Chebyshev error, not a generalized-prime tower.

## 3. The delayed bare gauge is only logarithmic

The divisor-prefix source of `b_4` is explicit. Indeed

\[
\zeta(s)B_4(s)
=\frac{1-4\,4^{-s}}{1-4^{-s}}
=1-3\sum_{r\ge1}4^{-rs}.
\]

Therefore

\[
\boxed{
\mathbf1*b_4
=\varepsilon-3\sum_{r\ge1}\delta_{4^r}.
}
\tag{T-90404.6]

Let `H_4(X)` be its ordinary prefix. Then

\[
H_4(X)=1-3\#\{r\ge1:4^r\le X\}
\]

for `X>=1`, and hence

\[
|H_4(X)|\le 1+3\log_4(2X).
\tag{T-90404.7}
\]

The prefix/carry identity gives

\[
|\mathcal L_{n,j}(b_4)|
\le |H_4(n)|+|H_4(j)|+|H_4(k)|
\ll\log(2n).
\tag{T-90404.8}
\]

Scaling all divisor and row variables by four gives exactly

\[
\mathcal L_{4n,4j}(\delta_4*b_4)
=\mathcal L_{n,j}(b_4).
\tag{T-90404.9}
\]

Consequently the second term of (T-90404.1) contributes only `O(log n)` to `I_circ`.

## 4. RH gives pointwise PIG

Assume RH. The classical von Koch estimate is

\[
\boxed{
E(x)=O\!\left(\sqrt x\,\log^2(2x)\right).
}
\tag{T-90404.10}
\]

Apply (T-90404.10) to the six terms in (T-90404.5). Uniformly for every split `n=j+k` with `j,k>=1`,

\[
\begin{aligned}
|\mathcal L_{4n,4j}(q_\circ)|
&\ll
(\sqrt n+\sqrt j+\sqrt k)\log^2(2n)+1\\
&\ll \sqrt n\log^2(2n).
\end{aligned}
\tag{T-90404.11}
\]

Together with (T-90404.8)--(T-90404.9), this proves

\[
\boxed{
|I_\circ(n,j)|
\ll \sqrt n\log^2(2n)
}
\tag{T-90404.12}
\]

and therefore the pointwise normalized innovation bound

\[
\boxed{
\frac{|I_\circ(n,j)|^2}{n}
\ll\log^4(2n).
}
\tag{T-90404.13}
\]

This is stronger than the averaged Positive Innovation Gate.

## 5. RH implies the block PIG of `T-90302`

On a logarithmic block `e^J<=n<e^(J+1)`, let `dnu_J` be the positive carry/physical measure of `T-90302`, normalized to total mass `O(1)`. Its innovation forcing is

\[
\mathcal I(J)
=\int\frac{|I_\circ(n,j)|^2}{n}\,d\nu_J(n,j).
\]

Equation (T-90404.13) gives

\[
\boxed{
\mathcal I(J)\ll(1+J)^4.
}
\tag{T-90404.14}
\]

Hence

\[
\boxed{\mathrm{RH}\Longrightarrow\mathrm{PIG}.}
\tag{T-90404.15}
\]

No property of the unknown carry-position measure beyond positivity and bounded total mass is used in this direction.

## 6. PIG is not a residual technicality

`T-90302` proves, subject to its declared exact Q4 block assembly and pole-energy consumer,

\[
\boxed{\mathrm{PIG}\Longrightarrow\mathrm{RH}.}
\tag{T-90404.16}
\]

Combining (T-90404.15) and (T-90404.16), within that corrected source/state framework,

\[
\boxed{\mathrm{PIG}\Longleftrightarrow\mathrm{RH}.}
\tag{T-90404.17}
\]

Thus the latest QIDR reduction is logically clean but has reached an RH-equivalent positive-mass theorem. The inertia work genuinely removed the formerly overstrong local matrix-PSD demand; it did not make the surviving positive innovation estimate sub-RH.

This distinction is load bearing:

```text
closed and sub-RH:
    source typing, all-pass orientation, collars,
    negative spectral mass, internal-state cancellation;

open and RH-equivalent:
    polynomial positive innovation energy.
```

## 7. Consequence for the next attack

A successful continuation cannot consist merely of another deterministic estimate of the Q4 reserve or another inertia bound. It must introduce information capable of proving the filtered Chebyshev mean square (T-90404.14). Viable mechanisms must therefore be tested directly against the spectral multiplier implicit in (T-90404.5), for example:

1. a new positive source identity that upper-bounds the product block containing `|I_circ|^2` without assuming its conclusion;
2. a configuration-sensitive finite-compression certificate beyond bandwidth-one first/two-trace data;
3. a genuinely new prime-correlation estimate;
4. an exact cancellation that changes the positive innovation observable itself while preserving pole visibility.

Any proposal surviving only because it renames (T-90404.14) has not advanced RH.

## 8. Proof boundary

Closed exactly, subject to review:

1. the aligned compact Chebyshev error formula (T-90404.5);
2. the explicit divisor-prefix source (T-90404.6);
3. logarithmic delayed-gauge bound;
4. `RH => |I_circ|^2/n << log^4 n` pointwise;
5. `RH => PIG`.

Imported conditionally from `T-90302`:

1. `PIG => RH` after the declared block assembly and pole consumer.

Open:

1. an unconditional proof of PIG;
2. RH.
