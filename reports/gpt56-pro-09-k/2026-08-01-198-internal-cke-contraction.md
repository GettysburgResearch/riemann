# Internal CKE contraction: exact Green–Cayley reduction and refutation of the advertised shortcut

Agent: `gpt56-pro-09-k`  
Date: 2026-08-01  
Target: prove `||CKE||<=1` in the completed Green-minimizer/plus-profile metric  
Verdict: **not proved**; the generic inference used in the source manuscript is false, and the exact theta-specific dissipativity is isolated.

## 1. Reconstructed operator

The lifted plus integrand is `(I+R)F`, the lifted minus integrand is `(I-R)F`,
and `R` is multiplication by `r=s+u>=0`. Thus

```text
K=(I-R)(I+R)^-1,
T=CKE,
CE=I.
```

Here `C` is Volterra observation and `E` is the Green-minimizer lift from the
observed plus profile to its lifted plus integrand.

Writing the recovered raw lift as `F_y=(I+R)^-1Ey`, define

```text
Uy=C F_y,
Vy=C R F_y.
```

Then

```text
U+V=I,
T=U-V.
```

On the zeroth-moment range put `L=V U^-1`. Exactly,

```text
T=(I-L)(I+L)^-1
```

and

```text
I-T*T=4(I+L)^-* Re(L) (I+L)^-1.
```

Therefore the completed contraction is precisely

```text
Re(L)>=0.
```

`L` is the induced first-moment/Dirichlet-to-Neumann operator on the actual
Green range.

## 2. Why the pointwise multiplier proof fails

Let `A_C=C*C`. Since `CE=I`,

```text
I-(CKE)*(CKE)=E*[A_C-K A_C K]E.
```

The Cayley algebra gives

```text
A_C-K A_C K
=2(I+R)^-1[R A_C+A_C R](I+R)^-1.
```

The pointwise estimate `|K|<=1` controls `I-K^2`. It does not control the
noncommutative anticommutator `R A_C+A_C R` created by Volterra integration.

## 3. Exact finite refutation

Take

```text
C=(1,1),
K=diag(1/5,4/5),
trace(z)=z_2,
Q(z)=|Cz|^2-|CKz|^2.
```

Then

```text
Q=[[24/25,21/25],[21/25,9/25]],
Q|ker(trace)=24/25>0.
```

The unique Green-stationary representative of trace `x` is

```text
z_x=(-7x/8,x),
```

but

```text
Cz_x=x/8,
CKz_x=5x/8.
```

After parametrizing by the observed plus value `y=x/8`,

```text
E(y)=(-7y,8y),
CE=I,
CKE=5I.
```

Thus Green stationarity, trace-zero coercivity, and `||K||=4/5` coexist with
`||CKE||=5`.

The entries are literal Volterra Cayley values:

```text
kappa(2/3)=1/5,
kappa(1/9)=4/5.
```

The Fraction-only verifier returns

```text
GREEN_STATIONARITY_DOES_NOT_IMPLY_CKE_CONTRACTION
```

with proof-object SHA-256

```text
7e5fca85abd94b7699f8e3b7227dfa93306eaa2cdfbe2f527eb5ba821d8cbe97.
```

Seven adversarial tests pass.

## 4. Exact theta form of the missing dissipativity

At `omega=0`, the observed zeroth and first moments are the Hankel transforms

```text
M=H_Psi f,
N=H_(t Psi) f.
```

Hence

```text
4 Re<M,N>=<f,{H_Psi,H_(t Psi)}f>.
```

In the multiplicative theta coordinates of `L-19814`, the same operator is

```text
2 T_theta* L_R T_theta
+{L_X,T_theta*T_theta}.
```

The exact internal completion is therefore an explicit square

```text
2 T_theta* L_R T_theta
+{L_X,T_theta*T_theta}
=4 J*J,
```

or equivalently

```text
Re(L)=J*J.
```

The theta feature satisfies

```text
(X d_X-R d_R)a_X(R)=a_X(R)/2,
```

so the remaining viable mechanism is a dilation/Green boundary identity that
turns the anticommutator into a boundary square plus positive bulk energy.

## 5. Outcome

The requested contraction is not established. What is established is:

1. the exact Green–Cayley defect factorization;
2. an exact finite counterexample to the source manuscript's generic
   `Euler orthogonality + |kappa|<=1` inference;
3. the smallest theta-specific missing identity, `Re(L)=J*J`.

This is a correction to the internal proof, not a counterexample to the Riemann
theta contraction itself. A proof of the final theta square would still close
the internal operator target.
