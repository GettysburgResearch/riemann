# Note U: the floor rows as a Rankin–Selberg / ratios / second-Poisson object — four routes, exact stopping points

```text
Status: DERIVED (exponent bookkeeping at the paper's contour; one rigorous obstruction, Prop. U.1) + LITERATURE (fetched today)
Scope: the floor-row sum of (7.5)/(10.5) at frequency U = Z^h, h = 13/16, contour (10.11): Re x = a0+16e, Re w = 1-a0-6e,
       Re z = z0 = 17/50, a0 = 51/100, delta0 = 1/50. Attack: represent L(w,chi_u)/L(x,eta chi_u) EXACTLY and average over u.
Exact sources: qrh_main.txt (7.5) 3085-3088; xi 2698-2713; Poisson 3000-3016; (4.7) 814; Lemma 8.1 3417-3446; (10.11) 4509;
       floor count 4567-4570, 4250-4262; (9.16) 4060-4068; (20.4)-(20.5) 11500-11583.
Literature (local text in scratchpad/dl_dfdh/): de Faveri–Dunn–Hoffstein arXiv:2607.07911 (dfdh.txt; Thm 1.1 l.152, Prop 8.1
       l.1895, (2.9) l.324, §2.2 l.322-380); Dunn–Radziwiłł arXiv:2109.07463 (dr.txt; Thm 1.1-1.2 l.117-150); Čech
       arXiv:2110.04409 (cech.txt; Thm 1.1-1.2 l.123-175, region (3.4) l.765-771, FEs (3.6)-(3.7) l.790-815);
       DIPP arXiv:2607.27131 (dl/dipp_2607.27131.txt; Z_aux l.455-470, mollifier remark l.188).
Companion notes: N (floor first moment, (N.1)-(N.3)), I §0 (coefficient classes), P §0-1 (triple series), E §3 (dial table).
Smallest remaining gap: the W(A_3) functional-equation group of §2 is formal (squarefree bookkeeping, correction factors and
       the eta-twist unverified, as in note P §2.2); it is not needed for the verdict, which rests on Prop. U.1 and (U.4).
```

## 0. The object, and three facts that bound every route

Row sum of the floor bin at dyad U (lines 3085-3088, 4559-4600), with the numerator reflected (Re w < 1/2) and z fixed:

    S_floor(U) = Σ_{u ≍ U, u floor}^{(6)} ξ(u) q_u^{-z} · ζ_F^S(6z) L^S(w, χ_•(u)) / L^S(x, ηχ_•(u)) · H_{η,u}(x,w,z).      (U.0)

Trivial (paper, Lemma 10.4 + Lemma 8.1): |S_floor| ≪ U^{1 - z0 + δ0/2 + ε} = U^{0.670}. Conjectural truth (random phases
ξ(u)·root numbers): U^{1/2 - z0 + ε} = U^{0.160}; this is "f = 1/2" in the normalisation S_floor ≪ U^{1-f}·U^{-z0+δ0/2}.

Three facts fix the landscape; everything below is a corollary of them.

(A) **No main term** (note N §3, (N.2)): ξ is nonprincipal at every prime of b*, of order dividing 6, so the u-sum of every
    pair (n,m) with χ_{nm} principal (nm = sixth power) is O(U^{1/6+ε}); and (line 3013-3016) the Poisson frequency H = 0 is
    absent. Consequence used repeatedly below: after Poisson in u, every pair (n,m) with q_{nm} ≤ U^{1-ε} contributes
    O(U^{-A}) — the u-sum is a *complete* smoothed character sum of length > modulus. The whole row sum lives on pairs with
    q_{nm} ≥ U^{1-ε}, where the dual sums are *incomplete* (length q_{nm}/U ≤ q_{nm}^{1/2} iff q_{nm} ≤ U²).

(B) **The exact ratio at one common contour is unbounded on zero rows** (Prop. U.1 below). So "average over all rows at the
    paper's contour" is not a theorem that can be false or true with a power saving; it is not a theorem at all without a
    hypothesis on the zeros of the family. The paper never does this: every bin has its own contour (10.11) at distance ≥ 16e
    from its zeros (Lemma 8.1), and the floor is defined by that buffer.

(C) **The paper's count of rows with zeros just above the floor is trivial**: (9.16) gives R(δ) = min{1, max{1-δ/2, 4/3-δ}}
    = 1 for δ ≤ 1/3 (line 4250-4262: "Since 1/50 < 1/3, R(1/50) = 1"). The sextic large sieve (Lemma 9.1, line 3692) is
    orthogonal only up to length U^{1/2}; the length-U detector needed for saturation (Prop. 8.3) costs (U·U)^{2/3} = U^{4/3},
    and de Faveri–Dunn–Hoffstein Thm 1.1 (dfdh.txt l.152) proves this (AB)^{2/3} loss is *sharp* for general coefficients.
    Consequence: as far as the proof knows, the floor rows may be a density-zero subset of the dyad; "floor = all − zero
    rows" with a mean value over all rows cannot bound the floor sum by anything smaller than the zero-row sum, which is
    U^{R(δ0+)} rows each of size ≥ U^{-z0+δ0/2}: **cap f ≤ 1 − R(δ0+) = 0 with (9.16)**, ≤ δ0 = 0.02 under density-hypothesis
    counts, and +0.0012 (Z-exponent; 0.0003 in B) after the far-class constraint of note N (N.3).

**Prop. U.1 (route-2/3 wall, rigorous).** Fix U, the dyad's finite family F_U = {ηχ_•(u) : u ≍ U sixth-power-free}, and a
line Re x = σ with 1/2 < σ < 1. Let d_U = min over ψ ∈ F_U and zeros ρ of L(·,ψ) with |Im ρ| ≤ T1 of |Re ρ − σ|, attained at
(ψ_0, ρ_0). Then
    Σ_{u ≍ U} ∫_{|Im x| ≤ T1} |L(w,χ_u)/L(x,ηχ_u)| |dx| ≥ c · |L(w,χ_{u_0})| · log(1/d_U) / |L'(ρ_0,ψ_0)| ·(1+o(1)),
and no lower bound for d_U or for |L'(ρ_0)| is known (there is no theorem repelling zeros of a sextic twist from a given
line, nor bounding |L'| below at a zero). Hence no estimate Σ_{all u ≍ U} (ratio) ≪ U^{A} holds for any A as a theorem about
the contour Re x = σ; the row-restricted statement with a buffer (Lemma 8.1) is the only one available, and the restriction
is analytic. In MDS language (§2): for Re z > 1 + (1−Re w)/2, the function x ↦ Σ_u ξ(u)q_u^{-z}L(w,χ_u)/L(x,ηχ_u) is
holomorphic exactly on Re x > β_sup := sup{Re ρ : ρ zero of some L(·, ηχ_u), u in the sum} (the u = 1 term alone contributes the
zeros of L(·,η), the target); under GRH for the family β_sup = 1/2 and the line Re x = 1/2 is a natural boundary (the poles of
the family are dense on it). Continuing the series to Re x = a0 = 0.51 presupposes a zero-free half-plane Re x > 0.51 for the
whole family, including η itself — far more than the 7/8 (or 13/15) being proved. This is where Čech's unconditional-looking
method needs GRH: cech.txt l.765-771, region (3.4) "Re(z) > 1/2" is obtained from (2.21) 1/L ≪ n^ε under GRH, and his
Theorem 1.2 (l.158) holds only for Re β > ε (denominator strictly right of 1/2) with error X^{max(1−2Re α, 1−2Re β, …)}.

## 1. Route (1): Möbius/Gauss-sum trick at the level of L-functions; the Rankin–Selberg object

**Object.** Formally (Re x > 1), 1/L(x,ηχ_u) = Σ_m μ(m)η(m)χ_m(u)q_m^{-x} with μ = γ_2³ᾱ on squarefree m ((4.7), line 814),
L(w,χ_u) = Σ_n χ_n(u)q_n^{-w}, so

    𝓡(w,x,z) := Σ_u ξ(u)q_u^{-z} L(w,χ_u)/L(x,ηχ_u) = Σ_{n,m} μ(m)η(m) q_n^{-w}q_m^{-x} L(z, ξχ_{nm}),                (U.1)

L(z, ξχ_{nm}) = Σ_u ξ(u)χ_{nm}(u)q_u^{-z}, a sextic Hecke L-function of conductor q_{b*}·rad(nm). Three nodes n — u — m with
cross symbols (u/n)_6, (u/m)_6 and *no* n–m cross term: the A_3 shape in the "L-function normalisation" (Čech (3.3): the
quadratic ratios series has the same shape), degree 6, with the Möbius on the m-node.

**Poisson in u = FE of L(z,ξχ_{nm}).** Using the Gauss-sum twisted multiplicativity (line 870, Lemma 4.4), the u-dual is

    Σ_{n,m} [γ_6(n,k)] [μ(m)η(m)γ_6(m,k)] (n/m)_6(m/n)_6 q_n^{-(w+z-1/2)} q_m^{-(x+z-1/2)} · U^{…} L(1−z, ξ̄χ̄_{nm}),

and by (4.7) μγ_1 = ᾱGγ̄_2 ∝ θ̄ (note I §0, note O §1.2): the n-node carries the **sextic Kubota coefficient** γ_6(n,·) (6-fold
cover, Whittaker coefficient of E^{(6)}), the m-node the **cubic theta coefficient** τ̄_3(m)η(m) (Patterson, 3-fold cover,
residual), and the cross term is (n/m)_6(m/n)_6 = (n/m)_3·(fixed phase) by sextic reciprocity. Absorbing (n/m)_3 into the
frequency of the Kubota series, the dual is

    Σ_u ξ̄(u)q_u^{z-1} Σ_m τ̄_3(m)η(m)(u/m)̄_6 q_m^{-(x+z-1/2)} · D_6(w+z−1/2 ; m² ū),     D_6(s;k) = Σ_n γ_6(n,k)q_n^{-s},

i.e. **a Rankin–Selberg sum over m of the cubic theta coefficient against the 6-fold-cover Whittaker coefficient at the
frequency m²ū** — the same mixed (3,6)-cover shape note P §0 found for the direct side (D_6 × quadratically twisted D_3 over
the row). It is not a Weyl-group MDS (Möbius node; note P §1(b): Cartan entry 3/2 for the (3,2)/(6) mixtures), and the
η-twist is outside Sawin–Whitehead's axioms (note P §1(b)). DFDH's regularised Rankin–Selberg (dfdh.txt §5, Prop 5.1/5.4)
treats θ_3 ⊗ θ̄_3, i.e. Σ|τ_3(m)|², and the second moment of Kubota series over the *frequency* (Prop 8.1, l.1895:
Σ_{N(a)≤A}|ψ(a,s)|² ≪ A^{1+ε} for Re s ≥ 1+ε, i.e. Re = 1/2+ε in the paper's normalisation); nothing in it or in Dunn–Radziwiłł
represents τ_3³ = μ·(phases) or a Möbius-weighted node: **μ is not the coefficient of an automorphic form, and the cube of
the theta coefficient is not a triple-product L-function coefficient.**

**Exponent.** Evaluate the dual at the paper's contour: the Kubota variable sits at Re(w+z−1/2) = 0.49+0.34−0.5 = 0.33 < 1/2
(left of its centre; conductor of D_6(·;k) in the frequency aspect is q_k, CFH (2.2)), the theta variable at Re(x+z−1/2) =
0.35, the u-variable at Re(1−z) = 0.66 with conductor q_{nm}. Every single-variable convexity/FE costs the conductor to a
positive power (the same computation as note P §2.5), and the only mean value available with a power saving is DFDH's
Prop 8.1 / DdFDS24 Lemma 6.6 (second moment over frequencies at the centre, Lindelöf on average = large-sieve quality).
But on floor rows the paper already has *pointwise* Lindelöf quality for every factor (Lemma 8.1 via Lemma 4.9); a
Lindelöf-on-average input can at most reproduce U^{1-z0+δ0/2+ε}. **Route (1) yields f = 0.** The exact point where it stops:
the dual (U.1) is the Poisson image of the same divergent series, so any bound for it at the contour is a bound for
𝓡 at the contour, which by Prop. U.1 does not exist without zero-freeness of the family (and the m-series does not converge
at Re x = 0.51 on rows with zeros below the contour either — its sum *is* 1/L there, with the poles).

## 2. Route (2): the ratios MDS; its functional-equation group; convexity at the contour

**Three generating FEs** (formal; (u,v,t) := (w−1/2, x−1/2, z−1/2); gamma factors and non-squarefree corrections dropped):

    σ_w (numerator, conductor q_u):            (u,v,t) ↦ (−u, v, t+u),   u-coefficient × γ_1(u)  [class 1 → μθ, Kubota 6-fold]
    σ_x (denominator, inverse root number):    (u,v,t) ↦ (u, −v, t+v),   u-coefficient × γ̄_1(u)·(η-phase)  [conjugate Kubota]
    σ_z (the u-sum L(z,ξχ_{nm}), cond. q_{nm}): (u,v,t) ↦ (u+t, v+t, −t), n × γ_6(n), m × μ(m)γ_6(m) ∝ τ̄_3(m)  [as in §1]

These are exactly the three FEs of the quadratic double-L series Σ_d L(s,χ_d)L(w,χ_d)|d|^{-z} (Diaconu–Goldfeld–Hoffstein,
group W(A_3) = S_4, order 24) and of Čech's A*(s,w,z) ((3.6), (3.7) plus the extra FE of his Theorem 1.2); the Möbius
changes coefficients, not conductors, so **the formal group of 𝓡 is W(A_3) = S_4** (degree-6 Gauss sums on the reflected
nodes; correction factors and the η-twist unverified, as for Z_η in note P §2.2). Polar divisor (formal): the S_4-orbit of
{w = 1} (the n = m = 1 term ζ_F(w)·L(z,ξ), the latter entire since ξ is nonprincipal), none from the Möbius node; the
ratios main terms of Čech (1.6) are the residues at s = 1 and s = 3/2 − w, and in our family both are killed by ξ
(fact (A)) — consistent with note N §3.

**Bochner continuation and where it stops.** Absolute convergence: R_0 = {Re w > 1, Re x > 1, Re z > 1}; convexity of the
numerator extends it to {Re x > 1, Re z > 1 + (1−Re w)/2} (Čech (3.4) second condition; unconditional, numerator only).
R_0 and σ_w(R_0) are connected through this strip, so the σ_w-chambers are reachable. R_0 and σ_x(R_0) = {Re x < 0, …} are
separated by the strip 0 ≤ Re x ≤ 1 in which the series has the poles of every 1/L(x,ηχ_u); Bochner's tube theorem needs a
*connected* tube of holomorphy, and connecting the two chambers through the strip is **equivalent to the family being
zero-free there** (Prop. U.1). Čech connects them with GRH (region (3.4): Re z > 1/2 for the denominator variable), and
even then only up to the natural boundary at Re = 1/2: Theorem 1.2 needs Re β > ε. So:

    (i) unconditionally: 𝓡 is defined at the paper's contour only through the row-wise representation, i.e. as the sum of
        the bins; "convexity on the paper's contour" is not defined for the all-row series;
    (ii) under GRH for the whole family (the only setting in which a ratios theorem is known, and for quadratic characters):
        Čech-type error X^{N(α,β)}, N = max(1−2Re α, 1−2Re β, …). Here α = Re w − 1/2 = −(δ0/2+6e) < 0 (reflect first with
        σ_w, prefactor U^{−α}) and β = Re x − 1/2 = δ0/2 + 16e, giving S ≪ U^{1 − δ0/2}·U^{−z0}·(root), i.e. **f = δ0 = 0.02 at
        most, proportional to the distance of the contour from the natural boundary**; nothing like f = 1/2.

**Route (2) verdict: f = 0 unconditionally (the needed continuation is the theorem's conclusion, for the whole family);
f ≤ δ0 = 0.02 even under GRH for the family.** The DIPP MDS (dipp l.455-470, Z_aux with two Kubota series = the A_3 second
moment, continued to C³ with a finite group via BB06) is the Möbius-free cousin; DIPP themselves treat 1/L only as a
truncated Möbius mollifier (l.188: "we do not optimize … by employing a truncated Möbius sum") — a polynomial, i.e. note N.

## 3. Route (3): the ξ-phase, the second Poisson, and a partition by distance to the nearest zero

**Exact form on floor rows.** On a floor row the retained x-integral on Re x = a0+16e equals, by Lemma 10.3's own contour
move run backwards (no zeros in between up to height T1; horizontal joins O(Z^B T1^{-N})), the integral on the absolute line,
i.e. the smoothed Möbius sum of length Z:

    ∫_{(a0+16e)} Z^{x+z-1}Φ(x+z−1)H_u(x,w,z)/L(x,ηχ_u) dx = Σ_m μ(m)ηχ_u(m)·Φ̌_z(q_m/Z)·(local H-corrections) + tails.  (U.2)

So Lemma 8.1's floor bound is, row by row, "Σ_{m ≲ Z} μ(m)ηχ_u(m)(smooth) ≪ Z^{a0+16e}U^ε": the quasi-RH-quality Möbius
cancellation that the row's zero-free rectangle buys. The floor-row sum is therefore a mean value over the (analytic) floor
set of Dirichlet polynomials of length Z = U^{1/h} = U^{1.23}, **longer than the family** — note N's R = 1/h, now seen to be
forced, not chosen. Cross-row cancellation would be a Bombieri–Vinogradov-type statement for twisted Möbius sums of length
Z over U characters with signs ξ(u): the proven B–V mechanism is "zero-density + per-row bound by the rightmost zero", i.e.
the paper's bins, and gives nothing beyond them; square-root cancellation over the family is of Elliott–Halberstam-with-
signs strength, with no mechanism.

**Second Poisson, honest exponent** (numerator and H set to size U^ε, Möbius sum of length Z, k the dual frequency,
incomplete dual sums of length K = q_m/U mod m, (A) kills q_m < U^{1-ε}):

    Σ_u ξ(u)q_u^{-z}Φ(q_u/U)χ_m(u) = U^{1-z}q_m^{-1}Σ_k g(ξχ_m,k)Φ̂(kU/q_m) ≈ U^{1-z}q_m^{-1/2}·Σ_{k ≲ K}χ̄_m(k)(phases)Φ̂.

    bound on the incomplete k-sums | m-sum      | result              | vs floor trivial U^{0.66}Z^{0.51}
    trivial (K)                    | absolute   | U^{-z0}Z^{3/2}      | × Z^{0.99}U^{-1} = U^{+0.22}   (loses)
    square-root (K^{1/2}, Burgess-conj.) | absolute | U^{1/2-z0}Z     | × Z^{0.49}U^{-1/2} = U^{+0.10} (loses)
    trivial (K)                    | square-root| U^{-z0}Z            | × Z^{0.49}U^{-1} = U^{-0.40}   (gains)
    square-root                    | square-root| U^{1/2-z0}Z^{1/2}   | = conjectural truth, f = 1/2

The only row that gains requires square-root cancellation in Σ_{m ≲ Z} μ(m)η(m)χ̄_m(k)·(…) for each dual frequency
k ≲ Z/U = U^{0.23}: a Möbius sum of length Z twisted by a sextic character of conductor k — **RH-quality cancellation for the
dual family {ηχ_k : k ≲ U^{0.23}}**, i.e. the same problem at the smaller scale, and now with length Z ≫ family size, where even
density-hypothesis counts do not compensate the per-row loss Z^{σ_k − 1/2} (one needs R'(δ) ≤ 1 − 2.67δ for the dual family,
beyond the density hypothesis). The "complete character sum that saves U^{1/2} outright" (fact (A)) applies only to q_m < U,
where the contribution is already O(U^{-A}): the ξ-phase has been fully spent by the paper's design (line 2713), and what
remains is entirely incomplete.

**Partition by distance of the nearest zero.** Classes a ∈ (a0, a0+e], (a0+e, a0+2e], … are the paper's bins; on class a the
Dirichlet series of 1/L converges (with Lindelöf-quality bounds) only for Re x ≥ a + 6e, so the class must be treated at its
own contour, and the mean value over a class is again a mean value over an analytic set: the count of the class is (C),
trivial for δ ≤ 1/3. Quantitatively, (N.3) with η = 0 and e > 0 fixed: truncation saving U^{-10re} (within the paper's O(e)
slack), near-floor subtraction cost U^{R(δ0+)} = U^1: **gain = 0 with (9.16); ≤ h(1−R(δ0+)) ≤ hδ0 with ideal counts.**

**Route (3) verdict: f = 0.** Stopping inequality: the dual of the ξ-twisted row sum is incomplete for every surviving pair,
and the dual m-sum needs the dual family's zero-freeness (U.3): for conductors k ≲ U^{0.23} and length Z,
    Σ_k Z^{σ_k} ≤ U^{0.23}Z^{1/2+ε}  ⟺  R'(δ) ≤ 1 − (log Z/log K)·δ/2 = 1 − 2.67δ   (false even under the density hypothesis).

## 4. Route (4): other mechanisms

(a) **Zero-row cap (general).** Any argument that reaches the floor set writes 1_floor = 1 − 1_{zero rows} (there is no
    arithmetic expression for the floor indicator: by the resolution principle, (N.1), a polynomial of length U^R resolves
    the zeros of a row only to U^{-R·dist}, and dist ≥ 16e is the paper's buffer, so a saving of U^{-16Re} per row at most),
    and must bound the zero-row sum, which has U^{R(δ0+)} terms each ≥ U^{-z0+δ0/2}·U^{-ε}. Hence
        f ≤ 1 − R(δ0+)                                                                                           (U.4)
    for every mechanism of this type. With (9.16): f = 0. Under density-hypothesis counts: f ≤ δ0 = 0.02, and the far-class
    constraint of (N.3) reduces the realised gain to +0.0012 (Z-exponent), 0.0003 in B. The dial-table value f = 0.1 → 0.857
    would need R(δ0+) ≤ 0.9, i.e. only U^{0.9} rows with a zero above 0.51 — beyond the density hypothesis (U^{0.98}).
(b) **Selberg/Jutila-type density near the floor** (provable, new, small): the sextic sieve is orthogonal up to length U^{1/2};
    a mollified second moment of the family with mollifier length U^θ, θ < 1/2 — DIPP's second moment with power saving
    (their Theorem B/C machinery, l.180-200) plus a truncated Möbius mollifier, which they say is routine — gives a
    Selberg-type count N(a) ≪ U^{1−c(θ)(a−1/2)} right from the floor, i.e. R(δ0+) = 1 − c δ0/2 < 1 for a small c. By (U.4) and
    (N.3) this is worth at most 0.0012 in the Z-exponent (0.0003 in B). It is the only route-4 item that is both provable and
    not already in the paper; it does not move the boundary.
(c) **exp of a short Dirichlet polynomial** (Radziwiłł–Soundararajan self-mollification: 1/L = exp(−log L), log L truncated
    at primes ≤ U^θ): log L(x,ψ) − P_θ(x) is governed by the zeros exactly as (N.1): resolution U^{-θ·dist}; on zero rows the
    truncated exponential is of size U^{θ(a−a0)}; same cap (U.4).
(d) **The bias.** DR (dr.txt l.117-150) and DFDH show the first moment of normalised Gauss sums has a main term from the theta
    pole (X^{5/6}/log X over primes; sharpness of (AB)^{2/3}). In the dual of §1 the n-node's first moment at fixed frequency
    has the sextic theta coefficient τ_6(m²ū) as its bias — unknown for 6-fold covers (DIPP 4.1.8: "outstanding open problem
    for r ≥ 4"). This complicates any exact evaluation of the dual but is not the obstruction: the primal has no main term
    (A), so the biases cancel across k; the obstruction is (U.4)/Prop. U.1.
(e) **Rankin–Selberg of θ_3 × θ̄_3 (DFDH §7-8)** gives Σ_{m≤M}|τ_3(m)|² ≍ M and Σ|ψ(a,s)|² ≪ A^{1+ε}; both are |·|²-type
    (positive) statements. The floor sum needs a *signed* mean value of τ_3³ = μ against the ξ·root-number phases; no
    Rankin–Selberg integral produces a cubed coefficient (the triple product L-function of θ_3 has degree 8 and is not
    Σ τ_3(m)³ m^{-s}).
(f) **Ray-class / ξ̂ structure.** CRT factorises g(ξχ_{nm},k) = τ-type factor at b* × g(χ_{nm},k'); the ξ̂-twist of the dual
    frequencies only removes k ≡ 0 and the S-primes (line 3013-3016). Nothing further.

## 5. Best f, the exact statement that would give f > 0, and the predicted boundary

* **Justified today: f = 0.** Every route is stopped by one of: Prop. U.1 (exact 1/L at a common contour: no theorem),
  (U.4) (zero-row cap with the paper's trivial count near the floor), or the dual-family inequality of §3 (the second
  Poisson needs RH-quality cancellation for twisted Möbius sums of length Z ≫ conductor).
* **Exact statement that would give f > 0** (two inputs, both needed):
    (I) [all-row mean value, polynomial] Σ_{u ≍ U} ξ(u)q_u^{-z}L(w,χ_u)P_R(x;u)H_u ≪ U^{1 − f'}·U^{-z0+δ0/2} for the Möbius
        polynomial of length U^R, R ≥ 1 (length ≥ family: outside every large sieve; Lemma 17.6 gives e(R) = (1+5R)/6 > 1);
    (II) [near-floor density] #{u ≍ U : L(·,ηχ_u) has a zero with Re ≥ a0 + e, |Im| ≤ 3iT1} ≪ U^{R(δ0+)} with R(δ0+) < 1.
  Then f = min(f', 1 − R(δ0+), 10Re) − (far-class cost of (N.3)); with R(δ0+) = 1 − δ0 (density hypothesis) the realised
  Z-exponent gain is +0.0012 and B moves by 0.0003. **The structural ceiling of every floor-row mechanism is 1 − R(δ0+) ≤ δ0.**
* **Predicted boundary (note E §3 dial, f = 0.1 → 0.857; each 0.01 of f ≈ 0.0025 in B):** with current counts f = 0 →
  0.874957 (unchanged); formal GRH-for-the-family ceiling f = δ0 = 0.02 → ≈ 0.870 on the dial, but (N.3) with the subtraction
  cost gives 0.8749 → 0.8746 at most; with ideal counts 0.869792 → 0.8695 (note N: +0.0012 Z-exponent). None of the four
  routes reaches f = 0.1.

## 6. Summary (≤ 400 words)

Four routes to cross-row cancellation at the paper's contour, each pushed to its stopping inequality.

(1) Expanding 1/L by μ = γ_2³ᾱ and Poisson-summing in u gives a three-node series n — u — m of A_3 shape, degree 6; after the
u-reflection the n-node is the 6-fold Kubota coefficient and the m-node the cubic theta coefficient τ̄_3 (μγ_1 ∝ θ̄), coupled
by a cubic cross symbol: a Rankin–Selberg sum over m of θ_3 against the sextic Whittaker coefficient at frequency m²ū. It is
not a WMDS (Möbius node), μ is not automorphic, and DFDH's regularised Rankin–Selberg controls |τ_3|² and second moments of
Kubota series (Prop 8.1, Lindelöf on average at the centre) — the quality the floor rows already have pointwise. f = 0.

(2) The ratios MDS 𝓡(w,x,z) has the formal functional-equation group W(A_3) = S_4 (as the quadratic ratios series of Čech and
the DGH double-L series). Its Bochner continuation from Re x > 1 to the chamber Re x < 0 must cross the strip where the
denominators have their zeros; Prop. U.1 shows the domain of holomorphy in x is exactly Re x > β_sup(family), so reaching
Re x = 0.51 presupposes a zero-free half-plane for the whole family including η — circular. Čech needs GRH precisely here
(region (3.4)), and even under GRH the contour's distance to the natural boundary caps the saving at f ≤ δ0 = 0.02.

(3) On floor rows the x-integral equals the smoothed Möbius sum of length Z = U^{1.23}, longer than the family. The second
Poisson leaves only incomplete dual sums (the complete ones, q_m < U, vanish by the ξ design); the honest exponents lose by
U^{0.22} (trivial) or U^{0.10} (Burgess-conjectural), and the one gaining line needs RH-quality Möbius cancellation for the
dual family of conductors ≤ U^{0.23} against length Z, beyond the density hypothesis.

(4) Any mechanism reaches the floor only as "all rows minus zero rows", so f ≤ 1 − R(δ0+) (U.4): zero with the paper's
count (9.16), ≤ δ0 under the density hypothesis, realised +0.0012 in the Z-exponent (0.0003 in B) after note N's far-class
constraint. A Selberg-type density near the floor (DIPP's second moment plus a mollifier) is provable but worth that same
0.0003.

Best justified f: 0. Boundary 0.874957 unchanged; ceiling of every floor-row mechanism 0.8746 (current counts) / 0.8695
(ideal counts). f = 0.1 (→ 0.857) would need fewer than U^{0.9} rows with a zero above 0.51, beyond the density hypothesis.
