# L-91751 — Positive source packets form a hereditary causal class and admit direct terminal realization

Claim ID: `L-91751`  
Status: **PROVED EXACT POSITIVE-PACKET REALIZATION AND HEREDITARY RESET THEOREM**  
Created: 2026-08-15  
Frozen inputs: `L-91375`, `L-91650`, `L-91653`, `L-91654`, `L-91656`, `L-91658`, `L-91726/L-91732`  
RH status: **unproved**

## 1. The positive source-packet class

Let \(\mathscr C\) be the smallest class containing every complete positive
endpoint atom `P_u` of `L-91653`, with causal zero extension below quotient one,
and closed under:

```text
finite positive sums;
positive source integrals;
source restriction;
normalized same-index placement U_p;
retention of complete provenance labels.
```

A packet in \(\mathscr C\) carries

\[
 (J,T,S,E,q,\Gamma,\Xi,b)
\]

in the exact normalization of `L-91653`. Root-global collars, omissions, finite
corrections and matrix ports are not descendant coordinates. Thus all
descendant ports are zero.

For a packet `P`, write `m(P)=T(P)`. Let `Delta(P)` be its optimal complete
literal-score deficit in the packet's own feasible cone.

## 2. Every positive packet has an immediate admissible row

For one atom,

\[
 T(u)=4\sqrt u-3,
 \qquad
 S(u)=5\sqrt u-3,
\]

and its canonical row has nonnegative literal score `E(u)`. Since

\[
 2T(u)-S(u)=3(\sqrt u-1)\ge0,
\]

\[
 \Delta(P_u)
 \le S(u)-E(u)
 \le S(u)
 \le2T(u).
\tag{L-91751.1}
\]

All operations defining \(\mathscr C\) are positive and preserve the canonical
row together with its exact ordinary/detail responses. Hence, for every
`P` in \(\mathscr C\), its integrated canonical row is feasible and

\[
 \boxed{\Delta(P)\le2m(P).}
\tag{L-91751.2}
\]

This is already a terminal realization theorem: a positive child packet need
not undergo another root Hall, quantizer, collar, omission, base correction or
matrix-port construction.

## 3. Exact hereditary reset, if recursion is desired

Fix `P` in \(\mathscr C\). Let `p_1<...<p_k` be the finite global rough-prime
list active on its source support. Put

\[
 r_i=p_i^{-1/2},
 \quad
 s_i=\prod_{h\le i}(1-r_h),
 \quad
 \lambda_i=r_is_{i-1},
 \quad
 \alpha_i=r_i\lambda_i.
\]

Use zero extension on inactive fibres. `L-91650` gives

\[
 \boxed{
 P=s_kP+
 \sum_i\lambda_i(P-r_iU_{p_i}P_{/p_i})+
 \sum_i\alpha_iU_{p_i}P_{/p_i}.
 }
\tag{L-91751.3}
\]

By positive integration of `L-91654`, every causal difference

\[
 C_i(P)=P-r_iU_{p_i}P_{/p_i}
\]

is a complete nonnegative current packet. Every child `P_{/p_i}` is a positive
source restriction/pushforward and remains in \(\mathscr C\). Complete
provenance labels advance with the child.

Define

\[
 P^{\rm cur}=s_kP+\sum_i\lambda_iC_i(P).
\]

Then

\[
 \boxed{
 P=P^{\rm cur}+\sum_i\alpha_iU_{p_i}P_{/p_i}
 }
\tag{L-91751.4}
\]

simultaneously in source, benchmark, target, declared score, literal score,
component row, ordinary response, radix-four response, and every descendant
boundary coordinate. Every term has zero root-global port.

## 4. Weighted child target and current debt

SHARP target monotonicity gives

\[
 m(U_{p_i}P_{/p_i})\le m(P).
\]

The actual weighted estimate is

\[
 \boxed{
 \sum_i\alpha_i m(U_{p_i}P_{/p_i})
 <\frac18m(P).
 }
\tag{L-91751.5}
\]

The global prime list is used once. Inactive fibre/prime pairs contribute zero,
so the coefficient list is not repeated per endpoint fibre.

Each causal generator has deficit at most twice its target mass by `L-91375`,
and `s_kP` has the direct realization (L-91751.2). Since current and children
form a nonnegative target partition,

\[
 m(P^{\rm cur})\le m(P),
\]

and therefore

\[
 \boxed{
 \Delta(P^{\rm cur})\le2m(P).
 }
\tag{L-91751.6}
\]

This establishes the hereditary typed reset directly rather than invoking a
conditional consumer as its own premise.

## 5. Two valid descendant bounds

### Direct terminalization

Use the immediate canonical row of every first-generation child. Then

\[
 \boxed{
 \sum_i\alpha_i\Delta(P_{/p_i})
 <\frac14m(P).
 }
\tag{L-91751.7}
\]

This follows from (L-91751.2) and (L-91751.5). No recursive tree is needed.

### Optional recursive envelope

If one recursively applies (L-91751.4), the usual normalized constants satisfy

\[
 C_{n+1}\le2+\frac18C_n,
 \qquad C_0\le2,
\]

so

\[
 \boxed{C_n<\frac{16}{7}.}
\tag{L-91751.8}
\]

Thus the recursive implementation is also uniformly controlled, but the
canonical closure packet uses the shorter direct terminalization.

## 6. Factor-67 root consequence

The retained factor-67 root target mass is below `3020` on the frozen density
input. Therefore the complete first-generation child deficit under direct
terminalization is below

\[
 \boxed{
 2\cdot\frac{3020}{8}=755.
 }
\tag{L-91751.9}
\]

No root-global correction is repeated below the root.

## 7. Boundary

```text
positive source-packet class                         EXPLICIT
canonical row feasible for every positive packet    EXACT
all positive packets have deficit <=2 target mass   EXACT
all-coordinate causal reset                          EXACT
actual weighted child target <1/8                    EXACT
current debt <=2 parent target                        EXACT
first-generation direct terminalization               DEFICIT < parent/4
optional complete recursive envelope                  <16/7 target mass
root-global corrections repeated on descendants       NO
one-shot total-row method                              L-91753
Riemann Hypothesis                                     UNPROVEN
```
