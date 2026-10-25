# An exact norm-profile Jacobi transfer, with its completion costs

Status: proved algebraic and profile identities; an exploratory application of an imported ordinary fourth moment. No improvement to a native inverse mean is obtained.
Scope: the good squarefree ideals and physical sextic characters of the Eisenstein framework. Natural zeros, a common licensed puncture, the fixed ray twist, and a common norm frequency are retained.
Exact dependencies: the arithmetic and smooth-profile conventions, and the no-prime-slot plain-product moment, of OpenAI's 30 September 2026 source at commit `1581d4cbdd69a0faf34b2089614fe2a814316a6a`, TeX blob `268c4e3206d460c617d3d2129742a72b831b3def`; the squarefree adapter in PR #1021, `standalone/2026-10-24-fresh-zero-free-routes/arithmetic/DIRECT_NATIVE_APPLICATION.md`, at `9b6aaaf8b969cdb55b909a5bd5d5e949dc49f154`. The identities below are proved directly.
What was actually run: symbolic argument and source-scope inspection; no finite character computation is used as analytic evidence.
Smallest remaining gap: a joint estimate for the shifted cubic-character kernel below, stronger than freezing its auxiliary variable and applying the ordinary moment. Its nonzero additive transforms are not coefficients licensed by that ordinary moment.

## 1. The complete local correlation

Let `O = Z[omega]`, let `q_a = Na`, and use the source's self-dual
additive pairing and measure, in which the covolume of `O` is one.
Every good prime `p` has `q_p = 1 mod 6`.
For either orientation `epsilon in {1,-1}`, put

\[
 f_n(x)=\chi_n\bigl(x^2(x+1)^4\bigr)^\epsilon
       =\chi_n(x)^{2\epsilon}
          \overline{\chi_n(x+1)^{2\epsilon}}.
 \tag{1}
\]

All powers in (1) have their original zero extension. In particular,
the factors vanish if a prime of `n` divides `x` or `x+1`.

**Lemma 1.** For every good squarefree ideal `n`,

\[
 \sum_{x\bmod n}f_n(x)=\mu(n).                 \tag{2}
\]

**Proof.** At a good prime, `A = chi_p^(2 epsilon)` is a nonprincipal
cubic character. On `x != -1`, the change of variable
`t=x/(x+1)` bijects the field with the point `1` deleted. Thus

\[
 \sum_x A(x)\overline{A(x+1)}
   =\sum_{t\ne1}A(t)=-1.
\]

The point `x=-1` contributes zero. The Chinese remainder theorem
multiplies these `-1` factors. The unit ideal gives `1`. QED.

This is a complete Jacobi correlation, equivalently the familiar
Ramanujan-sum identity `c_n(1)=mu(n)`. The change of variables explains
why (2), by itself, supplies no new cancellation estimate.

## 2. Exact completion using only norm profiles

There exists a nonnegative radial Schwartz function `phi` on `C`
with integral `1`, whose additive Fourier transform is supported
strictly inside the shortest nonzero dual-lattice vector. For example,
choose a nonzero smooth radial Fourier bump in a sufficiently small
disk, take its inverse transform `g`, and normalize `|g|^2`.
Poisson summation then gives the exact partition of unity

\[
 \sum_{\ell\in\mathcal O}\phi(z+\ell)=1
 \qquad(z\in\mathbb C).                        \tag{3}
\]

Write `phi(z)=Phi(|z|^2)`. Grouping the lattice sum by residue classes
in (2) yields

\[
 \boxed{\quad
 \mu(n)=\sum_{x\in\mathcal O}
        \Phi(q_x/q_n)\,
        \chi_n\bigl(x^2(x+1)^4\bigr)^\epsilon.
 \quad}                                        \tag{4}
\]

The sum is absolutely convergent. No angular profile has been
introduced: radiality makes `phi(x/n)=Phi(q_x/q_n)` exactly.

Fix the original row weight `w(u)`, common puncture `Q`, fixed ray
character `nu`, common real frequency `t`, and smooth annular profile
`W`. Define

\[
 M_u(D)=D^{-1/2}\sum_n\mu(n)\nu(n)
   \chi_n(u)^\epsilon 1_{(n,Q)=1}q_n^{it}W(q_n/D).
\]

Put `a_x=x^2(x+1)^4` and

\[
 A_{u,x}(D)=D^{-1/2}\sum_n\mu^2(n)\nu(n)
   \chi_n(ua_x)^\epsilon 1_{(n,Q)=1}q_n^{it}
       W(q_n/D)\Phi(q_x/q_n).
\]

Then (4) gives the exact actual-row identity

\[
                 M_u(D)=\sum_x A_{u,x}(D).       \tag{5}
\]

The same frequency `t` is present throughout. For fixed `y=q_x/D`,
the column profile is `W(s)Phi(y/s)`. Its finitely many required
logarithmic derivatives are bounded by
`C_K p_J(W)(1+y)^(-K)` for every fixed `K`, with fixed orders.
Thus norm-frequency alignment and smooth separation are not the
obstruction to using (5).

The cases `x=0,-1` are excluded from every invocation of a moving-twist
moment below: their numerator `a_x` is zero. By the natural zero
convention their terms vanish for every nonunit ideal `n`. The unit
ideal, if it meets the annular profile, contributes only at bounded
`D` and has `O(U)` second moment by direct counting. Once the unit
ideal leaves the fixed support, both terms are exactly zero.

For `x != 0,-1`, the complete multiplier, including its zero support,
remains in the row. Its norm and moving radical satisfy

\[
 q_{a_x}=q_x^2q_{x+1}^4\ll(1+q_x)^6,
 \qquad
 R_x=N\operatorname{rad}(x(x+1))\ll(1+q_x)^2.
 \tag{6}
\]

## 3. The cost of freezing the curve variable

The source no-slot fourth moment for a frozen moving twist of
radical `R_x` has cost `U R_x`, with its prescribed subpower loss,
fixed profile orders and polynomial height dependence. The exact
squarefree expansion used in PR #1021 preserves this fourth-moment
scope at a logarithmic cost. Cauchy over `O(U)` physical rows therefore
gives an ordinary squarefree second-moment norm bounded by

\[
 U^{1/2+\epsilon}R_x^{1/4}
 (1+|t|)^A p_J(W)(1+q_x/D)^{-K}.                \tag{7}
\]

Equation (7) applies only where the transformed inducing characters
are nonprincipal. One sufficient, explicitly stated subfamily is the
set of original rows for which the inducing character of
`nu^3 chi_n(u)^(3 epsilon)` is nonprincipal: multiplication by `a_x`
does not change that inducing character, because `a_x` is a square.
This qualification cannot be removed by calling `x` fixed. Other
physical rows remain part of the native problem and require their
principal contributions to be handled.

Assume `1 <= D <= U^C` for a fixed `C`, as in the native application.
Use (7) first for `q_x <= D^2`; its moving radical then stays in a
fixed bounded log-length range. For `q_x > D^2`, absolute column
counting and the Schwartz bound give a total row norm
`O(U^(1/2) D^(5/2-K))`. Choose a fixed sufficiently large `K`.
Thus no invocation of the source has an unbounded moving length.
On the qualified subfamily, Minkowski, (6), and lattice counting pay

\[
 \begin{split}
 \|M(D)\|_2
 &\ll U^{1/2+\epsilon}(1+|t|)^A p_J(W)
    \sum_x(1+q_x)^{1/2}(1+q_x/D)^{-K}\\
 &\ll U^{1/2+\epsilon}D^{3/2}
          (1+|t|)^A p_J(W),\qquad K>3/2.
 \end{split}                                    \tag{8}
\]

Hence this use of the ordinary theorem produces a second-moment cost
`U D^3`, even before treating the remaining principal-inducing cases.
It is worse than the direct trivial bound `U D`. This is a paid
transfer calculation, not an improved estimate.

The three powers of `D` have identifiable origins. A complete
correlation uses `O(D)` auxiliary lattice points at column norm `D`;
the source fourth moment contributes `R_x^(1/4) = O(D^(1/2))` to the
row norm. Triangle inequality therefore pays `D^(3/2)` before
squaring. Replacing the fourth moment by a direct bound with full
radical cost would lose an additional power of `D`.

## 4. Short completion creates a different coefficient problem

For an arbitrary positive scale `X`, let

\[
 \mathcal F_n(k)=\sum_{a\bmod n}f_n(a)e(ka/n).
\]

Poisson summation in residue classes gives

\[
 \sum_x\phi(x/\sqrt X)f_n(x)
   =\frac X{q_n}\sum_{k\in\mathcal O}
       \widehat\phi(\sqrt X\,k/n)\mathcal F_n(k).
 \tag{9}
\]

The zero-frequency coefficient is exactly
`F_n(0)=mu(n)`. At `X=q_n`, the chosen Fourier support removes every
nonzero frequency and (9) becomes (4). If `X<q_n`, nonzero frequencies
are generally present. They are additive transforms of the shifted
cubic kernel, rather than the ordinary coefficients of the source
plain-product theorem.

There is an elementary exact energy check:

\[
 \sum_{k\bmod n}|\mathcal F_n(k)|^2
   =q_n\sum_{a\bmod n}|f_n(a)|^2
   =q_n\prod_{p\mid n}(q_p-2).                 \tag{10}
\]

Thus the desired complete coefficient has squared magnitude `1`,
while almost all Fourier energy lies at nonzero frequencies. The
identity does not permit their omission or a free contraction on the
physical-row Hilbert space.

A successful use of short completion would need a joint estimate
that controls these actual transformed coefficients together with
the original rows and masks. Substituting the ordinary row-volume
bound for that missing estimate would strengthen its coefficient
scope without proof. None of (2)--(10) gives a wider fractional
coefficient interval, a native mean saving, or a new zero-free region.
