# Companion-corona attack on low-order descent

T-105222 removes adjacent-derivative poles by finite interpolation, but its
boundary norm can blow up under node coalescence.  T-105230 replaces that
interpolant by the canonical companion

```text
G_(k,delta)=F_(k+1)+i delta F_k.
```

The fixed field

```text
F_(k+1)/F_k
+ 2 lambda F_(k-1)/F_k
+ lambda^2 F_(k-1)^2/[F_k G_(k,delta)]
```

has the desired square-defect residues and only simple companion corrections.
The lower companion zeros are counted exactly by the nonreal-pair index of
`F_k`.  The low-order Levinson problem is thereby reduced to a one-sided
boundary-flux plus companion-pole-amplitude estimate `CIBF105230`.

This is a structural reduction, not a 90% theorem.  The next step is to use
the positive-Fourier companion and Pick/phase-velocity estimates to bound the
negative companion-pole charge at k=1,2,3.
