# A simple-spectrum countermodel at arbitrarily large first exceptional height

Status: proposed synthetic obstruction, with an exact finite control.

Scope: disproves an inference from one fixed low critical reserve, a narrow
horizontal strip, an arbitrarily high first possible off-line height, a
small inverse-square budget, and a coarse complete zero count to *global*
four-node Pick positivity. It is not a Riemann-data counterexample.

## Family

Fix a critical pair at squared ordinate `r=200`, of multiplicity one.
Let `M=256`, `a=3/8`, `d_j=j/2^20`, `1<=j<=M`, and choose a large integer B.
Use M off-line quartets, each of multiplicity one, at

\[
\pm a\pm i(B+d_j).
\]

All their locations are distinct; every zero of the resulting even
polynomial is simple. A normalized polynomial with precisely these zeros is

\[
E_B(z)=(1+z^2/r)\prod_{j=1}^M
 \frac{(z^2+c_j)^2+h_j}{c_j^2+h_j},\quad
c_j=(B+d_j)^2-a^2,\quad h_j=4a^2(B+d_j)^2.
\]

For every given H>=1024, choose B>H and sufficiently large. The complete
upper-zero count is at most 513, so `N_+(T)<=T log T` for all T>=H.
The inverse-square budget is at most `M/B^2`; enlarging B makes it smaller
than any specified positive budget, in particular
`2(log H+1)/H`. The critical reserve meets `sqrt(r)<=H/2`. Thus the family
satisfies the repaired source contract, including complete zero
correspondence and order zero, with all off-line zeros simple and the strip
`a<=3/8`.

## Cofinal negative determinant

Let

\[
\mu_k(B)=2r^k+4\sum_{j=1}^M\Re(B+d_j+ia)^{2k},\quad k=0,1,2,3.
\]

These are the exact four moments in the large-real-node expansion of the
kernel. Direct polynomial expansion gives

\[
\begin{split}
\mu_0\mu_2-\mu_1^2&=8M B^4+O(B^3),\\
\mu_1\mu_3-\mu_2^2
 &=8M\{r-8M[a^2-\operatorname{Var}(d)]\}B^6+O(B^5),
\end{split}                                                       \tag{S1}
\]

where variance uses the uniform measure on the M distinct shifts. To check
the second coefficient, write `S_k=sum_j d_j^k`. The B^6 coefficient is

`16[4M S_2-4S_1^2-4M^2a^2+Mr/2]`,

which is the displayed expression. The B^8 and B^7 coefficients cancel
exactly.

For the chosen shifts,

\[
\operatorname{Var}(d)=\frac{M^2-1}{12\,2^{40}}
<\frac1{2^{24}},\qquad
8M[a^2-\operatorname{Var}(d)]>287>r=200.
\]

The second leading coefficient in (S1) is therefore strictly negative,
while the first is strictly positive. For all sufficiently large B their
signs differ. Formula (9) of PROOF.md applies to this finite complete source:
for every fixed distinct positive `u_1,...,u_4`, and then all sufficiently
large L, `det K_B(Lu_i,Lu_j)<0`.

This is a proved two-stage cofinal family: B first makes the entire
exceptional spectrum arbitrarily high, and L then detects it with four
positive real nodes. It supplies no particular actual off-line zero. It
also makes no claim of a uniform relation between the two thresholds
without an additional remainder bound.

## What this rules out

The obstruction concerns a *fixed single reserve* and the listed source
hypotheses. It does not contradict the compact multi-anchor theorems: those
use several independent low critical pairs and restrict evaluation nodes
to an explicitly proved interval. It does not establish that actual xi
has a negative four-node packet anywhere.

The arithmetic source, its Euler product, and further complete-spectrum
constraints could rule out this polynomial family. Those additional
constraints must be used in a proof; they do not follow from a strip-width
bound or the first exceptional height.
