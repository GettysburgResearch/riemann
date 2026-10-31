# A complete complex-disk certificate for actual higher-order Bessel sums

Status: proposed finite source theorem with a complete analytic consumer and an outward-rational checker. This establishes the local boundary mechanism for actual higher-order coefficients after the earlier global positive-realization test failed. It does not prove the required unbounded sequence or RH.

The source is the literal theta-sampled Bessel transform of PR #1026, frozen at `11b4f6612275955a1fddb5c53f67dc21124783f8`. The exact source, radial derivative normalization, polynomial reduction, and decaying Weyl-function identity are preserved. No coefficient fitting, truncated theta tail, or floating special function enters the acceptance predicate.

## 1. The finite result

For either `(a,M)=(10,50)` or `(a,M)=(20,100)`, put

\[
c_n=I_n(a)\Phi\left(\tfrac12\operatorname{arsinh}(n/a)\right),
\quad
F_{a,M}(z)=c_0K_{iz/2}(a)+\sum_{n=1}^M c_n
\left[K_{n+iz/2}(a)+K_{n-iz/2}(a)\right].
\]

**Theorem.** Every zero of this complete finite Bessel sum in

\[
|z|\le\sqrt{2000}=20\sqrt5
\]

is real. Its polynomial boundary denominator has respectively six or eight zeros in the corresponding energy disk `|E|<=500`. In each case every denominator zero in the disk is simple, positive and real, none is canceled by the numerator, and every impedance residue there is strictly positive.

| Actual source | Complete pole count | Graeffe rounds | Boundary polynomial degree | Bernstein cells / maximum depth |
|---|---:|---:|---:|---:|
| `a=10, M=50` | 6 | 3 | 24 | 1 / 0 |
| `a=20, M=100` | 8 | 5 | 49 | 5 / 4 |

The exact certificates are `LOCAL_CERTIFICATE_10_50_500.json` and `LOCAL_CERTIFICATE_20_100_500.json`. The preceding pass's ordinary 180/360-digit Jacobi-fraction diagnostic found a failure of the **global** positive-impedance test for the first pair. That observation is not a premise of the present theorem. Both present local results are established independently by complete rational coverage.

This is an all-zero statement within a specified disk for a specific actual-source approximant. It is not a census of the zeros of zeta, a new verified height for zeta, or global real-rootedness of the approximant.

## 2. A sufficient disk criterion

Let `a>0`, `R>0`, and let A and B be the real boundary polynomials for a finite Bessel sum:

\[
\mathcal F(E)=A(E)y_E(0)+B(E)y_E'(0),\qquad
y_E(u)=K_{i\sqrt E}(ae^u),\qquad r(E)=-A(E)/B(E).
\]

The derivative is radial: `y_E'(0)=a K'_(i sqrt E)(a)`. Suppose the following are proved:

1. B has exactly k zeros in `|E|<R`, with none on the boundary.
2. There are k disjoint positive real intervals inside `(0,R)`, each with a strict B sign change at its endpoints.
3. On each interval, A and B' are nonzero and `-A/B'>0` by a full interval enclosure.
4. On the upper semicircle `E=R exp(i theta)`, `0<theta<pi`, one has `Im r(E)<0`.

Then r has no nonreal pole in the disk. Conditions 1 and 2 exhaust all complex zeros, counting multiplicity: each interval already supplies at least one distinct real zero, so all of them must be simple and there can be no additional zero. Condition 3 excludes common numerator/denominator roots and gives positive residues at all poles.

The imaginary part of r is harmonic in the upper half-disk away from those real boundary poles. Remove a small upper half-disk around each pole. Near a positive-residue pole lambda,

\[
\Im r(x+iy)=-\gamma\frac{y}{|x+iy-\lambda|^2}+O(y),\qquad\gamma>0.
\]

It is negative on a sufficiently small puncture semicircle. On the remaining real boundary it vanishes, and on the outer semicircle it is negative by condition 4. The maximum principle, followed by shrinking the punctures, proves

\[
\Im r(E)<0\quad(\Im E>0,\ |E|<R).
\tag{1}
\]

Conjugation gives the corresponding lower-half-disk sign. The decaying Weyl function satisfies

\[
\frac{\Im m_a(E)}{\Im E}
=\frac{\int_0^\infty|y_E(u)|^2du}{|y_E(0)|^2}>0.
\]

Its denominator cannot vanish at nonreal E by self-adjointness of the ordinary Dirichlet problem. Thus `m_a(E)=r(E)` has no nonreal solution in the disk. At a B zero, the numerator is nonzero and E is already positive real. For the actual positive-coefficient kernels, the Fourier transform is strictly positive on the imaginary z axis, so negative real energy cannot be a zero either. This proves the asserted all-real zero conclusion, including the boundary by the strict semicircle sign and the same Weyl identity.

The interior pole and residue conditions are essential. A correct sign on the outer semicircle alone does not permit applying the harmonic maximum principle across interior poles.

## 3. Exact complex zero counting by Graeffe and Rouché

Scale energy to z=E/R and write `p(z)=B(Rz)`. For any polynomial

\[
p(z)=p_{\rm even}(z^2)+z p_{\rm odd}(z^2),
\]

the Graeffe polynomial

\[
G(p)(z)=p_{\rm even}(z)^2-zp_{\rm odd}(z)^2
\]

has the squared roots of p, with multiplicity. A harmless nonzero scalar may be removed after each step. Hence repeated Graeffe steps preserve the number of roots inside the unit circle.

If the resulting coefficients satisfy, for some index k,

\[
|p_k|>\sum_{j\ne k}|p_j|,
\tag{2}
\]

Rouché's theorem gives exactly k zeros inside and no zeros on the unit circle. The checker evaluates every transformed coefficient with outward rational intervals and uses a lower bound for the left side and upper bounds for every term on the right. It cannot infer a count from a floating root list.

For the order-50 source, three squaring rounds prove a count of six with strict margin; for the order-100 source, five rounds prove a count of eight. Strict point evaluations then bracket respectively six or eight real roots; the total complex count proves those brackets are complete and contain simple roots. Interval refinement is stopped once the full residue enclosure is strictly positive and the normalized bracket width is below `10^(-12)`. Refinement never treats an unresolved midpoint sign as positive or negative; the code either uses the interval mean-value theorem or rejects insufficient precision.

## 4. The entire semicircle is a polynomial sign problem

Use the same positive scaling for A(Rz) and B(Rz), and write their coefficients as a_j and b_j. On `z=exp(i theta)`,

\[
\frac{\Im\{A(Rz)\overline{B(Rz)}\}}{\sin\theta}
=H(\cos\theta),
\]

where

\[
H(x)=\sum_{d\ge1}
\left[\sum_k(a_{k+d}b_k-a_kb_{k+d})\right]U_{d-1}(x).
\tag{3}
\]

Here `U_j` is the Chebyshev polynomial of the second kind. Terms beyond either polynomial's degree are zero. Since

\[
\Im r(Rz)=-\frac{\sin\theta\,H(\cos\theta)}{|B(Rz)|^2},
\]

it suffices to prove `H(x)>0` for **every** `-1<=x<=1`.

The checker changes variable `x=2t-1` and converts the power coefficients to the Bernstein basis on `[0,1]`. Every Bernstein basis function is nonnegative and their sum is one. Strictly positive lower endpoints for all Bernstein coefficients therefore prove a uniform positive lower bound. If necessary, exact de Casteljau subdivision supplies the same proof on a finite partition. For the order-50 source the initial degree-24 Bernstein coefficients already have strictly positive lower endpoints; no subdivision is needed. The order-100 source uses five accepted subintervals, with maximum subdivision depth four, for its degree-49 polynomial. The rational lower bounds are recorded in the certificates.

This proves the entire curved-boundary sign. It does not use an angular sample grid.

## 5. Reconstruction of the infinite primitive source

The checker reuses the reviewed rational interval class from the previous theta certificate, whose file digest is recorded in the output. It loads that file in an isolated namespace and configures its outward grid to `10^(-130)`. It reconstructs pi using 130 Machin-series terms. The unchanged exponential routine includes its explicit rational Taylor remainder and scaling-and-squaring enclosure; its exact tail remains part of every interval even when it is larger than the grid spacing.

For each `0<=n<=M`, the source sample is evaluated using only positive real arguments:

\[
x=n/a,\qquad Y=x+\sqrt{1+x^2},\qquad
w(x)=\sum_{k\ge1}(4\pi^2k^4Y^2-6\pi k^2Y)Y^{1/4}e^{-\pi k^2Y}.
\]

Integer square/fourth roots give outward root enclosures. Terms k=1 through 7 are evaluated. For k>=8, the terms are positive and bounded above by

\[
40 k^4Y^{9/4}e^{-3k^2Y}.
\]

Their successive upper-bound ratio is at most `(9/8)^4 exp(-51)<1/2`. Thus the **complete** omitted tail is bounded above by

\[
80\,8^4Y^{9/4}e^{-192Y}.
\]

The positive Bessel I series is evaluated through index 180 with its full decreasing-ratio geometric remainder. Every sample weight is enclosed and proved positive. A common c0 is divided out, which changes neither r nor the zero set. The exact order recurrences from the prior packet then reconstruct all coefficients of A and B. No float is used in any sign decision, root count, residue test, or boundary bound.

## 6. Two exact rejection controls

`verify_local_gate_controls.py` checks two distinct ways a boundary-only argument can fail.

- `r(z)=-z^3/(z^2+1/4)` passes the entire upper-unit-semicircle sign: its polynomial H is `x^2+3/4>0`. It nevertheless has two nonreal interior poles. The complete-count/real-coverage step rejects it.
- `r(z)=-z-(1/100)/(z-1/3)` has a strictly negative imaginary part on the outer semicircle and one real interior pole, but that pole has negative residue. The residue step rejects it.

These are mathematical countermodels to two omitted hypotheses, not perturbations of a saved success flag. Their receipt is `LOCAL_GATE_CONTROLS.json`.

## 7. Reproduction and remaining scale

```sh
python -I -S -B certify_bessel_window.py --a 10 --order 50 --radius 500
python -I -S -B certify_bessel_window.py --a 20 --order 100 --radius 500
python -I -S -B verify_local_gate_controls.py
```

The standard library is sufficient. The source dependency is preserved in the preceding packet on the parent branch. `-O` may be added; acceptance uses explicit checks and exceptions, not removable assertions.

The certificate establishes that the weaker local boundary strategy is attainable for actual higher-order coefficients. The cofinal companion theorem in the Bessel lane explains the exponentially small residues and isolates their limiting source ratio. Neither result supplies uniform local positivity on disks whose radii tend to infinity. That remains an infinite mathematical obligation.
