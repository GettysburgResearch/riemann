# Odd-notch first boundary: exact trace-zero extinction

Status: **exact all-odd-prime-power theorem**.  The previously observed
trace-zero first-boundary members occur only at the exceptional family degree
`n=3`; the entire first boundary is nonzero for every `n>=4`.

These are statements about the raw quadratic-family correlation sum
`S_(n,Q)`, not zeros of an individual L-function.

## Start here

Fix an odd prime power `q`, put

\[
 M=2n-1,\qquad h=\left\lfloor{n\over2}\right\rfloor,
\]

and let `Q` be monic squarefree of degree `M`.  The support-forced zero
stratum from PR #756 is

\[
 \min_{P\mid Q}\deg P>h
 \quad\Longrightarrow\quad S_{n,Q}=0.
 \tag{0.1}
\]

The first boundary outside it is

\[
 \min_{P\mid Q}\deg P=h.
 \tag{0.2}
\]

If `m_h` is the number of degree-`h` irreducible factors of `Q`, the exact
notch formula gives the complete first-boundary residual

\[
 \boxed{S_{n,Q}=m_hD_{n-2h}.}
 \tag{0.3}
\]

Therefore:

1. If `n=2h` is even, then
   \[
   \boxed{S_{n,Q}=m_h>0.}
   \tag{0.4}
   \]
2. If `n=2h+1` is odd, then
   \[
   S_{n,Q}=m_hD_1.
   \tag{0.5}
   \]
   For `n>=5`, one has `h>=2`, so `Q` has no linear factor.  Hence
   \[
   D_1=\sum_{a\in\mathbf F_q}\left({T-a\over Q}\right)
   \tag{0.6}
   \]
   is a sum of exactly `q` values in `{+1,-1}`.  Since `q` is odd,
   \[
   \boxed{D_1\equiv q\equiv1\pmod2,\qquad D_1\ne0.}
   \tag{0.7}
   \]

Combining the two parities proves

\[
 \boxed{
 n\ge4,\ \min_{P\mid Q}\deg P=h
 \quad\Longrightarrow\quad S_{n,Q}\ne0.}
 \tag{0.8}
\]

Thus, among conductors satisfying `min deg(P)>=h`, the support criterion is a
converse as soon as `n>=4`:

\[
 \boxed{
 S_{n,Q}=0
 \quad\Longleftrightarrow\quad
 \min_{P\mid Q}\deg P>h.}
 \tag{0.9}

This equivalence is only for the union of the support stratum and its first
boundary.  It says nothing about deeper profiles with minimum factor degree
at most `h-1`.

## 1. Frozen source and exact reduction

The source is the closed-place notch packet at frozen PR #756 head
`6e4609dfe1b073f1eb58445fdd1d7164dbc450d6`:

| source | git blob | role |
|---|---|---|
| `QUADRATIC_FAMILY_CLOSED_PLACE_WEIGHT_NOTCH.md` | `a1b8476ddd3cad6f63ff205392426ae9c2d0829c` | all-profile residual formula |
| `quadratic_family_closed_place_weight_notch.json` | `964935a3a936f03011366546d966ef1473c4e832` | canonical exact fixture |

For odd conductor degree the locked formula is

\[
 S_{n,Q}=\sum_{k=1}^{\lfloor n/2\rfloor}a_kD_{n-2k},
 \tag{1.1}
\]

where

\[
 \sum_{k\ge0}a_kx^k=\prod_{P\mid Q}(1-x^{\deg P})^{-1}.
 \tag{1.2}
\]

On the first boundary, `a_k=0` for `1<=k<h` and `a_h=m_h`.
There are no indices beyond `h` in (1.1).  This proves (0.3) without an
asymptotic or computation.

For even `n=2h`, the remaining index is zero and `D_0=1`, proving (0.4).
For odd `n=2h+1`, the remaining index is one, proving (0.5).

## 2. Root-free parity proof for odd `n`

The coefficient `D_1=p_1` is the degree-one coefficient of
`L(u,psi_Q)`.  Directly from the Dirichlet series,

\[
 p_1=\sum_{\substack{F\text{ monic}\\\deg F=1}}\psi_Q(F)
 =\sum_{a\in\mathbf F_q}\psi_Q(T-a).
 \tag{2.1}
\]

If every irreducible factor of `Q` has degree at least two, then
`gcd(T-a,Q)=1` for every `a`.  The quadratic character values in (2.1) are
therefore all `+1` or `-1`, never zero.  Their number is `q`, which is odd.
This proves (0.7).

The proof neither chooses a model of the hyperelliptic curve nor depends on a
quadratic-reciprocity sign.  Under the curve convention of the source packet,
`D_1=0` is equivalent to trace zero, but the nonvanishing is already visible
in the primitive Dirichlet coefficient.

Odd characteristic is binding.  The parity argument is not stated for even
`q`, and the entire quadratic-character setup would require a different
Artin--Schreier model there.

## 3. Why `n=3` is exceptional

At `n=3`, one has `h=1`.  The first-boundary condition says that `Q` has at
least one linear factor.  Some terms in (2.1) are then zero, so an even number
of nonzero `+1/-1` values can sum to zero.

A bounded prime-field replay over every monic squarefree quintic gives:

| `q` | support-forced (`min deg>1`) | first-boundary trace zero | all raw zeros from these two strata | squarefree quintics |
|---:|---:|---:|---:|---:|
| 3 | 72 | 30 | 102 | 162 |
| 5 | 1024 | 406 | 1430 | 2500 |
| 7 | 5712 | 2184 | 7896 | 14406 |

The replay examines `3^5+5^5+7^5=20175` monic quintics, uses polynomial gcd
only for squarefreeness, and evaluates the `q` oriented quadratic symbols.
It is a regression control for the low-degree exception, not evidence for an
asymptotic.

Equation (0.8) proves that this exception does not recur at larger `n`.

## 4. Density consequence

Let `Z_(q,n)` be the support-forced count from
`QUADRATIC_FAMILY_CLOSED_PLACE_NOTCH_DENSITY.md`, and let
`B_(q,n)^(1)` count zero raw sums on the first boundary (0.2).  Then

\[
 \boxed{B_{q,n}^{(1)}=0\qquad(n\ge4).}
 \tag{4.1}
\]

Consequently the first boundary contributes no additional `c_q/M` term—or
indeed any term—to the raw-zero density.  The existing expansion

\[
 {Z_{q,n}\over q^M}
 ={4\omega(4)\over M}+{D_\varepsilon\over M^2}+O_q(M^{-3})
 \tag{4.2}

is the exact zero count through the first boundary for all `n>=4`.

This does **not** prove that (4.2) is the full raw-zero density.  The next
possible contribution comes from

\[
 \min_{P\mid Q}\deg P=h-1,
 \tag{4.3}

where, for odd `n=2h+1` and `h` beyond the tiny collision cases,

\[
 S_{n,Q}=m_{h-1}D_3+m_hD_1.
 \tag{4.4}

Here `D_3` is even and `D_1` is odd when the conductor has no linear factor,
so a necessary condition for a zero is

\[
 m_h\equiv0\pmod2.
 \tag{4.5}

Whether this second boundary has a positive `1/M` contribution is now the
first genuine density problem.  It requires the joint distribution of
`D_3,D_1` across constrained large-factor profiles, not merely the trace-zero
distribution of `D_1`.

## 5. Exact boundary

Proved:

- the complete first-boundary residual (0.3);
- positivity for every even `n`;
- parity-forced nonvanishing for every odd `n>=5`;
- the two-stratum equivalence (0.9) for every `n>=4`;
- zero asymptotic contribution from the entire first boundary;
- the necessary parity condition (4.5) on the next odd boundary when no
  low-degree factor interferes.

Not proved:

- classification or density of zeros with `min deg(P)<=h-1`;
- equidistribution or monodromy for `(D_3,D_1)`;
- a connected-cumulant zero;
- a zero of an individual L-function, RH, or GRH;
- external novelty or priority.

The main correction to the finite `n=3` intuition is exact: the apparent
trace-zero boundary family is killed by odd parity in every asymptotic row.

