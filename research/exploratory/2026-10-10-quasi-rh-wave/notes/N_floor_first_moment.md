# Note N: the floor rows as a mollified first moment — cost/benefit, verdict

```text
Status: DERIVED (exponent-level analysis of the paper's own contour bookkeeping) + EMPIRICAL (grid search, scripts below)
Scope: note M's proposal (replace 1/L(x, eta chi_u) on floor rows by a Möbius polynomial M_r, bound the resulting
       first moment with an off-diagonal saving U^{-f}); the floor bin a0 = 51/100 at frequency U = Z^h
Exact sources (qrh_main.txt line numbers): (7.5) 3085-3088; xi 2698-2703, 2713, 3013-3016; Mellin weight W 4274, 4393;
       contours (10.11) 4509; outside factor 4733; (10.13) 4675; (10.15) 4694; floor count 4567-4568; Lemma 8.1 3417-3446;
       Lemma 8.2 proof 3504-3529; Prop 8.3 3556-3600; Lemma 10.3 4515-4549; region D1 4351-4353; Lemma 4.9 1278-1290;
       (20.4) 11500-11508; (20.5) 11583; Lemma 17.6 9249-9263; (19.3) 11200-11205; x = t+1-z 3062; Prop 2.1 381-460
What was run: scripts/floor_mollifier_cost.py (log_floor_mollifier.txt), scripts/floor_opt2.py, scripts/nearfloor2.py,
       scripts/ceiling_nofloor.py (note A's exponent_model.py with the floor constraint deleted)
Smallest remaining gap: the Phragmén–Lindelöf interpolation of the numerator bound between the reflected line and the
       zero-free rectangle (Section 4 below) is routine but not written; it only enlarges the (already negligible) window
```

## 0. Verdict in one paragraph

Note M's proposal **fails at first order, and at every order**. The coordinator's cost coefficient 4/3 is an
overcount (the correct coefficient is 1, Section 1), the truncation exponent r·eta is exact (Section 2), and the
"diagonal" that note M wanted to absorb into the signal **does not exist**: the row sum carries the fixed nonprincipal
ray phase xi(u), so the sixth-power diagonal is O(U^eps), not U (Section 3). With the corrected cost the proposal
still needs a mollifier longer than the family, r > 1/h = 16/13, and then a new obstruction appears that is
independent of f: the floor set is analytic, so the mean value must run over all rows and the rows with zeros in
(a0, a0+eta) must be subtracted at the moved contour, paying the full resolution cost Z^eta with no mollifier
compensation. With the paper's counts the best achievable change in the floor exponent is exactly 0 for every
(r, eta), even with f = infinity. With ideal counts a sliver of +0.0012 (Z-exponent; about 0.0003 in B) survives,
and it is an artefact of delta0 = 1/50 (Section 4). The wall is the delta -> 0 continuum of row classes, not the
floor bin (Section 5): deleting the floor constraint from note A's model changes nothing now and gives exactly
13/15 under ideal counts (Section 6).

## 1. The cost coefficient is 1, not 4/3 (task 1)

The Mellin weight of the high representation is (line 4274, repeated at 4393)

    W(X,Y,Z; s,w,z) = X^{1/2-z} Z^{s+z-1} Y^{w-1} e^{(s+z-1)^2} M(z) \hat W_1(w),

so Re s enters the outside power with coefficient exactly 1, Re w with coefficient l_y, Re z with 1 - l_x - d
(after q_u^{-z}). The retained contours (10.11), line 4509, are Re s = a+16e, Re w = 1-a-6e, Re z = 17/50, and the
outside factor computed in the proof of Lemma 10.4 (line 4733) is

    l_x(1/2 - z0) + a + z0 - 1 - a l_y - d z0 + (16 - 6 l_y)e.

The three appearances of a in (10.15) (line 4694),

    E = a - sigma0 + h(z0 - 1/6) - a l_y - l/2 + g + d(R + delta/2 - z0),   delta = 2a - 1,

are therefore: (i) Z^{Re s} with Re s = a + 16e (coefficient 1); (ii) Y^{Re w - 1} with Re w = 1 - a - 6e
(coefficient -l_y); (iii) the reflected numerator bound U^{delta/2+12e+eps} on Re w = 1-a-6e (line 4573, from Lemma 8.1
line 3444-3446), which enters (10.13) and gives d·delta/2 = d(a - 1/2) (coefficient d). The sum 1 - l_y + d = 4/3 at
d = h, (b,l) = (1/8,1/6), is the derivative of E with respect to the *bin value* a, when all three move together.

Note M only needs the reciprocal's variable moved: Re x = Re s -> a0 + eta + 16e, with w and z fixed. Checks:
the move stays in D1(eps0) (line 4351-4353: Re s >= 51/100, Re(s+w) >= 1+eps0 — both improve), H_{eta,u} << U^eps
there uniformly (Lemma 7.1, line 3266-3270), and the reciprocal stays inside the buffered rectangle Re >= a+6e of
Lemma 8.1 (line 3440-3441) where |1/L| << U^{eps1}. Pieces (ii) and (iii) are untouched. **The cost of eta is
Z^eta, coefficient 1.** (Moving w is not useful: moving it left costs (d - l_y)(a'-a) = (1/3)(a'-a) > 0 at d = h;
moving it right toward 1/2 costs l_y - d/2 = 7/96 > 0 per unit by Phragmén–Lindelöf between the two Lemma 8.1 bounds.
The paper's w-line is optimal independently.)

Consequence for the coordinator's inequality: cost eta versus gain h·min(f, r·eta) <= (13/16) r eta. For r <= 1 the
net change is >= 3 eta/16 > 0 (worse) for every eta > 0, so the first-order verdict is unchanged; the break-even
length is r = 1/h = 16/13 = 1.231 instead of 64/39 = 1.64. (Both at Liu's (b,l): h = 0.8119, 1/h = 1.232.)

## 2. The truncation error is exactly U^{-r(Re x - a0 - 6e) + eps}; eta -> 0 gives O(1) (task 2, escape (i))

Lemma 8.2's proof (lines 3504-3529) is the Perron representation of the Möbius polynomial,
M_r(x) = (1/2pi i) ∫ M_W(zeta) U^{r zeta} L(x+zeta, psi)^{-1} d zeta, shifted "only [for] the portion with added
frequency at most the assigned fraction of T1" to Re(x+zeta) = a + 6e, with the tails left on the absolute line
and bounded by O(U^B T1^{-N}). For an annular profile with V(t) = 1 near 0 the shift crosses zeta = 0 and picks up
the residue 1/L(x, psi); the remaining integral is bounded by sup |1/L| on the buffered line (Lemma 8.1: U^{eps1})
times ∫|M_W| times U^{-r(Re x - a0 - 6e)}. Hence on a floor row, at Re x = a0 + eta + 16e,

    1/L(x, psi) - M_r(x; psi) << U^{-r(eta + 10e) + eps1}.                                           (N.1)

Three remarks close escape (i):
* The **height** of the zero-free rectangle (2T1 = 2Z^tau) enters only through the Mellin tails O(U^B T1^{-N}) and the
  polynomial height factors (1+T1)^A = Z^{tau A}; it does not change the exponent. Rectangle versus half-plane is
  immaterial for the power of U.
* The bound (N.1) is **sharp on average over heights**: on the line Re(x+zeta) = a0+6e the integrand has modulus
  U^{-r(eta+10e)}|1/L| with |1/L| ≍ 1 typically, and it oscillates on the scale 1/(r log U) of U^{i r Im zeta}, as
  does 1/L itself; no cancellation in the zeta-integral is available (that would be a new mean value theorem for
  1/L on a zero-free line, which has no more content than the pointwise bound).
* At eta = C/log U the error is e^{-rC} U^{eps} = O(1): the truncation is not an approximation. This is the
  detector identity of Prop 8.3 read at a point: with D* = U^t, Y* = U^{20} (line 3577), J = o(1) at a zero while the
  unit term is e^{-1/Y*} = 1 + o(1), so "the resulting tail has absolute value 1 + o(1)" (line 3598-3600). A
  polynomial of length U^r resolves 1/L only to within U^{-r·dist}, dist = distance of Re x from the zero-free
  boundary; the paper's contour sits at dist = 16e, deliberately. **There is no eta -> 0 version with an exploitable
  off-diagonal: the main term and the error term are the same size there.**

Also, no approximant beats (N.1) at fixed effective length: a Neumann iterate 1/L ≈ M_r(1 + E + ... + E^{K-1}),
E = 1 - L M_r, has error U^{-K r eta} but is a Dirichlet series of effective length K r (after the approximate
functional equation for the L factors), and it is of size U^{K r (a - a0 - eta)} on a row with a zero at a. In every
such scheme (truncation exponent) = (zero-row blow-up exponent) = (effective length) =: R. Everything below is
stated for general R; for note M's M_r, R = r.

## 3. There is no diagonal: the ray phase xi(u) (task 3, escape (iii), and correction of note M §1)

The row sum in (7.5) (line 3085-3088) and (10.5) (line 4387-4393) is

    Σ_u^{(6)} q_u^{-z} xi(u) · zeta_F^S(6z) L^S(w, chi_•(u)) / L^S(s, eta chi_•(u)) · H_{eta,u}(s,w,z),

where xi is "a residue character modulo b* whose restriction to each prime factor is nonprincipal and whose order
divides six" (lines 2698-2702; b* = product of the primes of S). It is the primitive character that "will force the
Poisson frequency to be prime to S" (line 2713): in the Poisson step the Gauss sum at the primes of b* "vanishes
unless (H,S)=1. It therefore also removes H = 0. Every remaining element has a unique expression H = u a^6"
(lines 3013-3016). So (a) the zero Poisson frequency is absent by design, the principal row u = 1 is the *first*
nonzero frequency; (b) the factor zeta_F^S(6z) is the a^6-sum of H = u a^6 and is present in every row — it is not
a diagonal of the u-sum and nothing is double counted; (c) the outer xi(u) is a genuine nonprincipal character of
fixed modulus evaluated at the row.

Now take note M's formal expansion L(w,chi_•(u))/L(x,eta chi_•(u)) = Σ_{n,m} mu(m)eta(m) chi_{nm}(u) q_n^{-w} q_m^{-x}
(rigorously: after the approximate functional equation for the numerator and the Möbius polynomial for the
reciprocal, so finitely many pairs). The u-sum of a pair is

    Σ_u^{(6)} xi(u) chi_{nm}(u) q_u^{-z} W(q_u/U) · (local factors of H_u),

and for nm = k^6 the sextic symbol is 1_{(u,k)=1}. Every factor other than xi(u) is periodic modulo an ideal N
composed of good primes, (N, b*) = 1. The sixth-power-free restriction is Möbius over u = c^6 u' and xi(c^6 u') =
xi(u') because the order of xi divides 6 (this is exactly why the paper chose that order, line 3181: "xi(a)^6 = 1");
coprimality and divisibility conditions are Möbius over u = d u''. Each inner sum is a smooth sum over a disk of
xi(u'') times a function periodic mod N, whose main term is (1/q_{b*N}) Σ_{r mod b*N} xi(r) pi_N(r) · ∫ = 0 by the
Chinese remainder theorem, since Σ_{r mod b*} xi(r) = 0. The error is O((U/q_{c^6 d})^{-A}) for scales >= U^eps and
O(1) for the O(U^{1/6+eps}) small scales. Hence

    diagonal of the floor-row sum << U^{1/6 + eps}   (not U · zeta_F(6w)/L(x+5w, eta)).                   (N.2)

The coefficient sum Σ_{k} over nm = k^6 converges absolutely on the contour (Re(x+5w) ≈ 2.9, Re 6w ≈ 2.9), so (N.2)
is uniform there. Note M §1's "the floor wall is a diagonal" is therefore wrong: **the floor-row sum is main-term-
free to all orders; the trivial bound U^{1+delta0/2} is a pure triangle-inequality loss** against the conjectural
square-root size U^{1/2+delta0/2+eps} (random phases: the Gauss-sum root numbers of the reflected numerators times
xi). There is nothing to absorb into the signal of Prop 2.1; what note M calls "off-diagonal" is the whole sum.

Escape (iii) (expand 1/L where it converges, Re x > 1, then move x): the signal variable is x = t + 1 - z (line 3062)
and the outside power is Z^{s+z-1} = Z^t, so Re x = 1 + eps costs Z^{1 - a0} = Z^{0.49}. The maximal conceivable
saving of any mean value over U rows is square-root, Z^{h/2} = Z^{0.406} < Z^{0.49}. Moving x back afterwards is not
available: Prop 2.1 compares the *numbers* J_eta(Z) and f_eta(Z), (2.4)-(2.5), so an error term is paid at the
contour where it was estimated. Other placements: moving z left at fixed t moves x right but costs Z^{(l_x+h)eta}
= Z^{(1+l)eta} > Z^eta; z-moves at fixed x cost Z^{l·(shift)} and do not touch 1/L ("z0 cancels at d = h", note A).
The resolution cost Z^eta is the minimum over all placements, because Z^{Re x} *is* the signal scale (C has slope one,
Prop 2.1 line 381-383).

## 4. The decisive inequality (task 4b)

Fix the floor contour Re x = a0 + eta (+16e), Re w = 1 - a0 - 6e, Re z = z0, an approximant of effective length
U^R (R = r for M_r), and suppose the mean value Σ_{all u ≍ U} xi(u) q_u^{-z} L(w,chi_u) P(x;u) H_u saves U^{-f}.
The floor set is defined by zeros (Lemma 8.1 bins), so Σ_floor = Σ_all - Σ_{bins a > a0}, all at this contour.
Relative to the floor's trivial Z-exponent E_floor = C0 + 3 delta0/4 = -7/1200 ((20.5), line 11583), the pieces are:

  (M)  main term:                 eta - f h
  (T)  truncation on floor rows:  eta (1 - R h)                                 [count U^1, (N.1)]
  (S_delta) subtracted bin of class delta = 2a-1 > delta0, with the paper's own count U^{R(delta)} and amplitude q:
           E(h; delta, q) + Delta(delta),
           Delta(delta) = eta - (delta - delta0)(1 - l_y)/2 - h (delta - delta0)/4 + h R ((delta - delta0)/2 - eta)_+ ,

where E(h; delta, q) is (20.4) (line 11500-11508). The three terms of Delta are: the outside factor Z^{a0(1-l_y)+eta}
instead of Z^{a(1-l_y)}; the numerator at Re w = 1-a0-6e for a class-a row, U^{(delta+delta0)/4} by Phragmén–Lindelöf
between the reflected bound U^{delta/2} (line 4573) and the zero-free bound U^eps (Lemma 8.1) [with the crude
U^{delta/2} the term -h(delta-delta0)/4 is absent]; and the approximant, which on a row with a zero at a is of size
U^{R(a - a0 - eta)_+ + eps} (Lemma 8.2's shift crosses the pole at the zero — this is the detector's own largeness,
(8.1) and (8.4)). The new floor exponent is max{(M), (T), max_delta (S_delta)} + E_floor, and

    gain = E_floor - max{ E_floor + eta - f h,  E_floor + eta(1 - R h),  max_delta [E(h;delta) + Delta(delta)] }.   (N.3)

What (N.3) says:
1. (T) forces R > 1/h = 16/13 = 1.231 (= 1.232 at Liu's point) for any gain at all: a mollifier longer than the family.
2. The far classes bound R from above. Per unit (delta - delta0) the subtraction exceeds the paper's bin bound by
   h R/2 - (1 - l_y)/2 - h/4 = 0.406 R - 0.4635 (zero at R = 1.141; 0.4059R - 0.4639 at Liu's point). With the paper's
   counts the bin slack at the critical class delta_c = 0.389 is 2.3e-4 (note A), so already R = 1.231 costs
   0.0365·0.369 = 0.0135 there — two orders of magnitude over budget — unless eta >= 0.42, which (3) forbids. With
   ideal counts (slack 1/48 + delta/16) the far classes allow R <= 1.36.
3. **The near-floor classes delta -> delta0+ carry the full +eta with no compensation** (their zeros lie below the
   contour, so |P| << U^eps, but they are subtracted, not averaged). (S_{delta0+}) reads
   E(h; delta0+) + eta <= E_floor - gain, i.e. gain <= [E_floor - E(h; delta0+)] - eta. The bracket is
   h(1 - R(delta0)) - (small) = 0.0132 (paper's counts) or h delta0 = 0.0163 (ideal counts): the entire budget is the
   discontinuity between the floor's trivial count U^1 and the first bin's count U^{R(delta0)}.
   In the continuum normalisation (a row with zero at a0 + eta' costs Z^{eta - 1.74 eta'} relative to trivial under
   ideal counts, Z^{eta - 1.44 eta'} under the paper's; scripts/nearfloor2.py) the subtracted set must start at
   eta' > 0.575 eta (resp. 0.695 eta), and then (T) on the averaged set needs R h (eta - eta') > eta, i.e.
   R > 2.9 (resp. 4.0), at which point (2) explodes by ~0.5-0.9 in the exponent at delta = 5/6.

Numerics (scripts/floor_mollifier_cost.py, floor_opt2.py; grids r in [0.5, 6], eta in [0, 0.45], all classes, f = ∞):
* paper's counts (both (b,l) points): max gain = **0.0000** at every (r, eta); the proposal never beats the trivial
  floor bound, for any f. (And the floor is slack by 0.0056 against the critical class anyway, so even a positive
  floor gain would not move B = 0.874957.)
* ideal counts, PL numerator: max gain = **+0.0012** (Z-exponent) at r = 1.32, eta = 0.015, requiring only f >= 0.02
  but a mollifier of length U^{1.32}; in B this is ≈ 0.0003. The analytic bound from (N.3) items 2-3 is
  (Rh - 1)/(Rh) · h delta0 = 0.0016. With the crude numerator U^{delta/2} the far-class limit is R <= 0.82 < 1/h and the
  gain is 0 even with ideal counts.
* The sliver is proportional to delta0 = 1/50 and vanishes as a0 -> 1/2.
For comparison, the paper's own long-polynomial bound (Lemma 17.6, line 9249-9263; (19.3), line 11200-11205) gives
Σ_u |M_r|^2 << U^{(1+5r)/6+eps} for r >= 1, i.e. U^{1.27} at r = 1.32: through Cauchy–Schwarz that is f = -0.27, a
loss, so with the Section 17 tools even the sliver is unreachable.

## 5. Why the wall is intrinsic to "bound rows individually + detector" (task 4c)

(i) On a floor row every factor of the integrand is at pointwise Lindelöf quality already (Lemma 8.1 via Lemma 4.9,
    line 1278-1290: |L| + |1/L| << U^eps on the buffered rectangle; numerator U^{delta0/2} by the functional equation;
    H_u << U^eps; prime slots at amplitude q <= delta0/2). Nothing row-wise can improve, and the trivial bound is
    attained row by row. The only loss is the triangle inequality over the U rows: the floor-row sum is a
    main-term-free oscillating sum (Section 3) and the architecture, by construction, "applies the triangle
    inequality to the original row sum" after a pointwise partition (Lemma 10.4 proof, line 4722-4723).
(ii) Any cross-row cancellation needs a mean value over an arithmetically defined set; the floor is defined by zeros.
    Hence Σ_floor = Σ_all - Σ_{zero bins}, and Σ_all contains 1/L on rows with zeros, which has no bound. So 1/L must
    be replaced by a polynomial P, which (a) resolves 1/L only to U^{-R·dist} from the zero-free boundary, so the
    contour must leave the boundary by eta at the resolution cost Z^eta (Section 1-2), and (b) is of size
    U^{R(a - a0 - eta)} on zero rows — it is the detector.
(iii) The resolution cost is paid at the signal scale Z, the resolution is bought at the row scale U = Z^h with
    h = 1 - l_x + l < 1 (the direct side needs l_x > l). So (T) needs R > 1/h > 1: a polynomial longer than the family,
    outside the range where any large-sieve-type mean value is nontrivial (Lemma 17.6's e(r) > 1 for r > 1 is the
    paper's version of this).
(iv) Even granting (iii), the bins are continuous at the floor: the trivial exponent of class delta is the delta -> 0
    limit of the bin exponents (E(h;delta) -> C0 as delta -> 0 with R -> 1; the floor constraint is C0 <= 0, note E).
    Rows with zeros just above a0 are as numerous as floor rows and must be subtracted at the moved contour with the
    unmitigated Z^eta. This caps the gain by the count discontinuity h(1 - R(delta0)) at the floor edge — an artefact
    of delta0 = 1/50 — and sends it to zero as a0 -> 1/2.
Items (iii) and (iv) are each sufficient. (iv) is the cleaner statement: **the floor bin is not a wall; the
delta -> 0 continuum is**, and the only thing that breaches it is a mean value with cancellation over all low-lying
rows *at the paper's contour*, i.e. a ratios-type theorem for L(w,chi_u)/L(x, eta chi_u) with power saving and
no mollifier — Lindelöf-strength for the family, not a bookkeeping change.

## 6. Ceiling calibration (what the floor rows are worth at most)

scripts/ceiling_nofloor.py runs note A's model with the floor constraint deleted (equivalently f = 1/2 on the floor
bin as a free black box):

| counts | theta | with floor | floor deleted | active after deletion |
|---|---|---|---|---|
| Liu/paper | 1/12 | 0.874957 | **0.874957** | Blow, class (0.389, 1/2) |
| ideal | 1/12 | 0.869792 | **0.866667 = 13/15** | Blow, class delta -> 0 |
| ideal | 0 | 0.863950 | 0.859848 | Blow, class delta -> 0 |

So: zero value today; 0.0031 under ideal counts; and the value is exactly the a0 -> 1/2 dial of note A §5 item 6,
because after deletion the binding class is delta -> 0, i.e. the near-floor continuum of Section 5(iv).

## 7. Alternative idea for the floor rows and its predicted gain (task 4d)

The only floor-specific lever consistent with Sections 1-5 is the discontinuity itself: **extend the saturated
detector (Prop 8.3) to delta -> 0, i.e. a0 -> 1/2 + eps**, so that the floor bin shrinks to nothing and every row is
counted at U^{R(delta)} with its own class. Prop 8.3 uses delta >= 1/50 only in the saturation step
"delta{m - min(m,1-m)} << eps ... Since delta >= 1/50, this implies m <= 1/2 + O(eps)" (line 3665-3667); for
delta << eps the plain witness is not saturated, but the floor rows need no witness, so one can run the bins down to
a0 = 1/2 + eps_0 with eps_0 the detector's own loss, treating [1/2, 1/2 + eps_0) as the (now negligible) floor.
Predicted gain: 0 with the current counts (floor slack); 0.869792 -> 13/15 = 0.866667 with ideal counts (Section 6,
and note A §5 item 6). This is the ceiling of *any* floor-row idea; nothing beyond it is available without a
mean value over the low-lying continuum at the paper's contour (Section 5(iv)), whose conjectural value is f = 1/2
(ratios conjecture with the xi·root-number twist) and whose proven value, by every route examined here, is f = 0.

A structural alternative (unquantified, recorded for completeness): the resolution cost is Z^eta = U^{eta/h}; in a
probe with h >= 1 (rows' conductor at least the signal scale, i.e. l >= l_x) a mollifier of length U^{1} would resolve
the floor and (T) would hold at R = 1. This requires a direct-side (Gram) bound valid for l_x <= l, which the present
Prop 15.2/15.3 do not give (note J), and it does not remove obstruction 5(iv).

## 8. Deliverables summary

(a) Verdict: note M's proposal fails at first order (cost eta with coefficient 1, gain <= (13/16) r eta, r <= 1), and
    fails at every order (Section 4): with the paper's counts no (r, eta, f) beats the trivial floor bound; with
    ideal counts the ceiling is +0.0012 in the floor exponent (0.0003 in B), vanishing as a0 -> 1/2.
(b) Inequality: (N.3). In words: R h > 1 (truncation) and gain <= h(1 - R(delta0)) - eta (near-floor subtraction) and
    (delta - delta0)(h R/2 - (1-l_y)/2 - h/4) + eta(1 - Rh) <= -E(h; delta) for every class (far-class subtraction).
(c) Intrinsic reason: Section 5 — pointwise Lindelöf quality on every floor row, analytic (not arithmetic) definition
    of the floor forcing a subtraction of the zero bins, resolution paid at scale Z but bought at scale U = Z^h < Z,
    and continuity of the bin exponents at delta = 0, which makes the delta -> 0 continuum, not the floor bin, the wall.
(d) Alternative: a0 -> 1/2 via Prop 8.3 at small delta; predicted gain 0 now, 0.0031 (to 13/15) under ideal counts;
    this is the ceiling of every floor-row idea.
Corrections to earlier notes: note M §1 (no diagonal: xi(u) kills it, (N.2)); note M §4 and the coordinator's cost
    coefficient (1, not 1 - l_y + d/2 or 4/3).
