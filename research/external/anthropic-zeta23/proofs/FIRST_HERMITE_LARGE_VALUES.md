# First-Hermite prime large values and simultaneous almost-everywhere positivity

**Status:** `PROPOSED COMPLETE UNCONDITIONAL LARGE-VALUE THEOREM — INDEPENDENT ANALYTIC REVIEW REQUIRED`  
**RH status:** **unproved**  
**Base:** PR #385 at `ea2d7c26c1fd3a58c3e31609cb2411ea0c0fd20a`  
**Dependencies:** PR #379's exact first-Hermite explicit-formula scalar; the Chebyshev–Mertens estimate
\[
\sum_{n\le e^U}\frac{\Lambda(n)^2}{n}
=\frac{U^2}{2}+O(U);
\]
Montgomery–Vaughan mean value/Hilbert inequality; elementary Bernstein moments for independent bounded random variables.

## 1. Purpose

PR #385 proves the first-Hermite scalar positive pointwise in the phase-blind wedge

\[
q\le (4-\varepsilon)\log\log(2+|x|).
\]

The first unresolved scale is therefore the signed prime-power polynomial near

\[
\log n\asymp q,\qquad
n\asymp e^q.
\]

This note attacks that signed polynomial by large-value methods rather than by absolute values.

The outcome is much stronger than the pointwise phase-blind wedge, but deliberately not a proof of RH:

> for every fixed \(\varepsilon>0\), outside a set of exponentially small relative measure in every dyadic height block, the first-Hermite scalar is simultaneously positive at **every integer heat resolution**
> \[
> 1\le q\le(\log X)^{1-\varepsilon}.
> \]

Thus any hypothetical high-ordinate negative witness is an extreme large value of a very short Gaussian von Mangoldt polynomial. The remaining obstruction is genuinely pointwise: a single exceptional carrier is not eliminated by an average theorem.

## 2. The prime polynomial

For \(q\ge1\), define

\[
h_q(u)
=
\left(1-\frac{u^2}{2q}\right)e^{-u^2/(4q)}
\tag{LV.1}
\]

and

\[
b_q(n)
=
\frac{\Lambda(n)}{\sqrt n}\,h_q(\log n).
\tag{LV.2}
\]

Put

\[
S_q(x)
=
\sum_{n\ge2}b_q(n)n^{ix}.
\tag{LV.3}
\]

The prime channel in the exact scalar of PR #379 is

\[
\mathcal P(q,x)
=
\frac{1}{2\sqrt\pi\,q^{3/2}}\Re S_q(x).
\tag{LV.4}
\]

Write the complete scalar as

\[
\mathcal M(q,x)
=
\mathcal P_{\rm pole}(q,x)
+\mathcal G(q,x)
-\mathcal P(q,x),
\tag{LV.5}
\]

where \(\mathcal G\) is the archimedean gamma contribution.

Let

\[
I_X=[X,2X],\qquad L=\log X.
\]

Stirling, restricted to \(|t-x|\le q^{-1/2}\), gives absolute constants \(c_0,C_0>0\) such that, uniformly for \(x\in I_X\), \(q\ge1\), and large \(X\),

\[
\mathcal G(q,x)
\ge
\frac{c_0L-C_0}{q^{3/2}}.
\tag{LV.6}
\]

The pole term satisfies

\[
|\mathcal P_{\rm pole}(q,x)|
\ll
(1+x^2)e^{-q(x^2-1/4)}.
\tag{LV.7}
\]

Consequently there are absolute \(c_1>0\) and \(X_0\) such that

\[
\boxed{
x\in I_X,\quad
\mathcal M(q,x)<0
\quad\Longrightarrow\quad
|S_q(x)|\ge c_1L
}
\tag{LV.8}
\]

for every \(X\ge X_0\) and every \(q\ge1\).

The striking feature is that the threshold on the unnormalised Dirichlet polynomial is \(c_1\log X\), independent of \(q\).

## 3. Exact coefficient-energy scale

Put

\[
V(q)
=
\sum_{n\ge2}|b_q(n)|^2.
\tag{LV.9}
\]

Let

\[
A(U)
=
\sum_{\log n\le U}\frac{\Lambda(n)^2}{n}
=
\frac{U^2}{2}+O(U).
\tag{LV.10}
\]

Then

\[
V(q)
=
\int_0^\infty
\left(1-\frac{u^2}{2q}\right)^2
e^{-u^2/(2q)}\,dA(u).
\tag{LV.11}
\]

The main term is

\[
\begin{aligned}
\int_0^\infty
\left(1-\frac{u^2}{2q}\right)^2
e^{-u^2/(2q)}u\,du
&=
q\int_0^\infty(1-v)^2e^{-v}\,dv\\
&=q.
\end{aligned}
\tag{LV.12}
\]

Integrating the \(O(u)\) remainder in (LV.10) by parts gives \(O(\sqrt q)\). Therefore

\[
\boxed{
V(q)=q+O(\sqrt q).
}
\tag{LV.13}
\]

So the natural standard deviation of \(S_q\) is only \(\asymp\sqrt q\), while a negative first-Hermite witness requires size \(\gg\log X\).

## 4. Prime-block Bohr lift

For each prime \(p\), define the one-prime block

\[
Y_{p,q}(z)
=
\sum_{r\ge1}b_q(p^r)z^r,
\qquad |z|=1.
\tag{LV.14}
\]

On the infinite prime torus, with independent Haar variables \(\omega_p\),

\[
S_q(\boldsymbol\omega)
=
\sum_pY_{p,q}(\omega_p).
\tag{LV.15}
\]

Each block has mean zero, and orthogonality gives

\[
\sum_p\mathbb E|Y_{p,q}|^2=V(q).
\tag{LV.16}
\]

The scalar function

\[
\left|1-\frac{v^2}{2}\right|e^{-v^2/4}
\]

is bounded on the real line. Hence

\[
\begin{aligned}
\|Y_{p,q}\|_\infty
&\le
C\log p\sum_{r\ge1}p^{-r/2}\\
&=
C\frac{\log p}{\sqrt p-1}
\le B_0
\end{aligned}
\tag{LV.17}
\]

with one absolute \(B_0\), uniformly in \(p\) and \(q\ge1\).

Bernstein's inequality for the real and imaginary parts therefore gives

\[
\mathbb P\{|S_q(\boldsymbol\omega)|\ge t\}
\le
4\exp\left[
-c\min\left(\frac{t^2}{q+1},\frac{t}{B_0}\right)
\right].
\tag{LV.18}
\]

Integrating the tail yields the moment bound

\[
\boxed{
\int_{\mathbb T^\infty}
|S_q(\boldsymbol\omega)|^{2k}\,d\boldsymbol\omega
\le
\bigl[Ck(q+k)\bigr]^k
}
\tag{LV.19}
\]

for every integer \(k\ge1\).

This step uses the prime-power support rather than treating all coefficients as one arbitrary Dirichlet polynomial. Repeated powers of one small prime remain inside one bounded random block.

## 5. Gaussian truncation

Fix \(B=8\) and put

\[
N_q=e^{Bq}.
\tag{LV.20}
\]

Let

\[
S_{q,B}(x)
=
\sum_{2\le n\le N_q}b_q(n)n^{ix}.
\tag{LV.21}
\]

Using \(\Lambda(n)\le\log n\), replacing prime powers by all integers, and then setting \(u=\log t\), one obtains

\[
\begin{aligned}
|S_q(x)-S_{q,B}(x)|
&\le
C\int_{Bq}^\infty
u\left(1+\frac{u^2}{q}\right)
\exp\left(\frac u2-\frac{u^2}{4q}\right)\,du.
\end{aligned}
\tag{LV.22}
\]

The exponent completes the square:

\[
\frac u2-\frac{u^2}{4q}
=
\frac q4-\frac{(u-q)^2}{4q}.
\tag{LV.23}
\]

At \(u=8q\) it equals \(-12q\), and it decreases thereafter. Thus

\[
\boxed{
\sup_x|S_q(x)-S_{q,B}(x)|
\le
Cq^A e^{-12q}
}
\tag{LV.24}
\]

for one absolute \(A\).

In particular, for large \(X\), the implication (LV.8) remains valid with \(S_{q,B}\) in place of \(S_q\), after decreasing \(c_1\).

## 6. Transfer from the prime torus to a height interval

Raise the finite Dirichlet polynomial to the \(k\)-th power:

\[
S_{q,B}(x)^k
=
\sum_{m\le N_q^k}c_{q,k}(m)m^{ix}.
\tag{LV.25}
\]

Unique factorisation identifies its coefficient square with the Bohr moment:

\[
\sum_m|c_{q,k}(m)|^2
=
\int_{\mathbb T^\infty}
|S_{q,B}(\boldsymbol\omega)|^{2k}\,d\boldsymbol\omega.
\tag{LV.26}
\]

Montgomery–Vaughan's mean-value theorem gives, on any interval of length \(X\),

\[
\int_X^{2X}|S_{q,B}(x)|^{2k}\,dx
\le
\bigl(X+CN_q^k\bigr)
\sum_m|c_{q,k}(m)|^2.
\tag{LV.27}
\]

If

\[
Bkq\le\frac12L,
\tag{LV.28}
\]

then \(N_q^k\le X^{1/2}\), and (LV.19) yields

\[
\boxed{
\int_X^{2X}|S_{q,B}(x)|^{2k}\,dx
\le
CX\,[Ck(q+k)]^k.
}
\tag{LV.29}
\]

This is the load-bearing transfer. It is available at growing moment order because the relevant prime polynomial has effective length \(e^{O(q)}\), not height \(X\).

## 7. Large-value theorem

Define the negative set

\[
E_q(X)
=
\{x\in[X,2X]:\mathcal M(q,x)<0\}.
\tag{LV.30}
\]

Combining (LV.8), (LV.24), (LV.29), and Markov's inequality gives:

### Theorem 7.1

There are absolute constants \(B,C,c>0\) such that, for every sufficiently large \(X\), every \(q\ge1\), and every integer \(k\ge1\) satisfying

\[
Bkq\le\frac12\log X,
\]

one has

\[
\boxed{
\frac{|E_q(X)|}{X}
\le
C
\left[
\frac{Ck(q+k)}{(\log X)^2}
\right]^k.
}
\tag{LV.31}
\]

The case \(k=1\) already gives

\[
\boxed{
|E_q(X)|
\ll
X\frac{q+1}{(\log X)^2}
}
\tag{LV.32}
\]

throughout \(q\ll\log X\).

This improves the phase-blind theorem in a different direction: it does not enlarge the pointwise wedge, but it proves that violations outside that wedge are very rare.

## 8. Exponentially sparse exceptional centres

Choose a sufficiently small absolute \(\kappa>0\) and set

\[
k
=
\left\lfloor
\frac{\kappa L}{q+1}
\right\rfloor
\tag{LV.33}
\]

whenever the right side is at least one. Then

\[
Bkq
\le
B\kappa L
\]

and, for \(\kappa\) small enough, (LV.28) holds.

Moreover,

\[
\frac{Ck(q+k)}{L^2}
\le
\frac{C\kappa}{L}
+
\frac{C\kappa^2}{(q+1)^2}
\le\frac12
\tag{LV.34}
\]

for large \(X\). Hence

\[
\boxed{
|E_q(X)|
\le
CX\exp\left[-c\frac{\log X}{q+1}\right].
}
\tag{LV.35}
\]

Now let \(1\le Q\le \kappa\log X\). A union bound over integer heat resolutions gives

\[
\boxed{
\left|
\left\{
x\in[X,2X]:
\exists q\in\mathbb N,\ 1\le q\le Q,\ 
\mathcal M(q,x)<0
\right\}
\right|
\le
CXQ\exp\left[-c\frac{\log X}{Q+1}\right].
}
\tag{LV.36}
\]

In particular, for every fixed \(\varepsilon>0\),

\[
Q=(\log X)^{1-\varepsilon}
\]

gives

\[
\boxed{
\left|
\left\{
x\in[X,2X]:
\min_{1\le q\le(\log X)^{1-\varepsilon}\atop q\in\mathbb N}
\mathcal M(q,x)<0
\right\}
\right|
\le
X\exp[-c_\varepsilon(\log X)^\varepsilon].
}
\tag{LV.37}
\]

Thus the simultaneous positivity range is far larger than the pointwise
\(4\log\log X\) wedge for a density-one set of centres.

## 9. Mean-square constant

The same argument at \(k=1\) gives a useful calibration. From (LV.13) and Montgomery–Vaughan,

\[
\frac1X\int_X^{2X}|S_q(x)|^2\,dx
=
q+O(\sqrt q)
+
O\left(\frac{q^C e^{q/2}}{X}\right).
\tag{LV.38}
\]

The nonconjugate square has the same error scale, so

\[
\frac1X\int_X^{2X}(\Re S_q(x))^2\,dx
=
\frac q2+O(\sqrt q)
+
O\left(\frac{q^C e^{q/2}}{X}\right).
\tag{LV.39}
\]

Therefore

\[
\boxed{
\frac1X\int_X^{2X}|\mathcal P(q,x)|^2\,dx
=
\frac{1}{8\pi q^2}
\left(1+O(q^{-1/2})\right)
+
O\left(\frac{q^C e^{q/2}}{Xq^3}\right).
}
\tag{LV.40}
\]

The pointwise gamma reserve is of size

\[
\frac{\log X}{q^{3/2}}.
\]

Its square exceeds the natural prime variance by the factor

\[
\frac{(\log X)^2}{q}.
\tag{LV.41}
\]

That ratio is the probabilistic source of (LV.31).

## 10. Global density consequence

For fixed \(\varepsilon>0\), let

\[
\mathcal E_\varepsilon
=
\left\{
x\ge e^e:
\exists q\in\mathbb N,\ 
1\le q\le(\log x)^{1-\varepsilon},\
\mathcal M(q,x)<0
\right\}.
\tag{LV.42}
\]

Applying (LV.37) on dyadic blocks gives

\[
|\mathcal E_\varepsilon\cap[1,X]|
=
o(X).
\tag{LV.43}
\]

More strongly,

\[
\boxed{
\int_{\mathcal E_\varepsilon}\frac{dx}{x}<\infty.
}
\tag{LV.44}
\]

Indeed the contribution of the dyadic block
\([2^j,2^{j+1}]\) is at most
\(\exp(-c_\varepsilon j^\varepsilon)\), and these quantities are summable.

This is a large-value theorem about the continuum of possible centres. It does not by itself bound a discrete zero set, because a single exceptional point has measure zero.

## 11. Why this still does not prove RH

The theorem leaves two logically distinct gaps.

### 11.1 A single resonant carrier

The exceptional set in (LV.37) is tiny but nonempty. RH requires positivity at every centre, not almost every centre. A hypothetical terminal off-line zero may sit at one of those rare carriers.

No measure theorem alone can exclude one prescribed point.

### 11.2 Moment/support barrier

The transfer (LV.27) at order \(2k\) requires

\[
kq\ll\log X.
\tag{LV.45}
\]

A terminal pair at depth \(0<y<1/2\) contributes on scale

\[
e^{qy^2}.
\]

Its \(2k\)-th power therefore contributes at most

\[
e^{2kqy^2}
\le
X^{2y^2+o(1)}
=
o(X),
\tag{LV.46}
\]

even at the full moment budget, because \(2y^2<1/2\).

Thus the large-value theorem is consistent with one isolated pair. This is the pair-adapted version of the higher-moment support firewall already visible in Claude's finite-compression method.

## 12. Corrected frontier

Closed here, subject to independent review:

```text
first-Hermite coefficient variance V(q)=q+O(sqrt q)       PROPOSED COMPLETE
uniform bounded one-prime Bohr blocks                      PROPOSED COMPLETE
all-order torus Bernstein moments                          PROPOSED COMPLETE
growing-order MV transfer                                  PROPOSED COMPLETE
large-value bound for negative first-Hermite centres       PROPOSED COMPLETE
simultaneous density-one positivity to q=log^(1-eps) X     PROPOSED COMPLETE
finite logarithmic measure of the global exceptional set   PROPOSED COMPLETE
```

Still open:

```text
pointwise signed prime bound at every carrier
elimination of the exponentially sparse resonance set
full first-Hermite positivity
corrected-kernel arithmetic floor
Riemann Hypothesis
```

The next viable attack must be an **inverse theorem for the exceptional set**: convert a large value
\[
|S_q(x)|\gg\log X
\]
into a rigid simultaneous phase-resonance certificate for the prime blocks, and then rule out that certificate at a zeta-zero carrier. Another average estimate, however strong, cannot finish the route.
