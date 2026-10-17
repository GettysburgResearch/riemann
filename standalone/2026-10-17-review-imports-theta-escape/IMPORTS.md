# Version-pinned imports and application map

These are attributed analytical imports with exact primary links, not copies of the complete papers. Neither manuscript's full PDF bytes were obtained in the execution container. No hash of an undownloaded PDF is claimed. See `SOURCES.md` for reading scope and redistribution boundaries.

## A. Frei--Sofos--Widmer (FSW), arXiv:2610.18491v2

*Some applications of the quasi-Riemann hypothesis to class groups and small generators of number fields*, Christopher Frei, Efthymios Sofos and Martin Widmer, revision 14 October 2026.

Use QRH(delta) to mean zero exclusion in Re(s)>1-delta, with 0<delta<=1/2. **The authors explicitly state their results conditionally on QRH because they have not independently checked the upstream quasi-RH arguments.** Their abstract's “unconditional” phrasing is not an independent validation of those arguments. This qualification corrects the looser description in the preceding chat.

For a Galois extension L/K and conjugacy class C in G, Theorem 1.1, assuming QRH(delta) for zeta_L, gives

    |pi_C(x) - (|C|/|G|) Li(x)|
      <= c1 (|C|/|G|) x^(1-delta)
              log(Delta_L^(1/delta) x^[L:Q]),       x>2.

Here c1 is effectively computable and absolute. Corollary 1.2 supplies primes of the specified Frobenius type once

    x >= c(delta) (log Delta_L)^(1/delta)
                         (log log Delta_L)^(2/delta).

The exact source convention for small discriminants should be retained; a comparison of exponents is not a new universal numerical cutoff.

### Substitutions relevant to our program

| Boundary for the required field | delta | power of log Delta | power of log log Delta | Status of input |
|---|---:|---:|---:|---|
|31/32|1/32|32|64|CT v2 stated theorem|
|23/24|1/24|24|48|proposed #957|
|25/27|2/27|27/2|27|proposed #958|
|11/12|1/12|12|24|proposed #959|

This table is a direct conditional substitution into a theorem parameter. A verified #959 would therefore improve BOTH logarithmic exponents, not replace a discriminant power by 12. The Chebotarev x exponent changes from 31/32 to 11/12. Field-uniform constants do not follow from #959's detector estimates themselves; the explicit constants here come from FSW's separately stated theorem after its precise hypothesis is supplied.

FSW Corollary 1.4 assumes QRH for the **normal closure** of a degree-d extension L/K. Its class-group torsion discriminant exponent is

    1/2 - 1/[2 ell (d-1)] + epsilon.

It does not improve merely by increasing delta. Likewise their generator-height exponent 1/(2n) does not change. Normal-closure versus original-field hypotheses must not be interchanged in field-specific applications. The all-number-field form of a verified #959 would supply either, but a theorem only about zeta_Q would not.

Corollary 1.3's short-interval threshold has log-discriminant powers 2/delta and 6/delta. Theorem 1.5 concerns moments over field families with additional family-density parameters. These are not used as premises in the new proofs here.

## B. Bhargava--Vemulapalli (BV), arXiv:2610.20600v1

*The existence of small defining polynomials for number fields*, Manjul Bhargava and Sameera Vemulapalli, submitted 14 October 2026.

Their stated theorem produces an integral degree-n defining polynomial of coefficient height O_n(sqrt(D_K)). The polynomial need not be monic; its generating root is not thereby an algebraic integer. Their argument uses geometry of ideal lattices and, in a remaining CM regime, subconvexity rather than a quasi-RH premise.

The precise interface useful here is Proposition 9: for any totally complex K of degree 2m, the class/archimedean-scaling probability average of completed Epstein zeta functions is

    A_K(s) = [w_K/(m h_K R_K)]
               D_K^(s/2) ((2pi)^(-s) Gamma(s))^m zeta_K(s).

At s=1/2 this is a direct zeta period, not a reciprocal period. The average is over all ideal classes and the compact unit-scaling quotient. Deleting the class average or replacing full norms by Euclidean lengths breaks the identity.

`GEOMETRIC_ROUTE.md` proves two consequences of this interface: a positive-measure version of the source's short-vector exclusion argument, and a two-Mobius-convolution reciprocal detector with an explicit kernel. Neither is an estimate for the original CT pairing. BV's discriminant-aspect subconvex saving in its special CM reduction cannot simply be substituted as a Z-aspect saving over one fixed field.

## Import boundary

FSW's arXiv record uses the perpetual non-exclusive license; BV's HTML identifies CC BY 4.0. This packet distributes original annotations and deductions with attribution, not the source PDFs or their complete TeX. The analytic results are imported as stated, not newly formalized or independently proved end-to-end. No priority claim is made for classical Chebotarev substitution, Markov-type arguments, Hecke periods or Mobius inversion.
