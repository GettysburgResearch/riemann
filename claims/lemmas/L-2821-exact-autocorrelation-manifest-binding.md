# L-2821 — Exact binding of a D-0801 autocorrelation manifest to its dyadic vector

Claim ID: L-2821  
Title: Every carrier coefficient used by the prime producer is exactly recomputable from the frozen vector  
Status: PROPOSED  
Authoring agent: `gpt56-05-h`  
Created: 2026-07-25  
Dependencies: D-0801; X-2804 vector schema; elementary Gaussian-integer arithmetic  
Scope: producer provenance for X-2805/X-2816  
Related counterexample candidates: any future D-0801 fixed-vector certificate

## Statement

Let

\[
 v_j=\frac{r_j+i s_j}{2^b},
 \qquad
 r_j,s_j\in\mathbb Z,
 \qquad 0\le j<K.
\]

Define, for `0<=d<K`,

\[
 a_d=\sum_{j=0}^{K-1-d}\overline{v_j}v_{j+d},
 \qquad
 a_K=0.
\]

Then every coefficient has the exact dyadic representation

\[
 a_d=\frac{A_d+iB_d}{2^{2b}},
\]

where

\[
 \boxed{
 A_d=\sum_{j=0}^{K-1-d}(r_jr_{j+d}+s_js_{j+d}),
 }
\]

and

\[
 \boxed{
 B_d=\sum_{j=0}^{K-1-d}(r_js_{j+d}-s_jr_{j+d}).
 }
\]

Consequently a producer manifest containing

```text
autocorr_scale_bits 2*b
a d A_d B_d
```

for `d=0,...,K`, together with the exact vector, can be verified using integer arithmetic only. No floating eigenvector, FFT, complex arithmetic library, or transcendental function is involved.

For the recovered target, a valid binding certificate must prove simultaneously:

```text
canonical vector SHA-256
3ee8d915d69cd6bfe7bd68a3bff840a693f1966aef5c3a8f61d43e33021d4297

raw target-autocorrelation.txt SHA-256
e1bcc62d1b505ab3bdd03965f23dabcefab3b3cdab131a07531d1761d2b45739

normalization SHA-256
65bacffb2e03518fa6ffb771f79d276b0018f7a22a1b17f3a7566d119024c8be

parameter SHA-256
ac28f01b3804426fb19275c7cf0588226292d848b7b4d62bb983fd9ac7ad3e34
```

and exact equality of all `K+1=1025` coefficient pairs.

## Proof

Direct multiplication gives

\[
 \overline{v_j}v_{j+d}
 =\frac{(r_j-is_j)(r_{j+d}+is_{j+d})}{2^{2b}}.
\]

Its real and imaginary numerators are respectively

\[
 r_jr_{j+d}+s_js_{j+d}
\]

and

\[
 r_js_{j+d}-s_jr_{j+d}.
\]

Summing over `j` proves the displayed formulas. The support convention gives `a_K=0` because no cell pair has lag `K`. Every operation is exact in `Z`. ∎

## Certificate role

The current directed shard schema records the vector digest copied from the manifest. That prevents accidental mixing of visibly different vector labels, but by itself does not prove that the manifest's `a_d` table was computed from that vector.

A complete proof package should therefore contain one separate exact binding result. Once the binding is checked:

1. the vector fixes every `a_d` coefficient;
2. the manifest fixes the producer inputs;
3. each shard binds the manifest parameter/vector/normalization labels;
4. the complete shard ledger and raw-file digest preserve the exact finite computation.

The binding check need be performed once per exact vector/manifest pair, not once per shard.

## Fail-closed verifier requirements

A verifier must reject:

- any missing or duplicated lag;
- `a_count != K+1`;
- `autocorr_scale_bits != 2*vector_scale_bits`;
- a nonzero lag-`K` coefficient;
- any mismatch in `A_d` or `B_d`;
- vector, parameter, or normalization digest mismatch;
- a raw manifest SHA mismatch;
- malformed integers or unrecognized fields.

It should recompute the canonical vector digest from the exact JSON arrays rather than trust the stored digest.

## Gap audit

- A SHA-256 checksum preserves a file but does not prove its mathematical relation to the vector; coefficient equality supplies that relation.
- Coefficient equality does not prove the prime producer used the checked file; producer logs/binary/source fingerprints and raw input digests supply that provenance.
- The orientation matters: replacing `conj(v_j)*v_(j+d)` by `v_j*conj(v_(j+d))` conjugates the imaginary coefficients and can change the prime value.
- Normalizing the vector after manifest generation produces a different certificate and must fail.

## Adversarial tests

1. Mutate one real numerator of the vector and require both the vector digest and coefficient table to fail.
2. Mutate one imaginary `B_d` sign and require orientation failure.
3. Swap two lags and require index failure.
4. Set the terminal `a_K` nonzero and require rejection.
5. Change only whitespace in the raw manifest: coefficient verification may pass, but the raw-file SHA must change, visibly distinguishing mathematical equality from artifact identity.

## Suggested next attack

Run X-2817's exact binder on the recovered target before final sign promotion. Include its output digest in the final certificate index and require any independent producer to regenerate the same `1025` Gaussian-integer coefficients from the frozen vector.