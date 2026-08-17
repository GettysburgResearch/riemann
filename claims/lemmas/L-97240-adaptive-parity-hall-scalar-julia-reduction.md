# L-97240 - The unique 5:3 scalar is one reciprocal state with a zero-safe Mellin numerator

Claim ID: `L-97240`  
Status: **PROVED EXACT FINITE AND MELLIN ALGEBRA**  
Created: 2026-08-17  
Frozen parent: PR #561 at `db9bdc63c855c6ddf664b763d748f8155a6a2c67`  
RH status: **not assumed**

Put
\[
\mathcal R_X=5c_X(2)+3c_X(3).
\]
Then
\[
\mathcal R_X=\sum_{n\le X}\frac{a_*(n)}{\sqrt n}\log\frac Xn,
\]
where
\[
\boxed{a_*(n)=6\mathbf1_{n=1}-6\mu(n)
 +9\mathbf1_{2\mid n}\mu(n/2)-3\mathbf1_{4\mid n}\mu(n/4).}
\tag{L-97240.1}
\]
Its unsieved dictionary is
\[
q_*(1)=0,\quad q_*(2)=15,\quad q_*(3)=6,\quad q_*(4)=3,
\quad q_*(m)=6\ (m\ge5),
\tag{L-97240.2}
\]
so every nontrivial base coefficient is positive.

Let
\[
b=(\delta_1-\delta_2)*\mu,
\qquad
G(X)=\sum_{n\le X}\frac{b(n)}{\sqrt n}\log\frac Xn.
\]
The exact convolution identity
\[
\boxed{a_*=6\delta_1-3(2\delta_1-\delta_2)*b}
\tag{L-97240.3}
\]
gives
\[
\boxed{\mathcal R_X=6\log X-3\left(2G(X)-2^{-1/2}G(X/2)\right).}
\tag{L-97240.4}
\]

With `z=s+1/2`, termwise Mellin integration in the absolute half-plane gives
\[
\boxed{
\int_1^\infty\mathcal R_X X^{-s-1}\,dX
=\frac6{s^2}-\frac{3(1-2^{-z})(2-2^{-z})}{s^2\zeta(z)}.
}
\tag{L-97240.5}
\]
The finite numerator vanishes only when `2^{-z}=1` or `2^{-z}=2`, impossible
for `Re z>0`.

---

# L-97241 - Adaptive even depth makes the homogeneous parity truncation positive

Claim ID: `L-97241`  
Status: **PROVED EXACT/INEQUALITY THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

Let `0<=r_i<=r_max<1`, put `z=sum_i r_i`, and let `e_k` be the elementary
symmetric sums. For an even integer `L`, define
\[
S_{L-1}=\sum_{k=0}^{L-1}(-1)^ke_k.
\]
The full product is `P=prod_i(1-r_i)>0`. Maclaurin's inequality gives
`e_k<=z^k/k!`, and
\[
P\ge\exp\left(-\frac{z}{1-r_{\max}}\right).
\]
The exponential-tail Chernoff bound gives, for `L>z`,
\[
\sum_{k\ge L}e_k\le\sum_{k\ge L}\frac{z^k}{k!}
\le\left(\frac{ez}{L}\right)^L.
\]
Therefore
\[
\boxed{
L\log\frac{L}{ez}>\frac{z}{1-r_{\max}}
\quad\Longrightarrow\quad S_{L-1}>0.
}
\tag{L-97241.1}
\]
For rough-prime factors `r_i=p_i^{-1/2}`, one has `r_max<=67^{-1/2}`.
The smallest even integer satisfying
\[
L\ge8(z+1)
\tag{L-97241.2}
\]
obeys (L-97241.1). Hence adaptive depth escapes the fixed-depth sign no-go in
the complete homogeneous product model.

This theorem does not remove row-activation walls. Those walls are isolated in
`L-97244`.

---

# L-97242 - Every smooth-interior rough difference is nonnegative

Claim ID: `L-97242`  
Status: **PROVED EXACT CALCULUS THEOREM**  
Created: 2026-08-17  
RH status: **not assumed**

Put
\[
\phi(u)=u e^{u/2}\mathbf1_{u\ge0}.
\]
For every integer `r>=1` and `u>0`,
\[
\boxed{
\phi^{(r)}(u)=e^{u/2}\left(\frac{u}{2^r}+\frac{r}{2^{r-1}}\right)>0.
}
\tag{L-97242.1}
\]
Let `a_i>=0` and assume `u>=a_1+...+a_r`. Then repeated use of the fundamental
theorem of calculus gives
\[
\boxed{
\prod_{i=1}^r(I-T_{a_i})\phi(u)
=\int_0^{a_1}\!\cdots\!\int_0^{a_r}
\phi^{(r)}(u-v_1-\cdots-v_r)\,dv_1\cdots dv_r\ge0.
}
\tag{L-97242.2}
\]
Thus every rough history whose entire translation cube stays inside one active
row cell contributes nonnegatively. Any possible negative contribution is
supported on histories crossing at least one activation boundary.

---

# L-97243 - The 5:3 scalar has an exact parity-covariant positive Julia lift

Claim ID: `L-97243`  
Status: **PROVED EXACT MATRIX THEOREM**  
Created: 2026-08-17  
Inputs: exact scalar dictionary `L-97240`; dyadic Julia state of PR #562  
RH status: **not assumed**

Let
\[
g_2(n)=v_2(n)+1,
\qquad
h_*(n)=6g_2(n)+3\mathbf1_{2\mid n}g_2(n/2),
\]
and define
\[
\mathcal J_*(n)=
\begin{pmatrix}h_*(n)&a_*(n)\\a_*(n)&h_*(n)\end{pmatrix}.
\]
For every odd squarefree core `d>1`, the four nonzero dyadic levels satisfy
\[
\begin{array}{c|rrrr}
n&d&2d&4d&8d\\\hline
|a_*(n)|&6&15&12&3\\
h_*(n)&6&15&24&33.
\end{array}
\]
All other nonunit arithmetic cases have `a_*(n)=0`; the unit core is checked
separately. Hence
\[
\boxed{h_*(n)\ge|a_*(n)|,\qquad \mathcal J_*(n)\succeq0.}
\tag{L-97243.1}
\]

Put `D=diag(1,-1)`. For a rough history `h`,
\[
\boxed{D^{|h|}\mathcal J_*(n)D^{|h|}\succeq0}
\tag{L-97243.2}
\]
and its off-diagonal entry is `(-1)^{|h|}a_*(n)`. Thus cumulative parity is
implemented by positive conjugation rather than erased at terminalization.

---

# L-97244 - Global parity-Hall reduces exactly to one activation-boundary functional

Claim ID: `L-97244`  
Status: **PROVED EXACT REDUCTION; BOUNDARY SIGN OPEN**  
Created: 2026-08-17  
RH status: **unproved**

Fully expand the finite parity-labelled rough source at fixed endpoint `X`.
For each history, separate its translated logarithmic-ramp cube into:

1. the smooth-interior region, where every translated argument is active;
2. the activation-boundary region, where at least one translated argument
   crosses a row knot.

Summing with the exact one-owner coefficients gives
\[
\boxed{\mathcal R_X=\mathcal I_X+\mathcal B_X.}
\tag{L-97244.1}
\]
By `L-97242`,
\[
\boxed{\mathcal I_X\ge0.}
\tag{L-97244.2}
\]
Every source history occurs exactly once in either `I_X` or `B_X`; cumulative
history parity is retained. The unresolved producer is therefore
\[
\boxed{\mathrm{GABPT}:\quad \mathcal B_X\ge-\mathcal I_X
\text{ for all sufficiently large }X.}
\tag{L-97244.3}
\]
Equivalently, `GABPT` is eventual nonnegativity of the single scalar
`mathcal R_X`.

The complete `P_61` annular reserve of PR #556 may enter only as one globally
owned boundary budget. It may not be copied into separate leaves, installed in
canonical orientation after odd histories, or promoted into recursive source
mass.
