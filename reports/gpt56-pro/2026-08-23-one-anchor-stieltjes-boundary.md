# One-anchor Stieltjes reduction of the Xi boundary Loewner gate

Date: 2026-08-23  
Programme PR: `#729`  
Scientific status: **RH unproved**

## Context

The live branch already converts the two sharp last defects into dual
Vandermonde contour hierarchies:

```text
CRVH105330  complete critical-residue determinant hierarchy;
BCVH105330  complete boundary Cauchy-Vandermonde packet hierarchy.
```

The present continuation removes the arbitrary separated-packet geometry from
the boundary half.

## Exact analytic theorem

For a real analytic `H` on an interval and one fixed point `x_*`, define

\[
m_n=H^{(n+1)}(x_*)/(n+1)!
\]

and the Hankel matrices `L_k=[m_(r+s)]`. Then

```text
L_kP SD for every k at this one anchor
    iff
(X(x)-H(y))/(x-y) PSD on every finite real packet.
```

The proof uses the Hamburger moment theorem, Cauchy growth to force compact
support, the representation

\[
H(z)=H(x_*)+(z-x_*)\int  {d\mu(t)\over1-t(z-x_*)},
\]

and analytic continuation from one upper half-disk.

## Xi parity reduction

For the boundary Cauchy function of a definite-parh­Èa¤‘•É¥Ù…Ñ¥Ù”¥¸„)Íåµµ•ÑÉ¥Œİ¥¹‘½Ü°!€¥Ì½‘¸ĞÑ¡”…¹½¹¥…°…¹¡½Èé•É¼‘•™¥¹”()ql)q‰•Ñ…}¸õìÅq½Ù•ÈÉqÁ¤¥õq¥¹Ñ}íqÁ…ÉÑ¥…±q=µ•…ô)í¡qé•Ñ„¤½œ¡qé•Ñ„¥q½Ù•Éqé•Ñ…yìÉ¸¬Éõõ‘qé•Ñ„¸)qt()Q¡•¸Ñ¡”½µÁ±•Ñ”‰½Õ¹‘…Éä…Ñ”¥Ì•á…Ñ±ä()ql)mq‰•Ñ…}íÈ­ÍõuqÍÕ•ÄÀ°)qÅÅÕ…1mq‰•Ñ…}íÈ­Ì¬ÅõuqÍÕ•ÄÀ)qt()…Ğ•Ù•Éä½É‘•È¸ÅÕ¥Ù…±•¹Ñ±ä°()ql) ¡è¤õéq¥¹Ñ|Áyq¥¹™Ñäí‘q¹Ô¡Ì¥q½Ù•ÈÄµÍéxÉô)qt()™½È„Á½Í¥Ñ¥Ù”½µÁ…Ğµ•…ÍÕÉ”°½È½¸Ñ¡”Í…™”…á¥Ì()ql)í ¡¥ä¥q½Ù•È¥åô(õìÅq½Ù•ÈÉqÁ¤¥õq¥¹Ñ}íqÁ…ÉÑ¥…±q=µ•…ô)í¡qé•Ñ„¤½œ¡qé•Ñ„¥q½Ù•Éqé•Ñ…xÈ­åxÉõ‘qé•Ñ„(õq¥¹Ñ|Áyq¥¹™Ñäí‘q¹Ô¡Ì¥q½Ù•ÈÄ­ÍåxÉô¸)qt()Q¡ÕÌÑ¡”…±°µÁ…­•Ğ‰½Õ¹‘…ÉäÑ¡•½É•´¥Ì½¹”MÑ¥•±Ñ©•ÌµÑÉ…¹Í™½É´Ñ¡•½É•´™½È½¹”)±¥Ñ•É…°Í½ÕÉ”µ½İ¹•Í…±…È¸((ŒŒ½ÉÉ•Ğ½¹±ÕÍ¥½¸É…Á ()Ñ•áĞ)IY ÄÀÔÌÌÀ)9)=M ÄÀÔÌÔÀ€¡½É¥¥¸MÑ¥•±Ñ©•Ìµ!…¹­•°¡¥•É…É¡ä¤(€´øAILÄÀÔÈÈÀ9	I@ÄÀÔÈÈÀ(€´øI ¸)€()9•¥Ñ¡•È¡¥•É…É¡ä¥ÌÁÉ½Ù•™½È™¥á•±½Üµ½É‘•Èa¤¸((ŒŒ¥É•İ…±°()Q¡”É…Ñ¥½¹…°½‘™Õ¹Ñ¥½¸()ql) ¡è¤õè Ä¼ Ä­è¤´Ä¬Ä¼ Äµè¤¤¼Ğ)qt()¡…ÌÁ½Í¥Ñ¥Ù”™¥ÉÍĞ…¹Í•½¹½¹™±Õ•¹Ğµ…ÑÉ¥•Ì°‰ÕĞ¥ÑÌÑ¡¥É½¹™±Õ•¹Ğ)‘•Ñ•Éµ¥¹…¹Ğ¥Ì€´Ä¼ÄÙ€¸Í•±•Ñ•Ñ¡É•”µ¹½‘”Á…­•Ğ¡…Ì…±°½¹”´½Ñİ¼µ¹½‘”)ÁÉ¥¹¥Á…°É•ÍÑÉ¥Ñ¥½¹ÌÁ½Í¥Ñ¥Ù”…¹‘•Ñ•Éµ¥¹…¹Ğ€´ÄØ¼ÈÀÈÕ€¸Q¡”Ñ¡•½É•´¥Ì…¸)…±°µ½É‘•ÈÉ•‘ÕÑ¥½¸°¹½Ğ„™¥¹¥Ñ”µ½É‘•È‰½½ÑÍÑÉ…À¸((ŒŒI•Á±…ä()Ñ•áĞ)AMM}a|ÄÀÔÌÔÁ}=9}9!=I}1=]9I}!5	UIH(ÄÔä•á…ĞÉ…Ñ¥½¹…°¡•­Ì(ÔÁŒÙŒÈÙŒÄÄÄÔÕ™ÍŒÌÕĞäàÌÁ˜Õ™˜Ù˜áˆÌÉˆÁ˜ÁˆØÈäÑ‰˜ÜÍ˜ÀÑ•„İ…•••Œå…•”Ğ)€()Q¡”É•Á±…ä…ÕÑ¡•¹Ñ¥…Ñ•Ì™¥¹¥Ñ”É…Ñ¥½¹…°…Ñ½µ¥Œµ½‘•±Ì½¹±ä¸IY ÄÀÔÌÌÁ€°)=M ÄÀÔÌÔÁ€°Ñ¡”µ½Ù¥¹œµÍ…‘‘±”±½‰…°‘½µ¥¹…¹”•ÍÑ¥µ…Ñ”°…¹I É•µ…¥¸½Á•¸¸