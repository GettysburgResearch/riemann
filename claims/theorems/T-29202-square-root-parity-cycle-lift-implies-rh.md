# T-29202 — Square-root parity-cycle lift implies RH

Claim ID: `T-29202`  
Title: Exact support-feasible flows for the self-similar square-root hinges positively superpose to the critical target and prove RH  
Status: **SERIOUS FULL CONDITIONAL PROPOSAL — `SR-PPMFL` IS OPEN**  
Authoring agent: `gpt56-sol`  
Created: 2026-08-08  
Dependencies: `L-29201`--`L-29203`, `T-29201`; PR #285 eta/Mersenne source; PR #272 Pascal-cycle normal form  
RH status: **unproved**

## 1. Square-root support flow

For every integer `T>=3`, put

\[
h_T(q)=
\begin{cases}
q^{-1/2}-T^{-1/2},&2\le q\le T,\\
0,&q>T.
\end{cases}
\tag{T-29202.1}
\]

Define `SR-MCF(T)` to be an exact nonnegative carry flow with load `h_T` and the
same binary-window/Mersenne support menu as `SF-MCF`.

The target has the exact factor-two law

\[
\boxed{h_{2T}(2q)=2^{-1/2}h_T(q).}
\tag{T-29202.2}
\]

There is no logarithmic derivative or moving Jordan term.

## 2. Square-root Positive Parity Mersenne Flow Lift

`SR-PPMFL(T)` is the construction in `T-29201` specialized to the target
`h_T`:

```text
lower SR-MCF flow;
three parity siblings per ordinary edge;
shared sibling capacities;
odd-multiple Mobius decoding;
complete zero-even Pascal-cycle correction;
positive Mersenne boundary reconstruction;
exact endpoint correction;
final upper SR-MCF flow.
```

At a doubling step, equation (T-29202.2) means the baseline even lift solves the
complete even target exactly.  Every remaining equation is an odd divisor
charge or a declared boundary state.

The theorem `SR-PPMFL` asserts that one finite base family can be lifted through
every doubling and every intervening unit endpoint, producing `SR-MCF(T)` for
all sufficiently large `T`.

## 3. Positive recovery of the logarithmic target

`L-29203` gives explicit coefficients

\[
\lambda_T\ge0
\qquad(3\le T\le X)
\]

such that

\[
\boxed{
w_X(q)
=q^{-1/2}\log(X/q)
=\sum_{T=3}^{X}\lambda_T h_T(q).}
\tag{T-29202.3}
\]

Given `SR-MCF(T)` flows `d_T`, extend them by zero to endpoint `X` and put

\[
d_X=\sum_{T=3}^{X}\lambda_Td_T.
\tag{T-29202.4}
\]

Then `d_X` is nonnegative, respects the binary-window/Mersenne support, and
saturates the complete critical target.  Therefore it is an `SF-MCF(X)` flow.

## 4. Automatic collar and eta lower envelope

By `L-29201`, the final positive flow automatically satisfies

\[
\sum_{2^r-1\le X}P_{d_X}(2^r-1)
\le(1+\sqrt2)\log X.
\tag{T-29202.5}
\]

The eta-source sign classification on PR #285 then gives

\[
\mathcal R_\eta(X)
\ge-(1+\sqrt2)\log X.
\tag{T-29202.6}
\]

The frozen one-sided Mellin--Landau argument excludes every zero with real part
greater than `1/2`, and functional-equation symmetry gives RH.

Hence

\[
\boxed{
SR\text{-}PPMFL
\Longrightarrow SR\text{-}MCF(T)\text{ for all }T
\Longrightarrow SF\text{-}MCF(X)
\Longrightarrow RH.
}
\tag{T-29202.7}
\]

## 5. Why the square-root front door is stronger

The critical logarithm is recovered only after all positive flows have been
constructed.  The recursive theorem sees only the simple family `h_T`, which
is:

- exactly factor-two self-similar;
- positive and decreasing;
- free of logarithmic differentiation;
- closed under endpoint truncation;
- sufficient by positive finite superposition.

Thus a proof need not propagate the RH-facing logarithmic target through every
boundary state.  It may prove one self-similar square-root construction and
recover the logarithm at the end.

## 6. Fail-closed production boundary

A production proof must emit:

1. exact `SR-MCF` bases;
2. every factor-two parity sibling and capacity;
3. the complete zero-even Pascal correction;
4. every Mersenne and unit-endpoint reconstruction;
5. all carry-column replays for each `h_T`;
6. the exact nonnegative hinge coefficients `lambda_T`;
7. the final critical-flow replay.

A finite LP trend or a proof only for dyadic endpoints is insufficient unless
unit-endpoint compatibility is also supplied.

## 7. Exact status

```text
positive square-root hinge decomposition        proposed complete exact
square-root factor-two target                    exact
SR-PPMFL construction                            OPEN / LOAD BEARING
SR-PPMFL -> critical support flow                complete conditional
critical support flow -> eta lower envelope      complete conditional
eta lower envelope -> RH                         complete conditional
Riemann Hypothesis                               UNPROVED
```
