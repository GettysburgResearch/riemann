# Quotient-free physical correction on Hu's principal contour region

**Status:** Proposed source-dependent identity and local-majorant audit; independent review checked the algebra and displayed exponents. It is not a proof of the original local table, a complete contour shift, or a new zero-free region.

**Scope and sources.** Fix the field, allowed generators, finite set `S`, fixed unitary target `psi`, physical rows and disjoint slot windows of Hu, [*A seven-eighths zero-free half-plane for unitary Weil L-functions*](https://hexagonmath.org/2610.00216v1), equations (6.5), (6.9), (6.11)–(6.13). Write `N u` below for Hu's exterior norm `q_u=N(uR)`, not the absolute norm of a particular S-unit representative. Use the full `j=0,...,5` selected and unselected local table cited there, including its original zero extensions and unit phases, as an input. The independent source model is OpenAI's [*Quasi-Riemann Hypothesis*](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), Lemma 7.1 and §16.1; the two papers' phase conventions are not silently identified. The estimates below require the table to be valid with Hu's `psi`, conjugations, normalizations and fixed-type unit phases.

## Exact finite-operation identity

For a good prime `p`, put `Q=N(p)`,

    V=Q^(-6z),  W=chi_u(p) Q^(-w),
    D=psi(p) conjugate(chi_u(p)) Q^(-s),
    E=vartheta(p)^6 Q^(4-6s) V.

Both `W` and `D` retain the original zero extension at `p|u`. The local quantity `P_p*` is the completed-index restriction `p | c n^3`; its unit-part phases need not vanish at a ramified row prime. The physical operation in Hu (6.9) contributes, on initial absolute-convergence lines,

    Q^(z-1) [conjugate(psi)(p) Q^s P_p* - Q^(-w) P_p].

This is obtained directly from the Mellin weight in (6.5): `Z -> ZQ` contributes `Q^(s+z-1)` and the `X,Y -> X/Q,Y/Q` rescaling with `Q^(-3/2)` contributes `Q^(z-w-1)`. The conjugate on `psi` is Hu's convention and is essential here.

The local identity `P_p-P_p*=(1-V)^(-1)+W/(1-W)` gives the scalar-factor extraction

    Q^(z-1) [(1-V)^(-1)(1-W)^(-1)(1-D)] G_p,

where Hu (6.13) defines

    G_p = { (conjugate(psi)(p) Q^s - Q^(-w))(1-V)(1-W) P_p*
             - Q^(-w)(1-VW) } / (1-D).

This proves the identity first where the original local series and scalar factor converge; meromorphic continuation gives the same identity where their displayed continuations are valid. The expression for `G_p` does not divide by `P_p`, by its normalized factor `H_p`, or by `1-W`. In particular the derivation does not assume any of these quantities is nonzero at a later contour point.

With `H_p=P_p(1-V)(1-W)/(1-D)`, the complete correction is the finite sum over the actual slot tuples

    H_full = sum_(p_i in slot_i) product_i [W_i(Q_i/P_i) Q_i^(z-1) G_(p_i)]
                                 product_(p notin S, p not among p_i) H_p.

The windows' disjoint prime supports ensure no prime is replaced twice. This is the correction for the *same* physical operation, not a new definition of a high integral. The formula is valid for arbitrary positive `X,Y,Z` for which the base series is absolutely convergent initially; geometry only enters the outside Mellin kernel and slot sizes. For each fixed `Z` the slot tuple sum is finite.

## D2 holomorphy and uniform local majorant

On `D2 = {Re(s)>=7/8, Re(w)>=19/20, Re(z)>=33/200}`,

    |V| <= Q^(-99/100),  |E| <= Q^(-56/25),  |D| <= Q^(-7/8).

Thus `1-V`, `1-E`, and `1-D` are uniformly bounded away from zero at all good primes. The full source table expresses `P_p*` using those first two denominators and a finite sum of monomials in `Q^s,Q^w,Q^z` with unit-modulus local coefficients. On any compact real box in D2, it follows that `G_p << Q^C` uniformly in all three imaginary parts and in the unitary target and unit-sector phases; here `C` depends on that real box and fixed local data, not on the heights. This covers ramified selected primes only conditional on the cited six-class table.

For an unramified row prime, Hu (6.11) gives the explicit defect identity

    (1-E)(1-D)(H_p-1)
      = -D E + D V W^2 (Q-1) - Q D V W + D V + D W
        + E V W^2 - E W^2 + E W/Q + E - E/Q - V W.

Each monomial has magnitude at most `Q^(-363/200)` on D2, so `H_p=1+O(Q^(-363/200))`, uniformly in all imaginary parts and unit phases. This is a direct algebraic consequence of the displayed unramified formula, not a claim about the ramified classes.

For `p|u`, the imported ramified table supplies the source's weaker bound `H_p=1+O(Q^(-33/40))`; its phases retain the local unit part. Therefore, for each epsilon>0, the unselected product is normally convergent and

    product_(unselected p) |H_p| <<_(K,S,epsilon) (N u)^epsilon.

Indeed, the unramified defect is absolutely summable over prime ideals, and `product_(p|u)(1+C Q^(-33/40)) <<_epsilon (N u)^epsilon` by splitting off finitely many small primes. Removing selected factors from these positive majorants is harmless. The constants are uniform over the finite unit sectors because their phases have modulus one; any sector-specific finite factors at `S` are fixed data and are not silently inserted into an exterior Euler product.

For each fixed compact real box in D2, if `N u <= Z^D` and `P_i=Z^ell_i` with a fixed finite slot system, the fixed-field bound `#{p:N(p)<=x} <<_K x` gives

    |H_full| << Z^B

for a finite `B` depending on the box, `D`, geometry and fixed slot system, uniformly in all imaginary parts. The same bounds on a slightly enlarged neighborhood of each point establish holomorphy there via normal convergence. This supplies the correction-factor part of an all-height contour majorant. It does not bound the separate reciprocal L-functions near zeros, justify moving their contours, or establish the required Mellin-tail estimate by itself.

## S and unit sectors

All Euler factors displayed above are exterior factors outside the *same* fixed `S`, which contains the fixed bad primes and target conductor for the application. Both the base expression and its finite compensation use those same exclusions. Enlarging `S` changes the fixed calibration and all associated expressions together; it cannot be done in only one side of the identity. Positive-estimate sectors are finite classes modulo Hu's chosen unit subgroup. Keep their exact coefficients and masks through each local calculation, then recombine them according to the physical identity. Hu §6.4 identifies the **principal Kummer class** after this recombination; the statement `u=1 is the sole principal row` from the Eisenstein-unit setting must not be transferred independently to each general-field unit sector.

**Unresolved input:** Hu (6.11) explicitly writes the unramified factor, but refers to the full finite Gauss sum in (6.4) and external sources for the five ramified classes. An independent comparison of that table, all unit phases and the marked restriction for an infinite-type target has not been performed. The identity and bounds above are conditional on that source interface. The separate D1 joining region, zero-buffered reciprocal bounds, vertical growth of all other factors, and the complete high-side error budget remain distinct obligations.

**What was checked:** Direct Mellin-rescaling algebra, exact quotient-free extraction, the displayed unramified defect by symbolic algebra, D2 exponents, and the product/finite-tuple majorant. An independent review reproduced the rescaling, conjugation, polynomial, dominant exponent and source-conditional ramified exponent. The source table, unit-sector calibration and any complete contour shift were not independently verified.
