# LFAM2/6 exact function-field pilot report

Status: **exact finite result and normalization audit**.

Scope: the identities below hold coefficientwise in formal power series for the
declared quadratic character. The computed theorem is exhaustive only for monic
squarefree cubics in `F_5[T]` and reciprocal degrees `0 <= n <= 3`.

Exact sources or dependencies: unique factorization in `F_q[T]`, finite-field
Euler criterion, and direct enumeration. The interpretation was checked against
the integrated minimal-wavelet and Vaughan/half-divisor packets. No zero database,
floating-point calculation, or external algebra system is used.

## 1. Character and reciprocal identity

Let `q` be an odd prime, let `D` be monic, squarefree, and of positive odd
degree, and for monic `f` define

\[
  \chi_D(f)=\left(\frac{D}{f}\right)
  =\prod_{P^e\parallel f}\left(\frac{D}{P}\right)^e.
\]

The symbol at an irreducible monic `P` is evaluated exactly by

\[
 D^{(q^{\deg P}-1)/2}\equiv
 \left(\frac{D}{P}\right)\pmod P,
 \qquad \left(\frac{D}{P}\right)\in\{0,1,-1\}.
\]

Put

\[
 L_D(u)=\sum_{f\ {\mathrm{monic}}}\chi_D(f)u^{\deg f},\qquad
 B_D(n)=\sum_{\substack{f\ {\mathrm{monic}}\\\deg f=n}}
              \mu(f)\chi_D(f).
\]

Unique factorization gives the exact formal identities

\[
 L_D(u)=\prod_P(1-\chi_D(P)u^{\deg P})^{-1},
 \qquad
 \frac1{L_D(u)}=\prod_P(1-\chi_D(P)u^{\deg P})
               =\sum_{n\ge0}B_D(n)u^n.                 \tag{1}
\]

Thus, if `L_D(u)=sum_{k=0}^d A_D(k)u^k` with `A_D(0)=1`, then

\[
 B_D(0)=1,\qquad
 B_D(n)=-\sum_{k=1}^{\min(d,n)}A_D(k)B_D(n-k).          \tag{2}
\]

The checker computes the left side of (1) by the Moebius sum and the right side
of (2) independently, then checks their convolution is `(1,0,...,0)`.

For the frozen choice `q=5`, polynomial quadratic reciprocity has no sign:
`(D/f)=(f/D)` for monic coprime polynomials. Consequently the character is
periodic modulo `D`. Summing over residue classes proves directly that the
coefficients of `L_D` vanish from degree `deg D` onward. This is why `q=5` was
chosen instead of silently absorbing an infinite-place convention at
`q = 3 (mod 4)`.

## 2. Exact critical normalization

If

\[
 L_D(u)=\prod_{j=1}^{d}(1-\alpha_{D,j}u),
\]

then (1) and the generating function for complete homogeneous symmetric
polynomials give

\[
 B_D(n)=h_n(\alpha_{D,1},\ldots,\alpha_{D,d}).          \tag{3}
\]

When the Frobenius roots have modulus `sqrt(q)`, write

\[
 H_D(n):=q^{-n/2}B_D(n)
        =h_n(\alpha_{D,1}/\sqrt q,\ldots,
              \alpha_{D,d}/\sqrt q).                   \tag{4}
\]

No square roots are rounded. The producer stores (4) as an exact element
`a+b*sqrt(q)` of `Q(sqrt(q))`:

\[
 H_D(2r)=B_D(2r)/q^r,
 \qquad
 H_D(2r+1)=\frac{B_D(2r+1)}{q^{r+1}}\sqrt q.            \tag{5}
\]

Degree is the native logarithmic scale. No ratio-eight kernel or factor `67` is
ported: those are properties of a particular dyadic integer filter, not of (1).

## 3. Frozen exhaustive theorem

**Finite theorem.** Among all 100 monic squarefree cubic `D` in `F_5[T]`:

1. direct Moebius-character sums and the formal inverse (2) agree for every
   member through degree three;
2. every computed `L` polynomial is `1+A_D(1)u+5u^2` with
   `A_D(1)^2 <= 16 < 20`;
3. hence its two inverse roots are complex conjugates with product `5` and each
   has modulus `sqrt(5)`;
4. the toy signed cross-degree statistic

   \[
     C_D:=H_D(1)H_D(2)
         =\frac{B_D(1)B_D(2)}{5^{3/2}}
         =\frac{B_D(1)B_D(2)}{25}\sqrt5              \tag{6}
   \]

   is negative for 40 members, zero for 20, and positive for 40;
5. the exact family average of the integer numerator `B_D(1)B_D(2)` is zero.

The root-modulus assertion in item 3 is an elementary certificate here: the
quadratic `x^2+A_D(1)x+5` has negative discriminant and constant term `5`.
It does not import a general geometric-RH theorem.

The exact `A_D(1)` histogram is

```text
-4:5, -3:10, -2:15, -1:10, 0:20, 1:10, 2:15, 3:10, 4:5.
```

## 4. Explicit members and the family/member firewall

The following three members all pass the same reciprocal and root-modulus
checks:

| conductor `D` | `L_D` coefficients | `(B_0,B_1,B_2,B_3)` | `C_D` |
|---|---:|---:|---:|
| `T^3+2*T^2+4*T` | `(1,-2,5)` | `(1,2,-1,-12)` | `-2*sqrt(5)/25` |
| `T^3+1` | `(1,0,5)` | `(1,0,-5,0)` | `0` |
| `T^3+2*T` | `(1,-4,5)` | `(1,4,11,24)` | `44*sqrt(5)/25` |

This is an explicit false universalization: purity of all reciprocal roots does
not determine even this elementary lag-one coefficient sign. It also exhibits
the individualization gap cleanly: exact cancellation in a family average says
nothing memberwise.

The conclusion is deliberately narrow. `C_D` is not the canonical same-kernel
cross-core dispersion `OPEN.ARITH.XD`, the oriented near-collision statistic
`OPEN.ARITH.HCNC`, or a physical-occupancy theorem. Therefore the mixed signs do
not refute those predicates. A genuine port must first derive its degree kernel
from the same reciprocal-`L` source and preserve carrier recombination.

## 5. Reproduction and artifact contract

What was actually run:

```text
python research/l-families/atlas/function_field/pilot.py \
  --check research/l-families/atlas/function_field/fixtures.json
python tests/test_function_field.py
```

The reciprocal pass covers exactly `100*(1+5+25+125)=15,600` monic terms; the
independent `L` pass adds `100*(1+5+25)=3,100`, for 18,700 character terms in
all, with cached exact factorization. Every operation is integer modular
arithmetic or rational arithmetic. The producer caps any single monic
enumeration at 100,000 objects.

The canonical compact payload, before adding its own digest field, has SHA-256

```text
75f6145aafc014c64da34d68ec9741b4f0529397d73541a96b6776fd9dc195bd
```

The LF-normalized `pilot.py` source has SHA-256
`c9b4873daa50e96859c2c079dc031ebcdb5193bd495656e7049bfc6836a93258`.
This replay used CPython 3.12.10 and only the standard library.

The fixture is derived data, not an externally authenticated primitive. The
checker regenerates every conductor and every displayed statistic rather than
merely checking internal JSON consistency.

## 6. Smallest next theorem

The next useful step is not a larger scan. Fix one source-derived degree kernel
for a true function-field analogue of XD or HCNC, express it in Frobenius
eigenangles using (3)-(4), and decide separately:

- whether the sign/bound is memberwise;
- whether only its family trace is controlled;
- which monodromy or exponential-sum input performs the individualization.

That theorem would turn this normalization pilot into a mechanism result. The
number-field handoff would then be the corresponding explicit trace or
exponential-sum estimate, not an inference from known function-field RH.
