# X-23003 — Shell, digital, and parity-comb algebra

This standard-library exact regression checks the finite coefficient algebra of
`L-23008` and `L-23010`--`L-23012`.

It verifies through a declared endpoint:

- the exact fixed-ratio shell transfer from `d=1/2` to `c=2/3`, with rational
  cutoffs and floors retained;
- `sum_(n<=N)(1-v_2(n))=s_2(N)`;
- the bit-layer factorization of the binary digit coefficient;
- `c_2*b_2=delta_1-2delta_2`;
- `lambda_2*b_2=delta_1-3delta_2+2delta_4`, where
  `lambda_2(n)=(-1)^(n+1)`;
- `sum_(n<=N)b_2(n)=M(N)-M(floor(N/2))`.

It is a finite algebraic regression only. It proves no asymptotic shell bound,
no coercivity theorem, and no statement about RH.
