# Q4 UOSACF equivalence and finite-filter exhaustion

**Scientific status: the Riemann Hypothesis remains unproved.**

Frozen base: PR #595 at `e66a91166b80cbf0a520e3a78ea96582d263d563`.


---

# L-95600 — One-sided subpower annular Q4 is equivalent to the Riemann Hypothesis

Claim ID: `L-95600`  
Status: **PROPOSED COMPLETE EQUIVALENCE — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Frozen base: PR #595 at `e66a91166b80cbf0a520e3a78ea96582d263d563`  
Scientific status: **RH remains unproved**

Let \(\mathcal A(X)\) be the exact ten-band annular Q4 observation of PR #580,
and let \(\mathcal S_H(X)\) be the separated small-gcd coprime form with
\(H=(\log 2X)^B\). PR #595 proves

\[
\mathcal A(X)^2
=
\mathcal D_A(X)+\mathcal S_H(X)+E_H(X),
\]

with

\[
\mathcal D_A(X)=O(\log^2 X),
\qquad
E_H(X)=O_B(\log^{B+2}(2X)).
\]

It defines `UOSACF` by requiring, for every \(\varepsilon>0\),

\[
\mathcal S_H(X)\le C_\varepsilon X^\varepsilon
\]

for all sufficiently large \(X\), and proves `UOSACF -> RH`.

## Converse under RH

Let

\[
M(x)=\sum_{n\le x}\mu(n),
\qquad
M_o(x)=\sum_{\substack{n\le x\\n\ {\rm odd}}}\mu(n).
\]

The exact dyadic identity is

\[
M(x)=M_o(x)-M_o(x/2),
\]

hence

\[
\boxed{
M_o(x)=\sum_{j\ge0}M(x/2^j).
}
\tag{L-95600.1}
\]

Under RH, for every \(\eta>0\),

\[
M(x)=O_\eta(x^{1/2+\eta}),
\]

and therefore the same estimate holds for \(M_o\).

Write the exact ten-band weight as

\[
G_X(t)
=
\frac{(\log t)J_0(t/X)+(\log2)J_1(t/X)}{\sqrt t}.
\]

On each activation band, the deposited exact cubic formulas imply uniformly

\[
|G_X(t)|\ll \frac{\log(2X)}{\sqrt X},
\qquad
|G_X'(t)|\ll \frac{\log(2X)}{X^{3/2}}.
\tag{L-95600.2}
\]

Partial summation on each of the ten bands, retaining every real endpoint,
gives

\[
\boxed{
\mathcal A(X)=O_\eta(X^\eta\log(2X)).
}
\tag{L-95600.3}
\]

Given \(\varepsilon>0\), choose \(\eta<\varepsilon/4\). Then

\[
\mathcal S_H(X)
\le
\mathcal A(X)^2
+
O_B(\log^{B+2}(2X))
\le
C_\varepsilon X^\varepsilon.
\]

Thus RH implies UOSACF.

## Equivalence

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathrm{UOSACF}
\Longleftrightarrow
\mathcal A(X)=X^{o(1)}.
}
\tag{L-95600.4}
\]

The annular Q4 condition is therefore an exact RH criterion, not a weaker
standard Type-II estimate.


---

# L-95601 — Every subpower-invertible scale filter preserves the Q4/RH criterion

Claim ID: `L-95601`  
Status: **PROPOSED COMPLETE EXACT FILTER THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: `L-95600`

Let

\[
(SF)(X)=F(X/2)
\]

and let

\[
P(S)=\sum_{r=0}^{R}c_rS^r,
\qquad c_0=1.
\]

Suppose the formal inverse is

\[
P(S)^{-1}=\sum_{j\ge0}b_jS^j
\]

and, with \(L=\lfloor\log_2X\rfloor+O(1)\),

\[
\sum_{j\le L}|b_j|=\exp(o(L)).
\tag{L-95601.1}
\]

Then

\[
\boxed{
F(X)=X^{o(1)}
\Longleftrightarrow
P(S)F(X)=X^{o(1)}.
}
\tag{L-95601.2}
\]

The forward implication is finite linearity. For the reverse implication,
truncate the exact inverse after the last scale above the fixed base range.
The inverse coefficient mass is \(X^{o(1)}\), and the finitely many terminal
values also contribute \(X^{o(1)}\).

## Fixed critical-Haar differences

For every fixed integer \(k\ge1\),

\[
(I-S)^{-k}
=
\sum_{j\ge0}
\binom{j+k-1}{k-1}S^j,
\]

and

\[
\sum_{j=0}^{L}\binom{j+k-1}{k-1}
=
\binom{L+k}{k}
=
O_k(L^k).
\tag{L-95601.3}
\]

Thus any fixed number of additional vanishing Mellin moments preserves the
subpower criterion and cannot make the Q4 gate weaker than RH.

The same remains true for an endpoint-dependent order \(k=k(X)\) whenever

\[
k\log(1+L/k)=o(L).
\tag{L-95601.4}
\]

Therefore fixed finite filters, fixed moment annihilators, and a broad class of
slowly growing filters merely repackage the same RH criterion.


---

# L-95602 — The classical Vinogradov–Korobov bound transfers exactly to the annular Q4 packet

Claim ID: `L-95602`  
Status: **PROPOSED COMPLETE UNCONDITIONAL TRANSFER — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Depends on: exact ten-band kernels of PR #580

Use the classical consequence of the Vinogradov–Korobov zero-free region

\[
M(x)
\ll
x\exp\!\left[
-c(\log x)^{3/5}(\log\log x)^{-1/5}
\right].
\tag{L-95602.1}
\]

The exact identity

\[
M_o(x)=\sum_{j\ge0}M(x/2^j)
\]

gives the same form for the odd Mertens state, with a possibly smaller
constant.

Applying bandwise partial summation with the exact bounds

\[
|G_X(t)|\ll\frac{\log(2X)}{\sqrt X},
\qquad
|G_X'(t)|\ll\frac{\log(2X)}{X^{3/2}},
\]

yields

\[
\boxed{
|\mathcal A(X)|
\ll
\sqrt X\,\log(2X)
\exp\!\left[
-c_1(\log X)^{3/5}(\log\log X)^{-1/5}
\right].
}
\tag{L-95602.2}
\]

Consequently

\[
\boxed{
\mathcal S_H(X)
\ll_B
X\log^2(2X)
\exp\!\left[
-2c_1(\log X)^{3/5}(\log\log X)^{-1/5}
\right]
+
\log^{B+2}(2X).
}
\tag{L-95602.3}
\]

This is a genuine unconditional improvement over a source-blind
\(O(X\,\mathrm{polylog}\,X)\) estimate. It remains \(X^{1-o(1)}\), not
\(X^{o(1)}\), and therefore does not prove UOSACF or RH.


---

# L-95603 — Exact bridge from the finite odd-core source to the compact Q4 Schur current

Claim ID: `L-95603`  
Status: **PROPOSED COMPLETE SOURCE-INTERFACE THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-18  
Scope: exact source and critical-scale operators; no Schur domination claim

Put

\[
z=2^{-s},
\qquad
P=1-4z^2,
\qquad
R=1-z^2.
\]

The reciprocal source used by PRs #554--#595 is

\[
A_4(s)=\frac{P}{R\zeta(s)}.
\]

The compact source used by the older Q4 Schur programme is

\[
B_\sharp(s)=R A_4(s)=\frac{P}{\zeta(s)}.
\]

Let

\[
D_4(s)=-P A_4'(s)
\]

be the logarithmic Q4 source. Since

\[
R'(s)=(\log4)z^2,
\]

differentiation gives the exact identity

\[
\boxed{
R^2D_4
=
PR(-B_\sharp')
+
(\log4)Pz^2B_\sharp.
}
\tag{L-95603.1}
\]

The first term is the compact RH-sensitive current through a finite Q4
filter. The second is an explicit delayed bare-source gauge.

## Critical-scale realization

For a critical observation

\[
\mathcal O_c(X)=\sum_n\frac{c(n)}{\sqrt n}\psi(n/X),
\]

convolution by \(\delta_4\) acts as

\[
\mathcal O_{\delta_4*c}(X)=\frac12\mathcal O_c(X/4).
\]

Thus the factor \(R=1-4^{-s}\) is represented by

\[
I-\frac12S^2.
\]

Its squared inverse is stable:

\[
\boxed{
\left(I-\frac12S^2\right)^{-2}
=
\sum_{j\ge0}(j+1)2^{-j}S^{2j},
\qquad
\sum_{j\ge0}(j+1)2^{-j}=4.
}
\tag{L-95603.2}
\]

Therefore the finite odd-core observation and the compact current-plus-gauge
observation are equivalent at the subpower scale.

At a zeta zero of multiplicity \(m\), the compact current term has pole order
\(m+1\), while the bare gauge has order at most \(m\). The gauge cannot cancel
the conclusion-producing current pole.

This identifies the true nonlocal frontier: a source-complete Schur,
Bellman, or Hardy estimate for the compact current. It does not prove that
estimate.


---

# R-95600 — Finite moments and source-blind positive data cannot prove UOSACF

Claim ID: `R-95600`  
Status: **EXACT SCOPE FIREWALL**  
Created: 2026-08-18  
Depends on: exact top Q4 band from PR #580

On

\[
\frac23\le x\le\frac34,
\]

the annular kernels satisfy

\[
J_0(x)=W(x)=\frac{x(1-x)(2x-1)}3\ge\frac2{81},
\qquad
J_1(x)=0.
\tag{R-95600.1}
\]

Replace the actual Möbius signs by \(+1\) on the odd squarefree cores in

\[
\frac{2X}{3}\le m\le\frac{3X}{4}.
\]

This replacement preserves:

```text
all ten activation bands;
all fifteen inner squarefree/coprime moments;
all gcd and ratio constraints;
the complete diagonal;
every source-blind PSD or absolute-value datum;
every local kernel and passive fibre norm.
```

Yet the output satisfies

\[
\sum_{\substack{2X/3\le m\le3X/4\\m\ {\rm odd\ squarefree}}}
\frac{\log m}{\sqrt m}J_0(m/X)
\gg
\sqrt X\log X,
\tag{R-95600.2}
\]

while its diagonal is only \(O(\log^2X)\).

Therefore no argument based solely on the finite inner moments, local
activation geometry, diagonal energy, positive-kernel completion, or
source-blind inequalities can establish UOSACF. The outer Möbius parity must
be used before absolute values.


---

# O-95600 — Five-million-endpoint annular cross-sign reconnaissance

Claim ID: `O-95600`  
Status: **FLOATING DISCOVERY ONLY — NONPROBATIVE**  
Created: 2026-08-18

An optimized prefix-moment scanner evaluates the exact ten-band formulas in
floating arithmetic through \(X=5{,}000{,}000\).

Observed:

```text
positive off-diagonal endpoints: 74
last positive endpoint:          105
largest positive cross:          1.9002659466... at X=92
negative for every scanned X:    106 <= X <= 5,000,000
largest |A|:                     2.2195770335... at X=368
```

Representative values:

```text
X=106       cross = -0.0494798208...
X=1,000     cross = -8.8855594800...
X=100,000   cross = -44.3502628621...
X=5,000,000 cross = -97.4438376462...
```

The scan suggests a strong eventual Bessel/Schur phenomenon but proves no
cofinal sign, no UOSACF estimate, and no statement about RH. The exact
source code and retained JSON are included for targeted mutation and directed
follow-up.


---

# T-95600 — Q4 finite-filter exhaustion and the corrected nonlocal frontier

Claim ID: `T-95600`  
Status: **COMPLETE FRONTIER THEOREM — RH UNPROVED**  
Created: 2026-08-18  
Depends on: `L-95600`--`L-95603`, `R-95600`; PR #595

The combined result is:

\[
\boxed{
\mathrm{RH}
\Longleftrightarrow
\mathrm{UOSACF}
\Longleftrightarrow
\mathcal A(X)=X^{o(1)}.
}
\]

Every fixed finite scale filter, every fixed finite moment annihilator, and
every scale filter with subpower inverse mass preserves this equivalence.

The exact finite-band source is also stably equivalent to the compact Q4
current plus one explicit lower-pole-order delayed gauge. Hence further
finite-band or finite-moment preprocessing cannot be the missing theorem.

The corrected conclusion-producing frontier is:

> Prove a genuinely nonlocal, outer-sign-sensitive Schur/Bellman/Hardy
> estimate for the compact reciprocal-\(\zeta\) current, strong enough to give
> \(\mathcal A(X)=X^{o(1)}\).

A local PSD estimate, diagonal bound, finite moment calculation, or
source-blind large sieve cannot supply it.

```text
UOSACF -> RH                           RETAINED / PR #595
RH -> UOSACF                           PROPOSED COMPLETE
UOSACF <=> annular subpower            PROPOSED COMPLETE
subpower-safe filter invariance        PROPOSED COMPLETE
Vinogradov-Korobov Q4 transfer         PROPOSED COMPLETE UNCONDITIONAL
finite-moment source-blind closure     REFUTED
compact-current source bridge          PROPOSED COMPLETE
nonlocal compact-current domination    OPEN / RH-EQUIVALENT
Riemann Hypothesis                     UNPROVEN
```


---

# M-95600 — Hostile review protocol

Review in this order:

1. `L-95600`: verify the odd-Mertens dyadic identity and bandwise partial
   summation in both directions.
2. `L-95601`: verify every inverse coefficient and the subpower mass condition.
3. `R-95600`: retain the top-band sign-replacement witness.
4. `L-95603`: check source order, the derivative sign, the critical
   \(\delta_4\) coefficient, and pole orders.
5. `L-95602`: treat the classical zero-free-region estimate only as an
   unconditional \(X^{1-o(1)}\) bound.
6. Treat `O-95600` as floating discovery only.

Immediate rejection triggers:

```text
claiming the sign scan is cofinal;
claiming a fixed extra vanishing moment weakens RH;
dropping the J1 boundary without the exact source bridge;
using a source-blind moment or PSD inequality after R-95600;
cancelling the compact current pole by the lower-order gauge;
claiming RH has been proved.
```


---

# Q4 successor: UOSACF equivalence and finite-filter exhaustion

## Result

PR #595 correctly weakens SACF to a one-sided subpower estimate. This packet
proves the converse under RH, so that the weakened estimate is exactly
equivalent to RH.

It also proves that every fixed, and many slowly growing, scale filters have
subpower inverse cost. Additional finite annularization or moment cancellation
therefore cannot lower the arithmetic difficulty.

The finite odd-core source is related exactly to the older compact Q4 current
by

\[
R^2D_4=PR(-B_\sharp')+(\log4)Pz^2B_\sharp.
\]

The second term is a delayed lower-pole-order gauge. The first is the genuine
reciprocal-\(\zeta\) current.

## Unconditional progress

The best classical zero-free-region input transfers to the exact Q4 packet and
gives

\[
\mathcal S_H(X)
\ll
X\log^2X
\exp[-c(\log X)^{3/5}(\log\log X)^{-1/5}]
+\mathrm{polylog}.
\]

This is a genuine gain but remains \(X^{1-o(1)}\).

## Correct frontier

The remaining theorem must use the outer Möbius signs through a nonlocal
Schur, Bellman, Hardy, or equivalent global arithmetic mechanism. Fixed kernel
engineering is exhausted at the RH-equivalent scope.

RH remains unproved.
