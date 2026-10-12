# Composing the complete mixed tail with the final native census

Status: complete actual-source analytic composition, with exact rational
guards. No new root, moment or heat computation is claimed.
Scope: every complete Hausdorff mixed difference at t512 with

                         20*n >= 27*j + 60.

All integer multiplicities and the entire unknown complex and real tail
are included. The universal mixed criterion and RH remain open.
Exact dependencies: the frozen MM1–MM4 theorem
`../../operators/FINITE_CENSUS_MIXED_MOMENT_CONE.md`, SHA
`b904361d5af54885d6cd9bb1cfd730f11fdd05e6a0f2c1557328a92b5a40f166`,
its independently replayed exact receipt
`bffb559967304c3ccb46c6a185d03bed376be5a46dd84394852c68bea39b427f`,
the actual theta/Jensen count theorem `N(x)<=x^2` for x>=1024,
and the final count-free complete real census through7570. That last
input is the V2 source proof SHA
`84dff8dd45a579649bf8c515ef273559147d0b3f4a12a158ce1d7fcad1e9505b`
and full native normal/O receipt
`d6cf40e46dbe0292aff5a48dc5ebec357f378ffed4b2e3aefbfe4d848d517ba3`.
My complete mathematical/source/code and direct native acceptance is frozen
in `SHIFTED_MIXED_SOURCE_REVIEW.md` and `SHIFTED_V2_DIRECT_NATIVE_REVIEW.md`.
This composition neither edits nor replaces those earlier proof bytes.

## CC1. Entire-source comparison with the stronger closed head

Put `A=1/2,t=512,c=t^2-A^2`, and let

\[
 D_{n,j}=\sum_{h=0}^j(-1)^h{j\choose h}c^{n+h}C_{n+h+1}(t)
     =c^n\sum_\rho m_\rho
        \frac{(\rho^2+A^2)^j}{(\rho^2+t^2)^{n+j+1}}.
\tag{CC1}
\]

This is the complete moment sequence, without selected-root subtraction.
The accepted V2 guard gives a complete real head at `R=7570`, including
7343 positive roots. Its simplicity is available but not needed here.
Every remaining source occurrence has real part gamma>R.

As in MM2, `|(rho^2+A^2)/(rho^2+t^2)|<=1`, since
`|rho^2+A^2|<=gamma^2+1/2` and
`|rho^2+t^2|>=gamma^2+c`, with c>=1/2.
For every n>=1, the entire absolute tail after the factor c^n is therefore
bounded by the complete Stieltjes integral

\[
 T_n\le\frac{n+1}{n}Q^{-n}-cQ^{-n-1}<2Q^{-n},
                 \qquad Q=R^2+c.
\tag{CC2}
\]

The negative lower endpoint, the vanishing upper endpoint and all source
multiplicities are accounted for exactly as in the independently reviewed
MM3. This uses the theta/Jensen analytic upper count, not a historical
count or location input. Replacing R only changes the endpoint Q.

The authenticated real occurrence gamma_* in (14,15) belongs to this head.
Set `a=14^2+A^2=785/4`, `B=15^2+t^2=262369`. Its complete contribution
after c^n is strictly greater than `a^j/B^(n+j+1)`. Every other complete
real-head term is nonnegative. Consequently

\[
        2B r^n s^j<1\quad\Longrightarrow\quad D_{n,j}>0,
          \qquad r=B/Q,\quad s=B/a.
\tag{CC3}
\]

Here the exact stronger endpoint is `Q=230268175/4`. This sufficient
criterion can be used directly for any finite n,j; the simpler infinite
cone below is convenient and is not claimed optimal.

## CC2. Exact rational infinite cone

The accompanying finite checker proves the literal rational inequalities

\[
 0<r<1,\quad 2Br^3<1,\quad r^{27}s^{20}<1,
 \quad r^{\lceil27h/20\rceil}s^h\le1\quad(0\le h<20).
\tag{CC4}
\]

Their principal approximate values are `2Br^3=.0496773354` and
`r^27*s^20=.2032352736`. No floating-point predicate is used for acceptance.

Write `j=20q+h`, where0<=h<20. If `20n>=27j+60`, then
`n>=27q+ceil(27h/20)+3`. Since0<r<1,

\[
 2Br^n s^j\le(2Br^3)(r^{27}s^{20})^q
                     r^{\lceil27h/20\rceil}s^h<1.
\tag{CC5}
\]

This proves every mixed sign in the displayed infinite cone, including
arbitrarily high j and n. It does not enumerate or numerically enclose
those individual mixed differences. The whole tail estimate supplies the
infinite argument.

For clarity, each remainder inequality also follows from the strict block:
its twentieth power is at most `(r^27*s^20)^h` because
`20ceil(27h/20)>=27h`. For h>0 this is strictly below one, and h=0 gives
one. The explicit twenty checks independently verify the same finite
integer arithmetic.

## CC3. Execution and remaining scope

The composer authenticates the frozen previous cone receipt and its
direct sources, the final full native V2 receipt and its direct sources,
the known actual real-root interval, and the exact new constants. It
performs only rational guards. It does not rerun a native primitive or
assert that a finite program proves the source's infinite product, strip,
count or real-head theorem. Those already reviewed mathematical inputs
remain explicit imports.

This strictly enlarges the simpler previous cone `40n>=61j+120`, using the
same complete tail proof and a stronger already accepted source census.
It still leaves every unbounded family with n fixed and j tending to
infinity outside its scope. A hypothetical off-real occurrence must
violate some finite mixed test outside the proved cones, by the exact
Hausdorff criterion. No actual violation, universal mixed positivity,
cofinal progress guarantee, complete heat monotonicity or RH is proved.
