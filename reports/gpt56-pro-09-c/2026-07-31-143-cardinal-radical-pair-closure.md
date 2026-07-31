# Requested pair closed on an exact cofinal cardinal–radical packet

Agent: `gpt56-pro-09-c`  
Date: 2026-07-31  
Issue: #166  
Draft PR: #168  
Main theorem: `T-14306`

## Result

For every finite selected simple real-zero set `Z` and every finite exact global
radical packet `R_m`, define

```text
A_(Z,L)=V_Z P_L C_Z,
C_tilde_(Z,L)=P_L C_Z A_(Z,L)^-1,
B_(m,Z,L)=V_Z P_L R_m,
K_(m,Z,L)=P_L R_m-C_tilde_(Z,L) B_(m,Z,L).
```

Because `V_Z C_Z=I`, the evaluation matrix tends to the identity and is
invertible for large support. The two corrected finite maps satisfy exactly

```text
V_Z C_tilde_(Z,L)=I,
V_Z K_(m,Z,L)=0.
```

The supported packet

```text
U_(m,Z,L)=Ran C_tilde_(Z,L) + Ran K_(m,Z,L)
```

is a direct sum and

```text
U_(m,Z,L) intersect ker V_Z = Ran K_(m,Z,L).
```

## Quadratic cancellation

Put

```text
Delta_C=C_tilde-C_Z,
E=K-R_m.
```

Both exact identities are load bearing:

```text
V_Z Delta_C=0,
Q_W(R_m b,x)=0.
```

The Xi-cardinal decomposition and radicality therefore give

```text
Q_W(C_tilde a,C_tilde b)
 = <a,b> + Q_W(Delta_C a,Delta_C b),

Q_W(Kb,Kb)=Q_W(Eb,Eb),

Q_W(C_tilde a,Kb)=Q_W(Delta_C a,Eb).
```

Thus the cardinal error is quadratic, the radical error is quadratic, and the
mixed error is bilinear in the two discarded tails.

## The two requested limits

For fixed finite data, Xi-cardinal tails and Hermite arithmetic-radical tails
are superexponentially small in the logarithmic support. The complete Hardy
complement floor loses only an ordinary exponential factor. Therefore

```text
||(I-P_L) C_Z|| -> 0,

inf_(0!=f in U_(m,Z,L), V_Z f=0)
 Q_W(f,f)/||f||_G^2 >= -epsilon_(m,Z)(L),

epsilon_(m,Z)(L)->0,
```

and the complete squared Schur loss tends to zero.

No uniform lower bound on `|Xi'(gamma)|` is needed. For any growing finite zero
sets and radical ranks, choose the support after freezing each finite packet.
A diagonal sequence makes the tail, zero-kernel floor loss, and Schur loss all
at most `2^-j`.

## Exact replay

`X-14315` checks the finite algebra using only integers and
`fractions.Fraction`. The retained globally indefinite model certifies

```text
C_tilde = (1,0,1/8,0)^T,
K       = (0,1,19/160,0)^T,
Schur-corrected low block >= -(1/62) packet Gram.
```

Eight adversarial tests pass. Proof-object SHA-256:

```text
afe08c8b34ce1b1b8339d213ed306e2b0b26f17fc9a16a371c32b5c3a7795cc5
```

## Exact scope correction

The result closes the pair for the packet it constructs. It does not prove that
this packet contains every dangerous low-symbol direction.

If `U_L` is instead prescribed to be a form-dense complete dangerous packet,
the second requested estimate is equivalent to the substantive RH positivity
gate. Under false RH, applying the exact cardinal remainder projector to a
negative Weil witness preserves zero evaluations and makes its quadratic value
no larger. The first tail limit then localizes that negative kernel direction.

The remaining theorem for RH is consequently a **capture/saturation theorem**:
prove that the constructed exact cardinal–radical packet accounts for the full
low index, for example by the weighted-deficit trace margin or the finite
visible Schur saturation already isolated on PR #163.
