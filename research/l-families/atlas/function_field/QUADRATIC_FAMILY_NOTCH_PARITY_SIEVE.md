# Odd-conductor all-degree parity sieve

Status: **exact theorem for every odd prime power, every odd-degree
squarefree conductor, and every family degree**.  The odd notch is a
distinguished specialization.  The proof is coefficient algebra over `F_2`;
no field, polynomial, curve, or zero enumeration is used.

The zeros discussed below are zeros of the raw family correlation sum
`S_(n,Q)`, not zeros of an individual `L`-function.

## Start here

Let `q` be an odd prime power, let `Q` be monic squarefree, and write its
labelled irreducible-factor degrees as

\[
 d_P=\deg P\qquad(P\mid Q).
\]

Put

\[
 A(x)=\prod_{P\mid Q}(1-x^{d_P})^{-1}
     =\sum_{k\ge0}a_kx^k.
\]

For every family degree `r>=0`, with the convention `a_(-1)=0`, the complete
raw correlation sum satisfies

\[
 \boxed{S_{r,Q}\equiv a_r+a_{r-1}\pmod2.}
 \tag{0.1}
\]

At the odd notch

\[
 M=\deg Q=2n-1,
\]

the general theorem specializes to the requested all-profile congruence

\[
 \boxed{S_{n,Q}\equiv a_n+a_{n-1}\pmod2.}
 \tag{0.2}
\]

Consequently

\[
 \boxed{a_n\not\equiv a_{n-1}\pmod2
        \quad\Longrightarrow\quad S_{n,Q}\ne0.}
 \tag{0.3}
\]

Equivalently, every raw zero lies in the exact parity-sieve locus

\[
 \boxed{a_n\equiv a_{n-1}\pmod2.}
 \tag{0.4}
\]

This is a necessary condition, not a classification of the zeros in that
locus.

## 1. Reduction of the quadratic `L`-polynomial modulo two

For odd `M`, the frozen notch adapter has

\[
 P_Q(u)=L(u,\psi_Q)=\sum_{F\text{ monic}}\psi_Q(F)u^{\deg F}.
\]

Modulo two, `-1` and `+1` agree, while the character remains zero exactly
when `(F,Q) != 1`.  Hence

\[
\begin{aligned}
 P_Q(u)
 &\equiv \sum_{(F,Q)=1}u^{\deg F}\\
 &=\prod_{R\nmid Q}(1-u^{\deg R})^{-1}\\
 &={\prod_{P\mid Q}(1-u^{d_P})\over1-qu}
 \equiv {\prod_{P\mid Q}(1+u^{d_P})\over1+u}
 \pmod2.
\end{aligned}
\tag{1.1}
\]

The last quotient is a polynomial: every nonconstant factor
`1+u^(d_P)` is divisible by `1+u`.  This matches the frozen convention that
odd conductor degree has no split-infinity factor and
`P_Q=L(u,psi_Q)`.

Write

\[
 D_s=p_s-qp_{s-2},\qquad
 D(u)=\sum_{s\ge0}D_su^s=(1-qu^2)P_Q(u).
\]

Since `q` is odd, (1.1) gives

\[
 \boxed{
 D(u)\equiv
 (1+u)\prod_{P\mid Q}(1+u^{d_P})\pmod2.}
 \tag{1.2}
\]

The frozen odd-degree coefficient identity, before using the top notch, is

\[
 S_{n,Q}=[u^n]A(u^2)D(u).
 \tag{1.3}
\]

Over `F_2`, Frobenius squaring gives

\[
 A(u^2)
 \equiv\prod_{P\mid Q}(1+u^{2d_P})^{-1}
 =\prod_{P\mid Q}(1+u^{d_P})^{-2}.
\]

Multiplication by (1.2) therefore proves the full generating congruence

\[
 \boxed{A(u^2)D(u)\equiv(1+u)A(u)\pmod2,}
 \tag{1.4}
\]

and coefficient `u^r` proves (0.1) for every family degree `r`.  Taking
`r=n=(M+1)/2` proves the notch statement (0.2).

Odd conductor degree is needed for the no-infinity-factor adapter used in
(1.1).  The additional condition `M=2n-1` is needed only for the notch and
depth consequences below.  The formal identity (1.4) governs all family
degrees for the fixed odd conductor.

## 2. Binary subset-sum certificate

In `F_2[[u]]`, the binary telescoping identity is

\[
 {1\over1+u^d}
 =\prod_{j\ge0}(1+u^{2^jd}).
 \tag{2.1}
\]

For any fixed family degree `r`, only finitely many factors matter.  Introduce
the labelled binary atoms

\[
 \mathcal B_Q(r)
 =\{(P,j):P\mid Q,\ j\ge0,\ 2^jd_P\le r\},
\]

where `(P,j)` has weight `2^j*d_P`.  Factors of equal degree remain
distinct because the prime label `P` is retained.  Equation (2.1) gives

\[
 a_m\equiv
 \#\left\{E\subseteq\mathcal B_Q(r):
          \sum_{b\in E}{\rm wt}(b)=m\right\}\pmod2
 \qquad(m\le r).
 \tag{2.2}
\]

Adjoin one special atom `star` of weight one.  Combining (0.1) and (2.2)
produces the exact certificate

\[
 \boxed{
 S_{r,Q}\equiv
 \#\left\{E\subseteq
    (\mathcal B_Q(r)\sqcup\{\star\}):
    \sum_{b\in E}{\rm wt}(b)=r\right\}
 \pmod2.}
 \tag{2.3}
\]

Thus an odd number of labelled binary subset representations certifies
`S_(r,Q) != 0`.  At the notch take `r=n`.  A unique representation is a
particularly simple certificate.  An even number of representations is
inconclusive: their parities cancel, but the integer statistic need not
vanish.

## 3. Shallow-layer parity collapse

Put

\[
 h=\left\lfloor{n\over2}\right\rfloor,
 \qquad n=2h+\varepsilon,
 \qquad\varepsilon\in\{0,1\}.
\]

Suppose the minimum factor degree is

\[
 d=h-j
\]

and let `m_h` denote the number of degree-`h` prime factors of `Q`.  The
exact depth decomposition is

\[
 S_{n,Q}
 =m_dD_{2j+\varepsilon}
  +\sum_{\ell=1}^{j}a_{d+\ell}
       D_{2(j-\ell)+\varepsilon}.
 \tag{3.1}
\]

If

\[
 \boxed{h>3j+\varepsilon,}
 \tag{3.2}
\]

then `d>2j+epsilon`.  Formula (1.2) has no factor-degree contribution
through degree `2j+epsilon`, so in that range

\[
 D(u)\equiv1+u\pmod{(2,u^{2j+\varepsilon+1})}.
\]

Only the final `D_0` (even `n`) or `D_1` (odd `n`) term of (3.1) survives
modulo two.  Moreover (3.2) implies `2d>h`, so `a_h=m_h`.  Therefore

\[
 \boxed{
 h>3j+\varepsilon,\qquad \min_{P\mid Q}\deg P=h-j
 \quad\Longrightarrow\quad
 S_{n,Q}\equiv m_h\pmod2.}
 \tag{3.3}
\]

In particular, every raw zero on such a shallow layer must have an even
number of degree-`h` factors.  If `m_h` is odd, parity alone proves
nonvanishing.

Special cases:

- `j=0`, even `n`: (3.3) agrees with the exact identity `S=m_h>0`.
- `j=0`, odd `n>=5`: it agrees with `S=m_h*D_1` and the fact that `D_1` is
  odd.
- `j=1`: for even `n>=8` and odd `n>=11`, any raw zero on the second layer
  must have `m_h` even.

The inequalities are sufficient, not optimized for every small `n`.
Small rows can have extra low-degree contributions in (1.2) and should be
checked from the all-profile sieve rather than extrapolated from (3.3).

## 4. Consequences for structural-zero counting

Let `Z_q(n)` be any set of degree-`2n-1` squarefree conductors on which the
raw sum vanishes.  The exact containment is

\[
 Z_q(n)\subseteq
 \{Q:a_n(Q)\equiv a_{n-1}(Q)\pmod2\}.
 \tag{4.1}
\]

This provides a deterministic sieve before any trace, monodromy, or moment
analysis.  On fixed shallow depth it can be combined with (3.3) to remove
every profile with odd `m_h`.

No numerical density follows from (4.1) alone.  Proving one would require a
count of the parity-even binary subset-sum locus, with finite-field
feasibility of repeated degrees retained.  In particular, this packet does
not assume that the two parities are equidistributed or that every
parity-even profile is a zero.

The support-forced stratum is automatically parity-even by (0.2), because
its raw sum is exactly zero.  This yields a combinatorial consistency check
`a_n congruent a_(n-1)` on that stratum, not a new source of individual
`L`-function zeros.

## 5. A split-profile control

When all `M=2n-1` factors have degree one,

\[
 A(u)=(1-u)^{-M},\qquad
 a_m={M+m-1\choose m}.
\]

Pascal's identity reduces (0.2) to

\[
 S_{n,Q}\equiv {3n-3\choose n}\pmod2.
 \tag{5.1}
\]

By Lucas--Kummer parity, this is odd exactly when adding `n` and `2n-3` in
base two has no carry, equivalently

\[
 \boxed{n\mathbin{\&}(2n-3)=0.}
 \tag{5.2}
\]

This is a finite-field-feasible profile only when `Q` can have `2n-1`
distinct linear factors, hence `q>=2n-1`.  It is an exact control, not a
fixed-`q` asymptotic family.

## 6. Provenance and claim boundary

The source is the odd-conductor identity and curve orientation at frozen
PR #756 head `6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`, file
`QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md`, git blob
`a1b8476ddd3cad6f63ff205392426ae9c2d0829c`.

Proved:

- the all-family-degree congruence (0.1), including the notch congruence
  (0.2);
- the labelled binary subset-sum certificate (2.3);
- the fixed-shallow-depth collapse (3.3);
- the split-profile Lucas control (5.2).

Not proved:

- sufficiency of the parity condition for a raw zero;
- a density of parity-even or raw-zero conductors;
- equidistribution of binary subset sums;
- a zero of an individual `L`-function, RH, or GRH;
- external novelty or priority.

The mod-two Euler-product reduction and binary product identity are
elementary and should be treated as known or folklore.  The project-specific
contribution is their exact alignment with the closed-place odd-notch
statistic and its depth-indexed exterior channels.
