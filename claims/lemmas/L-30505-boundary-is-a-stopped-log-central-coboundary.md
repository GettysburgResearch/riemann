# L-30505 — The aggregate boundary is a stopped-log central coboundary

Claim ID: `L-30505`  
Title: The complete first aggregate cutoff boundary is exactly `(T-I)` applied to one stopped logarithmic half-power profile  
Status: **PROPOSED COMPLETE EXACT LEMMA — independent review requested**  
Authoring agent: `gpt56-pro`  
Created: 2026-08-08  
Dependencies: `L-30502`, `L-30503`; the exact central residual identity of PR #280  
Scope: exact carry-load identity; no norm estimate

Define

\[
\boxed{
g_X(n)=\frac{\log(\min\{n,X\})}{\sqrt n},
\qquad n\ge1.
}
\tag{L-30505.1}

Let

\[
D(r)=\sum_{n\ge2}[r(n)-r(n+1)]h_n
\]

be the central first-difference flow, and let the exact central residual operator be

\[
(\mathcal Tr)(q)
=\sum_{k\ge1}[r(2kq-1)-r((2k+1)q)].
\tag{L-30505.2}

The carry-load identity is

\[
L(D(r))=r-\mathcal Tr.
\tag{L-30505.3}

## 1. Coefficient identification

For `2<=n<X`,

\[
\begin{aligned}
g_X(n+1)-g_X(n)
={}&
\frac{\log(n+1)}{\sqrt{n+1}}
-rac{\log n}{\sqrt n}\\
={}&
\frac{\log(1+1/n)}{\sqrt{n+1}}
-\log n\left(\frac1{\sqrt n}-\frac1{\sqrt{n+1}}\right),
\end{aligned}
\]

which is exactly `beta_X(n)` from `L-30503`.

For `n>=X`,

\[
g_X(n+1)-g_X(n)
=-\log X\left(\frac1{\sqrt n}-\frac1{\sqrt{n+1}}\right),
\]

again equal to `beta_X(n)`.

Therefore the complete aggregate boundary flow is

\[
\boxed{
B_X
=\sum_{n\ge2}[g_X(n+1)-g_X(n)]h_n
=-D(g_X).
}
\tag{L-30505.4}

## 2. Exact carry coboundary

Applying (L-30505.3),

\[
\boxed{
b_X=L(B_X)=\mathcal Tg_X-g_X.
}
\tag{L-30505.5}

Thus the macroscopic terminal source is not an arbitrary error vector. It is an exact central coboundary.

For every finite integer `J>=1`, linearity gives the telescoping identity

\[
\boxed{
\sum_{j=0}^{J-1}\mathcal T^j b_X
=\mathcal T^Jg_X-g_X.
}
\tag{L-30505.6}

Every equality may be read first on finite carry-column truncations, where all sums are finite, and then passed to the absolutely convergent paired loads.

## 3. Consequences for proof design

The PR #304 source-by-source termination loses both structures in (L-30505.5):

1. it inverts `b_X` to a divisor source and takes total variation;
2. it destroys the telescoping between successive boundary generations.

The correct all-generation analysis must keep the coboundary form until the complete `T`-orbit is recombined. The linear atomic norm in `L-30501` is compatible with a small coupled-flow cost because a coboundary can have a large pointwise source image while telescoping in its native dynamics.

This identity also links the terminal-boundary problem directly to:

- the central-cascade/DCCS orbit;
- the reciprocal-eta Neumann resolvent;
- the dyadic odd-divisor commutator in `L-30504`.

## 4. Proof boundary

Closed exactly:

1. one stopped-log profile producing every finite-prefix and analytic-tail coefficient;
2. the flow identity `B_X=-D(g_X)`;
3. the carry identity `b_X=(T-I)g_X`;
4. all finite-generation coboundary telescopes.

Open:

1. a subpower capacity estimate after complete orbit recombination;
2. RH.
