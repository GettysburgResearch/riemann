# Native degree interference and microscopic prime-phase rigidity

**PROPOSED component proofs and exact finite computations. No full generalized
native moment, improved zero-free boundary, or RH proof. Independent review
has not been performed.**

This continuation also recovers the entire previously unpushed matching-geometry
packet. Its twelve files are byte-preserved at recovery commit
`8f5d93e6bd488ca3c2360f0a27e03c3f4d8bb1cd`; see RECOVERY.md. Historical
"not pushed" labels in those archived files describe the previous session.

Read [MICROSCOPIC_PHASE.md](MICROSCOPIC_PHASE.md) for the analytic result,
[DEGREE_GEOMETRY.md](DEGREE_GEOMETRY.md) for the exact census, and
[VALIDATION.md](VALIDATION.md) for execution and scope limits.

## New component theorem: rotations shrinking with the scale

For the principal fixed twist, define the actual phase-modified native sum

 A_theta(D,u)=sum mu_K(n) exp(i theta omega_K(n)) chi_n(u) W(Nn/D).

For a fixed nonzero nonnegative compact smooth test, the proposed proof gives,
uniformly for 0<|theta|<=c/log log D,

 Im A_theta(D,1)=c_W theta D/(log D)^2
                 *[1+O(1/log D+|theta|log log D)],  c_W>0.

The error retains its factor theta, even for polynomially tiny rotations.
An analytic-remainder/Cauchy argument is essential; differentiating an
unspecified real-variable big-O term would not justify this statement.
Classical Selberg--Delange/Hankel and fixed-field zero-free inputs are credited.

Genuine sixth-power rows inside the original ball then give

 M_{2k,theta}(D,D^h) >= c |theta|^(2k)
                    D^(2k+h/6)/(log D)^(4k+1).

At k=2,h=21/20, phases theta=D^(-a) therefore fail diagonal size when a<9/32.
The example theta=D^(-1/4) gives the lower bound

 M_{4,theta} >= c H D^(2+1/8)/(log D)^9.

This concerns CHANGED prime coefficients, not theta=0 or a refutation of RH.
An elementary complementary norm estimate transfers the native diagonal
moment to and from phase averages of width D^(-1/2), up to logarithms. It
does not prove either upper bound. For cofinal orders with h_k=o(k) and
excess e_k=o(k), every fixed wider power D^(-a), a<1/2, fails; at the
square-root resolution the average remains equivalent to the native target.
No sharp fixed-order sufficiency at a=9/32 is claimed.

## Direct measurement of the signed cancellation

The full product polynomial, graded by omega_K and by the six unit types,
gives exact small Hermitian Gram matrices. All original prime and composite
columns remain. The code covers every good squarefree ideal in D/2<Nn<=D
and every nonzero Eisenstein element in the row ball.

At D=8192,H=12855, the native fourth moment is 114,923,460,372, but the sum
of separate prime-degree energies is 1,652,703,692,676. Cross-degree terms
cancel about 93.0463% of that energy. This is a finite observation, not an
asymptotic cancellation rate.

The complete singleton sector is positive at D=64,H=79 (+2,496) and negative
at D=256,H=338 (-14,088). Its degree matrix has a negative diagonal entry:
it is not a positive form. At the latter case, the native phase z=-1 has
moment 3,021,246, whereas z=(-2+i sqrt(5))/3 gives 8,892,106/3. Thus the
Möbius phase is not a finite local or global moment minimum. The alternative
is evaluated exactly, without a floating-point optimizer.

## Still open

The large-radical, large-singleton native signed covariance must be bounded
at the actual Möbius endpoint. Grading it measures rather than removes it;
a phase average at a safely equivalent width is not automatically easier.
The new lower theorem prices a failed regularization route, and the positive
stability estimate states its exact boundary. No native power saving results.

## Reproduction

    python -B degree_census.py > replay.json
    python -B -O degree_census.py > replay.optimized.json
    cmp replay.json results.json
    cmp replay.optimized.json results.json
    python -B verify.py
    python -I -S -B verify_phase.py

The full census has nine retained cases (eight main heights plus one pilot).
Separate singleton resolution stops at D=1024; full degree Grams extend to
D=8192. NumPy accelerates explicitly guarded integer arrays. The two checkers
also passed in optimized mode with byte-identical output. Their finite scope
and shared primitive helper are disclosed in VALIDATION.md.
