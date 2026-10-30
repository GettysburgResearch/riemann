# A full-correction majorant in the first Euler region

**Status:** A local calculation from the displayed source formulas, conditional on their application to Hu's fixed-field unit sectors and physical row family. It does not independently establish those formulas, the exact high representation, a contour theorem, or a zero-free region. Its purpose is to isolate the all-height majorant needed by OpenAI's abstract trace-tail lemma without dividing by a local factor at its zeros.

Fix a number field K containing μ₁₂ and the finite bad set of Hu §6. Enlarge the latter by a fixed initial-prime cutoff depending on e>0. Assume Hu's unramified formulas (6.11)–(6.13) and the ramified table quoted there and in OpenAI Lemma 7.1, with their unit-modulus field/sector phases and the original row zeros. Let σ=Re(s), ω=Re(w), ξ=Re(z), and work on a compact real box contained in

    σ≥51/100,  ξ≥17/50,  ω≥−1/100,  σ+ω≥1+e.           (1)

For arbitrary imaginary parts, sixth-power-free exterior row ideals u with Nu≪Z^D, and a fixed finite set of smooth disjoint prime windows with polynomial scales in Z, the quotient-free full compensated Euler correction in Hu (6.9) is holomorphic in a neighborhood of the box and satisfies

    |H_(ψ,u,Z)(s,w,z)| ≪ Z^B,

for a finite B depending on the box, D, the field and the fixed slot system, uniformly in u and all imaginary parts. The same holds on a bounded real contour joining segment contained in (1). A constant may depend on the fixed target and arithmetic data. The estimate is deliberately polynomial rather than the sharper raised-line main/error bound.

## Unselected good primes away from u

Write Q=Np and use Hu's notation

    V=Q^(−6z), W=χᵤ(p)Q^(−w), D=ψ(p)conjugate(χᵤ(p))Q^(−s),
    R=ϑ(p)^6 Q^(4−6s)V.

All displayed character phases have absolute value one. Hu (6.11) gives the local P, and its scalar extraction is

    H_p=(1−V)(1−W)P/(1−D).

After cancellation of the apparent `1−W` pole, direct algebra gives

    |H_p−1| ≪ |DW| + |V|(1+|W|)^2(1+Q|D|)
                          + |R|(1+|W|)^2.                  (2)

The only remaining denominators are 1−D and 1−R; on (1), |D|≤Q^(−.51) and |R|≤Q^(−1.10). To see (2) without concealing any cancellation, multiply H_p−1 by Q(D−1)(R−1). The resulting numerator is

    −DRQ + DVW²Q² − DVW²Q − DVWQ² + DVQ + DWQ
       + RVW²Q − RW²Q + RW + RQ − R − VWQ.

Every term is bounded by the right side of (2) after division by Q. In particular, although |W| may grow like Q^.01 on the far side of (1), (2) gives

    |H_p−1| ≪ Q^(−1−e)+Q^(−1.53)+Q^(−1.08).

The fixed-field prime-ideal sum converges uniformly on the box and in all imaginary parts. Thus the product over unselected primes away from u converges normally. This argument does not assume |W|<1 and is valid at local zeros of H_p.

## Row-dividing primes and selected factors

At p|u the source's zero extensions make D=W=0, but the distinct ramified `W_loc` in the local table must be retained. For row valuation j∈{1,…,5}, the source table gives, with phases suppressed in absolute values,

    H_p=(1−V)P_p,  P_p=1/(1−V)+P_p*,
    |P_p*| ≪ |R| + 1_(j=1) Q^(1−σ−ω−6ξ)
                    + 1_(j≥2) Q^(1−σ−ω) + T_j,
    T_1=Q^(−σ−ω),  T_2=Q^(3/2−3σ),
    T_3=Q^(2−3σ−ω)+Q^(2−4σ),
    T_4=Q^(5/2−4σ−ω),  T_5=Q^(3−6σ).

On (1), all terms are O(Q^(−c)) for c=min{e,1/50}>0: for example, 2−3σ−ω≤1−2σ−e≤−1/50−e and 5/2−4σ−ω≤3/2−3σ−e≤−3/100−e. Hence |H_p|≪1+Q^(−c), and the product over p|u is O_ε((Nu)^ε). The bound on the separate local term for j≥2 uses the exponent `V^(1_(j≤1))` correctly: it is 1 in that case, not zero.

Each selected local factor G_p is the full holomorphic factor from Hu (6.13), not a quotient G_p/H_p. Its rational denominators are among 1−V, 1−R and 1−D after the displayed cancellation; on a fixed box they are bounded away from zero after the cutoff. The source ramified table and the unramified expression for P_p* imply |G_p|≪Q^C for some fixed C, uniformly in the imaginary parts. There are finitely many slots, with primes in polynomial-size annuli; ideal counting bounds the sum over selected prime tuples, the extracted Q^(z−1) powers and window weights by Z^B. Multiplying by the normally convergent unselected product and the row-divisor estimate gives the claim. The proof never asserts that the full product or its local factors are nonzero. □

## Remaining source matching

The field-dependent realization of the complete ramified table and of the selected polynomial is imported from Hu, not reproved from its finite Gauss sums here. The corresponding second Euler region near the principal residue is addressed in [the principal-region note](../2026-10-28-hu-principal-region/README.md). To invoke OpenAI Definition 10.1 one must additionally establish that Hu's independent theta-side expression has the exact compensated high identity for these scales, and retain a common choice of finite unit sectors, row masks, buffered reciprocal height and external smooth-test orders. OpenAI Lemma 10.2 then supplies integrated and trace tails as an abstract analytic statement; it does not itself supply the buffered reciprocal.
