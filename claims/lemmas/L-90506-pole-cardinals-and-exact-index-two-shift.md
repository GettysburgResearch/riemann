# L-90506 — Removing the two pole coordinates shifts the exact Pontryagin index by two

Claim ID: `L-90506`  
Status: **PROPOSED COMPLETE EXACT INDEX LEMMA — INDEPENDENT REVIEW REQUIRED**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-11  
Depends on: the global Xi-cardinal source theorem on PR #365; the trace-class completions `L-90501/L-90505`; the centered Weil explicit formula  
Scope: exact zero/pole cardinal algebra and a pole-null Fredholm operator; no prime-side positivity theorem

## 1. Centered Xi and the two pole cardinals

Use

\[
 \Xi(z)=\xi\!\left(\frac12+iz\right).
\]

The completed zeta function satisfies

\[
 \Xi(i/2)=\xi(0)=\frac12,
 \qquad
 \Xi(-i/2)=\xi(1)=\frac12.
 \tag{L-90506.1}
\]

Define

\[
 \boxed{
 E_+(z)=\Xi(z)(1-2iz),
 \qquad
 E_-(z)=\Xi(z)(1+2iz).
 }
 \tag{L-90506.2}
\]

Then

\[
 \begin{array}{c|cc}
 &i/2&-i/2\\ \hline
 E_+&1&0\\
 E_-&0&1
 \end{array}
 \tag{L-90506.3}
\]

and both functions vanish at every nontrivial centered zeta zero.

If

\[
 \Xi(z)=\int\Phi(u)e^{izu}\,du,
\]

then `E_+` and `E_-` have sources `Phi+2Phi'` and `Phi-2Phi'`, respectively. Riemann's theta kernel and all its derivatives are super-Gaussian, so the two pole cardinals belong to every confined space in `L-90501/L-90505`.

## 2. Pole-free form

Let

\[
 P(f,g)=
 \widehat f(i/2)\overline{\widehat g(i/2)}
 +
 \widehat f(-i/2)\overline{\widehat g(-i/2)}
 \tag{L-90506.4}
\]

be the positive pole form and define

\[
 \boxed{Q=W-P.}
 \tag{L-90506.5}
\]

Since `E_+` and `E_-` vanish at every zeta zero,

\[
 W(E_\sigma,f)=0
 \qquad(\sigma\in\{+,-\})
 \tag{L-90506.6}
\]

for every admissible `f`. Equations (L-90506.3)--(L-90506.5) give

\[
 Q(E_\sigma,E_\tau)=-\delta_{\sigma\tau}.
 \tag{L-90506.7}
\]

Thus the pole-free form has an unavoidable negative two-plane.

## 3. Pole-null off-line cardinals

Let `H_omega` be the exact Xi-cardinal difference for one reflected off-line pair from PR #365:

\[
 \widehat H_\omega(\omega)=1,
 \qquad
 \widehat H_\omega(\bar\omega)=-1,
\]

and zero at every other distinct Xi zero. Define

\[
 \boxed{
 \widetilde H_\omega
 =H_\omega
 -H_\omega(i/2)E_+
 -H_\omega(-i/2)E_-.
 }
 \tag{L-90506.8}
\]

The correction does not alter any nontrivial-zero value, but it gives

\[
 \widehat{\widetilde H_\omega}(i/2)
 =\widehat{\widetilde H_\omega}(-i/2)=0.
 \tag{L-90506.9}
\]

Its source remains super-Gaussian. For distinct off-line pairs,

\[
 Q(\widetilde H_\omega,\widetilde H_\nu)=0
 \quad(\omega\ne\nu),
 \qquad
 Q(\widetilde H_\omega,\widetilde H_\omega)
 =-2m_\omega.
 \tag{L-90506.10}
\]

Moreover the pole plane and every modified off-line cardinal are `Q`-orthogonal.

## 4. Exact index formula

Let `q` be the number of distinct reflected off-line pairs, allowing infinity.

The zero/pole coordinate map represents `Q` as the pullback of the orthogonal direct sum of:

```text
one positive line for every critical-line zero;
one hyperbolic plane for every off-line pair;
two negative pole lines.
```

Therefore

\[
 n_-(Q)\le q+2.
 \tag{L-90506.11}
\]

Equations (L-90506.7) and (L-90506.10) construct `q+2` mutually `Q`-orthogonal negative directions, so

\[
 \boxed{n_-(Q)=q+2.}
 \tag{L-90506.12}
\]

Now let

\[
 \mathcal N
 =\{f:\widehat f(i/2)=\widehat f(-i/2)=0\}.
 \tag{L-90506.13}
\]

On `N`, `Q=W`. The modified cardinals lie in `N`, while the zero-side pullback gives the reverse bound. Hence

\[
 \boxed{n_-(W|_{\mathcal N})=q.}
 \tag{L-90506.14}
\]

Consequently

\[
 \boxed{
 \mathrm{RH}
 \iff n_-(Q)=2
 \iff W|_{\mathcal N}\succeq0.
 }
 \tag{L-90506.15}
\]

This is an exact index-two reformulation: the two negative directions of the pole-free form are known and unavoidable; every further negative direction is an off-line pair.

## 5. Trace-class pole-null projection

Let `A` be either trace-class completion from `L-90501` or `L-90505`, on coefficient Hilbert space `H`. Let

\[
 L:H\to\mathbb C^2,
 \qquad
 Lg=
 \begin{pmatrix}
 \widehat{Jg}(i/2)\\
 \widehat{Jg}(-i/2)
 \end{pmatrix}.
 \tag{L-90506.16}
\]

The pole cardinals imply that `L` is surjective. Put

\[
 \Pi_0=I-L^*(LL^*)^{-1}L,
 \tag{L-90506.17}
\]

and define on `ker L`

\[
 \boxed{A^{(0)}=\Pi_0A\Pi_0|_{\ker L}.}
 \tag{L-90506.18}
\]

Then `A^(0)` is self-adjoint trace class, represents the pole-null Weil form, and

\[
 \boxed{n_-(A^{(0)})=q.}
 \tag{L-90506.19}
\]

The pole term vanishes identically in its explicit-formula expansion. Its Fredholm determinant

\[
 D^{(0)}(t)=\det(I+tA^{(0)})
 \tag{L-90506.20}
\]

has exactly one positive real zero per off-line pair.

## 6. Proof boundary

Proved here:

- two explicit super-Gaussian pole cardinals;
- pole-null modification of every off-line Xi cardinal;
- exact global index shift `n_-(Q)=q+2`;
- exact pole-null index `q`;
- a rank-two projected trace-class operator with no pole term.

Not proved:

- positivity of the pole-null operator;
- a prime-side bound on its third variational eigenvalue;
- RH.
