# Parity-contractive annular factor-67 after hostile reconstruction

## A standalone reconstruction, exact refutation, corrected source recursion, and direct Mellin-Landau frontier

**Frozen primary target:** PR #565 at `339e3367660f40c74795802a6f8170b15e19b13a`  
**Mandatory adversarial inputs:** PR #574 at `74fba7f3e55fa9a53d1eb814e5067f5011ef5e86`; PR #575 at `265c481ebd02807ab7d9a95cb0cf905a22c1876f`  
**Scientific status:** strongest honest correction; **RH remains unproved**.

## Abstract

PR #565 proposed to prove eventual nonnegativity of a single scale-four annular scalar by combining a finite `P_61` signed-bias certificate, a factor-67 causal decomposition, exact low-child recombination, and a strict parity contraction. The proposed scalar has an exact reciprocal-zeta Mellin transform whose numerator cannot cancel a nontrivial zeta zero, so the downstream Landau consumer is unusually clean.

This manuscript reconstructs the entire chain from literal sources. Two independent failures occur before the consumer. First, the claimed universal finite bias

\[
\frac1{40}\le \frac{F(x)}{M(x)}\le\frac18\qquad(x\ge67)
\]

is false. A 256-bit MPFR enclosure at `x=184` gives

\[
\frac{F(184)}{M(184)}
=0.023984293558766304673\ldots<\frac1{40}.
\]

Second, and more importantly, the finite `P_61` packet and the full rough-history source cannot be identified at the point where the bias is used. If `P_x` denotes the finite packet, its signed scalar is `F(x)` but it does not contain the native rough histories. If it denotes the full source, the advertised current retains unresolved rough histories and is not controlled by `F/M`; moreover low-child recombination returns the same-rank full packet rather than a terminal packet. This is a source-type obstruction, not a small constant error.

We replace the broken tree by the exact all-history recursion, prove first-owner uniqueness, parity, coefficient preservation, base cases, and finite termination, and run the PR #561 odd-history witness through the literal construction. We then reconstruct the entire single-scalar annular Mellin-Landau consumer, including support, continuity, growth, Fubini, the factor `1-4^{-s}`, pole noncancellation, Landau's hypotheses, and the functional-equation finish.

The strongest surviving theorem is therefore fail-closed: eventual positivity of the literal all-history scalar implies RH, but neither the finite `P_61` bias nor the `<1/8` coefficient budget proves that positivity. The first open producer is the sign of one explicit finite Riesz sum, equivalently the deterministic all-history recursion stated below. No RH-equivalent assumption is silently imported.

---

## 1. Frozen inputs and notation discipline

The proof is frozen at exact Git heads before any reconstruction. The source ledger is deposited in

```text
audits/gpt56-pro/2026-08-17-frozen-source-ledger.tsv
```

and includes PRs #565, #547, #559, #561, #574, #575, #556, and #552. The critical distinction is between four quantities:

| symbol | object | sign | scope |
|---|---|---:|---|
| `B_x` | finite `P_61` parity-labelled source | positive source | small-prime colors only |
| `F(x)` | signed scalar observation of `B_x` | signed number | finite `P_61` packet |
| `M(x)` | unsigned mass of `B_x` | nonnegative | finite `P_61` packet |
| `N_j(x)` | complete source with all ordered rough histories from `p_j` onward | positive source | native rough source |
| `R_j(x)` | signed scalar observation of `N_j(x)` | signed number | complete source |
| `U_j(x)` | unsigned mass of `N_j(x)` | nonnegative | complete source |

Every later equation is typed in these variables. In particular, no display is allowed to replace `R_j,U_j` by `F,M` unless all unresolved rough histories have actually been removed.

### 1.1 The scale-four hinge and scalar base dictionary

For real `x>0` and integer `n>=1`, define

\[
H_x(n)=\min\!\left(\log4,\log\frac xn\right)_+.
\]

Thus `H_x(n)=0` for `x<=n`, it is the logarithmic ramp on `n<x<4n`, and it equals `log4` for `x>=4n`.

The positive `5:3` scalar dictionary from PR #559 is

\[
q_\star(2)=15,
\qquad q_\star(3)=6,
\qquad q_\star(4)=3,
\qquad q_\star(m)=6\quad(m\ge5).
\]

Define the unsieved positive packet mass

\[
A_\star(x)=\sum_{m\ge2}\frac{q_\star(m)}{\sqrt m}H_x(m).
\]

The sum is finite for every `x`.

### 1.2 The finite `P_61` packet

Let

\[
P_{61}=\prod_{p\le61}p.
\]

The positive parity-labelled finite source `B_x` contains, for each squarefree `d|P_61` and every `m>=2` with `dm<=x`, one atom of unsigned mass

\[
\frac{q_\star(m)}{\sqrt{dm}}H_x(dm)
\]

in the parity channel determined by `mu(d)`. Its signed scalar and unsigned mass are

\[
F(x)=\sum_{d\mid P_{61}}
\frac{\mu(d)}{\sqrt d}A_\star(x/d),
\]

\[
M(x)=\sum_{d\mid P_{61}}
\frac1{\sqrt d}A_\star(x/d).
\]

These are exact finite quantities. They are not the full native annular scalar or full native source mass.

### 1.3 The complete scalar

Let `c_X(j)` denote the complete native component row. The scalar of interest is

\[
R_X=5c_X(2)+3c_X(3).
\]

Its scale-four annulus is

\[
A_X=R_X-R_{X/4}.
\]

The exact coefficient formula is

\[
A_X=\sum_{n\le X}\frac{a_\star(n)}{\sqrt n}H_X(n),
\]

where

\[
a_\star(n)=6\mathbf1_{n=1}-6\mu(n)
+9\mathbf1_{2\mid n}\mu(n/2)
-3\mathbf1_{4\mid n}\mu(n/4).
\]

This is the quantity that the arithmetic producer must make nonnegative.

---

## 2. Statement-to-use audit

The most important audit table is not a theorem list but a statement-to-use table. It records the exact gap between what each object says and what the composition needs.

| interface | certified or written statement | use in PR #565 | result |
|---|---|---|---|
| finite bias | asserted `1/40 <= F/M <= 1/8` | used universally | false at `x=184` |
| one-prime current | finite packet minus a placed finite child | treated as every full-source current | type mismatch |
| low child | exact cancellation to `lambda P_x` | treated as a terminal rank reduction | same full packet returns |
| recursive mass | raw `sum alpha_i<1/8` | used against finite `M(x)` | wrong object and missing normalized source equation |
| parity | each rough prime flips sign | retained for children | correct but insufficient |
| scalar | `5c_2+3c_3` has positive base dictionary | used instead of two rows | legitimate scalar simplification |
| Hall | no Hall is displayed | implicit physical feasibility sometimes suggested | forbidden unless full PR #574/#575 LP is solved |
| consumer | fixed scalar Mellin transform | Landau finish | independently correct |

The two failures below are independent. Correcting the constant does not correct the source type, and correcting the source type does not prove a universal finite bias.

---

## 3. Exact falsification of the universal `P_61` lower bias

### 3.1 Continuum structure

For fixed finite `P_61`, both `F(x)` and `M(x)` are continuous. Every source term enters at `x=dm` with logarithmic value zero and reaches its plateau at `x=4dm`. Between consecutive activation knots, both functions are affine in `log x`. Therefore a continuum certificate can be finite only if it covers every knot and controls the fractional-linear ratio on every interval with outward rounding.

The retained PR #565 replay explicitly reported that the directed certificate was not replayed there. We therefore rebuilt the finite sums directly.

### 3.2 The endpoint `x=184`

At `x=184`, only divisors `d|P_61` with `2d<=184` occur. Expanding the finite packet gives exactly 611 nonzero `(d,m)` terms. The independent verifier uses MPFR 4.2.2 at 256 bits and `RNDD/RNDU` for every square root, logarithm, division, multiplication, and signed accumulation.

It proves

\[
F(184)\in
[10.69357964877382995080531550498546444404,\
 10.69357964877382995080531550498546444405],
\]

\[
M(184)\in
[445.85760354260283631557807730110764267277,\
 445.85760354260283631557807730110764267278].
\]

Consequently

\[
\frac{F(184)}{M(184)}
\in
[0.02398429355876630467327315865313747748,\
 0.02398429355876630467327315865313747749].
\]

The direct separating inequality is

\[
40F(184)-M(184)
<-18.1144175916496382833<0.
\]

Hence

\[
\boxed{
\frac{F(184)}{M(184)}<\frac1{40}.
}
\]

This is an exact matching contradiction to `L-97100` as used by PR #565.

The same enclosure gives

\[
50F(184)-M(184)>88.82,
\qquad
20F(184)-M(184)<-231.98,
\]

so the local ratio lies between `1/50` and `1/20`. A diagnostic scan suggests that interval may hold much more widely, but no universal theorem is inferred from a finite scan.

### 3.3 Why merely replacing the constants is not a proof

If one assumes, only formally,

\[
\frac1{50}\le\frac{F}{M}\le\frac1{20}
\]

and a normalized recursive mass at most `1/8`, then the advertised rational algebra would have room:

\[
u_{\rm cur}
=\frac1{20}\frac{1+1/8}{1-1/8}
=\frac9{140},
\]

\[
\frac1{50}\left(1-\frac18\right)
-\frac9{140}\frac18
=\frac{53}{5600}>0.
\]

This is a valid conditional calculation. It is not a repaired theorem because the full currents are not finite packets controlled by `F/M`.

---

## 4. Literal all-history source recursion

### 4.1 Ordered rough histories

List the rough primes

\[
67=p_1<p_2<p_3<\cdots.
\]

Every squarefree integer has a unique factorization

\[
k=d p_{i_1}\cdots p_{i_r},
\qquad d\mid P_{61},
\qquad i_1<\cdots<i_r.
\]

The ordered tuple is the rough history. Its parity contribution is `(-1)^r`.

Let `S` swap the two positive parity channels. Define `N_j(x)` to be the positive source containing all atoms with:

- one small color `d|P_61`;
- an ordered rough history with every index at least `j`;
- one base index `m>=2`;
- activation `d p_{i_1}...p_{i_r}m<=x`;
- unsigned weight

\[
\frac{q_\star(m)}{\sqrt{d p_{i_1}\cdots p_{i_r}m}}
H_x(d p_{i_1}\cdots p_{i_r}m);
\]

- parity `mu(d)(-1)^r`.

The source is finite for every fixed `x`, since a history of length `r` has product at least `2*67^r`.

### 4.2 Exact first-owner identity

Every atom of `N_j(x)` either has empty rough history, hence belongs to `B_x`, or has a unique least rough prime `p_k`, `k>=j`. Removing `p_k` gives an atom of `N_{k+1}(x/p_k)`. Conversely, placing `p_k` restores the atom. The scale covariance is exact:

\[
p_k^{-1/2}
\frac{q_\star(m)H_{x/p_k}(n)}{\sqrt n}
=
rac{q_\star(m)H_x(p_kn)}{\sqrt{p_kn}}.
\]

Therefore

\[
\boxed{
N_j(x)=B_x\oplus
\bigoplus_{\substack{k\ge j\\p_k\le x/2}}
 p_k^{-1/2}S N_{k+1}(x/p_k).
}
\]

This is a disjoint direct sum. It proves first-owner uniqueness, coefficient preservation, cumulative parity, exact source normalization, and finite termination.

Let `R_j(x)` be the signed scalar and `U_j(x)` the unsigned mass. Then

\[
\boxed{
R_j(x)=F(x)-
\sum_{\substack{k\ge j\\p_k\le x/2}}
 p_k^{-1/2}R_{k+1}(x/p_k),
}
\]

\[
\boxed{
U_j(x)=M(x)+
\sum_{\substack{k\ge j\\p_k\le x/2}}
 p_k^{-1/2}U_{k+1}(x/p_k).
}
\]

When `x<2p_j`, the sum is empty and the exact base is `(R_j,U_j)=(F,M)`. The full native scalar is

\[
A_X=R_1(X).
\]

### 4.3 Coefficient cross-check

Each squarefree integer `k` has unique small color and rough history, with sign

\[
\mu(d)(-1)^r=\mu(k).
\]

Convolving the resulting squarefree coefficient with the positive base dictionary gives exactly the coefficient `a_star(n)` from Section 1. Thus the all-history recursion and the direct Riesz formula are identical.

---

## 5. Source-type no-go for the frozen contraction

PR #565 uses a packet `P_x` both as the root of the complete source tree and as an object whose current is controlled by `F/M`. Those requirements are incompatible.

### 5.1 Finite interpretation

If `P_x=B_x`, then

\[
B_x-p^{-1/2}SB_{x/p}
\]

is a positive finite packet, and a finite `F/M` theorem would be typed. But the root scalar is only `F(x)`, not the native `A_x`; every nonempty rough history is absent.

### 5.2 Full interpretation

If `P_x=N_j(x)`, then the root scalar is native. But the current

\[
N_j(x)-p_j^{-1/2}S N_{j+1}(x/p_j)
\]

contains the base packet together with all histories whose first rough prime is larger than `p_j`. Its scalar and mass are not `F(x)` and `M(x)`. The finite certificate does not apply.

### 5.3 Low-child recombination returns the same packet

For `alpha=lambda p^{-1/2}`,

\[
\lambda(P_x-p^{-1/2}SP_{x/p})
+
\alpha SP_{x/p}
=
\lambda P_x.
\]

This is exact. If `P_x` is full, it returns the same full packet at the same scale and with all unresolved histories. It is not rank descent or terminalization. If `P_x` is finite, it remains non-native.

### 5.4 Rough-child mass

The raw coefficient sum `<1/8` is not by itself an actual normalized source-mass theorem. The normalized statement requires the actual child source masses and survivor denominator, as emphasized by PR #575. More importantly, no coefficient or mass statement supplies the missing signed full-current cone.

---

## 6. The `X=61841` odd-history witness

PR #561 considers

\[
X=67\cdot71\cdot13=61841,
\]

with incoming history `(67)` and the next terminal parameters `(71,13)`. The history is odd, so the canonical target orientation is reversed. A directed certificate shows the canonical target surplus exceeds 17, making the reversed local Hall map impossible.

The exact all-history scalar at this endpoint decomposes by rough depth. A deterministic diagnostic gives

| contribution | value |
|---|---:|
| finite `P_61` base | `+387.576553051377...` |
| all odd one-prime histories | `-408.909828960219...` |
| all even two-prime histories | `+30.867932911878...` |
| total | `+9.534657003037...` |
| direct Riesz formula | `+9.534657003031...` |

The specific history `(67)` contributes approximately

\[
-67^{-1/2}F(923)=-6.09839539048\ldots,
\]

while the specific even continuation `(67,71)` contributes

\[
(67\cdot71)^{-1/2}F(13)=0.16698471655\ldots.
\]

These numbers are diagnostics, not a proof of global positivity. They show exactly where the odd history lives.

At the node `x=923`, the proposed low-child recombination for `p=71` is

\[
\lambda(N_{923}-71^{-1/2}SN_{13})
+
\lambda71^{-1/2}SN_{13}
=
\lambda N_{923}.
\]

The witness is not erased; the same full node returns. Any construction that then applies the finite `P_61` bias to `lambda N_923` has changed the packet type. The corrected recursion retains the odd contribution until the complete alternating scalar is formed.

---

## 7. Response to PRs #574 and #575

### 7.1 Global Hall findings

PR #574 proves that checkerboard inequalities, local determinant signs, and Cauchy-Binet expansions do not establish a global one-use Hall allocation. A genuine physical packing must solve the complete primal problem with target, score, every row, first moments, and ownership, or provide a dual certificate.

The corrected scalar frontier does not claim a physical packing. It evaluates the signed scalar of the literal source directly. Therefore the global Hall LP is genuinely inapplicable to the scalar theorem itself. It becomes mandatory again if one attempts to convert the scalar proof into a positive row or source realization.

### 7.2 Scalar lift

PR #575 proves that scalar exactness does not lift to two-row positivity. The counterexample is elementary: `(r_2,r_3)=(1,-1)` has positive `5:3` scalar equal to 2 while the third row is negative.

This manuscript accepts the distinction. Its consumer is the single scalar transform. It makes no inference that either component row is nonnegative.

### 7.3 Parity and ownership

Both adversarial PRs require cumulative history parity and one-use ownership. The exact recursion in Section 4 incorporates both directly. No parity label is stored and then ignored at terminal use.

A complete response matrix is deposited in

```text
audits/gpt56-pro/2026-08-17-pr574-pr575-response.tsv
```

---

## 8. Complete annular Mellin-Landau consumer

The downstream consumer survives and can be proved without project notation.

### 8.1 Coefficients and support

Define

\[
a_\star(n)=6\mathbf1_{n=1}-6\mu(n)
+9\mathbf1_{2\mid n}\mu(n/2)
-3\mathbf1_{4\mid n}\mu(n/4).
\]

Set

\[
R_X=\sum_{n\le X}
\frac{a_\star(n)}{\sqrt n}\log\frac Xn,
\]

and put `R_X=0` for `0<X<1`. Then

\[
A_X=R_X-R_{X/4}.
\]

The below-support convention is now explicit.

### 8.2 Continuity and knots

At an ordinary knot `X=n`, the entering term has `log(X/n)=0`. At a scale-four knot `X=4n`, the entering term of `R_{X/4}` has `log((X/4)/n)=0`. Hence `R_X` and `A_X` are continuous from both sides at every knot.

Between knots, the active sets are fixed and both functions are affine in `log X`. This justifies integer-knot reductions for diagnostics, but it does not prove positivity.

### 8.3 Growth and Fubini

The coefficients satisfy `|a_star(n)|<=24`. Therefore

\[
|R_X|
\le24\sum_{n\le X}n^{-1/2}\log(X/n)
=O(\sqrt X),
\]

and the same holds for `A_X`. The Mellin integral converges absolutely for `Re s>1/2`.

For `n>=1` and `Re s>0`,

\[
\int_n^\infty
\log(X/n)X^{-s-1}\,dX
=\frac{n^{-s}}{s^2}.
\]

Absolute convergence for `Re s>1/2` permits Fubini.

### 8.4 Dirichlet numerator

With `z=s+1/2`,

\[
\sum_{n\ge1}\frac{a_\star(n)}{n^z}
=6-
\frac{3(1-2^{-z})(2-2^{-z})}{\zeta(z)}.
\]

Thus

\[
\int_1^\infty R_XX^{-s-1}\,dX
=\frac6{s^2}
-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
\]

Since `R_Y=0` below support, the substitution `X=4Y` gives

\[
\int_1^\infty R_{X/4}X^{-s-1}\,dX
=4^{-s}
\int_1^\infty R_YY^{-s-1}\,dY.
\]

Therefore

\[
\boxed{
\int_1^\infty A_XX^{-s-1}\,dX
=(1-4^{-s})
\left[
\frac6{s^2}
-
\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}
\right].
}
\]

### 8.5 Noncancellation

If `Re s>0`, then

\[
|4^{-s}|=4^{-\Re s}<1,
\]

so `1-4^{-s}` is nonzero.

The finite reciprocal-zeta numerator vanishes only if

\[
2^{-z}=1
\quad\text{or}\quad
2^{-z}=2.
\]

The first equality forces `Re z=0`; the second forces `Re z=-1`. Neither can occur at a nontrivial zeta zero in `0<Re z<1`.

### 8.6 Landau's theorem

Assume `A_X>=0` for all sufficiently large `X`. Removing a compact initial interval changes the Mellin transform by an entire function. Put `X=e^t`; the remaining Mellin transform is the Laplace transform of a nonnegative locally integrable function with finite abscissa of convergence.

Landau's real-abscissa theorem says that a finite abscissa is a singularity on the real axis. The displayed meromorphic continuation has no singularity on the positive real axis: `1/zeta(s+1/2)` vanishes rather than blows up at `s=1/2`, and zeta has no positive real zero. Hence the abscissa is at most zero and the transform is analytic throughout `Re s>0`.

If zeta had a zero `rho` with `Re rho>1/2`, then `s=rho-1/2` would lie in `Re s>0`; the noncancellation result would force a pole of the transform there, contradiction. The functional equation maps a zero with `Re rho<1/2` to one with real part greater than `1/2`. Therefore eventual scalar positivity implies RH.

---

## 9. Strongest honest corrected theorem

The exact producer is now a single statement:

\[
\boxed{
R_1(X)=
5[c_X(2)-c_{X/4}(2)]
+3[c_X(3)-c_{X/4}(3)]
\ge0
}
\]

for all sufficiently large `X`, where `R_1` is the literal all-history recursion of Section 4.

This statement is not proved by:

- the false `1/40` finite bias;
- a putative replacement finite bias interval;
- the raw coefficient sum `<1/8`;
- low-child recombination;
- local Target-Lorenz signs;
- scalar exactness at a terminal leaf;
- finite scans.

A useful exact conditional cone theorem remains. Suppose every full-source current in a normalized causal decomposition satisfies

\[
a\,m(D)\le f(D)\le b\,m(D),
\]

and the normalized recursively swapped child mass is at most `rho`, with

\[
a(1-\rho)>b\rho.
\]

Then the parent scalar is positive. This is an exact contraction lemma, but the required current cone is a global all-history statement. PR #565 supplied only the finite base cone.

The first unsupported arrow is therefore sharply identified:

\[
\boxed{
\text{finite }P_{61}\text{ bias}
\not\Longrightarrow
\text{full-source current bias}.
}
\]

---

## 10. Independent implementation and mutation suite

The independent implementation was written only after the source contracts above were fixed. It contains:

1. a 256-bit MPFR verifier for the exact `x=184` counterexample;
2. an independent finite-source implementation of `F` and `M`;
3. a direct full Riesz implementation of the scalar;
4. an ordered rough-history decomposition at `X=61841`;
5. exact rational checks of the formal repaired constants;
6. scalar numerator factorization;
7. mutation tests for every load-bearing interface.

The retained result is

```text
PASS_HOSTILE_RECONSTRUCTION_AND_FAIL_CLOSED_FRONTIER
3ebf273d143b4ee1924cb9bee3e7096b5f15c92d7692926938a4e3f1a9a8ad87
```

The following mutations are rejected:

```text
stale lower bound 1/40;
finite P61 packet called the full native source;
low-child recombination called rank descent;
parity-blind terminalization;
positive scalar lifted to two rows;
local Hall signs called global feasibility;
omission of the factor 1-4^{-s};
a finite scan called a universal proof.
```

The `X=61841` history decomposition is diagnostic. The MPFR `x=184` enclosure is a finite proof object. Neither computation proves the open universal scalar sign.

---

## 11. RH status and research frontier

The manuscript closes every downstream analytic interface but falsifies the proposed arithmetic producer. No theorem in the reconstructed chain supplies zero-free-strip strength unconditionally.

```text
finite P61 lower bias 1/40              FALSE
universal corrected P61 bias            OPEN
all-history parity/source recursion      PROVED EXACT
PR565 parity contraction                 INVALID COMPOSITION
single-scalar Mellin transform           PROVED EXACT
pole noncancellation                     PROVED EXACT
Landau implication                       PROVED CONDITIONAL
global scalar annular positivity         OPEN / RH-BEARING
Riemann Hypothesis                       UNPROVED
```

The strongest honest successor is therefore a complete fail-closed reduction, not a proof announcement. A future closure must prove the literal alternating rough-history scalar directly or construct a global source-complete certificate satisfying the PR #574/#575 contracts. It may not reuse the finite bias certificate at a full-current interface.
