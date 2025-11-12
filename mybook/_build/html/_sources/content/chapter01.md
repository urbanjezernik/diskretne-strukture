```{raw} html
<style>
  body { counter-reset: chapter 0 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Izjavni račun

V tem poglavju si bomo pogledali, kako *formaliziramo* preproste izjave in kako *dokazujemo* njihovo veljavnost oziroma neveljavnost.

## Izjave in izjavni vezniki

<span class="definicija">Izjava</span> je poved, ki je bodisi resnična bodisi lažna.

<div class="zgled">

- Ena in ena je tri. *Lažna izjava.*

- Ena in ena je dve. *Resnična izjava.*

- Koliko je ena in ena? *Ni izjava.*

- Pojdimo na kavo! *Ni izjava.*

</div>

Izjave lahko razdelimo na dve skupini *po vsebini*, in sicer:

- <span class="definicija">resnične izjave</span>, ki imajo resničnostno vrednost $1$ ali $\top$ ali `true`,

- <span class="definicija">lažne izjave</span>, ki imajo resničnostno vrednost $0$ ali $\bot$ ali `false`.

Po *zgradbi* oziroma *obliki* pa izjave razdelimo na:

- <span class="definicija">osnovne</span>, ki ne vsebujejo izjavnih veznikov,

- <span class="definicija">sestavljene</span>, ki vsebujejo izjavne veznike.

<div class="zgled">

- Vreme je lepo. *Osnovna izjava.*

- Špela gre v hribe. *Osnovna izjava.*

- Vreme je lepo *in* Špela gre v hribe. *Sestavljena izjava.*

- *Če* je vreme lepo, *potem* gre Špela v hribe. *Sestavljena izjava.*

- Špela *ne* gre v hribe. *Sestavljena izjava.*

</div>

Naj bo $n \in \NN_0$. <span class="definicija">Izjavni veznik reda $n$</span> (ali <span class="definicija">$n$-mestni izjavni veznik</span>) je funkcija, ki vsaki urejeni $n$-terici ničel in enic priredi vrednost $0$ ali $1$.

<div class="zgled">

- Primer izjavnega veznika reda $1$ je <span class="definicija">negacija</span>. Simbol za ta veznik je $\lnot$. Če je $p$ izjava, njeno negacijo označimo kot $\lnot p$ in preberemo kot *ne $p$* ali kot *ni res, da velja $p$*. Negacija $1$-terici $0$ priredi vrednost $1$, $1$-terici $1$ pa priredi vrednost $0$.

  | $p$ | $\lnot p$ |
  |:-----:|:-----------:|
  |   0   |      1      |
  |   1   |      0      |

  Resničnostna tabela negacije

- Oglejmo si nekaj pomembnih dvomestnih izjavnih veznikov. Njihovi predpisi so zbrani v tabeli.

  - <span class="definicija">Konjunkcija</span> izjav $p$ in $q$ ima simbol $p \land q$, kar preberemo kot *$p$ in $q$*.

  - <span class="definicija">Disjunkcija</span> izjav $p$ in $q$ ima simbol $p \lor q$, kar preberemo kot *$p$ ali $q$*.

  - <span class="definicija">Implikacija</span> izjav $p$ in $q$ ima simbol $p \Rightarrow q$, kar preberemo kot *če $p$, potem $q$* ali kot *iz $p$ sledi $q$* ali kot *$p$ je zadosten pogoj za $q$* ali *kot $q$ je potreben pogoj za $p$*.

  - <span class="definicija">Ekvivalenca</span> izjav $p$ in $q$ ima simbol $p \Leftrightarrow q$, kar preberemo kot *$p$ natanko tedaj, ko $q$* ali kot *$p$, če in samo če $q$* ali kot *$p$ je ekvivalentno $q$*.

  | $p$ | $q$ | $p \land q$ | $p \lor q$ | $p \Rightarrow q$ | $p \Leftrightarrow q$ |
  |:--:|:--:|:--:|:--:|:--:|:--:|
  | 1 | 1 | 1 | 1 | 1 | 1 |
  | 1 | 0 | 0 | 1 | 0 | 0 |
  | 0 | 1 | 0 | 1 | 1 | 0 |
  | 0 | 0 | 0 | 0 | 1 | 1 |

  Resničnostna tabela nekaterih pomembnih dvomestnih izjavnih veznikov

- Izjavni veznik reda $0$ je funkcija iz množice urejenih $0$-teric ničel in enic. Obstaja natanko ena taka $0$-terica, in sicer *prazna $0$-terica*. Izjavni veznik reda $0$ je torej natanko določen s sliko te $0$-terice, za kar imamo dve možnosti, $0$ ali $1$.

  - Izjavni veznik reda $0$, ki ima vselej resničnostno vrednost $0$, imenujemo <span class="definicija">0</span> in preberemo kot *lažna izjava*.

  - Izjavni veznik reda $0$, ki ima vselej resničnostno vrednost $1$, imenujemo <span class="definicija">1</span> in preberemo kot *resnična izjava*.

  Izjavnima veznikoma reda $0$ pravimo tudi <span class="definicija">izjavni konstanti</span>.

</div>

Glede na zgornjo obravnavamo izjavnih veznikov redov $0$, $1$ in $2$ se lahko vprašamo, koliko je vseh $n$-mestnih izjavnih veznikov za poljuben $n \in \NN_0$. Vsak tak veznik je enolično določen s svojo resničnostno tabelo, v kateri zabeležimo vrednosti veznika v <span class="definicija">izjavnih spremenljivkah</span> $p_1, p_2, \dots, p_n$, kjer vsak $p_i$ zavzema vrednosti $0$ ali $1$.

| $p_1$ | $p_1$ | $\cdots$ | $p_n$ | veznik($p_1$, $p_2$, …, $p_n$) |
|:--:|:--:|:--:|:--:|:--:|
| 1 | 1 | $\cdots$ | 1 | 0 ali 1 *(dve možnosti)* |
| 1 | 1 | $\cdots$ | 0 | 0 ali 1 *(dve možnosti)* |
| $\vdots$ | $\vdots$ |  | $\vdots$ | $\vdots$ |
| 0 | 0 | $\cdots$ | 0 | 0 ali 1 *(dve možnosti)* |

Resničnostna tabela $n$-mestnega izjavnega veznika

Število vseh $n$-mestnih izjavnih veznikov torej izračunamo tako, da preštejemo število vseh možnih resničnostnih tabel. Število vrstic tabele je enako $2^n$, število vseh tabel pa je zato enako $2^{2^n}$.

| $n$ | $2^n$ |       $2^{2^n}$        |
|:-----:|:-------:|:------------------------:|
|   0   |    1    |            2             |
|   1   |    2    |            4             |
|   2   |    4    |            16            |
|   3   |    8    |           256            |
|   4   |   16    |          65536           |
|   5   |   32    |  $\sim 4 \cdot 10^9$   |
|   6   |   64    | $\sim 2 \cdot 10^{19}$ |

Hitra rast števila $n$-mestnih izjavnih veznikov

## Izjavni izrazi

<span class="definicija">Izjavni izraz</span> definiramo induktivno na naslednji način:

- *Osnovni izraz 1:* Vsaka *izjavna konstanta* (torej $0$ ali $1$) je izjavni izraz.

- *Osnovni izraz 2:* Vsaka *izjavna spremenljivka* $p_1, p_2, \dots$ je izjavni izraz.

- *Sestavljeni izraz:* Če je $f$ *izjavni veznik* reda $n$ in so $A_1, A_2, \dots, A_n$ izjavni izrazi, potem je $(f(A_1,A_2,\dots,A_n))$ izjavni izraz.

Izjavni izrazi so torej izjave, ki jih dobimo iz $0,1$ in izjavnih spremenljivk z (večkratno) uporabo izjavnih veznikov.

<div class="zgled">

Naj bodo $p,q,r$ izjavne spremenljivke. Tvorimo lahko izjavne izraze $(p \Rightarrow q)$, $(\lnot r)$, $((p \Rightarrow q) \land (\lnot r))$, …

</div>

Pri pisanju bolj zakompliciranih izjavnih izrazov se prične pojavljati mnogo oklepajev. V izogib pisanju prevelikega števila teh oklepajev uporabljamo naslednji <span class="definicija">dogovor o prednostnem vrstnem redu veznikov</span>:

- $\lnot$ ima prednost pred dvomestnimi vezniki,

- veznik iz $(\land, \lor, \Rightarrow, \Leftrightarrow)$ ima prednost pred vezniki desno od sebe,

- če isti veznik nastopi večkrat zapored, ima levi nastop prednost pred desnim,

- zunanji oklepaj spuščamo.

<div class="zgled">

- Izjavni izraz $(p \Rightarrow (q \land r))$ pišemo krajše kot $p \Rightarrow q \land r$.

- Izraz $p \Rightarrow q \Rightarrow r \Rightarrow s$ je okrajšava za izjavni izraz $(((p \Rightarrow q) \Rightarrow r) \Rightarrow s)$.

- Izraz $p \lor \lnot q \Leftrightarrow r \Rightarrow q$ je okrajšava za izjavni izraz $(( p \lor (\lnot q)) \Leftrightarrow (r \Rightarrow p))$.

</div>

Izjavni izrazi vsebujejo izjavne spremenljivke, zato določajo neko resničnostno tabelo in s tem tudi nek izjavni veznik.

<div class="zgled">

Naj bodo $p,q,r$ izjavne spremenljivke in naj bo $f(p,q,r) = (p \Rightarrow q) \land \lnot r$ izjavni izraz. Izračunamo lahko resničnostno tabelo tega izraza in na ta način lahko na $f$ gledamo kot na izjavni veznik reda $3$.

| $p$ | $q$ | $r$ | $(p \Rightarrow q) \land \lnot r$ |
|:-----:|:-----:|:-----:|:-----------------------------------:|
|   1   |   1   |   1   |                  0                  |
|   1   |   1   |   0   |                  1                  |
|   1   |   0   |   1   |                  0                  |
|   1   |   0   |   0   |                  0                  |
|   0   |   1   |   1   |                  0                  |
|   0   |   1   |   0   |                  1                  |
|   0   |   0   |   1   |                  0                  |
|   0   |   0   |   0   |                  1                  |

Resničnostna tabela izjavnega izraza $(p \Rightarrow q) \land \lnot r$

</div>

## Tavtologije in enakovredni izrazi

Če je izjavni izraz *resničen* pri vseh naborih svojih izjavnih spremenljivk, mu rečemo <span class="definicija">tavtologija</span>. Če je *lažen* pri vseh naborih, mu rečemo <span class="definicija">protislovje</span>. Če ni niti tavtologija niti protislovje, je <span class="definicija">kontingenten</span>.

<div class="zgled">

- Izjavna izraza $1$ in $p \lor \lnot p$ sta tavtologiji.

- Izjavna izraza $0$, $p \land \lnot p$ sta protislovji.

- Izračunajmo resničnostne tabele izjavnih izrazov $p \Rightarrow q \Leftrightarrow \lnot p \lor q$, $p \land \lnot (q \Rightarrow p)$ in $p \land (\lnot q \lor p)$.

  | $p$ | $q$ | $p \Rightarrow q \Leftrightarrow \lnot p \lor q$ | $p \land \lnot (q \Rightarrow p)$ | $p \land (\lnot q \lor p)$ |
  |:--:|:--:|:--:|:--:|:--:|
  | 1 | 1 | 1 | 0 | 1 |
  | 1 | 0 | 1 | 0 | 1 |
  | 0 | 1 | 1 | 0 | 0 |
  | 0 | 0 | 1 | 0 | 0 |

  Resničnostne tabele treh izjavnih izrazov

  Vidimo, da je prvi izraz tavtologija, drugi protislovje, tretji pa kontingenten.

  <div class="domacanaloga">

  Prepričaj se, da je resničnostna tabela izjavnega izraza $p \land (\lnot q \lor p)$ enaka resničnosti tabeli izjavnega izraza $p$. Sklepaj, da je izjava $p \land (\lnot q \lor p) \Leftrightarrow p$ tavtologija. Na podoben način se prepričaj, da je izraz $p \Rightarrow q \Leftrightarrow \lnot q \Rightarrow \lnot p$ tavtologija.

  </div>

</div>

Naj bosta $A$ in $B$ izjavna izraza. Kadar je $A \Leftrightarrow B$ tavtologija, tedaj rečemo, da sta izraza $A$ in $B$ <span class="definicija">enakovredna</span>. Z drugimi besedami, izraza $A$ in $B$ sta enakovrednosta, kadar imata enaka stolpca v resničnostni tabeli. V tem primeru uporabimo oznako $A \sim B$.

<div class="zgled">

Velja $p \Rightarrow q \sim \lnot p \lor q \sim \lnot q \Rightarrow \lnot p$ in $p \land (\lnot q \lor p) \sim p$.

</div>

Enakovrednemu paru izjavnih izrazov $A \sim B$ rečemo <span class="definicija">zakon izjavnega računa</span>. V vsakem izjavnem izrazu lahko poljuben izraz zamenjamo z enakovrednim in s tem poenostavimo izjavni izraz.

<div class="zgled">

Velja
```{math}
p \land (\lnot q \lor p) \Rightarrow (\lnot q \Rightarrow \lnot p) \sim
    p \Rightarrow (p \Rightarrow q).
```

</div>

Navedimo nekaj uporabnih zakonov izjavnega računa, ki veljajo za vse izjavne izraze $A,B,C$.

- $\lnot 0 \sim 1$, $\lnot 1 \sim 0$

- $A \land 0 \sim 0$, $A \land 1 \sim A$, $A \lor 0 \sim A$, $A \lor 1 \sim 1$

- $A \land A \sim A$, $A \lor A \sim A$ (<span class="definicija">idempotentnost</span>)

- $A \land B \sim B \land A$, $A \lor B \sim B \lor A$ (<span class="definicija">komutativnost</span>)

- $A \land (B \land C) \sim (A \land B) \land C$, $A \lor (B \lor C) \sim (A \lor B) \lor C$ (<span class="definicija">asociativnost</span>)

- $A \land (A \lor B) \sim A$, $A \lor (A \land B) \sim A$ (<span class="definicija">absorpcija</span>)

- $A \land (B \lor C) \sim (A \land B) \lor (A \land C)$, $A \lor (B \land C) \sim (A \lor B) \land (A \lor C)$ (<span class="definicija">distributivnost</span>)

- $\lnot \lnot A \sim A$ (<span class="definicija">dvojna negacija</span>)

- $\lnot (A \land B) \sim \lnot A \lor \lnot B$, $\lnot (A \lor B) \sim \lnot A \land \lnot B$ (<span class="definicija">De Morganova zakona</span>)

- $A \Rightarrow B \sim \lnot B \Rightarrow \lnot A$ (<span class="definicija">kontrapozicija</span>), $A \Rightarrow B \sim \lnot A \lor B$

- $A \Leftrightarrow B \sim (A \Rightarrow B) \land (B \Rightarrow A)$

<div class="zgled">

Izjavni izraz iz zadnjega zgleda lahko z naštetimi zakoni poenostavimo do
```{math}
p \Rightarrow (p \Rightarrow q) \sim
    \lnot p \lor (\lnot p \lor q) \sim
    (\lnot p \lor \lnot p) \lor q \sim
    \lnot p \lor q \sim
    p \Rightarrow q.
```

</div>

## DNO in KNO

Do sedaj smo govorili o tem, kako za dan izjavni izraz določimo njegovo resničnostno tabelo. V tem razdelku si bomo zastavili obratno nalogo. Recimo, da je dana resničnostna tabela nekega kontingentnega izjavnega izraza $A$. Pokazali bomo, da lahko zgolj z uporabo izjavnih veznikov $\lnot$, $\land$, $\lor$ sestavimo izjavni izraz $D$, tako da bo $A \sim D$. Za začetek si oglejmo, kako to naredimo na enem konkretnem primeru.

<div class="zgled">

Naj bo izjavni izraz $A$ dan z resničnostno tabelo $T$.

| $p$ | $q$ | $r$ | $A$ |
|:-----:|:-----:|:-----:|:-----:|
|   1   |   1   |   1   |   0   |
|   1   |   1   |   0   |   1   |
|   1   |   0   |   1   |   0   |
|   1   |   0   |   0   |   0   |
|   0   |   1   |   1   |   0   |
|   0   |   1   |   0   |   1   |
|   0   |   0   |   1   |   0   |
|   0   |   0   |   0   |   1   |

Resničnostna tabela $T$ izjavnega izraza $A$

Iskani izjavni izraz $D$ mora biti resničen natanko v 2., 6. in 8. vrstici tabele $T$. To je res natanko tedaj, ko velja $p \land q \land \lnot r$ ali $\lnot p \land q \land \lnot r$ ali $\lnot p \land \lnot q \land \lnot r$. Torej lahko vzamemo preprosto
```{math}
D = (p \land q \land \lnot r) \lor (\lnot p \land q \land \lnot r) \lor (\lnot p \land \lnot q \land \lnot r)
```
in res velja $D \sim A$. Dobljeni izjavni izraz $D$ lahko še nekoliko poenostavimo.

<div class="domacanaloga">

Z uporabo zakonov izjavnega računa se prepričaj, da velja $D \sim \lnot (p \Rightarrow q \Rightarrow r)$.

</div>

</div>

Naj bo zdaj $A$ poljuben kontingenten izjavni izraz in $T$ njegova resničnostna tabela. <span class="definicija">Disjunktivna normalna oblika</span> izraza $A$ je disjunkcija *osnovnih konjunkcij* tistih vrstic, kjer je $A$ resničen. Pri tem je osnovna konjunkcija neke vrstice konjunkcija tistih izjavnih spremenljivk, ki so v tej vrstici resnične, in negacij tistih izjavnih spremenljivk, ki so v tej vrstici lažne. Disjunktivno normalno obliko izraza $A$ krajše pišemo kot $\DNO(A)$.

<div class="zgled">

V zadnjem zgledu je $\DNO(A) = D$.

</div>

Disjunktivna normalna oblika $\DNO(A)$ je izjavni izraz, ki je zapisan le z uporabo izjavnih veznikov $\lnot$, $\land$, $\lor$. Preverimo še, da je ta izraz res enakovreden začetnemu izrazu $A$.

<div class="trditev">

Naj bo $A$ kontingenten izraz. Potem je $A \sim \DNO(A)$.

</div>

<div class="dokaz">

Naj bo $T$ resničnostna tabela izraza $A$. Naj bo $i$ poljubna vrstica $T$. Dokazati želimo, da imata $T$ in $\DNO(A)$ v tej vrstici enako resničnostno vrednost.

Če je $A$ resničen v vrstici $i$:  
Po definiciji disjunktivne normalne oblike je $\DNO(A)$ disjunkcija osnovnih konjunkcij vrstic $T$. V posebnem osnovna konjunkcija vrstice $i$ nastopa v $\DNO(A)$. Ta osnovna konjunkcija je v vrstici $i$ resnična, zato je resnična tudi disjunkcija $\DNO(A)$.

Če je $\DNO(A)$ resničen v vrstici $i$:  
V tem primeru mora biti resničen vsaj en člen disjunkcije $\DNO(A)$, torej mora biti v vrstici $i$ resnična osnovna konjunkcija neke vrstice $j$. Osnovna konjunkcija vrstice $j$ je izraz, ki je v vrstici $j$ resničen, v vseh ostalih vrsticah pa lažen. Od tod sledi, da je $i = j$. Torej $\DNO(A)$ vsebuje osnovno konjunkcijo vrstice $i$, zato je $A$ resničen v vrstici $i$.

Res imata torej $T$ in $\DNO(A)$ enake resničnostne vrednosti, torej sta $A$ in $\DNO(A)$ enakovredna.

</div>

V sestavljanju disjunktivne normalne oblike smo opazovali vrstice, kjer je dan izjavni izraz $A$ resničen. Analogno bi lahko opazovali vrstice, kjer je izraz $A$ lažen, in sestavili izjavni izraz, ki bo *lažen* natanko v vrsticah, v katerih je $A$ lažen. Na primeru pojasnimo, kako lahko na ta način dobimo alternativen izjavni izraz, ki je zopet izražen le z vezniki $\lnot$, $\land$, $\lor$ in je enakovreden izrazu $A$.

<div class="zgled">

Naj bo $T$ resničnostna tabela izjavnega izraza $A$ iz predzadnjega zgleda. Ta tabela je lažna v vrsticah $1,3,4,5,7$. Sestavimo izjavni izraz $K$, ki bo lažen natanko v teh vrsticah. To je enakovredno zahtevi, da je $K$ resničen natanko tedaj, ko nismo v nobeni od vrstic $1,3,4,5,7$. Slednjo zahtevo lahko izrazimo kot konjunkcijo *osnovnih disjunkcij* vrstic $1,3,4,5,7$, se pravi kot
```{math}
K = 
    (\lnot p \lor \lnot q \lor \lnot r) \land
    (\lnot p \lor q \lor \lnot r) \land
    (\lnot p \lor q \lor r) \land
    (o \lor \lnot q \lor \lnot r) \land
    (p \lor q \lor \lnot r).
```
Tako sestavljenemu izravnemu izrazu $K$ pravimo <span class="definicija">konjunktivna normalna oblika</span> izraza $A$, krajše $\KNO(A)$. Sorodno kot za disjunktivno normalno obliko se prepričamo, da velja $\KNO(A) \sim A$.

</div>

## Sklepanje v izjavnem računu

<span class="definicija">Sklep</span> je končno zaporedje izjav $p_1, p_2, \dots, p_k, z$. Pri tem izjavam $p_1, p_2, \dots, p_k$ pravimo <span class="definicija">predpostavke</span>, izjavi $z$ pa <span class="definicija">zaključek</span>.

<div class="zgled">

Opazujmo naslednje zaporedje izjav.

$p_1$:  
Če je ta žival ptič, potem ima krila.

$p_2$:  
Ta žival nima kril.

$z$:  
Ta žival ni ptič.

Imamo torej sklep $p_1, p_2, z$. Ta sklep lahko zapišemo nekoliko bolj natančno z upoštevanjem sestavljene strukture izjav v sklepu. Uvedimo izjavi $p$ in $q$ kot:

$p$:  
Ta žival je ptič.

$q$:  
Ta žival ima krila.

Sklep $p_1, p_2, z$ lahko torej zapišemo v obliki $p \Rightarrow q, \ \lnot q, \ \lnot p$.

</div>

Zaporedje izjavnih izrazov $A_1, A_2, \dots, A_k, B$ je <span class="definicija">pravilen sklep</span> (rekli bomo tudi <span class="definicija">veljaven sklep</span>), če je zaključek $B$ resničen pri vseh tistih naborih izjavnih spremenljivk, pri katerih so resnične vse predpostavke $A_1, A_2, \dots, A_k$. V tem primeru pišemo $A_1, A_2, \dots, A_k \models B$.

<div class="zgled">

Sklep iz zadnjega zgleda smo zapisali v obliki $p \Rightarrow q, \ \lnot q, \ \lnot p$. Če pri tem gledamo na $p$ in $q$ kot na izjavni spremenljivki (in ne kot oznaki za konkretne izjave), se lahko vprašamo o veljavnosti sklepa. V ta namen sestavimo resničnostno tabelo vseh izjavnih izrazov v sklepu.

| $p$ | $q$ | $p \Rightarrow q$ | $\lnot q$ | $\lnot p$ |
|:-----:|:-----:|:-------------------:|:-----------:|:-----------:|
|   1   |   1   |          1          |      0      |      0      |
|   1   |   0   |          0          |      1      |      0      |
|   0   |   1   |          1          |      0      |      1      |
|   0   |   0   |          1          |      1      |      1      |

Resničnostna tabela sklepa $p \Rightarrow q, \ \lnot q \models \lnot p$

Edini nabor izjavnih spremenljivk, pri katerih sta resnični obe predpostavki sklepa, je nabor $(p,q)=(0,0)$. Pri tem naboru je resničen tudi zaključek sklepa. Sklep je torej veljaven, se pravi $p \Rightarrow q, \ \lnot q \models \lnot p$.

</div>

Zabeležimo nekaj pomembnih veljavnih sklepov, ki jim pravimo <span class="definicija">osnovna pravila sklepanja</span>.

- $A, \ A \Rightarrow B \models B$ (<span class="definicija">modus ponens (MP)</span>)

- $A \Rightarrow B, \ \lnot B \models \lnot A$ (<span class="definicija">modus tollens (MT)</span>)

- $A \lor B, \ \lnot B \models A$ (<span class="definicija">disjunktivni silogizem (DS)</span>)

- $A \Rightarrow B, \ B \Rightarrow C \models A \Rightarrow C$ (<span class="definicija">hipotetični silogizem (HS)</span>)

- $A \land B \models A$ (<span class="definicija">poenostavitev (Po)</span>)

- $A, \ B \models A \land B$ (<span class="definicija">združitev (Zd)</span>)

- $A \models A \lor B$ (<span class="definicija">pridružitev (Pr)</span>)

Drugo od teh pravil smo spoznali v zadnjem zgledu in se tudi prepričali o veljavnosti. Na podoben način preverimo veljavnosti preostalih.

Pri večjem številu izjavnih spremenljivk je lahko preverjanje veljavnosti sklepa z resničnostno tabelo precej zamudno.

<div class="zgled">

Ali je sklep
```{math}
p \Rightarrow q, \ p \lor r, \ q \Rightarrow s, \ r \Rightarrow t, \ \lnot s \models t
```
veljaven? Ta sklep vsebuje $5$ izjavnih spremenljivk, zato bi za preverjanje veljavnosti morali sestaviti resničnostno tabelo z $2^5 = 32$ vrsticami.

</div>

V takih primerih si lahko pomagamo z naslednjim alternativnim načinom preverjanja veljavnosti sklepa.

<div class="izrek">

Naj bodo $A_1, A_2, \dots, A_k$ izjavni izrazi. Če obstaja zaporedje izjavnih izrazov $B_1, B_2, \dots, B_n$, tako da za vsak $i = 1, 2, \dots, n$ velja vsaj ena od možnosti:

1.  $B_i$ je eden on $A_1, A_2, \dots, A_k$,

2.  $B_i$ je tavtologija,

3.  $B_i \sim B_j$ za nek $j < i$,

4.  $B_i$ logično sledi iz $B_1, B_2, \dots, B_{i-1}$ po enem od osnovnih pravil sklepanja,

potem velja $A_1, A_2, \dots, A_k \models B_n$.

</div>

<div class="dokaz">

Dokazujemo z indukcijo na $n$.

Baza indukcije je $n = 1$. V tem primeru je po predpostavki izjavni izraz $B_1$ lahko le eden od $A_1, A_2, \dots, A_k$ ali tavtologija. V vsakem od teh primerov velja $A_1, A_2, \dots, A_k \models B_n$.

Predpostavimo zdaj, da trditev že velja za $1, 2, \dots, n-1$ in dokažimo veljavnost za $n$. Drži torej $A_1, A_2, \dots, A_k \models B_j$ za vsak $j = 1, 2, \dots, n-1$. Obravnavajmo različne možnosti glede na to, katera od predpostavk velja za $B_n$.

1.  Če je $B_n$ eden od $A_1, A_2, \dots, A_k$, potem velja $A_1, A_2, \dots, A_k \models B_n$.

2.  Če je $B_n$ tavtologija, potem velja $A_1, A_2, \dots, A_k \models B_n$.

3.  Če je $B_n \sim B_j$ za nek $j < n$, potem po indukcijski predpostavki $A_1, A_2, \dots, A_k \models B_j$ velja $A_1, A_2, \dots, A_k \models B_n$.

4.  Naj nazadnje $B_n$ logično sledi iz $B_1, B_2, \dots, B_{n-1}$. Ker vsak $B_j$ za $j < n$ logično sledi iz $A_1, A_2, \dots, A_k$, velja tudi $A_1, A_2, \dots, A_k \models B_n$.

</div>

<div class="zgled">

S pomočjo izreka o naravni dedukciji utemeljimo veljavnost sklepa iz zadnjega zgleda.

| $i$ | $B_i$             | utemeljitev  |
|:------|:--------------------|:-------------|
| 1     | $p \Rightarrow q$ | predpostavka |
| 2     | $p \lor r$        | predpostavka |
| 3     | $q \Rightarrow s$ | predpostavka |
| 4     | $r \Rightarrow t$ | predpostavka |
| 5     | $\lnot s$         | predpostavka |
| 6     | $p \Rightarrow s$ | HS(1,3)      |
| 7     | $\lnot p$         | MT(6,5)      |
| 8     | $r \lor p$        | $\sim$ 2   |
| 9     | $r$               | DS(8,7)      |
| 10    | <u>$t$</u>        | MP(9,4)      |

Uporaba naravne dedukcije za dokazovanje veljavnosti sklepa

</div>

Do zdaj smo se ukvarjali z dokazovanjem veljavnosti danega sklepa. Oglejmo si še, kako pokažemo, da sklep *ni* veljaven. Namesto tega, da sestavimo resničnostno tabelo vseh izjavnih izrazov v sklepu, lahko preprosteje pokažemo le na tisto vrstico resničnoste tabele, ki opazi neveljavnost sklepa. To pomeni, da poiščemo nek nabor vrednosti izjavnih spremenljivk, pri katerem so vse predpostavke resnične, zaključek pa je lažen. Takemu naboru rečemo <span class="definicija">protiprimer</span>.

<div class="zgled">

Opazujmo naslednji sklep.

$p_1$:  
Ta žival ima krila ali pa ni ptič.

$p_2$:  
Če je ta žival pritč, potem leže jajca.

$p_3$:  
Ta žival nima kril.

$z$:  
Torej ta žival ne leže jajc.

Ta sklep lahko zapišemo nekoliko bolj natančno, če uvedemo izjave $p,q,r$ kot:

$p$:  
Ta žival ima krila.

$q$:  
Ta žival je ptič.

$r$:  
Ta žival leže jajca.

Sklep lahko torej zapišemo na naslednji način:
```{math}
p \lor \lnot q, \ q \Rightarrow r, \ \lnot p \models \lnot r.
```

Poiščimo protiprimer. Želimo, da so resnične vse predpostavke, zaključek pa lažen. Vzeti moramo torej $r = 1$ in $p = 0$, od koder iz prve predpostavke dobimo še $q = 0$. S to izbiro je tudi druga predpostavka resnična. Nabor $p = 0, q = 0, r = 1$ je torej protiprimer, ki opazi, da sklep ni pravilen.

Če to prevedemo nazaj v človeški jezik, protiprimer torej predstavlja žival, ki nima kril, ni ptič in leže jajca. Konkretna taka žival je na primer kača ali krokodil.

</div>

Pri dokazovanju bolj kompleksnih sklepov si lahko včasih pomagamo tudi s kakšnimi <span class="definicija">pomožnimi sklepi</span>. Pogledali si bomo tri take osnovne pomožne sklepe, in sicer pogojni sklep, sklepanje s protislovjem in analiza primerov. Vse te pomožne sklepe bomo izpeljali s pomočjo naslednje trditve.

<div class="trditev">

Velja $A_1, A_2, \dots, A_k \models B$, če in samo če je $A_1 \land A_2 \land \dots \land A_k \Rightarrow B$ tavtologija.

</div>

<div class="dokaz">

Predpostavimo najprej, da velja $A_1, A_2, \dots, A_k \models B$. Če je $A_1 \land A_2 \land \cdots \land A_k$ resnična izjava, potem so resnične vse izjave $A_i$ za $i = 1,2, \dots, k$, torej so vse predpostavke $A_1, A_2, \dots, A_k$ resnične. Od tod sledi, da je resničen tudi zaključek $B$. Torej je $A_1 \land A_2 \land \cdot \land A_k \Rightarrow B$ tavtologija.

Predpostavimo sedaj, da je $A_1 \land A_2 \land \cdot \land A_k \Rightarrow B$ tavtologija. Dokazati želimo veljavnost sklepa $A_1, A_2, \dots, A_k \models B$. Predpostavimo torej, da so resnične vse predpostavke $A_1, A_2, \dots, A_k$. Potem je resnična tudi njihova konjunkcija $A_1 \land A_2 \land \cdots \land A_k$. Iz predpostavke od tod sledi, da mora biti resnična tudi izjava $B$. Sklep $A_1, A_2, \dots, A_k \models B$ je torej veljaven.

</div>

<span class="definicija">Pogojni sklep</span> (PS) uporabimo, kadar dokazujemo sklep, v katerem ima zaključek obliko implikacije. Če želimo sklepati na zaključek $B \Rightarrow C$, dodamo izjavo $B$ med predpostavke in skušamo sklepati na zaključek $C$. Veljavnost tega pomožnega sklepa sledi iz naslednjega izreka.

<div class="izrek">

Velja $A_1, A_2, \dots, A_k \models B \Rightarrow C$, če in samo če velja $A_1, A_2, \dots, A_k, B \models C$.

</div>

<div class="dokaz">

Naj bo $A = A_1 \land A_2 \land \cdots \land A_k$. Po zadnji trditvi je dovolj dokazati, da je $A \Rightarrow (B \Rightarrow C)$ tavtologija, če in samo če je $A \land B \Rightarrow C$ tavtologija. Ta dva izjavna izraza pa sta si v resnici enakovredna, saj velja
```{math}
A \Rightarrow (B \Rightarrow C) \sim \lnot A \lor (\lnot B \lor C) \sim (\lnot A \lor \lnot B) \lor C \sim \lnot (A \land B) \lor C \sim A \land B \Rightarrow C.
```
Izraza sta torej bodisi oba tavtologiji bodisi nobenen od njiju ni tavtologija. S tem je izrek dokazan.

</div>

<div class="zgled">

Dokažimo veljavnost sklepa
```{math}
p \Rightarrow q \lor r, \ \lnot r \models p \Rightarrow q.
```
Ker ima zaključek obliko implikacije, lahko uporabimo pogojni sklep.

| $i$ | $B_i$                    | utemeljitev     |
|:------|:---------------------------|:----------------|
| 1     | $p \Rightarrow q \lor r$ | predpostavka    |
| 2     | $\lnot r$                | predpostavka    |
| 3.1   | $p$                      | predpostavka PS |
| 3.2   | $q \lor r$               | MP(3.1, 1)      |
| 3.3   | $q$                      | DS(3.2, 2)      |
| 3     | <u>$p \Rightarrow q$</u> | PS(3.1–3.3)     |

Uporaba pogojnega sklepa

</div>

Pomožni <span class="definicija">sklep s protislovjem</span> (RA[^1]) lahko uporabimo kadar koli. Če želimo sklepati na zaključek $B$, dodamo izjavo $\lnot B$ med predpostavke in skušamo sklepati na zaključek $0$. To je še posebej uporabno, kadar ima zaključek obliko negacije $\lnot B$, saj v tem primeru dodatna predpostavka postane $\lnot \lnot B \sim B$. Veljavnost tega pomožnega sklepa sledi iz naslednjega izreka.

<div class="izrek">

Velja $A_1, A_2, \dots, A_k \models B$, če in samo če velja $A_1, A_2, \dots, A_k, \lnot B \models 0$.

</div>

<div class="dokaz">

Naj bo $A = A_1 \land A_2 \land \cdots \land A_k$. Kot v dokazu zadnjega izreka je dovolj dokazati, da je $A \Rightarrow B$ tavtologija, če in samo če je $A \land \lnot B \Rightarrow 0$ tavtologija. Ta dva izjavna izraza pa sta si v resnici enakovredna, saj velja
```{math}
A \land \lnot B \Rightarrow 0 \sim
    \lnot A \lor \lnot \lnot B \sim
    \lnot A \lor B \sim
    A \Rightarrow B.
```

</div>

<div class="zgled">

Dokažimo veljavnost sklepa
```{math}
p \Rightarrow \lnot (q \Rightarrow r), \ q \land s \Rightarrow r, \ s \models \lnot p.
```
Ker ima zaključek obliko negacije, še posebej radi uporabimo sklepanje s protislovjem.

| $i$ | $B_i$                                  | utemeljitev     |
|:------|:-----------------------------------------|:----------------|
| 1     | $p \Rightarrow \lnot(q \Rightarrow r)$ | predpostavka    |
| 2     | $q \land s \Rightarrow r$              | predpostavka    |
| 3     | $s$                                    | predpostavka    |
| 4.1   | $\lnot \lnot p$                        | predpostavka RA |
| 4.2   | $p$                                    | $\sim$ 4.1    |
| 4.3   | $\lnot (q \Rightarrow r)$              | MP(4.2, 1)      |
| 4.4   | $q \land \lnot r$                      | $\sim$ 4.3    |
| 4.5   | $q$                                    | Po(4.4)         |
| 4.6   | $q \land s$                            | Zd(4.5, 3)      |
| 4.7   | $r$                                    | MP(4.6, 2)      |
| 4.8   | $\lnot r \land q$                      | $\sim$ 4.4    |
| 4.9   | $\lnot r$                              | Po(4.8)         |
| 4.10  | $r \land \lnot r$                      | Zd(4.7, 4.9)    |
| 4.11  | $0$                                    | $\sim$ 4.10   |
| 4     | <u>$\lnot p$</u>                       | RA(4.1–4.11)    |

Uporaba sklepa s protislovjem

</div>

Pomožni sklep <span class="definicija">analiza primerov</span> (AP) uporabimo, kadar dokazujemo sklep, v katerem ima ena od predpostavk obliko disjunkcije $B_1 \lor B_2$. V tem primeru lahko sklep razdelimo na dva preprostejša sklepa, pri čemer prvemu dodamo predpostavko $B_1$, drugemu pa predpostavko $B_2$. Podobno kot pri prejšnjih dveh pomožnih sklepih veljavnost tega pomožnega sklepa sledi iz naslednjega izreka.

<div class="izrek">

Velja $A_1, A_2, \dots, A_k, B_1 \lor B_2 \models C$, če in samo če veljata oba sklepa $A_1, A_2, \dots, A_k, B_1 \models C$ in $A_1, A_2, \dots, A_k, B_2 \models C$.

</div>

<div class="domacanaloga">

Dokaži izrek o analizi primerov.

</div>

<div class="zgled">

Dokažimo veljavnost sklepa
```{math}
p \Rightarrow r, \ q \Rightarrow r, \ p \lor q \models r.
```
Tretja predpostavka ima obliko disjunkcije, zato lahko sklep dokažemo s pomočjo analize primerov.

| $i$ | $B_i$             | utemeljitev                     |
|:------|:--------------------|:--------------------------------|
| 1     | $p \Rightarrow r$ | predpostavka                    |
| 2     | $q \Rightarrow r$ | predpostavka                    |
| 3     | $p \lor q$        | predpostavka                    |
| 4.1.1 | $p$               | predpostavka AP(3)              |
| 4.1.2 | $r$               | MP(4.1.1, 1)                    |
| 4.2.1 | $q$               | predpostavka AP(3)              |
| 4.2.2 | $r$               | MP(4.1.1, 2)                    |
| 4\.   | <u>$r$</u>        | AP(3, 4.1.1–4.1.2, 4.2.1–4.2.2) |

Uporaba analize primerov

</div>

[^1]: Lat. *Reductio ad absurdum*.
