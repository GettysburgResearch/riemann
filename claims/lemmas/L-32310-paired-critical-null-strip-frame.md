# L-32310 — Uniform parity frame for the critical-null triple source

Claim ID: `L-32310`  
Title: The critical-null triple source has an explicit two-channel closed-strip frame reserve without the supercritical five-mode inverse  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro-xhigh`  
Created: 2026-08-08  
Dependencies: `L-32302`; parity-twist algebra of PR #263  
Scope: source multiplier reserve and positive paired forcing; no physical-block upper estimate

## 1. Local parity polynomials

Let

\[
P_\dagger(z)=(1-z)(1-z/2)(1-\sqrt2z).
\]

Since

\[
{1\over\zeta(s)}=(1-z)\mathcal O(s),
\qquad
z=2^{-s},
\]

with `O(s)` the odd Euler product, the plus channel of `Omega_dagger` has local polynomial

\[
\boxed{
 r_+(z)=(1-z)P_\dagger(z)
 =(1-z)^2(1-z/2)(1-\sqrt2z).
}
\tag{L-32310.1}
\]

Twisting by

\[
\chi_2(n)=(-1)^{v_2(n)}
\]

replaces `z` by `-z`, so

\[
\boxed{
 r_-(z)=(1+z)^2(1+z/2)(1+\sqrt2z).
}
\tag{L-32310.2}
\]

The paired source Dirichlet series are

\[
B_+(s)=r_+(z)\mathcal O(s),
\qquad
B_-(s)=r_-(z)\mathcal O(s).
\]

## 2. Explicit closed-strip reserve

On

\[
{1\over2}\le|z|\le{1\over\sqrt2},
\]

put

\[
m_1=1-{1\over\sqrt2},
\qquad
m_2=1-{1\over2\sqrt2}.
\]

Then

\[
|1\mp z|\ge m_1,
\qquad
|1\mp z/2|\ge m_2.
\]

Therefore

\[
\begin{aligned}
|r_+(z)|^2+|r_-(z)|^2
&\ge m_1^4m_2^2
\left(|1-\sqrt2z|^2+|1+\sqrt2z|^2\right)\\
&=2m_1^4m_2^2(1+2|z|^2)\\
&\ge\boxed{3m_1^4m_2^2>0.}
\end{aligned}
\tag{L-32310.3}
\]

No compactness argument or numerical minimization is needed.

## 3. Equivalence with the inverse-zeta source

Since

\[
|1-z|\le1+1/\sqrt2,
\]

and

\[
{1\over\zeta(s)}=(1-z)\mathcal O(s),
\]

(L-32310.3) gives, throughout

\[
{1\over2}\le\Re s\le1,
\]

\[
\boxed{
|B_+(s)|^2+|B_-(s)|^2
\ge
c_\dagger\left|{1\over\zeta(s)}\right|^2,
}
\tag{L-32310.4}
\]

where

\[
\boxed{
 c_\dagger
={3(1-1/\sqrt2)^4(1-1/(2\sqrt2))^2
 \over(1+1/\sqrt2)^2}>0.
}
\tag{L-32310.5}
\]

The reverse comparison follows from boundedness of all finite local factors and the lower bound `|1-z|>=1-1/sqrt2`.

Thus the paired triple source is uniformly equivalent to the unfiltered inverse-zeta source on the entire closed critical strip.

## 4. Positive paired Selberg forcing

Let `a_+` and `Lambda_+` be the positive inverse and generalized-prime sequences of `L-32302`.  Under the parity twist,

\[
a_- =\chi_2a_+,
\qquad
\Lambda_- =\chi_2\Lambda_+.
\]

The generalized Selberg coefficients obey

\[
C_+(n)=\Lambda_+(n)\log n+(\Lambda_+*\Lambda_+)(n)\ge0,
\]

and

\[
C_-(n)=\chi_2(n)C_+(n).
\]

Therefore

\[
\boxed{
C_+(n)+C_-(n)
=(1+\chi_2(n))C_+(n)\ge0.
}
\tag{L-32310.6}
\]

The two independent-frequency reflected identities may therefore be added with a coefficientwise nonnegative forcing channel.

## 5. Advantage over the five-mode source

The five-mode filter of `L-32303` also has a closed-strip frame, but its positive inverse contains the pole-model factor `(1-2^{1-s})^-1`, producing `2^nu` two-adic coefficients.

The triple source has instead

\[
a_\dagger(2^\nu m)=O(2^{\nu/2}),
\]

and hence the polylogarithmic square budget of `L-32309`.  It is therefore the preferred source for lower-scale Hilbert recombination.

## 6. Proof boundary

Closed exactly:

- parity source polynomials;
- explicit closed-strip reserve;
- two-sided inverse-zeta equivalence;
- positive paired Selberg forcing.

Open:

- a reflected physical-block upper estimate;
- strict lower-scale recurrence;
- RH.
