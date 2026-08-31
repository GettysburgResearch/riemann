# First possible actual d3: one complete highest-weight block

Status: preregistered before shape enumeration, elimination or source-lift acquisition.
Date: 2026-09-01. No d3 job may start until the complete higher-syzygy packet is frozen and the parent memory gate is confirmed.

## Target

In the same change-of-rings double complex, compute the complete weight744 block of

    d3: E3_(3,1),internal5 -> E3_(0,3),internal5 = B_(3,5).

The frozen target character is [555] trivial + [744] sign, dimension11. Weight744 is a complete highest-weight space of dimension1 with factor sign. A nonzero image at this block proves that d3 is nonzero and reaches the complete [744] sign summand. It does not prove surjectivity onto the separate [555] summand. If all bounded gates pass, weight555 may be preregistered later in a separate extension; it is not part of this first acquisition.

## Exact two-stage source formula

Start with every kernel vector

    z in Lambda^3 Q tensor B_(1,2)

of the first Q differential into Lambda^2 Q tensor B_(1,3), at total weight744. There is no incoming Lambda^4 Q tensor B_(1,1), since B_(1,1)=0. Use the accepted Q action's original-chain boundary witnesses to assemble eta1 in Lambda^2 Q tensor C_(2,3) with

    d_W eta1 = delta_Q z.

With total differential D=d_W+(-1)^q delta_Q, z+eta1 has residual delta_Q eta1. A source survives to E3 exactly when this residual is W-exact. Here the relevant E2_(1,2) incoming group is zero because B_(2,3)=0. For every surviving vector, solve in the complete original chain block

    d_W eta2 = - delta_Q eta1,

with eta2 in Q tensor C_(3,4). Then

    D(z+eta1+eta2) = -delta_Q eta2,

and the B_(3,5) class of the last expression is the preregistered d3 representative. Every displayed equality must be checked in original chain coordinates. Kernel vectors whose first obstruction is nonzero and surviving vectors whose d3 is zero are both retained.

The target is B_(3,5) itself: B_(3,4)=0 removes d1 incoming classes, and B_(2,3)=0 removes the possible d2 incoming source. No Euler characteristic or ambient Tor vanishing beyond these frozen individual groups identifies the map.

There is also no earlier d2 incoming quotient on the source: E2_(5,0),internal5 is the kernel of the standard map Lambda^5 Q -> Lambda^4 Q tensor B_(0,1). The frozen multiplication Q tensor B_(0,0) -> B_(0,1) is the identity identification, so this exterior comultiplication is injective in characteristic zero. This statement is checked directly on the declared Q basis; it is not inferred from the final ambient Betti table.

## Coverage and bounds

First output, without elimination, the complete weight744 dimensions for:

- Lambda^3 Q tensor B_(1,2) and Lambda^2 Q tensor B_(1,3);
- the required internal-degree4 W chain groups through homological degree3;
- the internal-degree5 W target chain groups through homological degree4.

Every eliminated matrix must have at most512 rows and512 columns. If any block exceeds this cap, shape mode refuses further acquisition and retains the exact dimensions. Do not select a submatrix or a fitted source vector. A separate streamed or isotypic theorem would require a new preregistration.

Use exact rational arithmetic,4096-bit coefficient cap, sparse vector/lift cap8192terms, artifact16MiB, working set1GiB and240second wall clock. Expected resource use is unknown until the shape-only report. Bind and authenticate the frozen Q-action, d2 and complete higher-syzygy packets before importing source helpers or parsing artifacts. No old cap is modified.

## Acceptance and scope

Accept one of: `VERIFIED_NONZERO_D3_744`, `VERIFIED_ZERO_D3_744`, `VERIFIED_NO_E3_SOURCE_744`, or an explicit bounded refusal. A nonzero result must match the target factor sign by direct transposition and three-cycle actions. Negative controls alter each lift stage, both totalization signs, the E3-survival predicate, the target boundary reduction, a frozen source pin and numeric JSON types. Ordinary and optimized replay are required.

This is an actual secondary-stage transgression and a prospective next transferred operation. It is not inferred from the Euler numerator, does not compute the [555] component, does not reconstruct the entire ambient resolution, and has no arithmetic-purity or RH consequence.
