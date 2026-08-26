# Odd-notch third-boundary trace-zero density

Status: **exact fixed-`q` residual and profile theorem, with raw detector-zero
density through `M^-3`, conditional only on the standard fixed-modulus
prime-polynomial progression theorem; not a statement about a zero of an
individual `L`-function**.

Exact replay:
[`quadratic_family_third_boundary_trace_zero_density.py`](quadratic_family_third_boundary_trace_zero_density.py).

## 0. Outcome

Fix an odd prime power `q`, put

\[
 n=2h+1,\qquad M=4h+1,\qquad d=h-2,
\]

and assume `h>=12`.  Let `Z^(3)_(q,h)` count monic squarefree degree-`M`
conductors whose least factor degree is exactly `d` and whose raw closed-place
notch detector vanishes.  Define the two finite local probabilities

\[
 \delta_{5,q}=\Pr(D_5=0),\qquad
 \delta_{53,q}=\Pr(D_5+D_3=0).
\tag{0.1}
\]

Then

\[
\boxed{
 {Z^{(3)}_{q,h}\over q^M}
 ={\delta_{5,q}(1+\log2)\over3h^2}
 +{1\over h^3}\left(
 {\delta_{5,q}(5+2\log2)\over6}
 +{\delta_{53,q}\over2}\right)
 +O_q(h^{-4}).}
\tag{0.2}
\]

After division by the exact squarefree count `q^M-q^(M-1)` and use of
`h=(M-1)/4`, this is

\[
\boxed{
 {Z^{(3)}_{q,h}\over q^M-q^{M-1}}
 ={1\over1-q^{-1}}\left[
 {16\delta_{5,q}(1+\log2)\over3M^2}
 +{32\bigl(\delta_{5,q}(2+\log2)+\delta_{53,q}\bigr)\over M^3}
 +O_q(M^{-4})\right].}
\tag{0.3}
\]

Both probabilities in (0.1) are strictly positive for every odd prime power
`q`.  Thus the third boundary has a genuine `M^-2` population.  It has no
`M^-1` population.  The first mixed channel appears at `M^-3`, while the
native `D_5+2D_1` channel is only `M^-4`.

## 1. Frozen inputs and claim boundary

This packet uses the following historical blobs, not the moving working-tree
copies.

| input | commit | blob |
|---|---|---|
| closed-place notch | `9716d2261e9e7843a6c1ffffd67ee8d6756060aa` | `a1b8476ddd3cad6f63ff205392426ae9c2d0829c` |
| depth phase diagram | `4fc8930e14eaa3863d3f3edc151c056d7d5aedce` | `01cefa8a55c9b1ae1a0b5bed9c11fe323fb6764e` |
| parity sieve | `0b9f407f10ab8b12f22526af8a08b870baaef0e9` | `38f1b6e95f9a7eb6756450673ff067308886a0ff` |
| second-boundary residual | `97cdc4a5ea27bc1052dbad7eef19276da331388c` | `80e6e3c5e3001011356df13381c9ad45b66d2245` |
| second-boundary third order | `f5aabadd65dd53cd9a69e3e3b38b9bc7693b3359` | `12aa4be45fd970f843be6b2024547f7ab7594b21` |

The only analytic input beyond those exact identities is the standard
prime-polynomial theorem in fixed residue classes.  Nothing below implies an
individual `L`-function zero, RH, GRH, or an external novelty claim.

## 2. Exact residual collapse

Write `m_j` for the number of irreducible factors of `Q` having degree `j`.
The locked notch identity is

\[
 S_{n,Q}=\sum_{k=1}^{h}a_kD_{n-2k},\qquad
 \sum_{k\ge0}a_kx^k=\prod_{P\mid Q}(1-x^{\deg P})^{-1}.
\tag{2.1}
\]

On the present boundary, `a_k=0` for `k<h-2`.  Since
`2(h-2)>h`, no sum of two factor degrees can enter any of the three
remaining coefficients.  Therefore

\[
 a_{h-2}=m_{h-2},\qquad a_{h-1}=m_{h-1},\qquad a_h=m_h,
\]

and (2.1) becomes the exact three-channel identity

\[
\boxed{
 S_{n,Q}=m_{h-2}D_5+m_{h-1}D_3+m_hD_1.}
\tag{2.2}
\]

Every monic polynomial of degree at most five is coprime to `Q`.  If
\(p_r=\sum_{\deg F=r}\psi_Q(F)\), then `p_1,p_3,p_5` are sums of an odd
number of signs and hence are odd.  Since

\[
 D_1=p_1,\qquad D_3=p_3-qp_1,\qquad D_5=p_5-qp_3,
\]

we have

\[
\boxed{D_1\equiv1\pmod2,\qquad D_3\equiv D_5\equiv0\pmod2.}
\tag{2.3}
\]

Thus every raw zero has even `m_h`.  The degree budget permits only
`m_h=0` or `m_h=2`.  In the latter case it forces the unique profile

\[
 (h-2,h,h,h+3),
\]

whose exact residual is `D_5+2D_1`.  This profile has four factors and
therefore total density `O_q(M^-4)`.

## 3. Exhaustive profile and parity table

For four factors write the three degrees after the distinguished `d` as
`d+x,d+y,d+z`.  Their nonnegative nondecreasing excesses obey

\[
 x+y+z=9.
\tag{3.1}
\]

This proves finiteness of the four-factor list.  Five factors are impossible
because `5(h-2)>4h+1` for `h>=12`.  The following table is exhaustive.

| residual condition | profiles | scale |
|---|---|---:|
| `D_5=0` | `(d,3h+3)`; `(d,e,3h+3-e)`, `h+1<=e<=(3h+3)/2`; `(d,d,2h+5)` | `M^-2`, including its `M^-3` correction |
| `D_5=0` | `(d,d,d,h+7)`, `(d,d,h+1,h+4)`, `(d,d,h+2,h+3)`, `(d,h+1,h+1,h+1)` | `M^-4` |
| `D_5+D_3=0` | `(d,h-1,2h+4)` | `M^-3` |
| `2D_5+D_3=0` | `(d,d,h-1,h+6)` | `M^-4` |
| `D_5+2D_3=0` | `(d,h-1,h-1,h+5)` | `M^-4` |
| `D_5+D_3=0` | `(d,h-1,h+1,h+3)`, `(d,h-1,h+2,h+2)` | `M^-4` |
| `D_5+2D_1=0` | `(d,h,h,h+3)` | `M^-4` |
| impossible by (2.3) | `(d,h,2h+3)`, `(d,d,h,h+5)`, `(d,h-1,h,h+4)`, `(d,h,h+1,h+2)` | zero |

The midpoint in the generic three-factor row is counted with weight `1/2`
when the two complementary degrees agree.  Equation (3.1) gives the entire
four-factor part of the table by listing the partitions of `9`; it is not an
asymptotic guess.

The whole fixed minimum-degree layer is `O_q(q^M/h^2)` by the locked rough
layer bound.  This already excludes an `M^-1` term.  The table then shows
that only the first generic row can contribute at `M^-2`; only its Euler
correction, `(d,d,2h+5)`, and `(d,h-1,2h+4)` can contribute at `M^-3`.

## 4. Exact profile weights through third order

Let `W_1(h)` be the principal `q^M` weight of the one-pinned `D_5=0`
profiles with two or three total factors.  Partial fractions, with half
weight at the midpoint, give the exact identity

\[
\begin{aligned}
 W_1(h)
 &= {1\over(h-2)(3h+3)}
 +{1\over h-2}\sum_{e=h+1}^{(3h+3)/2}{}^{\!*}
 {1\over e(3h+3-e)}\\
 &= {1+H_{2h+2}-H_h\over(h-2)(3h+3)}.
\end{aligned}
\tag{4.1}
\]

Euler--Maclaurin gives

\[
 H_{2h+2}-H_h=\log2+{3\over4h}+O(h^{-2}),
\]

and hence

\[
 W_1(h)
 ={1+\log2\over3h^2}
 +{7/12+(\log2)/3\over h^3}+O(h^{-4}).
\tag{4.2}
\]

The repeated-minimum profile has weight

\[
 {1\over2(h-2)^2(2h+5)}={1\over4h^3}+O(h^{-4}),
\tag{4.3}
\]

while the mixed profile has weight

\[
 {1\over(h-2)(h-1)(2h+4)}={1\over2h^3}+O(h^{-4}).
\tag{4.4}
\]

Multiplying (4.2)--(4.4) by their local zero probabilities proves (0.2).
The conversion

\[
 h^{-2}=16M^{-2}+32M^{-3}+O(M^{-4}),\qquad
 h^{-3}=64M^{-3}+O(M^{-4})
\]

then proves (0.3).

## 5. The finite local law

Let `N_r=I_q(r)` and let

\[
 S_r=\sum_{\deg R=r}\epsilon_R,
\]

where all `epsilon_R` are independent uniform signs.  Put

\[
\begin{aligned}
 h_2(S;N)&={S^2+N\over2},\\
 h_3(S;N)&={S^3+(3N+2)S\over6},\\
 h_5(S;N)&={S^5+(10N+20)S^3+(15N^2+50N+24)S\over120}.
\end{aligned}
\tag{5.1}
\]

Expanding the Euler product only through degree five gives

\[
\boxed{
 D_3=S_3+S_1S_2+h_3(S_1;N_1)-qS_1,}
\tag{5.2}
\]

and

\[
\boxed{
\begin{aligned}
 D_5={}&S_5+S_1S_4+S_2S_3+h_2(S_1;N_1)S_3
       +h_2(S_2;N_2)S_1\\
      &+h_3(S_1;N_1)S_2+h_5(S_1;N_1)\\
      &-q\bigl(S_3+S_1S_2+h_3(S_1;N_1)\bigr).
\end{aligned}}
\tag{5.3}
\]

These formulas make (0.1) exact finite probabilities.  For example, at
`q=3`,

\[
 \delta_{5,3}={11000690707734068076805\over151115727451828646838272},
\]

\[
 \delta_{53,3}={44252230658139381379541\over604462909807314587353088}.
\]

No polynomial or field enumeration is used to obtain these fractions; the
replay sums only the binomial multiplicities of the five aggregate sign
sums.

## 6. Positivity of both local constants

For odd `q`, the exact counts

\[
 N_3={q^3-q\over3},\qquad
 N_4={q^4-q^2\over4},\qquad
 N_5={q^5-q\over5}
\]

are even.  Set

\[
 e\equiv N_2\pmod2,\qquad
 S_1=1,\quad S_2=e,\quad S_3=S_4=0.
\]

All four prescribed sums are attainable.  Before choosing `S_5`, formulas
(5.2)--(5.3) reduce to

\[
 D_3=e+{1-q\over2},\qquad
 D_5=-{(q+3)(q-1)\over8}+{e(2-q)\over2}.
\tag{6.1}
\]

Choose `S_5=-D_5` to obtain `D_5=0`, or choose
`S_5=-D_5-D_3` to obtain `D_5+D_3=0`.  Both targets have the even parity of
`N_5`, and an elementary use of (6.1) gives

\[
 0\le -D_5,\,-D_5-D_3<q^2\le N_5.
\]

They are therefore attainable sums of `N_5` signs.  This proves

\[
 \boxed{\delta_{5,q}>0,\qquad\delta_{53,q}>0}
\]

for every odd prime power `q`.

## 7. Why the local law survives every leading profile

Every factor degree in the table tends to infinity with `h`, whereas

\[
 \mathcal R_{\le5}=\prod_{\deg R\le5}R
\]

is fixed for fixed `q`.  Character orthogonality and the prime-polynomial
theorem in progressions make the product residue of every fixed profile
uniform in `(F_q[T]/R_(<=5))^times`, with an exponential saving in `h`.
The distinctness correction for repeated degrees is exponentially smaller
as well.  There are only `O(h)` profiles, so all residue-class and
prime-count errors together are `O_q(q^M h^-4)`.

Consequently `delta_(5,q)` applies to the generic and repeated-minimum
`D_5=0` contributions at the required orders, and `delta_(53,q)` applies to
the single third-order mixed profile.

## 8. Proof ledger and bounded replay

Proved:

- the exact three-channel residual (2.2) and parity obstruction (2.3);
- the exhaustive profile list for every `h>=12`;
- absence of an `M^-1` channel and exact separation through `M^-3`;
- the harmonic compression and the two third-order profile corrections;
- the finite local laws (5.2)--(5.3) and positivity of both local constants;
- the fixed-`q` raw detector-zero asymptotic (0.2)--(0.3).

Not claimed:

- the `M^-4` coefficient, where all four-factor channels first interact;
- a limit uniform in both `q` and `h`;
- an individual `L`-function zero, RH, or GRH.

Run:

```text
python -B research/l-families/atlas/function_field/quadratic_family_third_boundary_trace_zero_density.py --check
python -B -O research/l-families/atlas/function_field/quadratic_family_third_boundary_trace_zero_density.py --check
python -B -m unittest tests.test_quadratic_family_third_boundary_trace_zero_density
python -B -O -m unittest tests.test_quadratic_family_third_boundary_trace_zero_density
```

The replay enumerates degree multisets only through `h=60`; it enumerates no
polynomial, irreducible, residue class, field element, curve, point, or zero.
