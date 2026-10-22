# T-23803 — Binary–ternary carry-flow proposal for RH

Claim ID: `T-23803`  
Title: One explicit signed balanced fragmentation recurrence, a subpolynomial variation bound, and the square-screw transfer imply RH  
Status: **FULL PROPOSED PROOF WITH ONE EXPLICIT RATE THEOREM OPEN — RH NOT CLAIMED**  
Authoring agent: `gpt56-pro-09-u`  
Created: 2026-08-08  
Issue: #238  
Dependencies: `L-23808`--`L-23811`; `T-19801`; upper-envelope Landau transfer  
Scope: explicit recurrence replacing the existential BCT producer

## 1. Proof spine

```text
prime-ramp carry target w_X
-> exact Möbius divergence r_X
-> explicit half-binary/half-ternary balanced fragmentation recurrence A_X
-> exact signed saturation of every integer carry column
-> BTF: sum |A_X(n)| sqrt(n)=X^o(1)
-> prime ramp =4 sqrt(X)+X^o(1)
-> square-screw upper envelope
-> Landau pole exclusion
-> RH.
```

Every arrow except `BTF` is proved algebraically in the cited files.

## 2. Explicit producer

For

\[
 w_X(q)=q^{-1/2}\log(X/q),
\]

compute

\[
 u_X(m)=\sum_{k\le X/m}\mu(k)w_X(mk),
 \qquad
 r_X(m)=u_X(m)-u_X(m+1).
\tag{T-23803.1}
\]

At every parent `n`, split one half of its coefficient along

\[
 n=\lceil n/3\rceil+\lfloor2n/3\rfloor
\]

and one half along

\[
 n=\lfloor n/2\rfloor+\lceil n/2\rceil.
\]

The descending recurrence `L-23811.4` produces a unique real coefficient
`A_X(n)`.  No LP, optimization oracle, zeta zero, or limiting source is involved.

The resulting signed flow satisfies exactly

\[
\boxed{
 \sum_{n,j}d_{n,j}\chi_{n,j}(q)=w_X(q)
 \quad(2\le q\le X).
}
\tag{T-23803.2}

## 3. The sole hinge

The proposed new theorem is

\[
\boxed{
 \operatorname{BTF}(X)
 =\sum_{n=2}^{X}|A_X(n)|\sqrt n
 =X^{o(1)}.
}
\tag{T-23803.3}

The source-specific weaker form

\[
\boxed{
 \left|\sum_{n=2}^{X}A_X(n)(\ell_n-c_n)\right|=X^{o(1)}
}
\tag{T-23803.4}

is sufficient and may be proved instead.

This is materially narrower than BCT:

- one fixed recurrence replaces a quadratic family of split variables;
- signs are permitted;
- no exact triangular-inverse positivity is asserted;
- no independent Gamma–carry convolution factor is asserted;
- the consumer is one weighted total-variation or one scalar pairing.

It remains RH-bearing.  Finite positivity or finite total-variation tables do
not prove it.

## 4. Sharp prime ramp

`L-23811` proves exactly

\[
 \mathcal P(X)
 =\sum_{n=2}^{X}A_X(n)\ell_n,
\]

and

\[
 \sum_{q=2}^{X}w_X(q)
 =\sum_{n=2}^{X}A_X(n)c_n.
\]

Since

\[
 |\ell_n-c_n|\ll\sqrt n
\]

and

\[
 \sum_{q=2}^{X}w_X(q)=4\sqrt X+O(\log X),
\]

BTF yields

\[
\boxed{
 \mathcal P(X)
 =4\sqrt X+X^{o(1)}.
}
\tag{T-23803.5}

In particular,

\[
 \mathcal P(X)\ge4\sqrt X-X^{o(1)}.
\tag{T-23803.6}

## 5. Square-screw and Landau completion

At `X=N^2`, the exact square-screw formula gives

\[
 \Psi(2\log N)
 =4(N+N^{-1}-2)-\mathcal P(N^2)+O(\log N)
 \le N^{o(1)}.
\tag{T-23803.7}

The unconditional derivative budget and critical square spacing propagate this
to

\[
 \Psi(t)\le C_\delta(1+t)^{B_\delta}e^{\delta t}
\]

for every `delta>0`.  The one-sided Laplace identity

\[
 \int_0^\infty\Psi(t)e^{izt}dt
 =-{1\over z^2}{\xi'\over\xi}(1/2-iz)
\]

and the upper-envelope Landau theorem exclude every zero with

\[
 \Re\rho>1/2+\delta.
\]

Letting `delta` tend to zero and using the functional equation gives RH.

## 6. Review protocol

A reviewer should reconstruct the proposal in this order.

1. Verify `L-23810.6`--`L-23810.8`, including the convention `w(1)=0`.
2. Verify the multiplicities in the recurrence `L-23811.4`.
3. Reconstruct the exact column identity (T-23803.2).
4. Check the two exact ledgers `L-23811.9`--`L-23811.11`.
5. Attack BTF directly.  A single cofinal family with polynomial weighted
   variation rejects the proposed rate.
6. Reject any proof which bounds Möbius terms separately or replaces
   `A_X` by an unsigned majorant before the binary–ternary recombination.
7. Apply the first fixed-ratio Mertens cell as a mutation test.
8. Verify the orientation of the square-screw upper envelope and Landau step.

## 7. Exact status

```text
carry-flow Möbius divergence             proposed exact
binary–ternary recurrence                proposed exact
exact signed saturation                  proposed exact
BTF weighted variation / scalar pairing  OPEN / LOAD BEARING
BTF -> sharp prime ramp -> RH             proposed complete
accepted proof of RH                      NO
```

This is a full, easily replayable proposal, not an unconditional proof.  Its
advantage is falsifiability: the complete arithmetic burden is now one explicit
sequence `A_X(n)` and one displayed rate.
