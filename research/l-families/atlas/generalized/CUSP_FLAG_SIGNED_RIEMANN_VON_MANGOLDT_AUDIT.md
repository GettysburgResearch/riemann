# Independent audit: native signed cusp-flag counting law

Status: PASS at the exact frozen source. The five-file proposed packet
remains byte-preserved; acceptance is recorded in this separate audit.

Scientific source: 24bfc73fc9aa3ba115902340affa8727dfa18970.
Authoring base: a27781310ded92125ef16d97d78db4d97cec4c1b.
Programme import: c54873f857edc67aad7c0f6f835dc377cef848b7.
Review date: 2026-08-31.

Root and a separate non-author reviewer read the complete
[written proof](CUSP_FLAG_SIGNED_RIEMANN_VON_MANGOLDT.md), producer, fixture,
source manifest and tests. Both independently reviewed the analytic
argument, reconstructed actual cusp-form arithmetic by other routes,
and checked the frozen dependencies. No repair was required.

## Accepted statement and exact count

Fix any level-one even weight k with d=dim S_k>=2. Retain the full Miller
basis, the specified first-coefficient functional ell=[q], W=ker ell,
and the original completed period quotient Q_k=det I/det I_W.

For every T>=2, with the upper cutoff inclusive,

    N_Q^+(T) = sum_(rho: 0<Im rho<=T) ord_rho Q_k
             = (2/pi) T log(T/(2pi e)) + O_k(log(T+2)).

The sum is over ALL real parts and uses NET multiplicity: zeros positive,
poles negative, after common determinant zeros cancel. This signed count
need not be monotone. The theorem does not give this asymptotic for the
unsigned zero count, the pole count, or their absolute sum.

The implied constants depend on the fixed weight/source. Neither an
effective numerical error constant nor uniformity in weight is supplied.
No period values, phases or analytic zeros were computed by the fixture.

## Analytic audit

1. With w=s+k-1, P=d!, and
   A=pi^-s (4pi)^(-s-k+1) Gamma(s) Gamma(s+k-1), write
   I/A=zeta(2s) D(w). Cauchy--Binet on finite coefficient panels, followed
   by the absolutely convergent Gram limit in a right half-plane,
   gives a nonnegative determinant Dirichlet expansion.

2. The full determinant's first nonzero tuple is (1,...,d). On W the
   coefficient column n=1 is ZERO and the first tuple is (2,...,d).
   Both products are d!, and both squared leading minors are one.
   Thus for either rank r=d or d-1,

       F_r(s) = P^w det(I_r(s)/A(s)) -> 1

   uniformly as Re s tends to infinity. The zeta(2s)^r factor only
   adds positive square-frequency multiples and changes no leading
   coefficient. Rational frequencies have a genuine positive gap;
   local finiteness and right absolute convergence are justified.

3. U_r=[s(s-1)]^r det I_r=det J_r is entire of order at most one by
   the actual theta estimate EF5--EF11, not by an assumed automorphic
   identity for the quotient. Endpoint values are nonzero positive
   Gram determinants up to the displayed even pole-clearing signs.
   Schwarz conjugation and reflection U_r(s)=U_r(1-s) hold.

4. H_r=(s-1)^r F_r=P^w U_r/(s A)^r is entire of order at most one.
   Here 1/(s A) is entire: the gamma pole at zero cancels the extra
   factor s. The entire reciprocal gamma factors have order one.
   F_r is holomorphic away from its possible pole at s=1.

5. Reflection gives the exact factor P^(2s-1)[A(1-s)/A(s)]^r.
   On a fixed vertical strip the absolute gamma ratio has power
   |t|^(2-4 Re s); the weight shifts cancel from that exponent.
   For a sufficiently far right C>2, F_r is bounded there, and on
   Re s=1-C it has growth O(|t|^(r(4C-2))). Pole-clearing raises the
   latter exponent to r(4C-1).

6. The polynomial fixed-strip bound is proved, not inferred from
   finite order alone. Divide H_r by (s+D)^B with D>C+1 and an
   integer B>=r(4C-1). The result is holomorphic on the strip and
   bounded on its vertical edges. Multiplication by exp(epsilon s^2)
   damps the horizontal edges because the global growth can be
   bounded by exp(O(|s|^(3/2))). Apply the maximum principle first
   as the rectangle height tends to infinity, then epsilon to zero.

7. Choose c far enough right that |F_r(c+it)-1|<1/2. For large T,
   B_T(z)=[F_r(z+iT)+F_r(z-iT)]/2 is holomorphic in the disk of
   radius 4c about c, because its shifted poles lie outside.
   Its centre is Re F_r(c+iT)>1/2. The larger fixed-strip bound and
   Jensen give O(log T) zeros in the disk of radius 2c. Hence
   Re F_r(x+iT) has O(log T) crossings on [1-c,c].

8. At a nonexceptional height, each segment between crossings stays
   in one open half-plane, so its NET change of argument is at most
   pi in absolute value. This proves an O(log T) horizontal argument
   bound; it does NOT bound total variation of the argument.
   The gamma factors and polynomial pole-clearing factors add only
   O(log T) across this fixed horizontal segment.

9. Right normalization and reflection place every zero of U_r in
   a finite vertical strip. The real zeros form a finite set.
   The rectangle argument principle, conjugation and reflection
   give N_r^+(T)=theta_r(T)/pi+O(log T), with real zeros absorbed
   into the fixed error. Continuous Stirling branches give

       theta_r(T) =
           2r T log(T/(2pi e)) - T log(d!) + O_k(1).

   The log(4pi^2) completion, two gamma factors, and unchanged
   coordinate s are all necessary for these constants.

10. Applying Jensen directly to F_r near c+iT also gives
    O(log T) zeros in a unit-height window covering the whole
    vertical zero strip. Alternatively, descending nonexceptional
    heights stabilize each determinant count at the inclusive
    cutoff. Exceptional heights therefore obey the same formula.
    This uses monotonicity only for the separate positive determinant
    counts, never for their signed difference.

11. Subtract the rank d-1 formula from the rank d formula. The two
    -T log(d!) terms cancel exactly, while 2d-2(d-1)=2. The real
    s(s-1) factor in Q=U_d/[s(s-1)U_(d-1)] contributes no
    positive-height divisor. Common zeros cancel pointwise, even
    when multiplicities exceed one.

## Independent exact replay

The root did not obtain its reference Miller coefficients by invoking
the packet's two authenticated family constructors. It formed Delta by
the finite Euler product q product(1-q^n)^24, E4/E6 by divisor sums,
formed the cusp basis Delta^j E4^(3(d-j)) M_r, and inverted its leading
coefficient matrix exactly. This gives the complete Miller basis through
q^(d+2) at every recorded source.

All 20 recorded basis digests matched, including (d,r)=(10,4),(20,8).
A row-exterior-algebra computation, independent of the producer's
Gaussian minor routine, reconstructed all 40 determinant coefficient
maps and all 184 nonzero entries. Direct SymPy exact Gram determinants
agreed with every Cauchy--Binet weighted sum.

Held-out checks added 16 native two-tail determinants at the six d=5
residual classes and two smaller sources. Twelve generic rational
Gram identities covered ranks 1--3 and weight exponents 1--4.
Seven finite signed-divisor cutoffs checked common multiplicities,
negative net counts, real/lower-half-plane exclusions, and inclusive
upper endpoints. These finite arrays are algebraic controls, not
samples of the continued cusp-period divisor.

The independent non-author review used a third Miller construction
based on Delta^d M_r and powers of j-744. It checked 20 recorded and
six held-out sources, all 40 native maps/184 entries, 16 two-tail
native matrices, 48 rational Gram identities, and seven signed
cutoff controls.

Root additionally rejected 27 tamper/type/cap variants in both modes.
The separate reviewer rejected 43 additional variants in both modes.
Resealed semantic attacks used an already authenticated complete
reference report, not repeated expensive reconstruction per attack.

## Runtime and source verification

- Supplied 32 tests: root normal PASS (6.439 s), optimized PASS
  (6.309 s). Separate reviewer normal PASS (4.939 s), optimized
  PASS (5.003 s).
- Producer --check: normal and optimized PASS.
- Root alternate-arithmetic audit: normal and optimized PASS.
- All ten primitive Git-blob/LF-SHA-256 bindings and four local
  artifact locks independently match.
- Ruff check/format and complete authoring-base diff check PASS.
- The fixture payload is unchanged and remains proposed; this
  separate audit records independent acceptance.

Report emission has one benign serialization distinction: the checked-in
fixture sorts rational-frequency keys numerically, while the CLI emitter
uses ordinary lexicographic JSON string-key sorting. Normal/optimized
emissions are byte-identical to each other and TYPED CANONICALLY identical
to the fixture, but are not LF-byte-identical to that fixture. Manifest
emissions are LF-byte-identical to the manifest in both modes.

Fixture LF SHA-256:
473f04cfe46ea9483e7d8c1e1e8fffc2ab0173ef134e28b1b95d3eba57ca3f51

Payload SHA-256:
0ba0cc755d9d8257ab6f22798245c8fc50ee0b8aca8d6ba9c0c4f43d5731b83d

Emitted report LF SHA-256:
d51db31b2d682728674e0c5f79d2ca4a0e2566f835926c396c2acac348dd8d4a

Frozen source Git blobs:

    proof     64c12988bda07d931fe4b9971f005ed5c238505f
    producer  321b1a0be854234a60978153c226f4fdd534dc5f
    fixture   502b22ef32ac56009453690e6189e98b1c0921c8
    manifest  9cb1fbaf70cc1bae4afdec0bbf5c448cc58a72b8
    tests     50daf5cafec811882d48a3de2e02077f999ea88d

## Classical sources and remaining boundary

The root directly read the relevant original passages in
[Trudgian, sections 2--3](https://arxiv.org/pdf/1208.5846v2),
including visual inspection of the real-part crossing and Jensen pages;
[Tao's classical counting framework](https://terrytao.wordpress.com/2014/12/15/254a-supplement-3-the-gamma-function-and-the-functional-equation-optional/);
[Tao's strip-damping exercise](https://terrytao.wordpress.com/2009/02/28/tricks-wiki-give-yourself-an-epsilon-of-room/);
and the [DLMF Stirling expansion](https://dlmf.nist.gov/5.11).
They supply classical context, not a theorem about this determinant
quotient by citation alone. The source-specific proof above is what was
audited. Remote source bytes are not part of the offline hash contract.

This accepts a native fixed-weight signed counting law, not a new general
Riemann--von Mangoldt theory. It neither locates zeros on the critical
line nor proves cancellation, absence/finiteness of additional poles,
a positive explicit formula, RH or GRH. Quantitative distribution of
the reduced quotient's separate zeros and poles remains open here.
