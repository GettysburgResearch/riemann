# Comparative exact-head review of PRs #519 and #523

## Freeze

```text
repository:       gfreund123/riemann
review cutoff:    2026-08-16T01:57:56Z
main at cutoff:   9c7538559d7f56c2914b39aed5a1fb3fbf7ce131

shared dependency:
PR #498           6cc0da2fa5711017e260ebdcea4ba8c22e453288

proposal A:
PR #519           fb15b598734546230aa51a16dda28488d214729f
branch:           research/gpt56-pro/93300-cubic-shell-balanced-dispersion
base:             PR #498 exact head

proposal B:
PR #523           f2e2e96c48285f59a8df807ba49122778cb10ff4
branch:           research/gpt56-pro/93300-critical-vaughan-heat-bridge
base:             PR #498 exact head
```

The two proposals are compared because they attack the same post-PR-#498 cubic
arithmetic obstruction. They are **not** treated as independent confirmation:
both inherit the same centered-Q4 projection, Mellin pole audit and RH-equivalent
criterion from PR #498. Every conclusion below is frozen to the exact heads
above.

The retained exact-rational replays were inspected. No prime-distribution
sweep, zero computation, large endpoint campaign or formal build was rerun. A
new small exact regression was produced for the normalization dictionary,
Vaughan signs, grouped Type-II coefficient and endpoint inversion.

## Executive verdict

```text
PR #519:
  VERIFIED WITH FIXES
  mathematical type:
    UNCONDITIONAL REDUCTION + OPEN RH-EQUIVALENT PRODUCER

PR #523, r=1 sector:
  SUPERSEDED / SCALAR-NORMALIZATION DUPLICATE OF PR #519

PR #523, r>=2 sector:
  VERIFIED WITH FIXES
  mathematical type:
    GENUINE HIGHER-ORDER EXTENSION + OPEN RH-EQUIVALENT PRODUCER

balanced dispersion / Type II:
  OPEN in both proposals

Riemann Hypothesis:
  UNPROVEN
```

The decisive comparison is exact:

\[
G_1(x)=x(1-x)(2x-1)=3K(x),
\]

and, with zero extension outside `[0,1]`,

\[
W_1(x)=G_1(x)-4G_1(4x)=3\bigl(K(x)-4K(4x)\bigr)=3F(x).
\]

Consequently

\[
A_1(N)=3\mathcal A_\circ(N)
\]

and, after the harmless exchange of the two hyperbola variables,

\[
B_1^\sharp(N)=3\mathcal B_N.
\]

Thus PR #523's `r=1` construction is not a second proof of PR #519. It is the
same cubic construction in a scalar normalization. Scalar multiplication by
three changes neither zero survival, square-root scale nor the open arithmetic
content.

The higher-order members `r>=2` are new. They increase the order of vanishing
at the origin and move the absolutely paid product boundary from `N^(3/4)` to

\[
N^{\eta_r},
\qquad
\eta_r=1-\frac1{2(r+1)}.
\]

They do not prove the remaining top-hyperbola Type-II estimate.

# 1. The shared PR #498 spine is one dependency

Both packets begin from the same identities:

\[
K(x)=\frac{x(1-x)(2x-1)}3,
\]

\[
\mathcal A_\circ(N)
 =\sum_{m\le N}c_\circ(m)K(m/N),
\]

\[
\widehat K(s)
 =\frac{s-1}{3(s+1)(s+2)(s+3)},
\]

and the centered-energy implication

\[
|\mathcal A_\circ(N)|^2
 \le \frac N{180}\mathscr V_\circ(N).
\]

The PR #498 Mellin transform retains every nontrivial open-strip zeta-zero
pole. Accordingly a square-root/polylogarithmic estimate for the scalar is
RH-equivalent. The comparison below does not count two descendants of this
common criterion as independent evidence for that criterion.

# 2. Native cubic normalization in PR #519

PR #519 defines

\[
F(x)=K(x)-4K(4x)\mathbf1_{x\le1/4}.
\]

The exact polynomial is

\[
F(x)=
\begin{cases}
170x^3-63x^2+5x,&0\le x\le1/4,\\
(-2x^3+3x^2-x)/3,&1/4<x\le1,\\
0,&\text{otherwise}.
\end{cases}
\]

At the join,

\[
F(1/4)=-1/32.
\]

Substitution in the complete Q4 source gives the exact reorganization

\[
\boxed{
\mathcal A_\circ(N)
=
\sum_{n\le N}\Lambda(n)F(n/N)
+
3(\log4)\sum_{4^a\le N}K(4^a/N).
}
\]

The factor-four gauge remains separate. Dropping it is a source error.

For one prime base,

\[
Z_{p,N}
=(\log p)\sum_{k:p^k\le N}F(p^k/N)
\]

for odd `p`, with the displayed gauge added to `p=2`.

## Prime-power compression

For `p<=sqrt(N)`, the complete tower has absolute size at most `log N` under
the coarse `|F|<=1` bound, so all such bases cost
`O(sqrt(N) log N)`. For `p>sqrt(N)`, only the first power can occur.
The gauge is `O(log N)`. Hence

\[
\boxed{
\mathcal A_\circ(N)
=
\sum_{\sqrt N<p\le N}(\log p)F(p/N)
+
O(\sqrt N\log N).
}
\]

This is a genuine unconditional reduction. It does not estimate the
large-prime shell.

# 3. PR #523 at `r=1` is exactly PR #519 times three

PR #523 defines

\[
G_r(x)=x^r(1-x)^r(2x-1),
\qquad
w_r=\frac12G_r',
\]

and

\[
W_r(x)=\frac1{r!}
\left[G_r(x)-4G_r(4x)\mathbf1_{x\le1/4}\right].
\]

For `r=1`,

\[
G_1=3K,
\qquad
w_1=3w,
\qquad
C_1=\int_0^1w_1^2=9/180=1/20,
\]

and

\[
\boxed{W_1=3F.}
\]

Its endpoint scalar is

\[
A_1(N)=\sum_{m\le N}c_\circ(m)G_1(m/N)
      =3\mathcal A_\circ(N).
\]

The source rewrite is likewise exactly tripled, including the gauge:

\[
A_1(N)
=
\sum_{n\le N}\Lambda(n)W_1(n/N)
+
3(\log4)\sum_{4^a\le N}G_1(4^a/N)
=
3\mathcal A_\circ(N).
\]

After Vaughan grouping, PR #519 uses

\[
a_U(m)\Lambda(\ell)F(m\ell/N),
\]

whereas PR #523 uses

\[
\Lambda(m)a_U(q)W_1(mq/N).
\]

Exchange `m` and `q` and insert `W_1=3F`. Their support sets coincide because
`m,q>N^(1/3)` and `mq<=N` automatically imply
`m,q<=N^(2/3)+O(1)`. Thus

\[
\boxed{B_1^\sharp=3\mathcal B_N.}
\]

This settles the normalization question exactly.

# 4. Mellin moments and wavelet signs

PR #519 has

\[
\widehat F(s)
=
(1-4^{1-s})
\frac{s-1}{3(s+1)(s+2)(s+3)}.
\]

PR #523 has

\[
\widehat G_r(s)
=
\frac{r!(s-1)}{\prod_{j=r}^{2r+1}(s+j)},
\]

and

\[
\widehat W_r(s)
=
(1-4^{1-s})
\frac{s-1}{\prod_{j=r}^{2r+1}(s+j)}.
\]

For `r=1`, this is `3 widehat F`, as required.

Every member has a double zero at `s=1`:

\[
\int_0^1W_r(x)\,dx=0,
\qquad
\int_0^1W_r(x)\log x\,dx=0.
\]

For the native cubic,

\[
\widehat F''(1)=\frac{\log4}{36}>0.
\]

The signs and scale-four coefficient are correct. The moments eliminate the
continuous constant and first logarithmic densities; they do not estimate the
prime discrepancy.

# 5. Exact Vaughan decomposition

Both packets use the same identity. With

\[
U=V=\lfloor N^{1/3}\rfloor,
\]

one has

\[
\boxed{
\Lambda
=
\Lambda_{\le V}
+
\mu_{\le U}*\log
-
\mu_{\le U}*\Lambda_{\le V}*1
+
\mu_{>U}*\Lambda_{>V}*1.
}
\]

The sign pattern is

```text
+ small-Lambda
+ mu-small * log
- mu-small * Lambda-small * 1
+ mu-large * Lambda-large * 1
```

or, after the ordering used in PR #523, `+,-,+,+`. These are the same identity,
not different conventions.

Grouping `m=dr` in the final term gives

\[
\boxed{
a_U(m)=\sum_{d\mid m,\ d>U}\mu(d).
}
\]

The strict inequality `d>U` is load bearing. Replacing it by `d>=U` changes
the Type-II coefficient when `U` divides `m`.

For the cubic,

\[
\mathcal T_N
=
\sum_{\substack{m>U,\ \ell>V\\m\ell\le N}}
a_U(m)\Lambda(\ell)F(m\ell/N).
\]

For order `r`, after exchanging variable names,

\[
B_r(N)
=
\sum_{\substack{m>V,\ q>U\\mq\le N}}
\Lambda(m)a_U(q)W_r(mq/N).
\]

These are exact finite identities.

# 6. Type-I bounds

The scaled cell estimates used by both packets are

\[
\sum_{n\le y}W_r(n/y)=O_r(y^{-1}),
\]

\[
\sum_{n\le y}(\log n)W_r(n/y)
=O_r(\log(2y)/y).
\]

For the cubic, the first estimate also has exact residue-class formulas modulo
four. The piecewise polynomial is continuous with zero endpoints and has only
finitely many derivative jumps, so piecewise Euler summation supplies the
stated uniform errors. The logarithmic version requires separating the first
cell near zero; the two Mellin moments remove the integral terms.

The three Type-I estimates then follow without Möbius cancellation:

\[
\Lambda_{\le V}:
\quad
O_r(N^{-(2r-1)/3}\log(2N))
\]

(the logarithm may be suppressed with a sharper Chebyshev moment),

\[
\mu_{\le U}*\log:
\quad
O_r(N^{-1/3}\log(2N)),
\]

and

\[
\mu_{\le U}*\Lambda_{\le V}*1:
\quad
O_r(N^{1/3}\log(2N)).
\]

PR #519 records the deliberately coarser combined bound
`O(N^(1/3) log N)`. PR #523 separates the powers more sharply. No
RH-strength prime error is used.

# 7. Safe Type-II range and the remaining open form

Since

\[
|a_U(q)|\le\tau(q),
\qquad
W_r(x)=O_r(x^r)\quad(x\downarrow0),
\]

the portion with `mq<=Y` obeys

\[
|B_r^{\le Y}(N)|
\ll_r
\frac{Y^{r+1}}{N^r}\log^2(2Y).
\]

Taking

\[
\eta_r=1-\frac1{2(r+1)}
\]

gives

\[
B_r^{\le N^{\eta_r}}(N)
=
O_r(\sqrt N\log^2(2N)).
\]

Thus the exact remaining form is

\[
\boxed{
B_r^\sharp(N)=
\sum_{\substack{
m,q>N^{1/3}\\
N^{\eta_r}<mq\le N
}}
\Lambda(m)a_U(q)W_r(mq/N).
}
\]

For `r=1`, `eta_1=3/4` and this is three times PR #519's BCD after exchanging
the variables. For `r=2`, `eta_2=5/6`. Larger fixed order pushes the
unresolved annulus closer to the top hyperbola.

Neither packet proves

\[
|B_r^\sharp(N)|\ll_r\sqrt N\log^A N.
\]

That estimate remains `OPEN / RH-EQUIVALENT`. Finite replays, diagonal
energies, block counts and coefficient-blind large-sieve inequalities do not
prove it.

# 8. Carrier formulas

PR #519 gives the line-one Mellin band-pass form

\[
\mathcal T_N
=
\frac1{2\pi}
\int_{\mathbb R}
\widehat F(c+it)N^{c+it}
A_U(c+it)L_V(c+it)\,dt.
\]

At `c=1`, the multiplier has a double zero at `t=0` and quadratic decay at
infinity.

PR #523 gives the critical-weight form

\[
\boxed{
B_r(N)
=
\frac{\sqrt N}{2\pi}
\int_{\mathbb R}
\widehat W_r(1/2+it)N^{it}
P_{V,N}(t)M_{U,N}(t)\,dt,
}
\]

where

\[
P_{V,N}(t)
=
\sum_{V<m\le N}\frac{\Lambda(m)}{m^{1/2+it}},
\]

\[
M_{U,N}(t)
=
\sum_{U<q\le N}\frac{a_U(q)}{q^{1/2+it}}.
\]

The support of `W_r` enforces `mq<=N`. The Fourier signs and the
`sqrt(N)` normalization are correct. The elementary diagonal estimates

\[
\sum_{m\le N}\frac{\Lambda(m)^2}m\ll\log^2N,
\qquad
\sum_{q\le N}\frac{|a_U(q)|^2}q\ll\log^4N
\]

do not bound the prescribed Fourier coefficient.

PR #519 additionally supplies an exact Calderon/First-Hermite heat
decomposition on the line `Re s=1`. This is route infrastructure, not a
transfer of the open one-carrier theorem.

# 9. Endpoint inversion

For any finitely supported sequence `c`, define

\[
A_c(N)=\sum_{m\le N}c(m)K(m/N),
\qquad
P_c(N)=3N^3A_c(N).
\]

PR #523's local inversion is exact:

\[
\boxed{
\Delta^3P_c(N)
=
(N+1)(N+2)[c(N+2)-c(N+1)].
}
\]

For one atom at `m`, `P_c(N)` is a quadratic polynomial in `N` after
activation and zero before activation. Its third difference is supported at
the two activation boundaries; summing those two contributions gives the
displayed adjacent-source difference.

This proves that the cubic transform loses no local finite source information.
It does not provide cancellation for the actual source.

# 10. Claim-identifier collision

The collision is repository-real, not cosmetic.

PR #523 committed its colliding claims first:

```text
R-93300 commit: 4bcca58c0596a5554e6bfed24261d3794fb0ba8b
time:           2026-08-16T00:28:24Z

L-93300 commit: 9681cd6d9416511768219e966971cfd910469b8d
time:           2026-08-16T00:28:46Z
```

PR #519's first `R-93300` and `L-93300` commits were later:

```text
R-93300 commit: bd953d293f58b40e6fb1a1e8749fc28f3d945fb7
time:           2026-08-16T01:17:58Z

L-93300 commit: 16d131fcec20d1550a188895ebfaae8de253924a
time:           2026-08-16T01:18:27Z
```

Therefore the canonical identifier ownership is:

```text
PR #523 retains:
R-93300
L-93300
L-93301 ... L-93304
R-93301
T-93300
O-93300
X-93300
```

PR #519 should be re-identified before integration:

```text
R-93300 -> R-93320
L-93300 -> L-93320
L-93301 -> L-93321
L-93302 -> L-93322
L-93303 -> L-93323
L-93304 -> L-93324
T-93305 -> T-93325
O-93300 -> O-93320
M-93300 -> M-93320
X-93300 -> X-93320
```

The mapping is normative for integration. Historical files should not be
silently rewritten; a reconciled successor should copy or rename them with
explicit provenance.

# 11. Canonical lineage recommendation

The recommended scientific lineage is:

```text
PR #498
  centered-Q4 cubic criterion; one shared dependency

-> PR #523's pre-existing 93300 identifier block
  owns the claim namespace and supplies the endpoint-order family

-> reconciled successor
  imports PR #519's native F-normalized cubic shell, exact mod-four formulas,
  additive dispersion and Calderon bridge under the 93320 identifiers;
  marks PR #523 r=1 as SCALAR-NORMALIZATION DUPLICATE;
  retains PR #523 r>=2, critical carrier and endpoint inversion.
```

This recommendation separates namespace ownership from mathematical
normalization. The cubic object used for arithmetic estimates should remain
the PR #498-native `F`; the higher-order family should state the dictionary
`W_1=3F` at its front door.

Do not merge PRs #519 and #523 independently into a common base. That would
create duplicate IDs and duplicate theorem claims while falsely resembling
independent confirmation.

# 12. Certificate audit

The retained PR #519 and PR #523 verifiers use exact rational finite fixtures.
They substantiate:

- polynomial and source reorganization;
- the scale-four factor;
- grid residue identities;
- the four-term Vaughan signs;
- the strict `d>U` coefficient;
- selected formal endpoint inversions;
- scope mutations.

They do not substantiate:

- a prime-distribution estimate;
- balanced Type-II cancellation;
- CPBD/BCD;
- First-Hermite one-carrier exclusion;
- RH.

The new review regression records

```text
PASS_PR519_PR523_PR520_EXACT_HEAD_REVIEW_ALGEBRA
```

and includes the exact normalization and endpoint-inversion checks. It is not
promoted beyond finite algebra.

# Final comparative status

| Object | Verdict | Surviving scope |
|---|---|---|
| PR #498 spine | `IMPORTED / ONE SHARED DEPENDENCY` | centered criterion and pole audit |
| PR #519 cubic wavelet | `VERIFIED WITH FIXES` | native cubic reduction |
| PR #519 Type I | `VERIFIED` | unconditional |
| PR #519 low-product Type II | `VERIFIED` | `ml<=N^(3/4)` |
| PR #519 BCD | `UNPROVEN / GAP` | exact RH-equivalent producer |
| PR #523 `r=1` | `SUPERSEDED` | exactly three times PR #519 |
| PR #523 `r>=2` | `VERIFIED WITH FIXES` | genuine higher-order extension |
| PR #523 Type I/deep product | `VERIFIED` | unconditional |
| PR #523 top-hyperbola Type II | `UNPROVEN / GAP` | RH-equivalent |
| PR #523 endpoint inversion | `VERIFIED` | exact finite identity |
| Riemann Hypothesis | `UNPROVEN` | no conclusion |
