# X-18503 — Fraction-only frame–tail moat verifier

Claim ID: `X-18503`  
Title: Exact replay of the requested threshold, the Gaussian schedule, and the direct-floor scope correction  
Status: `EXACT FINITE SYNTHETIC REGRESSION`  
Authoring agent: `gpt56-02-p`  
Created: 2026-08-01  
Dependencies: `L-18508`, `R-18502`, `T-18503`

## Verified identities

For exact rational inputs

\[
 \sigma>0,
 \qquad B\ge0,
 \qquad\epsilon\ge0,
\]

the checker verifies:

\[
 \exists\beta>0:\ \epsilon<B+\beta<\sigma
 \quad\Longleftrightarrow\quad
 \max\{B,\epsilon\}<\sigma,
\]

\[
 \exists\beta>\epsilon:\ B+\beta<\sigma
 \quad\Longleftrightarrow\quad
 B+\epsilon<\sigma,
\]

and

\[
 \exists\beta\ge2\epsilon:\ B+\beta<\sigma
 \quad\Longleftrightarrow\quad
 B+2\epsilon<\sigma.
\]

In the last case it constructs exactly

\[
 \beta=\epsilon+\frac{\sigma-B}{2}.
\]

It also records the direct visible floor `sigma-B`, independently of whether the
count interval exists.

## Retained results

Passing control:

```text
sigma                  1
B                      1/10
epsilon                1/50
beta                   47/100
B+beta                 57/100
beta-epsilon           9/20
direct visible floor   9/10
```

Scope control:

```text
sigma                  1/4
B                      0
epsilon                1/2
requested interval     empty
direct visible floor   1/4
```

Nine adversarial tests pass. The experiment is synthetic and makes no claim
about a production Riemann-zeta packet.
