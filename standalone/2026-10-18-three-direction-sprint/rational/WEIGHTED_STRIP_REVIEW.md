# Independent internal review of the weighted strip gate

Reviewed `../theta/WEIGHTED_STRIP_GATE.md`, actual file-byte SHA256
`cb4ed852b031f6899d1d7717f491317fdde80b5938a511141ec6f0fe4d2b6ee5`.
No blocking error found in the conditional cone consumer or its exact
false-completion construction. This is internal component review, not
external acceptance, cofinal cone membership, or a new zeta strip.

For b=u+it, s=|b|^2, the branch-root identities are
`|Im z|^2=(sqrt(s)-u)/(2s)` and `|z|^2=1/sqrt(s)`.
The displayed semialgebraic inequalities are equivalent to the stated
band and common modulus gap, including b=0. The nonnegative right
side before squaring prevents an extra branch. Under the strict gap,
`Re(b^2)>=eta*|b|^2`, so the matched second node power pays the
ENTIRE weighted modulus resource without a node-count or weight bound.

The union of the disk |z|<d and upper half-plane Im z>B has connected
nonempty intersection and is simply connected. Each canonical factor
has no zero there, and the logarithm normalized at zero therefore
exists on one common connected domain. Its real part is unambiguous.
The global elementary inequality
`|(1-w)exp(w)|<=exp(|w|^2/2)` supplies the stated normal-family bound
even for fractional positive weights. Every derivative of a cofinal
subsequential limit matches the actual target near zero; identity
continuation identifies it on the whole common domain, and Hurwitz
gives the claimed band. No convergence outside that domain is needed.

For B=1/3,R0=4, eta=17/18 is correct. The cited native MGF bound in
THETA_GROWTH.md is in the physical variable, as required here. Its
consequence at radius four is
`|H(z)-1|<=exp(5/11)-1<1`; this suffices for compatibility of the
common gap. This review checks that deduction and normalization,
not a new proof of the whole cited theta-growth theorem.

In the circle construction, N>2M makes the discrete Fourier averages
of both k+r and every nonzero k-r vanish for 2<=k,r<=M. The remaining
k=r term gives precisely A_k. The constant C dominates all cosine
perturbations, so all weights are positive; conjugate weights agree,
their total is C, and the modulus resource is C*R^2. Every branch root
has modulus R^(-1/2)<B. The three-point example has unit variance and
nonreal zero height arcosh(3)/2>1/3, so it explicitly disproves the
unguarded inference from these finite jets to a target band.

The gap is therefore doing essential analytic identification work.
A disconnected local/exterior branch domain cannot support that
identity-continuation step. The actual all-order positive cone
condition with the common gap remains open, and the file correctly
distinguishes logarithmic coefficient positivity from raw moments.
