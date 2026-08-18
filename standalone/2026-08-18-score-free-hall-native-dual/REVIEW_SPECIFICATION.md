# Hostile review specification

A valid review must independently answer:

- Does the compact Hall residual plus bonus equal the complete signed row in
  every component coordinate?
- Is the bonus target-free and score-free in every theorem and checker path?
- Does the same endpoint kernel act on source and bonus sorts?
- Are omissions removed before the kernel?
- Are all children normalized by actual target mass and below one eighth?
- Are Hall bonuses and root corrections absent from all children?
- Does one row supply both `q` and `4q` responses?
- Is `2<=q<K` covered without a cutoff atom?
- Is top source absent from output before being spent as terminal reserve?
- Is the final `Y_4` price computed from the actual slack vector?
- Is any RH-equivalent benchmark estimate used upstream?

Any negative answer rejects `T-98800` as a proof.  A failure of this candidate
does not refute RH.
