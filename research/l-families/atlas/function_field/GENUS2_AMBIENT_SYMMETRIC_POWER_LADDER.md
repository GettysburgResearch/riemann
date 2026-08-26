# The marked ambient genus-two symmetric-power ladder

Status: **PROVED as an exact virtual Frobenius-trace ladder** for
\(r=2,4,6,8,10\) and every odd prime power \(q\).  The proof uses the
source-locked marked curve-open trace theorems and rebuilds every
decomposable-boundary row in bounded exact algebra.

Scope: the alternating compactly supported geometric-Frobenius trace of
\(V_{(r,0)}=\operatorname{Sym}^rV\) on the marked ambient stack
\(\mathcal A_2(w^1)\).  These are virtual trace identities.  They do not
identify individual cohomology groups or motives.

What was actually run: sparse integer algebra in

\[
 \mathbf Z[\mathbb L,\Delta,\Phi_{2,8},\Phi_{2,10}],
\]

with seven frozen JSON sources.  No finite field, curve, abelian surface,
cohomology group, or modular-symbol space was enumerated.

## 1. Exact ladder

Write \(\Theta_{8,2}(q)\) and \(\Theta_{10,2}(q)\) for the prime-power
Frobenius traces of the unique weight-eight and weight-ten newforms on
\(\Gamma_0(2)\), and write \(\Theta_\Delta(q)\) for the corresponding trace
of the level-one weight-twelve form.  Then

\[
\boxed{
\begin{array}{c|l}
r&\operatorname{Tr}\!\left(F_q,
 e_c(\mathcal A_2(w^1),V_{(r,0)})\right)\\ \hline
2&-2q,\\
4&-3q,\\
6&1-3q-q\Theta_{8,2}(q),\\
8&1-4q-q\Theta_{10,2}(q),\\
10&2-4q-2q\Theta_\Delta(q).
\end{array}}
\tag{1}
\]

Thus the preliminary formulas are all correct.  The point of the packet is
not merely to list them: it exhibits the exact boundary rows and the channel
shift that generates the ladder.

## 2. Frozen marked-open inputs

The source-locked smooth-curve traces are

\[
\begin{array}{c|l}
r&T_{(r,0)}^{\rm open}(q)\\ \hline
2&q-1,\\
4&-3,\\
6&-4,\\
8&-\Theta_{8,2}(q)-q-6,\\
10&(q-1)\Theta_\Delta(q)-\Theta_{8,2}(q)
     -\Theta_{10,2}(q)-q-7.
\end{array}
\tag{2}
\]

The marked-stack adapter identifies these model averages with alternating
compactly supported traces on \(\mathcal M_2(w^1)\).  The adapter and every
row in (2) are exact all-field inputs, not interpolations from small \(q\).

## 3. Direct decomposable-boundary rebuild

The marked odd theta characteristic distinguishes the two elliptic factors,
so the decomposable locus is the ordered product

\[
 \mathcal A_{1,1}(w^1)\cong Y_0(2)\times\mathcal A_1,
\tag{3}
\]

not an \(S_2\)-quotient.  On it,

\[
 \operatorname{Sym}^r(W_1\oplus W_1)
 =\bigoplus_{i=0}^r W_i\boxtimes W_{r-i}.
\tag{4}
\]

The producer verifies for every displayed \(r\) that

\[
 \sum_{i=0}^r(i+1)(r-i+1)=\binom{r+3}{3}.
\tag{5}
\]

The exact elliptic compact-support formulas are

\[
\begin{array}{c|c|c}
j&e_c(\mathcal A_1,W_j)&e_c(Y_0(2),W_j)\\ \hline
0&\mathbb L&\mathbb L-1,\\
j>0\text{ even}&-S[j+2]-1&-S[\Gamma_0(2),j+2]-2,\\
j\text{ odd}&0&0\text{ in every product row}.
\end{array}
\tag{6}
\]

The odd rows vanish because the central involution acts nontrivially on the
unmarked \(\mathcal A_1\) factor.  In the bounded weight range,

\[
\begin{aligned}
S[4]=S[6]=S[8]=S[10]&=0,&S[12]&=\Delta,\\
S[\Gamma_0(2),4]=S[\Gamma_0(2),6]&=0,&
S[\Gamma_0(2),8]&=\Phi_{2,8},\\
S[\Gamma_0(2),10]&=\Phi_{2,10},&
S[\Gamma_0(2),12]&=2\Delta.
\end{aligned}
\tag{7}
\]

The last identity is the two-copy level-two oldspace; the weight-twelve
newspace is zero.

For even \(r\leq10\), equations (4)--(7) give the boundary in one line:

\[
\begin{aligned}
B_r={}&-(\mathbb L-1)(S[r+2]+1)\\
&+\sum_{\substack{2\leq i\leq r-2\\ i\text{ even}}}
  \bigl(S[\Gamma_0(2),i+2]+2\bigr)
 -\mathbb L\bigl(S[\Gamma_0(2),r+2]+2\bigr).
\end{aligned}
\tag{8}
\]

The exact results of the direct rebuild are

\[
\begin{array}{c|l}
r&B_r\\ \hline
2&1-3\mathbb L,\\
4&3-3\mathbb L,\\
6&5-3\mathbb L-\mathbb L\Phi_{2,8},\\
8&7-3\mathbb L+\Phi_{2,8}-\mathbb L\Phi_{2,10},\\
10&(1-3\mathbb L)\Delta+\Phi_{2,8}+\Phi_{2,10}
    -3\mathbb L+9.
\end{array}
\tag{9}
\]

Adding (2) and (9), with \(\mathbb L\) specialized to \(q\), proves (1).

## 4. Channel-shift mechanism

The ladder has a precise spectral interpretation:

1. At \(r=2\), the open constant \(-1\) cancels the boundary constant
   \(+1\), leaving \(-2\mathbb L\).
2. At \(r=4\), the constants \(-3\) and \(+3\) cancel, leaving
   \(-3\mathbb L\).
3. At \(r=6\), the decomposable endpoint first injects the shifted channel
   \(-\mathbb L\Phi_{2,8}\).
4. At \(r=8\), the unshifted \(\Phi_{2,8}\) in the open trace cancels the
   boundary copy, while the next channel survives as
   \(-\mathbb L\Phi_{2,10}\).
5. At \(r=10\), the unshifted \(\Phi_{2,8}\), \(\Phi_{2,10}\), and
   \(\Delta\) channels all cancel.  The two-copy level-two oldspace changes
   the remaining coefficient to \(-2\mathbb L\Delta\).

The last step is the exact calculation

\[
 (\mathbb L-1)\Delta+(1-3\mathbb L)\Delta
 =-2\mathbb L\Delta.
\tag{10}
\]

This is a compact example of cohomological spectroscopy: the boundary does
not merely add an error term; it moves the visible automorphic channel by one
Tate factor and, at weight twelve, changes its multiplicity.

## 5. Tiny exact controls

The packet specializes the symbolic identities at \(q=3,5,7,9\).  The
ambient rows are

| \(q\) | \(r=2\) | \(r=4\) | \(r=6\) | \(r=8\) | \(r=10\) |
|---:|---:|---:|---:|---:|---:|
| 3 | -6 | -9 | -44 | 457 | -1,522 |
| 5 | -10 | -15 | 1,036 | -4,369 | -48,318 |
| 7 | -14 | -21 | -7,132 | 6,637 | 234,390 |
| 9 | -18 | -27 | 38,044 | 135,235 | 5,234,186 |

The \(q=9\) entries use Frobenius-root power sums.  In particular,
\(\Theta_\Delta(9)=-290790\), not the Fourier coefficient at index nine.
These controls falsify transcription errors; the theorem is the symbolic
all-\(q\) calculation above.

## 6. Interpretation firewall

Equations (1) and (9) are identities of alternating compactly supported
Frobenius traces.  They do not imply:

- a direct-sum decomposition of an individual \(H_c^i\);
- an isomorphism of motives or compatible systems;
- the absence of mutually canceling cohomology objects;
- a memberwise sign, zero-free region, or RH/GRH criterion.

No external novelty claim is made without a dedicated literature search.
The exact \(r=10\) endpoint is independently source-locked to commit
`50cbe644c6fa9cc4e6a7f5f03683883ffea83d49`; this packet derives it again as
the last row of one uniform boundary calculation.

## 7. Replay and resource contract

The producer closes the sparse symbolic ladder before reading its seven
frozen sources.  It then verifies LF-normalized SHA-256 hashes, Git blob IDs,
schemas, canonical payload hashes, theorem semantics, the marked-stack
adapter, the decomposable geometry, and the committed ambient
\(\operatorname{Sym}^{10}\) endpoint.

Hard caps are 5,000 exact polynomial operations, seven source files, 32,768
bytes per source, 131,072 source bytes total, 65,536 bytes per packet file,
and five seconds wall time.

```text
python -B research/l-families/atlas/function_field/genus2_ambient_symmetric_power_ladder.py --check
python -B -O research/l-families/atlas/function_field/genus2_ambient_symmetric_power_ladder.py --check
python -B -m unittest tests.test_genus2_ambient_symmetric_power_ladder
python -B -O -m unittest tests.test_genus2_ambient_symmetric_power_ladder
```
