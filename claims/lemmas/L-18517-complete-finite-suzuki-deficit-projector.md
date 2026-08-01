# L-18517 — Complete finite Suzuki deficit and certified canonical projector

Claim ID: `L-18517`  
Status: `PROPOSED — COMPLETE FINITE PROOF WITH DIRECTED X-18509 CERTIFICATE`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `D-0001`; `L-18512`; finite generalized spectral theorem  
Scope: the actual X-18507 support `(c,N)=(10,2)`; this is a complete finite spectral deficit, not the infinite symbol-deficit operator

## 1. Complete finite lower model

Let `A` be the exact cutoff-free D-0001 even matrix at

\[
(c,N)=(10,2)
\]

in the unnormalised basis

\[
b_0=e_0,\qquad b_k=e_{-k}+e_k,
\]

with metric

\[
G=\operatorname{diag}(1,2,2).
\]

Every prime power through `10`, the complete pole block, and the cutoff-free
archimedean block are included in `A`.

Choose

\[
g={1\over4}
\]

and define the complete finite spectral deficit

\[
\boxed{D=gG-A.}
\tag{L-18517.1}
\]

The directed LDL certificate `X-18509` proves

\[
D\succ0.
\]

Thus

\[
\boxed{A=gG-D}
\tag{L-18517.2}
\]

is an equality with no omitted symbol, prime, archimedean, assembly, or
lower-model slack.

Set

\[
\Gamma={1\over1000},
\qquad
\theta=g-\Gamma={249\over1000},
\qquad
Q_0=I_3.
\]

The exact deficit-canonical augmentation is

\[
\boxed{
P_D=
\mathbf1_{(\theta,\infty)}
\left(G^{-1/2}DG^{-1/2}\right),
}
\tag{L-18517.3}
\]

transported back to the original generalized coordinates. Put `P_C=I-P_D`.

## 2. Proof-grade center frames

Let

```text
c = (
772846301980934704074421915396899854999885320654875187304597306128249654,
780825253029963795781224774457448353496365730860585722869323995400868824,
807799787166279260402465670748652523005181383995845011881003209651086855
)^T.
```

Define

\[
Y_C=c,
\]

and

\[
\boxed{
Y_D=
\begin{pmatrix}
-2c_1&-2c_2\\
c_0&0\\
0&c_0
\end{pmatrix}.
}
\tag{L-18517.4}
\]

Then exactly

\[
Y_D^*GY_C=0.
\]

The directed certificate proves

\[
\boxed{
Y_D^*(\Gamma G-A)Y_D\succ0,
}
\tag{L-18517.5}
\]

and

\[
\boxed{
Y_C^*(A-\Gamma G)Y_C>0.
}
\tag{L-18517.6}
\]

By min--max, the generalized eigenvalues of `(A,G)` satisfy

\[
\lambda_2<\Gamma<\lambda_3.
\]

Equivalently, the generalized deficit spectrum has exactly two eigenvalues
strictly above `theta` and one strictly below it. Therefore

\[
\operatorname{rank}P_D=2,
\qquad
\operatorname{rank}P_C=1.
\]

## 3. Exact-projector enclosure

Let

\[
r={c^*Ac\over c^*Gc}
\]

and

\[
\rho^2=
{(Ac-rGc)^*G^{-1}(Ac-rGc)\over c^*Gc}.
\]

The X-18509 interval computation proves

\[
r>0.174295607214687271825791203282426808
\]

and

\[
{\rho\over r-\Gamma}<10^{-52}.
\]

Let

\[
\widehat P_C={c(c^*G)\over c^*Gc},
\qquad
\widehat P_D=I-\widehat P_C.
\]

The exact top spectral projector satisfies

\[
\boxed{
\|P_C-\widehat P_C\|_G
=
\|P_D-\widehat P_D\|_G
<10^{-52}.
}
\tag{L-18517.7}
\]

### Proof of the projector radius

Whiten the metric and normalize `c`. Equation (L-18517.5) says that every
vector orthogonal to the normalized center has Rayleigh quotient below
`Gamma`; hence all spectral mass except the top eigenvalue lies at most at
`Gamma`. The squared residual is the spectral integral of `(lambda-r)^2`.
On the lower spectral subspace this factor is at least `(r-Gamma)^2`. Therefore
its mass is at most `rho^2/(r-Gamma)^2`. For rank-one orthogonal projectors, the
operator-norm distance equals the sine of the principal angle. This proves
(L-18517.7).

Thus the artifact emits the exact canonical projector by functional calculus,
a rational center, and a strict proof-grade enclosure of radius `10^-52`.

## 4. The source flag is not canonical

The X-18507 source-valid flag is

\[
Y_S=
\begin{pmatrix}
-2&-2\\
1&0\\
0&1
\end{pmatrix},
\]

whose metric-orthogonal complement is

\[
q=(1,1,1)^T.
\]

If `Ran Y_S` were the canonical spectral range, self-adjointness would force

\[
q^*DY_S=0.
\]

The directed intervals instead certify

\[
(q^*DY_S)_1<-0.0035173621680981225656,
\]

\[
(q^*DY_S)_2<-0.0154082689922869053188.
\]

Therefore

\[
\boxed{
\operatorname{Ran}Y_S\ne\operatorname{Ran}P_D.
}
\tag{L-18517.8}
\]

The source flag is close to, but not equal to, the true deficit-canonical
augmentation.

## 5. Existing direct short on the true packet

Because

\[
D=gG-A,
\]

the exact spectral projectors `P_D,P_C` reduce both `D` and `A`. Hence the
cross block is exactly zero:

\[
P_D^*AP_C=0.
\]

The directed full-matrix LDL certificate proves

\[
\boxed{
A\succeq {1\over200000000}G.
}
\tag{L-18517.9}
\]

Therefore the exact canonical block obeys the same floor. Applying `L-18512`
with trial solve `X=0` gives zero residual and

\[
\boxed{
S_D=A|_{\operatorname{Ran}P_D}
\succeq {1\over200000000}G|_{\operatorname{Ran}P_D},
\qquad
\Delta_D=0.
}
\tag{L-18517.10}
\]

The safe one-dimensional complement has the much larger certified floor

\[
\boxed{
A|_{\operatorname{Ran}P_C}
\succeq {17\over100}G|_{\operatorname{Ran}P_C}.
}
\tag{L-18517.11}
\]

## 6. Scope

- This is the first production decision of the source-versus-deficit flag at an
  actual X-18507 support.
- The deficit is the exact finite spectral deficit `gG-A`; it is not the global
  infinite-dimensional positive symbol-deficit compression.
- The finite canonical packet is strictly positive and has zero direct-short
  negative part.
- A single finite support does not prove a cofinal rate or RH.
