/*
   Rigorous high-height scalar evaluation using FLINT's dedicated
   acb_dirichlet_zeta_jet_rs implementation.

   Frozen exact point:
       s = 1/2 + 2^-10 + i * 20225875608343121406355 * 2^-32.

   The program evaluates zeta and zeta' using the Riemann--Siegel jet, then
   assembles F = xi'/xi in two algebraically distinct orders:

     (1) corrected logarithmic completion plus zeta'/zeta;
     (2) derivative of the four-factor completed-xi product.

   It emits exact binary rectangle endpoints accepted by
   verify_value_certificate.py.  No ordinary floating-point value enters the
   certificate.
*/

#include <stdio.h>
#include <stdlib.h>

#include <flint/flint.h>
#include <flint/fmpz.h>
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_dirichlet.h>

static void
print_fmpz_quoted(const fmpz_t x)
{
    flint_printf("\"");
    fmpz_print(x);
    flint_printf("\"");
}

static void
print_arb_interval(const arb_t x)
{
    fmpz_t a, b, e;
    fmpz_init(a);
    fmpz_init(b);
    fmpz_init(e);
    arb_get_interval_fmpz_2exp(a, b, e, x);
    flint_printf("{\"lower\":{\"mantissa\":");
    print_fmpz_quoted(a);
    flint_printf(",\"exponent\":");
    print_fmpz_quoted(e);
    flint_printf("},\"upper\":{\"mantissa\":");
    print_fmpz_quoted(b);
    flint_printf(",\"exponent\":");
    print_fmpz_quoted(e);
    flint_printf("}}");
    fmpz_clear(a);
    fmpz_clear(b);
    fmpz_clear(e);
}

static void
print_acb_rectangle(const acb_t z)
{
    flint_printf("{\"real\":");
    print_arb_interval(acb_realref(z));
    flint_printf(",\"imag\":");
    print_arb_interval(acb_imagref(z));
    flint_printf("}");
}

static void
set_exact_point(acb_t s)
{
    fmpz_t m, e;
    arb_t x, t, half;
    fmpz_init(m);
    fmpz_init(e);
    arb_init(x);
    arb_init(t);
    arb_init(half);

    arb_one(x);
    arb_mul_2exp_si(x, x, -10);

    fmpz_set_str(m, "20225875608343121406355", 10);
    fmpz_set_si(e, -32);
    arb_set_fmpz_2exp(t, m, e);

    arb_one(half);
    arb_mul_2exp_si(half, half, -1);
    arb_add(acb_realref(s), half, x, ARF_PREC_EXACT);
    arb_set(acb_imagref(s), t);

    fmpz_clear(m);
    fmpz_clear(e);
    arb_clear(x);
    arb_clear(t);
    arb_clear(half);
}

static void
mul4(acb_t out, const acb_t a, const acb_t b, const acb_t c,
     const acb_t d, slong prec)
{
    acb_t t;
    acb_init(t);
    acb_mul(t, a, b, prec);
    acb_mul(t, t, c, prec);
    acb_mul(out, t, d, prec);
    acb_clear(t);
}

int
main(int argc, char *argv[])
{
    slong prec = 128;
    if (argc >= 2)
        prec = atol(argv[1]);
    if (prec < 64)
    {
        flint_fprintf(stderr, "precision must be at least 64 bits\n");
        return 2;
    }

    flint_set_num_threads(2);

    acb_t s, sm1, halfs, zratio, digamma, f_parts, f_product;
    acb_t A, Aprime, B, Bprime, G, Gprime, xi, xiprime;
    acb_t exponent, term, tmp;
    arb_t pi, logpi, half_logpi, abs_zeta, abs_xi, half;
    acb_ptr jet;

    acb_init(s); acb_init(sm1); acb_init(halfs); acb_init(zratio);
    acb_init(digamma); acb_init(f_parts); acb_init(f_product);
    acb_init(A); acb_init(Aprime); acb_init(B); acb_init(Bprime);
    acb_init(G); acb_init(Gprime); acb_init(xi); acb_init(xiprime);
    acb_init(exponent); acb_init(term); acb_init(tmp);
    arb_init(pi); arb_init(logpi); arb_init(half_logpi);
    arb_init(abs_zeta); arb_init(abs_xi); arb_init(half);
    jet = _acb_vec_init(2);

    set_exact_point(s);

    /* Dedicated rigorous Riemann--Siegel value and first derivative. */
    acb_dirichlet_zeta_jet_rs(jet, s, 2, prec);
    acb_abs(abs_zeta, jet + 0, prec);
    if (!arb_is_positive(abs_zeta))
    {
        flint_fprintf(stderr, "zeta ball contains zero\n");
        return 3;
    }

    arb_const_pi(pi, prec);
    arb_log(logpi, pi, prec);
    arb_mul_2exp_si(half_logpi, logpi, -1);
    arb_one(half);
    arb_mul_2exp_si(half, half, -1);

    acb_sub_ui(sm1, s, 1, prec);
    acb_mul_2exp_si(halfs, s, -1);
    acb_digamma(digamma, halfs, prec);
    acb_mul_2exp_si(digamma, digamma, -1);
    acb_div(zratio, jet + 1, jet + 0, prec);

    /* Assembly 1: corrected completed logarithmic derivative. */
    acb_inv(f_parts, s, prec);
    acb_inv(term, sm1, prec);
    acb_add(f_parts, f_parts, term, prec);
    acb_sub_arb(f_parts, f_parts, half_logpi, prec);
    acb_add(f_parts, f_parts, digamma, prec);
    acb_add(f_parts, f_parts, zratio, prec);

    /* Assembly 2: differentiate A(s) B(s) Gamma(s/2) zeta(s). */
    acb_mul(A, s, sm1, prec);
    acb_mul_2exp_si(A, A, -1);
    acb_sub_arb(Aprime, s, half, prec);

    acb_mul_arb(exponent, s, half_logpi, prec);
    acb_neg(exponent, exponent);
    acb_exp(B, exponent, prec);
    acb_mul_arb(Bprime, B, half_logpi, prec);
    acb_neg(Bprime, Bprime);

    acb_gamma(G, halfs, prec);
    acb_mul(Gprime, digamma, G, prec); /* digamma already contains factor 1/2 */

    mul4(xi, A, B, G, jet + 0, prec);
    acb_abs(abs_xi, xi, prec);
    if (!arb_is_positive(abs_xi))
    {
        flint_fprintf(stderr, "completed xi ball contains zero\n");
        return 4;
    }

    mul4(xiprime, Aprime, B, G, jet + 0, prec);
    mul4(term, A, Bprime, G, jet + 0, prec);
    acb_add(xiprime, xiprime, term, prec);
    mul4(term, A, B, Gprime, jet + 0, prec);
    acb_add(xiprime, xiprime, term, prec);
    mul4(term, A, B, G, jet + 1, prec);
    acb_add(xiprime, xiprime, term, prec);
    acb_div(f_product, xiprime, xi, prec);

    if (!acb_overlaps(f_parts, f_product))
    {
        flint_fprintf(stderr, "two completed-log-derivative assemblies are disjoint\n");
        return 5;
    }

    flint_printf("{\n");
    flint_printf("  \"schema\":\"riemann.xi-passivity-value-balls.v1\",\n");
    flint_printf("  \"producer\":{\"backend\":\"FLINT C acb_dirichlet_zeta_jet_rs\",\"precision_bits\":%wd,\"threads\":2,\"assembly_gate\":\"termwise completion intersected with differentiated completed product\"},\n", prec);
    flint_printf("  \"points\":[{\n");
    flint_printf("    \"id\":\"carrier44-x10-rs\",\n");
    flint_printf("    \"x\":{\"numerator\":\"1\",\"denominator\":\"1024\"},\n");
    flint_printf("    \"t\":{\"numerator\":\"20225875608343121406355\",\"denominator\":\"4294967296\"},\n");
    flint_printf("    \"f_via_xi\":"); print_acb_rectangle(f_product); flint_printf(",\n");
    flint_printf("    \"f_via_parts\":"); print_acb_rectangle(f_parts); flint_printf(",\n");
    flint_printf("    \"zeta_abs_lower\":");
    {
        fmpz_t za, zb, ze;
        fmpz_init(za); fmpz_init(zb); fmpz_init(ze);
        arb_get_interval_fmpz_2exp(za, zb, ze, abs_zeta);
        flint_printf("{\"mantissa\":"); print_fmpz_quoted(za);
        flint_printf(",\"exponent\":"); print_fmpz_quoted(ze); flint_printf("}\n");
        fmpz_clear(za); fmpz_clear(zb); fmpz_clear(ze);
    }
    flint_printf("  }],\n");
    flint_printf("  \"channels\":[{\"id\":\"scalar-carrier44-x10-rs\",\"kind\":\"scalar\",\"point\":\"carrier44-x10-rs\"}],\n");
    flint_printf("  \"declared_channel_ids\":[\"scalar-carrier44-x10-rs\"],\n");
    flint_printf("  \"classification\":\"primitive rigorous RS balls; exact checker decides sign\"\n");
    flint_printf("}\n");

    _acb_vec_clear(jet, 2);
    acb_clear(s); acb_clear(sm1); acb_clear(halfs); acb_clear(zratio);
    acb_clear(digamma); acb_clear(f_parts); acb_clear(f_product);
    acb_clear(A); acb_clear(Aprime); acb_clear(B); acb_clear(Bprime);
    acb_clear(G); acb_clear(Gprime); acb_clear(xi); acb_clear(xiprime);
    acb_clear(exponent); acb_clear(term); acb_clear(tmp);
    arb_clear(pi); arb_clear(logpi); arb_clear(half_logpi);
    arb_clear(abs_zeta); arb_clear(abs_xi); arb_clear(half);
    flint_cleanup();
    return 0;
}
