# T-101510: two-orientation regional AND-gate

Let `F` be the fixed conclusion-facing detector. Suppose adaptive finite-completion positivity and L-101501 give

```text
F(X)_- <= [R(X)]_+.
```

Suppose L-101502 supplies two nonnegative source-faithful majorants

```text
[R(X)]_+ <= L(X),
[R(X)]_+ <= R_opp(X),
```

arising respectively from the least-owner and greatest-owner triangular forms.

For each horizon `Y`, let `Omega_Y` be any measurable subset of `[1,Y]`. Assume

```text
LCOR101510:
int_(Omega_Y) L(X) dX/X = Y^o(1),

RCOR101510:
int_([1,Y]\Omega_Y) R_opp(X) dX/X = Y^o(1).
```

Then

```text
int_1^Y F(X)_- dX/X = Y^o(1).
```

Consequently the fixed Mellin-Landau consumer yields RH.

## Proof

On `Omega_Y`, use `F_-<=L`; on the complement, use `F_-<=R_opp`; then integrate.

The canonical adaptive choice `Omega_Y={L<=R_opp}` gives the pointwise minimum. The two terminal regional estimates remain open.
