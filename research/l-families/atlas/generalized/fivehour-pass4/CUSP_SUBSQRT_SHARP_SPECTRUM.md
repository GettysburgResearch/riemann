# Sharp native cusp spectrum below the square-root scale

Status: preregistered analytic theorem target; independent review required.
No period-zero, quotient, or RH conclusion.

Authoring parent: `09ca23951`.  Retain the exact notation and normalization
of the accepted K/L packets.  In particular `nu=k-1`, `T_k` is the
Petersson compression of the finite part `E_0=h+r_0`, and

\[
 m_{k,J}={\nu\over24J}-{1\over2}\log{\nu\over4\pi J}+c_0.
\]

## Frozen target

For every sequence of even weights and indices

\[
 1\le J=J_k=o(\sqrt{k}),
\]

prove the strict refinement of Theorem L

\[
 \boxed{\lambda_J(k)=m_{k,J}+o(1).}                 \tag{S1}
\]

The intended new step is to remove L's fixed `R_1` upper loss.  On the
coefficient flag `W_J`, use full-cusp Parseval to split the `n=J` Fourier
mass from `n>J` and the compact mass.  The radial conditional-Gamma symbols
must satisfy

\[
 \mu_{\nu,4\pi J}-\mu_{\nu,4\pi(J+1)}\longrightarrow\infty,    \tag{S2}
\]

uniformly in this range.  Any mass outside the first Fourier mode then pays
an unbounded radial loss.  For the retained `n=J` mass, prove that it lies
above a height tending to infinity, where the nonconstant term `r_0`
vanishes exponentially.  The loss must absorb all compact and cross-term
contributions without assuming the Fourier pieces are orthogonal below
height one.

## Stop conditions

- Preserve the fixed-width L theorem if the compact/cusp bookkeeping does
  not yield a uniform `o(1)`.
- Do not claim S1 for the full `J=o(k)` range.
- Do not infer the first correction to a period zero; the exact-period
  analytic remainder is a separate term.
- Do not infer scalar quotient noncancellation or interlacing.
