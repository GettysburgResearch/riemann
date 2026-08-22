# L-102725 — Two activation-zero SHARP rays survive the signed compact filter

Claim ID: `L-102725`  
Status: **PROVED EXACT KERNEL THEOREM**  
Created: 2026-08-22  
Depends on: PR #690 active shifted quadratics; PR #719 `P_2` filter  
RH status: **not assumed**

Put

\[
 P_2=(I-\sqrt2S_2)(I-S_2)^2
 =I-(2+\sqrt2)S_2+(1+2\sqrt2)S_4-\sqrt2S_8.
\]

For a real shift `z`, let

\[
 W_z(y)=|4\sqrt y-3+z|^2\mathbf1_{y\ge1},
 \qquad K_z=P_2W_z.
\]

Two special shifts are retained:

\[
 z_1=-1,\qquad z_2=-\frac12.
\]

They both belong to the exact SHARP disk of PR #690.

## 1. The activation-zero ray `z=-1`

Writing `x=sqrt(y)`, direct expansion gives

\[
K_{-1}(y)=
\begin{cases}
16(x-1)^2,&1\le y<2,\\
-8\sqrt2x^2+32\sqrt2x-16\sqrt2-16,&2\le y<4,\\
4x^2-16x+16\sqrt2,&4\le y<8,\\
2(2-\sqrt2)x^2,&y\ge8,\\
0,&0<y<1.
\end{cases}
\tag{L-102725.1}
\]

Every piece is nonnegative and every interior point `y>1` is strictly
positive.  The derivative signs on the four cells are respectively

\[
32(x-1),\quad16\sqrt2(2-x),\quad8(x-2),
\quad4(2-\sqrt2)x,
\]

so the endpoint checks prove the assertion without a numerical scan.

There is also a positive B-spline representation.  In logarithmic coordinate
`u=log y`,

\[
P_2=(1-e^{-h(D-1/2)})(1-e^{-hD})^2,
\qquad h=\log2,
\]

and

\[
(D-\tfrac12)D^2W_{-1}=8e^u\mathbf1_{u\ge0}+8\delta_0.
\]

Hence `K_-1` is the convolution of a positive measure with a positive
three-box exponential spline.

## 2. The second ray `z=-1/2`

The same calculation gives

\[
K_{-1/2}(y)=
\begin{cases}
(8x-7)^2/4,&1\le y<2,\\
-[32\sqrt2x^2-112\sqrt2x+49(1+\sqrt2)]/4,&2\le y<4,\\
[16x^2-56x+49\sqrt2]/4,&4\le y<8,\\
2(2-\sqrt2)x^2,&y\ge8,\\
0,&0<y<1.
\end{cases}
\tag{L-102725.2}
\]

The first and fourth pieces are immediate.  On `[sqrt(2),2]` the second
piece has its maximum at `x=7/4`, so its minima are the endpoints

\[
\frac{175-113\sqrt2}{4}>0,
\qquad
\frac{-49+47\sqrt2}{4}>0.
\]

On `[2,2sqrt(2)]` the third piece is increasing and begins at

\[
-12+\frac{49\sqrt2}{4}>0.
\]

Thus

\[
\boxed{K_{-1}(y)\ge0,\qquad K_{-1/2}(y)>0\quad(y\ge1).}
\tag{L-102725.3}
\]

## 3. Uniform boundary scaling

Put

\[
 c_\infty=2(2-\sqrt2).
\]

For `y>=8`, both kernels equal `c_infty y`.  Direct cell calculus gives

\[
0\le K_{-1}(y)\le\frac53c_\infty y,
\]

\[
0<K_{-1/2}(y)\le2c_\infty y
\qquad(y\ge1).
\tag{L-102725.4}
\]

The constants are deliberately rounded upward.  The exact suprema are
`4(sqrt(2)-1)` for the first ray and less than `1.986` for the second.

These two kernels are special members of the SHARP quadratic family.  The
general signed filter remains non-cone-preserving; no full-disk assertion is
made.