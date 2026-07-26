/* flint_pr71_nested_total_counts.c

   Rigorous nested total-zero counts around the exact PR #71 ordinate.

   For exact dyadic radii R, FLINT's Turing routine evaluates the total number
   N(t) of nontrivial zeta zeros below t, counted with multiplicity. The exact
   difference

       N(T+R) - N(T-R)

   is unconditional. Under RH it is also a critical-line count and therefore
   feeds the L-9303 / L-9302 order-statistic deflation.

   Build:
     cc -O3 -std=c11 -Wall -Wextra -Werror \
       flint_pr71_nested_total_counts.c -o flint_pr71_nested_total_counts \
       -lflint -lmpfr -lgmp -lpthread -lm
*/
#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb_dirichlet.h>

#define DEFAULT_PREC 192
#define RADIUS_COUNT 9

static const char *T_NUM = "20225875608341108140435";
/* R = 2^e: 1/32 through 8. */
static const slong RADIUS_EXP[RADIUS_COUNT] = {-5, -4, -3, -2, -1, 0, 1, 2, 3};

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

static void print_exact_radius(slong exponent)
{
    fmpz_t value;
    fmpz_init(value);
    fmpz_one(value);
    if (exponent >= 0)
    {
        fmpz_mul_2exp(value, value, (ulong) exponent);
        flint_printf("{\"numerator\":");
        print_fmpz_string(value);
        flint_printf(",\"denominator\":\"1\"}");
    }
    else
    {
        fmpz_mul_2exp(value, value, (ulong) (-exponent));
        flint_printf("{\"numerator\":\"1\",\"denominator\":");
        print_fmpz_string(value);
        flint_printf("}");
    }
    fmpz_clear(value);
}

static void set_exact_target(arb_t target)
{
    fmpz_t numerator, exponent;
    fmpz_init(numerator);
    fmpz_init(exponent);
    if (fmpz_set_str(numerator, T_NUM, 10) != 0)
    {
        flint_fprintf(stderr, "invalid target numerator\n");
        abort();
    }
    fmpz_set_si(exponent, -32);
    arb_set_fmpz_2exp(target, numerator, exponent);
    fmpz_clear(numerator);
    fmpz_clear(exponent);
}

int main(int argc, char **argv)
{
    slong precision = DEFAULT_PREC;
    int threads = 4;
    if (argc >= 2) precision = atol(argv[1]);
    if (argc >= 3) threads = atoi(argv[2]);
    if (precision < 80 || threads < 1)
    {
        flint_fprintf(stderr, "usage: %s [precision>=80] [threads>=1]\n", argv[0]);
        return 2;
    }
    flint_set_num_threads(threads);

    arb_t target, radius, lower, upper, n_lower_ball, n_upper_ball;
    arb_init(target);
    arb_init(radius);
    arb_init(lower);
    arb_init(upper);
    arb_init(n_lower_ball);
    arb_init(n_upper_ball);
    set_exact_target(target);

    fmpz_t n_lower, n_upper, count, previous_count;
    fmpz_init(n_lower);
    fmpz_init(n_upper);
    fmpz_init(count);
    fmpz_init(previous_count);
    fmpz_zero(previous_count);

    flint_printf("{\n");
    flint_printf("  \"schema\":\"riemann.x9302-pr71-total-count-windows.v1\",\n");
    flint_printf("  \"backend\":\"FLINT acb_dirichlet_zeta_nzeros exact dyadic windows\",\n");
    flint_printf("  \"precision_bits\":%wd,\n", precision);
    flint_printf("  \"threads\":%d,\n", threads);
    flint_printf("  \"target\":{\"numerator\":\"%s\",\"denominator\":\"4294967296\"},\n", T_NUM);
    flint_printf("  \"count_interval_convention\":\"(T-R,T+R]\",\n");
    flint_printf("  \"windows\":[\n");

    for (slong i = 0; i < RADIUS_COUNT; i++)
    {
        arb_one(radius);
        arb_mul_2exp_si(radius, radius, RADIUS_EXP[i]);
        arb_sub(lower, target, radius, ARF_PREC_EXACT);
        arb_add(upper, target, radius, ARF_PREC_EXACT);
        if (!arb_is_positive(lower))
        {
            flint_fprintf(stderr, "nonpositive lower endpoint at radius index %wd\n", i);
            return 3;
        }

        acb_dirichlet_zeta_nzeros(n_lower_ball, lower, precision);
        acb_dirichlet_zeta_nzeros(n_upper_ball, upper, precision);
        if (!arb_get_unique_fmpz(n_lower, n_lower_ball) ||
            !arb_get_unique_fmpz(n_upper, n_upper_ball))
        {
            flint_fprintf(stderr,
                "Turing count did not isolate integers at radius index %wd; increase precision\n",
                i);
            return 4;
        }
        fmpz_sub(count, n_upper, n_lower);
        if (fmpz_sgn(count) < 0)
        {
            flint_fprintf(stderr, "negative window count at radius index %wd\n", i);
            return 5;
        }
        if (fmpz_cmp(count, previous_count) < 0)
        {
            flint_fprintf(stderr, "nested count decreased at radius index %wd\n", i);
            return 6;
        }

        flint_printf("    {\"id\":\"r_");
        if (RADIUS_EXP[i] < 0)
            flint_printf("m%wd", -RADIUS_EXP[i]);
        else
            flint_printf("p%wd", RADIUS_EXP[i]);
        flint_printf("\",\"radius\":");
        print_exact_radius(RADIUS_EXP[i]);
        flint_printf(",\"lower_endpoint\":");
        print_arb_interval(lower);
        flint_printf(",\"upper_endpoint\":");
        print_arb_interval(upper);
        flint_printf(",\"N_lower_ball\":");
        print_arb_interval(n_lower_ball);
        flint_printf(",\"N_upper_ball\":");
        print_arb_interval(n_upper_ball);
        flint_printf(",\"N_lower\":");
        print_fmpz_string(n_lower);
        flint_printf(",\"N_upper\":");
        print_fmpz_string(n_upper);
        flint_printf(",\"count_lower\":");
        print_fmpz_string(count);
        flint_printf("}%s\n", i + 1 < RADIUS_COUNT ? "," : "");
        fmpz_set(previous_count, count);
    }

    flint_printf("  ],\n");
    flint_printf("  \"classification\":\"CERTIFIED_NESTED_TOTAL_ZETA_ZERO_COUNTS\",\n");
    flint_printf("  \"proof_boundary\":\"Every count is the unconditional FLINT Turing difference N(T+R)-N(T-R), hence uses the half-open interval (T-R,T+R], with multiplicity. Under RH only, the same counts become critical-line order-statistic bounds for L-9303. A negative downstream row requires independent primitive reproduction and analytic review.\"\n");
    flint_printf("}\n");

    arb_clear(target);
    arb_clear(radius);
    arb_clear(lower);
    arb_clear(upper);
    arb_clear(n_lower_ball);
    arb_clear(n_upper_ball);
    fmpz_clear(n_lower);
    fmpz_clear(n_upper);
    fmpz_clear(count);
    fmpz_clear(previous_count);
    flint_cleanup();
    return 0;
}
