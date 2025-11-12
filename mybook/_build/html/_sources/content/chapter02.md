```{raw} html
<style>
  body { counter-reset: chapter 1 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Predikatni račun

Predikatni račun je *nadgradnja* izjavnega računa, ki omogoča bolj natančno logično izražanje. Najprej si bomo na konkretnih primerih pogledali, katere novosti prinaša predikatni račun. Za tem bomo te formalno definirali in razvili podobno teorijo kot v izjavnem računu.

## Motivacija

Na konkretnih zgledih si oglejmo nekaj simbolov in formul, ki jih bomo videli v predikatnem računu. Ti zgledi nam bodo pomagali, da bomo v naslednjem razdelku lažje predelali formalne definicije predikatnega računa.

<div class="zgled">

Oglejmo si naslednji sklep, zapisan v slovenščini.

$p_1$:  
Vsak zajec ljubi korenje.

$p_2$:  
Feliks je zajec.

$z$:  
Torej Feliks ljubi korenje.

V izjavnem računu ta sklep zapišemo kot $p_1, p_2 \models z$. Seveda pa ta sklep v izjavnem računu ni veljaven, protiprimer je namreč nabor $p_1 = 1, p_2 = 1, z = 0$.

Kljub temu se zdi, da je ta sklep v slovenščini vsekakor pravilen. Predikatni račun je nadgradnja izjavnega računa, v katerem izjavne spremeljivke $p_1, p_2, z$ obravnavamo nekoliko podrobneje, tako da bo ta sklep pravilen v tem novem računu.

Uvedimo naslednje oznake:

$Z(x)$:  
$x$ je zajec.

$K(x)$:  
$x$ ljubi korenje.

$a$:  
Feliks

$\forall x$:  
za vsak $x$

S temi oznakami lahko sklep zapišemo bolj natančno takole:

$p_1$:  
$\forall x \colon (Z(x) \Rightarrow K(x))$

$p_2$:  
$Z(a)$

$z$:  
$K(a)$

V predikatnem jeziku bomo torej poleg izjavnih vezikov in ločil iz izjavnega računa imeli <span class="definicija">individualne spremenljivke</span> ($x$), <span class="definicija">individualne konstante</span> ($a$), <span class="definicija">predikate</span> ($Z$, $K$) in <span class="definicija">univerzalni kvantifikator</span> ($\forall$).

</div>

<div class="zgled">

Prevedimo nekaj izjav iz slovenščine v nov jezik predikatnega računa, kot smo to storili v zadnjem zgledu. Izjave so naslednje:

1.  Vsi gasilci so hrabri.

2.  Nekateri gasilci so hrabri.

3.  Nekateri gasilci niso hrabri.

4.  Noben gasilec ni hraber.

Uvedimo naslednje oznake:

$G(x)$:  
$x$ je gasilec.

$H(x)$:  
$x$ je hraber.

$\exists x$:  
obstaja $x$

Izjave v slovenščini lahko s temi oznakami zapišemo na naslednji način:

1.  $\forall x \colon (G(x) \Rightarrow H(x))$

2.  $\exists x \colon (G(x) \land H(x))$

3.  $\exists x \colon (G(x) \land \lnot H(x))$

4.  $\forall x \colon (G(x) \Rightarrow \lnot H(x))$

Tukaj smo videli še en simbol kvantifikacije, ki ga bomo imeli v predikatnem računu, in sicer <span class="definicija">eksistenčni kvantifikator</span> ($\exists$).

</div>

<div class="zgled">

Storimo podobno kot v zadnjih dveh zgledih še za naslednjo matematično izjavo. *Evklidov izrek* nam pove, da obstaja neskončno mnogo praštevil.

Če želimo to izjavo zapisati na podoben način kot prejšnje izjave v tem poglavju, nam bo v pomoč, če jo prepišemo v nekoliko drugačno obliko, in sicer kot izjavo, da obstajajo poljubno velika praštevila. Še vedno ni jasno, kako bi izrazili del izjave, ki pravi, da obstajajo *poljubno velika* števila, zato bodimo še nekoliko bolj eksplicitni glede tega dela izjave. Evklidov izrek je ekvivalenten izjavi, da za vsako naravno število obstaja večje naravno število, ki je praštevilo. To zadnjo izjavo pa lahko zapišemo v predikatnem računu.

Uvedimo naslednje oznake:

$P(x)$:  
$x$ je praštevilo.

$V(x,y)$:  
$x$ je večje od $y$.

V tem zgledu so naše spremenljivke $x$ iz množice naravnih števil, v prejšnjem zgledu pa so bile iz množice ljudi. Pomembno je, da se na začetku dogovorimo o področju pogovora oziroma <span class="definicija">domeni</span>, saj izjave, ki jih zapišemo, morda v drugi domeni pomenijo čisto nekaj drugega.

Evklidov izrek lahko nazadnje zapišemo v predikatnem računu na naslednji način:
```{math}
\forall x \exists y \colon (V(y,x) \land P(y)).
```

Tukaj smo srečali predikat $V$, ki je nekoliko drugačen od predikatov, ki smo jih videli do sedaj. Predikat $V$ je namreč *dvomesten* (ima dva parametra), drugi predikati pa so bili vsi *enomestni*.

</div>

<div class="zgled">

V prejšnjem zgledu smo govorili o praštevilih, za katere smo uvedli predikat $P$. Seveda pa bi lahko samo dejstvo, da je spremenljivka $x$ praštevilo, se pravi da je izjava $P(x)$ resnična, podrobneje opisali v predikatnem računu. To storimo v tem zgledu.

Po definiciji je naravno število $n$ praštevilo, če in samo če ima natanko dva naravna delitelja. Uvedimo naslednje oznake:

$f(x,y)$:  
produkt $x$ in $y$

$E(x,y)$:  
$x$ je enak $y$.

Definicijo predikata $P$ lahko zapišemo na naslednji način:
```{math}
\forall x \colon \left( 
    P(x) \Leftrightarrow V(x,1) \land \forall u \forall v \colon ( E(x, f(u,v)) \Rightarrow E(u,1) \land E(v,1) ).
    \right)
```

Tukaj smo naleteli še na zadnji fenomen, ki ga bomo imeli v predikatnem računu, in sicer je to <span class="definicija">funkcijski simbol</span> $f$, ki iz danih števil izračuna njun produkt.

</div>

## Sintaksa predikatnega računa

Zdaj smo pripravljeni, da formalno definiramo vse koncepte v predikatnem računu. Sistematično bomo našteli simbole, ki jih uporabljamo, in opisali, kako iz njih sestavljamo izjavne formule.

Naj bo področje pogovora dano z neko množico $D$.

### Simboli

V predikatnem računu uporabljamo naslednje simbole:

1.  <span class="definicija">Individualne konstante</span>, ki jih bomo označevali z $a,b,c,\dots$. To so *konkretni* elementi množice $D$.

2.  <span class="definicija">Individualne spremenljivke</span>, ki jih bomo označevali z $x,y,z,\dots$. To so *poljubni* elementi množice $D$.

3.  <span class="definicija">Predikati</span>, ki jih bomo označevali s $P,Q,R,\dots$. Ti predstavljajo relacije med elementi množice $D$. Predikati so lahko enomestni, dvomestni, …, $n$-mestni, …

4.  <span class="definicija">Funkcijski simboli</span>, ki jih bomo označevali s $f,g,h,\dots$. Tudi ti so lahko $n$-mestni za poljubno naravno število $n$. Funkcijski simboli predstavljajo funkcije iz $n$-teric elementov $D$ v $D$.

5.  Izjavni vezniki iz izjavnega računa

6.  <span class="definicija">Simbola kvantifikacije</span> $\forall$ in $\exists$.

7.  Ločila `():,`

### Termi

Najosnovnejše izjave, ki jih v predikatnem računu sestavljamo z naštetimi simboli, so <span class="definicija">termi</span>. Definiramo jih induktivno,[^1] in sicer na naslednji način:

- *Osnovni term 1:* Vsaka *individualna konstanta* je term.

- *Osnovni term 2:* Vsaka *individualna spremenljivka* je term.

- *Sestavljeni term:* Če je $f$ *$n$-mesten funkcijski simbol* in so $t_1, t_2, \dots, t_n$ termi, potem je $f(t_1,t_2,\dots,t_n)$ term.

Termi, ki *ne* vsebujejo nobenih individualnih spremenljivk, se imenujejo <span class="definicija">zaprti termi</span>.

<div class="zgled">

Naj bo $a$ individualna konstanta, $x,y$ individualni spremenljivki, $f$ enomesten funkcijski simbol, $g$ dvomesten funkcijski simbol. Tedaj so
```{math}
x, \ y, \ a, \ f(x), \ f(a), \ f(f(a)), \ g(x,f(f(y)))
```
termi. Tretji, peti in šesti izmed teh so zaprti termi.

</div>

### Izjavne formule

<span class="definicija">Izjavne formule</span> so bolj kompleksne izjave v predikatnem računu, ki jih sestavljamo s pomočjo termov. Njihova definicija je induktivna, in sicer:

- *Osnovna izjavna formula:* Naj bo $P$ neki $n$-mestni predikat in $t_1, t_2, \dots, t_n$ termi. Potem je $P(t_1, t_2, \dots, t_n)$ izjavna formula. Taki izjavni formuli rečemo <span class="definicija">atomarna</span>.

- *Sestavljena izjavna formula 1:* Naj bo $F$ neki $n$-mestni izjavni veznik in $\phi_1, \phi_2, \dots, \phi_n$ izjavne formule. Potem je $F(\phi_1, \phi_2, \dots, \phi_n)$ izjavna formula.

- *Sestavljena izjavna formula 2:* Naj bo $\phi$ izjavna formula in $x$ individualna spremenljivka. Potem sta $(\forall x \colon \phi)$ in $(\exists x \colon \phi)$ izjavni formuli. Pri tem je $\forall x$ <span class="definicija">univerzalni kvantifikator</span>, $\exists x$ <span class="definicija">eksistenčni kvantifikator</span>, formula $\phi$ pa je <span class="definicija">doseg kvantifikatorja</span>.

Kot pri izjavnem računu sprejmemo <span class="definicija">dogovor o prednostnem vrstnem redu kvantifikatorjev in opuščjanju ločil</span>:

- za izjavne veznike in zunanje oklepaje velja dogovor iz izjavnega računa,

- kvantifikatorji imajo prednost pred izjavnimi vezniki,

- ločila med zaporednimi kvantifikatorji izpuščamo.

<div class="zgled">

V zgledih na začetku tega poglavja smo srečali naslednje izjavne formule:
```{math}
Z(x), \ K(x), \ Z(a), \ K(a), \ \lnot H(x), \ \forall x \colon (G(x) \Rightarrow H(x)), \ \forall x \exists y \colon (V(y,x) \land P(x)).
```

</div>

Analogno definiciji zaprtosti termov uvedemo koncept zaprtosti izjavnih formul. Nastop individualne spremenljivke v izjavni formuli je <span class="definicija">vezan</span>, če je del kvantifikatorja ali leži v dosegu kvantifikatorja, ki vsebuje to spremenljivko. Če nastop ni vezan, je <span class="definicija">prost</span>. Izjavna formula je <span class="definicija">zaprta</span>, če so vsi nastopi individualnih spremenljivk v njej vezani.

<div class="zgled">

Naslednje izjavne formule so zaprte:
```{math}
P(a), \ \forall x \colon P(x), \ \forall x \exists y \colon V(x,y).
```
Naslednje izjavne formule pa niso zaprte:
```{math}
P(x), \ \exists y \colon V(x,y), \ \forall x \colon (V(x,y) \Rightarrow \exists P(y)).
```

</div>

Postojmo le še pri enem osnovnem konceptu v zvezi z izjavnimi formulami, in sicer substitucijo. Naj bo $\phi$ izjavna formula z individualno spremenljivko $x$, tako da lahko zapišemo formulo kot $\phi(x)$. Če je $t$ nek term, potem s $\phi(t)$ označimo izjavno formulo, ki jo dobimo iz $\phi(x)$, če v njej vse *proste* nastope $x$ zamenjamo s $t$. V tem primeru rečemo, da smo $\phi(t)$ dobili s <span class="definicija">substitucijo</span> iz $\phi(x)$ spremenljivke $x$ s termom $t$.

<div class="zgled">

Naj bo $\phi(x) = \exists y \colon R(x,y)$ in $t = f(a)$. Potem je $\phi(t) = \exists y \colon R(f(a), y)$.

</div>

Analogno lahko v formuli $\phi(x_1, x_2, \dots, x_n)$ z različnimi individualnimi spremenljivkami $x_1, x_2, \dots, x_n$ izvedemo substitucijo vseh prostih nastopov $x_i$ s termom $t_i$ za $i = 1,2,\dots,n$.

## Semantika predikatnega računa

Do zdaj smo se ukvarjali s tem, kako v predikatnem računu zapišemo izjavne formule. Te formule same po sebi pa seveda nimajo nikakršnega pomena, dokler ne določimo, kaj je domena in kaj predstavljajo individualne konstante, predikati in funkcijski simboli. S tem se ukvarja *semantika* predikatnega računa. Če smo torej do zdaj iz izjav v slovenščini sestavljali formule, bomo tukaj iz formul sestavljali izjave v slovenščini.

Naj bo $\Fcal$ neka množica izjavnih formul, ki jim želimo določiti pomen. <span class="definicija">Interpretacijo</span> $I$ formul iz $\Fcal$ podamo tako, da:

1.  izberemo neprazno množico objektov (to je <span class="definicija">domena</span> ali področje pogovora),

2.  vsaki individualni konstanti $a$ iz $\Fcal$ priredimo nek element $\bar a \in D$,

3.  vsakemu $n$-mestnemu predikatu $P$ iz $\Fcal$ priredimo neko podmnožico $\bar P$ v $D^n = D \times D \times \cdots \times D$, ki predstavlja vse $n$-terice elementov, za katere je $P$ resničen,[^2]

4.  vsakemu $n$-mestnemu funkcijskemu simbolu $f$ priredimo preslikavo $\bar f$, ki vsako urejeno $n$-terico elementov $D$ preslika v točno določen element $D$, se pravi funkcijo iz $D^n$ v $D$.

Izjavne veznike iz izjavnega računa interpretiramo,kot smo jih že v izjavnem računu. Simbola kvantifikacije interpretiramo na naslednji način:

- $\forall x$ intepretiramo kot *za vsak $x$ iz $D$*,

- $\exists x$ interpretiramo kot *obstaja $x$ iz $D$*.

<div class="zgled">

Naj bo
```{math}
\Fcal = \{ P(a), P(x), \forall x \colon P(x), P(f(a,b)) \}
```
množica izjavnih formul. Da lahko te formule interpretiramo, moramo izbrati neko intepretacijo. Vzemimo tole intepretacijo $I$:
```{math}
D = \NN, \ \bar a = 2, \ \bar b = 3, \ \bar P = \PP, \ \bar f(x,y) = 2x + y,
```
kjer je $\PP$ množica praštevil. V tej interpretaciji term $\overline{f(a,b)}$ torej intepretiramo kot
```{math}
\overline{f(a,b)}
    = \bar f (\bar a, \bar b)
    = 2 \bar a + \bar b
    = 7.
```
Oglejmo si pomene izjavnih formul v $\Fcal$ v interpretaciji $I$.

| formula $\phi$ | poved $\bar \phi$ | komentar |
|:--:|:---|:---|
| $P(a)$ | $2$ je praštevilo | resnična izjava |
| $P(x)$ | $x$ je praštevilo | ni izjava |
| $\forall x \colon P(x)$ | vsako naravno število je praštevilo | lažna izjava |
| $P(f(a,b))$ | $7$ je praštevilo | resnična izjava |

Interpretacije formul iz $\Fcal$ v $I$

</div>

Zaprtemu termu $t$ ustreza element $\bar t \in D$, zaprti izjavni formuli $\phi$ pa ustreza izjava $\bar \phi$. Kadar izjavna formula $\phi$ ni zaprta, tedaj $\bar \phi$ *ni* izjava, saj je odvisna od prostih spremenljivk.

<div class="zgled">

Opazujmo izjavno formulo $\phi = \forall x \exists y \colon R(x,y)$. Poglejmo si nekaj različnih interpretacij te formule.

| interpretacija $I$ | poved $\bar \phi$ | komentar |
|:---|:---|:---|
| $I_1$: $D = \NN$, $\bar R(x,y) = x < y$ | za vsako naravno število obstaja večje naravno število | resnična izjava |
| $I_2$: $D = \NN$, $\bar R(x,y) = x > y$ | za vsako naravno število obstaja manjše naravno število | lažna izjava |
| $I_3$: $D = \ZZ$, $\bar R(x,y) = x > y$ | za vsako celo število obstaja manjše celo število | resnična izjava |

Različne interpretacije formule $\phi$

</div>

Dani zaprti izjavni formuli $\phi$ lahko torej v nekaterih interpretacijah ustrezajo resnične izjave, v drugih interpretacijah pa lažje izjave. Rečemo, da je zaprta izjavna formula $\phi$ <span class="definicija">resnična v interpretaciji</span> $I$, če je resnična izjava $\bar \phi$. V tem primeru pišemo $I \models \phi$.

## Logično veljavne formule in enakovrednosti

Kadar je zaprta izjavna formula $\phi$ resnična v *vseh* interpretacijah, ji pravimo <span class="definicija">logično veljavna</span>. Sorodno izjavni formuli $\phi$, ki je lažna v *vseh* interpretacijah, pravimo <span class="definicija">protislovna</span>.

<div class="zgled">

Naj bosta $P$ in $Q$ enomestna predikata. Opazujmo izjavno formulo
```{math}
\phi = \forall x \colon P(x) \lor \forall x \colon Q(x) \Rightarrow \forall x \colon (P(x) \lor Q(x)).
```
Prepričajmo se, da je $\phi$ logično veljavna formula.

V ta namen moramo dokazati, da za *vsako* interpretacijo $I$ velja $I \models \phi$. Naj bo torej $I$ poljubna interpretacija. V tej interpretaciji moramo torej dokazati, da je izjava $\bar \phi$ veljavna, kar je enakovredno veljavnosti sklepa $\models \bar \phi$, se pravi veljavnosti sklepa
```{math}
\models 
    \forall x \colon \bar P(x) \lor \forall x \colon \bar Q(x) \Rightarrow \forall x \colon (\bar P(x) \lor \bar Q(x)).
```
Zaključek tega sklepa ima obliko implikacije, zato lahko uporabimo pogojni sklep. Dokazati moramo torej veljavnost sklepa
```{math}
\forall x \colon \bar P(x) \lor \forall x \colon \bar Q(x)
    \models
    \forall x \colon (\bar P(x) \lor \bar Q(x)).
```
Predpostavka tega sklepa ima obliko disjunkcije, zato lahko uporabimo analizo primerov.

1.  Predpostavimo $\forall x \colon \bar P(x)$. Dokazati želimo, da je izjava $\forall x \colon (\bar P(x) \lor \bar Q(x))$ resnična. V ta namen izberimo poljuben $x_0 \in D$. Po predpostavki za vsak $x$ iz $D$ velja $\bar P(x)$, zato v posebnem to velja za element $x_0$, se pravi da je izjava $\bar P(x_0)$ resnična. Od tod sledi, da je resnična tudi izjava $\bar P(x_0) \lor \bar Q(x_0)$. Ker je bil $x_0$ poljuben element iz $D$, smo s tem premislili, da je izjava $\forall x \colon (\bar P(x) \lor \bar Q(x))$ resnična. To je bil naš cilj, zato je sklep v tem primeru veljaven.

2.  Predpostavimo $\forall x \colon \bar Q(x)$. Kot zgoraj želimo dokazati, da je izjava $\forall x \colon (\bar P(x) \lor \bar Q(x))$ resnična. Dokaz je povsem analogen tistemu iz prejšnje točke, le $P$ in $Q$ zamenjamo med sabo.

S tem smo dokazali veljavnost sklepa in torej veljavnost $I \models \phi$. Ker je bila interpretacija $I$ poljubna, je torej $\phi$ res logično veljavna formula.

</div>

<div class="zgled">

Naj bosta $P$ in $Q$ enomestna predikata. Opazujmo izjavno formulo
```{math}
\psi = \forall x \colon (P(x) \lor Q(x)) \Rightarrow \forall x \colon P(x) \lor \forall x \colon Q(x).
```
Prepričajmo se, da $\psi$ ni logično veljavna.

V ta namen zadošča poiskati neko interpretacijo $I$, v kateri $\psi$ ni resnična. Možnosti za to je veliko. Vzamemo lahko naslednjo interpretacijo:
```{math}
D = \NN, \ \bar P = \{ 2 n \mid n \in \NN \}, \ \bar Q = \{ 2n - 1 \mid n \in \NN \}.
```
Velja $\psi = \psi_1 \Rightarrow \psi_2$, kjer je
```{math}
\psi_1 = \forall x \colon (P(x) \lor Q(x)), \
    \psi_2 = \forall x \colon P(x) \lor \forall x \colon Q(x).
```
V interpretaciji $I$ je izjava $\bar \psi_1$ enakovredna izjavi, da je vsako naravno število sodo ali liho, izjava $\bar \psi_2$ pa je enakovredna izjavi, da so vsa naravna števila soda ali pa so vsa naravna števila liha. Prva od teh dveh izjav je resnična, druga pa je lažna. V interpretaciji $I$ je zato $\bar \psi_1 \Rightarrow \bar \psi_2$ lažna izjava, torej je $\bar\psi$ lažna v $I$. Izjavna formula $\psi$ torej res ni logično veljavna.

<div class="domacanaloga">

Poišči kakšno interpretacijo, v kateri je izjavna formula $\psi$ resnična.

</div>

</div>

<div class="zgled">

Naj bo $R$ dvomestni predikat. Opazujmo izjavno formulo
```{math}
\chi = \exists y \forall x \colon (R(x,y) \Leftrightarrow \lnot R(x,x)).
```
Prepričajmo se, da je $\chi$ protislovna izjavna formula.

V ta namen moramo dokazati, da za *vsako* interpretacijo $I$ velja, da je izjava $\bar \chi$ lažna v $I$. Naj bo torej $I$ poljubna interpretacija. Dokazati želimo veljavnost sklepa
```{math}
\models \lnot \left( \exists y \forall x \colon (\bar R(x,y) \Leftrightarrow \lnot \bar R(x,x)) \right).
```
Ker ima zaključek obliko negacije, lahko uporabimo sklepanje s protislovjem. Predpostavimo torej, da je v interpretaciji $I$ izjava $\lnot \bar \chi$ lažna, se pravi da je $\bar \chi$ resnična. Dokazati želimo protislovje $0$. Po predpostavki o resničnosti $\bar \chi$ obstaja nek $y_0 \in D$, za da je izjava
```{math}
\forall x \colon (\bar R(x, y_0) \Leftrightarrow \lnot \bar R(x,x))
```
resnična. Torej za vsak $x$ iz $D$ velja $\bar R(x, y_0) \Leftrightarrow \lnot \bar R(x,x)$. V posebnem to velja za element $y_0$, se pravi da je izjava $\bar R(x_0, y_0) \Leftrightarrow \lnot \bar R(x_0,x_0)$ resnična. Ampak zadnja izjava je po izjavnem računu enakovredna $0$. Na ta način smo izpeljali, da je $0$ resnična izjava. To je lažno, zato smo izpeljali $0$, kar je bil naš cilj dokazovanja s protislovjem. Izjava $\lnot \bar \chi$ je torej v interpretaciji $I$ resnična, kar pomeni, da $\chi$ ni resnična v $I$. Ker je bila $I$ poljubna interpretacija, smo se s tem prepričali, da je $\chi$ protislovna izjavna formula.

</div>

Po analogiji z izjavnim računom rečemo, da sta izjavni formuli $\phi, \psi$ <span class="definicija">enakovredni</span>, če je formula $\phi \Leftrightarrow \psi$ logično veljavna. V tem primeru pišemo $\phi \sim \psi$.

Zabeležimo nekaj pomembnih enakovrednosti, ki veljajo v predikatnem računu. Za vsaki izjavni formuli $\phi, \psi$ in individualni spremenljivki $x,y$ velja:

- $\lnot \forall x \colon \phi \sim \exists x \colon \lnot \phi$,  
  $\lnot \exists x \colon \phi \sim \forall x \colon \lnot \phi$ (<span class="definicija">negacija kvantificirane formule</span>)

- $\forall x \forall y \colon \phi \sim \forall y \forall x \colon \phi$,  
  $\exists x \exists y \colon \phi \sim \exists y \exists x \colon \phi$ (<span class="definicija">komutativnost istovrstnih kvantifikatorjev</span>)

- $\forall x \colon (\phi \land \psi) \sim \forall x \colon \psi \land \forall x \colon \psi$,  
  $\exists x \colon (\phi \lor \psi) \sim \exists x \colon \psi \lor \exists x \colon \psi$ (<span class="definicija">distributivnost kvantifikatorjev glede na $\land, \lor$</span>)

- $\forall x \colon (\phi \lor \psi) \sim \forall x \colon \phi \lor \psi$, če $x$ ne nastopa prosto v $\psi$;  
  $\exists x \colon (\phi \land \psi) \sim \exists x \colon \phi \land \psi$, če $x$ ne nastopa prosto v $\psi$

- $\forall x \colon \phi \sim \phi$, če $x$ ne nastopa prosto v $\phi$;  
  $\exists x \colon \phi \sim \phi$, če $x$ ne nastopa prosto v $\phi$ (<span class="definicija">opuščanje odvečnih kvantifikatorjev</span>)

- $\forall x \colon \phi(x) \sim \forall y \colon \phi(y)$, če $y$ ne nastopa v $\phi(x)$ niti prosto niti vezano;  
  $\exists x \colon \phi(x) \sim \exists y \colon \phi(y)$, če $y$ ne nastopa v $\phi(x)$ niti prosto niti vezano (<span class="definicija">preimenovanje vezanih spremenljivk</span>).

<div class="zgled">

Za vsako izjavno formulo $\phi$ obstaja enakovredna formula $\psi$, pri kateri stojijo vsi kvantifikatorji na začetku formule. Rečemo, da je $\psi$ v <span class="definicija">preneksni obliki</span>. Kako ta transformacija deluje, si oglejmo na dveh konkretnih primerih.

Opazujmo najprej izjavno formulo
```{math}
\lnot \forall x \exists y \colon R(x,y).
```
S pomočjo negacije kvantificirane formule izpeljemo, da je ta izjavna formula enakovredna formuli
```{math}
\exists x \colon (\lnot \exists y \colon R(x,y))
    \sim \exists x \forall y \colon \lnot R(x,y),
```
slednja pa je v preneksni obliki.

Oglejmo si zdaj še izjavno formulo
```{math}
\exists x \colon P(x) \land \exists x \colon Q(x).
```
Spremenljivki $x$ v obeh delih konjunkcije sta neodvisni, zato lahko za večjo jasnost v drugem delu to spremenljivko preimenujemo in dobimo enakovredno izjavno formulo
```{math}
\exists x \colon P(x) \land \exists y \colon Q(y).
```
Zdaj lahko uporabimo distributivnost kvantifikatorjev glede na konjunkcijo, da dobimo
```{math}
\exists x \colon ( P(x) \land \exists y \colon Q(y) )
    \sim 
    \exists x \colon ( \exists y \colon Q(y) \land P(x) ).
```
Slednja formula je enakovredna
```{math}
\exists x \exists y \colon (Q(y) \land P(x)),
```
ki je v preneksni obliki.

</div>

## Sklepanje v predikatnem računu

Končno zaporedje izjavnih formul $\phi_1, \phi_2, \dots, \phi_k, \psi$ je <span class="definicija">veljaven</span> ali <span class="definicija">pravilen sklep</span>, če je izjavna formula $\phi_1 \land \phi_2 \land \cdots \land \phi_k \Rightarrow \psi$ logično veljavna. V tem primeru uporabljamo oznako $\phi_1, \phi_2, \dots, \phi_k \models \psi$.

Podrobno si oglejmo, kako lahko uporabimo znanje o predikatnem in izjavnem računu, da dokažemo veljavnost nekaterih sklepov.

<div class="zgled">

Dokažimo veljavnost sklepa
```{math}
P(a), \ \forall x \colon (P(x) \Rightarrow Q(x)) \models Q(a).
```
Dokazati torej želimo, da je formula
```{math}
P(a) \land \forall x \colon (P(x) \Rightarrow Q(x)) \Rightarrow Q(a)
```
logično veljavna.

V ta namen na bo $I$ *poljubna* interpretacija. Dokažimo resničnost izjave
```{math}
\bar P( \bar a) \land \forall x \colon (\bar P(x) \Rightarrow \bar Q(x)) \Rightarrow \bar Q(\bar a).
```
Za to lahko uporabimo *pogojni sklep*. Predpostavimo, da je resnična izjava
```{math}
\bar P( \bar a) \land \forall x \colon (\bar P(x) \Rightarrow \bar Q(x))
```
Dokazati želimo, da je resnična tudi izjava $\bar Q(\bar a)$.

Najprej na predpostavki uporabimo *poenostavitev*. Resnični sta torej izjavi
```{math}
\bar P( \bar a), \ \forall x \colon (\bar P(x) \Rightarrow \bar Q(x)).
```
Torej je za vsak $x_0 \in D$ resnična izjava $P(x_0) \Rightarrow Q(x_0)$. V posebnem to velja za $x_0 = \bar a$, zato je izjava $\bar P(\bar a) \Rightarrow \bar Q(\bar a)$ resnična. Ker je resnična tudi izjava $\bar P( \bar a)$, lahko uporabimo *modus ponens*. Sledi, da je resnična tudi izjava $\bar Q(\bar a)$. S tem je dokaz zaključen.

Res torej velja
```{math}
I \models \bar P( \bar a) \land \forall x \colon (\bar P(x) \Rightarrow \bar Q(x)) \Rightarrow \bar Q(\bar a).
```
Ker je bila interpretacija $I$ poljubna, smo s tem dokazali veljavnost sklepa
```{math}
P(a), \ \forall x \colon (P(x) \Rightarrow Q(x)) \models Q(a).
```

V posebnem je veljaven sklep, ki smo ga videli na začetku tega poglavja in ki nas je motiviral k definiciji predikatnega računa.

<div class="description">

Vsak zajec ljubi korenje.

Feliks je zajec.

Torej Feliks ljubi korenje.

</div>

</div>

<div class="zgled">

Dokažimo veljavnost sklepa
```{math}
\exists x \colon P(x), \
    \forall x \colon (P(x) \Rightarrow \lnot Q(x) \lor \forall y \colon R(y)) \models
    \exists x \colon (Q(x) \Rightarrow R(x)).
```
V ta namen naj bo $I$ *poljubna* interpretacija. Zopet lahko uporabimo pogojni sklep in predpostavimo, da sta resnični izjavi
```{math}
\exists x \colon \bar P(x), \
    \forall x \colon (\bar P(x) \Rightarrow \lnot \bar Q(x) \lor \forall y \colon \bar R(y)).
```
Dokazati želimo resničnost izjave $\exists x \colon (\bar Q(x) \Rightarrow \bar R(x))$, ki trdi, da obstaja element v $D$ z neko posebno lastnostjo.

Kako najti ta element? Uporabimo lahko prvo predpostavko, po kateri obstaja element $\bar a \in D$, da je izjava $\bar P(\bar a)$ resnična. Hkrati po drugi predpostavki za vsak $x_0 \in D$ velja
```{math}
\bar P(x_0) \Rightarrow \lnot \bar Q(x_0) \lor \forall y \colon \bar R(y).
```
V posebnem to velja za $x_0 = \bar a$, zato je resnična izjava
```{math}
\bar P(\bar a) \Rightarrow \lnot \bar Q(\bar a) \lor \forall y \colon \bar R(y).
```
Ker je po predpostavki izjava $\bar P(\bar a)$ resnična, lahko uporabimo *modus ponens* in sklenemo, da je resnična tudi izjava
```{math}
\lnot \bar Q(\bar a) \lor \forall y \colon \bar R(y).
```
Zdaj lahko uporabimo *analizo primerov*.

1.  Predpostavimo, da je resnična izjava $\lnot \bar Q(\bar a)$. Uporabimo *pridružitev* in sklenemo, da je resnična izjava
    ```{math}
    \lnot \bar Q(\bar a) \lor \bar R(\bar a) \sim \bar Q(\bar a) \Rightarrow \bar R(\bar a)
    ```

2.  Predpostavimo, da je resnična izjava $\forall y \colon \bar R(y)$. Torej za vsak $y_0 \in D$ velja $\bar R(y_0)$. V posebnem to velja za $y_0 = \bar a$. Torej je resnična izjava $\bar R(\bar a)$. Uporabimo *pridružitev* in sklenemo, da je resnična izjava
    ```{math}
    \lnot \bar Q(\bar a) \lor \bar R(\bar a) \sim \bar Q(\bar a) \Rightarrow \bar R(\bar a).
    ```

Z analizo primerov smo zaključili, da je resnična izjava
```{math}
\bar Q(\bar a) \Rightarrow \bar R(\bar a).
```
Torej je resnična tudi izjava
```{math}
\exists x \colon ( \bar Q(x) \Rightarrow \bar R(x) ),
```
kar smo ravno želeli dokazati.

</div>

[^1]: Ta induktivna definicija je podobna kot induktivna definicija izjavnih izrazov v izjavnem računu.

[^2]: Podmnožicam $D^n$ rečemo tudi <span class="definicija">$n$-mestne relacije</span> v $D$.
