# Separate complete amplification bounds for the first three derivatives

Status: proposed complete-source corollary, pending independent full review.
Scope: global complete xi Pick order 1,476,000 with the classical strip,
or 1,545,000 with the additional complete 3/8 displacement hypothesis.
Finite orders and changing-cutoff tails remain distinct; RH is open.
Dependencies: the separately frozen and independently reviewed
[VOLTERRA_SQUARE_DOUBLE_COUNT.md](VOLTERRA_SQUARE_DOUBLE_COUNT.md), SHA-256
`f749951aa06421b4856d26ff795127f22649980371d16b619e4003df0dba6629`,
and its source/node/rational-class, Turing, density and published critical-line
verification inputs. The optional narrower strip retains its explicitly
additional imported theorem scope. No earlier packet is changed.
What was run: exact rational complete exponential-tail bounds, derivative
reserve inequalities, complete-source scalar gaps and literal paid-order
checks in verify_separate_amplification.py, normal and optimized Python.
Smallest remaining gap: independent review of this new amplification proof.

## DA1. Retain the improved square inside the whole Minkowski series

Use the complete weighted polynomial dilation bounds

`||D||<=d*n^2`, `||D^2||<e*n^4`,
`d=3191/5000`, `e=2907/10000`, `n>=850000`.

Set `r=e/d^2<1`, `q=n^2/T`, `xi=2A*d*q`, and let
`p>exp(4A*q/n)` bound the original signed-pole prefactor. Since D commutes
with its powers,

`||D^j||<=e*d^(j-2)*n^(2j)` for every j>=2.

Apply this term by term to the same full variable-path discrete Minkowski
series; each ordinate retains its independently chosen displacement and
all paths tau*a_b. The complete polynomial amplitudes for P, DP and D²P,
relative respectively to `1`, `d*n²`, and `e*n⁴`, are bounded by

\[
 S_0=p[1+\xi+r(e^\xi-1-\xi)],\quad
 S_1=p[1+r(e^\xi-1)],\quad S_2=pe^\xi.
\tag{DA1}
\]

For DP the j=0 term uses the first bound, while all j>=1 terms use the
square bound. For D²P every term uses the square bound and then additional
powers of D. These are full exponential-series bounds, with no truncated
Taylor remainder or constant-displacement substitution.

For a fixed endpoint q0, replace `exp(xi)` in DA1 by a complete exact
rational upper E at `xi0=2A*d*q0`. The resulting upper amplitudes apply
uniformly to all q<=q0. They are increasing because each power-series
coefficient is nonnegative. They satisfy `S0,S1<=S2`, `S1>=1`, and
`S0/S1<=S2`. At the accepted endpoints below, `S2<8/5`.

## DA2. Preserve each derivative's own amplitude in the product rule

The original rational prefactor estimates give

`||R||src<=S0*sqrt(S(q)B)`,
`||b R'||src<=(d*S1+3*S0/n)*n²*sqrt(S(q)B)`.

The exact guard `d+24/(5*850000)<C1=6383/10000` gives
`||b R'||src<=C1*S1*n²*sqrt(S(q)B)` uniformly, since S0/S1<8/5.
For R'' retain the VS5 bound: the D² term has amplitude S2 and every
lower term has amplitude at most S2. Thus

`||b² R''||src<=C2*S2*n⁴*sqrt(S(q)B)`, `C2=291/1000`.

The unshifted continuous derivative bounds and twice-integrated count
quadrature are unchanged: `C=C2+C1²`, `J=4*cA'*C`,
`cA'=3762011/28729000`, and `S(q)=U*+J*q²` with the frozen density
constants `m*=(113/355)(1-1838/28729)`, `U*=106/333`.

For f=R+R-, each of the two outer second-derivative product terms now
costs `C2*S2*S0*q²*S(q)B`, and the middle term costs
`2*C1²*S1²*q²*S(q)B`. The complete conjugate Taylor remainder therefore
has loss at most

\[
 A^2[C_2S_2S_0+C_1^2S_1^2]q^2(U_*+Jq^2)B.
\tag{DA2}
\]

All multiplicities, both signed-pole classes, and reflected upper members
of the complete source remain included. The factor A² follows from the
unchanged integral remainder A²/2 and the product-rule factor two.

## DA3. Two exact finite source payments

Use the exact uniform prefactor upper `p=500001/500000`, and the complete
positive exponential upper through degree eight with its full geometric
tail. The two endpoint choices are

| Complete A bound | q0 | Global headline order | Maximum even order at H0 |
| --- | --- | ---: | ---: |
| 1/2 | 727/1000 | 1,476,000 | 1,476,820 |
| 3/8 | 199/250 | 1,545,000 | 1,545,314 |

The checker verifies `exp(4A*q0/850000)<p`, computes the entire upper
amplitudes, and verifies the exact strict reserve

\[
 m_*-Jq_0^2-
 A^2[C_2S_2S_0+C_1^2S_1^2]q_0^2(U_*+Jq_0^2)>0.
\tag{DA3}
\]

The reserves are about 0.000313850 and 0.000703081, respectively. Only
the exact rational endpoint reserves in the receipt are acceptance guards.
All negative costs increase with q, so this pays every q<=q0.

At any node-independent good cutoff T>=H0=3000000000000, each complete
tail is strictly positive at every even n>=850000 satisfying respectively
`1000*n²<=727*T` or `250*n²<=199*T`. Principal submatrices cover all
smaller orders. Cofinal good cutoffs give selectable orders for changing
tail kernels. Adding the entire verified critical source below or at the
common cutoff in `[H0,H0+20]` gives the two global headline orders. The
same imported published verification covers that entire cutoff interval.
No new zero census or cutoff calculation is used. The second result also
retains its additional uniform narrower strip. Neither claim proves global
all-order positivity or RH.
