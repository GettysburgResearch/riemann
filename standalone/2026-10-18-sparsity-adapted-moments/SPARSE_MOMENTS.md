# Sparsity before AFE summation: selected moments at every fixed order

Status: PROPOSED complete deductions from the stated unconditional large sieve and standard Hecke functional equation/approximate functional equation (AFE). Independent mathematical review is needed. No RH, inverse-L moment, new pointwise zero-free region, or uniform growing-order theorem is claimed.

## 1. Family, source contracts and the new estimate

Fix an integer n>=3, a number field F containing mu_n, and the fixed admissible family data of de Faveri, *Optimal large sieve for fixed order characters*, arXiv:2610.04045v1, Sections 1-2. Rows a are n-th-power-free exterior ideals, ordered by FULL Na<=U, not by radical or conductor. Fix a finite-order S-supported twist psi and retain the original zeros at nonunits. All constants depend on these fixed data. Distinct equal-norm ideals are distinct indices.

The imported Theorem 1.1 is the operator bound on BOTH power-free indices

    sum_a^flat |sum_(Nc<=V)^flat z_c chi_a(c)|^2
      << (UV)^eta K_n(U,V) sum_c |z_c|^2,
    K_n(U,V)=U+V+U^(1-1/n)V^(2/n)+U^(2/n)V^(1-1/n).       (1)

The primary source explicitly distinguishes this Theta_n kernel from the squarefree-only Xi_n kernel. Fixed twists go into common column coefficients. Conjugating the entire matrix preserves its norm, without reordering rows by a^(n-1). A row subset can be retained by positivity. The sieve itself is imported, not reproved here.

Let E be ANY subset with |E|<=U^nu, 0<=nu<=1. It may depend on zeros, L-values, or the height; no independence is assumed. Put

    k_n(v)=max(1,v,1-1/n+2v/n,2/n+(1-1/n)v),
    Phi_n(nu,l,sigma)=max_(0<=v<=l)
               [(1-2sigma)v+min(nu+v,k_n(v))].            (2)

For each fixed integer r>=1, fixed 1/2<=sigma<1, and eta>0, the proposed theorem is

    sum_(a in E) |L_F^S(sigma+it,psi chi_a)|^(2r)
       << U^(Phi_n(nu,r/2,sigma)+eta)(2+|t|)^C.          (3)

The constant is independent of E, nu and U; C may depend on fixed field, n, r and sigma. Uniformity in n, r, discriminants or a varying character modulus is NOT claimed. Finite inducing-principal rows are handled separately. Their possible AFE polar terms must not be omitted.

The gain is taking the cheaper of row counting and the sieve on EACH product dyad before summing the AFE. Taking the minimum of two already-summed estimates can be strictly worse.

## 2. Full columns, not an imaginary power-free AFE

Consider a dyadic polynomial over V<Nb<=2V with common coefficients bounded by C_eta (Nb)^(-sigma+eta). Divisor factors of any FIXED order are allowed in this bound. The trivial estimate on E is

    sum_E |P_a|^2 << U^O(eta) V^(1-2sigma+O(eta)) R V,
    R=|E|.                                               (4)

For the sieve alternative write b=c d^n uniquely, with c n-th-power-free. Shared primes between c and d are allowed. Exactly,

    (psi chi_a)(c d^n)
      =psi(c)psi(d)^n chi_a(c) 1_((a,d)=1).              (5)

If a and d share a prime the term is zero, including when c is a unit there. For fixed d the coefficient-square mass is

    << V^(1-2sigma+O(eta)) (Nd)^(-n),                    (6)

by ideal counting on c~V/(Nd)^n. Apply (1), retaining the mask in (5) as a row subset. Minkowski across d costs sum_d (Nd)^(-n/2+O(eta)), convergent because n>=3. Monotonicity of K_n in its second variable gives

    sum_E |P_a|^2 << (UV)^O(eta) V^(1-2sigma)
                                     K_n(U,V).          (7)

Consequently (4) and (7) give the SAME polynomial the bound

    << (UV)^O(eta) V^(1-2sigma) min(RV,K_n(U,V)).         (8)

This is a coefficient-sensitive full-column lemma. It is NOT an operator bound for arbitrary unweighted coefficients on all ideals. Such a claim would lose the decaying mass in (6). Empty subunit ranges are omitted; a bounded initial dyad includes the unit ideal explicitly.

## 3. The complete AFE, including its negative conductor factor

Use the standard AFE for L(s,psi chi_a)^r. Its primitive analytic conductor has finite part Q_a^r with Q_a<=C Na, and its two pieces have length Q_a^(r/2) times a fixed height power and an arbitrarily small U power. The coefficients are d_r(b) times the character. The dual root number has modulus one.

First split by ACTUAL conductor dyads Q, and by the finite S/gamma types. In each type Mellin inversion on a small positive line separates the conductor-dependent weights. After this separation coefficients are common across rows; imaginary conductor powers are row phases, not arbitrarily chosen column arrays. Minkowski outside the row l2 norm and integrable gamma/Mellin tails pay fixed height powers and arbitrarily small U losses. Fixed omitted Euler factors are finite polynomials and do not change these exponents. Truncations beyond the displayed lengths have arbitrarily rapid dyadic decay, not zero tails.

For the main AFE dyad use (8). Put V=U^v and first ignore the already allotted small losses/height factors. Its exponent is bounded by the expression in (2), with 0<=v<=r/2. Summing O(log U) significant dyads costs only an arbitrary power loss.

For the dual piece the local real part is 1-sigma, and the SQUARED exterior conductor factor is Q^(r(1-2sigma)). Since sigma>=1/2 and V<=Q^(r/2),

    Q^(r(1-2sigma)) <= V^(2-4sigma).                    (9)

Multiplying (8) at 1-sigma by (9) gives EXACTLY the same power V^(1-2sigma). One must not replace a negative power of Q by the corresponding negative power of U. With V<=Q^(r/2) U^eta times a height power, (9) has only the previously allotted small norm and polynomial height losses.

Separate conductor dyads may use R=|E| as an upper bound on their row count. Summing them costs logarithms. Handle the finite principal rows with their polar AFE terms/fixed-function bounds. The RHS exponent in (2) is at least nu>=0. This proves (3). The argument is a standard AFE method with a different order of estimates, not a new proof of the AFE or the large sieve.

## 4. Closed formula for all fixed orders

The piecewise-affine function k_n has successive formulas

    1                         on [0,1/2],
    1-1/n+2v/n                on [1/2,1],
    2/n+(1-1/n)v              on [1,2],
    v                         on [2,infinity).          (10)

For n=3 the two middle formulas agree. Let

    v0(nu)=1-nu                         if 1/2<=nu<=1,
           (n-1-n*nu)/(n-2)             if 1/n<=nu<=1/2,
           2-n*nu                       if 0<=nu<=1/n. (11)

Then nu+v crosses k_n(v) at v0. At nu=0 equality continues for v>=2. Before the crossing the function maximized in (2) has positive slope 2-2sigma. After it, the function is convex. Therefore

    Phi_n = nu+2(1-sigma)l,                         l<=v0;
    Phi_n = max(nu+2(1-sigma)v0,
                k_n(l)+(1-2sigma)l),                l>=v0. (12)

This proves the entire continuous parameter formula, not merely a sampled grid. At nu=1 it recovers the full-family envelope

    max(1,r(1-sigma),1-1/n+r((1+2/n)/2-sigma),
                       2/n+r(1-1/(2n)-sigma)).          (13)

At sigma=1/2 this is the previously used numerator envelope. In particular its r/2 term grows with r: (3) does not manufacture the missing diagonal inverse-Mobius hierarchy by taking r to infinity.

## 5. A concrete power bound, with its overlap made explicit

For n=6, r=2 and sigma=3/4, (12) gives

    Phi_6(nu,1,3/4)=nu+1/2,            0<=nu<=1/6;
                       5/8+nu/4,       1/6<=nu<=1/2;
                       1/2+nu/2,       1/2<=nu<=1.     (14)

For a subset of at most U^(1/2) rows, the fourth moment is therefore U^(3/4+eta), and its first mean is at most U^(9/16+eta). The full-family FOURTH moment followed by Holder gives U^(5/8+eta) for that first mean, so the selected fourth-moment argument saves U^(1/16) relative to that particular comparison. No special position of the subset relative to the zeros is assumed. However, the full-family EIGHTH moment at 3/4 is already U^(1+eta), and Holder with that stronger moment gives the SAME U^(9/16+eta). Therefore this numerical example is NOT claimed as an independent improvement over the complete higher-moment envelope. The source-specific contribution is the direct, all-fixed-order selected-dyad formula. The strict new comparison in this packet is the cardinality-sensitive mollifier and density theorem in ZERO_DENSITY.md.

The sparse moment is not stated to be asymptotically sharp. It is the exact envelope of the two proved dyadic upper estimates. Optimizing that envelope is different from proving a lower bound on L-values.

## 6. What still has to be proved for RH

These are numerator L-value moments on arbitrary selected families. They do not bound the reciprocal L-values or the fixed-principal native Mobius source. The new zero-density consequence is in ZERO_DENSITY.md and needs no CT theta input. No improved all-number-field zero-free composition is asserted without redoing its entire Poisson comparison. The positivity/subset methods here do not provide the missing signed critical estimate.
