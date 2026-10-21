# A localized sixth-moment route to 0.8745

Status: PROPOSED SOURCE-DEPENDENT CONDITIONAL DEDUCTION. The sixth-moment hypothesis below is OPEN. No new unconditional zero-free boundary is asserted.

Scope: a scalar/analytic replacement in Section 14 of Baiying Liu, *Zero-free half-planes for Hecke L-functions over number fields*, arXiv:2610.26835v1. Its baseline and underlying analytic recursion are imported, not independently proved here. Author-side review only; no independent referee, proof-assistant verification, or literature-wide priority claim.

## 1. Target and source conventions

Use the exact row classes, centrally normalized plain blocks, finite bad-prime/ray system, primitive inducing characters, selected prime factors, and norm-twist/profile interfaces of Liu, Sections 13 and 14, especially Proposition 14.3. These are actual arithmetic rows, not independent random characters or freely chosen coefficient arrays.

Fix a permitted cyclotomic field F and all fixed source data. The source's previously obtained common bound beta_*(F) <= 7/8 licenses kappa=3/4. Our target is

    B = 1749/2000 = 0.8745.

The numerical improvement over the source's B_flat=0.874886647039964... would be about 0.000386647, IF the new hypothesis is proved. Nothing below establishes that hypothesis.

Set, exactly,

    b=7/100, ell=253/1500, kappa=3/4,
    h=(1+b+3 ell)/2=197/250,
    l_y=(1+b-ell)/2=169/375,
    l_x=(1-b-ell)/2=571/1500,
    B=11/12-ell/4.

For 1/8 <= delta <= 5/6 and 0 <= x <= 1/2, put

    c=1/(3 kappa),
    D_kappa=3-(1+2c)x,
    P_kappa=(2-2cx)(1-x),
    J=(5/6-delta)D_kappa+delta P_kappa,
    R=1-delta+(5/6-delta)delta P_kappa/(2J),
    g=delta x, theta=g/(6 kappa),
    K_2=(3R+1)/4,
    C_0=-1/4+b/6+5ell/4.

J is strictly positive on the full rectangle. The original high-side endpoint is

    E=C_0+delta/2+delta x[ell+c(h/4-l_y/2)]-3h(1-R)/4.   (1)

The input domain that needs a new estimate is only

    Rcrit=[3/8,5/8] x [9/20,1/2].                       (2)

The other classes will use the original fourth moment unchanged.

## 2. The missing arithmetic hypothesis H6(1/10)

Let Bcal be any source row class whose parameters lie in a fixed neighborhood of (2), for example [37/100,63/100] x [11/25,1/2], intersected with the physical parameter domain. Let U be its row scale, Lcal its available selected-prime length, and #Bcal << U^(R+epsilon)(1+H)^A. Include every sixth-power-free nonunit row and every original natural nonunit zero; do not discard powerful row parts or exceptional members.

For every epsilon>0, choose the prime mesh and capacity decrement BEFORE fixing the finite system of positions, as in Proposition 14.3. Let S_{j,m}(u), j=1,2,3, be centrally normalized plain ideal polynomials of common length U^m for the actual presentation character, with independently permitted smooth profiles and norm twists. Let Q_sel be a product of selected original prime blocks of total length exponent z, with their actual coefficients, phases, and ray restrictions.

H6(1/10) is the assertion

    sum_{u in Bcal} |S_{1,m}(u) S_{2,m}(u) S_{3,m}(u) Q_sel(u)|^2
       << U^(11/10+epsilon)(1+H)^A                     (3)

whenever 3m+6 kappa z <= 1 (with the source's arbitrarily small decrement). It ALSO requires the unselected version z=0 for every retained AFE length

    0 <= m <= 1/2+r_F/100+epsilon, r_F=[F:Q]/2,
    1 <= H <= U^(1/100).                               (4)

The estimate must hold for both conjugate character orientations, the source's finite ray expansions, the differentiated profiles needed for conductor and height discretization, and all original zero-only masks. Constants may depend on fixed field/target/source data and the requested loss, but not on U, the row, the selected class, or the varying profile coordinates inside the declared bounded smooth family. For an all-target statement it is required for each fixed finite-order target in the source construction. No growing-field uniformity is asserted.

The unselected clause (4) is important: (3) with z=0 and m<=1/3 alone does NOT suffice. This is a structured sixth moment, not an arbitrary-coefficient improvement to the sextic large sieve, and not the inverse/plain mixed moment in PR #1006.

## 3. H6 gives a stronger first numerator moment

More generally suppose the corresponding 2k-th moment has size U^(1+omega+epsilon), with capacity km+6 kappa z<=1 and the same unselected AFE clause. Put

    K_k=((2k-1)R+1+omega)/(2k).

The source's amplitude ordering gives |Q_sel(u)| >= U^(gz-o(1)) on the whole class. Removing that factor from the moment and applying Holder gives

    sum_{Bcal}|S_m(u)| << U^(K_k-gz/k+epsilon)(1+H)^A.  (5)

For m<=1/k choose z=(1-km)/(6 kappa), when supply permits. Including the AFE's central-shift coefficient U^(-theta m) makes the exponent

    K_k-theta m-g(1-km)/(6 kappa k)=K_k-theta/k.        (6)

For m>=1/k the unselected clause gives the same bound, since -theta m <= -theta/k.

When Lcal<1/(6 kappa), the short supply-limited portion has

    m<=m_0=(1-6 kappa Lcal)/k.

Use the literal pointwise bound |S_m| << U^(m/2+epsilon), not a nonexistent selected product. Its exponent differs from the target by

    R+(1/2-theta)m_0-(K_k-theta/k)
      = [R-omega-(6 kappa-2g)Lcal]/(2k) <= 0,          (7)

using the original source condition R <= (6 kappa-2g)Lcal. The source proves that condition in the maximal-length regime used here; it is not deleted by our replacement.

Carry out the source AFE transfer with these block bounds. The bad-prime factors have finite total absolute coefficient mass. Both AFE pieces retain their conjugate character orientation and their exact gamma/profile factors. Row-dependent conductors are handled by the same auxiliary logarithmic parameter and derivative argument, now applied to S_1 S_2 S_3 Q_sel. The derivative is a sum of three products of the type explicitly included in (3). The conductor deficit for powerful rows and the full tails remain those of the source. The mesh and smoothness losses can be arbitrarily small; the unselected clause covers (4).

Consequently the proposed replacement for Proposition 14.3 is

    sum_{u in Bcal}|L(1/2+theta+it,bar(psi_u^*))|
       << U^(K_k-theta/k+epsilon)(1+H)^A.              (8)

For k=3, omega=1/10, comparison with the source exponent K_2-theta/2 gives the saving

    gamma=(1-R-2theta-2omega)/12.                       (9)

The exact certificate proves 1-R-2theta >= 7/30 throughout (2). Hence gamma>=1/360. We use only nu=1/400, leaving a strict 1/3600 reserve for arbitrarily small losses. For general k the analogous gain is

    [(k-2)(1-R-2theta)-2omega]/(4k).                   (10)

These are deductions from the moment hypothesis, not proofs of moments.

## 4. Complete continuous scalar certificate

The checker reconstructs (1), clears only the positive J, transforms the resulting rational polynomials into Bernstein form on rectangles, and recursively bisects until every Bernstein coefficient is strictly positive. Their convex-hull property proves the inequalities on EVERY point, not merely a sampled grid.

The full rectangle is covered as follows:

| Region | Proven inequality | Positive Bernstein leaves |
|---|---|---:|
| delta in [1/8,3/8], x in [0,1/2] | E < -1/20000 | 1 |
| delta in [5/8,5/6], x in [0,1/2] | E < -1/20000 | 1 |
| delta in [3/8,5/8], x in [0,9/20] | E < -1/20000 | 8 |
| Rcrit | E-h/400 < -1/5000 | 8 |
| Rcrit | 1-R-2theta > 7/30 | 1 |
| full rectangle | J>0 | 1 |

There are 20 leaves total. Every polynomial, box and rational Bernstein margin is in results/endpoint_certificate.json.

The uncollapsed row-scale expression in the source is, with a=(1+delta)/2 and z_0=17/50,

    Ecal(d)=a-B-l_y(1/2+theta)+h(z_0-1/6)-ell/2+ell g
             +d(K_2+theta/2-z_0).

At d=h this equals (1). In Rcrit the replacement is Ecal(d)-nu d. Since K_2>=3/8, its slope is at least

    3/8-17/50-1/400=13/400>0.

Thus all d<=h are covered by the endpoint, and sufficiently small source slack d<=h+zeta is paid by the strict margins. The parameters also satisfy ALL the separate conditions of Remark 14.1 other than its unchanged endpoint requirement, which is precisely what has been replaced. The checker verifies the small-delta endpoint, floor endpoint, small-row bound, principal domain, capacity and supply inequalities exactly. Its strict minimum complement margin is 1/20000, so continuity allows a positive mesh/slack; one must take those losses after fixing the displayed certificate, not silently set them to zero.

Retain Liu's source local correction estimates, height truncations, Lemma 14.4 and closure argument. On the complement use the old numerator bound; on Rcrit use (8) and nu. This supplies the proposed conditional conclusion beta_*(F)<=1749/2000 under H6 and the imported analytic inputs. The scalar certificate alone proves no holomorphy theorem.

For ordinary zeta, it is enough to establish the required hypothesis for the source construction over F=Q(zeta_12), with its fixed target data. The abelian Dedekind factorization contains zeta as a factor, and the other Dirichlet factors have no poles in the target open half-plane. For all-number-field Hecke conclusions, one would instead need the hypothesis for every required cyclotomic field and the imported descent argument. That stronger scope is not inferred from one field.

## 5. Why this is NOT an achieved boundary

With no new gain, delta=12/25 and x=1/2 give

    E=2305801/1336050000 > 0.

The checker deliberately attempts the false unconditional certificate and rejects it. This excludes the temptation to publish 0.8745 merely from successful parameter optimization.

The existing fourth moment plus the pointwise bound |S_m|<<U^(m/2+epsilon) yields a sixth-moment cost at best U^(1+m+epsilon). At m=1/2 this is U^(3/2+epsilon), not U^(11/10+epsilon). A single synthetic value U^(1/4) already has fourth energy U and sixth energy U^(3/2): fourth-moment control alone cannot supply (3). This is an obstruction to that inference, not an arithmetic counterexample to H6.

PR #1011's stronger Gauss-weighted conductor mean is a different norm; its character, Gauss factors, divisor marks and pair-conductor prices cannot be dropped. PR #1012's signed projector cancellation is real, but it does not bound the surviving off-diagonal kernel. The new Xu-Sang sextic-sieve lower-bound paper also rules out a generic arbitrary-coefficient shortcut at its stated scope. None of those resources currently proves H6.

The smallest remaining analytic task is therefore explicit: establish (3)-(4), uniformly at the source interfaces, on the selected critical classes. A proof would turn this conditional target into a smaller boundary; the present work does not.

## Sources and replay

- Liu v1: https://arxiv.org/html/2610.26835v1 (Sections 13-14; Proposition 14.3, Lemma 14.4, Remark 14.1 and endpoint assembly).
- Xu-Sang v2: https://arxiv.org/html/2610.15291v2 (earlier amplified-numerator framework; credited, not newly discovered here).
- Latest repo interfaces are pinned in SOURCES.md.

Run `python checks/endpoint_certificate.py` and `python -O checks/endpoint_certificate.py` from this packet. SymPy is used for exact polynomial formation; all subsequent coefficients and covers use fractions.Fraction. Both runs were executed with identical JSON output. This is author-side algebra and coverage verification, not independent analytic review.
