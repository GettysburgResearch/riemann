# LEMMA A (CAP-A) — Single-pair count cap: extra(G) <= 6

Status: PROVED (under the fattened single-pair hypothesis (H1) below). RH not addressed.
Depends on: L-105061 §2 ([I-PF], proved), L-105062 §1 (Hadamard product).
Fattening constant: `R4 := 2 + sqrt(3) (= 3.7320508...)`.
Numerics: scan3.py / scan4.py in this directory (23,640 configs, 0 violations, max extra = 2).

## 0. Setting

`F` real entire, order <= 1, `F(t) = c t^{m0} prod_nu (1 - t^2/tau_nu^2)` (absolutely
locally-uniformly convergent; L-105062 §1). Real zeros `{t_n}` (mult `m_n`), non-real
conjugate pairs `{x_j ± i y_j}` (`0 < y_j <= 1/2`, mult `m_j`). Gap `G = (a,b)` a bounded
component of `R \ {real zeros}`, `g = |G|`. `h := F'/F`, analytic on `G`. By [I-PF]
(L-105061 Lemma 2.1), on `G`:

```
h'(t) = -B(t) + Sum_j m_j phi'_j(t),   B(t) = m0/t^2 + Sum_n m_n/(t-t_n)^2,
phi'_j(t) = 2(y_j^2 - (t-x_j)^2)/((t-x_j)^2 + y_j^2)^2,
```

absolutely locally uniformly convergent, hence (Weierstrass) differentiable termwise
to every order on `G`.

For a pair `j` define the **fattened interval** `Itilde_j := (x_j - R4 y_j, x_j + R4 y_j)`
(it contains the overhang interval `I_j = (x_j - y_j, x_j + y_j)` since `R4 > 1`).

## 1. Statement

**Lemma A.** Suppose

> **(H1)** at most one pair — call it `(x, y)`, multiplicity `m1 >= 1` — has
> `Itilde ∩ G ≠ ∅`; every other pair `j` satisfies `Itilde_j ∩ G = ∅`.

Then

```
extra(G) := #{real zeros of F' in G, with multiplicity} - 1  <=  6  =: C_A ,
```

and moreover `Z_mult(h', G) <= 6`, all zeros of `h'` in `G` lying in `I ∩ G`,
`I = (x - y, x + y)`. If additionally the pair does not overhang `G`
(`I ∩ G = ∅`), or no pair touches at all, then `extra(G) <= 0`.

`C_A = 6` is absolute (independent of `F`, `G`, `m1`, all multiplicities and positions).
Empirical sharp value: 2 (§5). The hypothesis "exactly one pair overhangs, all others
`R4`-far" is a fattened-interval single-pair hypothesis; L-105061 §1 accepts fattened
overhang shapes verbatim downstream.

## 2. Calculus of the dipole profile (exact; verified symbolically)

Write `f(s) := 2(y^2 - s^2)/(s^2 + y^2)^2`, `s = t - x`, so `phi'(t) = f(t - x)`;
`f` is even. All claims reduce by homogeneity (`s -> s/y`) to `y = 1` and are pure
factorization (sympy-verified, scan directory):

```
f'(s)    =  4 s (s^2 - 3y^2) / (s^2+y^2)^3
f''(s)   = -12 (s^4 - 6 s^2 y^2 + y^4) / (s^2+y^2)^4
f''''(s) = -240 (s^2 - y^2)(s^2 - 4sy + y^2)(s^2 + 4sy + y^2) / (s^2+y^2)^6
```

Sign tables (all strict on the open regions):

- `f > 0` iff `|s| < y`; `f <= 0` for `|s| >= y`.
- `f'' < 0` on `|s| < (sqrt2 - 1) y` and on `|s| > (sqrt2 + 1) y`;
  `f'' > 0` on `(sqrt2 - 1) y < |s| < (sqrt2 + 1) y` (roots `|s| = (sqrt2 ∓ 1) y`).
- `f'''' > 0` on `|s| < (2 - sqrt3) y`; `f'''' < 0` on `(2 - sqrt3) y < |s| < y`;
  `f'''' > 0` on `y < |s| < (2 + sqrt3) y`; `f'''' < 0` on `|s| > (2 + sqrt3) y`
  (roots `|s| ∈ {(2 - sqrt3) y, y, (2 + sqrt3) y}`; note `2 - sqrt3 = 1/R4`).

Since `2 + sqrt3 > sqrt2 + 1 > 1`, **beyond radius `R4 y`, simultaneously
`f <= 0`, `f'' <= 0`, `f'''' <= 0`** (strictly for `|s| > R4 y`). This is what `R4` is for.

## 3. The comparison function Q

Define on `G`:

```
Q(t) := B(t) - Sum_{other pairs j} m_j phi'_j(t),   so   h' = g := m1 f(t - x) - Q(t).
```

**Lemma 3.1.** Under (H1), on `G`: `Q > 0`, `Q'' > 0`, `Q'''' > 0`.

*Proof.* Termwise (legitimate by absolute locally-uniform convergence + Weierstrass).
For `c` a real zero: `(t-c)^{-2} > 0`, `d^2/dt^2 (t-c)^{-2} = 6 (t-c)^{-4} > 0`,
`d^4/dt^4 (t-c)^{-2} = 120 (t-c)^{-6} > 0`; likewise `m0/t^2` (the origin is a real zero
or `m0 = 0`, so `0 ∉ G`). For each other pair `j`: (H1) gives `|t - x_j| >= R4 y_j` for
all `t ∈ G`, hence by §2 `-phi'_j >= 0`, `-(phi'_j)'' >= 0`, `-(phi'_j)'''' >= 0` on `G`.
Summing, each derivative of `Q` in question is `>=` the corresponding derivative of `B`,
which is a nonempty sum of strictly positive terms (`a, b` are real zeros). QED.

**Lemma 3.2 (localization).** Every zero of `h'` in `G` lies in `I ∩ G`,
`I = (x - y, x + y)`. In particular if `I ∩ G = ∅` (no overhang, or no pair at all,
in which case `g = -Q`), `h'` has no zero in `G`, `h` is strictly decreasing through
its single simple zero on `G` (as `h: +∞ -> -∞`), and `extra(G) = 0`.

*Proof.* At a zero, `m1 f(t - x) = Q(t) > 0` (Lemma 3.1), and `f > 0` iff `|t - x| < y` (§2).
For the addendum: `g = m1 f - Q < 0` on `G` when `f <= 0` on `G`; `h` analytic on `G` with
`h -> +∞` at `a+`, `-∞` at `b-` (double poles of `h'`, simple poles of `h` at the endpoint
zeros) and `h' < 0`: exactly one zero, simple. QED.

## 4. Proof of Lemma A

Assume `J := I ∩ G ≠ ∅` (else done by Lemma 3.2). `J` is an open interval;
`g = m1 f(· - x) - Q` is real-analytic on `G`.

**Step 1 (finiteness).** `g` and `h` have finitely many zeros in `G`. Near `a+`,
`h'(t) = -m_a (t-a)^{-2}(1 + o(1)) -> -∞` and `h(t) = m_a (t-a)^{-1}(1+o(1)) -> +∞`
(where `m_a` = mult of the zero at `a`; the remaining series is bounded near `a` by
local-uniform convergence), symmetrically at `b-`: both are zero-free near `∂G`.
An interior accumulation point of zeros would force the real-analytic function to
vanish identically on `G`, contradicting the endpoint blow-up. Same for `g''`
(`g'' -> -∞` at `∂G` since `Q'' >= B'' -> +∞` while `m1 f''` stays bounded on
compacta of `R`... more simply: `g''` real-analytic, and its zeros lie in the compact
set where `g''` is not dominated; interior accumulation again forces `g'' ≡ 0`,
impossible since `g'' < 0` near `a+`).

**Step 2 (Rolle with multiplicity).** For `psi` real-analytic with finitely many zeros
on an interval `J`: `Z_mult(psi, J) <= Z_mult(psi', J) + 1`. *Proof:* distinct zeros
`u_1 < ... < u_r`, mults `mu_i`; `psi'` has a zero of mult `mu_i - 1` at `u_i` and, by
Rolle, at least one zero in each `(u_i, u_{i+1})`; these are distinct locations, so
`Z_mult(psi', J) >= Sum (mu_i - 1) + (r - 1) = Z_mult(psi, J) - 1`.

**Step 3 (count of `g''` on `J`): `Z_mult(g'', J) <= 4`.** Partition `J` by the two
points `x ± (2 - sqrt3) y` into at most three open pieces `J_L, C, J_R`
(`C = J ∩ {|s| < (2 - sqrt3) y}`, `J_{L,R} = J ∩ {(2 - sqrt3) y < ∓s ... < y}`... i.e.
the left and right pieces of `J` with `(2 - sqrt3) y < |s| < y`).

- On `C`: `|s| < (2 - sqrt3) y < (sqrt2 - 1) y`, so `f'' < 0` (§2), hence
  `g'' = m1 f'' - Q'' < 0` (Lemma 3.1): **no zeros**. The partition points themselves
  satisfy `|s| = (2 - sqrt3) y < (sqrt2 - 1) y`, so `g'' < 0` there too: no zeros are
  lost at the cuts.
- On `J_L` and on `J_R`: `(2 - sqrt3) y < |s| < y`, so `f'''' < 0` strictly (§2), hence
  `g'''' = m1 f'''' - Q'''' < 0` (Lemma 3.1): `g''` is **strictly concave** on the piece.
  A strictly concave function `psi` (here `psi = g''`, `psi'' = g'''' < 0`) has
  `Z_mult(psi) <= 2` on an interval: three distinct zeros `u < v < w` are impossible
  (`psi(u) = psi(w) = 0` forces `psi > 0` on `(u,w)`); a multiple zero `u`
  (`psi(u) = psi'(u) = 0`) has `psi(t) < psi(u) + psi'(u)(t-u) = 0` for `t ≠ u`
  (strict concavity), so it is the only zero, and its multiplicity is exactly 2
  because `psi''(u) < 0`. So each piece carries at most 2 zeros with multiplicity.

Total: `Z_mult(g'', J) <= 0 + 2 + 2 = 4`.

**Step 4 (assembly).** By Step 2 applied twice on `J`. (Finiteness patch,
hostile review: Step 1 establishes finiteness for `g` and `g''` but Step 2
is also applied to `g'`; `g'` too has finitely many zeros in `J`, since
`Z_mult(g'', J) <= 4` is sign-based and unconditional (Step 3), so
infinitely many zeros of `g'` would produce, by Rolle, infinitely many
zeros of `g''` — contradiction.) Then:

```
Z_mult(h', G) = Z_mult(g, J)            [Lemma 3.2]
             <= Z_mult(g', J) + 1
             <= Z_mult(g'', J) + 2 <= 6.
```

Real zeros of `F'` in `G` are exactly the zeros of `h = F'/F` there, with the same
multiplicities (`F ≠ 0` on `G`). By Step 2 applied to `h` on `G` (finiteness, Step 1):
`Z_mult(h, G) <= Z_mult(h', G) + 1 <= 7`. Hence

```
extra(G) = Z_mult(h, G) - 1 <= Z_mult(h', G) <= 6.   QED
```

**Remarks.** (i) `m1` enters only through the positive factor `m1` multiplying `f`,
`f''`, `f''''`; every sign argument is invariant, so general multiplicity (= `m1`
copies of one pair) is covered with the same constant. (ii) The regress obstruction
(L-105061 §5(ii)) is evaded because the localization `Q > 0 ⇒ zeros ⊂ I` confines the
count to `|s| < y`, where `f''''` has the single fixed-sign trouble core
`|s| < (2 - sqrt3) y` — and there `f'' < 0` already kills `g''`. The 4th-derivative
positivity band `y < |s| < (2 + sqrt3) y` of `f` lies wholly outside `I`.
(iii) Only derivatives of order 0, 2, 4 of the other-pair profiles are used, which is
why the single fattening radius `R4 = 2 + sqrt3` (the largest root among levels 0, 2, 4)
suffices; no unbounded level escalation occurs.

## 5. Numerical confirmation (this directory: scan3.py, scan4.py)

Instances: finite real polynomial configurations (for which [I-PF] is exact algebra):
`h(t) = Sum 1/(t - t_n) + Sum m_j 2(t - x_j)/((t - x_j)^2 + y_j^2)`.

- **Grid scan** (scan3.py): 18,144 configs — `g ∈ {0.1, 0.5, 1, 2}`; 7 background
  families (bare gap; right cluster; asymmetric neighbor; double and triple endpoint
  zeros; flanking near zeros; far + near mixed), optional `R4`-far extra pair on either
  side; `y ∈ {0.01, ..., 0.5}`; 12 pair positions from non-overhang through center to
  beyond `b`; `m1 ∈ {1, 2, 5}`. Result: **max extra = 2, max `Z(h', G)` = 2, zero
  configs with extra > 2**; the maximizer (`g = 0.1`, bare gap, `x = 0.01`, `y = 0.01`,
  `m1 = 5`) re-verified in mpmath (30 dps).
- **Adversarial + random** (scan4.py): 2,496 endpoint-hugging / tiny-`y` (`0.001`) /
  high-`m1` (to 50) / stacked-endpoint-multiplicity configs plus 3,000 random configs
  (log-uniform `g`, `y`, background offsets): **max extra = 2, max `Z(h') = 2`**.
- Precision discipline: float64 produced spurious counts (13 fake sign changes of a
  near-cancelling symmetric `h`, with `Z(h') = 0` — parity-impossible), reproducing the
  L-105061 §4 incident; eliminated by a cancellation-aware filter
  (`|h| > 10^{-11} Sum |terms|`) with mpmath re-verification of every flagged or
  extremal config. Zero genuine flags.

**Confirmed: the proved cap `C_A = 6` is never approached; observed sharp value 2.**

## 6. Interface notes for the assembly

- Weight compatibility: the pair in Lemma A overhangs `G` in the fattened sense; if it
  overhangs in the original sense the L-105061 threshold weight applies as-is, and the
  additive form `extra <= 6 <= 6 * W(G)` holds on gaps with `W(G) >= 1` — which by
  Corollary 3.4 (safety net) are the only gaps needing a cap. If the pair only
  `R4`-touches without overhanging, Lemma A gives `extra = 0` outright, so no weight
  is even consumed.
- What Lemma A does **not** cover: two or more pairs with intersecting fattened
  intervals on the same gap (cooperation case) — that is CAP-B territory; (H1) is
  exactly the complement of it.

## 7. Falsifiers

A configuration satisfying (H1) with `extra(G) >= 7`, or with a zero of `h'` in
`G \ I`; either refutes this lemma (or [I-PF] upstream). Not found in 23,640 configs.
