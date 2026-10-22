# L-26207 — Finite parity-frame synthesis of the factor-five dyadic transition source

Claim ID: `L-26207`  
Status: `PROPOSED COMPLETE — exact finite source and block map pending independent review`  
Scope: bridge from `L-26206` to PR #269's `omega_2` factor-five programme  
Date: 2026-08-08  
Depends on: `L-26206`; PR #269 `L-26901/L-26902`

Put

\[
z=2^{-s},
\qquad
\mathcal O(s)=\prod_{p\ {\rm odd}}(1-p^{-s}),
\]

and retain

\[
B_+(s)=p(z)\mathcal O(s),
\qquad
B_-(s)=p(-z)\mathcal O(s),
\tag{L-26207.1}
\]

where

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2.
\]

The opposite-parity source of PR #269 is

\[
\boxed{
\Omega_2(s)
=q(z)\mathcal O(s),
\qquad
q(z)=(1-z)^2(1-z/2).
}
\tag{L-26207.2}
\]

It is the Dirichlet series of

\[
\omega_2(n)
=\mu(n)-\frac32\mathbf1_{2\mid n}\mu(n/2)
 +\frac12\mathbf1_{4\mid n}\mu(n/4).
\]

## 1. Exact finite synthesis

Let `U` be the positive Bézout polynomial of `L-26206`, so

\[
U(z)p(z)+U(-z)p(-z)=1.
\]

Multiplying by `q(z)mathcal O(s)` gives

\[
\boxed{
\Omega_2(s)
=V_+(z)B_+(s)+V_-(z)B_-(s),
}
\tag{L-26207.3}
\]

where

\[
V_+(z)=q(z)U(z),
\qquad
V_-(z)=q(z)U(-z).
\tag{L-26207.4}
\]

Both synthesis filters have degree six. Explicitly,

\[
\boxed{
\begin{aligned}
V_+(z)={}&\frac12
+\left(-\frac{59}{12}+\frac{7\sqrt2}{2}\right)z\\
&+\left(\frac{67}{6}-\frac{103\sqrt2}{12}\right)z^2
+\left(-\frac{65}{12}+\frac{43\sqrt2}{12}\right)z^3\\
&+\left(-\frac{47}{6}+\frac{73\sqrt2}{12}\right)z^4
+\left(\frac{53}{6}-\frac{73\sqrt2}{12}\right)z^5\\
&+\left(-\frac73+\frac{3\sqrt2}{2}\right)z^6.
\end{aligned}}
\tag{L-26207.5}
\]

The coefficients of `V_-` are obtained by replacing the coefficient of `z^j` in `U` by `(-1)^j` before multiplying by `q`; they are retained exactly by (L-26207.4).

No inverse or infinite filter occurs.

## 2. Physical finite-delay map

Let a fixed real compact window `H` be used in all channels. Define

\[
Q_\pm(t)
=\sum_n\frac{b_\pm(n)}{\sqrt n}H(t-\log n),
\qquad
Q_\omega(t)
=\sum_n\frac{\omega_2(n)}{\sqrt n}H(t-\log n).
\]

After the usual centered normalization of the local variable, (L-26207.3) becomes an exact finite translation formula

\[
\boxed{
Q_\omega
=\sum_{j=0}^6v_j^+\tau_{j\log2}Q_+
 +\sum_{j=0}^6v_j^-\tau_{j\log2}Q_-,
}
\tag{L-26207.6}
\]

with explicit coefficients obtained from `V_+-` after inserting the critical factor `2^{-j/2}`. Every delay is at most `6 log 2`.

Consequently, for every unit or dyadic block `I_m`,

\[
\boxed{
\int_{I_m}|Q_\omega|^2
\le C_V
\sum_{r=0}^6
\int_{I_{m-r}^{+}}
\left(|Q_+|^2+|Q_-|^2\right),
}
\tag{L-26207.7}
\]

where `I_(m-r)^+` denotes the finitely enlarged neighboring block required by the fixed window support, and `C_V` is the explicit squared `ell1` synthesis norm. Thus subexponential paired energy implies subexponential `omega_2` energy without any analytic inversion.

## 3. Connection to the factor-five theorem

PR #269 proves for `omega_2`:

1. an exact pointwise carry wavelet;
2. localization of every negative logarithmic Kummer row to
   \[
   2m\le n<5m;
   \]
3. an absolute carry-feature Schur reserve on that transition sector.

Equation (L-26207.6) supplies the missing exact source-level bridge **into** that factor-five source from the parity-paired reflected frame. It does not yet identify the physical two-frequency transition Gram with the carry-feature Gram.

A combined production certificate may therefore work on only one fixed finite source family:

```text
parity-paired reflected block
 -> degree-six finite synthesis
 -> omega_2 factor-five transition source
 -> carry Schur reserve
 -> lower-scale shell recurrence.
```

The only remaining nonformal arrow is the source-specific physical-normal-to-carry transference on the transition cells `2,3,4`.

## 4. Mutation preservation

The map preserves the mandatory firewalls:

- the `omega_2` numerator has no zero in the open critical strip;
- every odd Möbius coefficient remains present;
- the same-sign odd Möbius cube is represented in both parity analysis channels;
- the `2/3` shell remains accessible through the all-ratio causal transfer;
- every synthesis delay is declared and finite.

## 5. Proof boundary

Closed exactly:

- finite synthesis of `omega_2` from the parity pair;
- the degree-six source map;
- the finite neighboring-block energy implication;
- compatibility with PR #269's factor-five source.

Not closed:

- physical-normal-to-carry transference;
- a transition LMI on the actual reflected matrices;
- the factor-five recurrence;
- RH.
