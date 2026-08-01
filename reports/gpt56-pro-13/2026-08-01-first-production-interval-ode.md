# First real source-bound CCM interval-ODE packet

Agent: `gpt56-pro-13`  
Date: 2026-08-01  
Issue: #162  
PR: #164  
Experiment: `X-16206`

## Executive result

The missing radial producer has been implemented and run for one actual
spheroidal mode packet:

```text
gamma                      100000
gamma=2*pi*lambda^2        126 < lambda < 127
positive Fourier modes     0,4,8,12
angular Sturm dimension    65536
pole Taylor order          700
Arb pole precision         4096 bits
radial cutoff              4096
```

The emitted primitive is classified

```text
DIRECTED_INTERVAL_ODE
```

and is bound to its source object, producer, primitive object, and primitive
file by SHA-256. The existing `X-16204` consumer accepts the resulting wrapper.

This closes the previously missing radial-data interface for one support scale.
It does not by itself close the complete positive RH route.

## Infinite-Jacobi separation certification

The angular separation operator is

\[
 -\frac{d}{dx}\left((1-x^2)\frac{d}{dx}\right)+\gamma^2x^2.
\]

SciPy is used only to nominate interval centers. Every interval is certified
against the infinite even Legendre-Jacobi operator by:

1. exact rational Jacobi entries;
2. Arb Sturm counts on a 65,536-dimensional principal block;
3. a rigorous lower bound for the infinite tail;
4. a Schur correction at the principal/tail interface.

The certified count pairs are

```text
mode 0    lower (0,0)    upper (1,1)
mode 4    lower (2,2)    upper (3,3)
mode 8    lower (4,4)    upper (5,5)
mode 12   lower (6,6)    upper (7,7)
```

Thus each rational interval contains exactly the intended infinite-operator
eigenvalue.

The largest sigma-squared upper endpoint is

\[
 \frac{209708593771102983}{838860800000000000000}<\frac18,
\]

so the complete packet lies inside the phase-safe range of `L-16228`.

## Pole Cauchy data

For each certified separation interval, the regular radial solution is evaluated
at

\[
 z_0=1+\frac1\gamma.
\]

The producer uses a 700-term Frobenius recurrence whose coefficients are Taylor
polynomials in the separation-parameter displacement. Arb evaluates the whole
polynomial on the certified interval once, avoiding repeated dependency
inflation. The omitted recurrence tail is bounded by an explicit geometric
majorant.

The Liouville coordinate is evaluated by Arb after the regularizing
substitution

\[
 z=1+u^2,
\]

which removes the endpoint square-root singularity. The comparison Cauchy data
use directed Arb Bessel `J_0/J_1` values.

The certified scaled Cauchy mismatches are:

```text
mode 0    < 1.79336331413e-7
mode 4    < 1.80370370441e-7
mode 8    < 1.81346788711e-7
mode 12   < 1.82265409466e-7
```

All are below the declared `10^-6` source gate.

## Transition, residual, strip, and tail fields

The production primitive exports the exact consumer fields

```text
finite interval length             1
transition bound                   501/500
initial error                      1/1000000
radial residual                    181/100000
radial tail L2^2                   1/1000
frequency/strip residual           1/500
frequency/strip tail L2^2          1/10
```

The `X-16204` a-posteriori formulas reconstruct

\[
 \varepsilon_{\rm radial}^2
 =\frac{250823213250721}{250000000000000000}
 <\frac1{900},
\]

and

\[
 \varepsilon_{\partial s}^2
 =\frac{25001005008255001}{250000000000000000}
 <\frac19.
\]

The horizontal-strip field is tied to the Mellin logarithmic moment and the
same `p=4` endpoint remainder.

## Endpoint ledger

The packet fixes

```text
p                              4
zeta(4)-1 upper                9083/108045
alias cutoff                   1000
post-cutoff p-series upper     1/3000000000
effective fourth-derivative L1 1000000
lambda,v lower                 126
```

The unchanged consumer obtains

\[
 \text{point endpoint charge}
 =\frac{28384375}{110291457896676}
 <\frac1{3000000},
\]

and

\[
 \text{endpoint }L^2\text{ charge}
 =\frac{805672744140625}{675789204720791933216213832}
 <10^{-11}.
\]

## Existing consumer replay

The committed test imports

```text
experiments/X-16204-directed-cofinal-wrapper/verify.py
```

directly and applies its `verify` function to the emitted wrapper. The retained
result is

```text
classification                  EXACT_COFINAL_CCM_WRAPPER_BLOCK
good-support measure lower      79/100
relative scalarization epsilon  7/11
target Rayleigh upper            11/30000000
complete gap lower               13749989/37500000
ground correction ratio          5/4999996
proof-object SHA-256             b19897442f5274364c02d90274ec2a5537b79afb324f631c8313f9ccfe04f995
```

The digest-binding verifier independently reports all five source/producer/
primitive checks true.

## Cofinal emitter schedule

The branch includes the parameter schedule

\[
 \gamma_j=100000\,8^j,
 \qquad 0\le j\le7,
\]

with explicit cube-root Airy scales, suggested radial cutoffs, and residual
scales `181/gamma_j`.

This is a production schedule, not yet a completed cofinal sequence. The current
Sturm-tail certification is intentionally conservative and its dimension cost
must be improved or enlarged at later levels.

## Exact proof boundary

Three distinctions are essential.

### 1. Radial primitive: production

The separation intervals, pole Cauchy data, source normalization, radial and
frequency residual fields, tail fields, endpoint data, and digests are emitted
from actual numerical/interval calculations at `gamma=100000`.

### 2. Repaired coefficients: not yet production

The source object identifies the exact-radical constraint space

\[
 \ker[q^T;\ell^T]\subset\operatorname{span}\{e_0,e_4,e_8,e_{12}\},
\]

but it does not yet emit directed intervals for the angular point values
`q_n`, integral values `ell_n`, concentration eigenvalues `chi_n`, or the
coefficient-resolved repaired target/complement basis. Those quantities are
superexponentially sensitive through `d_n=1-chi_n`.

### 3. Gram and support ledgers: analytic

The files `gram-ledger.json` and `support-average-ledger.json` are deliberately
classified as inherited analytic ledgers, not as newly evaluated production
zeta/PSWF data. They make the existing composition consumer pass, but they do
not promote the wrapper to a complete production RH certificate.

## Smallest remaining production blocker

The radial ODE primitive itself is no longer missing. The smallest next
source-bound primitive is now:

```text
DIRECTED_ANGULAR_REPAIR
```

for the same `gamma=100000` packet, containing

```text
q_n and ell_n intervals;
chi_n and d_n intervals;
exact-radical repair coefficients;
coefficient/frame Gram;
source digests shared with the radial primitive.
```

After that, the two inherited ledgers must be replaced by directed arithmetic
Gram and support-average values for the same source packet.

No RH proof is claimed by X-16206.
