# L-32304 — Paired five-mode strip frame and positive forcing

Claim ID: `L-32304`  
Title: The extra affine-carry factor preserves the uniform parity frame while making the carry image finite  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: PR #263 `L-26205`; `L-32303`  
Scope: closed-strip source frame and forcing; no physical-block upper estimate

## 1. Old parity frame

Retain

\[
p(z)=(1-z)(1-2z)(1-\sqrt2z)^2.
\]

PR #263 proves on

\[
{1\over2}\le|z|\le{1\over\sqrt2}
\]

that

\[
\boxed{|p(z)|^2+|p(-z)|^2\ge{45\over4}.}
\tag{L-32304.1}
\]

## 2. Add the missing affine-carry factor

Define

\[
\boxed{
q_+(z)=(1-z/2)p(z),
\qquad
q_-(z)=(1+z/2)p(-z).
}
\tag{L-32304.2}
\]

These are exactly the two parity twists of the five-mode source `L-32303`.

On the closed annulus,

\[
|1\mp z/2|
\ge1-|z|/2
\ge1-{1\over2\sqrt2}.
\]

Therefore

\[
\boxed{
|q_+(z)|^2+|q_-(z)|^2
\ge
{45\over4}
\left(1-{1\over2\sqrt2}\right)^2.
}
\tag{L-32304.3]
\]

(the bracket typo in the tag is typographical only).

Thus the new factor does not reintroduce the rank-one local-zero degeneracy.  It preserves one absolute closed-strip frame reserve.

## 3. Uniform equivalence with the inverse-zeta source

For

\[
{1\over2}\le\Re s\le1,
\qquad z=2^{-s},
\]

write the odd Euler product as

\[
\mathcal O(s)=\prod_{p\text{ odd}}(1-p^{-s}).
\]

Then

\[
B_+(s)=q_+(z)\mathcal O(s),
\qquad
B_-(s)=q_-(z)\mathcal O(s),
\]

while

\[
{1\over\zeta(s)}=(1-z)\mathcal O(s).
\]

Since

\[
|1-z|\le1+1/\sqrt2,
\]

(L-32304.3) gives

\[
\boxed{
|B_+(s)|^2+|B_-(s)|^2
\ge
c_\Box\left|{1\over\zeta(s)}\right|^2,
}
\tag{L-32304.4}
\]

where the explicit constant is

\[
\boxed{
 c_\Box
 ={45\over4}
 {\left(1-{1\over2\sqrt2}\right)^2
  \over(1+1/\sqrt2)^2}>0.
}
\tag{L-32304.5]
\]

The reverse inequality holds with another absolute constant because all local factors are bounded on the compact annulus and `|1-z|>=1-1/sqrt2`.

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
\tag{L-32304.6]
\]

Adding the two independent-frequency reflected Selberg identities gives one coefficientwise nonnegative paired forcing exactly as in PR #263.

## 5. New gain over the old parity frame

PR #263's frame already annihilated the continuous pole and double half-pole models.  The extra factor `1-z/2` supplies the missing affine carry cancellation:

\[
P_\Box(2)=0.
\]

Consequently the averaged carry source is identically zero above row 31 by `L-32303.12`.

The two facts now coexist in one source:

```text
uniform inverse-zeta strip frame;
coefficientwise positive paired Selberg forcing;
positive inverse on the plus channel;
finite averaged carry bank n=2,...,31;
positive compact five-window Green potential.
```

## 6. Proof boundary

Closed exactly:

- explicit paired multiplier;
- uniform closed-strip frame lower bound;
- two-sided equivalence with `1/zeta`;
- positive summed Selberg forcing;
- compatibility with the factor-32 carry localization.

Open:

- an upper estimate for the complete independent-frequency physical block in terms of the finite carry bank plus strict-delay tails;
- a strict scale recurrence;
- RH.
