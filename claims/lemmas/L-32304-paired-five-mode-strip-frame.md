# L-32304 — Paired five-mode strip frame and positive forcing

Claim ID: `L-32304`  
Title: The carry-localizing dyadic factors preserve the uniform parity frame while making the averaged carry image finite  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: PR #263 `L-26205`; `L-32303`  
Scope: closed-strip source frame and forcing; no physical-block upper estimate

## 1. Old parity frame and normalization

Retain

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2.
\]

PR #263 writes its source relative to the odd Euler product

\[
\mathcal O(s)=\prod_{p\text{ odd}}(1-p^{-s}),
\qquad z=2^{-s},
\]

as

\[
B_E^+(s)=p(z)\mathcal O(s),
\qquad
B_E^-(s)=p(-z)\mathcal O(s).
\tag{L-32304.1}
\]

Since

\[
{1\over\zeta(s)}=(1-z)\mathcal O(s),
\]

this corresponds, relative to `1/zeta`, to the critical Euler factor

\[
(1-2z)(1-\sqrt2z)^2.
\]

PR #263 proves on

\[
{1\over2}\le|z|\le{1\over\sqrt2}
\]

that

\[
\boxed{|p(z)|^2+|p(-z)|^2\ge{45\over4}.}
\tag{L-32304.2}
\]

## 2. Add both carry-localizing factors

The five-mode source `L-32303` is, relative to `1/zeta`,

\[
P_\Box(z)
=(1-z)(1-z/2)(1-2z)(1-\sqrt2z)^2.
\]

Therefore, relative to the odd Euler product, its plus-channel polynomial is

\[
\boxed{
q_+(z)=(1-z)(1-z/2)p(z),
}
\tag{L-32304.3}
\]

not merely `(1-z/2)p(z)`.  The parity twist sends `z` to `-z`, so

\[
\boxed{
q_-(z)=(1+z)(1+z/2)p(-z).
}
\tag{L-32304.4}
\]

These are exactly the two parity twists of the coefficient sequence in `L-32303`.

On the closed annulus,

\[
|1\mp z|\ge1-|z|\ge1-{1\over\sqrt2},
\]

and

\[
|1\mp z/2|\ge1-|z|/2\ge1-{1\over2\sqrt2}.
\]

Hence

\[
\boxed{
\begin{aligned}
|q_+(z)|^2+|q_-(z)|^2
\ge{}&{45\over4}
\left(1-{1\over\sqrt2}\right)^2\\
&\times
\left(1-{1\over2\sqrt2}\right)^2.
\end{aligned}
}
\tag{L-32304.5}
\]

Thus the two additional carry factors preserve one absolute closed-strip frame reserve.

## 3. Uniform equivalence with the inverse-zeta source

Define

\[
B_+(s)=q_+(z)\mathcal O(s),
\qquad
B_-(s)=q_-(z)\mathcal O(s).
\]

Since

\[
|1-z|\le1+1/\sqrt2,
\]

(L-32304.5) gives

\[
\boxed{
|B_+(s)|^2+|B_-(s)|^2
\ge
c_\Box\left|{1\over\zeta(s)}\right|^2,
}
\tag{L-32304.6}
\]

with the explicit constant

\[
\boxed{
 c_\Box
 ={45\over4}
 {\left(1-1/\sqrt2\right)^2
  \left(1-1/(2\sqrt2)\right)^2
  \over(1+1/\sqrt2)^2}>0.
}
\tag{L-32304.7}
\]

The reverse inequality also holds with one absolute constant because every local factor is bounded on the compact annulus and

\[
|1-z|\ge1-1/\sqrt2>0.
\]

Hence the paired five-mode source is uniformly equivalent to the unfiltered inverse-zeta source on the entire closed critical strip.

## 4. Positive summed Selberg forcing survives

Let `a_+` be the positive inverse of `B_+` and let

\[
\chi_2(n)=(-1)^{v_2(n)}.
\]

The parity twist obeys

\[
a_- =\chi_2a_+,
\qquad
\Lambda_- =\chi_2\Lambda_+,
\qquad
C_- =\chi_2 C_+.
\]

By `L-32303`,

\[
C_+(n)=
\Lambda_+(n)\log n+(\Lambda_+*\Lambda_+)(n)
\ge0.
\]

Therefore

\[
\boxed{
C_+(n)+C_-(n)
=(1+\chi_2(n))C_+(n)
\ge0.
}
\tag{L-32304.8}
\]

Adding the two independent-frequency reflected Selberg identities gives one coefficientwise nonnegative paired forcing exactly as in PR #263.

## 5. Stable relation to the old parity frame

Equations (L-32304.3)--(L-32304.4) give the finite forward maps

\[
B_+=(1-z)(1-z/2)B_E^+,
\qquad
B_-=(1+z)(1+z/2)B_E^-.
\tag{L-32304.9}
\]

Conversely, throughout the closed critical strip,

\[
{1\over(1-z)(1-z/2)}
=\sum_{r\ge0}\alpha_r z^r,
\qquad \alpha_r>0,
\]

and

\[
{1\over(1+z)(1+z/2)}
=\sum_{r\ge0}(-1)^r\alpha_r z^r.
\]

Because `|z|<=1/sqrt2`, both inverse filters are absolutely summable with one uniform geometric bound. Thus the new pair and the old PR #263 pair are related by bounded causal filters in both directions. Every old finite synthesis to the `omega_2` factor-five source remains available after this source change.

## 6. New gain over the old parity frame

The old parity frame annihilated the continuous pole and double half-pole Green models. The two extra factors supply the two long carry cancellations

\[
P_\Box(1)=0,
\qquad
P_\Box(2)=0.
\]

Consequently the averaged carry source is identically zero above row 31 by `L-32303`.

The following properties now coexist in one source:

```text
uniform inverse-zeta strip frame;
coefficientwise positive paired Selberg forcing;
positive inverse on the plus channel;
bounded causal equivalence to the old parity frame;
finite averaged carry bank n=2,...,31;
positive compact five-window Green potential.
```

## 7. Proof boundary

Closed exactly:

- correct odd-Euler normalization;
- explicit paired multiplier;
- uniform closed-strip frame lower bound;
- two-sided equivalence with `1/zeta`;
- positive summed Selberg forcing;
- bounded causal equivalence with PR #263's frame;
- compatibility with factor-32 carry localization.

Open:

- an upper estimate for the complete independent-frequency RH-sensitive carry/physical block in terms of the finite current bank plus strict-delay tails;
- a strict scale recurrence;
- RH.
