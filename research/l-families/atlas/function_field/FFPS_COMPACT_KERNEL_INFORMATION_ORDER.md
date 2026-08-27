# Every fixed compact BV kernel has an exact beta information order

Status: **universal compact-kernel moment classification, exact reverse bound,
BV Abel forward bound, fixed-kernel RH equivalence, and sufficient moving-kernel
safe factor; no unconditional beta cancellation, converse outside the safe
window, or proof of RH**

Bounded replay:
[ffps_compact_kernel_information_order.py](ffps_compact_kernel_information_order.py).
Canonical summary:
[ffps_compact_kernel_information_order.json](ffps_compact_kernel_information_order.json).

Frozen source: the carrier-ensemble condition firewall at commit
**f49c463be37b264d121aa27677f9b7ae2a2afdac**. The producer pins all
four source blobs and imports no live predecessor module.

## 0. Outcome

The beta, Legendre, tilted, and ensemble packets can all be placed inside one
kernel theorem.

Let \(K\) be a fixed real compactly supported BV kernel that is not equal to
zero almost everywhere, viewed as an \(L^2\) class. Define its information
order

\[
 \boxed{
 r(K)=\min\left\{q\in\mathbb Z_{\ge0}:
 \int_{\mathbb R}t^qK(t)\,dt\ne0\right\},}
\tag{0.1}
\]

and its normalized sensitivity

\[
 \boxed{
 b(K)=\frac{(-1)^{r(K)}}{r(K)!}
 \int_{\mathbb R}t^{r(K)}K(t)\,dt.}
\tag{0.2}
\]

The order is finite. Indeed, if all polynomial moments vanished, polynomial
density on the compact support would force \(K=0\) in \(L^2\).

Let

\[
 \mu_X=\sum_{n\le X}\frac{\beta(n)}{\sqrt n}\delta_{\log n},
 \qquad
 H_{K,X}=K*\mu_X,
 \qquad
 B(X)=\mu_X(\mathbb R).
\tag{0.3}
\]

If the essential-support hull of \(K\) has width \(W\), set
\(L=W+\log X\). Then

\[
 \boxed{
 \|H_{K,X}\|_2^2
 \ge |b(K)|^2\frac{C_r}{L^{2r+1}}|B(X)|^2,}
\tag{0.4}
\]

where

\[
 C_r=(r!)^2(2r+1)\binom{2r}{r}^2.
\tag{0.5}
\]

On the other hand, log-coordinate Abel summation gives

\[
 \boxed{
 \|H_{K,X}\|_2^2
 \le L\bigl(\|K\|_\infty+\operatorname{Var}_{\mathbb R}K\bigr)^2
 \bigl(B^*(X)\bigr)^2,}
\tag{0.6}
\]

where \(K\) is zero-extended and
\(B^*(X)=\sup_{y\le X}|B(y)|\).

The duplicate-67 beta prefix satisfies the frozen RH equivalence. Therefore,
for every such fixed kernel,

\[
 \boxed{
 \mathrm{RH}
 \Longleftrightarrow
 \|H_{K,X}\|_2^2=X^{o(1)}
 \Longleftrightarrow
 \frac{L^{2r+1}}{|b(K)|^2C_r}\|H_{K,X}\|_2^2=X^{o(1)}.}
\tag{0.7}
\]

This does not prove the estimate. It says something structural and useful:
fixed compact detector design cannot change the logical difficulty class. The
kernel selects the first beta-prefix moment it can see; RH supplies the forward
cancellation, and the same moment supplies the reverse implication.

## 1. The universal reverse bound

The carrier-ensemble packet proves the exact compact primitive factorization.
If the first \(r\) moments of \(K\) vanish as in (0.1), its \(r\)-fold primitive

\[
 Q_K(t)
 =\frac1{(r-1)!}\int_{-\infty}^t(t-u)^{r-1}K(u)\,du
\tag{1.1}
\]

is compactly supported on the same hull for \(r\ge1\), with

\[
 D^rQ_K=K,
 \qquad
 \int Q_K=b(K).
\tag{1.2}
\]

For \(r=0\), take \(Q_K=K\). The signed sharp support theorem yields

\[
 \|K\|_2^2\ge |b(K)|^2\frac{C_r}{W^{2r+1}}.
\tag{1.3}
\]

Convolution preserves all vanished moments below \(r\), while

\[
 \int t^rH_{K,X}(t)\,dt
 =(-1)^rr!b(K)B(X).
\tag{1.4}
\]

The field is supported in a hull of length \(L\). Applying the same sharp
Legendre projection to \(H_{K,X}\) proves (0.4). Equivalently, the normalized
energy

\[
 \mathcal R_K(X)
 =\frac{L^{2r+1}}{|b(K)|^2C_r}\|H_{K,X}\|_2^2
\tag{1.5}
\]

always satisfies

\[
 \boxed{\mathcal R_K(X)\ge |B(X)|^2.}
\tag{1.6}
\]

This reverse inequality is arithmetic-source-faithful but contains no
cancellation theorem.

## 2. BV Abel summation

Put \(\ell=\log X\) and let

\[
 A_X(u)=\sum_{\substack{n\le X\\\log n\le u}}
 \frac{\beta(n)}{\sqrt n}.
\tag{2.1}
\]

It vanishes before the first source point, equals \(B(X)\) after \(\ell\), and
satisfies \(\|A_X\|_\infty\le B^*(X)\). With consistent right-continuous
Stieltjes representatives, summation by parts gives, for almost every \(t\)
outside the translated jump and endpoint set,

\[
 H_{K,X}(t)
 =B(X)K(t-\ell)
 -\int_{[0,\ell]}A_X(u)\,d_uK(t-u).
\tag{2.2}
\]

Hence

\[
 |H_{K,X}(t)|
 \le B^*(X)
 \left(\|K\|_\infty+\operatorname{Var}_{\mathbb R}K\right).
\tag{2.3}
\]

The translated field has support length at most \(L\), so integration proves
(0.6).

Under RH, \(B^*(X)=X^{o(1)}\). For fixed \(K\), every kernel constant is fixed
and \(L=O(\log X)\), proving both forward implications in (0.7). Conversely,
either energy condition in (0.7), together with (0.4) and the polylogarithmic
factor, gives \(B(X)=X^{o(1)}\), hence RH.

The BV bound is intentionally robust rather than always sharp. Smooth carriers
can exploit \(L^2\) Young bounds, endpoint localization, or exact Legendre
orthogonality to obtain smaller constants and wider moving-parameter windows.

## 3. Moving kernels and the safe geometric factor

Now let \(K_X\) vary with \(X\). Assume:

- each \(K_X\) is a nonzero real compact BV kernel;
- the information order is one fixed integer \(r\);
- \(b_X=b(K_X)\ne0\);
- the support width is \(W_X\), with \(L_X=W_X+\log X\).

Define

\[
 M_X=\|K_X\|_\infty+\operatorname{Var}_{\mathbb R}K_X
\tag{3.1}
\]

and the dimensionless geometric factor

\[
 \boxed{
 \mathcal G_X
 =\frac{L_X^{2r+2}M_X^2}{|b_X|^2C_r}.}
\tag{3.2}
\]

The reverse theorem remains exact:

\[
 \mathcal R_{K_X}(X)
 =\frac{L_X^{2r+1}}{|b_X|^2C_r}\|K_X*\mu_X\|_2^2
 \ge |B(X)|^2.
\tag{3.3}
\]

Under RH, the BV bound gives

\[
 \mathcal R_{K_X}(X)
 \le \mathcal G_X\bigl(B^*(X)\bigr)^2.
\tag{3.4}
\]

Therefore

\[
 \boxed{
 \mathcal G_X=X^{o(1)}
 \quad\Longrightarrow\quad
 \left[
 \mathrm{RH}
 \Longleftrightarrow
 \mathcal R_{K_X}(X)=X^{o(1)}
 \right].}
\tag{3.5}
\]

This is sufficient, not necessary. Failure of the geometric window does not
prove that a particular arithmetic kernel family fails; it only says that the
universal BV-forward argument no longer certifies it.

The factor also exposes two common fake improvements:

1. letting \(b_X\) tend to zero hides the beta prefix and explodes the reverse
   normalization;
2. making the carrier sharply concentrated can shrink formal support while
   increasing \(M_X\) by the reciprocal Sobolev scale.

Both must be charged before claiming a detector gain.

## 4. Translation, amplitude, and dilation laws

Translation does not change information order or sensitivity. If
\(K_a(t)=K(t-a)\), the binomial expansion shows

\[
 r(K_a)=r(K),
 \qquad
 b(K_a)=b(K).
\tag{4.1}
\]

The support width, supremum, and variation are also unchanged. Thus the
normalized theorem is translation invariant.

Multiplying \(K\) by a nonzero scalar \(c\) sends
\(b\mapsto cb\), \(M\mapsto|c|M\), and energy to \(c^2\) times energy.
Both \(\mathcal R\) and \(\mathcal G\) are invariant. Pure amplitude dilution
cannot fake a result.

The sensitivity-preserving dilation at information order \(r\) is

\[
 \boxed{
 K_S(t)=S^{-r-1}K(t/S).}
\tag{4.2}
\]

It is supported on a width \(SW\), has the same \(r\) and \(b\), and obeys

\[
 M(K_S)=S^{-r-1}M(K).
\tag{4.3}
\]

Consequently

\[
 \boxed{
 \mathcal G_{K_S,X}
 =\left(\frac{L_X}{S}\right)^{2r+2}
 \frac{M(K)^2}{|b(K)|^2C_r}.}
\tag{4.4}
\]

The universal BV safe exponent is \(2r+2\). For the derivative beta carriers,
this recovers the same support power that appears in the simple forward window
of the higher-derivative hierarchy. More refined \(L^2\) arguments can improve
secondary factors but cannot remove the reverse exponent \(2r+1\).

## 5. Exact polynomial certificates

The producer uses four kernels on \([0,1]\).

| kernel | coefficients | \(r\) | \(b\) |
|---|---:|---:|---:|
| low pass | \(1\) | \(0\) | \(1\) |
| linear bandpass | \(1-2t\) | \(1\) | \(1/6\) |
| optimal rung one | \(6-12t\) | \(1\) | \(1\) |
| optimal rung two | \(60-360t+360t^2\) | \(2\) | \(1\) |

For a polynomial \(K(t)=\sum c_dt^d\) on \([0,S]\), the replay uses the exact
safe envelope

\[
 \|K\|_\infty+\operatorname{Var}_{\mathbb R}K
 \le
 \sum_d|c_d|S^d
 +|c_0|
 +\left|\sum_dc_dS^d\right|
 +\sum_{d\ge1}|c_d|S^d.
\tag{5.1}
\]

This avoids root searches and quadrature. It is a certified upper bound, not
an asserted exact BV norm.

For \(K(t)=1-2t\), translation by three gives \(7-2t\) on \([3,4]\). Exact
moments verify that \(r=1,b=1/6\) are unchanged. The dilation by five gives

\[
 K_5(t)=\frac1{25}-\frac{2t}{125},
 \qquad 0\le t\le5,
\tag{5.2}
\]

again with \(r=1,b=1/6\).

For the optimal first-rung detector, the exact zero-extended variation is

\[
 \operatorname{Var}_{\mathbb R}(6-12t)=24.
\tag{5.3}
\]

The coefficient envelope is larger, as expected; it is used only to certify
the universal moving-kernel bound.

## 6. Interpretation

Information order is not a new zero detector and not an invariant of an
\(L\)-function. It is the lowest polynomial moment through which a compact
kernel can see the beta prefix.

Two kernels with different shapes but the same \(r\) and nonzero \(b\) have
the same reverse power \(L^{2r+1}\). Their practical difference lies in the
forward geometry \(M/|b|\) and in any source-specific Fourier cancellation
that the universal theorem deliberately ignores.

This classification gives future agents a quick test:

1. compute \(r\) and \(b\);
2. charge the exact reverse normalization;
3. compute or bound \(M\);
4. verify \(\mathcal G_X=X^{o(1)}\) before allowing the kernel to move;
5. only then investigate arithmetic cancellation beyond the BV baseline.

## 7. Scope and firewalls

| statement | grade |
|---|---|
| compact information order and primitive factorization | **PROVED** |
| universal moment reverse bound | **PROVED** |
| BV Abel forward bound under RH | **PROVED** |
| every fixed nonzero compact real BV kernel gives an RH-equivalent energy | **PROVED** |
| moving-kernel safe factor (3.2) | **PROVED SUFFICIENT** |
| translation, amplitude, and sensitivity-preserving dilation laws | **PROVED** |
| failure outside the safe geometric window | **NOT PROVED** |
| new unconditional beta cancellation | **NOT PROVED** |
| RH or GRH | **NOT PROVED** |

The fixed-kernel theorem requires compact BV regularity. More singular
distributions, noncompact tails, and kernels depending on \(X\) outside (3.5)
need separate analysis.

The conclusion uses the already established beta-prefix formulation of RH. It
is an exact classification of equivalent observables, not an independent
estimate of the observable.

No external novelty or priority is claimed.

## 8. Bounded replay

The producer:

- verifies the frozen ensemble quartet by full Git blob ID;
- computes information orders, sensitivities, sharp constants, coefficient BV
  envelopes, reverse factors, and moving geometric factors with exact rational
  arithmetic;
- verifies translation and sensitivity-preserving dilation on an exact
  bandpass example;
- checks four polynomial kernels of degree at most two, below the declared
  degree-four cap;
- performs no beta sum, prime enumeration, zeta evaluation, root search,
  random sampling, quadrature, or curve computation.

~~~text
python -B research/l-families/atlas/function_field/ffps_compact_kernel_information_order.py --check
python -O -B research/l-families/atlas/function_field/ffps_compact_kernel_information_order.py --check
python -B -m unittest tests.test_ffps_compact_kernel_information_order
python -O -B -m unittest tests.test_ffps_compact_kernel_information_order
python -m ruff check research/l-families/atlas/function_field/ffps_compact_kernel_information_order.py tests/test_ffps_compact_kernel_information_order.py
python -m ruff format --check research/l-families/atlas/function_field/ffps_compact_kernel_information_order.py tests/test_ffps_compact_kernel_information_order.py
~~~
