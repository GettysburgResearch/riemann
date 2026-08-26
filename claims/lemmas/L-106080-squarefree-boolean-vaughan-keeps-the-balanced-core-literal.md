# L-106080 — Squarefree Boolean Vaughan keeps the balanced core literal

Claim ID: `L-106080`  
Programme aliases: `LFAM1.SQUAREFREE_VAUGHAN`, `STRESS.LITERAL_CORE_BOOLEAN_ALGEBRA`, `LFAM2.SQUAREFREE_EULER_COORDINATE`  
Status: **PROVED EXACT SOURCE IDENTITY AND POWER-SAVING TYPE-I REDUCTION**  
Created: 2026-08-25  
Depends on: parent `L-102880`, `L-102886--L-102888`; `L-102505`; `R-106071`  
Programme issues: #743, #736, #737  
RH status: **not assumed**

The horizon-safe completion source is supported on literal squarefree cores:

\[
N=P a^2,
\qquad
P=pq,
\qquad
\mu^2(a)=1,
\qquad
(a,P)=1.
\]

The ordinary Dirichlet-convolution Vaughan coordinate is exact after all of its
rows are recombined, but its individual rows contain nonsquarefree
factorization artifacts.  Those artifacts obscure which prime labels are
actually available for owner selection.  This lemma gives an exact alternative
coordinate inside the finite squarefree Euler algebra.

## 1. Boolean convolution

On squarefree integers coprime to `P`, define

\[
(f\star g)(n)
=
\sum_{\substack{de=n\\(d,e)=1}}f(d)g(e).
\tag{L-106080.1}
\]

Equivalently, prime supports are combined by disjoint union.  Let
`1_sf(n)=1` and let `mu_sf(n)=mu(n)` on this algebra.  Then

\[
\boxed{\mu_{\rm sf}\star\mathbf1_{\rm sf}=\varepsilon.}
\tag{L-106080.2}
\]

Freeze the same dyadic cutoff `U` as in the parent and put

\[
\mu_U=\mu_{\rm sf}\mathbf1_{n\le U},
\qquad
a_U=\varepsilon-\mu_U\star\mathbf1_{\rm sf}.
\]

The usual Vaughan algebra uses only associativity and
`mu_sf star 1_sf = epsilon`; hence coefficientwise

\[
\boxed{
\mu_{\rm sf}
=2\mu_U
-\mu_U\star\mu_U\star\mathbf1_{\rm sf}
+a_U\star a_U\star\mu_{\rm sf}.
}
\tag{L-106080.3}
\]

No nonsquarefree physical core occurs in any row.

## 2. Balanced support contains two distinct core primes

For every squarefree `n` with `1<n<=U`, all divisors of `n` occur in the
truncated Boolean convolution, so

\[
a_U(n)=0.
\]

Also `a_U(1)=0`.  Therefore every nonzero representation in

\[
a_U\star a_U\star\mu_{\rm sf}
\]

has

\[
r>U,
\qquad s>U,
\qquad r,s>1,
\qquad (r,s)=1.
\]

Thus its physical core contains at least two distinct prime labels:

\[
\boxed{
(a_U\star a_U\star\mu_{\rm sf})(a)\ne0
\quad\Longrightarrow\quad
\omega(a)\ge2.
}
\tag{L-106080.4}
\]

The number of disjoint Boolean factorizations is at most
`3^omega(a)=a^(o(1))`, and `|a_U(n)|<=tau(n)`.  Hence the square-core
coefficient bounds required by the coherent phase theorem `L-102883` are
unchanged up to a subpower factor.

## 3. Squarefree zero-moment lattice

For a finite squarefree exclusion set `R`, put

\[
\mathscr L_{K,{\rm sf}}^{(R)}(Z)
=
\sum_{\substack{m\ge1\\\mu^2(m)=1\\(m,R)=1}}
\frac1mK_L(Z/m^2).
\]

Using

\[
\mu^2(m)=\sum_{k^2\mid m}\mu(k)
\]

and writing `m=k^2 n` gives the exact reindexing

\[
\boxed{
\mathscr L_{K,{\rm sf}}^{(R)}(Z)
=
\sum_{\substack{k\ge1\\(k,R)=1}}
\frac{\mu(k)}{k^2}
\mathscr L_K^{(R)}(Z/k^4).
}
\tag{L-106080.5}
\]

The owner/exclusion operator is a finite product of factors
`I-p^(-1)S_(p^2)`.  Parent `L-102880` therefore gives, uniformly on a finite
horizon,

\[
\mathscr L_K^{(R)}(W)
\ll X^{o(1)}W^{-1/2}.
\]

Only `k<=Z^(1/4)` can be active in (L-106080.5), and consequently

\[
\boxed{
\mathscr L_{K,{\rm sf}}^{(R)}(Z)
\ll X^{o(1)}Z^{-1/4}.
}
\tag{L-106080.6}
\]

With `U=Y^(1/6)`, the Boolean Type-I row satisfies

\[
\begin{aligned}
|\mathcal T_{U,{\rm sf}}^{K,(P)}(Y)|
&\ll
X^{o(1)}Y^{-1/4}
\left(\sum_{d\le U}d^{-1/2}\right)^2\\
&\ll
\boxed{X^{o(1)}Y^{-1/12}.}
\end{aligned}
\tag{L-106080.7}
\]

The same square-shift and finite-Euler operators act in the logarithmic source
Hilbert space with summable or polylogarithmic norm.  Thus the parent Type-I
assembly remains power-saving after the Boolean restriction.  The fixed
terminal rows are unchanged.

## 4. Exact replacement coordinate

The complete owner-excluded derivative core can therefore be written as

\[
\boxed{
\mathcal C_P^K
=
\mathcal T_{U,{\rm sf}}^{K,(P)}
+
\mathcal B_{U,{\rm sf}}^{K,(P)},
}
\tag{L-106080.8}
\]

where the first row is power-small and every atom of the second row has a
literal squarefree core containing at least two distinct prime labels.

This is an alternative exact Vaughan coordinate for the same fixed detector.
It does not alter the carrier, the marked-`67` ledger, the horizon-safe owner
allocation, or any hypothetical reciprocal-zeta pole.

## Scope

The lemma proves the source identity, literal support, factorization bound and
zero-moment Type-I estimate.  It does not by itself estimate the coherent
balanced owner current.  The owner rule which exploits (L-106080.4) is
`L-106081`; its global phase composition is `L-106082`.