## T105430 addendum — Xi critical-sign rigidity

The global Xi boundary gate collapses once the complete critical sign is retained.

For every fixed derivative ratio

```text
m_r(z)=Xi^(r)(z)/Xi^(r+1)(z),
```

completed-zeta Stirling asymptotics prove an unconditional positive safe half-plane

```text
Im m_r(x+iy)>0,  y>=H_r.
```

If every zero of `Xi^(r+1)` is real, its paired Hadamard product and the fixed-strip gamma decay give cofinal vertical sides with

```text
sup_side |m_r| <= exp(O(log X loglog X)).
```

If, additionally, every critical residue is nonpositive, the bottom edge of the strip is nonnegative in the limiting sense. The vertical-side harmonic measure is `exp(-pi X/H)`, which beats the side growth. A finite-strip Lindelof argument therefore gives

```text
Im m_r(z)>0  in the complete upper half-plane.
```

Hence `m_r` is Pick, `Xi^(r)` is real-rooted, and every boundary Loewner/Stieltjes/source-capacity matrix is positive. The Herglotz affine coefficient vanishes because `m_r(iy)=O(i/log y)`, so the complete source measure is exactly the positive critical-atom measure.

Thus, globally for the Xi derivative class,

```text
CRVH105330
  -> Pick
  -> exact source-critical saturation
  -> BRP/OASH/OSCC
  -> real-rootedness.
```

At `r=0`, the complete critical sign is an exact RH-equivalent criterion. The former remote quarter-arc phase gate is not independent under the complete sign.

Binding firewall: `z^4-z^2+1` has all critical points real and positive imaginary-axis ratio, but its outer residues are `3/16>0` and its roots are nonreal. The residue orientation remains the irreducible open input.

```text
safe half-plane                              PROVED / REVIEW
subexponential good sides                    PROVED CONDITIONAL / REVIEW
critical sign -> Pick and real-rootedness    PROVED CONDITIONAL / REVIEW
exact source saturation                      PROVED CONDITIONAL
complete low-Xi critical sign                OPEN / RH-EQUIVALENT
RH                                            UNPROVEN
```

Replay:

```text
PASS_X_105430_CRITICAL_SIGN_RIGIDITY
b2924d153ad3b49690f7329228d2445893bbfb7437e7cd77bc320e6ac9b69cb4
17 checks
RH_UNPROVEN
```
