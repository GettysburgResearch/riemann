# Three activation phases at the four-prime native boundary

The leading four-prime distance atlas has a central two-coordinate face
only on its outer-gap wall. The original kernel changes that picture:
near the wall there is an open central-face strip, then a phase with
exactly one inactive endpoint, then an interior phase. This is a
second-order source effect, with the full native kernel retained.

The source is the same squarefree four-prime product, all16 factor
allocations, actual2ds and physical1/sqrt(K) from
HIGHER_NATIVE_CLUSTER_ATLAS.md at
`755b27c2c9747f3db255238c59c2622dee6cad8b`. The cubic kernel remainder
and its finite central-face application are frozen in
SECOND_ORDER_NATIVE_FACE_SELECTION.md at
`2e772b2048a00af9b6d59aa594f2e64ec96a5529`.
No all-family gamma or principal-moment bound is asserted.

## 1. The source family and the three regimes

Fix a,b>0 and let

\[
 A=144+64\sqrt2,\qquad C=\frac{288a(a+b)}A,
 \qquad h_1=C/4,\quad h_2=3C/4.\tag{1}
\]

Take actual primes whose logarithms are

\[
 (\log p_1,\ldots,\log p_4)
 =L1+\epsilon(0,a,a+b,2a+b+\epsilon h)+e,
 \qquad\|e\|_\infty\le M\epsilon^3.\tag{2}
\]

Assume the original cardinality bands are separated. Let q minimize the
complete original observed energy on the activation simplex. Fix a
compact range |h|<=H and exclude a fixed positive neighborhood of
|h|=h1,h2. As epsilon tends to zero, uniformly under those conditions,
write Q=q1+q2. Then Q=1/2+O(epsilon^2), and for h>=0 the regimes are:

| parameter range | exact inactive coordinates | endpoint activation asymptotics |
|---|---|---|
|0<=h<h1|q1=q4=0|q2,q3=1/2+O(epsilon^2)|
|h1<h<h2|q1=0|q4=epsilon(4h-C)/(16a)+O(epsilon^2)|
|h>h2|none|q1=epsilon(4h-3C)/(24a)+O(epsilon^2), q4=epsilon(8h-3C)/(24a)+O(epsilon^2)|

In each row the middle coordinates are positive. In the second row q4
is strictly positive; in the third all four coordinates are strictly
positive. For negative h reflect the endpoints and middle coordinates.
The table excludes equality at either threshold: the next order can
decide a zero slack there, and this packet does not silently assign it.

The unique minimizing field is defined in the original Mellin norm.
A zero activation does not mean removal of source factor allocations
containing that prime. All16 remain in the source coefficient census.

## 2. The exact kernel reduction with a uniform error

Let x_epsilon be the normalized logarithmic shape in (2). Define the
same-cardinality source forms

\[
 H_x(q)=\sum_{|S|=|T|}q(S)q(T)|x(S)-x(T)|,
 \qquad
 J_x(q)=\sum_{|S|=|T|}q(S)q(T)(x(S)-x(T))^2.\tag{3}
\]

The actual kernel has

    Gamma(delta)=Gamma0-A|delta|-36delta^2+R3(delta),
    |R3(delta)|<=30|delta|^3  for |delta|<=log2.

After removing the positive physical scale and the constant band mass,
minimizing the original energy is exactly maximizing

\[
 \Phi_\epsilon(q)=H_{x_\epsilon}(q)
       +\frac{72}{A}\epsilon J_{x_\epsilon}(q)
       +\mathcal R_\epsilon(q),
 \qquad\|\nabla\mathcal R_\epsilon\|_\infty=O(\epsilon^2).
 \tag{4}
\]

The bound follows from the full cubic kernel remainder, not merely a
pointwise asymptotic without derivative control. All forms are quadratic
in q. The explicit bound from the cited source is
`240 C4 T^3 epsilon^2/A`, with C4=20 and T a uniform bound for all
same-cardinality shape differences. The perturbation e/epsilon in (2)
is O(epsilon^2); the native Lipschitz bound contributes another
O(epsilon^2) gradient error. Its constants are uniform for bounded h
and fixed a,b,M. No shrinking support or extra measure is introduced.

Write endpoint variables u0=q1,v0=q4 and Q=q1+q2. In the chamber c>=a,
the exact leading four-prime atlas is

\[
 H=8(a+b+c)+8bQ(1-Q)-8au_0^2+8au_0v_0
              -4(3c-a)v_0^2+4(c-a)v_0.\tag{5}
\]

For c<a its reflected formula applies. At c=a the unique maximizer is
q0=(0,1/2,1/2,0). The native perturbation and c-a=O(epsilon) therefore
give q-q0=O(epsilon) by the fixed strictly concave singleton band.

At q0 with c=a, the Q derivative of J is zero by reflection. Its
endpoint derivatives are both

\[
 \partial_{u_0}J=\partial_{v_0}J=-4a(a+b).\tag{6}
\]

One derivation uses the r=4 second-moment coefficient-4 of X2_q on a
reflection-symmetric perturbation. Moving mass t to both endpoints
increases X2_q by2a(a+b)t, so the combined derivative is-8a(a+b);
reflection gives the two individual derivatives in (6).

Equation (5) has Q derivative-16b(Q-1/2) independent of the endpoints.
Since q-q0 and c-a are O(epsilon), the Q derivative of the correction
in (4) is O(epsilon^2). The exact active Q equation thus gives
Q=1/2+O(epsilon^2). The middle coordinates remain strictly positive.

## 3. The rescaled source quadratic and its complete KKT solution

Put q1=epsilon u,q4=epsilon v. For h>=0, the endpoint terms of (4),
after subtracting constants and dividing by epsilon^2, converge with
uniform gradient error O(epsilon) on bounded u,v to

\[
 \Psi_h(u,v)=-8a(u^2-uv+v^2)-Cu+(4h-C)v,
 \qquad u,v\ge0.\tag{7}
\]

The Hessian has eigenvalues-8a and-24a, so there is one maximizer.
Its derivatives are

    Psi_u=-16a u+8a v-C,
    Psi_v=8a u-16a v+4h-C.

At(0,0), both are negative exactly when h<C/4. On the face u=0,
stationarity gives v=(4h-C)/(16a); the remaining inactive derivative is
`2h-3C/2`, strictly negative exactly when h<3C/4. In the interior,
solving the two equations gives

\[
 u=\frac{4h-3C}{24a},\qquad
 v=\frac{8h-3C}{24a}.\tag{8}
\]

These are both positive for h>3C/4. The three rows in Section1 are
therefore the complete KKT solution, not an optimization restricted to a
reflection-symmetric path. At h<0 the reflected chamber swaps u and v
and replaces h by |h| to this order. The change of the smaller outer gap
from a to a+epsilon h only contributes to the already bounded next-order
error.

## 4. Why the exact finite zero patterns follow

Convergence of a minimizer alone would not prove an exact zero. For
each open regime solve the full original quadratic problem restricted
to the support in the corresponding row of Section1. Its Hessian on
that support is uniformly definite. The gradient residual at the
displayed approximation is O(epsilon^2), so the actual supported solution
differs by O(epsilon^2).

The middle coordinates remain bounded away from zero. Every endpoint
declared positive has mass at least a fixed positive constant times
epsilon when h stays away from the thresholds. Every endpoint declared
inactive has a strictly negative maximization gradient, with margin a
fixed positive constant times epsilon. The O(epsilon^2) remainder cannot
reverse these inequalities. These are the complete original KKT
conditions, so strict convexity of the original Gram energy proves the
unique full-simplex minimizer and its exact zero pattern.

This argument is uniform on compact h ranges a positive distance from
the thresholds. It does not claim a uniform conclusion while h approaches
a threshold at an epsilon-dependent rate. It also does not assign the
exact equality cases by continuity.

## 5. Actual source realization and cofinal primes

For each fixed small epsilon and h, ordinary PNT supplies primes in four
fixed relative intervals about the logarithmic targets in (2), with
logarithmic widths at most min(M,1)epsilon^3. Choose the common horizon
large after fixing epsilon and impose cardinality separation. A diagonal
sequence proves cofinal actual prime families in each open regime,
without a uniform shrinking-interval prime theorem.

Every resulting activation is realized by a single monotone source path.
Activate zero coordinates while the positive coordinates are still zero,
then use proportional positive power exponents for the positive group.
A common rescaling of those exponents can make each at least one without
changing the integrated coefficients. Thus endpoint regularity does not
require singular power derivatives. That reparameterization need not
preserve a literal primitive-site square ledger; the theorem optimizes
the stated observed current, not an unidentified Wick diagonal.

The original source amplitude is still1/sqrt(K). In this boundary layer
the extra selection among nearby face regimes changes energy at order
epsilon^3/K, while the earlier departure from uniform is generally
order epsilon/K. A nonzero exact active-set effect is not a large-moment
or approximation-complexity lower bound.

## 6. Three literal prime tuples in the original kernel

The preregistered acquisition retained the first three primes
99999931,101999927,104039917. Its original fourth-prime control and
the first primes in the two fixed new windows give:

|fourth prime|certified active coordinates|
|---|---|
|106120717|2,3|
|106163179|2,3,4|
|106248047|1,2,3,4|

The discovery is frozen at
`a5e4bb182ca8c7629938cc43a47eece70c61e7ae`. It retains every one of
the15 nonempty simplex supports for each tuple, all16 source factor
allocations, and all69 same-band ordered subset pairs. Exact original
kernel expressions and outward512-bit intervals certify the active
Cramer equations and every inactive KKT sign. No quadratic substitute
for the kernel or post hoc change of a prime window was used. All
three predicted regimes were certified; the replay also retains the
unsuccessful candidate supports. The corresponding asymptotic theorem
still excludes exact threshold equality.
