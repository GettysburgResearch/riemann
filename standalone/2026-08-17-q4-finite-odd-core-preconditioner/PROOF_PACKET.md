# Q4 finite odd-core preconditioner packet

**Scientific status: RH remains unproved.**


---

# L-95310 — Double dyadic preconditioning makes the Q4 odd-core packet finite

Claim ID: `L-95310`  
Status: **PROPOSED COMPLETE EXACT ARITHMETIC THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Frozen parent: PR #563 at `c4cc65cccb3f13a6499506cf3c26bd521c455864`  
Scope: exact critical Q4 source reduction; no deterministic odd-core cancellation bound

## 1. Source and preconditioner

Retain

\[
A_4(s)
=
\frac{1-4^{1-s}}{(1-4^{-s})\zeta(s)}
=
\sum_{n\ge1}\frac{a_4(n)}{n^s},
\]

and

\[
d_4=(\varepsilon-4\delta_4)*(a_4\log).
\]

Define the safe finite preconditioner

\[
p_2=(\varepsilon+\delta_2)^{*2}
=
\varepsilon+2\delta_2+\delta_4,
\]

and put

\[
\boxed{e_4=p_2*d_4.}
\tag{L-95310.1}
\]

Its Dirichlet multiplier \((1+2^{-s})^2\) has no zero in \(\Re s>0\).

## 2. Finite odd-core table

Write \(n=2^rm\), where \(m\) is odd. If \(m\) is not squarefree, then

\[
e_4(2^rm)=0.
\]

If \(m\) is odd squarefree, then

\[
\boxed{
e_4(2^rm)
=
\mu(m)
\left[A_r\log m+B_r\log2\right],
\qquad 0\le r\le5,
}
\tag{L-95310.2}
\]

where

\[
(A_0,\ldots,A_5)=(1,1,-8,-8,16,16),
\tag{L-95310.3}
\]

and

\[
(B_0,\ldots,B_5)=(0,-1,-8,0,32,16).
\tag{L-95310.4}
\]

For every \(r\ge6\),

\[
\boxed{e_4(2^rm)=0.}
\tag{L-95310.5}
\]

Equivalently, the six values are

\[
\mu(m)
\left(
\log m,\,
\log(m/2),\,
-8\log(2m),\,
-8\log m,\,
16\log(4m),\,
16\log(2m)
\right).
\tag{L-95310.6}
\]

Thus the infinite dyadic state of PR #563 becomes one literal factor-32 packet
after a safe finite filter.

## 3. Dirichlet-series proof

Let

\[
z=2^{-s},
\qquad
M_{\rm odd}(s)
=
\sum_{\substack{m\ge1\\m\ {\rm odd}}}
\frac{\mu(m)}{m^s}
=
\frac{1}{(1-z)\zeta(s)},
\]

and put

\[
P(z)=1-4z^2.
\]

The dyadic local factor of \(A_4\) is

\[
L(z)=\frac{P(z)}{1+z},
\]

so

\[
A_4(s)=L(z)M_{\rm odd}(s).
\]

The Dirichlet series of \(d_4\) is

\[
D_4(s)=-P(z)A_4'(s).
\]

Multiplying by \((1+z)^2\) gives

\[
\boxed{
(1+z)^2D_4(s)
=
\mathcal A(z)\bigl[-M_{\rm odd}'(s)\bigr]
+
(\log2)\mathcal B(z)M_{\rm odd}(s),
}
\tag{L-95310.7}
\]

where

\[
\mathcal A(z)
=
(1+z)(1-4z^2)^2
=
1+z-8z^2-8z^3+16z^4+16z^5,
\tag{L-95310.8}
\]

and

\[
\mathcal B(z)
=
-z(1-4z^2)(1+8z+4z^2)
=
-z-8z^2+32z^4+16z^5.
\tag{L-95310.9}
\]

Coefficient comparison proves (L-95310.2)–(L-95310.5).

## 4. Critical observation and stable inverse

For the centered Q4 cubic \(W\), define

\[
\mathcal C_d(X)
=
\sum_{n\le X}
\frac{d_4(n)}{\sqrt n}W(n/X),
\]

and define \(\mathcal C_e\) analogously with \(e_4\). Dirichlet convolution
and critical square-root scaling give

\[
\boxed{
\mathcal C_e(X)
=
\mathcal C_d(X)
+
\sqrt2\,\mathcal C_d(X/2)
+
\frac12\mathcal C_d(X/4).
}
\tag{L-95310.10}
\]

Let \(S F(X)=F(X/2)\). Then

\[
\mathcal C_e=(I+2^{-1/2}S)^2\mathcal C_d.
\]

Since \(2^{-1/2}<1\),

\[
\boxed{
\mathcal C_d(X)
=
\sum_{j\ge0}
(-1)^j(j+1)2^{-j/2}
\mathcal C_e(X/2^j),
}
\tag{L-95310.11}
\]

and the sum is finite at every endpoint. Its absolute coefficient mass is

\[
\sum_{j\ge0}(j+1)2^{-j/2}
=
(1-2^{-1/2})^{-2}.
\tag{L-95310.12}
\]

Therefore a polylogarithmic bound for \(\mathcal C_e\) is equivalent, up to a
fixed constant and exponent, to the original OCHD bound for
\(\mathcal C_d\).


---

# L-95311 — The finite odd-core packet has polylogarithmic diagonal energy

Claim ID: `L-95311`  
Status: **PROPOSED COMPLETE UNCONDITIONAL ENERGY THEOREM — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-17  
Depends on: `L-95310`; the exact Q4 cubic of PR #531

Define

\[
K_0(x)
=
\sum_{r=0}^{5}
A_r2^{-r/2}W(2^rx),
\tag{L-95311.1}
\]

and

\[
K_1(x)
=
\sum_{r=0}^{5}
B_r2^{-r/2}W(2^rx).
\tag{L-95311.2}
\]

Then the preconditioned critical observation is exactly

\[
\boxed{
\mathcal C_e(X)
=
\sum_{\substack{m\le X\\m\ {\rm odd}}}
\frac{\mu(m)}{\sqrt m}
\left[
(\log m)K_0(m/X)
+
(\log2)K_1(m/X)
\right].
}
\tag{L-95311.3}
\]

Only odd squarefree \(m\) contribute.

## Diagonal estimate

The safe pointwise Q4 bound

\[
|W(x)|\le32
\qquad(0\le x\le1)
\]

and the coefficient sums

\[
\sum_{r=0}^{5}|A_r|2^{-r/2}<16,
\qquad
\sum_{r=0}^{5}|B_r|2^{-r/2}<16
\]

give

\[
|K_0(x)|<512,
\qquad
|K_1(x)|<512.
\tag{L-95311.4}
\]

For

\[
F_{m,X}
=
\frac{
(\log m)K_0(m/X)
+
(\log2)K_1(m/X)
}{\sqrt m},
\]

one therefore has

\[
|F_{m,X}|
\le
512\frac{\log(2m)}{\sqrt m}.
\]

Consequently

\[
\boxed{
\sum_{\substack{m\le X\\m\ {\rm odd}}}
|F_{m,X}|^2
\le
2^{18}
(1+\log(2X))^3.
}
\tag{L-95311.5}
\]

Thus every same-core diagonal and the complete Rademacher-randomized model are
already polylogarithmic:

\[
\boxed{
\mathbb E_\varepsilon
\left|
\sum_m\varepsilon_mF_{m,X}
\right|^2
=
\sum_m|F_{m,X}|^2
=
O(\log^3X).
}
\tag{L-95311.6}
\]

No prime number theorem, zero table or RH input is used.

## Exact surviving correlation

Write

\[
|\mathcal C_e(X)|^2
=
\mathcal D(X)+\mathcal X(X),
\]

where

\[
\mathcal D(X)=\sum_m|F_{m,X}|^2
\]

and

\[
\boxed{
\mathcal X(X)
=
2\sum_{m<n}
\mu(m)\mu(n)F_{m,X}F_{n,X}.
}
\tag{L-95311.7}
\]

The diagonal \(\mathcal D\) is closed by (L-95311.5). The entire deterministic
OCHD obstruction is the distinct odd-core cross correlation
\(\mathcal X(X)\).


---

# R-95310 — Fibrewise passivity and diagonal energy do not prove OCHD

Claim ID: `R-95310`  
Status: **EXACT SOURCE-BLIND FIREWALL**  
Created: 2026-08-17  
Depends on: `L-95310/L-95311`; PR #563

On the interval

\[
\frac23\le x\le\frac34,
\]

all scaled terms \(W(2^rx)\) with \(r\ge1\) vanish. Hence

\[
K_0(x)=W(x),
\qquad
K_1(x)=0.
\tag{R-95310.1}
\]

On this interval,

\[
W(x)=\frac{x(1-x)(2x-1)}3
\ge\frac2{81}.
\tag{R-95310.2}
\]

Replace the actual Möbius signs temporarily by \(+1\) on the odd squarefree
cores in

\[
\frac{2X}{3}\le m\le\frac{3X}{4}.
\]

Every fibrewise state identity, passive norm and diagonal square estimate is
unchanged by this sign replacement. However the critical observation is at
least

\[
\frac2{81}
\sum_{\substack{2X/3\le m\le3X/4\\m\ {\rm odd\ squarefree}}}
\frac{\log m}{\sqrt m}
\gg
\sqrt X\log X,
\tag{R-95310.3}
\]

using the elementary positive density of odd squarefree integers.

At the same time its diagonal square is only \(O(\log^2X)\) on this block.

Therefore:

\[
\boxed{
\text{fibrewise passivity}
+
\text{polylog diagonal energy}
\not\Longrightarrow
\text{critical deterministic output control}.
}
\tag{R-95310.4}
\]

The actual Möbius signs, and specifically their cross-core cancellation, are
load bearing.


---

# T-95310 — Finite odd-core cross correlation is the corrected OCHD frontier

Claim ID: `T-95310`  
Status: **COMPLETE CONDITIONAL REDUCTION — CROSS-CORRELATION THEOREM OPEN**  
Created: 2026-08-17  
Depends on: `L-95310/L-95311`, `R-95310`; the centered-cubic Mellin consumer

Define the finite odd-core packet \(\mathcal C_e(X)\) by (L-95311.3).

A sufficient conclusion-producing theorem is:

> **Finite Odd-Core Cross Correlation (`FOCC`).**  
> For some fixed \(A\),
> \[
> |\mathcal X(X)|\le(\log(2X))^A
> \]
> for every sufficiently large \(X\).

Since the diagonal is already \(O(\log^3X)\), FOCC gives a polylogarithmic
bound for \(\mathcal C_e\). The stable inverse (L-95310.11) gives the same for
the original critical Q4 observation \(\mathcal C_d\).

The Mellin transform is multiplied only by the safe factor

\[
(1+2^{-s})^2,
\]

whose zeros lie on \(\Re s=0\). No hypothetical zeta pole with real part
greater than \(1/2\) is cancelled. The centered-cubic Mellin argument then
gives RH.

Thus

\[
\boxed{
\mathrm{FOCC}
\Longrightarrow
\mathrm{OCHD}
\Longrightarrow
\mathrm{RH}.
}
\]

This packet does not prove FOCC. It replaces the infinite dyadic/passive
formulation by one explicit six-band odd-squarefree correlation and closes its
entire diagonal sector.

```text
infinite dyadic state                  ELIMINATED AT CRITICAL SCALE
finite six-band odd-core packet        EXACT
stable preconditioner inverse          EXACT
same-core diagonal                     POLYLOG
randomized model                       POLYLOG RMS
source-blind sign argument             REFUTED
distinct odd-core correlation FOCC     OPEN / RH-BEARING
Riemann Hypothesis                     UNPROVEN
```


---

# M-95310 — Hostile review protocol for the finite odd-core Q4 successor

Review in this order:

1. `L-95310`: check the signs in `d4`, both factors of
   `epsilon+delta_2`, and the six coefficient pairs.
2. Check the physical scale factors
   `1, sqrt(2), 1/2` in the preconditioned observation.
3. `L-95311`: verify the finite kernels and distinguish diagonal energy from
   the deterministic square.
4. `R-95310`: retain the top-band sign-replacement firewall.
5. `T-95310`: treat FOCC as open.

Immediate falsifiers:

```text
one nonzero dyadic coefficient at depth >=6;
a missing logarithmic boundary coefficient B_r;
a preconditioner zero in Re(s)>0;
an unstable inverse coefficient;
a diagonal estimate promoted to a deterministic estimate;
an omission of distinct-core cross terms;
a claim that the replay proves FOCC or RH.
```


---

# Q4 continuation: finite odd-core preconditioning

The passive state of PR #563 can be converted at the critical \(1/\sqrt n\)
normalization into a literal finite packet.

Applying

\[
(\varepsilon+\delta_2)^{*2}
\]

to the logarithmic Q4 source cancels the dyadic denominator created by the
reciprocal state and its derivative. Every odd squarefree core then occupies
only the six levels

\[
m,2m,4m,8m,16m,32m.
\]

The preconditioner is stably invertible in critical scale because its
half-scale coefficient is \(2^{-1/2}<1\).

The complete same-core diagonal is \(O(\log^3X)\). The remaining theorem is
only the deterministic cross correlation between distinct odd squarefree
cores. A top-band sign-replacement example proves that no fibrewise passive or
diagonal argument can supply that cancellation.
