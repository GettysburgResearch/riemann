# M-20301 — Proof-producing Möbius-tail pipeline

Claim ID: `M-20301`  
Status: `PROPOSED METHODOLOGY`  
Authoring agent: `gpt56-03-p`  
Created: 2026-08-01

## Input

At one support level provide:

1. the exact complete selected-real-zero kernel basis \(J\);
2. its compact multiplicative support \([a,b]\);
3. the exact metric Gram \(G_K\);
4. the positive ambient block \(C\) and kernel cross \(Z_K\);
5. a Möbius cutoff \(N\) with \(Na>b\);
6. a normalized source corrector \(\psi\subset(0,a)\);
7. exact or directed Weil-form producers.

## Construction

For every basis column \(h\):

```text
g(u) = u^(-1/2) h(u)
f_N(x) = sum_(n<=N) mu(n) g(nx)
         - [sum_(n<=N) mu(n)/n] [integral g] psi(x)
r_N = E(f_N)
t_N = r_N-h
```

The verifier requires:

```text
f_N(0)=0
integral f_N=0
r_N=h on [a,b]
support(t_N) subset (0,a)
```

## Two independent residual producers

Physical:

```text
t_N(u)
 = u^(1/2) sum_(k>N) A_N(k) g(ku)
 - correction,
A_N(k)=sum_(d|k,d<=N) mu(d).
```

Mellin:

```text
hat(t_N)(z)
 = [zeta(s)P_N(s)-1] hat(h)(z)
 - pole_correction,
s=1/2-iz.
```

Both must bind the same Fourier/Mellin convention and overlap after directed
evaluation.

## Final gate

Assemble the exact/directed matrix upper bound

\[
|Q_W(T_N,T_N)|_{\rm op}
+
\|C^{-1/2}Z_KJ\|_{\rm op}^2
\le\eta.
\]

Promotion requires the complete coefficient-space LMI

\[
\eta G_K-H_{\rm tail}-H_{\rm cross}\succeq0.
\]

A selected vector, midpoint eigenvalue, or entrywise tail estimate does not
replace the operator inequality.

## Mandatory zero audit

At every certified zero used in the proof object, verify

\[
\widehat t_N(z_\rho)=-\widehat h(z_\rho).
\]

A producer that instead reports a small residual at a nonzero target evaluation
has a normalization, pole-correction, or source-constraint bug.

## Cofinal scheduler

At level \(j\):

1. construct the actual complete packet;
2. extract a finite simple-line frame;
3. build the exact graph kernel;
4. choose \(N_j a_j>b_j\);
5. assemble the physical and Mellin tail matrices;
6. increase arithmetic precision until the matrix sign is decided;
7. record \(\eta_j\);
8. promote only an analytic theorem proving \(\eta_j\to0\), never an
   extrapolated finite trend.
