# R-97700 — Every subcritical threshold depth has an eventually negative native current

Claim ID: `R-97700`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC NO-GO THEOREM**  
Created: 2026-08-18  
Depends on: the sharp annular base theorem on PR #587; `L-97700`  
RH status: **unproved**

Let `b(X)=F_61(X)`. The exact annular theorem gives

\[
b(Y)=a\sqrt Y+O(1),
\qquad
 a=12\prod_{p\le61}(1-1/p)>0,
\tag{R-97700.1}
\]

and `b(Y)>=0`. For an even integer `L=L(X)>=2`, define the literal natural
current through depth `L-1` by

\[
C_L(X)=
\sum_{\substack{m\in\mathcal R_{67}^{\rm sf}\\\omega(m)<L}}
 {\mu(m)\over\sqrt m}b(X/m).
\tag{R-97700.2}
\]

If

\[
\boxed{L(X)\log L(X)=o(\log\log X),}
\tag{R-97700.3}
\]

then

\[
\boxed{C_L(X)<0}
\tag{R-97700.4}
\]

for all sufficiently large `X`.

## Proof

Put `k=L-1`, which is odd, and

\[
z_X=\sum_{67\le p\le X}{1\over p},
\qquad
W=X^{1/(2k)},
\qquad
z_W=\sum_{67\le p\le W}{1\over p}.
\]

From (R-97700.1) there are constants `0<c<C` such that

\[
b(Y)\ge c\sqrt Y\quad(Y\text{ large}),
\qquad
|b(Y)|\le C\sqrt Y\quad(Y\ge1).
\tag{R-97700.5}
\]

Every `k`-fold product of primes at most `W` is at most `sqrt(X)`, so its
argument `X/m` is large. If `e_j(S)` denotes the elementary symmetric sum of
order `j` in `{1/p:p in S}`, then, discarding other negative levels,

\[
C_L(X)
\le C\sqrt X\sum_{j=0}^{k-1}e_j(\{p\le X\})
   -c\sqrt X\,e_k(\{p\le W\}).
\tag{R-97700.6}
\]

The standard bounds

\[
e_j(\{p\le X\})\le {z_X^j\over j!}
\]

and, with `s_2=sum_(p>=67)p^(-2)<infinity`,

\[
e_k(\{p\le W\})
\ge {z_W^k\over k!}
\left(1-{\binom{k}{2}s_2\over z_W^2}\right)
\tag{R-97700.7}
\]

follow respectively from the multinomial expansion and a union bound on
repeated coordinates in the ordered `k`-tuple expansion.

Condition (R-97700.3) implies `k/z_X ->0`. Hence

\[
\sum_{j=0}^{k-1}{z_X^j\over j!}
\le(1+o(1)){z_X^{k-1}\over(k-1)!}.
\tag{R-97700.8}
\]

Mertens' theorem gives

\[
z_W=z_X-\log(2k)+o(1).
\tag{R-97700.9}
\]

Therefore

\[
{e_k(\{p\le W\})
 \over z_X^{k-1}/(k-1)!}
\ge(1-o(1)){z_W\over k}
\left({z_W\over z_X}\right)^{k-1}
\longrightarrow\infty,
\tag{R-97700.10}
\]

because `k log k=o(z_X)`. The final odd layer in (R-97700.6) therefore
strictly dominates every preceding positive layer, proving (R-97700.4).

## Exact finite witnesses

The 256-bit MPFR replay certifies

\[
C_2(32605)>0>C_2(32606)
\]

and

\[
C_2(61841)<-21.3,
\qquad
\mathcal A_{61841}>9.5.
\]

Thus a negative threshold current can coexist with a positive native root; the
current sign is not a proxy for the conclusion.
