# R-102725 — The positive outer-ray resolvent is one-way

Claim ID: `R-102725`  
Status: **PROVED SOURCE-BLIND CONVERSE FIREWALL**  
Created: 2026-08-22  
Depends on: `L-102740`  
RH status: **unproved**

The exact identity

\[
\mathcal L=\frac52(D+3/10)Y
\]

has a positive causal inverse, so negative mass of `mathcal L` controls negative
mass of `Y`.

The converse is false without arithmetic information.

On a fixed interval, take

\[
Y_N(u)=\sin(Nu).
\]

Then

\[
\mathcal L_N(u)
=
\frac52
\left[N\cos(Nu)+\frac3{10}\sin(Nu)\right].
\]

The negative mass of `Y_N` on each complete period is bounded independently of
`N`, whereas the negative mass of `mathcal L_N` is comparable to `N`.
Multiplying by a fixed smooth cutoff changes only bounded endpoint terms.

Therefore

\[
\int(Y)_-=Y^{o(1)}
\not\Longrightarrow
\int(\mathcal L)_-=Y^{o(1)}
\]

by a source-free differential argument.

The remaining programme may use the positive resolvent in the direction

```text
outer-ray negative mass -> critical variation,
```

but cannot recover the outer-ray estimate from critical variation without
additional native-source cancellation.