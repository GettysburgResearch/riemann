# A projected annular frame for global Pick positivity through order twelve

Status: proposed quantitative theorem, requiring independent review of the
proof and the stated published inputs. RH remains unproved. This file is a
new result; it does not replace the frozen compact packet.

## 1. Statement and inputs

Let `E(z)=xi(1/2+z)`, `F=E'/E`, and `p(t)=F(sqrt(t))/sqrt(t)`.
For positive nodes define

\[
 K(x,y)=\frac{F(x)+F(y)}{x+y}
       =\frac{xp(x^2)+yp(y^2)}{x+y}.
\]

The complete squared-pole source is

\[
 p(t)=\sum_\alpha\frac{w_\alpha}{t+s_\alpha}.
 \tag{1}
\]

A critical pair at ordinate `b`, multiplicity `m`, contributes
`s=b^2,w=2m`. A reflected off-line quartet of depth `a` and height `b`
contributes `s=b^2-a^2 +/- 2iab`, each with weight `2m`. Thus total squared-pole
weight in an ordinate interval is exactly twice the upper-zero multiplicity
count in that interval. All sums here use the complete source and include
multiplicity.

The theorem uses these inputs:

1. The classical critical strip gives `0<=a<=1/2`.
2. The published Platt--Trudgian verification gives every zero through the
   conservative height `H=3*10^12` on the critical line.
3. Trudgian's published argument bound, with the elementary theta remainder
   detailed in section 7, gives, for every `L>=H` and every interval
   `(alpha L,beta L)` inside `[L,2L]` with `beta-alpha=1/128`, more than
   `L log L/2000` upper zeros, with multiplicity.
4. The native theta/Jensen proof in [COARSE_ZERO_COUNT.md](COARSE_ZERO_COUNT.md)
   gives `N_+(T)<=T log T` for `T>=1024`.
5. The classical xi Hadamard source, its locally normal convergence, and the
   standard zero-count/argument identities used below.

**Conditional on these explicit classical and published inputs, every Pick
packet of at most twelve positive nodes is positive semidefinite. It is
positive definite when the nodes are distinct.** All nodes may vary over the
entire positive axis; no bound on their ratios or sizes is imposed.

The new quantitative deduction is not a rerun of either published computation.
The strip improvement from the recent quasi-RH paper is unnecessary for this
order-twelve result. Higher orders and all-order positivity remain open.

## 2. Exact rational moment congruence at arbitrary nodes

Fix `n` distinct positive nodes `x_1,...,x_n`, and put

\[
 q(s)=\prod_{i=1}^n(x_i^2+s),\qquad
 M_j=\sum_\alpha\frac{w_\alpha s_\alpha^j}{q(s_\alpha)}
 \quad(0\le j\le n-1).
 \tag{2}
\]

All these sums converge absolutely: their summands are `O(w/|s|)` at the
largest index, and smaller at the other indices. Conjugation makes them real.
The same definitions may be restricted to an annulus.

Let `a=ceil(n/2), b=floor(n/2)`, and

\[
 H_a^0=(M_{i+j})_{0\le i,j<a},\qquad
 H_b^1=(M_{i+j+1})_{0\le i,j<b}.
\]

For each row `i`, expand

\[
 P_i(z)=\prod_{k\ne i}(x_k+z)
       =E_i(z^2)+z O_i(z^2).
\]

Let `T` have as row `i` the coefficients of `E_i(-s)`, followed by those of
`O_i(-s)`, in ascending powers of `s`. Then exactly

\[
 \boxed{K=T\,\operatorname{diag}(H_a^0,H_b^1)\,T^T.}
 \tag{3}
\]

Indeed, as a polynomial identity in `s`,

\[
 E_i(-s)E_j(-s)+sO_i(-s)O_j(-s)
 =(s+x_ix_j)\prod_{k\ne i,j}(x_k^2+s)
 \tag{4}
\]

when `i!=j`; for `i=j` it equals `prod_{k!=i}(x_k^2+s)`.
For real positive `s`, (4) is the real part of
`P_i(i sqrt(s)) conjugate(P_j(i sqrt(s)))`; its polynomial validity extends
to complex `s`. Multiplying by `w/q(s)` gives the complete source kernel.

The coefficient matrix of the `P_i` is invertible because
`P_i(-x_j)=0` for `j!=i` and `P_i(-x_i)!=0`. Splitting even and odd columns
and changing their signs preserves invertibility. More precisely,

\[
 |\det T|=|\Delta(x)|,
 \qquad \Delta(x)=\prod_{i<j}(x_j-x_i).
\]

Therefore (3) is an exact inertia equivalence. In particular,

\[
 \det K=\Delta(x)^2\det H_a^0\det H_b^1.
 \tag{5}
\]

This reduction is nonconfluent and covers mixed scales directly. No local
matrix-monotonicity implication is imported.

## 3. Uniform annular normalization and quadratic error

It suffices now to take `n=12`, hence both Hankel blocks have size six.
Fix any nodes and any annulus of zero heights `(L,2L]`, with `L>=H`.
Set

\[
 \rho_i=x_i^2/L^2,\quad D=\prod_i(1+\rho_i),\quad
 \phi(v)=\frac D{\prod_i(\rho_i+v)},\quad u=v/4.
\]

For a pole pair, write

\[
 v=\frac{b^2-a^2}{L^2},\qquad
 \delta=\frac{2ab}{L^2},\qquad
 \frac{s}{L^2}=v+i\delta.
\]

Since `a<=1/2`, `L>=1024`, and `L<b<=2L`,

\[
 255/256\le v\le4,\qquad |\delta|\le2/L.
 \tag{6}
\]

Normalize the moments by

\[
 \nu_j=\frac{D L^{2n-2j}}{4^j}M_j
      =\sum_\alpha w_\alpha
        \phi(s_\alpha/L^2)(s_\alpha/(4L^2))^j.
 \tag{7}
\]

Both Hankel blocks in (7) are positive scalar and diagonal congruences of the
blocks in (2). Replace every conjugate pole pair by two copies of its real
projection `v`; call the resulting positive Hankel blocks `P^0,P^1`.

For `0<=j<=11`, define `f_j(z)=phi(z)(z/4)^j`. On a vertical segment through
`v`, logarithmic differentiation gives

\[
 |f_j''(z)|\le
 \frac{|f_j(z)|}{|z|^2}(n+j)(n+j+1).
\]

The three factors used to bound `|f_j(z)|/|z|^2` are each below `17/16`:

\[
 \phi(v)\le(256/255)^{12}<17/16,
\]
\[
 (1+\delta^2/v^2)^{j/2}
 \le(1+1/510^2)^6<17/16,
\]
\[
 1/v^2\le(256/255)^2<17/16.
\]

Here `u<=1`, and the denominators grow in absolute value on the vertical
segment. Since `(17/16)^3<5/4` and
`(n+j)(n+j+1)<4n^2`, we obtain `|f_j''|<5n^2`.
Conjugation cancels the linear term, so Taylor's integral remainder yields

\[
 \boxed{|\Re f_j(v+i\delta)-f_j(v)|<10n^2/L^2.}
 \tag{8}
\]

If `W` is the total annular pole weight, each entry of either normalized
Hankel error has absolute value below `10n^2 W/L^2`. Hence

\[
 \boxed{\|E^k\|_{op}<6\cdot10n^2 W/L^2,\qquad k=0,1.}
 \tag{9}
\]

These bounds are independent of all node scales and their ratios.

## 4. Six separated projected bands and their conditioning

Use the following six height bands, with every endpoint multiplied by `L`:

| j | lower alpha_j | upper beta_j |
|---|---:|---:|
| 1 | 1035/1024 | 1043/1024 |
| 2 | 81/64 | 163/128 |
| 3 | 1513/1024 | 1521/1024 |
| 4 | 851/512 | 855/512 |
| 5 | 117/64 | 235/128 |
| 6 | 2029/1024 | 2037/1024 |

Every width is `1/128`; all bands lie strictly inside `(L,2L)`.
Their projected `u=(b^2-a^2)/(4L^2)` lie in the disjoint rational intervals

\[
 I_j=[\ell_j,h_j],\qquad
 \ell_j=\alpha_j^2/4-2^{-22},\quad h_j=\beta_j^2/4.
 \tag{10}
\]

The subtracted quantity is more than the possible horizontal correction at
`L>=1024`, and is independent of `L`.

For arbitrary points `u_j in I_j`, let `V` have columns
`v(u_j)=(1,u_j,...,u_j^5)^T`. The Lagrange polynomial for column `j` shows

\[
 \operatorname{tr}((VV^T)^{-1})\le\Gamma,
\]

where the explicit rational number is

\[
 \Gamma=\sum_{j=1}^6
 \frac{\prod_{k\ne j}(1+h_k)^2}
 {\prod_{k<j}(\ell_j-h_k)^2
  \prod_{k>j}(\ell_k-h_j)^2}.
 \tag{11}
\]

The coefficient Euclidean norm is bounded by its absolute coefficient sum;
that sum is at most the product in the numerator's square root. Consequently
`lambda_min(VV^T)>=1/Gamma`. The checker evaluates (11) exactly and obtains
`611192582<Gamma<611192583`.

For real projected `v`, each denominator factor satisfies
`(1+rho_i)/(rho_i+v)>=1/4`, so `phi(v)>=4^-n`.
Also `u>=255/1024`. If every band has projected weight at least `W_min`,
then pairing arbitrary probability distributions from the six bands gives

\[
 \boxed{\lambda_{min}(P^k)\ge
 \frac{255}{1024}\frac{4^{-n}W_{min}}\Gamma,
 \qquad k=0,1.}
 \tag{12}
\]

This averaging argument requires separated bands, not separated individual
zeros. Multiplicity is allowed, and neither zero spacing nor critical-line
membership of the annular zeros is assumed.

## 5. Exact domination, all heights, all positive nodes

The source-qualified lower band count gives
`W_min>L log L/1000`. The complete upper count gives
`W<=2N_+(2L)<8L log L`. Therefore `W/W_min<8000`.
Equations (9) and (12) give both normalized Hankel blocks positive definite if

\[
 L^2>
 C:=8000\cdot6\cdot10\cdot12^2\cdot\Gamma\cdot4^{12}
       \frac{1024}{255}.
 \tag{13}
\]

The exact rational checker verifies

\[
 \boxed{C/H^2<1/3,\qquad H=3\cdot10^{12}.}
 \tag{14}
\]

Thus every dyadic annulus `(2^kH,2^{k+1}H]` is positive definite for every
packet of twelve distinct positive nodes, uniformly over `k>=0` and over all
node locations.

All zeros at heights at most `H` are critical and each contributes the
positive rank-two kernel

\[
 2m\frac{b^2+xy}{(x^2+b^2)(y^2+b^2)}.
\]

Adding these kernels and all the annular kernels, with the complete source
convergence, proves the stated global result. An annulus already supplies
strict positivity at twelve distinct nodes. Smaller distinct packets are
principal submatrices after appending nodes. Repeated-node packets are
limits, or coefficient-summing congruences, and are positive semidefinite.

This proves no all-order result. The constants depend on the fixed packet
size. In particular it gives no control as that size tends to infinity.

## 6. Relation to the frozen controls and prior exterior claims

The cofinal sparse countermodels in the frozen packet obey an upper count
and a strip bound, but omit the lower annular zero densities used here.
Their negative global order-four witnesses are therefore compatible with
this theorem. The mechanism of the present result is the positive projected
frame supplied by the actual complete zero count.

PR461's proposed exterior Hankel theorem uses moving ordinate bands and a
quadratic projection error, but addresses local impedance Hankels and a
claimed local-to-global monotonicity passage. The present argument uses an
exact arbitrary-node congruence and uniform rational denominator comparisons;
it closes the mixed-scale Pick gap at a fixed explicit order. It does not
inherit PR461's proposed growing-order constants or a local-to-global theorem.

The annular theorem also explains why finite low-order tests cannot force RH:
a sufficiently high annulus can contain off-line zeros while its fixed-order
projected frame dominates their negative directions.

## 7. Lower band source and endpoint conventions

The published input is Timothy Trudgian, *An improved upper bound for the
argument of the Riemann zeta-function on the critical line II*, J. Number
Theory **134** (2014), 280--292:

\[
 |S(T)|\le .112\log T+.278\log\log T+2.510\qquad(T\ge e).
 \tag{15}
\]

At ordinates away from zeros, `N_+(T)=1+theta(T)/pi+S(T)`.
An elementary Euler--Maclaurin remainder for `z=1/4+iT/2` gives

\[
 \theta(T)=\frac T2\log\frac T{2\pi}-\frac T2-\frac\pi8+\epsilon(T),
 \qquad |\epsilon(T)|<1/T.
 \tag{16}
\]

One derivation starts from the remainder bound
`|R(z)|<=1/(6T)+pi/(12T)` in Stirling's formula; the changes from the
argument and magnitude of `z` to the displayed main term add at most
`1/(8T)+1/(16T)`. With `pi<4` their sum is below `1/T`.
For `T>=H`, `log T>28`, and `log log T<=log T/8`. The latter follows from
`log 28<7/2` and the decreasing derivative of `log u-u/8` for `u>=28`.
The exact coefficient bound

\[
 .112+.278/8+2.510/28+.001<1/4
\]

then gives

\[
 |N_+(T)-\mathcal M(T)|<\tfrac14\log T,
 \quad
 \mathcal M(T)=\frac T{2\pi}\log\frac T{2\pi}
               -\frac T{2\pi}+\frac78.
 \tag{17}
\]

If `beta-alpha=1/128`, with `1<=alpha<beta<=2`, the main increment is
at least `L/(256 pi) log(L/(2pi))`. Since `pi<4`, `log(2pi)<3`, and
`log L>28`, this is greater than
`25 L log L/28672`. The sum of endpoint errors is less than `log L`.
Thus the band count is greater than

\[
 (25L/28672-1)\log L>L\log L/2000
 \qquad(L\ge H).
 \tag{18}
\]

For endpoints that are zero ordinates, first use nonzero endpoints inside the
band and then take one-sided limits. The strict margins in (18) apply to
open bands as well; all masses used in section 4 can be restricted to their
open interiors. No endpoint zero must be counted to obtain the lower bound.
The dyadic upper endpoints may be assigned consistently to the preceding
annulus. The published critical-line verification used in section 1 is
Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to
3*10^12*, Bull. London Math. Soc. **53** (2021), 792--797,
DOI `10.1112/blms.12460`; its verified endpoint exceeds our conservative `H`.

## 8. Replay boundary

[verify_annular.py](verify_annular.py) checks the exact rational frame,
constant inequalities, independent finite arbitrary-node congruences,
Pfaffian identities, and finite controls in normal and optimized Python.
These finite checks do not independently establish the complete Hadamard
source, Trudgian's published argument estimate, or the published verified
height. The analytic annular and summation arguments above are essential.
