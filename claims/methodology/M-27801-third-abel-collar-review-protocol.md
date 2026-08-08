# M-27801 — Third-Abel collar review protocol

Claim ID: `M-27801`  
Status: **METHODOLOGY / FAIL-CLOSED REVIEW PROTOCOL**  
Created: 2026-08-08  
Target: `L-27801/T-27801`

## Review objective

Review the proposed source-specific implication

```text
third cumulative producer kernel + exact critical endpoint collar
-> binary–ternary producer positivity
-> sharp prime ramp
-> RH.
```

Do not replace it by a stronger generic positivity statement: two such statements are exactly false.

## Frozen mutations

Every implementation or proof must reproduce:

```text
X=8, basis target q=4:              A(3)  = -1
X=60, second-prefix Q=59:           A(11) = -13/16
```

These are exact Fraction witnesses from `R-27801/X-27801`.

## Mandatory algebra checks

1. Reconstruct `U(m)=sum mu(k)w(mk)` with the exact finite endpoint.
2. Reconstruct `r(m)=U(m)-U(m+1)`.
3. Reconstruct the descending half-binary/half-ternary recurrence with repeated central children counted twice.
4. Verify the third cumulative definition
   ```text
   S_X(n,Q)=sum_(q<=Q) binom(Q-q+2,2) K_X(n,q).
   ```
5. Verify the exact third-Abel identity with zero extension beyond `X`.
6. Keep the last three source differences; do not invoke continuous complete monotonicity across the artificial zero extension.

## TACP-I review gate

A proof of all-scale third-prefix positivity must be symbolic or inductive. Finite scans, even exact scans to very large `X`, are evidence only.

Any induction must expose where Möbius signs are recombined. Termwise positivity of the raw Möbius forcing is not expected and is not a valid hidden hypothesis.

Review quotient-cell boundaries, repeated children, parity/ternary residue cases, and the node-one conservation separately.

## TACP-B review gate

The endpoint collar must be an exact source-bound statement. Acceptable forms include:

- a fixed finite collar with rigorous interval inequalities uniform in `X`;
- a polylogarithmic collar with a proved recurrence;
- a direct exact inequality for the complete collar sum.

Reject:

- dropping `w(X+1..X+3)=0` boundary terms;
- replacing the collar by an `O(1/X)` statement without a sign moat;
- assuming third differences remain positive after zero extension.

## RH-firewall checks

The proof must retain the actual target

```text
w_X(q)=q^-1/2 log(X/q).
```

It must also retain the inherited dyadic / fixed-ratio Mertens mutation and the reviewed square-screw/Landau normalization. A proof for arbitrary smooth decreasing targets is not required; a proof obtained by absolute Möbius bounds is suspect because it would erase the reciprocal-zeta source.

## Status vocabulary

```text
exact finite identity                  PROVED / VERIFIED when replayed
finite third-prefix scan               FINITE RECONNAISSANCE
TACP-I                                 OPEN until all-scale proof
TACP-B                                 OPEN until uniform proof
producer positivity                    OPEN until TACP or another proof
RH                                     UNPROVED
```
