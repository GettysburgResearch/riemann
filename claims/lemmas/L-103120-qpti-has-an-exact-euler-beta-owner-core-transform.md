# L-103120 — QPTI has an exact Euler–Beta owner–core transform

Claim ID: `L-103120`  
Status: **PROVED EXACT FINITE-SOURCE AND ABSOLUTELY-CONVERGENT MELLIN IDENTITY**  
Created: 2026-08-26  
Depends on: `L-102746`, `L-102951`, `L-103111--L-103112`; PR #751 `L-106132--L-106134`; PR #730 at `b3114562acbeb8c5890ef7a5fc59eed8db71d29a` for the corrected bounded-detector symbol  
RH status: **not assumed**

This lemma removes the adaptive quarter-power cutoffs from the final formula.
They prove an exact support identity, but the resulting physical field has one
fixed Euler–Beta transform.

## 1. Complete equal-pair physical source

Work first on a finite labelled prime set `mathcal L`; repeated copies of a
physical prime remain distinct labels.  For a Mellin parameter `s`, put

\[
z_p(s)=p^{-s-1/2}.
\tag{L-103120.1}
\]

The owner atom `x_p=p^{-1/2}U_p` contributes `z_p(s)`.  A core atom
`y_p=p^{-1}U_(p^2)` contributes

\[
p^{-1-2s}=z_p(s)^2.
\]

Hence the Mellin polynomial of the complete canonical equal-pair lift of the
squarefree harmonic source is

\[
\boxed{
\mathscr E_{\mathcal L}(s)
=
\sum_{\substack{p<q\\p,q\in\mathcal L}}
\ \sum_{\substack{c\ {m squarefree}\\
                   \operatorname{supp}(c)\subseteq
                   \mathcal L\setminus\{p,q\}}}
 {\mu(c)\over\binom{\omega(c)+2}{2}}
 z_p(s)z_q(s)
 \prod_{r\mid c}z_r(s)^2 .
}
\tag{L-103120.2}
\]

Equivalently, one physical atom is

\[
N=pq\,c^2,
\qquad
{\mu(c)\over\binom{\omega(c)+2}{2}\sqrt{pq}\,c}
K_L(X/N).
\tag{L-103120.3}
\]

The map `(p,q,c)->pq c^2` is injective after the unordered owner pair and
literal prime labels are retained, because `pq` is the squarefree kernel of
`N`.

## 2. Exact Beta product formula

The elementary identity

\[
{1\over\binom{k+2}{2}}
=2\int_0^1(1-\theta)\theta^k\,d\theta
\tag{L-103120.4}
\]

and finite Fubini give

\[
\boxed{
\mathscr E_{\mathcal L}(s)
=2\int_0^1(1-\theta)
\sum_{p<q}z_pz_q
\prod_{r\ne p,q}(1-\theta z_r^2)
\,d\theta .
}
\tag{L-103120.5}
\]

Put

\[
P_\theta(s)=\prod_{r\in\mathcal L}(1-\theta z_r^2),
\]

\[
A_\theta(s)=\sum_{p\in\mathcal L}
 {z_p\over1-\theta z_p^2},
\qquad
B_\theta(s)=\sum_{p\in\mathcal L}
 {z_p^2\over(1-\theta z_p^2)^2}.
\]

Then

\[
\boxed{
\mathscr E_{\mathcal L}(s)
=
\int_0^1(1-\theta)P_\theta(s)
\bigl(A_\theta(s)^2-B_\theta(s)\bigr)
\,d\theta .
}
\tag{L-103120.6}
\]

The subtraction of `B_theta` is exactly the distinct-owner/Wick diagonal
removal.  It is not an asymptotic correction.

There is also one auxiliary Euler polynomial

\[
\mathcal F_{\mathcal L}(u,\theta;s)
=
\prod_{p\in\mathcal L}
(1+u z_p-\theta z_p^2),
\]

for which

\[
\boxed{
\mathscr E_{\mathcal L}(s)
=
\int_0^1(1-\theta)
\left.\partial_u^2
\mathcal F_{\mathcal L}(u,\theta;s)
\right|_{u=0}
\,d\theta .
}
\tag{L-103120.7}
\]

Thus QPTI is a second owner variation of one literal Euler product, with the
Möbius square core retained before any absolute value.

## 3. Infinite-source scope

For `Re(s)>1/2`, the owner sums and products in
(L-103120.5)--(L-103120.7) converge absolutely, so the identities pass to the
full prime set by dominated convergence.  On the critical finite horizon they
remain coefficient-exact finite identities; no infinite Euler product is
invoked there.

## 4. Direct bounded-detector observation

The corrected direct Mellin symbol from PR #730 is

\[
\boxed{
\widehat K_L(s)
=
{4(s-1)(1-2^{-s})^2
 (1-\sqrt2\,2^{-s})
 \over s(s-1/2)}.
}
\tag{L-103120.8}
\]

Consequently, before the inherited closed packets are removed,

\[
\boxed{
\widehat H_{\rm eq}(s)
=
\widehat K_L(s)\mathscr E(s).
}
\tag{L-103120.9}
\]

This direct formula does not use the historical, now-corrected identity
`Khat_L=P*Ahat^2`.  Reflection and common-mother coordinates require the
stable dyadic/differential bridge of PR #730; QPTI itself remains the direct
bounded `K_L` current.

## 5. Quarter-power identification

By `L-103111`, on each dyadic owner block the quarter-power balanced source has
zero physical response.  By `L-103112`, the complementary quarter-power
Type-I lift therefore has exactly the same physical current as
(L-103120.2), modulo the already-closed root, first-chaos, repeated-label,
squared-activity and terminal fields.

Hence `QPTI103112` is precisely the one-sided physical estimate for the
inverse Mellin transform of

\[
\widehat K_L(s)\mathscr E_{\rm live}(s),
\]

where `E_live` is obtained from (L-103120.2) only by the frozen closed-ledger
subtractions.

## Scope

This lemma proves the exact global arithmetic transform and removes an
ambiguity about where the adaptive cutoff lives.  It does **not** estimate the
signed inverse Mellin transform, prove `QPTI103112`, or prove RH.
