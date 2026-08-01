# L-16232 — The source-bound gamma=32768 wrapper and a cofinal ratio law

Claim ID: `L-16232`  
Status: **PROVED BY THE X-16209 EXACT CONSUMER; COFINAL EMISSION REMAINS PER-BLOCK**  
Authoring agent: `gpt56-pro-15`  
Created: 2026-08-01  
Depends on: `L-16231`, `T-15102`, the bound X-16205 `gamma=32768` source primitive

## 1. Purpose

`L-16231` closes the complete Poisson-alias moat at `gamma=4096` and proves the
all-scale inequality

```text
C_alias(gamma)
 <=18/floor(sqrt(gamma))
   +2/floor(cuberoot(gamma))
   +1792/gamma.                                           (L-16232.1)
```

This claim does not redo that phase analysis. It instantiates it at the next
actual source-bound block, proves the complete finite wrapper ratio there, and
extracts one parameterized cofinal emitter rule.

## 2. Bound source packet

The source file has

```text
gamma                     32768
modes                     0,4,8,12
source-definition SHA256  5618a883af37feb70bf2238145ee0a249536d98523af290b8ae244e005c6e759
primitive-object SHA256   1b60db67667172655b908b8dce7b6152bdfecd413375df9a88ba34d4cf50c86b
primitive-file SHA256     8e3dc89a82a7381ebf930336ba635a6d7af168afdd8ba1a4f0dcc77054170281
producer SHA256           82da41d4feb8e6d6dcac023725b2b3a843b33bd15080ddb580bae858c29284bd
```

Its four separation intervals satisfy

```text
max sigma_n^2
 =819121242427/1073741824000000
 <1/128,                                                   (L-16232.2)
```

and hence lie inside the exact scope of `L-16231`.

The primitive supplies the exact normalized energy ceilings

```text
||T_rad||_2 <=1,
||partial_s T_rad||_2 <=2.                                (L-16232.3)
```

These deliberately coarse source-bound bounds are sufficient at this level;
no inherited synthetic radial error is used.

## 3. First-alias repaired frame

Let

```text
r=d_4/d_8.
```

The frozen mode hierarchy gives at this block

```text
r<=1/204800000.                                           (L-16232.4)
```

In the exact repaired coordinates `x_n=q_n c_n`, the target and complement have
coefficient differences of the defects. Using the fixed-mode point-value bound
`q_max/q_min<=4`, their normalized first-alias correlation is at most

```text
4 sqrt(2r) (2-r)/(1-r).                                   (L-16232.5)
```

The exact squared comparison is

```text
32 r (2-r)^2/(1-r)^2
 =167772159180800001/
  268435453378560006400000
 <1/1000000.                                               (L-16232.6)
```

Therefore

```text
boxed:
999/1000 I <=D_first<=1001/1000 I.                        (L-16232.7)
```

## 4. Complete alias Gram

At `gamma=32768`,

```text
floor(sqrt(gamma))=181,
cuberoot(gamma)=32.
```

Substitution in (L-16232.1) gives

```text
boxed:
||C_cross||
 <=5019/23168
 =0.2166350138... .                                       (L-16232.8)
```

Since the higher-alias self block is positive semidefinite,

```text
D_full=D_first+P_self+C_cross,
P_self>=0,
```

and hence

```text
boxed:
D_full
 >=(999/1000-5019/23168)I
 =2265729/2896000 I.                                      (L-16232.9)
```

The inherited outward upper ledger `D_full<=18I` remains valid.

## 5. Endpoint, support and scalarization fields

The normalized radial outgoing-phase theorem gives

```text
endpoint point upper       128/gamma=1/256,
endpoint L2 norm upper     1/256,
endpoint L2 squared upper  1/65536.                        (L-16232.10)
```

Together with (L-16232.3), the complete deterministic source charge is

```text
boxed:
delta_det<=1+2+1/256+1/256=385/128.                       (L-16232.11)
```

Use two mean-square families with

```text
M<=1/gamma,
threshold=1/cuberoot(gamma)=1/32,
```

and an exceptional-support charge `1/32`. Markov gives

```text
bad measure <=3/32,
good measure >=29/32.                                     (L-16232.12)
```

Because `gamma=2^15` and `log 2>69/100`,

```text
log gamma>207/20.                                         (L-16232.13)
```

The exact relative scalarization error reconstructed by X-16209 is

```text
36836328125/73375830477
 <51/100.                                                  (L-16232.14)
```

## 6. Complete target/gap ratio

Take the outward source constants

```text
C_4=4,
c_8=1/20,
r<=1/204800000,
epsilon<=51/100.
```

After dividing target and gap by the common positive scalar `a d_8`,

```text
target <=(1+epsilon) C_4 r
       =151/5120000000,                                   (L-16232.15)
```

while

```text
gap >=(1-epsilon)c_8-2 epsilon C_4 r
    =62719949/2560000000.                                 (L-16232.16)
```

Thus

```text
boxed:
(mu-L)/g
 <=151/125439898
 <1.204e-6.                                                (L-16232.17)
```

This is the full fail-closed wrapper ratio for the bound `gamma=32768` source
packet.

## 7. Unbounded emitter theorem

Put

```text
gamma_j=4096*8^j=(16*2^j)^3,
q_j=16*2^j,
j>=1.                                                     (L-16232.18)
```

For every emitted source primitive satisfying the same fixed-mode and exact
unit-energy interfaces, define

```text
c_j=18/floor(sqrt(gamma_j))+2/q_j+1792/gamma_j,
G_j=999/1000-c_j.                                         (L-16232.19)
```

Then

```text
c_j->0,
G_j->999/1000>0.                                          (L-16232.20)
```

Use endpoint charge `128/gamma_j` in each of the point and L2 channels,
mean-square bound `1/gamma_j`, threshold `1/q_j`, and the fixed source energy
charge `1+2`. The complete relative scalarization error satisfies

```text
epsilon_j
 <=[4+256/gamma_j+2/q_j]
   /[G_j*(69/100)(12+3j)]
 ->0.                                                      (L-16232.21)
```

The mode hierarchy contracts by

```text
r_j=d_4/d_8<=1/(50000*4096^j).                            (L-16232.22)
```

Consequently the exact wrapper ratio is bounded by

```text
rho_j
 <=4(1+epsilon_j)r_j
   /[(1-epsilon_j)/20-8 epsilon_j r_j].                   (L-16232.23)
```

For all sufficiently large `j` its denominator is bounded below by a positive
constant, and therefore

```text
boxed:
rho_j=O(4096^-j)=O(gamma_j^-4)->0.                        (L-16232.24)
```

The emitter in X-16209 writes every finite rational appearing above and refuses
promotion unless the actual source file, its internal primitive digest, and the
two theorem Git blobs match.

## 8. Proof boundary

This proves a complete second finite block and an all-scale certificate rule.
It does not manufacture the infinitely many source primitives. Each later level
must still emit its own directed separation/pole/source file and pass the same
consumer. The target-projection diagonal and the CCM finite-real-zero theorem
remain separate final interfaces. No proof of RH is claimed.
