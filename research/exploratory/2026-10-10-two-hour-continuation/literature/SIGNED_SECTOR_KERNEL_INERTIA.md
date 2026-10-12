# The complete finite signed-sector kernel is indefinite

Status: proved finite-kernel inertia from exact source diagonal removal and
the already certified positive full signed compact witness. This does not
rule out a signed trace estimate or extend the source coefficient class.
No negative eigenvector is claimed realizable by factorable source weights.

## SI1. Complete radial source kernel and exact sector filter

Use the physical eight-prime source family and exact critical classification
in `FULL_SIGNED_COMPACT_WITNESS.md`, SHA256
`1c0a1718080e6f763a3531f9f9a8f8fcd31868c48d241290406fe4cef61644ca`.
The eight distinct prime ideals have norms 7,7,13,13,19,19,31,31, at D=30
and H=40. The fixed smooth norm window has precisely these nonzero ideal
samples. All prime Möbius values are -1, so every four-prime coefficient
has positive sign. The finite family is a literal instance of the source
norm-filtered family, not an asymptotic prime-only replacement.

Let alpha=(p,q) and beta=(r,s) range over all 64 ORDERED prime pairs.
Define M_alpha,beta to be the complete source radial row trace of
`chi_p(u)chi_q(u) conjugate(chi_r(u)chi_s(u))`, multiplied by the actual
left/right norm/ray/Möbius pair coefficients and the exact PR914 critical
indicator `g1!=1, Ng1*sqrt(Ng2)>H`. Use the genuine Schwartz companion
Phi_delta of the frozen compact Fourier witness, delta=10^(-12).
The full row sum converges absolutely. Swapping alpha,beta conjugates
the character and coefficients and preserves the critical indicator,
so M is Hermitian. Every moving principal mask is retained.

On a diagonal alpha=beta, the tuple is `(p,q,p,q)`. Every appearing
prime occurs at least twice, so g1=1 even if p=q. Thus

\[
                   M_{\alpha,\alpha}=0,\qquad\operatorname{tr}M=0.
\tag{SI1}
\]

This is the selected signed critical kernel, not the full moment's
positive Gram matrix. Its diagonal removal is exactly the source sector
definition; it is not a newly chosen subtraction.

## SI2. The certified positive form forces a negative eigenvalue

The complete all-ones quadratic form of M is precisely the actual full
signed R2 for this family and Phi_delta. The frozen independent normal
and optimized receipt for the compact source, before smoothing, has SHA256
`46e642fa1c4774f1d31166de547731762fa7f89ac3f0a3ce6b0c500f91571d93`.
It gives R2 approximately8852.5068916. The complete source Schwartz
perturbation bound in the frozen proof and independent full-C review is
less than0.35. Consequently

\[
                         \mathbf1^*M\mathbf1>8852.
\tag{SI2}
\]

Hence M is nonzero. A nonzero trace-zero Hermitian matrix cannot be
positive semidefinite. More quantitatively, its largest eigenvalue is
greater than8852/64 by the all-ones Rayleigh quotient. Its remaining
63 eigenvalues sum to the negative of that largest eigenvalue, so

\[
             \lambda_{\min}(M)<-\frac{8852}{64\cdot63}
                              =-\frac{2213}{1008}.
\tag{SI3}
\]

This is a property of the complete finite radial selected-sector kernel,
including the paid genuine Schwartz source. It is stronger than an
indefinite isolated-prime factor. It is still not an inertia statement
about the full moment, which remains positive.

## SI3. The fully coprime leading face has the same obstruction

Restrict the ordered pair basis to p!=q, leaving 56 pairs, and set an
entry to zero unless all four prime ideals are distinct. This is the
actual leading b=f=g=1 face in the same finite instance. Its matrix L
is Hermitian with exactly zero diagonal. Its complete all-ones form is
the leading compact witness in `FOURIER_COMPACT_BALANCED_TRACE.md`,
SHA256 `480cb96c363ddddf5d35306b0b25739c110b6f407e8101a43aaddae04605f120`.
The frozen independent receipt SHA256
`fa2e817911ebaee9411f3b617149fa55ad98e9b7abc6e604dd6b3a1d6cc6aae8`
gives approximately3916.766519, with paid Schwartz error below0.001.
Therefore its genuine Schwartz form is greater than3916 and

\[
             \lambda_{\min}(L)<-\frac{3916}{56\cdot55}
                              =-\frac{979}{770}.
\tag{SI4}
\]

Every leading tuple has four distinct actual prime ideals and remains
critical at H=40. Equal prime norms have not been conflated with equal
prime ideals. No zero or principal mask is discarded.

## SI4. Exact consequence and finite control scope

A positive-kernel inequality such as
`|M_alpha,beta|^2<=M_alpha,alpha*M_beta,beta` would make every off-diagonal
entry zero because the diagonal is zero. The certified nonzero signed
form excludes that adapter for this complete finite selected kernel.
A different signed linear trace bound, higher correlation estimate or
restricted source-coefficient argument can still hold. The negative
eigenvectors are arbitrary vectors in this finite pair space and are
not asserted to factor into the source's literal one-column weights.
No new source moment bound or impossibility theorem follows.

`check_signed_sector_inertia.py` independently reconstructs both actual
prime fields at each norm and all 150 lattice rows of the auxiliary
spatial disk Nu<=40. It computes the complete 64-by-64 critical kernel
and 56-by-56 disjoint leading kernel with exact Eisenstein integers.
The auxiliary exact forms reproduce the earlier1176 and456 witnesses,
their diagonals vanish, and explicit nonzero off-diagonal entries give
negative two-by-two determinants. This auxiliary disk is not the compact
Fourier source. The actual Schwartz-source inertia above instead uses
the imported fully audited compact-source receipts and complete error
budgets, whose hashes the checker separately binds.
