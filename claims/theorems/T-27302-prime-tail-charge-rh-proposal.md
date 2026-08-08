# T-27302 — Prime residual suffix-charge proposal for RH

Claim ID: `T-27302`  
Title: A subpower maximum suffix of the parabolic ordinary-prime residual implies the Riemann Hypothesis  
Status: **FULL ELEMENTARY PROPOSAL — `PTC` OPEN; RH UNPROVED**  
Authoring agent: `gpt56-pro-22`  
Created: 2026-08-08  
Issue: #273  
Depends on: `L-27301`--`L-27303`; PR #248 `L-24517/L-24520`; PR #265 `L-26202`; PR #271 boundary lift

## 1. Exact residual

Let \(p_1<\cdots<p_N\le X\) be the primes through \(X\), and define

\[
r_i
=
v_{p_i}(b_X^{(0)})
-
\frac1{\sqrt{p_i}}\log\frac X{p_i}.
\tag{T-27302.1}
\]

The parabolic ordinary-prime objective satisfies

\[
J_{\mathbb P,X}(b_X^{(0)})
\ge4\sqrt X-O(\log^2X).
\tag{T-27302.2}
\]

## 2. Prime Tail Charge theorem (`PTC`)

Prove

\[
\boxed{
C_X^{\uparrow}
=
\max_{1\le k\le N}
\left(
 \sum_{j=k}^{N}r_j
\right)_+
=X^{o(1)}.
}
\tag{PTC}
\]

This is one explicit scalar family. It has no arbitrary operator, packet, or
hidden flow quantifier.

## 3. Exact constructive lift

`L-27303` constructs a nonnegative sum of constant blocks between consecutive
ordinary primes. Every internal prime residual becomes nonpositive, every
proper-prime-power response is unchanged, and the only remaining row is one
exterior prime \(Y>X\) carrying exactly \(C_X^{\uparrow}\).

The construction is optimal among all nonnegative upward prime-incidence block
transports.

## 4. Prime-ramp consequence

The interior blocks have nonnegative physical objective increment. The exterior
affine boundary lift therefore gives

\[
P_X
\ge
J_{\mathbb P,X}(b_X^{(0)})
-C_X^{\uparrow}\log Y.
\tag{T-27302.3}
\]

Choose \(Y<2X\) by Bertrand's postulate. Under PTC,

\[
C_X^{\uparrow}\log Y=X^{o(1)},
\]

and hence

\[
\boxed{
P_X\ge4\sqrt X-X^{o(1)}.
}
\tag{T-27302.4}
\]

Adding the proper-prime-power tail changes the ramp by only \(O(\log^2X)\).
The inherited square-screw identity, interpolation estimate, Landau one-sign
theorem, and functional-equation symmetry then give RH.

Thus

\[
\boxed{\mathrm{PTC}\Longrightarrow\mathrm{RH}.}
\tag{T-27302.5}
\]

## 5. Why PTC is the sharpest current finite target

The hierarchy is now

```text
annular ADF
  -> subpower L2 flow
  -> affine boundary control
  -> PTC-type scalar control;

PNL
  -> exact zero boundary charge;

PTC
  -> only subpower exterior charge.
```

`PTC` is weaker than exact PNL and much weaker than the annular `L^2` frame.
It retains precisely the one-sided error tolerated by the square-screw consumer.

## 6. Continuum evidence and exact firewall

The continuum parabolic defect satisfies the exact tail inequality

\[
\int_\theta^1E(u)\,du\le0.
\]

Therefore the continuum analogue of \(C_X^{\uparrow}\) is zero.  The open
arithmetic problem is to transfer this order to the ordinary-prime finite
residual with only subpower discrepancy.

The full suffix beginning at \(p_1=2\) contains the logarithmic prime-ramp mode;
a proof of PTC cannot be obtained from the PNT with a conventional
zero-free-region error, nor by taking absolute values.

## 7. Reviewer-first rejection conditions

Reject a claimed proof of PTC if it:

- omits any ordinary prime through \(X\);
- replaces residual suffixes by continuum integrals without a subpower finite
  error;
- transports mass downward while using the upward-block formula;
- forgets the exterior charge at \(Y\);
- allows a block endpoint that is not an ordinary prime and still claims exact
  proper-power neutrality;
- invokes PNT error terms of size \(X^{1/2-o(1)}\) as though they were
  subpower;
- removes the suffix beginning at \(2\), which contains the RH-bearing scalar
  mode.

## 8. Status

```text
ordinary-prime positive feasibility       PROPOSED COMPLETE
prime-incidence greedy construction       PROPOSED COMPLETE
least suffix-charge formula               PROPOSED COMPLETE
continuum tail inequality                 INHERITED
finite prime tail charge PTC              OPEN / RH-BEARING
PTC -> prime ramp -> RH                   PROPOSED COMPLETE
Riemann Hypothesis                        UNPROVED
```
