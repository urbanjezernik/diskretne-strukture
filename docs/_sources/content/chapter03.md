```{raw} html
<style>
  body { counter-reset: chapter 2 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Relacije

Ena od pomembnih komponent predikatnega računa so *predikati*. V konkretni interpretaciji $I$ z domeno $D$ te predstavimo kot množice nekaterih $n$-teric iz $D$. Enomestni predikati so torej kar podmnožice $D$, dvomestni predikati pa so podmnožice $D \times D$. V tem poglavju si bomo podrobneje pogledali dvomestne predikate, ki jih nasploh v matematiki imenujemo *relacije*. Pogledali si bomo njihove *lastnosti* ter različne *konstrukcije* relacij.

## Definicija in lastnosti relacij

Množica $R$ je <span class="definicija">dvomestna relacija</span> v množici $A$, če je $R \subseteq A \times A$.

<div class="zgled">

- Naj bo $A = \{ 1,2,3,4 \}$. V tej množici imamo relacijo
  ```{math}
  R = \{ (1,2), (2,3), (3,1), (3,3), (3,4) \} \subseteq A \times A.
  ```
  To relacijo lahko predstavimo grafično z <span class="definicija">grafom relacije</span>. Elementi množice $A$ so vozlišča, vozlišči $a$ in $b$ pa povežemo s puščico od $a$ do $b$, če je $(a,b) \in R$.

  <figure>
  <img src="img/relacije-graf.png" />
  <figcaption>Graf relacije <span class="math inline"><em>R</em></span></figcaption>
  </figure>

- Naj bo $A = \NN_0$ in $R$ relacija, podana kot
  ```{math}
  R = \{ (x,y) \in \NN_0 \times \NN_0 \mid \exists z \in \NN_0 \colon x + z = y \}.
  ```
  Ta relacija $R$ predstavlja relacijo $\leq$ na množici $\NN_0$, se pravi $(x,y) \in R \Leftrightarrow x \leq y$.

- V vsaki množici $A$ imamo naslednje relacije:

  - $R = \emptyset \subset A \times A$. To je <span class="definicija">prazna relacija</span>. V tej relaciji noben element množice $A$ ni v relaciji z nobenim drugim.

  - $R = A \times A \subseteq A \times A$. To je <span class="definicija">univerzalna relacija</span>. V tej relaciji je vsak element množice $A$ v relaciji z vsakim drugim.

  - $R = \{ (x,x) \mid x \in A \} \subseteq A \times A$. To je <span class="definicija">relacija enakosti</span>. Zanjo uporabljamo oznako $id_A$. V tej relaciji je vsak element množice $A$ v relaciji le s sabo.

</div>

Če je $R \subseteq A \times A$ relacija, potem namesto oznake $(x,y) \in R$ pišemo tudi $xRy$ in beremo *$x$ je v relaciji $R$ z $y$*.

Relacijo si lahko predstavljamo kot množico točk v *kvadratu* $A \times A$. Za vsaka $x,y \in A$, za katera je $xRy$, označimo točko $(x,y)$ v tem kvadratu. Na ta način lahko relacijo $R$ vidimo kot neko množico točk v $A \times A$. Kot pri grafih funkcij uporabimo terminologijo, ki nam pove, kako izgleda ta množica točk. <span class="definicija">Domena/definicijsko območje</span> relacije $R$ je množica
```{math}
\mathcal{D}_R = \{ x \in A \mid \exists y \in A \colon x R y \},
```
<span class="definicija">zaloga vrednosti</span> relacije $R$ pa je
```{math}
\mathcal{Z}_R = \{ y \in A \mid \exists x \in A \colon x R y \}.
```

<div class="zgled">

- Naj bo $A = \{ 1,2,3,4 \}$ in $R = \{ (1,3), (2,2), (4,3) \}$. V tem primeru je $\mathcal{D}_R = \{1,2,3\}$ in $\mathcal{Z}_R = \{2,3\}$.

- Naj bo $A = \NN_0$ in
  ```{math}
  R  = \{ (x,y) \in \NN_0 \times \NN_0 \mid \exists z \in \NN_0 \colon x + z + 1 = y \}.
  ```
  Relacija $R$ predstavlja relacijo $<$ v $\NN_0$. V tem primeru je $\mathcal{D}_R = \NN_0$ in $\mathcal{Z}_R = \NN$.

</div>

Izpostavimo <span class="definicija">nekaj lastnosti, ki jih lahko ima relacija</span> $R \subseteq A \times A$. Rečemo, da je relacija $R$:

- <span class="definicija">refleksivna</span>, če $\forall x \in A \colon x R x$,

- <span class="definicija">irefleksivna</span>, če $\forall x \in A \colon \lnot x R x$,

- <span class="definicija">simetrična</span>, če $\forall x,y \in A \colon (x R y \Rightarrow y R x)$,

- <span class="definicija">asimetrična</span>, če $\forall x,y \in A \colon (x R y \Rightarrow \lnot y R x)$,

- <span class="definicija">antisimetrična</span>, če $\forall x,y \in A \colon (xRy \land yRx \Rightarrow x = y)$,

- <span class="definicija">tranzitivna</span>, če $\forall x,y,z \in A \colon (xRy \land yRz \Rightarrow xRz)$,

- <span class="definicija">intranzitivna</span>, če $\forall x,y,z \in A \colon (xRy \land yRz \Rightarrow \lnot xRz)$,

- <span class="definicija">strogo sovisna</span>, če $\forall x,y \in A \colon (xRy \lor yRx)$,

- <span class="definicija">sovisna</span>, če $\forall x,y \in A \colon x \neq y \Rightarrow xRy \lor yRx$,

- <span class="definicija">enolična</span>, če $\forall x,y,z \in A \colon (xRy \land xRz \Rightarrow y = z)$.

<div class="zgled">

- Opazujmo relacijo enakosti $=$ v množici $A$. Od naštetih lastnosti je ta relacija refleksivna, simetrična, antisimetrična, tranzitivna in enolična.

- Opazujmo relacijo $\leq$ v $\NN_0$. Ta relacija je refleksivna, antisimetrična, tranzitivna in strogo sovisna.

- Opazujmo relacijo $<$ v $\NN_0$. Ta relacija je irefleksivna, asimetrična, tranzitivna in sovisna.

- Opazujmo relacijo *je mama* v množici ljudi. Ta relacija je irefleksivna, asimetrična, antisimetrična in intranzitivna.

</div>

## Ekvivalenčne relacije

Relacija $R \subseteq A \times A$ je <span class="definicija">ekvivalenčna</span>, če je refleksivna, simetrična in tranzitivna.

<div class="zgled">

Naslednje relacije so ekvivalenčne:

- relacija enakosti $=$,

- univerzalna relacija $A \times A$,

- relacija vzporednosti premic v $\RR^2$,

- relacija *ima enako barvo oči kot* v množici ljudi,

- relacija *ima enak BDP kot* v množici držav.

</div>

Naj bo $R \subseteq A \times A$ ekvivalenčna relacija. Vsakemu elementu $x \in A$ priredimo njegov <span class="definicija">ekvivalenčni razred</span>
```{math}
R[x] = \{ y \in A \mid yRx \}.
```
Element $x$ je <span class="definicija">predstavnik</span> ekvivalenčnega razreda $R[x]$. Množico vseh ekvivalenčnih razredov označimo z
```{math}
A/R = \{ R[x] \mid x \in A \}
```
in jo imenujemo <span class="definicija">kvocientna množica</span> množice $A$ po relaciji $R$.

<div class="lema">

Naj bo $R \subseteq A \times A$ ekvivalenčna relacija. Tedaj velja
```{math}
\forall x,y \in A \colon (R[x] = R[y] \Leftrightarrow xRy).
```

</div>

<div class="dokaz">

Vzemimo poljubna $x,y \in A$.

$(\Rightarrow)$: Predpostavimo, da velja $R[x] = R[y]$. Ker je $R$ refleksivna relacija, velja $xRx$, torej je $x \in R[x]$. Od tod sledi $x \in R[y]$, zato je $xRy$.

$(\Leftarrow)$: Predpostavimo, da velja $xRy$. Izberimo poljuben $z \in R[x]$. Velja torej $zRx$. Ker je $R$ tranzitivna relacija, iz $xRy$ in $zRx$ sledi $zRy$. To pomeni, da je $z \in R[y]$. Ker je bil $z$ poljuben element $R[x]$, od tod sklepamo, da velja $R[x] \subseteq R[y]$. Zaradi simetričnosti relacije $R$ lahko ponovimo ta argument, pri čemer vlogi $x$ in $y$ zamenjamo med sabo. Na ta način dobimo še vsebovanost $R[y] \subseteq R[x]$. Res torej velja $R[x] = R[y]$.

</div>

Iz leme v posebnem sledi, da je vsak element danega ekvivalenčnega razreda tudi njegov predstavnik.

<div class="izrek">

Naj bo $R \subseteq A \times A$ ekvivalenčna relacija. Tedaj velja:

1.  Za vsak $x \in A$ je $R[x] \neq \emptyset$.

2.  Za vsaka $x,y \in A$ velja implikacija $R[x] \neq R[y] \Rightarrow R[x] \cap R[y] = \emptyset$,

3.  $\bigcup_{x \in A} R[x] = A$.

</div>

Povedano še drugače, ekvivalenčna relacija razdeli množico $A$ na paroma tuje neprazne bloke.

<div class="dokaz">

1\. Vzemimo poljuben $x \in A$. Ker je $R$ refleksivna, velja $x R x$, zato je $x \in R[x]$. Torej je res $R[x] \neq \emptyset$.

2\. Vzemimo poljubna $x,y \in A$. Dokažimo kontrapozicijo trditve, se pravi veljavnost implikacije
```{math}
R[x]\cap R[y] \neq \emptyset \Rightarrow R[x] = R[y].
```
Predpostavimo lahko, da obstaja $z \in R[x] \cap R[y]$. To pomeni, da velja $zRx \land zRy$. Zaradi simetričnosti $R$ sledi $xRz \land zRy$, od koder zaradi tranzitivnosti $R$ velja $xRy$. Iz leme zdaj sledi, da je $R[x] = R[y]$.

3\. Vzemimo poljuben $x \in A$. Velja $x \in R[x]$, zato je $x \in \bigcup_{y \in A} R[y]$. Ker je bil $x$ poljuben, sledi $\bigcup_{y \in A} R[y] \supseteq A$. Obratna vsebovanost je očitna.

</div>

<div class="zgled">

- Naj bo $A$ množica ljudi in $R$ relacija *ima enako barvo oči kot*. Ekvivalenčni razred neke osebe z modrimi očmi torej sestavljajo ravno vse osebe z modrimi očmi. Ekvivalenčni razredi torej ustrezajo barvam oči.

- Naj bo $A$ poljubna množica in $R$ relacija enakosti v $A$. Za vsak $x \in A$ velja $R[x] = \{ x \}$. Množica ekvivalenčnih razredov je enaka $A/R = \{ \{ x \} \mid x \in A \}$.

- Naj bo $A$ poljubna množica in $R$ univerzalna relacija v $A$. Za vsak $x \in A$ velja $R[x] = A$. Imamo torej en sam ekvivalenčni razred in velja $A/R = \{ A \}$.

- Naj bo $A$ množica premic v prostoru $\RR^3$ in naj bo $R$ relacija vzporednosti premic. Za dano premico $p$ je torej $R[p]$ ravno množica vseh premic, ki so vzporedne $p$. Ekvivalenčni razredi torej ustrezajo vsem smerem v $\RR^3$ oziroma enotskim vektorjem v $\RR^3$.

- Množico $\ZZ$ lahko definiramo kot kvocientno množico množice $A = \NN_0 \times \NN_0$ po relaciji $R$, kjer je $(a,b)R(c,d)$, če in samo če $a+d = b+c$. Velja
  ```{math}
  R[(a,b)] = \{ (c,d) \in \NN_0 \times \NN_0 \mid c-d = a-b \},
  ```
  zato lahko množico ekvivalenčnih razredov $A/R$ identificiramo z množico $\ZZ$ prek bijekcije $R[(a,b)] \mapsto a-b$ za $(a,b) \in A$.

- Naj bo $m \in \NN$. Na množici celih števil $\ZZ$ definiramo relacijo <span class="definicija">kongruence po modulu</span> $m$ kot
  ```{math}
  x \equiv y \pmod{m} \Longleftarrow \exists k \in \ZZ \mid x - y = k \cdot m.
  ```
  Elementa $x,y \in \ZZ$ sta torej kongruentna po modulu $m$, če im samo če dajeta isti ostanek pri deljenju z $m$. Ni se težko prepričati, da je to ekvivalenčni relacija. Označimo jo z $R_m$. Ekvivalenčni razredi ustrezajo ostankom pri deljenju z $m$:
  ```{math}
  \begin{aligned}
          R_m[0] &= \{ x \in \ZZ \mid \exists k \in \ZZ \colon x = k m \}, \\
          R_m[1] &= \{ x \in \ZZ \mid \exists k \in \ZZ \colon x = k m + 1 \}, \\
          \vdots \\
          R_m[m-1] &= \{ x \in \ZZ \mid \exists k \in \ZZ \colon x = k m +m-1 \}.
      
  \end{aligned}
  ```
  Za $m = 1$ je torej $R_1 = A$, za $m = 2$ pa ima $R_2$ dva ekvivalenčna razreda, in sicer množico sodih števil in množico lihih števil.

</div>

## Operacije z relacijami

Relacije v dani množici $A$ so podmnožice $A \times A$, zato lahko z njimi izvajamo vse operacije, ki jih imamo na voljo z množicami. Nekaj osnovnih takih operacij in njihovih interpretacij je zbranih v naslednji trditvi.

<div class="trditev">

Naj bosta $R,S \subseteq A \times A$ relaciji. Potem so tudi
```{math}
R \cup S, \
    R \cap S, \
    R \backslash S, \
    R \oplus S = (R \cup S) \backslash (R \cap S)
```
relacije v $A$ in za vse $x,y \in A$ velja:

- $x(R \cup S) y \Leftrightarrow x R y \lor x S y$,

- $x(R \cap S) y \Leftrightarrow x R y \land x S y$,

- $x(R \backslash S) y \Leftrightarrow x R y \land \lnot (x S y)$,

- $x(R \oplus S) y \Leftrightarrow x R y + x S y$.

</div>

Oglejmo si še nekaj manj poznanih operacij z relacijami. Za dano relacijo $R \subseteq A \times A$ je <span class="definicija">komplement relacije</span> $R$ relacija $R^c = A \times A \backslash R$. <span class="definicija">Transponirana relacija</span> relacije $R$ je relacija $R^T = \{ (x,y) \in A \times A \mid (y,x) \in R \}$. Tudi ti dve relaciji lahko intepretiramo na enostaven način.

<div class="trditev">

Za vse $x,y \in A$ velja:

- $x R^c y \Leftrightarrow \lnot (x R y)$,

- $x R^T y \Leftrightarrow y R x$.

</div>

<div class="zgled">

Naj bo $A = \NN$. Med dobro poznanimi relacijami v $\NN$ veljajo naslednje enakosti:

- $(<) \cup (=) = (\leq)$

- $(\leq) \backslash (=) = (<)$,

- $(\leq) \cap (\geq) = (=)$,

- $(\leq) \cup (\geq) = \NN \times \NN$,

- $(<) \cap (>) = \emptyset$,

- $(<) \cup (>) = (\neq) = (=)^c$,

- $(\leq)^c = (>)$,

- $(\leq)^T = (\geq)$.

</div>

Nazadnje si oglejmo še eno nekoliko bolj zapleteno operacijo. Naj bosta $R,S$ relaciji v $A$. <span class="definicija">Kompozitum</span> relacij $R,S$ je relacija
```{math}
R \circ S = \{ (x,y) \in A \times A \mid \exists u \in A \mid (x S u \land u R y)\}.
```

Oglejmo si nekaj osnovnih lastnosti operacij transponiranja in kompozituma. Za vse relacije $R,S,T \subseteq A \times A$ velja:

- $(R^T)^T = R$,

- $(R \cup S)^T = R^T \cup S^T$,  
  $(R \cap S)^T = R^T \cap S^T$,  
  $(R \backslash S)^T = R^T \backslash S^T$,  
  $(R \oplus S)^T = R^T \oplus S^T$,

- $R \circ id_A = R = id_A \circ R$ (<span class="definicija">$id_A$ je enota za komponiranje</span>),

- $(R \circ S) \circ T = R \circ (S \circ T)$ (<span class="definicija">asociativnost komponiranja</span>),

- $(R \circ S)^T = S^T \circ R^T$,

- $(R \cup S) \circ T = R \circ T \cup S \circ T$,  
  $R \circ (S \cup T) = R \circ S \cup R \circ T$ (<span class="definicija">distributivnost $\circ$ glede na $\cup$</span>),

- $R \subseteq S \Rightarrow R \circ T \subseteq S \circ T$,  
  $R \subseteq S \Rightarrow T \circ R \subseteq T \circ S$ (<span class="definicija">monotonost $\circ$ glede na $\subseteq$</span>).

Preverimo le zelo pomembno asociativnost komponiranja. Za vsaka $x,y \in A$ velja
```{math}
\begin{aligned}
    x (R \circ S) \circ T y &\Leftrightarrow \exists u \colon (xTu \land u R \circ S y) \\
    &\Leftrightarrow \exists u \colon (xTu \land \exists v \colon (uSv \land v Ry)) \\
    &\Leftrightarrow \exists u \exists v \colon (xTu \land (uSv \land vRy)) \\
    &\Leftrightarrow \exists v \exists u \colon ((xTu \land uSv) \land vRy) \\
    &\Leftrightarrow \exists v \colon (\exists u \colon ( (x T u \land uSv) \land vRy) ) \\
    &\Leftrightarrow \exists v \colon (x S \circ T v \land vRy) \\
    &\Leftrightarrow x R \circ (S \circ T) y.
\end{aligned}
```

<div class="zgled">

Naj bo $A$ množica ljudi.

- Kaj je relacija $\text{hči} \circ \text{mož}$? Za osebi $x,y \in A$ velja
  ```{math}
  x (\text{hči} \circ \text{mož}) y \Leftrightarrow
          \exists u \colon (x \text{mož} u \land u \text{hči} y),
  ```
  torej kadar je $x$ hčerin mož $y$-a, se pravi kadar je $x$ zet $y$. Velja torej $\text{hči} \circ \text{mož} = \text{zet}$.

- $\text{oče} \circ \text{brat} = \text{stric}$

- $\text{zakonec} \circ \text{mati} = \text{tašča}$

</div>

Osnovne lastnosti relacij lahko opišemo v jeziku operacij z relacijami na naslednji način.

<div class="izrek">

Naj bo $R \subseteq A \times A$. Tedaj je:

1.  $R$ refleksivna, če in samo če $id_A \subseteq R$,

2.  $R$ irefleksivna, če in samo če $R \cap id_A = \emptyset$,

3.  $R$ simetrična, če in samo če $R = R^T$,

4.  $R$ asimetrična, če in samo če $R \cap R^T = \emptyset$,

5.  $R$ antisimetrična, če in samo če $R \cap R^T \subseteq id_A$,

6.  $R$ tranzitivna, če in samo če $R \circ R \subseteq R$,

7.  $R$ intranzitivna, če in samo če $(R \circ R) \cap R = \emptyset$,

8.  $R$ strogo sovisna, če in samo če $R \cup R^T = A \times A$,

9.  $R$ sovisna, če in samo če $R \cup R^T \cup id_A = A \times A$,

10. $R$ enolična, če in samo če $R \circ R^T \subseteq id_A$.

</div>

<div class="dokaz">

6\. $(\Rightarrow)$: Predpostavimo, da je $R$ tranzitivna. Dokazati želimo, da je $R \circ R \subseteq R$. V ta namen izberimo poljuben element $(x,y) \in R \circ R$. To pomeni, da obstaja $u \in A$, za katerega velja $xRu \land uRy$. Iz tranzitivnosti relacije $R$ od tod sledi $xRy$. Slednje pomeni ravno $(x,y) \in R$. Ker je bil $(x,y)$ poljuben element $R \circ R$, smo s tem dokazali vsebovanost $R \circ R \subseteq R$.

6\. $(\Leftarrow)$: Predpostavimo, da je $R \circ R \subseteq R$. Dokazati želimo, da je $R$ tranzitivna. V ta namen predpostavimo, da za poljubne elemente $x,y,z \in A$ velja $xRy$ in $yRz$. Torej $\exists u \colon (xRu \land uRz)$, kar pomeni, da je $(x,z) \in R \circ R$. Ker je $R \circ R \subseteq R$, od tod sledi $(x,z) \in R$, se pravi $xRz$. S tem smo dokazali tranzitivnost relacije $R$.

10\. Velja
```{math}
\begin{aligned}
    \text{$R$ enolična} &\Leftrightarrow \forall x,y,z \colon (xRy \land xRz \Rightarrow y=z) \\
    &\Leftrightarrow \forall x,y,z \colon (yR^Tx \land xRy \Rightarrow y = z) \\
    &\Leftrightarrow \forall y,z \colon \left( \forall x \colon (\lnot(yR^Tx \land xRy) \lor y=z) \right) \\
    &\Leftrightarrow \forall y,z \colon \left( \lnot \exists x \colon (yR^Tx \land xRy) \lor y=z \right) \\
    &\Leftrightarrow \forall y,z \colon \left( \lnot (y R \circ R^T z) \lor y = z \right) \\
    &\Leftrightarrow \forall y,z \colon (y R \circ R^T z \Rightarrow y = z) \\
    &\Leftrightarrow \forall y,z \colon \left( (y,z) \in R \circ R^T \Rightarrow y = z \right) \\
    &\Leftrightarrow R \circ R^T \subseteq id_A.
\end{aligned}
```

</div>

## Potence in ovojnice relacij

Naj bo $R \subseteq A \times A$. <span class="definicija">Kompozicijsko potenco</span> relacije $R$ definiramo induktivno na naslednji način:

osnova:  
$R^0 = id_A$,

indukcijski korak:  
$\forall n \in \NN_0 \colon R^{n+1} = R^n \circ R$.

<div class="zgled">

Najprej velja
```{math}
R^1 = R^{0+1} = R^0 \circ R = id_A \circ R = R,
```
za tem velja
```{math}
R^2 = R^{1+1} = R^1 \circ R = R \circ R
```
in induktivno je $R^n$ enak kompoziciji $n$-tih $R$-jev. Ker je operacija komponiranja asociativna, nam pri tem ni potrebno postavljati oklepajev, saj je rezultat neodvisen od vrstnega reda izvajanja kompozicij.

</div>

Kompozicijske potence delijo nekatere lastnosti s potencami števil.

<div class="trditev">

Za vse $m,n \in \NN_0$ velja $R^n \circ R^m = R^{n+m}$ in $(R^n)^m = R^{n \cdot m}$.

</div>

<div class="dokaz">

Vaja. Najlažje bo šlo z indukcijo na $m$.

</div>

<div class="zgled">

Naj bo $A$ množica ljudi in $R = \text{otrok}$. Tedaj je $R^2 = \text{vnuk} \cup \text{vnukinja}$ in $R^3 = \text{pravnuk} \cup \text{pravnukinja}$ in za vsak $n \geq 2$ je
```{math}
R^n = \text{(pra)$^{n-2}$vnuk} \cup \text{(pra)$^{n-2}$vnukinja}.
```

</div>

Naj bo $R \subseteq A \times A$. S pomočjo kompozicijske potence definirajmo še dve pomembni konstrukciji, in sicer

- $R^+ = \bigcup_{k = 1}^\infty R^k = R \cup R^2 \cup R^3 \cup \cdots$,

- $R^* = \bigcup_{k = 0}^\infty R^k = id_A \cup R \cup R^2 \cup R^3 \cup \cdots$,

Seveda velja $R^* = R^+ \cup id_A$. Relaciji $R^+$ in $R^*$ lahko opišemo še na naslednji način. Za vsaka $x,y \in A$ velja:

- $x R^+ y \Leftrightarrow \exists k \in \NN \colon x R^k y$,[^1]

- $x R^+ y \Leftrightarrow \exists k \in \NN_0 \colon x R^k y$,[^2]

<div class="zgled">

Naj bo $A$ množica ljudi in $R = \text{otrok}$. Velja $R^+ = \text{potomec} \cup \text{potomka}$.

</div>

Nazadnje se pogovorimo še o tem, kako dano relacijo $R \subseteq A \times A$, ki ne zadošča določenim želenim lastnostim,[^3] *popraviti* do nove relacije, ki ni preveč drugačna od $R$, a za razliko od $R$ zadošča želenim lastnostim. Iščemo torej novo relacijo, ki *vsebuje* relacijo $R$, ima želene lastnosti in je hkrati *najmanjša* relacija med vsemi relacijami, ki imajo ti dve lastnosti.

Naj bo $\mathcal{L}$ neka lasnost relacij v množici $A$. Naj bo $R \subseteq A \times A$. Relacija $R^{\mathcal{L}}$ je $\mathcal{L}$-ovojnica relacije $R$, če velja:

- $R \subseteq R^{\mathcal{L}}$,

- $R^{\mathcal{L}}$ ima lastnost $\mathcal{L}$,

- če ima poljubna relacija $S \subseteq A \times A$ lastnost $\mathcal{L}$ in velja $R \subseteq S$, potem je $R^{\mathcal{L}} \subseteq S$.

V primeru, ko relacija $R$ že ima lastnost $\mathcal{L}$, je seveda $R^{\mathcal{L}} = R$. V splošnem pa ovojnica $R^{\mathcal{L}}$ ne obstaja vedno. Prepričajmo se, da vselej obstajajo vsaj ovojnice glede na najbolj pomembne lastnosti relacij.

<div class="izrek">

Za vsako relacijo $R \subseteq A \times A$ obstajajo ovojnice $R^\text{refleksivnost}$, $R^\text{simetričnost}$, $R^\text{tranzitivnost}$, $R^\text{ekvivalenčnost}$ in velja:

- $R^\text{refleksivnost} = R \cup id_A$ (<span class="definicija">refleksivna ovojnica</span>),

- $R^\text{simetričnost} = R \cup R^T$ (<span class="definicija">simetrična ovojnica</span>),

- $R^\text{tranzitivnost} = R^+$ (<span class="definicija">tranzitivna ovojnica</span>),

- $R^\text{ekvivalenčnost} = (R \cup R^T)^*$ (<span class="definicija">ekvivalenčna ovojnica</span>).

</div>

<div class="dokaz">

Preverimo le trditev glede tranzitivne ovojnice. Dokazati torej želimo, da relacija $R^+$ zadošča vsem trem kriterijem v definiciji ovojnice.

Preverimo najprej, da velja $R \subseteq R^+$. Res, ker je $R^+ = R \cup R^2 \cup \cdots$, je seveda $R \subseteq R^+$.

Prepričajmo se zdaj, da je relacija $R^+$ vselej tranzitivna. V ta namen predpostavimo, da za poljubne $x,y,z \in A$ velja $xR^+y$ in $yR^+z$. To pomeni
```{math}
\exists k \in \NN \colon x R^k y \land \exists l \in \NN \colon y R^l z,
```
kar lahko prepišemo v
```{math}
\exists k, l \in \NN \colon (x R^k y \land y R^l z).
```
Od tod sklepamo, da velja
```{math}
\exists k, l \in \NN \colon (x R^l \circ R^k z),
```
torej velja tudi
```{math}
\exists m \in \NN \colon x R^m z,
```
saj lahko vzamemo $m = k + l$. S tem smo dokazali $x R^+ z$, kar pomeni, da je relacija $R^+$ res tranzitivna.

Nazadnje preverimo še, da je $R^+$ najmanjša tranzitivna relacija, ki vsebuje $R$. V ta namen naj bo $S$ tranzitivna relacija v $A$, za katero velja $R \subseteq S$. Dokazati želimo, da velja $R^+ \subseteq S$. Ker je $R^+ = R \cup R^2 \cup R^3 \cup \cdots$, bo za to dovolj dokazati, da za vsak $k \in \NN$ velja vsebovanost $R^k \subseteq S$. Slednje dokažimo z indukcijo na $k$.

Osnova indukcije ($k = 1$):  
Dokazati želimo $R \subseteq S$. To velja po predpostavki.

Indukcijski korak ($k \to k+1$):  
Predpostavimo, da velja $R^k \subseteq S$. Dokazati želimo, da velja $R^{k+1} \subseteq S$. Na predpostavki uporabimo $\circ R$ in zaradi monotonosti kompozicije dobimo $R^{k+1} = R^k \circ R \subseteq S \circ R$. Hkrati lahko na predpostavki $R \subseteq S$ uporabimo $S \circ$ in zopet iz monotonosti sledi $S \circ S \subseteq S \circ S$. Ker je $S$ tranzitivna relacija, velja $S \circ S \subseteq S$. S tem smo torej dokazali
```{math}
R^{k+1} \subseteq S \circ R \subseteq S \circ S \subseteq S,
```
kar je ravno želena vsebovanost.

</div>

<div class="zgled">

Naj bo $A$ množica ljudi. Velja
```{math}
\text{otrok}^\text{tranzitivnost} = \text{otrok}^+ = \text{potomec} \cup \text{potomka}.
```

</div>

[^1]: To pomeni, da v grafu relacije $R$ obstaja usmerjena pot dolžine vsaj $1$ od $x$ do $y$. Več o takih poteh bomo spoznali v razdelku o grafih.

[^2]: To pomeni, da v grafu relacije $R$ obstaja usmerjena pot od $x$ do $y$, pri čemer dopuščamo tudi možnost zanke.

[^3]: Na primer, $R$ morda ni refleksivna ali pa ni tranzitivna.
