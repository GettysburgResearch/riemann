# A uniform low-height region from nonreal linear-character induction

**Status:** Proposed elementary transfer of a published Hecke estimate; awaits independent review and prior-art search. No improvement for the Riemann zeta function is claimed.

**Inputs:** The order-at-least-three case of Ahn–Kwon, [*Some explicit zero-free regions for Hecke L-functions*](https://doi.org/10.1016/j.jnt.2014.06.008), the conductor–discriminant formula for abelian extensions, the discriminant tower formula, class field theory, and full Artin induction including ramified local factors. The group-theoretic spanning condition below is a hypothesis, not asserted for all Artin representations.

## Theorem

Let `K/F` be a finite Galois extension of number fields with group `G`, and write `d_K=|disc(K/Q)|`. Suppose that the character of a nonzero complex representation `rho` has an identity in the integral character ring

    chi_rho = sum_(i=1)^m n_i Ind_(H_i)^G lambda_i,
    n_i in Z,

where every `H_i` is a subgroup of `G` and every `lambda_i` is a one-dimensional character of `H_i` of order `m_i>=3`. Put `k_i=|ker(lambda_i)|`, let `phi` be Euler's totient, and

    R = max_i 15.10 / [k_i phi(m_i)].

Then the full Artin L-function `L(s,rho,K/F)` is holomorphic and nonzero on

    Re(s) > 1 - 1/(R log d_K),
    |Im(s)| < (1/3) tan(pi/8).

The statement includes `s=1`. It is unconditional subject to the imported classical theorems and the explicit character identity. It makes no assertion outside this region. The representation identity forces `rho` to have no invariant vectors, because each induced nontrivial character has zero trivial multiplicity by Frobenius reciprocity.

## Proof

Let `N_i=ker(lambda_i)`, `M_i=K^N_i` and `E_i=K^H_i`. Then `M_i/E_i` is cyclic of degree `m_i`, and `K/M_i` has degree `k_i`. Let `f_i` be the conductor of the primitive Hecke character associated to `lambda_i` over `E_i`. The `phi(m_i)` faithful characters of the cyclic group `H_i/N_i` have conductor `f_i`: they are its powers coprime to `m_i`, hence have the same kernel on every local unit group. Other characters have conductor norm at least one. The conductor–discriminant formula and the absolute discriminant tower formula yield

    d_(M_i) >= d_(E_i)^m_i (N_(E_i/Q) f_i)^phi(m_i)
              >= [d_(E_i) N_(E_i/Q) f_i]^phi(m_i).
    A_i := d_(E_i) N_(E_i/Q) f_i.

Since `d_(M_i)^k_i <= d_K` and `d_(E_i)>=1`,

    log A_i <= [log d_K]/[k_i phi(m_i)].

Ahn–Kwon's theorem applies because the primitive Hecke character has order `m_i>=3`. It gives its zero-free region for `|Im(s)|<(1/3)tan(pi/8)` and `Re(s)>1-1/(15.10 log A_i)`. The displayed bound on `A_i` makes this region contain the common one in the theorem. Each inducing character is nontrivial, so its primitive Hecke L-function is entire. Artin induction and class field theory give an identity of full meromorphic L-functions, including ramified local factors,

    L(s,rho,K/F) = product_i L_(E_i)(s,lambda_i)^(n_i).

Every factor is holomorphic and nonzero in the common region. Its integer power, including negative powers, is holomorphic and nonzero there, so their product has the same properties. In particular no assumption of Artin holomorphy is needed.

The logarithms are nonzero: `K/F` has a subgroup with a nontrivial cyclic quotient of order at least three, hence `K` is a number field of degree at least three and `d_K>1`; each nontrivial cyclic extension has `A_i>1` by the discriminant formula.

## Recovered A5 example

For `G=A5`, the character identities in [the A5 report](../../reports/2026-10-29-a5-hecke-transfer.md) use order-5 characters of `C5` (`k=1`), an order-3 character of `C3` (`k=1`), and an order-3 character of `A4` (`k=4`). The generic theorem therefore gives `R=15.10/2=7.55` for every nontrivial irreducible character, and `R=15.10/8=1.8875` for the five-dimensional character. The same argument applies over an arbitrary base field `F` and measures the bound in the absolute discriminant `d_K`.

**What was checked:** elementary conductor and exponent inequalities; the cited Ahn–Kwon constant and height range appear in the journal's published abstract. An independent character-lattice search, comparison with sharper Hecke results, and full source review are still required. The theorem is not a priority claim and does not replace a family-specific proof of its representation hypothesis.

## Two irreducibles of `PSL(2,7)`

As another concrete family, take `G=PSL(2,7)` of order 168. Its point stabilizer in the faithful degree-seven action is isomorphic to `S4`, so it contains a subgroup `H_12=A4` with quotient `H_12/V4=C3`. The normalizer of a Sylow-7 subgroup is `H_21=C7 ⋊ C3`, whose abelianization is `C3`. Choose nontrivial linear characters `omega_12, omega_21` of these respective quotients. The standard `PSL(2,7)` character table and Frobenius reciprocity give

    Ind_(H_21)^G omega_21 = chi_8,
    Ind_(H_12)^G omega_12 = chi_6 + chi_8,

where `chi_6` and `chi_8` are the irreducibles of those degrees. Hence `chi_6=Ind_(H_12)^G omega_12 - Ind_(H_21)^G omega_21`. For a quick check, the irreducible character values on the identity, order-2, order-3 and order-7 classes are

    degree     1       2       3       7A       7B
       1       1       1       1        1        1
       3       3      -1       0        a      conjugate(a)
      3'       3      -1       0    conjugate(a)   a
       6       6       2       0       -1       -1
       7       7      -1       1        0        0
       8       8       0      -1        1        1

with `a+conjugate(a)=-1`. In `H_21` the six elements of order seven split equally between the two order-seven classes; its fourteen order-three elements split evenly between the two nontrivial quotient values. The multiplicity of an irreducible `chi` in `Ind_(H_21)^G omega_21` is thus `(chi(1)+3 chi(7A)+3 chi(7B)-7 chi(3))/21`, yielding one only for `chi_8`. In `H_12` the three involutions lie in the kernel and the eight order-three elements split evenly between the two nontrivial quotient values. The corresponding multiplicity is `(chi(1)+3 chi(2)-4 chi(3))/12`, yielding one exactly for `chi_6` and `chi_8`.

For `H_21`, the kernel has order seven; for `H_12`, it has order four. The theorem gives the explicit common height range with denominator `15.10/(7*2)=151/140` for `L(s,chi_8)` and `15.10/(4*2)=1.8875` for `L(s,chi_6)`. This applies to every `PSL(2,7)`-Galois extension `K/F` of number fields, with the absolute discriminant `d_K`. It is a concrete consequence of the imported Hecke estimate, not a claim that this comparison is the best previously published bound for those representations.
