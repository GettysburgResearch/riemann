# Fixed-lambda Xi held-out alignment and finite normalized Gram

Status: PREREGISTERED BOUNDED SCOPE; no new held-out computation yet.
Authoring base: 0e3fc9b482f0f115a49a6209ccbfeffae640014a (FC).
All frozen parent science and review records remain unchanged.

## Exact source and held-out coverage

The primitive is the actual unrescaled f(z)=xi_R(1/2+i z), with the ONE
exact constant lambda64=[Re psi(1/4+32i)/2-log(pi)/2]^-1.
It is not refrozen at the new heights. Define R_k=f^(k)-i lambda64 f^(k+1),
C_k=f^(k)+i lambda64 f^(k+1), and raw Theta0=R0/C0 as in FC.

The three new open boxes, in this order, are exactly

    (250,262)+i(0,1), (506,518)+i(0,1), (1018,1030)+i(0,1).

These endpoints and the old fourteen FC nodes are fixed before computing
any new count, root or alignment value. There is no predicted root count,
alignment threshold, growth trend or Gram constant. No box or strip may
be silently moved or discarded. Every failed certification tier must be
retained with its literal obstruction; an unresolved boundary remains an
unresolved boundary, not a complete census.

## Declared arithmetic and search schedule

The existing pinned FLINT runtime will be used. New, explicitly labeled
primitive wrappers extend the old x<150 domain only to 20<Re z<1100,
with -1<Im z<2 for boundary rectangles. Parent wrappers are not edited.
Only 256, 512 and 1024-bit working precision are permitted.

Boundary certification tiers, attempted in order until one succeeds:

| Tier | Bits | Segment length | Taylor terms |
|---|---:|---:|---:|
| 1 | 256 | 1/16 | 32 |
| 2 | 512 | 1/32 | 40 |
| 3 | 1024 | 1/64 | 48 |

All tiers use the SAME full closed box boundary, the BC analytic Cauchy
tail proof with rho=1/8 and outer radius1/4, and exact rational polygon
winding. This is declared mesh/precision refinement, not endpoint tuning.
The series cap is at most 55, matrix order at most 64, JSON at most
24000000 bytes/600000 nodes/depth24, rational components at most4096 bits.

Uncertified root-location scouting uses the fixed real mesh j/4 across
each box and imaginary seeds 1/8,3/8,5/8,7/8, at 256 bits with at most
24 Newton steps per seed. Seed outcomes (converged candidate, duplicate,
domain exit, derivative obstruction or iteration limit) are retained.
Scouts are not proof. Candidate centers are rounded to denominator2^180;
the root discs have radius2^-120. Root certification tries256/512/1024
bits in that order, using the FC Rouche and full-rectangle noncommon guards.
The complete boundary count must match the distinct certified root discs
before any box is called exhaustive. Extra candidates or missed counts
must remain visible; no extra seed survey is preregistered.

## Finite targets and quantifier firewall

Rebuild the old fourteen FC root certificates and raw values. For them
and every new certified surviving node b=x+i y, compute the complete
normalized Hardy Gram G_ij=2sqrt(y_i y_j)/(y_i+y_j+i(x_j-x_i)), including
all old/new cross entries. Report outward row-sum Bessel upper bounds for
the old span and each nested added-box prefix. These are finite constants,
not a uniform infinite-family bound; absolute row sums can grow even if
an infinite family is Bessel.

Compute exact ball-enclosed partial sums and each new-box increment of

    sum |raw Theta0(b)|^2 Im(b)/|Re(b)|.

This is the weighted alignment in the root's proposed Laplace low-pass
criterion. Every modulus uses the entire certified root rectangle. Do not
replace raw values by reduced ones, and do not call the weighted sum a
physical trace. The finite special-function evaluations are unconditional;
operator interpretations retain the component-innerness premise. No finite
prefix establishes uniform Bessel control, divergent weighted alignment,
cofinal physical capture, native outer-metric capture or RH.

A possible separate analytic interface is transport from real simple f6
zeros t with kappa^2=-f7(t)/f5(t)>0 to R5 zeros of approximate height
1/(lambda64*kappa^2), under explicit local Taylor remainder and raw-value
conditions. Such conditions are unpaid actual-Xi hypotheses; a one-wave
Riemann--Siegel approximation is not assumed. Any lemma developed must
state those hypotheses fully and must not convert finite tests into them.
