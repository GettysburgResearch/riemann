# L-92921 — An oriented Hall–causal–physical coupling has the native, not rough-lift, output marginal

Claim ID: `L-92921`  
Status: **PROVED EXACT COMPOSITION THEOREM ON FROZEN POSITIVE-KERNEL INPUTS — INDEPENDENT REVIEW REQUIRED**  
Created: 2026-08-15  
Strengthens: PR #500 `L-91850/L-91851`  
Primary inputs: `L-91361`, `L-91362`, `L-91650`, `L-91654`, `L-91674`, `L-91850`, `L-92920`  
RH status: **unproved**

## 1. Oriented source label

Augment every PR #500 coupling label by an orientation bit

\[
 \epsilon\in\{0,1\}.
\]

The complete label is

\[
 (s,d,p,h,\epsilon,a,t),
\]

where `s` is the endpoint coordinate, `d` the small-prime colour, `p` the least
rough owner, `h` the source history, `a` the current/child class, and `t` the
physical same-index target.

Before Hall or physical placement, replace a paired packet `P` by

\[
 \operatorname{or}_\epsilon(P)=S^\epsilon P.
\tag{L-92921.1}
\]

## 2. Hall realization respects orientation

For the oriented pair, declare its positive channel as even capacity and its
negative channel as odd demand.  The deterministic no-upward Hall coupling
exhausts the odd marginal and splits the even marginal into matched and
residual parts.  The standard residual-plus-edge-bonus identity gives a
nonnegative physical row whose typed observation is

\[
 \boxed{
 \mathcal O(H_\epsilon(P))
 =\Sigma(S^\epsilon P)
 =(-1)^\epsilon\Sigma(P).
 }
\tag{L-92921.2}
\]

The same Hall edges are used in target, declared score and every component row.
Ordinary responses are evaluated at `q` and `4q` before detail is formed.

## 3. Actual child placement

The causal kernel is stochastic on each positive oriented source packet.  A
child is sent through the positive same-index physical placement supplied by
the frozen causal-generator and functor theorems.  The placement contract is

\[
 \mathcal O(P^{\rm phys}_{b})
 =\Sigma(S^{\epsilon_b}\mathbf P_b).
\tag{L-92921.3}
\]

The least rough prime is part of the kernel, so first-owner classes are disjoint.
The orientation bit is not erased when the child is formed.

No actual child response is promoted to a full native child capacity.

## 4. Native commuting square

Apply the coupling to the complete paired stopping line of `L-91362`.  Hall
realizes the finite forcing; the oriented physical child kernels realize every
actual rough child.  By `L-92920.8`, before finite/continuum comparison,

\[
\begin{CD}
 \mathbf P_X @>{\text{stopping line}}>>
 \mathbf F_{61,X}\oplus\bigoplus_b\mathbf P_b\\
 @V{\Sigma}VV @VV{\text{Hall + oriented child placement}}V\\
 N_X @= d_X^{\rm ideal}
\end{CD}
\tag{L-92921.4}
\]

commutes in every declared linear observation.  In particular,

\[
 \boxed{
 C_{d_X^{\rm ideal}}=w_X,
 \qquad
 \Xi(d_X^{\rm ideal})=\Omega_X
 }
\tag{L-92921.5}
\]

before support restriction, quantization and the separately typed signed
comparison.

## 5. One global quantizer

Sum Hall residuals, Hall bonuses, causal currents and all oriented actual child
placements in the common tagged endpoint target.  Apply one Markov quantizer
which depends only on physical endpoint state.  Positive linearity preserves
the commuting square; labels may be erased only after this step.

The exported recursive family is empty.  This is not because a rough lift is
being mistaken for native data, but because every actual oriented child has
already been physically inserted into the native total.

## 6. Fail-closed checks

The compiler rejects any certificate in which:

```text
the orientation bit is absent;
a least rough owner occurs twice;
a child uses an unoriented full native capacity;
the quantizer depends on a child label;
ordinary q and 4q are not observed before detail;
the precomparison q=2 marginal equals the rough lift.
```

Dropping the orientation bit changes (L-92921.4) to the rough-lift branch and is
caught quantitatively by `R-92920`.

## 7. Boundary

```text
paired stopping-line source ownership                 exact
rough-prime orientation                               explicit
Hall residual/bonus physical positivity               frozen exact input
actual child physical placement                       frozen exact input
precomparison output                                  native
full child-capacity promotion                          absent
one label-blind quantizer                              exact
all-column finite comparison                           next lemma
Riemann Hypothesis                                     unproved
```
