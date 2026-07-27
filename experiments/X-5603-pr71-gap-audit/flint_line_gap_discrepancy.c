/* flint_line_gap_discrepancy.c

   A direct finite RH-counterexample producer for the empirical PR #71 gap.

   1. FLINT's Platt/Turing Hardy-Z routine returns consecutive critical-line
      zero balls around the exact dyadic target.
   2. Exact dyadic endpoints are placed strictly between those balls.
   3. FLINT's Turing zero-count routine computes N(b)-N(a), the number of all
      nontrivial zeta zeros in the full critical-strip slab, with multiplicity.

   The interior slab contains no Hardy-Z zero.  Therefore:

       N(b)-N(a) > 0  =>  an off-critical zero exists  =>  RH is false.

   A zero discrepancy proves only that this finite interior slab is empty.

   Build:
     cc -O3 -std=c11 -Wall -Wextra -Werror \
       flint_line_gap_discrepancy.c -o flint_line_gap_discrepancy \
       -lflint -lmpfr -lgmp -lpthread -lm
*/
#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_dirichlet.h>

#define DEFAULT_PREC 160
#define DEFAULT_LEN 128

static const char *T_NUM = "20225875608341108140435";
/* Smooth N(T) is about 19743642386014, so this block brackets the target. */
static const char *START_INDEX = "19743642385950";

static void print_fmpz_string(const fmpz_t x)
{
    flint_printf("\"");
    fmpz_print(x);
    flint_printf("\"");
}

static void print_arb_interval(const arb_t x)
{
    fmpz_t lo, hi, exp;
    fmpz_init(lo);
    fmpz_init(hi);
    fmpz_init(exp);
    arb_get_interval_fmpz_2exp(lo, hi, exp, x);
    flint_printf("{\"lower\":{\"mantissa\":");
    print_fmpz_string(lo);
    flint_printf(",\"exponent\":");
    print_fmpz_string(exp);
    flint_printf("},\"upper\":{\"mantissa\":");
    print_fmpz_string(hi);
    flint_printf(",\"exponent\":");
    print_fmpz_string(exp);
    flint_printf("}}");
    fmpz_clear(lo);
    fmpz_clear(hi);
    fmpz_clear(exp);
}

static void set_exact_target(arb_t t)
{
    fmpz_t num, exp;
    fmpz_init(num);
    fmpz_init(exp);
    if (fmpz_set_str(num, T_NUM, 10) != 0)
    {
        flint_fprintf(stderr, "invalid target numerator\n");
        abort();
    }
    fmpz_set_si(exp, -32);
    arb_set_fmpz_2exp(t, num, exp);
    fmpz_clear(num);
    fmpz_clear(exp);
}

static void index_plus(fmpz_t out, const fmpz_t start, slong offset)
{
    fmpz_set(out, start);
    if (offset >= 0)
        fmpz_add_ui(out, out, (ulong) offset);
    else
        fmpz_sub_ui(out, out, (ulong) (-offset));
}

/* Set out to the first dyadic at the source interval's own exponent that is
   strictly above the source upper endpoint. */
static void exact_dyadic_above(arb_t out, const arb_t source)
{
    fmpz_t lo, hi, exp;
    fmpz_init(lo);
    fmpz_init(hi);
    fmpz_init(exp);
    arb_get_interval_fmpz_2exp(lo, hi, exp, source);
    fmpz_add_ui(hi, hi, 1);
    arb_set_fmpz_2exp(out, hi, exp);
    fmpz_clear(lo);
    fmpz_clear(hi);
    fmpz_clear(exp);
}

/* Set out to the first dyadic at the source interval's own exponent that is
   strictly below the source lower endpoint. */
static void exact_dyadic_below(arb_t out, const arb_t source)
{
    fmpz_t lo, hi, exp;
    fmpz_init(lo);
    fmpz_init(hi);
    fmpz_init(exp);
    arb_get_interval_fmpz_2exp(lo, hi, exp, source);
    fmpz_sub_ui(lo, lo, 1);
    arb_set_fmpz_2exp(out, lo, exp);
    fmpz_clear(lo);
    fmpz_clear(hi);
    fmpz_clear(exp);
}

int main(int argc, char **argv)
{
    slong prec = DEFAULT_PREC;
    slong len = DEFAULT_LEN;
    int threads = 4;
    if (argc >= 2) prec = atol(argv[1]);
    if (argc >= 3) len = atol(argv[2]);
    if (argc >= 4) threads = atoi(argv[3]);
    if (prec < 80 || len < 8 || threads < 1)
    {
        flint_fprintf(stderr, "usage: %s [precision>=80] [len>=8] [threads>=1]\n", argv[0]);
        return 2;
    }

    flint_set_num_threads(threads);

    fmpz_t start, idx_lo, idx_hi, na, nb, discrepancy;
    fmpz_init(start);
    fmpz_init(idx_lo);
    fmpz_init(idx_hi);
    fmpz_init(na);
    fmpz_init(nb);
    fmpz_init(discrepancy);
    if (fmpz_set_str(start, START_INDEX, 10) != 0)
    {
        flint_fprintf(stderr, "invalid start index\n");
        return 2;
    }

    arb_ptr line_zeros = _arb_vec_init(len);
    slong got = acb_dirichlet_platt_hardy_z_zeros(
        line_zeros, start, len, prec);
    if (got < 2)
    {
        flint_fprintf(stderr, "FLINT returned only %wd Hardy-Z zeros\n", got);
        return 3;
    }

    arb_t target, a, b, na_ball, nb_ball, line_gap, interior_width;
    arb_init(target);
    arb_init(a);
    arb_init(b);
    arb_init(na_ball);
    arb_init(nb_ball);
    arb_init(line_gap);
    arb_init(interior_width);
    set_exact_target(target);

    slong below = -1, above = -1;
    for (slong i = 0; i < got; i++)
    {
        if (arb_lt(line_zeros + i, target))
            below = i;
        else if (arb_gt(line_zeros + i, target))
        {
            above = i;
            break;
        }
        else
        {
            flint_fprintf(stderr,
                "target overlaps Hardy-Z zero ball at local index %wd; increase precision\n",
                i);
            return 4;
        }
    }
    if (below < 0 || above < 0 || above != below + 1)
    {
        flint_fprintf(stderr,
            "Hardy-Z block does not consecutively bracket target: below=%wd above=%wd got=%wd\n",
            below, above, got);
        return 5;
    }

    index_plus(idx_lo, start, below);
    index_plus(idx_hi, start, above);
    exact_dyadic_above(a, line_zeros + below);
    exact_dyadic_below(b, line_zeros + above);
    if (!arb_lt(a, target) || !arb_lt(target, b) || !arb_lt(a, b))
    {
        flint_fprintf(stderr, "failed to construct an exact nonempty target slab\n");
        return 6;
    }

    /* These are rigorous Turing counts of all nontrivial zeros, with
       multiplicity. If an endpoint is itself a zero ordinate, the result will
       fail to isolate a unique integer and the producer fails closed. */
    acb_dirichlet_zeta_nzeros(na_ball, a, prec);
    acb_dirichlet_zeta_nzeros(nb_ball, b, prec);
    if (!arb_get_unique_fmpz(na, na_ball) || !arb_get_unique_fmpz(nb, nb_ball))
    {
        flint_fprintf(stderr,
            "Turing count did not isolate unique integers; increase precision or move endpoints\n");
        return 7;
    }
    fmpz_sub(discrepancy, nb, na);
    if (fmpz_sgn(discrepancy) < 0)
    {
        flint_fprintf(stderr, "negative zero-count discrepancy\n");
        return 8;
    }
    if (!fmpz_is_zero(discrepancy) && fmpz_fdiv_ui(discrepancy, 2) != 0)
    {
        flint_fprintf(stderr,
            "positive line-empty slab discrepancy is not even; fail closed\n");
        return 9;
    }

    arb_sub(line_gap, line_zeros + above, line_zeros + below, prec);
    arb_sub(interior_width, b, a, prec);

    flint_printf("{\n");
    flint_printf("  \"schema\":\"riemann.x5603-line-gap-discrepancy.v1\",\n");
    flint_printf("  \"backend\":\"FLINT Platt Hardy-Z isolation plus Turing total-zero counts\",\n");
    flint_printf("  \"precision_bits\":%wd,\n", prec);
    flint_printf("  \"threads\":%d,\n", threads);
    flint_printf("  \"requested_start_index\":"); print_fmpz_string(start); flint_printf(",\n");
    flint_printf("  \"requested_length\":%wd,\n", len);
    flint_printf("  \"returned_hardy_zero_count\":%wd,\n", got);
    flint_printf("  \"target\":{\"numerator\":\"%s\",\"denominator\":\"4294967296\"},\n", T_NUM);
    flint_printf("  \"lower_hardy_zero_index\":"); print_fmpz_string(idx_lo); flint_printf(",\n");
    flint_printf("  \"upper_hardy_zero_index\":"); print_fmpz_string(idx_hi); flint_printf(",\n");
    flint_printf("  \"lower_hardy_zero_ball\":"); print_arb_interval(line_zeros + below); flint_printf(",\n");
    flint_printf("  \"upper_hardy_zero_ball\":"); print_arb_interval(line_zeros + above); flint_printf(",\n");
    flint_printf("  \"line_gap\":"); print_arb_interval(line_gap); flint_printf(",\n");
    flint_printf("  \"interior_slab_lower_exact\":"); print_arb_interval(a); flint_printf(",\n");
    flint_printf("  \"interior_slab_upper_exact\":"); print_arb_interval(b); flint_printf(",\n");
    flint_printf("  \"interior_slab_width\":"); print_arb_interval(interior_width); flint_printf(",\n");
    flint_printf("  \"N_lower_ball\":"); print_arb_interval(na_ball); flint_printf(",\n");
    flint_printf("  \"N_upper_ball\":"); print_arb_interval(nb_ball); flint_printf(",\n");
    flint_printf("  \"N_lower\":"); print_fmpz_string(na); flint_printf(",\n");
    flint_printf("  \"N_upper\":"); print_fmpz_string(nb); flint_printf(",\n");
    flint_printf("  \"total_zero_discrepancy_in_line_empty_slab\":");
    print_fmpz_string(discrepancy); flint_printf(",\n");
    if (fmpz_is_zero(discrepancy))
        flint_printf("  \"classification\":\"CERTIFIED_EMPTY_FULL_STRIP_INTERIOR_SLAB\",\n");
    else
        flint_printf("  \"classification\":\"CERTIFIED_OFF_CRITICAL_ZERO_IN_LINE_EMPTY_SLAB\",\n");
    flint_printf("  \"counterexample_candidate\":");
    if (fmpz_is_zero(discrepancy)) flint_printf("null,\n");
    else flint_printf("\"PENDING_INDEPENDENT_REPRODUCTION_AND_REVIEW\",\n");
    flint_printf("  \"proof_boundary\":\"A positive discrepancy is the L-5605 finite RH-disproof predicate. Acceptance still requires independent backend reproduction and audit of the FLINT producer invocation. A zero discrepancy proves only this exact interior slab is empty.\"\n");
    flint_printf("}\n");

    arb_clear(target);
    arb_clear(a);
    arb_clear(b);
    arb_clear(na_ball);
    arb_clear(nb_ball);
    arb_clear(line_gap);
    arb_clear(interior_width);
    _arb_vec_clear(line_zeros, len);
    fmpz_clear(start);
    fmpz_clear(idx_lo);
    fmpz_clear(idx_hi);
    fmpz_clear(na);
    fmpz_clear(nb);
    fmpz_clear(discrepancy);
    flint_cleanup();
    return 0;
}
