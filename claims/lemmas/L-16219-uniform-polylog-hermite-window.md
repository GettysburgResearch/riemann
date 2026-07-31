# L-16219 — Uniform Hermite point values on the quadratic-log mode window

Claim ID: `L-16219`  
Status: **PROVED ASYMPTOTIC TRANSFER FROM DUNSTER; DIRECTED CONSTANTS NOT EXTRACTED**  
Authoring agent: `gpt56-pro-12`  
Created: 2026-08-01  
Primary input: Dunster equations (6.2)--(6.4), (6.9) and their uniform error
range; CCM equations (7.5), (7.9)--(7.12)

## 1. Statement

Let `h_(n,lambda)` be the `L2([-lambda,lambda])`-normalized eigenfunction of

```text
PW_lambda
 =-partial_x[(lambda^2-x^2)partial_x]+(2 pi lambda x)^2,  (L-16219.1)
```

with the Hermite labeling of CCM. Let `h_n` be the correspondingly normalized
Hermite function on the real line. Put

```text
gamma=2 pi lambda^2.                                     (L-16219.2)
```

Fix `C_M<infinity` and let

```text
M_lambda<=C_M(log lambda)^2.                             (L-16219.3)
```

Then there are constants `A,C,c>0`, independent of `lambda` and `n`, such that
for every even `0<=n<=4M_lambda+4`,

```text
||h_(n,lambda)-h_n||_(L2[-lambda,lambda])
 +|h_(n,lambda)(0)-h_n(0)|
 <=C (n+1)^A gamma^(-2/3)log gamma.                       (L-16219.4)
```

The power `A` is inessential; one may take a fixed sufficiently large integer
from the elementary parabolic-cylinder recurrence bounds.

Consequently, uniformly for `0<=j<=M_lambda+1`,

```text
boxed:
c(j+1)^(-1/4)
 <=|h_(4j,lambda)(0)|/|h_(0,lambda)(0)|
 <=C(j+1)^(-1/4).                                        (L-16219.5)
```

In particular,

```text
q_max/q_min=O(M_lambda^(1/4)),                            (L-16219.6)
```

which is exactly the point-value input required in `L-16218`.

## 2. Dunster's range contains the complete packet

Dunster's results are uniform, for fixed `delta in (0,1)`, on

```text
0<=n<=2 gamma(1-delta)/pi.                               (L-16219.7)
```

Since

```text
M_lambda/gamma
 =O((log lambda)^2/lambda^2)->0,                          (L-16219.8)
```

the complete packet lies a vanishing fraction of the distance to the boundary
of that range. Thus all `O` constants in the angular and radial formulas may be
chosen uniformly over the packet.

## 3. Uniform small-turning-point expansion

Dunster's separation parameter is encoded by `sigma_n` through

```text
gamma integral_0^sigma
 sqrt((sigma^2-t^2)/(1-t^2))dt
 =(pi/2)(n+1/2)+O(gamma^-1).                              (L-16219.9)
```

For `sigma<=1/2`, Taylor expansion under the integral gives

```text
integral_0^sigma
 sqrt((sigma^2-t^2)/(1-t^2))dt
 =(pi/4)sigma^2+O(sigma^4).                              (L-16219.10)
```

Since `n=O(log^2 lambda)=o(gamma^(1/2))`, bootstrap in
(L-16219.9)--(L-16219.10) gives uniformly

```text
boxed:
gamma sigma_n^2
 =2n+1+O((n+1)^2/gamma).                                 (L-16219.11)
```

Dunster's parabolic-cylinder parameter `alpha_n` is defined by

```text
alpha_n^2
 =(4/pi) integral_0^sigma
 sqrt((sigma^2-t^2)/(1-t^2))dt,                           (L-16219.12)
```

so the quantization formula gives the sharper identity

```text
boxed:
gamma alpha_n^2
 =2n+1+O(gamma^-1).                                      (L-16219.13)
```

Thus the order of the parabolic-cylinder model is

```text
-gamma alpha_n^2/2
 =-n-1/2+O(gamma^-1),                                    (L-16219.14)
```

uniformly over the whole packet.

## 4. Angular model and Hermite scaling

Dunster's interior angular formula (6.9) expresses the angular PSWF as a
parabolic-cylinder function with parameter (L-16219.14), argument determined by
his `zeta` map, and relative envelope error

```text
O(gamma^(-2/3)log gamma),                                (L-16219.15)
```

uniformly in the range (L-16219.7).

For the physical variable `x=lambda z`, CCM's scale relation gives

```text
sqrt(2gamma) z
 =sqrt(4pi)x.                                             (L-16219.16)
```

Equations (L-16219.11)--(L-16219.13) and the defining integral for `zeta` imply,
on the Hermite scale `|x|<=C sqrt(n+log gamma)`,

```text
sqrt(2gamma) zeta(x/lambda)
 =sqrt(4pi)x
  +O((n+1)^(3/2)/gamma).                                  (L-16219.17)
```

The normalized parabolic cylinder at the integer order `-n-1/2` is exactly the
CCM Hermite function. Standard recurrence relations for `U(a,z)` and its first
derivatives show that changing the order and argument by the amounts in
(L-16219.14),(L-16219.17) costs at most a fixed polynomial in `n` times
`gamma^-1`.

Outside the Hermite scale, both the normalized parabolic-cylinder model and the
Hermite function have a Gaussian envelope; its total `L2` mass is smaller than
any fixed inverse power of `gamma` after the cutoff constant is chosen.

Combining these estimates with (L-16219.15) and the exact angular normalization

```text
integral_(-1)^1 Ps_n^0(x,gamma^2)^2dx=2/(2n+1)           (L-16219.18)
```

proves the `L2` part of (L-16219.4).

## 5. Point evaluation

On the central interval `|x|<=1`, the difference satisfies the rescaled prolate
ODE with coefficients uniformly bounded by a fixed polynomial in `n`. A
one-dimensional interior Sobolev estimate, followed by the ODE, gives

```text
|u(0)|
 <=C[(n+1)||u||_(L2[-1,1])
     +||(H_0-E_n)u||_(L2[-1,1])].                         (L-16219.19)
```

Apply this to

```text
u=h_(n,lambda)-h_n.                                      (L-16219.20)
```

The prolate differential equation differs from the harmonic oscillator by

```text
lambda^-2(x^2 partial_x^2+2x partial_x),                 (L-16219.21)
```

whose action on the `n`th Hermite function has `L2` norm `O((n+1)^2/lambda^2)`
by the creation-annihilation relations. The angular approximation already
controls the remaining spectral-label error. This proves the point-value part
of (L-16219.4), after increasing the harmless fixed power `A`.

## 6. Wallis bounds

For an even Hermite index `n=2m`,

```text
|h_(2m)(0)|^2/|h_0(0)|^2
 =binomial(2m,m)/4^m.                                    (L-16219.22)
```

The central-binomial Wallis bounds give

```text
c(m+1)^(-1/2)
 <=binomial(2m,m)/4^m
 <=C(m+1)^(-1/2).                                        (L-16219.23)
```

For `n=4j`, this is

```text
|h_(4j)(0)|/|h_0(0)|=Theta((j+1)^(-1/4)).                (L-16219.24)
```

The error in (L-16219.4) is

```text
poly(log lambda) lambda^(-4/3)log lambda=o(M^-1/4),       (L-16219.25)
```

so it is smaller than a fixed fraction of the smallest Hermite point value in
the packet. Equations (L-16219.5)--(L-16219.6) follow.

## 7. What this does and does not prove

This closes the uniform Hermite/point-value part of the growing-frame program.
Together with `L-16218`, it removes the need for a growing-index Fuchs defect
formula.

For a machine-checkable production theorem, Dunster's explicit error constants,
the parabolic-cylinder recurrence bounds and the finite threshold in
(L-16219.25) still need to be outward-rounded in the exact CCM normalization.
The asymptotic proof does not supply those numerical constants.

This lemma does not address the arithmetic Poisson aliases, the zero-side local
Weyl error, or RH.
