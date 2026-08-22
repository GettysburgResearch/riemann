## T-105300 continuation — the low-order Levinson difficulty

The high-order coherence tail from T-105200 is not the low-order descent. This
commit attacks the missing step directly.

### Exact finite theorem

For a real monic squarefree polynomial `p` with squarefree `p'`, define

```text
A = R[x]/(p')
q = -p/(p'') mod p'
B(u,v) = Tr_A(q u v)
H = <1> direct-sum B.
```

Then

```text
signature(H) = number of real roots of p.
```

A direct entire-window version is also exact. For a regular rectangle,

```text
B_ij = -(2 pi i)^(-1) integral [F/F'] z^(i+j) dz
```

has inertia `(G+C,E+C)`. Therefore its signature is the literal
`good-extrema - wrong-extrema` count, while every nonreal critical pair
contributes one positive and one negative direction. Any source-owned analytic
compression gives a rigorous rank--trace lower bound for the real zeros of the
antiderivative, with both endpoint bits retained.

A real critical point contributes the one-dimensional sign `-p(c)/p''(c)`;
a nonreal conjugate pair contributes a `(1,1)` block. Equivalently, the
negative index is exactly half the number of nonreal roots of `p`.

For every polynomial `w` coprime to `p'`, replacing `q` by `q w^2` is a
source-faithful congruence and preserves inertia. The rank–trace certificate is

```text
real-root proportion >=
  2 (tr H_w)_+^2/[n tr(H_w^2)] - 1.
```

The exact record target is

```text
Theta > 0.83625  ->  line proportion > 0.67250.
```

A higher resolvent hierarchy recovers the exact sign count and is available if
two moments remain sharp.

### Anthropic/Xi-prime bridge

The frozen public Lean artifact proves `0.86864` of Xi-prime zeros are simple
and on the line with the quartic window. A low-order good-extrema/coherence
fraction above

```text
77057/86864 = 0.8870993737...
```

would beat `0.67250`; the clean target `9/10` gives `0.694912`.

### Binding firewall

For `p=x^3-3x+3/2`, all roots are real and both critical residues are negative,
but unweighted residue coherence is only `16/25`. Scalar coherence is therefore
not a faithful low-order proxy; the inertia/preconditioning route is required.

### Boundary

```text
finite Hermite-Pick inertia                PROVED EXACT
polynomial preconditioning                 PROVED EXACT
rank-trace and sign-resolvent hierarchy    PROVED EXACT
record threshold arithmetic                PROVED EXACT
LHRT105300                                 OPEN / RECORD-BEARING
LEXI105301                                 OPEN / RECORD-BEARING
Anthropic record beaten                    NO
Riemann Hypothesis                         UNPROVED
```
