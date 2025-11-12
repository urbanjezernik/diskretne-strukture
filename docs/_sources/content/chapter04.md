```{raw} html
<style>
  body { counter-reset: chapter 3 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Urejenosti

V tem poglavju si bomo podrobneje pogledali *strukture urejenosti*. To so relacije na dani množici, ki imajo določene dodatne lastnosti, s katerimi izrazimo, da te relacije podajajo *ureditev* elementov dane množice. Glede na lastnosti razlikujemo več tipov urejenosti.

## Delna in linearna urejenost

Naj bo $R$ relacija v $A$. Rečemo, da $R$ <span class="definicija">delno ureja</span> $A$, če je $R$ refleksivna, antisimetrična in tranzitivna. Rečemo, da $R$ <span class="definicija">linearno ureja</span> $A$, če $R$ delno ureja $A$ in je $R$ sovisna.

<div class="zgled">

- Relacija $\leq$ linearno ureja realna števila $\RR$.

- Relacija deljivosti $|$ delno ureja naravna števila $\NN$.

- Naj bo $A$ neka množica množic, na primer $A = \{ B \mid B \subseteq \{ 1,2,\dots, 10\} \}$. Tedaj relacija $\subseteq$ vsebovanosti množic delno ureja $A$.

</div>

Kadar je $R$ relacija delne urejenosti, ponavadi namesto oznake $R$ pišemo kar $\leq$. Formulo $x R y$ torej zapišemo kot $x \leq y$, preberemo pa jo kot *$x$ je pod $y$*.

Iz vsake relacije delne urejenosti $\leq$ v $A$ lahko konstruiramo še dve relaciji, in sicer:

- <span class="definicija">relacija stroge delne urejenosti</span> $<$:
  ```{math}
  \forall x, y \in A \colon (x < y \Leftrightarrow x \leq y \land x \neq y),
  ```

- <span class="definicija">relacija neposrednega predhodnika</span> $< \cdot$:
  ```{math}
  \forall x, y \in A \colon \left( x < \cdot y \Leftrightarrow x < y \land \lnot \exists z \in A \colon (x < z \land z < y) \right).
  ```

Relacija $<$ je vselej irefleksivna, asimetrična in tranzitivna. Relacija $< \cdot$ je vselej irefleksivna, asimetrična in intranzitivna.

Delno urejeno množico $A$ lahko predstavimo grafično s <span class="definicija">Hassejevim diagramom</span>. Elemente množice $A$ pri tem narišemo kot točke v ravnini. Če je $x < y$, potem $x$ narišemo niže od točke $y$. Če je $x < \cdot y$, potem $x$ in $y$ povežemo s črto.

<div class="zgled">

- Naj bo $A = \{ 1,2,\dots, 10 \}$, opremljena z relacijo deljivosti naravnih števil $|$.

  <figure>
  <img src="img/relacije-hasse.png" />
  <figcaption>Hassejev diagram relacije deljivosti</figcaption>
  </figure>

- Naj bo $A = \{ B \mid B \subseteq \{ 1,2,3 \} \}$, opremljena z relacijo $\subseteq$ vsebovanosti množic.

  <figure>
  <img src="img/relacije-hasse-mnozice.png" />
  <figcaption>Hassejev diagram relacije vsebovanosti množic</figcaption>
  </figure>

- Naj bo $A = \{ 1,2,3,4,5 \}$, opremljena z običajno relacijo $\leq$ (manjše ali enako).

  <figure>
  <img src="img/relacije-hasse-linearna.png" />
  <figcaption>Hassejev diagram običajne relacije <span class="math inline">≤</span></figcaption>
  </figure>

</div>

## Posebni elementi v delno urejenih množicah

Naj relacija $\leq$ delno ureja množico $A$. Izpostavimo nekaj posebnih elementov množice $A$ glede na to delno urejenost, in sicer tiste, ki so v Hassejevem diagramu narisani tako, da pod oziroma nad njimi ni nobenega drugega elementa ali pa so celo pod oziroma nad vsemi drugimi elementi.

Naj bo $a \in A$. Rečemo, da:

- $a$ je <span class="definicija">minimalen</span> v $A$, če in samo če $\forall x \in A \colon (x \leq a \Rightarrow x = a)$,

- $a$ je <span class="definicija">maksimalen</span> v $A$, če in samo če $\forall x \in A \colon (a \leq x \Rightarrow x = a)$,

- $a$ je <span class="definicija">prvi/najmanjši</span> v $A$, če in samo če $\forall x \in A \colon a \leq x$,

- $a$ je <span class="definicija">zadnji/največji</span> v $A$, če in samo če $\forall x \in A \colon x \leq a$.

<div class="zgled">

- Naj bo $A = \{ 1, 2, \dots, 10 \}$, opremljena z relacijo deljivosti $|$. Minimalni element je $1$ in to je hkrati tudi prvi element. Maksimalnih elementov je več, in sicer $7$, $10$, $9$, $6$, $8$. Zadnjih elementov pa ni.

- Naj bo $A = \{ B \mid B \subseteq \{ 1, 2, 3 \} \} \backslash \{ \emptyset \}$, opremljena z relacijo vsebovanosti množic $\subseteq$. Minimalni elementi so $\{ 1 \}$, $\{ 2 \}$, $\{ 3 \}$. Prvih elementov ni. Maksimalni element je $\{ 1, 2, 3 \}$ in ta je hkrati zadnji.

- Naj bo $A = \ZZ$, opremljena z relacijo $\leq$. Tukaj ni nobenih posebnih elementov.

- Naj bo $A$ poljubna množica, opremljena z relacijo $id_A$. Tukaj je vsak element maksimalen in vsak minimalen. Če ima $A$ vsaj $2$ elementa, potem ni niti prvih niti zadnjih elementov.

</div>

<div class="trditev">

Naj bo $A$ delno urejena z $\leq$.

1.  Vsak prvi element je minimalen.

2.  Vsak zadnji element je maksimalen.

3.  Če v $A$ obstaja prvi element, je en sam.

4.  Če v $A$ obstaja zadnji element, je en sam.

</div>

<div class="dokaz">

1\. Naj bo $a \in A$ prvi. Dokazujemo, da je $a$ minimalen. V ta namen izberimo poljuben $x \in A$, za katerega velja $x \leq a$. Dokazati želimo, da je $x = a$. Ker je $a$ prvi, velja $a \leq x$. Iz antisimetričnosti relacije $\leq$ od tod sledi $x = a$.

2\. Naj bosta $a,b \in A$ prva. Dokazati želimo, da je $a = b$. Ker je $a$ prvi, velja $a \leq b$. Ker je $b$ prvi, velja $b \leq a$. Iz antisimetričnosti relacije $\leq$ sledi $a = b$.

</div>

<div class="trditev">

Naj bo $A$ *linearno* urejena z $\leq$.

1.  Element $a \in A$ je prvi, če in samo če je $a$ minimalen.

2.  Element $a \in A$ je zadnji, če in samo če je $a$ maksimalen.

</div>

<div class="dokaz">

1\. Po prejšnji trditvi bo dovolj dokazati implikacijo $(\Leftarrow)$. Naj bo torej $a \in A$ minimalen. Dokazati želimo, da je $a$ prvi. V ta namen izberimo poljuben $x \in A$. Dokazati želimo, da je $a \leq x$. Linearna urejenost je strogo sovisna, zato velja $a \leq x$ ali $x \leq a$. Uporabimo analizo primerov.

- Če je $a \leq x$, potem želeno velja.

- Če je $x \leq a$, iz minimalnosti $a$ sledi $x = a$, torej velja tudi $a \leq x$. .

</div>

Naj bo množica $A$ delno urejena z relacijo $R$ in naj bo $B \subseteq A$ poljubna podmnožica $A$. V tem primeru lahko relacijo $R$ <span class="definicija">zožimo</span> na množico $B$ in dobimo relacijo
```{math}
R |_B = R \cap (B \times B) \subseteq B \times B
```
v množici $B$. Na ta način lahko govorimo o minimalnih, maksimalnih, prvih in zadnjih elementih množice $B$ glede na relacijo $R|_B$.

- Če ima $B$ prvi element, ga imenujemo <span class="definicija">minimum</span> množice $B$ in označimo z $\min B$.

- Če ima $B$ zadnji element, ga imenujemo <span class="definicija">maksimum</span> množice $B$ in označimo z $\max B$.

- Element $a \in A$ je <span class="definicija">zgornja meja</span> za $B$, če $\forall x \in B \colon \; x \leq a$.

- Element $a \in A$ je <span class="definicija">spodnja meja</span> za $B$, če $\forall x \in B \colon \; a \leq x$.

<div class="zgled">

- Naj bo $A = \RR$, opremljena z relacijo $\leq$. Naj bo $B = (0,1)$ odprti interval. Tedaj $\min B$ in $\max B$ ne obstajata. Vsako število $a \geq 1$ je zgornja meja za $B$ in vsako število $a \leq 0$ je spodnja meja za $B$.

- Naj bo $A = \NN$, opremljena z relacijo deljivosti $|$. Naj bo $B = \{ 12, 18, 24, 72 \}$. Tedaj $\min B$ ne obstaja, $\max B$ pa je enak $72$. Vsako število oblike $72k$ za $k \in \NN$ je zgornja meja za $B$. Števila $1$,$2$,$3$,$6$ so spodnje meje za $B$.

</div>

Med vsemimi zgornjimi oziroma spodnjimi mejami včasih obstajajo najmanjše oziroma največje take meje. Za te uvedemo posebno ime.

- Naj bo $M$ množica vseh zgornjih mej za $B$, se pravi
  ```{math}
  M = \{ a \in A \mid \forall x \in B \colon \; x \leq a \}.
  ```
  Če ima $M$ prvi element, ga imenujemo <span class="definicija">supremum</span> ali <span class="definicija">najmanjša zgornja meja</span> množice $B$ in označimo s $\sup B$.

- Naj bo $m$ množica vseh spodnjih mej za $B$, se pravi
  ```{math}
  m = \{ a \in A \mid \forall x \in B \colon \; a \leq x \}.
  ```
  Če ima $m$ zadnji element, ga imenujemo <span class="definicija">infimum</span> ali <span class="definicija">največja spodnja meja</span> množice $B$ in označimo s $\inf B$.

<div class="zgled">

- Naj bo $A = \RR$, opremljena z običajno relacijo $\leq$. Naj bo $B = (0,1)$. Velja $\inf B = 0$ in $\sup B = 1$.

- Naj bo $A = \NN$, opremljena z relacijo deljivosti $|$. Naj bo $B = \{ 12, 18, 24, 72 \}$. Tedaj je infimum $\inf B$ enak največjemu skupnemu delitelju $D(12, 18, 24, 72) = 6$, supremum $\sup B$ pa je enak najmanjšemu skupnemu večkratniku $v(12, 18, 24, 72) = 72$.

- Infimum in supremum ne obstajata vedno. Na primer, če vzamemo $A = \RR$ z relacijo $\leq$ in $B = \{ n \mid n \in \NN \}$, potem množica $B$ nima zgornjih mej v množici $A$, torej je $M = \emptyset$. Prazna množica seveda nima prvega elementa, torej množica $B$ nima supremuma.

</div>

Kadar ima množica $B$ zadnji element, je ta seveda enak $\sup B$. Sorodno velja v primeru, ko ima $B$ prvi element, takrat je ta enak $\inf B$.

## Mreža

Nazadnje si na hitro oglejmo še eno strukturo urejenosti, ki leži vmes med delno urejenostjo in linearno urejenostjo.

Delno urejena množica $A$ je <span class="definicija">mreža</span>, če za vsaka dva elementa $a,b \in A$ obstajata $\inf \{ a, b \}$ in $\sup \{ a, b \}$.

<div class="zgled">

- Vsaka linearno urejena množica $A$ je mreža. Res, za vsaka $a,b \in A$ velja $\inf \{ a, b \} = \min \{ a,b \}$ in $\sup \{ a, b \} = \max \{ a, b \}$ in tako minimum kot maksimum obstajata, ker je $A$ linearno urejena in zato v posebnem sovisna.

- Naj bo $A = \NN$, opremljena z relacijo deljivosti $|$. Ta delno urejena množica je mreža, saj za vsaka $a, b \in \NN$ velja $\inf \{ a,b \} = D(a,b)$ in $\sup \{ a, b \} = v(a,b)$.

- Naj bo $S$ poljubna neprazna množica in naj bo $A$ množica podmnožic $S$, se pravi $A = \{ B \mid B \subseteq S \}$, opremljena z relacijo vsebovanosti množic $\subseteq$. Ta delno urejena množica je mreža, saj za vsaki množici $B, C \in A$ velja $\inf \{ B, C \} = B \cap C$ in $\sup \{ B, C \} = B \cup C$.

- Zadnji zgled modificirajmo tako, da za množico $A$ vzamemo le *neprazne* podmnožice množice $S$. To je še vedno delno urejena množica. Za različna elementa $x,y \in S$ infimum $\inf \{ \{ x \}, \{ y \} \}$ *ne* obstaja. To torej ni mreža.

</div>

*Linearna urejenost* je torej poseben primer *mreže*, ta pa je poseben primer *delne urejenosti*.
