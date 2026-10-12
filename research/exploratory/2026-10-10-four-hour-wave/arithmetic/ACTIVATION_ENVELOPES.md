# Prime activation envelopes beyond the label-exclusion bound

Status: **Root-reviewed analytic lemmas P-A1--P-A7; full normal and
optimized all-power certificates passed with byte-identical receipts.
Root source replay and further independent audit are pending.** Literal beta, SHARP and the duplicate labelled 67 are
preserved. Critical power one and RH remain open.

**Proposed theorem A-PA1.** For every real m>=9/7 and x>=1, H_m(x)>0.

The new step prices omitted one-label activation in the exact exclusion-
pair bound (E6), rather than upper-bounding each omitted normalized kernel
by one. It uses a complete convergent prime tail, partitioned into finitely
many bins plus a final entire Euler tail. The finite bins do not replace
or censor that infinite tail.

## 1. An upper kernel for each prime-tail bin

Fix N=10^7, B=N/2, a=(m+1)/2, z=x^-1/2, x>=N. For a label q,

\[
 r_q(m,x)=q^{-a}\frac{(1-3\sqrt q\,z/4)^m}{(1-3z/4)^m}
                 \mathbf1_{q\le x}.
 \tag{P-A1}
\]

Choose edges

\[
 C_0=B,\quad C_1=3N/4,\quad C_2=N,\quad C_3=5N/4,\quad C_4=3N/2.
\]

For q>C_i in its corresponding finite or final infinite bin, if q is
active then its positive numerator is <=(1-3sqrt(C_i)z/4)^m. If q is
inactive its contribution is zero. The representative numerator is
positive throughout x>=N: indeed

\[
 0\le 3\sqrt{C_i}\,z/4\le(3/4)\sqrt{3/2}<15/16<1.
 \tag{P-A2}
\]

Thus the same representative upper bound applies even when C_i>x and
every label in that bin is inactive. This avoids an unjustified smooth
continuation of the native activation kernel; only a positive majorant
is continued there.

Let t_i=sum_(C_i<q<=C_(i+1))q^-a for i=0,...,3, and let
 t_4=sum_(q>C_4)q^-a. All these sums are over ordinary primes. The extra
67 is already among the selected labels <=B. Exact prefix selection gives

\[
 t_4=V(a)-C_{1,0}(a,B)-\sum_{i=0}^3t_i>0.
 \tag{P-A3}
\]

The prime list through C_4 is complete (970704 primes, last 14999981).
The finite bin masses are positive direct sums, and V(a) is the independently
bounded convergent prime-zeta sum with its full Möbius tail (P10). Therefore
(P-A3) prices the entire omitted prime mass. Its directed upper endpoints
and those of the finite bins safely bound their actual positive weights.

## 2. A polynomial upper bound valid close to the activation boundary

For 1<m<2 the expansion

\[
 (1-v)^m=1-mv+\sum_{j=2}^\infty b_j(m)v^j,
\quad b_2=m(m-1)/2,\quad b_{j+1}=b_j(j-m)/(j+1)
 \tag{P-A4}
\]

has positive, decreasing coefficients b_j for j>=2. For any fixed
0<=v<=v_*<1 and integer J>=3, its positive omitted tail obeys

\[
 \sum_{j=J}^\infty b_jv^j\le\frac{b_J}{1-v_*}v^J.
 \tag{P-A5}
\]

This follows termwise from b_j<=b_J for j>=J and the geometric series.
Use v_*=15/16 and J=32. Substitution v=3sqrt(C_i)z/4 gives an upper
polynomial U_i(z) of degree 32. All bin edges and powers are exact rational
inputs and every coefficient enclosure is directed Arb. The bound remains
valid throughout the full required z interval by (P-A2).

Let Q_1(z) be the selected single-label upper polynomial from (W4), and
set

\[
 Q_A(z)=Q_1(z)+\sum_{i=0}^4t_i^+U_i(z),
 \tag{P-A6}
\]

where t_i^+ are directed upper mass endpoints. Then S_1(m,x)<=Q_A(z)/d_m(z),
with the exact normalization denominator d_m=(1-3z/4)^m. There is no
unpriced omitted one-label contribution.

## 3. The uniform power-slab polynomial

On a slab [m0,m1], use Q_A at m0, the global removal upper V(a0)<3,
and selected ordinary/marked lower polynomials P_k,P_k^D at m1, for
k=2,4,6. Monotonicity in m and x is proved in (E9). Write
c_k=1-V(a0)/(k+1)>0. With d_l,d_h the positive lower normalization
polynomials and d_h^+ the upper normalization polynomial, (E6) gives

\[
 \frac{H_m(x)}{T(x)^m}\ge
 1-\frac{Q_A(z)}{d_l(z)}+
 \frac{\sum_{k=2,4,6}[c_kP_k(z)+P_k^D(z)/(k+1)]}{d_h^+(z)}.
\]

Multiplying by the positive d_l d_h^+, then lowering its positive leading
term d_l d_h^+ to d_l d_h, proves that it suffices to certify

\[
 N_A(z)=d_l d_h-Q_A d_h^+
       +d_l\sum_{k=2,4,6}[c_kP_k+P_k^D/(k+1)]>0.
 \tag{P-A7}
\]

This polynomial has degree at most 38. A complete Bernstein proof on the
full interval 0<=z<=N^-1/2 proves all real x>=N in the slab. The cap is
rounded upward to an exact forty-bit dyadic rational, and both children
of every allowed subdivision are retained. Positivity requires every
entire coefficient ball to be strictly positive.

## 4. Complete all-real coverage and controls

The exact power points are

\[
 9/7,1.286,1.2865,1.2872,1.2882,1.2896,1.2916,1.2944,1.2984,1.3.
\]

Nine consecutive slabs cover [9/7,1.3]. On every slab, 21 endpoint
intervals in (S-W2) cover [1,N], using the complete four-level rectangle
bound (S-E2). Selected odd level three is complete there; any omitted
single-label mass is explicitly added as a prime-zeta upper bound. For
each slab the whole tail [N,infinity) is covered by (P-A7). The preceding
A-EP1 packet covers every m>=1.3. Together these imply A-PA1 if every
finite guard passes and the analytic and implementation contracts receive
independent review.

`verify_activation_stitch.py` retains each real rectangle and every
whole-tail Bernstein certificate, and binds source hashes. Normal and
optimized JSON receipts must be byte-identical. `test_activation_tail.py`
checks representative kernel upper polynomials against the literal real
kernel, finite bin masses against independent direct prime sums, their
complete Euler-tail accounting, and invalid kernel/metadata domains.
The marked prefix and exact removal controls remain required inputs from
`test_exclusion_moments.py`.

The final prime tail still converges only for a>1, the removal comparison
still requires V<3, and the exact finite coverage in this theorem is fixed.
No extension to every m>1 follows by extrapolation of the receipt.
