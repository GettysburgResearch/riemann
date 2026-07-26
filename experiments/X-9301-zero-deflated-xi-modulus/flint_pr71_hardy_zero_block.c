/*
   Rigorous block of critical-line zero balls around the exact PR #71 ordinate.

   The producer calls FLINT's Platt/Turing Hardy-Z zero isolator at an exact
   starting index, verifies that every returned ball is strictly ordered and
   disjoint, and emits the full block.  Each emitted ball is a proof-grade
   lower-count-one critical-line zero bin for L-9301.

   Build:
     cc -O3 -std=c11 -Wall -Wextra -Werror \
       flint_pr71_hardy_zero_block.c -o flint_pr71_hardy_zero_block \
       -lflint -lmpfr -lgmp -lpthread -lm
*/
#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb_dirichlet.h>

#define DEFAULT_PREC 192
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

static void index_plus(fmpz_t output, const fmpz_t start, slong offset)
{
    fmpz_set(output, start);
    if (offset >= 0)
        fmpz_add_ui(output, output, (ulong) offset);
    else
        fmpz_sub_ui(output, output, (ulong) (-offset));
}

int main(int argc, char **argv)
{
    slong precision = DEFAULT_PREC;
    slong length = DEFAULT_LEN;
    int threads = 4;
    const char *start_index = START_INDEX;
    if (argc >= 2) precision = atol(argv[1]);
    if (argc >= 3) length = atol(argv[2]);
    if (argc >= 4) threads = atoi(argv[3]);
    if (argc >= 5) start_index = argv[4];
    if (precision < 80 || length < 8 || threads < 1)
    {
        flint_fprintf(stderr,
            "usage: %s [precision>=80] [length>=8] [threads>=1] "
            "[start_zero_index]\n", argv[0]);
        return 2;
    }

    flint_set_num_threads(threads);

    fmpz_t start, index;
    fmpz_init(start);
    fmpz_init(index);
    if (fmpz_set_str(start, start_index, 10) != 0)
    {
        flint_fprintf(stderr, "invalid start index\n");
        return 2;
    }

    arb_ptr zeros = _arb_vec_init(length);
    slong returned = acb_dirichlet_platt_hardy_z_zeros(
        zeros, start, length, precision);
    if (returned < 2)
    {
        flint_fprintf(stderr, "FLINT returned only %wd Hardy-Z zeros\n", returned);
        return 3;
    }

    for (slong i = 0; i + 1 < returned; i++)
    {
        if (!arb_lt(zeros + i, zeros + i + 1))
        {
            flint_fprintf(stderr,
                "Hardy-Z balls overlap or are not strictly ordered at local index %wd\n",
                i);
            return 4;
        }
    }

    arb_t target;
    arb_init(target);
    set_exact_target(target);
    slong below = -1, above = -1;
    for (slong i = 0; i < returned; i++)
    {
        if (arb_lt(zeros + i, target))
            below = i;
        else if (arb_gt(zeros + i, target))
        {
            above = i;
            break;
        }
        else
        {
            flint_fprintf(stderr,
                "target overlaps Hardy-Z zero ball at local index %wd\n", i);
            return 5;
        }
    }
    if (below < 0 || above < 0 || above != below + 1)
    {
        flint_fprintf(stderr,
            "block does not consecutively bracket target: below=%wd above=%wd returned=%wd\n",
            below, above, returned);
        return 6;
    }

    flint_printf("{\n");
    flint_printf("  \"schema\":\"riemann.x9301-pr71-hardy-zero-block.v1\",\n");
    flint_printf("  \"backend\":\"FLINT acb_dirichlet_platt_hardy_z_zeros\",\n");
    flint_printf("  \"precision_bits\":%wd,\n", precision);
    flint_printf("  \"threads\":%d,\n", threads);
    flint_printf("  \"requested_start_index\":");
    print_fmpz_string(start);
    flint_printf(",\n");
    flint_printf("  \"requested_length\":%wd,\n", length);
    flint_printf("  \"returned_count\":%wd,\n", returned);
    flint_printf("  \"target\":{\"numerator\":\"%s\",\"denominator\":\"4294967296\"},\n",
        T_NUM);
    flint_printf("  \"target_below_local_index\":%wd,\n", below);
    flint_printf("  \"target_above_local_index\":%wd,\n", above);
    index_plus(index, start, below);
    flint_printf("  \"target_below_zero_index\":");
    print_fmpz_string(index);
    flint_printf(",\n");
    index_plus(index, start, above);
    flint_printf("  \"target_above_zero_index\":");
    print_fmpz_string(index);
    flint_printf(",\n");
    flint_printf("  \"zeros\":[\n");
    for (slong i = 0; i < returned; i++)
    {
        index_plus(index, start, i);
        flint_printf("    {\"local_index\":%wd,\"zero_index\":", i);
        print_fmpz_string(index);
        flint_printf(",\"ball\":");
        print_arb_interval(zeros + i);
        flint_printf("}%s\n", i + 1 < returned ? "," : "");
    }
    flint_printf("  ],\n");
    flint_printf("  \"classification\":\"CERTIFIED_CRITICAL_LINE_ZERO_BLOCK\",\n");
    flint_printf("  \"proof_boundary\":\"Every emitted interval is a FLINT Platt-isolated Hardy-Z zero ball indexed with multiplicity. Independent backend reproduction is required before a negative downstream certificate is promoted.\"\n");
    flint_printf("}\n");

    arb_clear(target);
    _arb_vec_clear(zeros, length);
    fmpz_clear(start);
    fmpz_clear(index);
    flint_cleanup();
    return 0;
}
