# Independent review of the long-shift HLC continuation

Reviewer: fractional/native agent, independently of the author.

Verdict: **passes in its stated conditional and component scope**.
The long-shift Type II estimate is proved from the displayed ordinary
Mertens premise. The exact Type I term preserves the target Mertens
signal. Neither the Type II saving nor the finite affine contraction is
being passed off as a bound for the complete prime correlation.

## Exact reviewed files

These are local byte authentications, not a claim of remote publication.

| File | Bytes | SHA256 | Git blob |
|---|---:|---|---|
| `AVERAGED_HLC.md` | 26420 | `fb04005fe40e7f809e0b548503351efed6d294d88e25fe0e1be44a1a335363fb` | `a8ebf7488836bab8300ba46a1fa053bfebcec037` |
| `check_averaged_hlc.py` | 5802 | `2f8cc80138abb8018b212ac7cda8765fc1028cbabb3ce057f2b2d39d74da63b0` | `1bd16d0d9338cead0a448a09cfa422d89c9754be` |

The mathematical and checker files were read in full. The checker was
run independently and returned PASS. The relevant parts of
[Ye, arXiv:2610.20242v1](https://arxiv.org/html/2610.20242v1)
were freshly read for the source comparison: equations (4.4)--(4.5),
the state and kernel definitions (4.11)--(4.17), the dirty-edge bound
(4.48), trace transfer (4.64)--(4.68), and list collision bound (4.73).
This is not an independent certification of that entire preprint.

## 1. Both Möbius signs and the powers of H

The two integrations by parts in the double sum are legitimate for the
stated compact smooth profiles. The two minus signs cancel. On the
support, the two Mertens prefixes are bounded by a constant times
`C_beta M^beta` and `C_beta X^beta`.

I independently differentiated the kernel. The four terms have total
L1 costs

\[
 O(H/X),\quad O(1),\quad O(1),\quad O(X/H).
\]

In particular the fourth term cannot be omitted. This verifies the
factor `1+X/H` before division by `H` and the two terms
`H^(-1)+XH^(-2)` afterwards. With `B_N<<N(log X)^C` and
`N=X/M`, the long-shift bound is
`X^beta M^(beta-1)(log X)^C`. For `H=X^theta` the dominant
displayed exponent is correctly
`beta+2-m(1-beta)-2theta`. The shortened-shift requirement in the
note follows from this expression; it does not inherit the long-shift
gain automatically.

The example `beta=7/8,m=1/5` gives `17/20` exactly.
This calculation is conditional on the summatory premise. A family
zero-free cap would be used with the explicitly acknowledged arbitrarily
small epsilon loss, not silently as the exact endpoint summatory bound.

## 2. Smooth Vaughan identity and the complete Type I expression

The convolution identity (8) is exact with the smooth cutoffs as defined.
It uses `log=Lambda*1` and `mu*1=delta_1`, and does not require
the smooth cutoff to be an idempotent indicator.

The support of `F_X` lies in `[X/2,2X]` for the stated positive
shift kernel and `c<=1/4`. Hence the `Lambda_1` term vanishes
under `2V<X/2`. Poisson summation in the final free factor has the
correct spacing factor `q^(J-1)`. The derivative estimate
`||F_X^(j)||_infinity<<X^(beta-j)` follows from one summation by
parts in the second Möbius variable because `H` is a fixed
positive multiple of `X`.

For the two Type I errors, the sums over the cutoff divisors cost
`U^J` and `(UV)^J log V`. After division by `H` these give
the claimed error in (10), with fixed profile constants.
The scale separation `UV<=X^(1-epsilon_0)` is retained before
the fixed derivative order is chosen.

The Type II coefficient `b_r=(Lambda_2*1)(r)` is nonnegative,
bounded by `log r`, and vanishes for `r<=V`. Summing its
dyadic estimates over the first factor is geometric because
`beta-1<0`. This proves (11) without a hidden smoothness
assumption on `b_r`.

The signs in (12) are correct:

\[
 (1/\zeta)(1)=0,\qquad (1/\zeta)'(1)=1,\qquad
 \sum_d\frac{\mu(d)\log d}{d}=-1.
\]

The smoothed tails have the claimed orders under the Mertens premise.
The variable substitution `t=v-Hy` in (13) is exact and keeps
`u-cy` positive. Therefore the Type I continuum term is exactly
(14), with leading coefficient tending to one. The conclusion (15)
is a centered correlation estimate. It does not bound the remaining
Mertens main term by a smaller power.

## 3. Mellin modes and finite affine averaging

The multiplier (16) follows by inserting
`dM_rho(v)=rho v^(rho-1)dv` into the already computed linear
operator. The factor `rho X^rho` cancels in the ratio. For a fixed
detectable mode and polynomially growing `U,V`, the displayed
multiplier tends to one.

The modulation `W_tau(u)=W_0(u)u^(-i tau)`, with nonzero
nonnegative `W_0` and `tau=Im rho`, makes the denominator a
positive real Mellin integral. It prevents an accidental profile zero
from concealing the mode. This is an operator test, not a claim that
the actual Mertens function has a one-zero asymptotic.

The complete affine identity (17) is exact. For distinct field
points, the affine group ranges through all ordered distinct pairs.
Separating the diagonal gives the two variance factors divided by
`p-1` and leaves the constant component exactly. The note correctly
retains that component and correctly distinguishes a complete finite
affine average from Ye's incomplete integer determinant average.

## 4. Uniform characters, principal poles and common moduli

Section 6 explicitly introduces the additional all-family Dirichlet
zero-free premise. It does not infer character-uniform estimates from
ordinary Mertens control alone.

One analytic precision issue was raised and resolved during this
review. In the principal case, merely multiplying by `s-1` would
make the Euler-disk logarithm grow like `log|t|` at large height.
The final file instead takes the logarithm of

\[
             \frac{s-1}{s+1}L(s,\chi_0).
\]

This cancels the pole, is nonzero in the working right half-plane,
and has a bounded logarithm on the Euler disk. The auxiliary pole
at -1 is outside the domain. Thus the Borel--Caratheodory /
three-circles proof has the required bounded inner disk. Its principal
residue is restored in the prime contour.

The natural imprimitive factors have no zeros in positive real part
and uniformly bounded Euler logarithms on `Re s>=2`. Their
polynomial conductor growth is sufficient for the same argument.
The stated subpower conductor loss and finite profile orders are
consistent with a fixed buffer to the right of the imported ceiling.

Character orthogonality gives the per-modulus bound in (19), and the
sum over moduli costs `Q^(1+epsilon)`. The resulting
`X^(1-beta)` scale is correctly stated as the available modulus
budget. It is not promoted to a square-root level or to a bound for
all divisors generated by the marked expansion.

## 5. The Ye scale audit and its precise limitations

The source does discard the selected-quotient Möbius sign in the
Cauchy step (4.4), before the determinant form (4.5).
Its state lists consist of distinct primes dividing the first
coordinate, and each transition replaces one entry per band.
Consequently at most `2R` initial entries per band can depart
along a path of `2R` edges.

For the inert product `I`, dividing every first coordinate and
every actual shared product by `I` preserves the normalized
determinant exactly. The stated gcd condition after division is
also correct. Two precision points were resolved with the author:

1. The reduced damping count must exclude primes in `I` from its
   prime universe. Merely evaluating the original distinct-prime
   count at `u/I` would be wrong when an inert prime still
   divides that quotient. The final file explicitly defines
   `omega_rem` and obtains exact cancellation with the reduced
   list sizes.
2. The condition `nu<eta/2` is the uniform lower-endpoint budget
   obtained by using `p_min>=X^eta`. It is not asserted as a
   necessary inequality for every possible subfamily inside the
   larger interval. The final wording makes this distinction.

The central obstruction is sourced correctly: the good-state tests
(4.14)--(4.15) quantify over every hypothetical omitted list entry.
A prime inert on the realized path can be omitted in those tests.
Thus the unprojected coordinate identity does not remove the inert
product from the actual projected operator.

The remaining factor in the trace-to-pairing step is also present in
the source: `(d_0Y)^(1/(2R))`. The proposed active-list bound gives
the stated cost `X^(2eta K+eta K/R)`. The dirty-edge Schur gain
has only the `J^(-K/2)` scale, before logarithmic factors.
These **available upper bounds** do not produce a net power gain.
The note correctly avoids treating their failure as a lower bound on
the true norm or an impossibility theorem.

## 6. Broad selector coverage and coherent recombination

The Ramaré-type identity (21) is exact for all integers. On a
squarefree integer, its selected-prime terms add with denominator
equal to the number of eligible primes. For a nonsquarefree integer,
either coprimality fails or the remaining Möbius factor is zero.

The Rankin proof of (22) gives the displayed exponent for every
fixed `A>0`. A fixed positive sigma slightly above
`max(0,1-1/A)` makes the logarithm of the small-prime Euler
product `o(log X)`. The shift average in (23) costs only
`O(H)`, and the von Mangoldt logarithm is absorbed in epsilon.
Thus the coverage error at `A=4` is a genuine
`X^(3/4+epsilon)` bound.

The intermediate fractional coefficients do have a branch at one:
the local Euler correction in (25) is absolutely convergent and
nonzero on compact subsets of `Re s>1/2`, while
`zeta(s)^(-rho)` retains the nonintegral zero-order branch for
`0<rho<1`. A uniform below-one power estimate omitting its
principal contribution is therefore not supplied by a zero-free cap.

The derivative identity (26) has the correct sign and denominator.
The factor `(1-rho p^(-s))^(-1)` retains the coprimality restriction;
it is not replaced by an independent prime factor.
The final Type II estimate recombines this entire finite prime-factor
expression before taking absolute values. Its prefix is
`M(v)` minus the smooth-number Möbius prefix. Applying the double
summation-by-parts proof with that prefix proves (27). This
recombination eliminates the spurious intermediate branch issue but
does not eliminate the already identified Type I unit multiplier.

## 7. Checker scope and outcome

The independent replay passed:

* two nonzero exact double-summation identities, with a wrong-sign
  negative control;
* 912 smooth-cutoff Vaughan coefficient identities, using formal
  prime logarithms;
* four complete affine-group second moments, with a missing-mean
  negative control;
* 6000 exact broad-selector identities.

All checks use rational arithmetic. The finite piecewise-polynomial
cutoffs test convolution identities; they do not certify the analytic
smooth seminorm estimates, summatory premises, or any zero-free
conclusion. The checker uses explicit exceptions, so its checks are
not disabled by Python optimization.

No remaining mathematical blocker was found in the reviewed claims
at the scopes stated above. The distinction between the proved Type II
gain and the surviving Type I target is mathematically necessary and
is preserved throughout the final file.
