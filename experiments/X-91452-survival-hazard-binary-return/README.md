# X-91452 — Survival/hazard binary canonical return

The replay checks:

1. positivity of the survival matrix `C_p` and hazard matrix `H_p`;
2. exact target partition `t(C_p+H_p)=t`;
3. exact score surplus `s(C_p+H_p)=s+(0,r(1-r))`;
4. the minimal pure-reserve hazard subsidy;
5. the target-null correction matrix;
6. three-prime sequential target and score telescopes;
7. positivity and normalization of sample branch target fractions.

The replay checks finite algebra only. It does not prove the ordinary/radix-four
row lift or RH.
