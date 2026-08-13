# L-91904 — The infinitesimal safe Pick kernel is a countable RH criterion

Claim ID: `L-91904`  
Status: **PROPOSED COMPLETE LINEAR RH-EQUIVALENT CRITERION — REVIEW REQUIRED**  
Created: 2026-08-13  
Depends on: standard Carathéodory/Nevanlinna--Pick interpolation; the canonical product for Xi  
RH status: **unproved**

## 1. Centered logarithmic derivative

Put

\[
 \Xi(z)=\xi\left(\frac12+z\right),
 \qquad
 F(z)=\frac{\Xi'(z)}{\Xi(z)}
 =\frac{\xi'}{\xi}\left(\frac12+z\right).
 \tag{L-91904.1}

For a positive rational `q`, define the safe value

\[
 \boxed{
 L(q)=F\left(\frac12+q\right)
 =\frac{\xi'}{\xi}(1+q).
 }
 \tag{L-91904.2}

Every value lies in the absolute Euler half-plane and is real.

For a finite positive rational tuple `q_1,...,q_N`, put

\[
 \boxed{
 \mathcal H[\mathbf q]_{ij}
 =\frac{L(q_i)+L(q_j)}{1+q_i+q_j}.
 }
 \tag{L-91904.3}

This is the safe restriction of the right-half-plane Carathéodory kernel

\[
 \frac{F(z)+\overline{F(w)}}{z+\overline w}.
 \]

## 2. RH implies positivity

Assume RH.  The even canonical product has the form

\[
 \Xi(z)=\Xi(0)
 \prod_{\gamma>0}
 \left(1+\frac{z^2}{\gamma^2}\right)^{m_\gamma},
 \tag{L-91904.4}

with locally uniform logarithmic derivative

\[
 \boxed{
 F(z)=
 \sum_{\gamma>0}m_\gamma
 \left(
  \frac1{z-i\gamma}
  +\frac1{z+i\gamma}
 \right).
 }
 \tag{L-91904.5}

For `Re z>0`, every summand has positive real part.  Hence `F` is a
positive-real function on the right half-plane and

\[
 \boxed{
 \frac{F(z)+\overline{F(w)}}{z+\overline w}
 \succeq0.
 }
 \tag{L-91904.6}

In particular every matrix (L-91904.3) is positive.

## 3. Safe positivity implies RH

Assume (L-91904.3) is positive for every finite positive rational tuple.
The Carathéodory interpolation theorem, applied along an exhaustion of the
countable rational set, gives a positive-real analytic function

\[
 G:\{\Re z>0\}\longrightarrow\{\Re w\ge0\}
\]

such that

\[
 G\left(\frac12+q\right)=L(q)
 \qquad(q\in\mathbb Q_{>0}).
 \tag{L-91904.7}

The meromorphic function `F` is analytic in `Re z>1/2`, since Xi has no zero
there by the classical zero-free half-plane `Re s>1`.  The rational set in
(L-91904.7) has accumulation points inside that overlap, so the identity
theorem gives

\[
 G=F
 \qquad(\Re z>1/2).
\]

Thus `G` is an analytic continuation of `F` to the whole right half-plane.
An off-line zero of Xi in `Re z>0` would give a pole of `F`, impossible for
`G`.  Functional-equation symmetry then gives RH.

Consequently

\[
 \boxed{
 \mathrm{RH}
 \quad\Longleftrightarrow\quad
 \mathcal H[\mathbf q]\succeq0
 \text{ for every finite positive rational tuple.}
 }
 \tag{L-91904.8}

False RH has a finite rational negative-matrix witness by finite
Carathéodory interpolation.

## 4. Infinitesimal relation to the finite-displacement Pick flow

For `P_u=C_u-D_uC_uD_u` from `L-91901`,

\[
 D_0=I,
 \qquad
 C_0=(1+q_i+q_j)^{-1}.
\]

The Cauchy-metric derivative cancels at first order, and `L-91902.17` gives

\[
 \boxed{
 P_0'
 =\left(
  \frac{L(q_i)+L(q_j)}{1+q_i+q_j}
 \right)_{i,j}
 =\mathcal H[\mathbf q].
 }
 \tag{L-91904.9
}

Thus the entire countable finite-displacement criterion has an already
conclusion-producing **linear infinitesimal shadow**.

This does not prove that shadow positive.  It removes the nonlinear quotient
and the horizontal flow from the statement of the remaining arithmetic sign.

## 5. Safe explicit formula

Every entry uses

\[
 \boxed{
 \begin{aligned}
 L(q)={}&
 \frac1{1+q}+\frac1q
 -\frac12\log\pi
 +\frac12\psi\left(\frac{1+q}{2}\right)\\
 &-\sum_{n\ge2}\Lambda(n)n^{-1-q}.
 \end{aligned}
 }
 \tag{L-91904.10
}

The series is absolutely convergent.  Therefore the criterion is a linear
completed gamma/pole reserve versus one prime-power sampling kernel, entirely
on the safe real axis.

## 6. Significance and firewall

This is formally much smaller than CSG:

```text
one logarithmic derivative;
one Cauchy denominator;
linear dependence on the completed prime/gamma data;
no exponentiation;
no moving-metric connection;
no finite horizontal displacement.
```

But it remains RH-equivalent.  Positive scalar values `L(q)>0`, complete
monotonicity of a related one-Green ratio, or positivity of the diagonal do
not imply (L-91904.3).  The complete polarized Cauchy kernel is essential.

## 7. Exact boundary

```text
RH -> centered log derivative positive real         EXACT
safe Caratheodory matrix criterion                   PROPOSED COMPLETE
infinitesimal identity P'_0=H                        EXACT
all entries safely Eulerian                          EXACT
unconditional positivity of H                        OPEN / RH-EQUIVALENT
Riemann Hypothesis                                   UNPROVED
```
