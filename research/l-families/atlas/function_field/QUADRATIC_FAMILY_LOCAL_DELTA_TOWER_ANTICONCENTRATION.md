# Local delta-tower anti-concentration

Status: **exact local theorem for every fixed odd prime power and depth;
proves absolute summability of the displayed fixed-depth coefficients, but
does not sum the conductor layers**.

Exact replay:
[`quadratic_family_local_delta_tower_anticoncentration.py`](quadratic_family_local_delta_tower_anticoncentration.py).

## 0. Outcome

Fix an odd prime power `q`, an integer `j>=1`, and put

\[
 r=2j+1,\qquad N=I_q(r).
\]

Use the local probabilities of the fixed-depth packet:

\[
 \delta_{j,0,q}=\Pr(D_r=0),
\tag{0.1}
\]

and, for `1<=s<=j`,

\[
 \delta_{j,s,q}=\Pr(D_r+D_{r-2s}=0).
\tag{0.2}
\]

The `s=0` convention in (0.1) is important: the random variable is the
single `D_r`, not `2D_r` or two independent copies of `D_r`.

For every `0<=s<=j`,

\[
\boxed{
 \delta_{j,s,q}
 \le 2^{-N}{N\choose\lfloor N/2\rfloor}
 \le {1\over\sqrt N}
 \le \sqrt{{3r\over2}}\,q^{-r/2}.}
\tag{0.3}
\]

The terminal channel obeys the stronger exact identity

\[
 \boxed{\delta_{j,j,q}=0}
\tag{0.4}
\]

by parity.  Since `r=2j+1`, (0.3) gives, uniformly in `s`,

\[
 \boxed{\delta_{j,s,q}=O_q(\sqrt j\,q^{-j})}
\tag{0.5}
\]

and therefore

\[
 \boxed{
 \sum_{s=0}^{j}\delta_{j,s,q}
 =O_q(j^{3/2}q^{-j}).}
\tag{0.6}
\]

It follows that both the `M^-2` and `M^-3` coefficient towers in the
fixed-depth theorem are absolutely summable over `j`.

This last statement concerns the displayed coefficients only.  It does not
justify summing the underlying conductor-layer asymptotics: their
`O_(q,j)(M^-4)` remainders and their stable profile ranges are not uniform
when `j` grows with `M`.

## 1. Frozen inputs and claim boundary

The replay checks these historical blobs.

| input | commit | blob |
|---|---|---|
| closed-place Euler product | `9716d2261e9e7843a6c1ffffd67ee8d6756060aa` | `a1b8476ddd3cad6f63ff205392426ae9c2d0829c` |
| fixed-depth theorem | `d61323f8c269bdf114d958d6596d0d32bf793efb` | `1803cdf033710d2bbb53b83144cbf4b2ae324554` |
| fixed-depth replay | `d61323f8c269bdf114d958d6596d0d32bf793efb` | `935c3ddbef1550675384441daa679802d75636a6` |
| fixed-depth JSON | `d61323f8c269bdf114d958d6596d0d32bf793efb` | `68e17b580208e12756cc3ed9f102407e07765dfd` |

The result is a theorem inside the finite independent-sign model already
proved to govern each fixed-depth profile.  It makes no assertion about
uniform conductor-layer errors, an individual `L`-function zero, RH, GRH,
or external priority.

## 2. Isolating the independent top-degree sum

Attach an independent uniform sign `epsilon_P` to every irreducible `P` of
degree at most `r`, and write

\[
 P_\epsilon(u)
 =\prod_{\deg P\le r}(1-\epsilon_Pu^{\deg P})^{-1}
 =\sum_{m\ge0}p_m(\epsilon)u^m.
\tag{2.1}
\]

In the coefficient of `u^r`, choosing a degree-`r` irreducible uses the
whole degree budget.  It occurs to the first power and cannot be accompanied
by any other positive-degree factor.  Hence

\[
 p_r=S_r+F_r,\qquad
 S_r:=\sum_{\deg P=r}\epsilon_P,
\tag{2.2}
\]

where `F_r` depends only on signs of irreducibles of degree strictly below
`r`.  The same is true of `p_(r-2)` and of every `D_(r-2s)` with `s>=1`.
Since `D_r=p_r-qp_(r-2)`, there are lower-sign-measurable integers
`A_r,B_(r,s)` such that

\[
 D_r=S_r+A_r,
\tag{2.3}
\]

and, for `1<=s<=j`,

\[
 D_r+D_{r-2s}=S_r+B_{r,s}.
\tag{2.4}
\]

The coefficient of `S_r` is exactly one in both formulas.  Moreover, `S_r`
is independent of every sign entering `A_r` and `B_(r,s)`.

Condition on all signs of degrees below `r`.  Each zero event now asks the
same sum of `N=I_q(r)` independent Rademacher variables to hit one specified
integer.  Averaging the conditional bound proves

\[
 \delta_{j,s,q}\le\max_t\Pr(S_r=t)
\tag{2.5}
\]

for every `s`, with (2.3) used at `s=0` and (2.4) used at positive `s`.

At `s=j`, the fixed-depth parity theorem says that `D_r` is even and `D_1`
is odd.  Their sum cannot vanish, proving (0.4) independently of (2.5).

## 3. A fully explicit central-binomial bound

For a sum `S_N` of `N` independent signs,

\[
 \Pr(S_N=t)
 =2^{-N}{N\choose(N+t)/2}
\]

when the lower entry is integral, and the probability is zero otherwise.
Unimodality of the binomial coefficients gives

\[
 \max_t\Pr(S_N=t)
 =2^{-N}{N\choose\lfloor N/2\rfloor}.
\tag{3.1}
\]

For completeness, define

\[
 a_m=4^{-m}{2m\choose m}.
\]

We claim the elementary bound

\[
 a_m\le{1\over\sqrt{3m+1}}.
\tag{3.2}
\]

It is equality at `m=0`.  Since

\[
 {a_{m+1}\over a_m}={2m+1\over2m+2},
\]

the induction step follows from

\[
 \left({2m+1\over2m+2}\right)^2
 \le {3m+1\over3m+4},
\tag{3.3}
\]

whose cross-multiplied right side minus left side is exactly `m`.

If `N=2m`, (3.1)--(3.2) give

\[
 \max_t\Pr(S_N=t)=a_m
 \le(3m+1)^{-1/2}\le N^{-1/2}.
\]

If `N=2m+1`, the maximum is

\[
 {2m+1\over2m+2}a_m
 \le a_m\le(3m+1)^{-1/2}\le N^{-1/2}.
\]

This proves the middle inequality of (0.3) for every `N>=1`, including all
small cases.

## 4. Lower-bounding the number of top-degree signs

For odd `r>=3`, Möbius inversion gives

\[
 rI_q(r)=\sum_{e\mid r}\mu(e)q^{r/e}.
\]

Every proper divisor term has `e>=3`, hence exponent at most `r/3`.  Bounding
the number of such terms by `r` yields

\[
 rI_q(r)\ge q^r-rq^{r/3}.
\tag{4.1}
\]

For `q>=3` and odd `r>=3`,

\[
 3r\le q^{2r/3}.
\tag{4.2}
\]

Equality holds at `q=r=3`, and the ratio of the right side to the left side
increases when `r` is replaced by the next odd integer.  Combining
(4.1)--(4.2) gives

\[
\boxed{I_q(r)\ge {2q^r\over3r}.}
\tag{4.3}
\]

Therefore

\[
 I_q(r)^{-1/2}
 \le\sqrt{{3r\over2}}\,q^{-r/2},
\]

which completes (0.3).  With `r=2j+1`, this is explicitly

\[
 \delta_{j,s,q}
 \le\sqrt{{3(2j+1)\over2q}}\,q^{-j}
 =O_q(\sqrt j\,q^{-j});
\]

more simply, using `2j+1<=3j`,

\[
 \delta_{j,s,q}
 \le {3\over\sqrt{2q}}\sqrt j\,q^{-j}.
\tag{4.4}
\]

Multiplication by the `j+1` possible shifts proves (0.6).

## 5. Absolute summability of the coefficient tower

The squarefree-normalized fixed-depth theorem has `M^-2` coefficient

\[
 C_{2,j}
 ={16(1+\log2)\over3(1-q^{-1})}\delta_{j,0,q},
\tag{5.1}
\]

and `M^-3` coefficient

\[
 C_{3,j}
 ={32\over1-q^{-1}}\left[
 {\delta_{j,0,q}\bigl((7j+4)+(4j+1)\log2\bigr)\over9}
 +\sum_{s=1}^{j}\delta_{j,s,q}\right].
\tag{5.2}
\]

Equations (0.5)--(0.6) imply

\[
 C_{2,j}=O_q(\sqrt j\,q^{-j}),\qquad
 C_{3,j}=O_q(j^{3/2}q^{-j}).
\tag{5.3}
\]

Since a geometric factor dominates every fixed power of `j`,

\[
\boxed{
 \sum_{j\ge1}|C_{2,j}|<\infty,
 \qquad
 \sum_{j\ge1}|C_{3,j}|<\infty.}
\tag{5.4}
\]

The same conclusion holds before squarefree normalization.

## 6. What coefficient summability does not prove

Equation (5.4) closes the local delta-tower question left by the fixed-depth
packet: its displayed leading coefficients decay absolutely in `j`.

It does **not** permit termwise summation of the full conductor-layer
asymptotics.  The fixed-depth theorem has a remainder

\[
 O_{q,j}(M^{-4}),
\]

with no bound uniform in `j`.  Its profile classification also assumes
`h>=5j+2`, which changes regime when `j` grows with `M`.  Controlling those
remainders and the complementary growing-depth layers is a separate global
problem.  In particular, this packet does not prove that the total raw-zero
population over all minimum-degree layers is `O(M^-2)`.

## 7. Proof ledger and bounded replay

Proved:

- exact coefficient-one isolation of the independent top-degree sum `S_r`;
- the normalized `s=0` event and the parity-zero `s=j` endpoint;
- the explicit central-binomial inequality (3.2) and max-atom bound;
- the irreducible-count lower bound (4.3);
- uniform local decay (0.5), the summed bound (0.6), and coefficient
  summability (5.4).

Not claimed:

- a uniform-in-`j` conductor-layer asymptotic;
- summation of the `O_(q,j)(M^-4)` remainders;
- control of the growing-depth profile regime;
- an individual `L`-function zero, RH, or GRH consequence.

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_local_delta_tower_anticoncentration.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_local_delta_tower_anticoncentration.py --check
python -B -m unittest tests.test_quadratic_family_local_delta_tower_anticoncentration
python -B -O -m unittest tests.test_quadratic_family_local_delta_tower_anticoncentration
```

The replay checks only central binomial atoms up to `N=512`, exact
irreducible counts through `j=12` for `q=3,5,7,9`, and a few symbolic channel
signatures.  It enumerates no polynomial, irreducible, residue class, field
element, curve, point, or zero.
