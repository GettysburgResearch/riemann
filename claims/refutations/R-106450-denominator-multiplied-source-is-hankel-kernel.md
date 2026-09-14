# R-106450 — A denominator-multiplied analytic source lies in the Hankel kernel

Claim ID: `R-106450`  
Status: **BINDING EXACT REFUTATION OF THE L-106400 SOURCE-TO-INITIAL-SPACE STEP**  
Created: 2026-08-25  
Depends on: standard Toeplitz--Hankel factorization  
RH status: **not assumed**

Let

\[
U={N\over D}
\]

be a reduced rational all-pass function in the upper-half-plane Hardy model.
Assume `g` is analytic and both `Dg` and `Ng` belong to `H^2`.  Then

\[
U(Dg)=Ng\in H^2,
\]

and therefore

\[
\boxed{
H_U(Dg)=P_-(U Dg)=0.
}
\tag{R-106450.1}

Equivalently, if

\[
U=\omega {B_+\over B_-}
\]

is the reduced inner quotient, then

\[
\ker H_U=B_-H^2.
\]

The analytic denominator contains the upper inner factor `B_-`, so every
admissible denominator-multiplied vector belongs to the kernel.  It cannot
simultaneously lie in the nonzero initial space

\[
\mathcal I_U=(\ker H_U)^\perp=K_{B_-}.
\]

Hence the assumption printed in the first version of `L-106400`,

```text
S=D G subset I_U,
```

forces `S={0}` at the literal Hardy-space scope.

## Minimal exact fixture

On the unit circle take

\[
U(z)=z^{-1},
\qquad N(z)=1,
\qquad D(z)=z,
\qquad g(z)=1.
\]

Then

\[
Dg=z\in H^2,
\qquad U(Dg)=1\in H^2,
\qquad H_U(Dg)=0.
\]

But

\[
\mathcal I_U=\operatorname{span}\{1\},
\]

and `z` is orthogonal to it.  The all-pass index is nonzero even though the
entire denominator-multiplied source is invisible to the Hankel operator.

## Consequence for the endpoint numerator

The algebra

\[
N-D=2i\lambda
 \bigl(F F^{(K+1)}-F'F^{(K)}\bigr)
\]

remains exact.  However

\[
P_-((N-D)g)=0
\]

whenever the stated analytic hypotheses hold, because both `Ng` and `Dg` are
analytic.  Thus the exterior-square numerator cannot be identified with a
nonzero restricted Hankel leakage by multiplying source vectors by `D`.

The genuine conclusion-facing symbol is

\[
\boxed{
U-1={N-D\over D}.
}
\tag{R-106450.2}

The denominator resolvent and its pole principal parts are load bearing.  They
are exactly the residue weights in `L-106442`.

## Binding disposition

The following survive:

```text
endpoint all-pass winding identities;
intermediate-companion cancellation;
N-D exterior-square Fourier source;
signed Fourier-tail and residue-Gram normal forms;
companion barycenter and derivative-root compression.
```

The following do not survive as proved conclusion-facing estimates:

```text
L-106400.5--L-106400.6 nonzero Dg initial-space compression;
L-106413/L-106443 promotion of the finite source ratio to H_U P;
T-106420 absolute-coverage chain as sourced through that promotion;
T-106430 and T-106440 percentage implications using the claimed visible cost.
```

A repaired theorem must estimate the literal quotient `(N-D)/D`, or its exact
confluent residue Gram, without placing `D H^2` in the Hankel initial space.