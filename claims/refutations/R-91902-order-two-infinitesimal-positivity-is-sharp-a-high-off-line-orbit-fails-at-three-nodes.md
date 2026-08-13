# R-91902 — Order-two infinitesimal positivity is sharp: one high off-line orbit fails at three nodes

Claim ID: `R-91902`  
Status: **EXACT RATIONAL THREE-NODE CONTROL**  
Created: 2026-08-13  
Depends on: `L-91904/L-91905`  
RH status: **unproved**

## 1. A symmetric high-ordinate orbit

Take

\[
 a=\frac25,
 \qquad
 b=14,
 \qquad
 \lambda=a+ib.
\]

Consider the even real entire polynomial

\[
 \Xi_{a,b}(z)
 =(z^2-\lambda^2)(z^2-\overline\lambda^2).
 \tag{R-91902.1}

Its zeros are the off-line quadruple

\[
 \pm a\pm ib.
\]

Put

\[
 F_{a,b}(x)=\frac{\Xi_{a,b}'(x)}{\Xi_{a,b}(x)}
 \qquad(x>1/2).
\]

With

\[
 A=a^2-b^2,
 \qquad B=2ab,
\]

one has

\[
 \boxed{
 F_{a,b}(x)
 =\frac{4x(x^2-A)}{(x^2-A)^2+B^2}.
 }
 \tag{R-91902.2
}

The one- and two-node Carathéodory matrices are positive by the orbitwise
argument of `L-91905`: the ordinate is larger than one.

## 2. Three safe rational nodes

Choose

\[
 x_1=\frac35,
 \qquad
 x_2=8,
 \qquad
 x_3=36.
 \tag{R-91902.3}

Every point lies strictly to the right of `1/2`.  Form

\[
 H_{ij}
 =\frac{F_{a,b}(x_i)+F_{a,b}(x_j)}{x_i+x_j}.
 \tag{R-91902.4}

Direct rational simplification gives

\[
 \boxed{
 H=
 \begin{pmatrix}
 \frac{19620}{965497}
 &\frac{110113180}{7008542723}
 &\frac{8904707640}{2997932873299}\\[2mm]
 \frac{110113180}{7008542723}
 &\frac{1450}{94367}
 &\frac{12280475}{2462318131}\\[2mm]
 \frac{8904707640}{2997932873299}
 &\frac{12280475}{2462318131}
 &\frac{8325}{3105067}
 \end{pmatrix}.
 }
 \tag{R-91902.5}

Its determinant is

\[
 \boxed{
 \det H
 =-\frac{
  201516024836691562500
 }{
  1055839030806150723363641645963
 }<0.
 }
 \tag{R-91902.6}

Thus the three-node kernel is indefinite.

## 3. Meaning

The orbit obeys exactly the two scalar monotonicities behind `L-91905`, so
all order-two tests pass.  Nevertheless its logarithmic derivative has poles
in the right half-plane, and a three-node safe-real packet already detects the
failure.

Therefore

\[
 \boxed{
 \text{order two is the largest universal positivity forced merely by}
 \quad |\Im\lambda|>1,\ |\Re\lambda|<1/2.
 }
 \tag{R-91902.7}

Any unconditional advance to order three must use arithmetic or collective
zero information beyond the elementary orbit geometry.

## 4. Relation to actual zeta

This polynomial is a control, not the zeta Xi function.  It proves that the
new two-node theorem cannot be bootstrapped abstractly to all packets.  The
actual Xi kernel contains the full collection of critical-line and possible
off-line orbits, and the remaining three-and-higher-node sign is genuinely
source specific.

## 5. Exact boundary

```text
high off-line symmetric orbit                    EXACT
all one/two-node tests positive                   EXACT BY L-91905
explicit three-node rational packet               EXACT
three-node determinant                            STRICTLY NEGATIVE
order-two-to-all-orders bootstrap                 REFUTED
actual-Xi order-three positivity                  OPEN
all-order positivity                              OPEN / RH-EQUIVALENT
Riemann Hypothesis                                UNPROVED
```
