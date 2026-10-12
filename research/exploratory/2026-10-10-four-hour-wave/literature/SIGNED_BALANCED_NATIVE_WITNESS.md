# A native signed remainder surviving diagonal completion

Status: exact arithmetic witness and source-qualified structural deductions.
The remaining signed moment estimate is open. This finite computation proves
no asymptotic lower bound and gives no new zero-free region.

## N1. Frozen source and the precise remainder

The source is PR #914, commit
`0cc0428fedbbfc340044c7451b3d392c1da9a103`, especially
`CONDUCTOR_SECTORS.md` Sections 7–10 and `A2_COMPLETION.md` Sections 6–7.
Their SHA256 values are respectively
`c160bbb1b1d7c6bcc5514d496ad41f15fd17ea3d36206b0d05cfa0d7d6503983`
and
`d99eade56807077b07e5ec1325001f1592115db216e1e10e6a3906a3e01f0aad`.
The accompanying checker verifies these literal files before calculating.
Those analytic controlled-sector and Poisson statements are imported;
the finite computation below is native arithmetic.

For a Hermitian 2k-tuple let g1 be the product of primes occurring exactly
once and g2 the product of nonprincipal primes occurring exactly twice.
The remaining signed quantity is exactly

    R_k = sum[t : g1 != 1, (Ng1)^2 Ng2 > H^2] c(t) S_t.

Each S_t retains all principal masks and all sextic character zero
extensions. For the smooth source row test, the proved controlled sectors
give M_2k = R_k + O(H D^(k+epsilon)). Bounding this actual signed R_k at
that scale remains the unpaid task.

## N2. Subtracting the product diagonal leaves R_k unchanged

If the product of the k left ideals equals the product of the k right
ideals, unique prime factorization gives r_p=s_p at every prime.
Every occurring prime then has multiplicity 2r_p>=2; hence g1=1.
Consequently the product diagonal is disjoint from the defining support
of R_k, at every k. This remains true at k>=6, where a principal residual
can have exponent +/-6: such a prime is still not a singleton.

Thus subtracting the original product-column diagonal does not remove
even one tuple from R_k. The source's full signed first-Poisson diagonal
identity is useful because it removes a large *dual positive volume*
before estimating the centered expression. It is not an estimate of
the nonprincipal singleton remainder.

The A2 inverse has a further exact constraint. For correction triples
t=(c,d,e) put s_t=c^3 d^3 e^4. Its pulled-back diagonal is

    s_t x1 x2 = s_t' y1 y2,

not equality of the factor pairs. Already (a,b) and (b,a) are distinct
pairs on the same product diagonal. Replacing this covariance by the
pair diagonal changes the centered expression.

## N3. The signed common-factor collapse is inert on the leading face

The exact source regrouping in `BELOW_DIAGONAL_SOURCE_ADAPTER.md`
has c_j=f m_j, g=gcd(c1,c2), d_j=c_j/g and local signed factor

    sum[f|g] mu(f) 1[(g/f,k)=1] = mu(g) 1[g|k].

It remains valid with the balanced residual coefficient R_L(b c_j):
that coefficient is independent of f in these coordinates. After k=g h
the coupled Fourier profile is

    Psi(H Nh / (Ng Nd1 Nd2)).

On the face where all 2k original prime factors are pairwise distinct,
the two product columns are coprime. Therefore b=g=f=1 and the displayed
signed factor is identically one. The entire leading singleton face
survives this cancellation unchanged. For k=2 and four prime columns,
the original four Mobius signs also multiply to +1. Any saving there
must come from the actual nonprincipal row correlations or their exact
centered transforms, rather than an auxiliary divisor cancellation.

## N4. An exact finite witness with the actual inverse coefficients

Work in O=Z[omega], omega^2+omega+1=0, with the principal finite character
nu and excluded primes above 2 and 3. Take D=30 and a fixed nonnegative
smooth W with disjoint tiny bumps of value 1 at

    7/30, 13/30, 19/30, 31/30,

each bump supported within distance1/60 of its center. Only ideals of
these four rational prime norms meet W(Nn/D). The four primary generators
are -2-3omega, 1-3omega, -2+3omega, 1+6omega, together with their
conjugates: eight distinct prime ideals. Every actual inverse coefficient
is mu(n) W(Nn/D)=-1.

Take H=40. A fixed smooth radial nonnegative Phi can equal 1 for Nu<=40
and 0 for Nu>=41 after scaling by sqrt(H). Since lattice norms are
integers, its row values are exactly the 150 nonzero rows in this finite
calculation. The u=0 term vanishes. This realizes the witness within the
`CONDUCTOR_SECTORS.md` smooth-majorant contract. It does not identify this
compact spatial Phi with the different Fourier-compact Poisson test in
`A2_COMPLETION.md`.

The checker computes the literal sextic symbol in each residue field
F_q: omega maps to -A/B modulo q for pi=A+Bomega, and a nonzero residue
v maps to v^((q-1)/6), identified with its exact Eisenstein unit. At a
nonunit the symbol is exactly zero. All arithmetic uses integer pairs
in Z[omega], with no floating point or sampling.

The result is:

| Quantity | Exact value |
|---|---:|
| Full native fourth moment |16752|
| Critical signed remainder R_2 |1176|
| Controlled complementary contribution |15576|
| Original product-column diagonal |15564|
| Pairwise-distinct leading contribution to R_2 |456|
| Critical Hermitian tuples |3696|
| Critical tuples removed by the product diagonal |0|
| Pairwise-distinct leading Hermitian tuples |1680|

The full Hermitian expansion has 4096 tuples. The checker independently
compares direct |A_u|^4 with the exact expansion, compares each tuple's
literal character product with its residual character and zero mask,
and verifies that all 1680 leading tuples lie in the critical off-diagonal
region. Removing principal zero extensions and replacing sextic phases
by cubic phases are rejected by explicit negative controls.

This witness demonstrates that the exact surviving quantity can be
nonzero and positive, including on the coprime leading face. Its small
fixed parameters do not test an asymptotic conjecture, imply a violation
of the target estimate, or show that the remainder is large in general.

## N5. The remaining analytic contract after the useful centering

At the longest balanced fourth-moment core L=D^2 and H=D^(1+theta),
0<theta<1, the first Poisson frequency has size Hcal=L^2/H=D^(3-theta).
Thus Hcal/L=D^(1-theta)>1 on the unchanged b=f=1 component. The completed
coefficient does not improve this ratio.

For the source's Fourier-compact row test and its exact R_L, the leading
centered expression is

    E_cen = (1/L) sum[k != 0] sum[c1 != c2, (c1,c2)=1]
        a_xi(c1) conjugate(a_xi(c2))
        chi_c1(k) conjugate(chi_c2(k))
        R_L(c1) conjugate(R_L(c2))
        Psi(H Nk/(Nc1 Nc2)).

Its contribution to the source normalized moment is (H/L) E_cen.
An estimate |E_cen| << L D^epsilon would therefore pay this leading
component at size H D^epsilon. It is still open for the actual balanced
divisor/Gauss coefficients and the coupled Fourier profile. The other
common-factor components and moving masks must also be paid before
claiming the full moment.

The full signed diagonal centering changes the analytic target by
removing its positive baseline. The native tuple support, conductor
ratio and the leading signed correlations remain. A conductor-uniform
centered bilinear estimate, with the reconstructed A2 covariance above,
would be a concrete next theorem; a bound for positive completed energy
alone does not supply it.

## Reproducer

    python literature/check_signed_balanced_native.py
    python -O literature/check_signed_balanced_native.py

Run from this wave directory, or use the absolute script path. Both
executions check the frozen source files under
`/workspace/.riemann-research/moment-sources/914/standalone/` (override
with `--source-root`) and emit deterministic JSON. Analytic claims are
source-qualified and the generalized moment/RH flags stay false.
