# Keeping the positive quartet squares improves the height power

Status: proposed exact identity and conditional compact-node theorem.

Use the complete source and selected critical anchors in
[DENOMINATOR_FRAME.md](DENOMINATOR_FRAME.md). This note replaces the
absolute signed-shadow estimate by an exact decomposition of each quartet
into positive and negative rank-one kernels. It is particularly useful when
the first possible off-line height H is large.

## Exact quartet identity

For one quartet set `c=b^2-a^2>0`, `h=4a^2b^2`,
`Q(x)=(x^2+c)^2+h`, `f_k(x)=x^k/Q(x)`, and write `f tensor f` for the
rank-one kernel `f(x)f(y)`. Its contribution to K is exactly

\[
\begin{split}
K_{a,b,m}=4m\{&c(c^2+h)(f_0+f_2/c)\otimes(f_0+f_2/c)\\
             &+(f_3+cf_1)\otimes(f_3+cf_1)\\
             &-h f_1\otimes f_1-(h/c)f_2\otimes f_2\}.             \tag{N1}
\end{split}
\]

This follows by multiplying by Q(x)Q(y). In the even polynomial basis
`1,x^2`, the coefficient block divided by 4m is
`[[c(c^2+h),c^2+h],[c^2+h,c]]`. In the odd basis `x,x^3`, it is
`[[c^2-h,c],[c,1]]`. Completing the two squares gives (N1).

All terms and all signs refer to the exact actual quartet. The positive
squares are retained in the full kernel; they are not estimated as an error.

## Derivative bounds for the two negative features

The factorization of Q has its four roots `+/-a+/-ib`. At every real x,
the absolute value of each root denominator is at least b. Leibniz gives

\[
\frac{|(1/Q)^{(k)}(x)|}{k!}
\le\binom{k+3}{3}b^{-k-4}.                          \tag{N2}
\]

There are exactly `binom(k+3,3)` weak compositions of k among the four
reciprocal factors, and each normalized derivative has the asserted bound.

Write `U=X/S`, `beta=S/H`, `C_k=binom(k+3,3)`, and give terms with negative
indices value zero. Define for k>=0

\[
v_k=U C_k\beta^k+\mathbf1_{k\ge1}C_{k-1}\beta^{k-1},
\]

\[
w_k=U^2 C_k\beta^k
    +2U\mathbf1_{k\ge1}C_{k-1}\beta^{k-1}
    +\mathbf1_{k\ge2}C_{k-2}\beta^{k-2}.              \tag{N3}
\]

The product rule applied to `f_1(Su)=Su/Q(Su)` and
`f_2(Su)=S^2u^2/Q(Su)` gives, on `[0,U]`,

\[
|\partial_u^k f_1(Su)|/k!\le S b^{-4}v_k,\qquad
|\partial_u^k f_2(Su)|/k!\le S^2b^{-4}w_k.            \tag{N4}
\]

Let `d_i=D_+^(i)(U)/i!` be the same nonnegative upper polynomial derivative
bounds as before, and set

\[
V=\sum_{i=0}^{n-1}\left(\sum_{k=0}^i d_{i-k}v_k\right)^2,
\qquad
W=\sum_{i=0}^{n-1}\left(\sum_{k=0}^i d_{i-k}w_k\right)^2.            \tag{N5}
\]

Under the denominator-weighted Newton congruence, the two negative feature
vectors in (N1) have squared norms at most `S^2 V/b^8` and `S^4 W/b^8`.
This follows from normalized Leibniz and the divided-difference integral
formula, exactly as in (D8), now for a single feature rather than a kernel.

## Improved compact theorem

Put `S_j=sum_off m/b^j` and `zeta=1-A^2/H^2>0`. Since h=4a^2b^2 and
`c=b^2-a^2>=zeta b^2`, the complete negative kernel from (N1) has operator
norm after congruence at most

\[
\eta_-:=16A^2\left(S^2 V S_6+\frac{S^4 W S_8}{\zeta}\right).       \tag{N6}
\]

The positive quartet squares and every unused critical atom remain PSD.
The anchor lower bound (D6) therefore proves:

**Theorem N.** If

\[
\boxed{\eta_-<\frac2{S^2\tau J},}                   \tag{N7}
\]

every packet of size at most n with nodes `0<x_i<=X` is PSD, and packets
with distinct nodes are PD.

For the source-qualified all-height bound `N_+(T)<=T log T`, partial
summation gives for every real j>1

\[
S_j\le\frac{j((j-1)\log H+1)}{(j-1)^2H^{j-1}}.       \tag{N8}
\]

At H=3*10^12, the exact elementary enclosure `log H<63/2` gives

\[
S_6<\frac{951}{25H^5},\qquad S_8<\frac{1772}{49H^7}.                 \tag{N9}
\]

Thus the leading negative tail costs `H^-5`, compared with the `H^-3`
absolute shadow-error bound. Both are complete-tail theorems; neither uses
a local zero census as a global substitute.

The sums of the positive squares converge on every compact real interval:
the first has size `O(m/b^2)`, the second `O(mX^2/b^4)`. The negative
squares have the stronger (N6) bound. The all-height count supplies the
necessary summability. Hence the splitting passes to the complete source.

## Scientific boundary

This result proves only the declared finite-order inequality. At any fixed
H, increasing n or X can eventually invalidate the sufficient estimate.
The exact one-reserve countermodel in PROOF.md, and the separate five-node
obstruction for a finite critical background, explain why a strip theorem
does not automatically give all-order positivity. The quasi-RH strip bound
reduces A in (N6), while the new improvement in the height power comes from
the explicit quartet square decomposition.

## A second completion moves the negative features to degrees two and three

If `c^2>h`, complete the original odd coefficient block about its first
diagonal rather than its second. The exact quartet formula becomes

\[
\begin{split}
K_{a,b,m}=4m\{&c(c^2+h)(f_0+f_2/c)\otimes(f_0+f_2/c)\\
 &+(c^2-h)(f_1+c f_3/(c^2-h))\otimes(f_1+c f_3/(c^2-h))\\
 &-(h/c)f_2\otimes f_2-[h/(c^2-h)]f_3\otimes f_3\}.               \tag{N10}
\end{split}
\]

In particular, the degree-one negative feature can be eliminated using an
actual positive square of the *same quartet*. No independent critical
reserve is spent in this operation. The remaining negative features have
degrees two and three.

For p=2,3 define, with beta=S/H,

\[
\ell_{p,k}=\sum_{j=0}^{\min(p,k)}
 {p\choose j}U^{p-j}{k-j+3\choose3}\beta^{k-j},\qquad
W_p=\sum_{i=0}^{n-1}\left(\sum_{k=0}^i d_{i-k}\ell_{p,k}\right)^2.  \tag{N11}
\]

Normalized Leibniz and (N2) bound the transformed feature vector f_p by
`S^(2p) W_p/b^8` in squared norm. Put
`zeta_c=1-A^2/H^2`, `zeta_o=1-6A^2/H^2`, and require `zeta_o>0`.
Since `c>=zeta_c b^2` and
`c^2-h=b^4-6a^2b^2+a^4>=zeta_o b^4`, (N10) bounds the complete
transformed negative kernel by

\[
\eta_{2,3}=16A^2\left(
       \frac{S^4W_2S_8}{\zeta_c}
      +\frac{S^6W_3S_{10}}{\zeta_o}\right).            \tag{N12}
\]

**Theorem N2,3.** Replacing eta_- in (N7) by eta_(2,3) proves the same
finite-order compact positivity conclusion. This leading negative tail
is `H^-7` rather than `H^-5` or the absolute-error `H^-3`.

At the declared height, the exact logarithm enclosure gives

\[
S_{10}<\frac{2845}{81H^9}.                            \tag{N13}
\]

The convergence argument is unchanged. Each term in (N10) is an actual
square with a specified positive or negative coefficient; keeping the
positive parts can only improve the lower bound.

The recompletion has an intrinsic limitation: each quartet still has two
negative directions. Changing its Gram basis cannot make the entire
quartet PSD. The compact anchor theorem must still dominate those
directions, and its declared finite-order inequality remains indispensable.
