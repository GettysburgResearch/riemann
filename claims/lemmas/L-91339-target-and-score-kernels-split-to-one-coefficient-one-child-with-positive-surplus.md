# L-91339 — Target and score kernels split to one coefficient-one child with positive local surplus

Claim ID: `L-91339`  
Status: **PROVED EXACT SOURCE/SCORE RESET IDENTITY**  
Created: 2026-08-12  
Depends on: `L-91108`, `L-91330`, `R-91307`  
RH status: **unproved**

## 1. The two conclusion-relevant kernels

At the squarefree source level, the SHARP target and endpoint score are carried
by

\[
\boxed{
 W_\Psi(x,n)
 =\frac{4\sqrt x}{n}-\frac3{\sqrt n},
}
\tag{L-91339.1
}

and

\[
\boxed{
 W_S(x,n)
 =\frac{5\sqrt x}{n}-\frac3{\sqrt n},
}
\tag{L-91339.2
}

for `n<=x`, with causal zero extension.

Indeed, summing against `mu(n)` gives

\[
 \Psi=L+2R=4\sqrt x\,B-3A
\]

and

\[
 2L+R=5\sqrt x\,B-3A.
\]

Both kernels are strictly positive on their support, and

\[
\boxed{
 W_S(x,n)-W_\Psi(x,n)=\frac{\sqrt x}{n}>0.
}
\tag{L-91339.3
}

## 2. Geometric child split

Let `p` be prime, put

\[
 r=p^{-1/2},
 \qquad B_p=1-r,
\]

and assume `n<=x/p`. Direct algebra gives

\[
\boxed{
 W_\Psi(x,n)
 =W_\Psi(x/p,n)
  +4B_p\frac{\sqrt x}{n},
}
\tag{L-91339.4
}

and

\[
\boxed{
 W_S(x,n)
 =W_S(x/p,n)
  +5B_p\frac{\sqrt x}{n}.
}
\tag{L-91339.5
}

For `x/p<n<=x`, the child kernels vanish and the parent kernels form a positive
activation frontier.

Thus, with `H_x(n)=sqrt(x)/n`,

```text
parent target
 = coefficient-one child target
   + 4 B_p H_x on the inner support
   + positive target frontier;

parent score
 = coefficient-one child score
   + 5 B_p H_x on the inner support
   + positive score frontier.
```

## 3. Exact payment of the hazard score deficit

The harmonic slack has pointwise score surplus

\[
\boxed{
 5B_pH_x-4B_pH_x=B_pH_x>0.
}
\tag{L-91339.6
}

The frontier has pointwise score surplus

\[
\boxed{
 W_S-W_\Psi=H_x>0.
}
\tag{L-91339.7
}

Consequently the child inherits the same coefficient—exactly one—in target and
score. All terms left at the current generation have nonpositive signed score
loss.

This is the source-level repair of `R-91307`: the survival and hazard pieces
must be recombined before canonical return. Their child coefficients add to

\[
 (1-p^{-1/2})+p^{-1/2}=1,
\]

and the apparently missing hazard score is precisely the local positive
harmonic surplus.

## 4. Positive measure version

Let `nu` be any finite positive source measure. Define

\[
 \mathfrak T_x(\nu)=\sum_{n\le x}\nu(n)W_\Psi(x,n),
\]

\[
 \mathfrak S_x(\nu)=\sum_{n\le x}\nu(n)W_S(x,n).
\]

Split `nu` into its inner and frontier restrictions at `x/p`. Equations
(L-91339.4)--(L-91339.5) give

\[
\boxed{
 \mathfrak T_x(\nu)
 =\mathfrak T_{x/p}(\nu_{\le x/p})
  +4B_p\sqrt x\sum_{n\le x/p}\frac{\nu(n)}n
  +\mathfrak T_x(\nu_{>x/p}),
}
\tag{L-91339.8
}

and

\[
\boxed{
 \mathfrak S_x(\nu)
 =\mathfrak S_{x/p}(\nu_{\le x/p})
  +5B_p\sqrt x\sum_{n\le x/p}\frac{\nu(n)}n
  +\mathfrak S_x(\nu_{>x/p}).
}
\tag{L-91339.9
}

Every measure on the right is positive. Subtracting,

\[
\boxed{
 [\mathfrak T_x-\mathfrak S_x](\nu)
 \le
 [\mathfrak T_{x/p}-\mathfrak S_{x/p}](\nu_{\le x/p}).
}
\tag{L-91339.10
}

Therefore the signed score loss obeys a coefficient-one one-child recurrence,
with favorable local slack and frontier.

## 5. Factor-54 specialization

For `p>=67`,

\[
 x/p<c_0x.
\]

Choosing the first rough scale factor therefore sends the sole inherited child
inside the next factor-54 endpoint. The harmonic slack and activation frontier
remain positive current-generation source packets.

This is stronger than the branching consumer: for any positive source measure
already expressed in the kernel class of Section 4, the rough split has one
child and coefficient one.

## 6. What remains

The finite small-prime/parity forcing must be represented as a positive measure
`nu` in the kernel class used above, together with the interval/butterfly packets
already resident on the branch. Scalar positivity of the finite forcing alone
does not provide that representation.

The common Hilbert endpoint port remains available for the finite signed
observation corrections, but it is no longer needed to subsidize the hazard
score ledger.

## 7. Proof boundary

```text
positive target kernel W_Psi                    EXACT
positive endpoint-score kernel W_S              EXACT
coefficient-one geometric child split           EXACT
positive harmonic score surplus                 EXACT
positive frontier score surplus                 EXACT
one-child score-loss recurrence for nu>=0       EXACT
factor-54 child contraction                      EXACT
positive-kernel representation of finite forcing OPEN / SOURCE TYPING
full reset synthesis                             OPEN / RH-BEARING
Riemann Hypothesis                               UNPROVEN
```
