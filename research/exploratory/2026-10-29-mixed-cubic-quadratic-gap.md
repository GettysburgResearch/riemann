# The missing joint cubic–quadratic estimate in the long dual

**Status.** This records a source-specific obstruction to inserting existing estimates into the long-dual argument; it does not rule out a different method or prove an L-function zero-free region. The displayed exponent comparisons refer to the schematic unit-gcd, unit-divisor block; the exact physical sum has additional coupled masks and profiles. The recent source statements below are not independently verified here.

At the target primal scales, let D=Y^(6/5) be the inverse-column norm and H=D²/Y=Y^(7/5)=D^(7/6) the dual row norm. The special θ coefficient after the first sextic Poisson step is, schematically,

    P_v = D^(−1/2) Σ_{n good sf} α(n)^(−1) γ₂(n) ξ(n)
                         χ_n(v) W(Nn/D),

where χ is a sextic symbol and γ₂ is the cubic Gauss coefficient, with its fixed finite ray corrections. At coprime good arguments, retain the exact elementary factorization

    χ_n(v) = χ_n(v)^4 χ_n(v)^3.                              (1)

The first factor is cubic and the second is quadratic; the formula also retains the original zero when the two arguments collide. Cubic Gauss CRT combines γ₂(n) with χ_n(v)^4 into a G(nv)-type coefficient times the scalar G(v) and fixed reciprocity phases, in the squarefree v, coprime subcase. The quadratic factor χ_n(v)^3 then remains and varies simultaneously with both indices. Its good-prime conductor grows with v and cannot be replaced by a finite ray phase.

## Why direct quadratic sieving loses the diagonal

On squarefree v, write b_n=D^(−1/2)α(n)^(−1)γ₂(n)ξ(n)W(Nn/D) and β_n(v)=b_n χ_n(v)^4. The sought polynomial is Σ_n β_n(v)χ_n(v)^3. The coefficients for the quadratic sum depend on the **same** row v being averaged, so [Goldmakher–Louvel's quadratic large sieve](https://arxiv.org/abs/1112.1642) cannot be applied as if β_n were common.

A valid but very lossy decoupling introduces an independent squarefree row w and majorizes the diagonal w=v by the entire positive double sum. For each fixed v, the quadratic sieve can then be applied in w, giving

    Σ_{v,w sf; Nv,Nw≲H} |Σ_n β_n(v)χ_n(w)^3|²
       ≪ (HD)^ε H(H+D) Σ_n|b_n|²
       ≪ D^(7/3+ε).                                         (2)

The desired signed θ remainder is O(D^(1+ε)); even the existing positive θ upper bound is O(H)=D^(7/6). Thus dropping the same-row coupling loses far too much. An operator-norm product bound for the cubic and quadratic kernels makes a comparable separation and does not recover the diagonal. Restricting v to squarefree rows in this calculation is only a test: (2) is not an upper bound for the full natural-row physical sum unless the remaining row types are treated separately.

## Concrete source ranges

The September 25 [OpenAI cubic Gauss first-moment draft](https://github.com/openai/math/blob/main/preprints/An-unconditional-first-moment-for-cubic-Gauss-sums-September-25-2026/paper.pdf), Proposition 3.1, treats a G(ru) Type-I sum with arbitrary level coefficients but an **unrestricted smooth inner u sum** and level Nr≤X^0.51, where X≈N(ru). If the dual row v is used as r and n as u, their endpoint scales give X=HD=Y^(13/5) and Nr=X^(7/13), with 7/13≈0.53846>0.51. Interchanging the variables puts the outer scale at X^(6/13), within the numerical range, but the remaining factor χ_n(v)^3 is a nonconstant quadratic twist coupling the inner and outer variables, not the unrestricted smooth inner weight in that theorem. Coprimality, fixed ray phases and the actual nonseparable physical kernel still need matching in either orientation.

The same draft's Proposition 5.1 treats Type-II scales X^0.32≤B≤X^1/2. The numerical value B=D=X^(6/13) lies in that interval, but it exceeds X^0.40, where the printed hypothesis requires the specified bounded prime-convolution class. More fundamentally its coefficient β_b is common across the outer row; putting χ_n(v)^3 in β makes it row-dependent. Separating a finite number of ray classes does not remove a quadratic character whose good conductor varies with v. The draft's fixed-angular appendix likewise retains the Type-II coefficient and independence hypotheses. A decomposition of the actual weight into an allowed common β, with all small-prime and mask tails controlled, would be an additional theorem.

The level Voronoi theorem used there, its Theorem 2.4, handles cube-completed cubic Gauss sums with squarefree moving level r, an explicit residual main term and an O(X^ε (Nr)^(1/2)) error. Theorem 2.5 gives a fixed-level spectral second moment `∫_{−T}^T |f_r(1/2+ε+it)|²dt ≪(Nr)^(1/2+4ε)T²`. These are valuable moving-level inputs, but neither is a joint mean uniform in the extra quadratic twist χ_n(v)^3 with coefficients coupled to v. Dunn's [fixed cubic metaplectic cusp-form large sieve](https://doi.org/10.2140/ANT.2025.19.1823) treats Fourier coefficients of a fixed cusp form and has level dependence; it likewise does not state the desired θ-family remainder after subtracting all residual modes.

## A quantitative target

The independently reviewed [separated signed calculation](2026-10-29-signed-theta-mass-cancellation.md) cancels the θ diagonal using the zero integral of the signed row transform. The source absolute nonprincipal off-diagonal is O(D^(41/36+ε)) at H=D^(7/6); the schematic primal target needs O(D^(1+ε)), a fixed D^(5/36) gain. The [self-loop note](2026-10-29-theta-inverse-self-loop.md) shows that the unit-gcd term of the current θ proof obtains its bound from the original same-scale long-inverse mean, with no scale contraction.

A genuine next theorem would therefore have to retain (1) and the same v through the quadratic and cubic sides, or control the exact signed two-column Poisson kernel before making a positive bound. It must include the residual θ spectrum, moving good-prime conductors, finite ray/unit sectors, squarefree and nonsquarefree row strata, and the fixed shared smooth profiles; a bound for a fixed twist, a full positive double average like (2), or a mere projection onto finitely many fixed Gauss modes does not suffice. No source found in this targeted search states that theorem.
