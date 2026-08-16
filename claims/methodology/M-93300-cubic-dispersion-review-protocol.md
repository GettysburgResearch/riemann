# M-93300 — Hostile review protocol for the cubic shell and balanced dispersion packet

Status: **NORMATIVE REVIEW PROTOCOL**  
Created: 2026-08-16  
Frozen base: PR #498 at `6cc0da2fa5711017e260ebdcea4ba8c22e453288`

## Review order

1. `L-93300`: reconstruct the PR #498 centered cubic identity, normalization,
   interpolation and Mellin pole audit.
2. `R-93300`: enforce the magnitude-only and hidden-RH firewall.
3. `L-93301`: check the scale-four source reindexing and large-prime shell.
4. `L-93302`: check both Mellin moments and all four grid residue formulas.
5. `L-93303`: reconstruct Vaughan's identity, the three Type-I bounds, the
   grouped coefficient \(a_U\), and the low-product estimate.
6. `L-93304`: verify the Gaussian Fourier transform and Calderón formula.
7. `T-93305`: confirm that BCD is displayed as open and that every earlier
   estimate is unconditional.
8. Replay `X-93300`, run mutations, and verify both checksum ledgers.

## Mandatory interfaces

### Analytic spine

```text
predecessor N-j-1;
mean-zero normalization;
|A|^2 <= N V / 180;
Khat(s)=(s-1)/(3(s+1)(s+2)(s+3));
source factor 1-4^(1-s);
O(1) integer-real interpolation;
all off-line poles retained.
```

### Arithmetic reduction

```text
F=K-4K(4.) on [0,1/4];
small prime bases <=sqrt(N) paid once;
four-adic gauge paid once;
two Mellin moments exact;
Vaughan signs +,+,-,+ exact;
a_U(m)=sum_(d|m,d>U) mu(d);
m,l both in [N^(1/3),N^(2/3)];
low products m l <=N^(3/4) paid;
only the displayed balanced form remains.
```

### First-Hermite bridge

```text
Fourier convention fixed;
h_q transform equals 4 sqrt(pi) q^(3/2) t^2 exp(-q t^2);
Calderon integral uses line Re(s)=1;
no critical-line one-carrier theorem imported.
```

## Immediate rejection conditions

Reject the packet if any of the following occurs:

1. one PR #498 analytic identity fails;
2. the scale-four source is missing the separate four-adic gauge;
3. a higher prime power with base greater than \(\sqrt N\) is retained;
4. either Mellin moment is nonzero;
5. one grid residue formula fails;
6. the Vaughan decomposition fails on a finite exact fixture;
7. the low-product estimate uses Möbius cancellation;
8. BCD is marked proved;
9. a fixed-power PNT, Mertens square-root estimate, CPBD, or First-Hermite
   pointwise positivity is imported;
10. a checksum or hostile mutation fails.

## Computation boundary

The replay is exact finite rational algebra.  It is not a prime-distribution
experiment and does not authenticate BCD or RH.  No large endpoint scan,
zero computation, formal build, or optimization campaign is required.
