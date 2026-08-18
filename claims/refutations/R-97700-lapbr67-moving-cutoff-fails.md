# R-97700 — `LAPBR67` fails at moving least-prime states just above the critical cutoff

Claim ID: `R-97700`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC REFUTATION**  
Created: 2026-08-18  
Depends on: PR #578 `L-97501/T-97500`; repaired `P_61` base asymptotic from PR #576; classical Mertens theorem for prime reciprocals and Bertrand's postulate  
RH status: **not assumed**

## 1. Statement

Let

\[
Z_X=(\log X)^{1/4}
\]

and let `p_0(X)` be the least prime strictly larger than `max(67,Z_X)`.
For the exact natural rough current of PR #578, let

\[
C_{L,p_0}(X)=
\sum_{\substack{m\ \mathrm{squarefree}\\
P^-(m)\ge p_0,\ \omega(m)<L}}
{\mu(m)\over\sqrt m}\,b(X/m),
\]

where `b=F_61` is the complete annular `5:3` base and inactive terms are zero.
The adaptive depth of `L-97501` is

\[
L_X(p_0)=\min\{L\ge2:\ L\text{ even},\ L\ge8(z_{p_0}(X)+1)\},
\qquad
z_{p_0}(X)=\sum_{p_0\le p\le Z_X}{1\over p}.
\]

For the moving state above, `z_{p_0}(X)=0`, hence

\[
\boxed{L_X(p_0(X))=8.}
\]

Then, for all sufficiently large `X`,

\[
\boxed{C_{8,p_0(X)}(X)<0.}
\]

Moreover the small-prime cube of PR #578 contains only the empty history, so

\[
\mathcal S_{p_0(X)}(X)=b(X)\ge0,
\qquad
\mathcal L_{p_0(X)}(X)=C_{8,p_0(X)}(X)-b(X)<0.
\]

Therefore the quantified theorem `LAPBR67`, which requires
`\mathcal L_{p_0}(X)>=0` uniformly at every admissible state for all sufficiently
large endpoints, is false.

## 2. Uniform base bounds

The repaired annular base satisfies

\[
b(Y)=a_*\sqrt Y+O(1),
\qquad a_*>0,
\]

and `b(Y)>=0` for every active `Y`.
Consequently there are absolute constants `c,C>0` and `Y_0` such that

\[
0\le b(Y)\le C\sqrt Y\qquad(Y\ge1),
\]

and

\[
b(Y)\ge c\sqrt Y\qquad(Y\ge Y_0).
\]

The compact range is absorbed into `C`; no uniformity issue in `Y` remains.

## 3. Positive even layers

Put

\[
z_+(X)=\sum_{p_0(X)\le p\le X}{1\over p}.
\]

For `r=0,2,4,6`, positivity of `b` and the global upper bound give

\[
\sum_{\substack{m\le X,\ P^-(m)\ge p_0\\
\omega(m)=r}}
{1\over\sqrt m}b(X/m)
\le
C\sqrt X
\sum_{\substack{m\le X,\ P^-(m)\ge p_0\\
\omega(m)=r}}{1\over m}.
\]

Dropping the product constraint only enlarges the positive sum.  If `e_r` is
the elementary symmetric polynomial in the variables `{1/p}`, then

\[
e_r\le {z_+^r\over r!}.
\]

Hence the complete contribution of the even layers is at most

\[
C\sqrt X\left(1+{z_+^2\over2!}+{z_+^4\over4!}+{z_+^6\over6!}\right).
\tag{R-97700.1}
\]

The odd layers `r=1,3,5` are nonpositive and may be discarded in an upper
bound.

## 4. A seventh-layer negative reservoir

Restrict the `r=7` layer to seven distinct primes in

\[
p_0(X)\le p\le X^{1/8}.
\]

Every resulting product is at most `X^{7/8}`, hence
`X/m>=X^{1/8}>=Y_0` for large `X`.  Therefore this subfamily contributes at most

\[
-c\sqrt X\,e_7\!\left(\left\{{1\over p}:p_0(X)\le p\le X^{1/8}\right\}\right).
\tag{R-97700.2}
\]

Let

\[
z_-(X)=\sum_{p_0(X)\le p\le X^{1/8}}{1\over p}.
\]

For fixed `r`, if positive variables `x_i` have sum `z` and
`s_2=\sum x_i^2`, then

\[
r!e_r=z^r+O_r(s_2 z^{r-2}).
\tag{R-97700.3}
\]

Indeed `z^r` is the sum over all ordered `r`-tuples, while tuples with a
repeated index have total mass at most
`\binom r2 s_2 z^{r-2}` times an `r`-dependent multiplicity.
Here

\[
s_2\le {z_-\over p_0(X)}=o(z_-),
\]

so

\[
e_7={z_-^7\over7!}(1+o(1)).
\tag{R-97700.4}
\]

## 5. Prime-harmonic comparison

Bertrand gives

\[
Z_X<p_0(X)\le2Z_X
\]

for all sufficiently large `X`.  Mertens' theorem for primes therefore yields

\[
z_-(X)
=
\log\log(X^{1/8})-\log\log p_0(X)+O(1)
\to\infty,
\]

and

\[
z_+(X)=z_-(X)+O(1).
\tag{R-97700.5}
\]

Combining (R-97700.1)--(R-97700.5),

\[
C_{8,p_0(X)}(X)
\le
C\sqrt X\,O(z_-^6)
-
{c\sqrt X\over7!}z_-^7(1+o(1))<0.
\]

This proves the claim.

## 6. Consequence for the closure architecture

The positive small-prime cube of PR #578 remains a valid theorem.  What fails
is its proposed complementary uniform large-prime sign.  The failure is not a
finite-endpoint accident: it is forced by a moving admissible state where the
small-prime mass is empty but the future reciprocal-prime mass diverges.

Thus a successful continuation must retain the future-prime profile, or exploit
signed Type-I/Type-II cancellation, rather than assigning a fixed depth after
crossing the moving cutoff.

```text
small-prime critical cube                   RETAINED / PROVED
LAPBR67 as quantified in PR #578            REFUTED
moving-cutoff mechanism                     PROVED ASYMPTOTIC
future-prime / signed-correlation repair     REQUIRED
Riemann Hypothesis                           UNPROVED
```
