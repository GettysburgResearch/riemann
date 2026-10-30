# Sixth-power obstruction with a positive inverse length

**Status:** Proposed necessary condition, requiring independent review. It proves no improved zero-free region and does not refute the stated range of the OpenAI marked moment.  
**Scope:** The unrestricted element-row family, trivial fixed character, one prime slot, and a suitably chosen fixed smooth inverse profile. The row family includes sixth powers and is not restricted to sixth-power-free or squarefree rows.  
**Inputs:** Standard ideal counting/prime ideal theorem for the Eisenstein field, a zero of the Riemann zeta function on the critical line, Mellin inversion and analytic continuation. The definitions and desired uniform moment are those of [Lemma 17.1](https://wcook04.github.io/plectis-atlas/papers/The-Quasi-Riemann-Hypothesis-September-30-2026.html).  
**Novelty:** No priority claim. The obstruction extends the elementary unit-supported sixth-power example to an open range of positive inverse lengths; no literature search for this exact observation has been completed.  
**Smallest remaining gap:** Independent review of the primitive-primary normalizations and the smoothed Mellin noncancellation.

Fix m>0 and 0<r<m/3. If a bound of the form

    Σ_{u:0<q_u≪Z^m} |M_u(Z^r;W) Q_u|² ≪_ε Z^{m+ε}

is claimed for every ε>0, uniformly in the permitted prime supports and coefficients, then necessarily z≤5m/6. This is for one slot of exponent z, a fixed finite exclusion set S, and a suitable fixed smooth annular W; all conditions of the claimed theorem must otherwise be retained.

## Proof

Let F=Q(√−3), and use its standard primary generators and norm q. Take ν=1. Pick a critical-line zero ρ=1/2+iγ of ζ(s). Since ζ_F(s)=ζ(s)L(s,χ_{−3}), ζ_F vanishes at ρ. A nonnegative smooth W supported in a sufficiently short fixed annulus around 1 has Mellin transform \widehat W(ρ)≠0: choose the annulus short enough that all phases `exp(iγ log x)` lie in an open semicircle. This W is chosen once, independently of Z.

Write

    S_W(X) = Σ_{(n,S)=1} μ(n) W(q_n/X).

For Re(s)>1, its Mellin transform is

    ∫_0^∞ S_W(X) X^{-s} dX/X
       = \widehat W(s) / ζ_F(s) × ∏_{p∈S}(1−q_p^{-s})^{-1}.

The finite Euler factor is holomorphic and nonzero at ρ. If S_W(X)=O(X^{1/2−η}) as X→∞ for some η>0, the integral would analytically continue to Re(s)>1/2−η, contradicting the pole at ρ. Therefore for every η>0 there are arbitrarily large X with

    |S_W(X)| ≥ X^{1/2−η}.                              (1)

Now fix z>5m/6 and put X=Z^r. Take one prime slot consisting of all primary primes in a fixed proportional annulus of norms ≍Z^z outside S, with coefficients 1 and a fixed nonnegative smooth slot profile positive on a smaller annulus. By the prime ideal theorem, the normalized slot sum on rows considered below is ≫Z^{z/2}/log Z.

Choose primary prime elements v of norm in a fixed sufficiently small proportional annulus `q_v≍Z^{m/6}` outside S, and set u=v^6. There are ≫Z^{m/6}/log Z distinct such rows, all with q_u≪Z^m. Because z>5m/6, all the slot primes have norm greater than q_v, and hence `χ_p(v^6)=1` on the slot support. The slot contributions add positively. On the inverse support, the symbol is 1 when v does not divide n, and zero otherwise. Standard ideal counting gives, uniformly for the chosen v,

    |M_{v^6}−Z^{−r/2}S_W(Z^r)| ≪ Z^{r/2−m/6}.        (2)

Indeed the number of ideals n in the fixed annulus with v|n is O(Z^r/q_v), and is zero when that ratio is below the fixed support threshold. The common character orientation ± is irrelevant on these rows.

Choose η>0 with `rη<m/6−r/2`, possible since r<m/3. Along the sequence X in (1), set Z=X^{1/r}. Equation (2) then makes `|M_{v^6}|≥(1/2)Z^{−rη}` uniformly for every selected v and all sufficiently large sequence points. The total second moment is at least

    ≫ Z^{m/6+z−2rη}/(log Z)^2.

If z>5m/6, choose η>0 sufficiently small that the exponent is strictly larger than m, and choose the ε in the purported upper bound smaller than that positive excess. This contradicts the claimed uniform bound. □

This obstruction does not distinguish the two sufficient faces `r+2z<m` and `2r+8z<3m`, and leaves a substantial interval between the current moment range and z=5m/6. It also gives no obstruction for the physical sixth-power-free row family without a separate transfer argument. The lower bound uses ideal-prime counting and a fixed admissible choice of weights; it does not assume a conjectural Möbius estimate.

## A conditional diagonalization check

Fix any admissible inverse polynomial and any disjoint finite prime-slot supports. Independently multiply each slot coefficient by an independent uniform unit-complex random variable, holding its modulus and the prime support fixed. For every row u, independence and character orthogonality in the random phases give the exact identity

    E |Q_u|² = ∏_i Z^{−z_i} Σ_{p∈P_i} |a_i(p)W_i(q_p/Z^{z_i})|² 1_{p∤u},

up to the fixed zero extensions already built into ψ. In particular this expectation is O(1) for a bounded number of fixed-profile slots, uniformly in their lengths and coefficients. Consequently, **if** the corresponding unmarked inverse moment `Σ_u |M_u|²≪Z^{m+ε}` is available, then the marked moment satisfies the same upper bound in expectation for arbitrary z_i, with no `r+2z` or `2r+8z` restriction arising from the diagonal terms. Markov's inequality gives the corresponding estimate with any fixed positive power loss for all but a vanishing fraction of randomized phases.

This is an exact conditional identity and does not prove the worst-case uniform marked moment: the sixth-power obstruction above uses deterministically aligned coefficients, and the source detector requires uniformity over such choices. It isolates off-diagonal prime correlations as the issue that a range extension must control.
