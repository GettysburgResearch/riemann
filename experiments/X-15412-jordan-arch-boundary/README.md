# X-15412 — Exact Jordan/archimedean/boundary regression

Status: exact finite rational algebra  
Agent: `gpt56-05-l`  
Claims: `L-15425`--`L-15427`, `R-15405`, `T-15410`  
Issue: #180

## Checks

The checker uses the exact specialization `omega=1/2`, for which
`J_(2 omega)=J_1=phi`, and verifies:

1. the Jordan Stinespring norm identity on six parent integers;
2. the divisor conditional expectation and exact carré du champ at `n=12`;
3. the two-positive-channel archimedean algebra `g=b-v`, `ell=b+v`;
4. equality of the beta and Volterra moments at the gamma-zero boundary;
5. the Hardy Cauchy derivative/endpoint identity;
6. the pole-zero finite limit and divergent positive-majorant coefficient.

Retained exact values include

```text
Jordan conditional mean       1/9
Jordan conditional variance   961/648
archimedean score              1/3
Cauchy Gram                    15/19
endpoint derivative sum        1
signed pole-zero limit         15/28
positive pole coefficient      15/14
```

## Reproduction

```bash
python verify.py certificates/synthetic.json \
  --output results/synthetic-verification.json
python -m unittest discover -s tests -v
```

## Proof boundary

The checker validates finite algebra only. It does not prove the regularized
full-`Phi` Mellin/Volterra metric identity and therefore does not prove
`T_omega^*T_omega=I` or RH.
