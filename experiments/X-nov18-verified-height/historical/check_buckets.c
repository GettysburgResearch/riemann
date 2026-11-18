/* Reproduce the original rounded bin selection for each actual precision.
   Link with the unmodified historical win_zeta.c, which defines arb_get_d. */
#include <stdio.h>
#include <arb.h>
extern double arb_get_d(arb_t x);

int main(void)
{
    const long precs[] = {100, 120, 128, 144, 152, 160};
    for (size_t j=0; j<sizeof(precs)/sizeof(precs[0]); j++)
    {
        const long prec=precs[j], hp=prec+50;
        arb_t root_pi, two_pi, s, exact, delta, limit;
        arb_init(root_pi); arb_init(two_pi); arb_init(s);
        arb_init(exact); arb_init(delta); arb_init(limit);
        arb_const_pi(root_pi,hp); arb_sqrt(root_pi,root_pi,hp);
        arb_const_pi(two_pi,prec); arb_mul_2exp_si(two_pi,two_pi,1);
        arb_set_str(limit,"0.500021",prec);
        for (long n=1; n<=768000; n++)
        {
            arb_mul_ui(s,root_pi,n,hp); arb_log(s,s,hp);
            arb_div(s,s,two_pi,prec);
            long bucket=(long) (arb_get_d(s)*5376.0+0.5);
            arb_mul_ui(exact,s,5376,prec); arb_sub_ui(delta,exact,bucket,prec);
            arb_abs(delta,delta);
            if (bucket<1 || bucket>=16384 || !arb_lt(delta,limit))
            {
                printf("Failed precision %ld, n %ld\n",prec,n);
                return 1;
            }
        }
        printf("precision %ld: all 768000 residuals below 0.500021/5376\n",prec);
        arb_clear(root_pi); arb_clear(two_pi); arb_clear(s);
        arb_clear(exact); arb_clear(delta); arb_clear(limit);
    }
    return 0;
}
