# R-91656 — The old GRRT/CFFP frontier is superseded by the direct native-row reset

Claim ID: `R-91656`  
Status: **SUPERSESSION AND REVIEW-SCOPE RECORD**  
Created: 2026-08-14

The standalone packet `SPP-91661` correctly marked `GRRT` and `CFFP` open for
its two proposed root architectures. Those open statements are not silently
renamed as proved.

The new route changes the architecture:

1. it uses the exact native equality row `c_X`, whose ordinary and detail
   responses are exactly `w_X` and `Omega_X`;
2. it proves a positive source-disjoint Hall realization of that same row;
3. it subtracts the complete canonical fixed-67 child row and inserts an
   arbitrary feasible child at the same row indices;
4. it displays the ordinary and detail residual inequalities after the complete
   current row is summed;
5. it pays literal score through the global fixed-67 inequality `L-91666`;
6. it charges outer mismatch, collar, terminal, and corrected port once as
   current-only packets.

Therefore the old Hall-disintegration `GRRT` and the two-label `CFFP` are no
longer antecedents of the proposed conclusion. The reviewer objections to the
old `L-91659` remain valid and permanent.

```text
old formal complement root proof          rejected
old GRRT/CFFP route                       retained as alternate open research
new direct native-row root                review target L-91667/T-91654
RH                                        not accepted before review
```
