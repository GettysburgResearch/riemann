# Low-height Artin transfer from abelian subgroups

**Status:** Proposed elementary transfer from published zero-free and low-order theorems; independent review and a broader prior-art search are needed.  
**Scope:** Full Artin L-functions of finite Galois number-field extensions. No Artin holomorphy conjecture is assumed.  
**Novelty:** No priority or best-known claim. The construction combines classical class-field and Artin identities with cited explicit results. The fixed half-plane claimed by [Liu (2026)](https://arxiv.org/abs/2610.26835), if independently validated, would dominate these logarithmic regions; it is not an input here.  
**Dependencies:** [Ahn–Kwon (2014)](https://doi.org/10.1016/j.jnt.2014.06.008), [Das–Gaba–Lee–Savalia–Wong (2026), Theorem 1.2](https://arxiv.org/html/2506.19319), Stark's low-order Artin holomorphy theorem, class field theory and the conductor–discriminant formula. The cited analytic inputs are not reproved. The `M0=Q` case also uses the [Platt–Trudgian verification](https://doi.org/10.1112/blms.12460) to control the trivial zeta factor.  
**Smallest remaining gap:** Independent check of the conductor orbit bound, full ramified local factors, scope of imported theorems, and prior art.

## Theorem

Let K/k be a finite Galois extension of number fields with group G, and H≤G a finite abelian subgroup with E=H²={h²:h∈H} nontrivial. Write

    h=|H|, e=|E|, M=K^H, M0=K^E,
    D=|disc(K/Q)|, d=|disc(M/Q)|, d0=|disc(M0/Q)|,
    n0=[M0:Q].

Let X be the nonempty set of characters χ of H of order greater than two. Write fχ for its finite Hecke conductor over M and put

    Q*=max_{χ∈X} N_{M/Q} fχ,
    r*=min_{χ∈X} φ(ord χ),
    T=log D−(h−r*) log d.

For n0≥2, define C(n0) using

    n0       2          3          4          5          6       >=7
    C(n0)  16.01983   19.55293   16.72207   13.71235   11.78180   11.51910.

Set

    Δ=min{ r*/(15.10 T), 1/[C(n0) log d0] }  if n0≥2,
    Δ=r*/(15.10 T)                            if n0=1.

Then T>0, and on `Re(s)>1−Δ`, `|Im(s)|<(1/3)tan(π/8)`, every irreducible Artin L-function of degree at least two and every nonreal one-dimensional Artin L-function is holomorphic and nonzero. Across all remaining real one-dimensional factors, at most one simple real zero can occur. At s=1, every nontrivial irreducible factor is holomorphic and nonzero; the trivial one has the usual pole of ζ_k. Any exceptional character is trivial on E.

For n0≥2 the following simpler width is valid:

    min{ r*/15.10, e/C(n0) } / log D.                  (1)

For n0≥7 the minimum is always the first term, because r*≤e and 15.10>11.51910; the uniform width is r*/(15.10 log D). When n0=1 that same simple width is valid. The stronger directly conductor-dependent width replaces the first term in Δ by `1/[15.10 log(dQ*)]`.

## Proof

The map h↦h² is a homomorphism because H is abelian. A character of H is trivial on E exactly when its square is trivial. Therefore Artin–Hecke factorization, including ramified places, gives the meromorphic identity

    ζ_K(s)/ζ_M0(s) = ∏_{χ∈X} L_M(s,χ).                 (2)

Each factor is the full primitive Hecke L-function of a nontrivial finite-order character of order≥3, and is entire. Taking a power of a finite-order character enlarges each local ramification kernel, so its finite conductor divides the original one; raising to an exponent coprime to the order preserves all local kernels and the conductor.

Choose χ∈X with Qχ=Q*. The φ(ordχ) distinct faithful powers of χ have this same finite conductor. The conductor–discriminant formula for K/M implies

    D ≥ d^h (Q*)^{φ(ordχ)} ≥ d^h (Q*)^{r*}.            (3)

All omitted conductor factors have integer norm at least one. Thus `log(dQ*)≤T/r*`. Also `dQ*>1`: if d=1 then M=Q, where every nontrivial Dirichlet character has finite conductor at least 2; otherwise d>1. Hence T>0.

For a character of order t, χ(E)=χ(H)² has order t/gcd(t,2). This divides e, and φ(t)≤t/gcd(t,2), so in particular r*≤e. The tower discriminant formula gives d0^e≤D, and clearly T≤log D.

Ahn–Kwon's theorem supplies a zero-free region for every factor of (2) with denominator `15.10 log(dQχ)`, at the stated height. All factors therefore are holomorphic and nonzero on the Hecke part of Δ. For n0≥2, the other part of Δ lies in the Das et al. low-height region: ζ_M0 has at most one zero there, and it is real. It is simple by Ahn–Kwon's separate low-height Dedekind theorem, since C(n0)>2 and the real exceptional point lies within the strict width `1/(2 log d0)`. By (2), ord ζ_K=ord ζ_M0 at every point in the region away from s=1, so ord ζ_K≤1 and any zero is real and simple.

Stark's theorem makes every irreducible Artin L-function holomorphic at every such point. In the regular factorization `ζ_K=∏_ρ L(s,ρ)^{dim ρ}`, all orders are now nonnegative integers. Their weighted sum is ≤1, excluding zeros of degree≥2 and limiting all one-dimensional factors together to one simple zero. Any nonreal one-dimensional χ has a distinct conjugate χ̄ with conjugate L-values at real s; a zero of one would also be a zero of the other, giving ζ_K order≥2. Hence the only possible exceptional factor is real one-dimensional. Such a character is trivial on E because its values are ±1. At s=1, the standard Brauer–Hecke argument gives nonvanishing for every nontrivial irreducible, while the trivial one has a simple pole.

When n0=1, `M0=Q` implies M=Q, k=Q, and G=H=H². The last equality makes H an odd-order abelian group, so every nontrivial character of G belongs to X. Moreover D≥(Q*)^{r*} and Q*≥2, hence the Hecke region lies in `Re(s)>1/2`. The cited Platt–Trudgian result excludes nonreal ζ zeros at the small heights in question; the standard sign of ζ on `(0,1)` and the Euler product exclude real and σ>1 zeros. Thus ζ_M0 has no zeros there, and the preceding argument applies with no exception away from its pole.

The simple width follows from (3), d0^e≤D and r*≤e. All displayed inequalities remain valid when Q*=1; the positive denominator then comes from d>1. □

## Explicit example and comparison

For an A10-extension K/k, embed H=C5×C5 using disjoint 5-cycles. Then h=e=25, r*=4, M0=M and the normal closure of H is A10. Here [M:Q]≥7, and the theorem gives all nontrivial irreducible Artin factors the field-specific width

    4 / [15.10 (log D−21 log d)].

The Das cap is automatic because D≥d^25. The simpler uniform width is 4/(15.10 log D). This is an explicit application, not a claim of global novelty. Comparing with the cyclic subgroup P generated by one 5-cycle, put M'=K^P. Since [M':M]=5, d_{M'}≥d^5; thus the bound derived from the same general discriminant estimate for P has denominator `log D−4 log d_{M'}≤log D−20 log d`, whereas the abelian bound has denominator `log D−21 log d`. These inequalities alone do **not** establish that the abelian bound is sharper for a specific field, because d_{M'} may be substantially larger than d^5; retain the exact conductor-dependent widths for a field-specific comparison.

For k=Q, if G has no quotient of order two, ζ_K itself is zero-free throughout the theorem's region except for its pole at s=1: the theorem leaves only a possible real one-dimensional factor, which must be the trivial ζ_Q factor; since dQ*≥2, Δ≤1/(15.10 log 2)<1/2, and the cited partial RH verification together with the real-axis sign excludes its zeros at the relevant heights. Eliminating such exceptional zeros for fields with no quadratic subfield is classical; see [Pierce–Turnage-Butterbaugh–Wood, Theorem 5.9 and Theorem N](https://dukespace.lib.duke.edu/bitstreams/6ca77058-c44c-4932-8fa5-cb7c8c9570ec/download). No claim of priority is made for the consequence.
