# L-97400 — The literal rough-history source has a finite, parity-covariant, one-owner ledger

Claim ID: `L-97400`  
Status: **PROVED EXACT INTERFACE THEOREM**  
Created: 2026-08-18  
RH status: unproved

Let

`P_61=product_(p<=61) p`.

Every squarefree source index has the unique factorization

`k=d p_1...p_t`,

where `d|P_61` and `67<=p_1<...<p_t`. The ordered rough history is `h(k)=(p_1,...,p_t)`. If `S(E,O)=(O,E)` denotes the parity swap, the literal source at endpoint `X` has the finite owner expansion

`N_X = direct_sum_(ell in L_X) omega_ell S^{|h_ell|} P_ell`,

with `omega_ell>=0`. Every original occurrence retains exactly

```text
coefficient magnitude   k^(-1/2),
activation              X/k,
signed character        mu(d)(-1)^|h| = mu(k),
least unused rough owner,
activation side at every real knot.
```

## Proof

Moving a rough prime `p|k` from the source index into the history sends `(X,k)` to `(X/p,k/p)`. It preserves activation and coefficient magnitude because

`(X/p)/(k/p)=X/k`

and

`p^(-1/2)(k/p)^(-1/2)=k^(-1/2)`.

It swaps the two parity channels once. Unique factorization supplies a unique ordered history and first owner. For fixed `X` the root source is finite and every source index contains at most `floor(log X/log 67)` rough factors, so no projective limit is needed.

Any grouping map acting diagonally on parity space commutes with `S`. Any signed row or scalar observation anti-commutes with one swap. Therefore

`O_l G S^m = (-1)^m O_l G`.

This proves the complete atomwise conservation identity before any Hall or physical observation. It does not assert positivity of a swapped terminal packet.

## Atomwise conservation under the formal causal identity

For active rough primes `p_i`, put

```text
r_i=p_i^(-1/2),
s_0=1,
s_i=product_(h<=i)(1-r_h),
lambda_i=r_i s_(i-1),
alpha_i=r_i lambda_i.
```

Then

`P=s_k P + sum_i lambda_i(P-r_i U_iP_i) + sum_i alpha_i U_iP_i`

is an exact linear identity because `s_k+sum lambda_i=1` and `alpha_i=r_i lambda_i`. This identity must be interpreted in the free labelled source space: the `alpha_i` children, current differences, true source terms, reserves, and ownership transfers remain distinct labels until cancellation. An oriented difference is not separately a positive physical row.

For every original atom, expanding and cancelling the `-lambda_i r_i` and `+alpha_i` terms leaves coefficient one on the parent occurrence. Thus the fully expanded root marginal is the literal native marginal, not a reweighted rough lift. Applying the scalar observation only after completed parity gives exactly

`R_X=5c_X(2)+3c_X(3)`.

```text
finite source expansion             PROVED EXACT
unique ownership                    PROVED EXACT
activation and magnitude            PROVED EXACT
cumulative parity                   PROVED EXACT
formal coefficient conservation     PROVED EXACT
terminal positivity                 NOT ASSERTED
```
