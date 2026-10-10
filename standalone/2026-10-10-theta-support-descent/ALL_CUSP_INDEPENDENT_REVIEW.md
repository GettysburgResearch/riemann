# Independent review of the all-cusp reflection adapter

Reviewer: the `gauss_analytic` agent, independently of the `theta_review` agent who authored `ALL_CUSP_REFLECTION.md`.

Reviewed content: `ALL_CUSP_REFLECTION.md`, SHA256
`4a0201c3de364c1747726b9561f91ffc825da0aca926528844c543c9bbcd908d`.

Verdict: PASS at the stated source-conditional, full-completion scope. This is an independent AI-agent mathematical review of the new adapter, not independent external verification of the imported theta automorphy or of the generalized moment target.

## Scope of the independent check

I read the complete reviewed file and independently checked its matrix construction, Fourier normalizations, cusp reduction, opposite derivative, Mellin functional equation, transformed support, and Ramanujan consequence. My own preceding derivation of the standard infinity face did not assume the all-cusp extension.

1. **The translation denominator is preserved.** For a primitive original column `(a,c)`, the transformed column `gamma_sigma(a,c)` remains primitive. The six Eisenstein units give the claimed normalization modulo 3. In the ramified case the congruence `AD=1 mod(3C)` is solvable because `(A,3C)=1`; in the unramified case `D=0 mod3` and `AD=1 mod C` are compatible because `(C,3)=1`. The resulting residue matrices match the displayed finite H types. Defining `g=gamma_sigma^(-1)G` then gives back the original unit-normalized first column. Hence the coordinate denominator remains `c|q`, and no transformed denominator C is inserted into the conductor bound.

2. **No new cusp expansions are assumed.** The identities `L_u=J^(-1)T_(-u)J` and `theta(T_u J w)=theta(L_(-u)w)` follow from the supplied `SL_2(Z)` invariance. Changing u by `Z+3O` uses exactly the supplied translation invariance. The quotient has the three classes represented by `0,omega,-omega`, with `-omega` and `omega^2` differing by an integer. Thus every constructed H gives one of the three explicit source functions, with their actual common frequency lattice and coefficient bounds.

3. **The constant correction is accounted for.** The Fourier-index multiplier is applied to `lambda^4 ell`, so its additive translate is `lambda^3 h/q`. The term `-a_sigma F(0)v^(2/3)` in equation (1.7) is necessary and is retained. A horizontal derivative annihilates it and the corresponding constant at every transformed cusp.

4. **The opposite derivative and norm powers agree.** Applying the source coordinate formula to the original g gives `partial_z bar(z')=-1/(bar(c)^2v^2)` and zero height derivative at the origin. The v substitution leaves `alpha(c)^2(Nc)^(1-2s)`. The Bessel Mellin scalar is `i Gamma(s+1/3)Gamma(s+2/3)/(4(2pi)^(2s))`. Consequently equation (3.8), including its minus sign and `R(t)^(-1)`, is correct.

5. **The contour and support constants are exact.** The inherited weight transform is holomorphic for `Re(t)>-5/6`, so moving its line from `3/4` to `-3/4` crosses no kernel pole. Entire theta continuation removes all potential constant-mode residues. The completed Dirichlet series has the required polynomial bounds by the displayed source-style strip argument. The cancellation `R(t)R(-t)=1` yields `V(27x)`, not `V(x)`. Since every nonzero dual frequency has norm at least `1/81`, the support threshold is exactly the stated sufficient condition `X>3R(Nq)^2`.

6. **The Ramanujan application keeps the correct masks.** The two-term expansion of the whole local Ramanujan product is an exact divisor identity with no extra `(g,x)=1` condition. The multiplier `psi(x)chi_k(x)^3 1_{d|x}` has period dividing a fixed bad modulus times `kd`, with the actual k zeros intact. Substituting the inherited raw scale and `a=dg` cancels the k and d norms exactly and gives equation (5.5).

## Boundaries that remain load-bearing

The cancellation applies to the complete frequency sum with the exact inherited reflected weight. It does not apply to an isolated cube index, squarefree theta index, ramified valuation, or dyadic frequency block. It supplies no bound for an uncompleted sum after dropping those terms.

The inactive local Fourier contributions can cancel when all Ramanujan allocations are reunited, restoring activity at every original divisor prime. Therefore the support theorem does not, by itself, reduce the conductor of the reunited whole or prove a diagonal fourth/higher moment. These limitations are correctly stated in the reviewed file.

No numerical test, Lean build, or independent verification of the upstream analytic inputs was performed for this review. The scope is the exact new adapter at the content hash above.
