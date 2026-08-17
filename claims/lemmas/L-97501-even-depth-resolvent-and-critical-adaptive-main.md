# L-97501 — Even-depth resolvents and a positive exact small-prime critical cube

Claim ID: `L-97501`  
Status: **PROVED EXACT OPERATOR THEOREM + UNCONDITIONAL SOURCE-COMPLETE ASYMPTOTIC THEOREM**  
Created: 2026-08-17  
Inputs: PR #576 `L-97400`; PR #561 `L-96502`; classical PNT/Mertens theorems  
RH status: **not assumed**

Let `A` be positive and nilpotent and suppose

\[
 (I+A)\mathcal F=g.
\]

For every even integer `L>=2`, put

\[
 C_L(A)=\sum_{j=0}^{L-1}(-A)^j g.
\]

The finite geometric identity gives

\[
 \boxed{C_L(A)=(I-A^L)\mathcal F.}
 \tag{L-97501.1}
\]

For a fixed even `L`, componentwise positivity of `C_L(A)` implies positivity
of `mathcal F`, because

\[
 (I-A^L)^{-1}=\sum_{m\ge0}A^{mL}
\]

is a finite positive sum.  More generally, one may choose a different even
stopping depth at every state and conclude by finite induction on the remaining
scale, provided the corresponding current is nonnegative at every state.

For the natural rough operator, `C_L(R)` is the exact current through history
depth `L-1`.  PR #561/#568 prove that every **fixed** even depth is eventually
negative in each fixed component row and in the `5:3` scalar.

## 1. Source-mass depth becomes full expansion

Let

\[
 z_{1/2}(Y)=\sum_{67\le p\le Y}p^{-1/2}
\]

and let `D(Y)` be the maximum number of distinct primes at least `67` whose
product is at most `Y`.  The sufficient homogeneous depth in PR #569 is

\[
 L\ge8(z_{1/2}(Y)+1).
\]

The prime number theorem and partial summation give

\[
 z_{1/2}(Y)\sim\frac{2\sqrt Y}{\log Y},
\]

whereas

\[
 D(Y)\asymp\frac{\log Y}{\log\log Y}.
\]

Consequently the source-mass depth exceeds the full nilpotence depth for all
sufficiently large `Y`.  It is a correct homogeneous inequality but not a
proper asymptotic stopping line.

## 2. Exact annular base and natural fixed-depth current

Let `b(Y)` be the complete `P_61` annular `5:3` scalar of PR #576.  In the
notation of its `L-97400`, `b(Y)=F(Y)`.  That theorem gives

\[
 b(Y)\ge0\quad(Y\ge1)
\]

and its finite Euler-ramp expansion gives the unconditional asymptotic

\[
 \boxed{
 b(Y)=a_*\sqrt Y+O(1),
 \qquad
 a_*=12\prod_{p\le61}\left(1-\frac1p\right)>0.
 }
 \tag{L-97501.2}
\]

Fix an admissible state whose allowed rough primes are `p>=p_0>=67`.  Exact
least-prime expansion gives the even-depth current

\[
 \boxed{
 C_{L,p_0}(X)=
 \sum_{\substack{m\ \mathrm{squarefree}\\
                  P^-(m)\ge p_0,\ \omega(m)<L}}
 \frac{\mu(m)}{\sqrt m}\,b(X/m),
 }
 \tag{L-97501.3}
\]

with the convention `b(u)=0` when the annular packet is inactive.  This is a
literal source partition, not a formal Euler product.

## 3. A positive exact small-prime cube

For `X>e^e`, set

\[
 Z_X=(\log X)^{1/4},
 \qquad
 z_{p_0}(X)=\sum_{p_0\le p\le Z_X}\frac1p,
\]

and let `L_X(p_0)` be the smallest positive even integer satisfying

\[
 \boxed{L_X(p_0)\ge8\bigl(z_{p_0}(X)+1\bigr).}
 \tag{L-97501.4}
\]

Define the exact small-prime part of (L-97501.3) by

\[
 \mathcal S_{p_0}(X)=
 \sum_{\substack{m\ \mathrm{squarefree}\\
                  p\mid m\Rightarrow p_0\le p\le Z_X,\\
                  \omega(m)<L_X(p_0)}}
 \frac{\mu(m)}{\sqrt m}\,b(X/m).
 \tag{L-97501.5}
\]

Then, uniformly in every admissible `p_0`,

\[
 \boxed{\mathcal S_{p_0}(X)>0}
 \tag{L-97501.6}
\]

for all sufficiently large `X`.

### Proof

Write `L=L_X(p_0)` and let `e_j` be the elementary symmetric sums of
`{1/p:p_0<=p<=Z_X}`.  Maclaurin's inequality gives

\[
 e_j\le z^j/j!,\qquad z=z_{p_0}(X),
\]

and

\[
 P=\prod_{p_0\le p\le Z_X}(1-1/p)\ge e^{-2z}.
\]

The standard exponential-tail estimate and `L>=8(z+1)` give

\[
 \sum_{j\ge L}e_j
 \le e^z\left(\frac{ez}{L}\right)^L
 <\frac12e^{-2z}\le\frac12P.
\]

Since `L` is even,

\[
 \boxed{
 \sum_{j=0}^{L-1}(-1)^je_j>\frac12P>0.
 }
 \tag{L-97501.7}
\]

Every `m` occurring in (L-97501.5) satisfies

\[
 m\le Z_X^L
 =\exp\!\bigl(O(\log\log X\,\log\log\log X)\bigr)
 =X^{o(1)}.
\]

Thus `X/m->infinity` uniformly over the whole cube.  Substitution of
(L-97501.2) into (L-97501.5) gives

\[
 \mathcal S_{p_0}(X)
 =a_*\sqrt X\sum_{j=0}^{L-1}(-1)^je_j+E_X,
 \tag{L-97501.8}
\]

where

\[
 |E_X|
 \ll\prod_{p_0\le p\le Z_X}(1+p^{-1/2}).
\]

By the prime number theorem,

\[
 \log\prod_{p_0\le p\le Z_X}(1+p^{-1/2})
 \ll \frac{\sqrt{Z_X}}{\log Z_X}
 \ll\frac{(\log X)^{1/8}}{\log\log X}.
\]

Mertens' theorem gives `P>>1/log Z_X`.  Hence the positive main term in
(L-97501.8) is

\[
 \gg\frac{\sqrt X}{\log Z_X},
\]

whereas `E_X=X^{o(1)}`.  The main term dominates uniformly and proves
(L-97501.6).

Finally,

\[
 z_{p_0}(X)=O(\log\log\log X),
 \qquad
 L_X(p_0)=O(\log\log\log X),
 \tag{L-97501.9}
\]

while the complete rough depth is asymptotic to
`log X/log log X` at the root.  Thus this is a genuinely partial,
source-complete, growing-order positive block.  It includes the exact annular
base `b(X/m)`; activation and finite-`P_61` remainders have not been discarded.
