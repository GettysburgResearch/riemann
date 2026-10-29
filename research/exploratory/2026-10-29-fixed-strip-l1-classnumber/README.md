# Conditional L(1) and class-number consequences of a fixed strip

**Status:** Classical analytic consequence of an assumed fixed zero-free half-plane; not a new zero-free theorem and no priority claim. The staged Lean candidate in [the return audit](../2026-10-29-arvi-return/README.md) states a formal Dirichlet nonvanishing assertion with θ=4369351/5000000. Its imported constants subsequently passed `leanchecker --fresh` in the same Lean kernel. The deduction below assumes that assertion applies to the conventional complex Dirichlet L-function for every nonprincipal primitive character and that the imported analytic framework has the intended mathematical interpretation; those are separate review gates, as are external verification and tracker admission. No new Lean formalization of the deduction is claimed here.

Suppose there is a fixed, explicit `0<θ<1` such that every nonprincipal primitive Dirichlet character χ modulo q satisfies

    L(s,χ)≠0  whenever Re s>θ.                            (H)

Then there is an **effectively computable** positive constant c_θ such that, for every such χ,

    c_θ / log log(q+3) ≤ |L(1,χ)|
                         ≤ C_θ log log(q+3).             (1)

In particular this implies the requested weaker bound `≫_θ 1/log(q+2)`. For every negative fundamental discriminant D, the associated primitive quadratic character is real and nonprincipal; the imaginary quadratic class-number formula gives

    h(D) = [w_D sqrt(|D|)/(2π)] L(1,χ_D)
         ≫_θ sqrt(|D|)/log log(|D|+3),                    (2)

with an effectively computable constant. Consequently, for each fixed class number H, these bounds give an effective finite upper bound on |D| for imaginary quadratic fields with h(D)=H. Here w_D is the number of roots of unity in Q(√D), equal to 2 except for D=−3,−4. The result also implies the weaker `≫sqrt(|D|)/log(|D|+2)` bound. No exceptional real character remains under (H).

## Uniform logarithmic bound

Put δ=1−θ and η=δ/2. For Re s>1 let `log L(s,χ)` be its Euler-product logarithm. Under (H) this has a single holomorphic continuation to the simply connected half-plane Re s>θ, with that normalization. Uniformly for `1−η≤σ≤2` and t∈R,

    |log L(σ+it,χ)| ≪_θ log((q+3)(|t|+3)).              (3)

Indeed, nonprincipality and periodicity give `|Σ_{n≤x}χ(n)|≤q`. The elementary summation-by-parts identity, valid for Re s>0, gives `|L(s,χ)|≪q |s|/Re s`. Apply Borel–Carathéodory to `g(z)=log L(z,χ)` on the disk centered at `2+it` of radius `1+3δ/4`. Its left edge is `1−3δ/4>θ`; the above estimate controls `Re g=log|L|` there by `O_θ(log(q(|t|+3)))`. At the center, the absolutely convergent Euler logarithm gives `|g(2+it)|≤log ζ(2)`. The target strip lies inside the concentric disk of radius `1+δ/2`, separated from the boundary by δ/4, so Borel–Carathéodory gives (3). The construction and constants are effective once θ is fixed.

## Smoothed Euler logarithm

For y≥3, Mellin inversion on Re z=1 gives

    (1/2πi)∫_(1) Γ(z) log L(1+z,χ) y^z dz
       = Σ_{m≥2} Λ(m)χ(m)/(m log m) · exp(−m/y).        (4)

The series and integral are absolutely convergent there. Shift the contour to Re z=−η. The holomorphic logarithm is valid throughout the strip by (H); the only pole crossed is Γ's simple pole at zero, with residue `log L(1,χ)`. Uniform bound (3) and exponential decay of Γ give

    log L(1,χ)
       = Σ_{m≥2} Λ(m)χ(m)/(m log m) · exp(−m/y)
         + O_θ(y^(−η) log(q+3)).                          (5)

All implied constants are effective. Choose `y=max{3, [log(q+3)]^(1/η)}`; the error is O_θ(1). Taking real parts and using `|χ(m)|≤1`,

    log|L(1,χ)| ≥ −Σ_{p,k≥1} exp(−p^k/y)/(k p^k) − O_θ(1)
                 ≥ −log log y − O_θ(1).                 (6)

For the last bound, Mertens' elementary upper estimate controls `Σ_{p≤y}1/p`; prime powers with k≥2 contribute O(1); and primes p>y are bounded by the convergent integer tail `Σ_{n>y}exp(−n/y)/n=O(1)`. The same absolute bound on the weighted series in (5) also gives `|log L(1,χ)|≤log log y+O_θ(1)`. Since `log y≪_θ log log(q+3)`, exponentiating gives both bounds in (1). Formula (2) follows from the classical analytic class-number formula. □

The same Borel–Carathéodory argument gives a shorter but weaker proof of the `1/log q` bound: (3) and Cauchy's estimate bound `L'/L` by `O_θ(log(q+3))` on `[1,1+1/log(q+3)]`; the Euler product gives `|L(1+a,χ)|≥ζ(2+2a)/ζ(1+a)≫a`, and integration of the log derivative over a=1/log(q+3) transfers this to s=1.

## Prior implications and evidence

The order `1/log log q` is classical: [Granville–Soundararajan](https://arxiv.org/abs/math/0106176) attribute it to Littlewood under GRH. It follows already from a fixed zero-free half-plane by the argument above, and is the correct order in known extremal examples. In the current formal literature, [Daugherty–Ryan–Ward, *Unconditional explicit Littlewood bounds in Lean 4*](https://zenodo.org/records/23459046) report a fresh dependency-closure replay and `L(1,χ)≥0.0621/log log q` for primitive real χ with `q≥10^100`, using the formal 7/8 theorem; their separate [formal statement page](https://prove2.me/theorems/2d1a57d1-6f7a-49e9-ac5b-c96941121ac8) records the conditional fixed-strip implication. We have not independently rechecked that archive or its imported theorem. Those prior claims make no novelty claim for (1)–(2); the simple complex-character proof here is included to expose the consequence and its assumptions.

The constant c_θ has not been numerically optimized here. Its effective existence follows from explicit, standard versions of the elementary partial-sum bound, Borel–Carathéodory, Stirling's formula and Mertens' estimate; extracting a published explicit number would require tracking those constants. The formal candidate's source-interpretation and external-verification qualifications remain essential and are not resolved by this deduction.

**Independent review:** Two researchers checked the uniform Borel–Carathéodory disk, logarithm branch, Mellin shift, y choice, effectiveness and class-number normalization under (H). This does not independently verify the formal zero-free candidate or its conventional interpretation.

## A polylogarithmic prime nonresidue consequence

The same hypothesis (H) also implies that for every fixed `A>1/(1−θ)`, every primitive quadratic character χ modulo q has a prime nonresidue

    min{p prime: χ(p)=−1} ≪_{θ,A} (log(q+3))^A,          (7)

with an effective constant. This is another inherited consequence, not a new independent zero-free region or a priority claim. For the candidate θ=4369351/5000000, `1/(1−θ)=5000000/630649≈7.92834`, so A=8 is admissible. PR94's own smaller-than-7/8 claimed boundary already gives the same exponent; the formal 7/8 boundary alone yields every exponent strictly larger than 8 by this argument.

The exact exponent 8 is already claimed from the earlier 7/8 input in [teal-sea's QRH nonresidue report, Theorem 1](https://zeta.teal-sea.com/read/hunts/qrh_nonresidue/RESULTS.html), which labels its result proved given that input and unreviewed. Its least-integer statement implies the same bound for a prime: if χ(n) is neither 0 nor 1, at least one prime factor has χ(p)≠1. We have not independently audited that report or its input. Thus exponent 8 is not a new consequence in the literature; the calculation here records what follows by this particular elementary argument from the staged smaller boundary.

To prove (7), choose a fixed κ>0 with `1/(1−θ−κ)<A` and put `σ₀=θ+κ`. The Borel–Carathéodory argument above, with a fixed margin κ/2 around the vertical line, followed by Cauchy's estimate, gives

    |L'/L(σ₀+it,χ)| ≪_{θ,κ} log((q+3)(|t|+3)).          (8)

Fix a nonnegative smooth W supported in [1,2] and positive on a smaller interval. Mellin inversion and a shift from Re s=2 to σ₀, crossing no pole under (H), give uniformly

    |Σ_m Λ(m)χ(m)W(m/x)| ≪_{θ,κ,W} x^σ₀ log(q+3).      (9)

The rapidly decaying Mellin transform absorbs the t-growth in (8). The prime number theorem gives `Σ_p log p W(p/x)≥c_W x` for all sufficiently large x. Suppose there is no prime nonresidue below 2x. Then every prime power m in the support has χ(m) either 1 or 0, so the left side of (9) is nonnegative and at least `c_W x−Σ_{p|q}log p≥c_W x−log q`. Take `x=C_{θ,κ,W} [log(q+3)]^(1/(1−σ₀))` with a sufficiently large effective constant. The right side of (9) is then at most `c_W x/4`, while x dominates log q for large q. This contradiction supplies a prime p≤2x with χ(p)=−1. The fixed finite range of small q can be absorbed effectively. Since `1/(1−σ₀)<A`, (7) follows. This use of an effective prime number theorem is separate from the class-number proof above.
