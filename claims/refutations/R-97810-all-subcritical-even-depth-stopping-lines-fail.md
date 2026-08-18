# R-97810 — Every subcritical count-depth factor-67 stopping line is eventually negative

Claim ID: `R-97810`  
Status: **PROVED UNCONDITIONAL ASYMPTOTIC NO-GO**  
Created: 2026-08-18  
Frozen base: PR #590 at `223f11259b3e7134f78d6492795e6e94caca8be3`  
RH status: **not assumed**

Let `b(Y)` be the complete `P_61` annular `5:3` base scalar.  The retained
annular theorem gives constants `c_0,C_0,Y_0>0` such that

\[
 b(Y)\ge c_0\sqrt Y\quad(Y\ge Y_0),
 \qquad
 0\le b(Y)\le C_0\sqrt Y\quad(Y\ge1).
\tag{R-97810.1}
\]

For an even integer-valued depth `L=L(X)>=2`, define the exact natural root
current

\[
 C_L(X)=
 \sum_{\substack{m\le X\\m\ \mathrm{squarefree}\\P^-(m)\ge67\\
                  \omega(m)<L}}
 \frac{\mu(m)}{\sqrt m}\,b(X/m).
\tag{R-97810.2}
\]

Put

\[
 \Lambda_X=\sum_{67\le p\le X}\frac1p.
\]

Assume

\[
 \boxed{L(X)\log(2L(X))=o(\Lambda_X).}
\tag{R-97810.3}
\]

Then

\[
 \boxed{C_L(X)<0}
\]

for all sufficiently large `X`.

## Proof

Write `r=L-1`, so `r` is odd.  Let

\[
 B_j(X)=
 \sum_{\substack{m\le X\\m\ \mathrm{squarefree}\\P^-(m)\ge67\\
                  \omega(m)=j}}
 \frac1{\sqrt m}\,b(X/m),
\]

so that `C_L=sum_(j=0)^r (-1)^j B_j`.

Choose

\[
 Y=X^{1/(2r)},
 \qquad
 A_Y=\sum_{67\le p\le Y}\frac1p.
\]

Mertens' prime-harmonic theorem gives

\[
 A_Y=\Lambda_X-\log(2r)+O(1).
\tag{R-97810.4}
\]

The hypothesis implies

\[
 \frac r{A_Y}\longrightarrow0,
 \qquad
 r\log\frac{\Lambda_X}{A_Y}\longrightarrow0.
\tag{R-97810.5}
\]

Every product of `r` primes at most `Y` is at most `sqrt(X)`.  Hence, for large
`X`, every such child lies in the lower range of (R-97810.1).  If `e_r(Y)` is
the elementary symmetric sum of the weights `{1/p:67<=p<=Y}`, then

\[
 B_r(X)\ge c_0\sqrt X\,e_r(Y).
\tag{R-97810.6}
\]

Let `S_2=sum_(p>=67)p^-2<infinity`.  Expanding `A_Y^r`, and using a union bound
for ordered tuples with a repeated coordinate, gives

\[
 r!e_r(Y)
 \ge A_Y^r-\binom r2S_2A_Y^{r-2}
 =A_Y^r(1-o(1)).
\tag{R-97810.7}
\]

For `j<r`, (R-97810.1) and Maclaurin's elementary bound give

\[
 B_j(X)\le C_0\sqrt X\frac{\Lambda_X^j}{j!}.
\tag{R-97810.8}
\]

Because `r/Lambda_X -> 0`, these majorants increase throughout `0<=j<r`, and

\[
 \sum_{j<r}B_j(X)
 \le 2C_0\sqrt X\frac{\Lambda_X^{r-1}}{(r-1)!}
\tag{R-97810.9}
\]

for large `X`.  Therefore

\[
 \frac{B_r(X)}{\sum_{j<r}B_j(X)}
 \ge
 \frac{c_0}{2C_0}\frac{A_Y}{r}
 \left(\frac{A_Y}{\Lambda_X}\right)^{r-1}(1-o(1))
 \longrightarrow\infty
\tag{R-97810.10}
\]

by (R-97810.5).  The dominating layer has odd index `r`, so it enters the
current with a minus sign.  Thus `C_L(X)<0`.

## Consequences

1. PR #590's refutation is not special to its published adaptive depth.  Every
   count-depth rule satisfying (R-97810.3) fails.
2. Since `Lambda_X~log log X`, any successful count-depth stopping line must
   leave the subcritical regime; in particular, depths
   `O(log log log X)` are impossible.
3. This theorem does not refute the complete small-prime cube or a non-depth
   Bellman/Lorenz resummation.  It rules out requiring a shallow full rough
   current to be nonnegative.
