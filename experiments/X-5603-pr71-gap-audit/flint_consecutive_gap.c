/* flint_consecutive_gap.c

   Rigorous PR #71 local-gap producer using FLINT's built-in Platt/Turing
   zeta-zero isolation.  The proof object is a pair of consecutive *zeta* zero
   balls bracketing the exact rational ordinate.  No sign-change heuristic or
   smooth census is used.

   Build:
     cc -O3 -std=c11 -Wall -Wextra -Werror flint_consecutive_gap.c \
        -o flint_consecutive_gap -lflint -lmpfr -lgmp -lpthread -lm
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

    fmpz_t start, idx_lo, idx_hi;
    fmpz_init(start);
    fmpz_init(idx_lo);
    fmpz_init(idx_hi);
    if (fmpz_set_str(start, START_INDEX, 10) != 0)
    {
        flint_fprintf(stderr, "invalid start index\n");
        return 2;
    }

    acb_ptr zeros = _acb_vec_init(len);
    slong got = acb_dirichlet_platt_zeta_zeros(zeros, start, len, prec);
    if (got < 2)
    {
        flint_fprintf(stderr, "FLINT returned only %wd zeros\n", got);
        return 3;
    }

    arb_t target, gap, left, right, two_pi, density, normalized;
    arb_init(target);
    arb_init(gap);
    arb_init(left);
    arb_init(right);
    arb_init(two_pi);
    arb_init(density);
    arb_init(normalized);
    set_exact_target(target);

    slong below = -1, above = -1;
    for (slong i = 0; i < got; i++)
    {
        const arb_struct *im = acb_imagref(zeros + i);
        if (arb_lt(im, target))
            below = i;
        else if (arb_gt(im, target))
        {
            above = i;
            break;
        }
        else
        {
            flint_fprintf(stderr,
                "target overlaps returned zero ball at local index %wd; increase precision\n", i);
            return 4;
        }
    }

    if (below < 0 || above < 0 || above != below + 1)
    {
        flint_fprintf(stderr,
            "returned block does not strictly bracket target: below=%wd above=%wd got=%wd\n",
            below, above, got);
        return 5;
    }

    index_plus(idx_lo, start, below);
    index_plus(idx_hi, start, above);
    arb_sub(gap, acb_imagref(zeros + above), acb_imagref(zeros + below), prec);
    arb_sub(left, target, acb_imagref(zeros + below), prec);
    arb_sub(right, acb_imagref(zeros + above), target, prec);

    arb_const_pi(two_pi, prec);
    arb_mul_2exp_si(two_pi, two_pi, 1);
    arb_div(density, target, two_pi, prec);
    arb_log(density, density, prec);
    arb_div(density, density, two_pi, prec);
    arb_mul(normalized, gap, density, prec);

    flint_printf("{\n");
    flint_printf("  \"schema\":\"riemann.x5603-flint-consecutive-gap.v1\",\n");
    flint_printf("  \"backend\":\"FLINT acb_dirichlet_platt_zeta_zeros\",\n");
    flint_printf("  \"precision_bits\":%wd,\n", prec);
    flint_printf("  \"threads\":%d,\n", threads);
    flint_printf("  \"requested_start_index\":"); print_fmpz_string(start); flint_printf(",\n");
    flint_printf("  \"requested_length\":%wd,\n", len);
    flint_printf("  \"returned_length\":%wd,\n", got);
    flint_printf("  \"target\":{\"numerator\":\"%s\",\"denominator\":\"4294967296\"},\n", T_NUM);
    flint_printf("  \"lower_zero_index\":"); print_fmpz_string(idx_lo); flint_printf(",\n");
    flint_printf("  \"upper_zero_index\":"); print_fmpz_string(idx_hi); flint_printf(",\n");
    flint_printf("  \"lower_zero_imaginary_ball\":"); print_arb_interval(acb_imagref(zeros + below)); flint_printf(",\n");
    flint_printf("  \"upper_zero_imaginary_ball\":"); print_arb_interval(acb_imagref(zeros + above)); flint_printf(",\n");
    flint_printf("  \"target_minus_lower\":"); print_arb_interval(left); flint_printf(",\n");
    flint_printf("  \"upper_minus_target\":"); print_arb_interval(right); flint_printf(",\n");
    flint_printf("  \"gap\":"); print_arb_interval(gap); flint_printf(",\n");
    flint_printf("  \"gap_in_local_mean_spacings\":"); print_arb_interval(normalized); flint_printf(",\n");
    flint_printf("  \"classification\":\"CERTIFIED_CONSECUTIVE_TOTAL_ZERO_GAP_IF_API_COMPLETES\",\n");
    flint_printf("  \"counterexample_candidate\":null,\n");
    flint_printf("  \"proof_boundary\":\"The FLINT Platt/Turing API supplies consecutive zeta-zero balls. This certifies only the local zero gap; it does not determine a global Pick form or prove RH elsewhere.\"\n");
    flint_printf("}\n");

    arb_clear(target);
    arb_clear(gap);
    arb_clear(left);
    arb_clear(right);
    arb_clear(two_pi);
    arb_clear(density);
    arb_clear(normalized);
    _acb_vec_clear(zeros, len);
    fmpz_clear(start);
    fmpz_clear(idx_lo);
    fmpz_clear(idx_hi);
    flint_cleanup();
    return 0;
}
