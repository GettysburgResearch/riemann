# PR #496 / PR #500 native-versus-rough `q=2` audit

## Verdict

The earlier `109/1200` number is correct only when the pre-correction physical
marginal is the full `P_61` rough lift.  Its unconditional use against PR #496
or PR #500 is withdrawn.

At `X=10^16`, the thinned rough lift has normalized `q=2` excess greater than
`7/75`.  Exact rational reconstruction of the frozen nonterminal, omission and
terminal allowances gives a total below `1/400`, leaving strict excess
`109/1200`.

PR #500 avoids the separator only if its actual rough children retain the extra
paired-channel swap from the stopping-line source.  The frozen PR contains an
excellent physical coupling compiler but does not make this native/rough
commuting square explicit or test it in its synthetic replay.

## Repair

The successor adds the orientation bit to the physical source label.  Applying
the signed paired observation gives:

```text
finite P61 forcing                 = native + rough reservoir;
actual oriented rough children     = minus rough reservoir;
complete coupled output            = native.
```

Dropping the orientation is a fail-closed mutation detected at `q=2`.

## Route comparison

```text
PR #496:
  source/observation separation         retained;
  terminal-child fallback               useful;
  full-child-capacity promotion         not controlling here.

PR #500:
  Hall marginals and first owners       retained;
  actual child physical placements      retained;
  one label-blind quantizer             retained;
  native/rough orientation              supplied by successor;
  root cost                             unchanged, <60989.
```

## Scientific status

The new packet is a candidate-complete composition on frozen inputs.  It does
not independently authenticate the analytic Hall/profile inequalities,
endpoint integral, all-column estimates or endpoint-to-RH consumer.  RH remains
unproved pending reconstruction.
