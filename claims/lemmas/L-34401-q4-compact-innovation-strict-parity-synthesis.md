# L-34401 — The compact Q=4 innovation has a strict parity-frame synthesis

Claim ID: `L-34401`  
Title: A finite Bézout cycle reconstructs the Q=4 compact innovation with critical current charge below two fifths of the parity-frame reserve, while the complete derivative gauge factors through a strictly delayed ordinary Möbius source  
Status: **PROPOSED COMPLETE EXACT FINITE-FILTER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-09  
Dependencies: PR #263 `L-26205/L-26206`; PR #334 `L-32408`; PR #342 `L-34003`; elementary polynomial algebra  
Scope: exact compact-source/current synthesis and gauge typing; no final delayed-state recurrence or RH conclusion

## 1. Common odd Euler core

Put

\[
z=2^{-s},
\qquad
\mathcal O(s)=\prod_{p\ {m odd}}(1-p^{-s}),
\]

and retain the parity analysis polynomial

\[
p(z)=(1-z)(1-2z)(1-\sqrt2 z)^2.
\]

The parity sources are

\[
B_+(s)=p(z)\mathcal O(s),
\qquad
B_-(s)=p(-z)\mathcal O(s).
\tag{L-34401.1}
\]

PR #263 proves on the closed critical annulus

\[
{1\over2}\le |z|\le{1\over\sqrt2}
\]

the uniform frame reserve

\[
\boxed{|p(z)|^2+|p(-z)|^2\ge {45\over4}.}
\tag{L-34401.2}
\]

The compact Q=4 innovation source of PR #342 is

\[
B_\circ(s)={1-4^{1-s}\over\zeta(s)}.
\]

Since `1/zeta=(1-z)O`,

\[
\boxed{
T(z)=(1-z)(1-4z^2),
\qquad
B_\circ(s)=T(z)\mathcal O(s).
}
\tag{L-34401.3}
\]

Thus the compact Q=4 innovation and the parity frame are finite polynomial sources over exactly the same odd Euler core.

## 2. Bézout cycle freedom

PR #263 supplies

\[
U(z)p(z)+U(-z)p(-z)=1,
\tag{L-34401.4}
\]

where

\[
\begin{aligned}
U(z)={}&{1\over2}
+\left(-{11\over3}+{7\sqrt2\over2}\right)z
+\left(1+{\sqrt2\over6}\right)z^2\\
&+\left({14\over3}-3\sqrt2\right)z^3.
\end{aligned}
\tag{L-34401.5}
\]

For any polynomial `H`, define

\[
\boxed{
\begin{aligned}
W_+(z)&=T(z)U(z)+H(z)p(-z),\\
W_-(z)&=T(z)U(-z)-H(z)p(z).
\end{aligned}}
\tag{L-34401.6}
\]

The cycle terms cancel identically:

\[
\boxed{W_+(z)p(z)+W_-(z)p(-z)=T(z).}
\tag{L-34401.7}
\]

No approximation or inverse filter occurs.

## 3. A simple exact certificate

Take

\[
\boxed{
H(z)={1\over1000}
\left(
123+296z-387z^2+117z^3-14z^4+62z^5+303z^6
\right).
}
\tag{L-34401.8}
\]

In particular,

\[
\boxed{H(1)={1\over2}.}
\tag{L-34401.9}
\]

Write

\[
W_\pm(z)=\sum_{j=0}^{10}w_{\pm,j}z^j.
\]

On the critical line, `z^j` is a delay by `j log 2` with squared amplitude `2^{-j}`. Define

\[
q_W=\sum_{j=0}^{10}
(w_{+,j}^2+w_{-,j}^2)2^{-j}.
\tag{L-34401.10}
\]

Exact arithmetic in `Q(sqrt(2))` gives

\[
\boxed{
q_W
={14014874005-9814156296\sqrt2\over32000000}
=4.2362833733\ldots .
}
\tag{L-34401.11}
\]

Moreover

\[
\boxed{q_W<{9\over2}.}
\tag{L-34401.12}
\]

Indeed

\[
{9\over2}-q_W
={-13870874005+9814156296\sqrt2\over32000000}>0,
\]

because

\[
2(9814156296)^2-(13870874005)^2
=234181942048139207>0.
\]

Comparing with (L-34401.2),

\[
\boxed{
{q_W\over45/4}<{2\over5}.
}
\tag{L-34401.13}
\]

Thus the **complete current-scale finite synthesis** of the compact innovation uses less than two fifths of the fixed parity-frame coefficient reserve.

No numerical optimization statement is used: (L-34401.8) is simply an explicit exact certificate.

## 4. Exact source reconstruction

Substituting `z=2^{-s}` in (L-34401.7),

\[
\boxed{
B_\circ(s)
=W_+(2^{-s})B_+(s)
+W_-(2^{-s})B_-(s).
}
\tag{L-34401.14}
\]

The synthesis has only the declared delays `0,log2,...,10log2`.

## 5. Differentiate the reconstruction

Let

\[
q_\circ=B_\circ',
\qquad q_\pm=B_\pm'.
\]

Since

\[
{d\over ds}W_\pm(2^{-s})
=-(\log2)zW_\pm'(z),
\]

differentiating (L-34401.14) gives

\[
\boxed{
\begin{aligned}
q_\circ={}&W_+(z)q_+ +W_-(z)q_-\\
&-(\log2)z
\left[W_+'(z)B_+ +W_-'(z)B_-\right].
\end{aligned}}
\tag{L-34401.15}
\]

The first line is the complete parity-current synthesis and has the strict charge (L-34401.13).

The second line is the exact derivative gauge. We now identify its source completely rather than leaving it as an arbitrary parity state.

## 6. The derivative gauge is only delayed ordinary Möbius source

Define

\[
G_H(z)
=z\left[W_+'(z)p(z)+W_-'(z)p(-z)\right].
\tag{L-34401.16}
\]

It has an explicit factor `z` by definition. Direct differentiation of (L-34401.6), followed by evaluation at `z=1`, gives for an arbitrary cycle polynomial `H`

\[
\boxed{G_H(1)=3-6H(1).}
\tag{L-34401.17}
\]

For the certificate (L-34401.8), equation (L-34401.9) therefore gives

\[
G_H(1)=0.
\]

Consequently there is one polynomial

\[
R_H(z)\in\mathbf Q(\sqrt2)[z],
\qquad \deg R_H\le11,
\]

such that

\[
\boxed{G_H(z)=z(z-1)R_H(z).}
\tag{L-34401.18}
\]

Since

\[
B_0(s)={1\over\zeta(s)}=(1-z)\mathcal O(s),
\]

the derivative gauge in (L-34401.15) becomes exactly

\[
\boxed{
-(\log2)G_H(z)\mathcal O(s)
=(\log2)zR_H(z)B_0(s).
}
\tag{L-34401.19}
\]

This has two important consequences:

1. every gauge term is delayed by at least one `log 2` block;
2. every gauge term is an **ordinary Möbius boundary source**, not a new parity/current species.

PR #334 `L-32408` already identifies the reconstructed ordinary Möbius boundary as the coefficient-one unweighted boundary channel. Thus the compact-innovation differentiation introduces no new source type.

Equation (L-34401.19) is a source identity only; this lemma does not spend the same reflected reserve twice on the current and delayed boundary channels.

## 7. Actual Q=4 current innovation

PR #342 proves

\[
(\varepsilon-\delta_4)q_4
=q_\circ-(\log4)\delta_4*b_4.
\tag{L-34401.20}
\]

In critically normalized physical coordinates, every `delta_4` term is delayed by `log 4`. Combining (L-34401.15), (L-34401.19), and (L-34401.20) gives the exact source classification

```text
current scale:
    finite parity-current synthesis,
    critical charge < 2/5 of the fixed parity-frame reserve;

strictly earlier blocks:
    finite ordinary-Mobius boundary gauge from (L-34401.19);
    explicit Q=4 bare-source gauge from (L-34401.20).
```

Hence the compact innovation has **no unsynthesized current-scale arithmetic source** and **no new derivative-gauge source species**.

## 8. Proof boundary

Closed exactly here:

1. finite source reconstruction of `B_circ` from the parity pair;
2. explicit rational cycle polynomial (L-34401.8);
3. exact critical synthesis charge and strict `<2/5` bound;
4. exact differentiated current identity;
5. Möbius factorization of the complete derivative gauge;
6. strict-delay classification of every gauge term;
7. composition with the live Q=4 current innovation.

Still open:

1. joint reflected accounting of the delayed Möbius boundary and the delayed Q=4 bare state without double spending;
2. composition with PR #341's terminal-state curvature theorem into one coefficient-one block recurrence;
3. RH.

A reviewer is asked to verify the finite identities and inequalities supplied above, not to construct the remaining recurrence.
