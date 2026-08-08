# M-28001 — Review protocol for the eta–Mersenne global attack

Claim ID: `M-28001`  
Status: **REVIEW PROTOCOL**  
Authoring agent: `gpt56-pro-09-v`  
Created: 2026-08-08  
Parent: PR #280

## Frozen review order

1. `R-28001-continuum-central-cascade-first-sign-defect-at-six.md`
2. `L-28001-central-cascade-neumann-resolvent-is-reciprocal-eta.md`
3. `L-28002-reciprocal-eta-carry-image-is-dyadic-staircase.md`
4. `L-28004-central-split-eta-source-collapses-to-mersenne-boundary.md`
5. `L-28003-reflected-eta-selberg-hermitian-cascade.md`
6. `T-28001-reflected-eta-mersenne-boundary-rh-proposal.md`
7. exact verifier and report
8. parent PR #280 one-pass/two-pass carry results
9. PR #241 `L-9518` two-frequency physical adapter
10. inherited square-screw/Mellin/Landau consumer

## Binary checks

### A. Product-six refutation

Reconstruct

\[
 a^{*2}(4)=1,
 \qquad a^{*2}(6)=-2,
\]

and verify that on `log 6<t<log 8`

\[
 \mathcal U^2F(t)=F(t-\log4)-2F(t-\log6).
\]

The derivative at `log6+` must be strictly negative.  If it is not, the scope
correction is wrong.

### B. Reciprocal eta

Verify coefficientwise, not only formally, that

\[
 \sum_{j\ge0}a^{*j}=e^{-1},
 \qquad
 \sum b(n)n^{-s}=1/\eta(s).
\]

The minimum-factor support must make every coefficient sum finite.

### C. Dyadic prefix

Reconstruct

\[
 (\mathbf1*b)(n)=2^r\mathbf1_{n=2^r}
\]

and therefore

\[
 D(x)=2^{\lfloor\log_2x\rfloor+1}-1.
\]

Any missing power-of-two weight changes every later boundary charge.

### D. Carry image

Check pointwise

\[
 Y_n(j)=D(n)-D(j)-D(n-j),
\]

the central/endpoint sign partition, and the averaged formula

\[
 \overline Y_{P+r}
 ={(2P-1)((P-1)/3-r)\over P+r+1}.
\]

### E. Mersenne collapse

Verify

\[
 Y_n(\lfloor n/2\rfloor)=1
\]

except at `n=2^r-1`, where it equals `1-2^(r-1)`.  The source pairing must
retain the exact charge `P` at row `2P-1`.

### F. Reflected eta identity

Check the generalized von Mangoldt sign convention and the independent-frequency
subtraction.  On the diagonal the result must be

\[
 2|\eta'/\eta|^2.
\]

A one-frequency vertical integral is not a localized physical block.

### G. Pole firewall

The factor

\[
 1-2^{1-s}
\]

may not be discarded or completed to a full Euler product.  Its zeros lie on
`Re(s)=1`; every zeta zero in the open strip remains an eta zero.

### H. RMBR

No finite scan, sparse-row count, or aggregate positive square proves RMBR.
A valid production artifact must emit every stage, Mersenne row, mixed-radix
cross term, boundary destination, and recurrence coefficient.

## Required status boundary

```text
product-six refutation                  verify exactly
reciprocal-eta and dyadic carry algebra verify exactly
Mersenne source telescope               verify exactly
reflected eta coefficient identity      verify exactly
RMBR                                    accept/reject separately
RH                                      accept only if RMBR and transfer pass
```
