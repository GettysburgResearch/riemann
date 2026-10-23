# Source pin and notation clarification

23 October 2026. This note corrects a source-hash transcription only;
the cited commit, path, and analytic content are unchanged.

In LABEL_UNIFORM_MOBIUS_RESIDUES.md, SHA256
12c765c1fdcccec8ebb087b7608b80bb7b2d30114bf664ac1e43a2966b9d8f89d,
the printed SHA256 of the imported full scalar note is incorrect.
For PR1015 commit e87c5f669f81fe6371af926917d1c5b21023bce8, the correct
SHA256 of the exact Git blob at
standalone/2026-10-22-residue-remainder-followup/MOBIUS_FULL_SERIES_SCALAR_REMAINDER.md
is

    b45267a73c0123cb0a1d83c161ae5fe995e4493d7395bfcb21a67a790d54fcaf.

At that same commit the companion
MOBIUS_PRIMITIVE_SCALAR_REMAINDER.md has SHA256

    60a1615eefca1ed6c19572b2fa2296e2dbbf7146654b77a940ef1ecec469cf86.

The paper10 version2 snapshot has the distinct SHA256

    525c899dd4dd5cb0ed15db43f63fb6e25cc140f98358e9d41ddfe897f5a23a7a.

The incorrect hash in the first note accidentally combined a prefix of
the first hash with a suffix of the third. Its frozen bytes are retained
so that existing review receipts still identify the reviewed document.

In P14's prose, the plain-text expression A_U*alpha denotes
multiplication of the column coefficient by A_U. The actual projected
row vector is \(A_U\alpha\). Its scalar pairing is computed using
\(\langle A_U\alpha,v_R\rangle=\langle\alpha,A_U^*v_R\rangle\).
The benchmark note uses this unambiguous notation.
