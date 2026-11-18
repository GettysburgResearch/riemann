# An exact multiplicity-aware polynomial approximant

Agent: li_advocate. Date:2026-11-17. Status: self-contained elementary derivation, independently reconstructed from the parent's double-root target, then generalized without reading the equivalence agent's proof. No claim of historical or publishable novelty. This establishes an explicit finite-dimensional calculation; it does not resolve the arithmetic infinite-zero problem.

## Exact theorem

Fix integers m≥1,N≥0, set L=N+m and D=∏_(j=1)^m(L+j). Let P(z)=(1−z)^m. Among all complex polynomials A of degree≤N, the unique minimizer of

(1/(2π))∫_0^(2π)|1−P(e^(iθ))A(e^(iθ))|² dθ

has coefficients

a_n=binom(n+m−1,m−1) · ∏_(j=0)^(m−1)(L−n−j)/D, 0≤n≤N.

The exact minimum is

1−[∏_(j=0)^(m−1)(L−j)]/[∏_(j=1)^m(L+j)].

For fixed m as N→∞ this equals m²/N+O_m(N^(−2)). The reciprocal coefficients are binom(n+m−1,m−1), so the optimal window is degree m in n; the optimal coefficient itself has degree2m−1. N≥0 is allowed. m=1 gives minimum1/(N+2); m=2 gives2(2L+1)/[(L+1)(L+2)].

## Proof

Let f(x)=binom(x+m−1,m−1)·∏_(j=0)^(m−1)(L−x−j)/D, interpreting the binomial as a polynomial in x. Its degree is2m−1. It vanishes at x=−1,…,−(m−1) and x=N+1,…,N+m=L. Also f(−m)=(−1)^(m−1), because ∏_(j=0)^(m−1)(L+m−j)=D. For m=1 the first zero list is empty; the same identity holds.

Extend the finite coefficient array a_n=f(n),0≤n≤N, by zero elsewhere. If R=1−(1−z)^m A=∑_(k=0)^L c_k z^k then

c_k=δ_(k0)−∑_(j=0)^m(−1)^j binom(m,j)a_(k−j).

Using the polynomial values f instead of the zero-extended array gives the same formula without δ_(k0): for k≥1, every missing index lies in one of the two zero lists; for k=0, the only extra term is (−1)^m f(−m)=−1, which exactly accounts for δ_(k0). Therefore

c_k=−∇^m f(k), 0≤k≤L,

where ∇f(k)=f(k)−f(k−1). In particular c_k is the restriction of a polynomial in k of degree≤m−1. Its mth forward difference vanishes. Hence for every n=0,…,N,

∑_(j=0)^m(−1)^j binom(m,j)c_(n+j)=0.

This is precisely the orthogonality of R to every column z^n(1−z)^m in the coefficient Hilbert space. Thus R is the orthogonal residual of1 from P times the degree≤N polynomials, proving optimality; injectivity of multiplication by nonzero P proves uniqueness. Parseval identifies this coefficient norm with the circle norm. Finally

||R||²=⟨R,1−PA⟩=⟨R,1⟩=c_0=1−a_0,

which is the stated product ratio. For fixed m, expanding log∏_(j=0)^(m−1)(L−j)/(L+j+1) gives −m²/L+O_m(L^(−2)), yielding the asymptotic.

## Evidence and interpretation

`experiments/code/multiplicity_general_exact.py` performs exact Fraction residual, orthogonality, and norm checks for80 pairs m=1,…,10 and N∈{0,1,2,3,5,10,30,100}. These finite checks corroborate the all-m proof rather than replace it.

The relevant primary-source comparison is Bettin–Conrey–Farmer, arXiv:1211.5191v1 p.3: the paragraph before Theorem2 gives a multiplicity-squared asymptotic for optimal polynomial approximation, while Theorem2's explicit triangular reciprocal window assumes simple roots. The exact formula above is consistent with that asymptotic and extends the simple boundary-root model by using a degree-m window. No contradiction to BCF is alleged. The finite double-root counterexample to the unchanged linear window is independently reviewed in `audits/adversarial_reviews/toy_advocate.md`.

An exact continuation question is to treat two roots separated by θ=c/N and obtain the uniform asymptotic interpolating constant as c varies, then compare an adapted window to the optimum. An arithmetic continuation would require boundedness of residue/principal-part sums for ζ, including multiplicities; the polynomial theorem supplies no such estimates.
