# L-94020 — The live endpoint fibre and `P_61` source tree have explicit root parameters and coefficients

Claim ID: `L-94020`
Status: **PROVED EXACT SOURCE-MARGINAL AND OWNER THEOREM**
Created: 2026-08-16
Depends on: `L-91107`, `L-91362`; normalization firewall `L-91377--L-91379`
Replay: `X-94020-live-endpoint-source`
RH status: **unproved**

This theorem supplies the concrete data that review #504 found absent.  It is a
source theorem, not yet a positive physical-realization theorem.

## 1. Continuum endpoint fibre

For a global endpoint `X` and endpoint parameter `s`, put

\[
 x=\frac Xs.
\tag{L-94020.1}
\]

The exact continuum inverse of `L-91107` is the paired equality source

\[
 \lambda^\star(x)
 =\sum_{k\le x}
  \frac{\mu(k)}{\sqrt k}
  \left(2\sqrt{x/k}-1\right).
\tag{L-94020.2}
\]

Thus the live fibre has the literal positive colour masses

\[
 a_{x,k}
 =\frac{|\mu(k)|}{\sqrt k}
  E(x/k),
 \qquad
 E(z)=2\sqrt z-1,
\tag{L-94020.3}
\]

with parity `sign(mu(k))`.  Every colour at fixed `s` multiplies the same
endpoint feature packet.  The root parameter is `x=X/s`; it is not a free
fitting parameter.

The SHARP target and declared score use the same occurrence coefficient and the
unique two-channel identities

\[
 T(z)=4\sqrt z-3=E(z)+2R(z),
\]

\[
 S(z)=5\sqrt z-3=2E(z)+R(z),
\]

\[
 R(z)=\sqrt z-1\ge0.
\tag{L-94020.4}
\]

The equality channel carries the component row and every ordinary response.
The reserve channel is row-zero.  No coefficient may be changed between these
coordinates.

## 2. Literal finite endpoint occurrence

On integer cell `m`, the exact finite occurrence is

\[
 \boxed{
 a_{X;m,k}^{\rm fin}
 =\frac{|\mu(k)|}{\sqrt{mk}}
  \log\frac X{mk},
 \qquad k\le X/m.
 }
\tag{L-94020.5}
\]

Its owner label is

```text
(endpoint cell m,
 root parameter X/m,
 small-prime divisor d,
 ordered rough history h,
 least rough owner,
 Möbius parity).
```

The finite occurrence and continuum occurrence are different marginals; their
signed difference is the retained quadrature/finite-realization ledger.  The
witness `R-94020.3` prevents their atomwise identification.

## 3. Exact `P_61` and rough history map

For squarefree `k`, write uniquely

\[
 k=d\,p_1\cdots p_t,
\tag{L-94020.6}
\]

where `d|P_61` and

\[
 67\le p_1<\cdots<p_t.
\]

Then

```text
small divisor       d;
rough history       h=(p_1,...,p_t);
first rough owner   p_1 when t>0, otherwise root;
parity              (-1)^(omega(d)+t).
```

This is a disjoint and exhaustive owner registry.

For the paired source `P_1^(a)(x)`, the coefficient at this occurrence is

\[
 \frac{1}{\sqrt{d p_1\cdots p_t}}
 \left(a\sqrt{\frac{x}{d p_1\cdots p_t}}-1\right),
\tag{L-94020.7}
\]

placed in the parity coordinate above.  Formula (L-94020.7), including `a=2` for the equality channel, `3P_1^(4/3)` for the
single-SHARP target and `3P_1^(5/3)` for declared score, is the actual initial
source coefficient.  These three labels share the occurrence coefficient and
owner; only the channel profile changes.

## 4. Exact stopped-tree nodes

The least-prime recursion gives one node for every `(d,h)`.  If `h` is empty,
the node belongs to the `P_61` finite forcing.  If `h` is nonempty, the node is
owned by its least rough prime and is an actual paired child occurrence.  The
path coefficient before physical observation is exactly

\[
 (d p_1\cdots p_t)^{-1/2};
\tag{L-94020.8}
\]

the parity swaps once at every rough edge.

Applying the row, ordinary, `q/4q`, detail, boundary and literal-score maps to
this *same* registry preserves the identity by linearity.  This theorem thereby
instantiates the source/path marginal in every native coordinate.  It does not
assert that individual oriented children have positive physical observations;
`R-94020` proves they do not.
