```{raw} html
<style>
  body { counter-reset: chapter 4 izrek 0 zgled 0 domacanaloga 0
                 lema 0 trditev 0 definicija 0 dokaz 0; }
</style>
```

# Grafi

Diskretne strukture, ki smo jih obravnavali do sedaj (torej relacije), so izhajale iz našega študija izjavnega in predikatnega računa. Ogledali smo si že, kako lahko relacije predstavimo z *grafom relacije*. V tem zadnjem razdelku bomo ta abstrakten objekt, *graf*, obravnavali neodvisno. Ta diskretna struktura je zelo pogosta v različnih področjih matematike, še posebej v njenih aplikacijah v resničnem svetu. Ogledali si bomo nekaj lastnosti te strukture in dokazali nekaj osnovnih izrekov o njej.

## Osnovne definicije

<span class="definicija">Graf</span> $G$ je par množic $(V,E)$, kjer je $V$ neka končna[^1] neprazna množica, $E$ pa je neka množica dvoelementnih podmnožic[^2] množice $V$. Množici $V$ pravimo <span class="definicija">množica točk/vozlišč grafa</span>, množici $E$ pa pravimo <span class="definicija">množica povezav grafa</span>.

<div class="zgled">

Naj bo $V = \{ 1, 2, 3, 4, 5 \}$ in naj bo
```{math}
E = \{  
        \{ 1, 2 \}, 
        \{ 2, 3 \},
        \{ 3, 4 \},
        \{ 4, 1 \},
        \{ 1, 3 \},
        \{ 4, 5 \}
         \}.
```

Graf $G = (V,E)$ si lahko vizualiziramo tako, da vozlišča narišemo kot točke v ravnini, za tem pa vozlišči $u,v \in V$ povežemo, če in samo če je $\{ u, v \} \in E$.

<figure>
<img src="img/grafi-prvizgled.png" />
<figcaption>Zgled vizualizacije grafa</figcaption>
</figure>

</div>

Kadar za vozlišči $u,v \in V$ velja $\{ u, v \} \in E$, potem rečemo, da sta vozlišči $u,v$ <span class="definicija">sosednji</span> in pišemo $u \sim v$. Povezavo $\{ u, v \} \in E$ včasih pišemo krajše kot $uv$.

Včasih definicijo grafa nekoliko omehčamo do te mere, da dopustimo obstoj <span class="definicija">vzporednih povezav</span> (to pomeni, da med istim parom točk obstaja več povezav) in <span class="definicija">zank</span> (to so povezave, ki imajo obe krajišči enaki). Takim splošnejšim strukturam rečemo <span class="definicija">multigrafi</span>.

<div class="zgled">

<figure>
<img src="img/grafi-multigraf.png" />
<figcaption>Zgled multigrafa</figcaption>
</figure>

</div>

Naj bo $G = (V,E)$ graf in $u \in V$. <span class="definicija">Stopnja točke</span> $u$ je število povezav v $E$, ki imajo $u$ za svoje krajišče. Stopnjo označimo kot $\deg_G(u)$ ali krajše kot $d(u)$. Točkam stopnje $0$ pravimo <span class="definicija">izolirane točke</span>, točkam stopnje $1$ pa <span class="definicija">listi</span>.

<div class="zgled">

Naj bo $G$ graf, predstavljen na naslednji sliki.

<figure>
<img src="img/grafi-std-izolirana.png" />
<figcaption>Graf z listom in izolirano točko</figcaption>
</figure>

Stopnje vozlišč so $d(a) = 2$, $d(b) = 2$, $d(c) = 3$, $d(d) = 1$, $d(e) = 0$. Vozlišče $d$ je list, vozlišče $e$ pa je izolirana točka.

</div>

Najmanjšo stopnjo vozlišča označimo z
```{math}
\delta(G) = \min \{ d(u) \mid u \in V \},
```
največjo stopnjo pa označimo z
```{math}
\Delta(G) = \max \{ d(u) \mid u \in V \}.
```
Graf je <span class="definicija">regularen</span>, če je $\delta(G) = \Delta(G)$, torej če imajo vsa vozlišča enako stopnjo. Če je ta stopnja $d$, rečemu grafu <span class="definicija">$d$-regularen</span>.

<div class="zgled">

- <figure>
  <img src="img/grafi-2reg.png" />
  <figcaption>Zgled <span class="math inline">2</span>-regularnega grafa</figcaption>
  </figure>

- <figure>
  <img src="img/grafi-3reg.png" />
  <figcaption>Zgled <span class="math inline">3</span>-regularnega grafa</figcaption>
  </figure>

- <figure>
  <img src="img/opis-petersen.png" />
  <figcaption>Petersenov graf je <span class="math inline">3</span>-regularen</figcaption>
  </figure>

</div>

Grafe lahko ekvivalentno opišemo s pomočjo matrik. Za to imamo na voljo dve možnosti.

Prva možnost je <span class="definicija">matrika sosednosti</span> grafa $G$. Za njeno konstrukcijo najprej oštevilčimo množico vozlišč $V = \{ v_1, v_2, \dots, v_n \}$ in nato sestavimo matriko $A(G) = [a_{ij}]_{1 \leq i,j \leq n}$ z vnosi
```{math}
a_{ij} = \begin{cases}
        1 & v_i \sim v_j \\
        0 & \text{sicer.}
    \end{cases}
```

<div class="zgled">

Naj bo $G$ graf, predstavljen na naslednji sliki. Ta graf bomo srečali še večkrat, zato mu dajmo ime <span class="definicija">lizika</span>.

<figure>
<img src="img/grafi-std.png" />
<figcaption>Lizika</figcaption>
</figure>

Matrika sosednosti lizike je
```{math}
A(G) = \begin{pmatrix}
        0 & 1 & 1 & 0 \\
        1 & 0 & 1 & 0 \\
        1 & 1 & 0 & 1 \\
        0 & 0 & 1 & 0
    \end{pmatrix}.
```
Opazimo, da je ta matrika simetrična. To ni slučaj, saj za vsaka $i,j$ velja $a_{ij} = 1$, če in samo če je $v_i \sim v_j$, torej če in samo če je $a_{ji} = 1$.

</div>

Druga možnost je <span class="definicija">incidenčna matrika</span> grafa $G$. Za njeno konstrukcijo najprej oštevilčimo množico vozlišč $V = \{ v_1, v_2, \dots, v_n \}$ in povezav $E = \{ e_1, e_2, \dots, e_m \}$ in nato sestavimo matriko $B(G) = [b_{ij}]_{1 \leq i \leq n, 1 \leq j \leq m}$ z vnosi
```{math}
b_{ij} = \begin{cases}
        1 & v_i \in e_j \\
        0 & \text{sicer.}
    \end{cases}
```

<div class="zgled">

Opazujmo liziko. Povezave označimo kot $e_1 = \{ 1, 2 \}$, $e_2 = \{ 1, 3 \}$, $e_3 = \{ 2, 3 \}$ in $e_4 = \{ 3, 4 \}$. Incidenčna matrika je
```{math}
B(G) =
    \begin{pmatrix}
        1 & 1 & 0 & 0 \\
        1 & 0 & 1 & 0 \\
        0 & 1 & 1 & 1 \\
        0 & 0 & 0 & 1
    \end{pmatrix}.
```
Ta matrika ni simetrična. V splošnem to niti ni kvadratna matrika, saj je število vozlišč grafa lahko različno od števila povezav.

</div>

Vsak stolpec incidenčne matrike vsebuje natanko dve enici, ker ima vsaka povezava natanko dve krajišči. Torej je vsota vseh členov matrike $B(G)$ enaka dvakratniku števila povezav, se pravi $2 |E|$. Po drugi strani pa je število enic v $i$-ti vrstici matrike $B(G)$ enako stopnji $d(v_i)$. Torej je vsota vseh členov matrike $B(G)$ enaka vsoti stopenj vseh vozlišč grafa. Na ta način smo izpeljali naslednjo elementarno, a pomembno lastnost grafov.

<div class="lema">

Za vsak graf $G = (V,E)$ velja
```{math}
\sum_{v \in V} d(v) = 2 |E|.
```

</div>

<div class="zgled">

- Petersenov graf je $3$-regularen graf na $10$ vozliščih. Iz leme o rokovanju sklepamo, da je $10 \cdot 3 = 2 \cdot |E|$, torej ima Petersenov graf $15$ povezav. Ta sklep velja za vsak $3$-regularen graf na $10$ vozliščih.

- Ali obstaja $3$-regularen graf na $9$ vozliščih? Če bi obstajal, potem bi po lemi o rokovanju veljalo $9 \cdot 3 = 2 \cdot |E|$, torej je $|E| = 27/2$, kar ni mogoče. Tak graf torej ne obstaja.

</div>

<div class="posledica">

Vsak graf ima sodo mnogo točk lihe stopnje.

</div>

<div class="dokaz">

Naj bo $G = (V,E)$ graf. Po lemi o rokovanju je $\sum_{v \in V} d(v)$ sodo število. Naj bo $V^0 = \{ v \in V \mid d(v) \text{ sodo} \}$ in $V^1 = \{ v \in V \mid d(v) \text{ liho} \}$. Torej je
```{math}
\sum_{v \in V^0} d(v) + \sum_{v \in V^1} d(v)
```
sodo število. Ker so v prvi vsoti vsi členi $d(v)$ sodi, mora biti druga vsota soda. Vsak člen v drugi vsoti pa je lih, zato mora biti velikost množice $V^1$ soda. S tem je dokaz zaključen.

</div>

Graf $H$ je <span class="definicija">podgraf</span> grafa $G$, če velja $V(H) \subseteq V(G)$ in $E(H) \subseteq E(G)$. V tem primeru pišemo $H \subseteq G$. Rečemo tudi, da graf $G$ <span class="definicija">vsebuje</span> graf $H$. Podgraf $H$ je <span class="definicija">vpet</span>, če velja $V(H) = V(G)$.

<div class="zgled">

Naj bo $G$ lizika z vozlišči $V(G) = \{ 1,2,3,4 \}$. Naj bo $H$ graf z vozlišči $V(H) = \{ 1,2,3,4 \}$ in povezavami $E(H) = \emptyset$. Tedaj je $H$ vpet podgraf grafa $G$.

</div>

## Standardni primeri in operacije

V tem razdelku si bomo ogledali nekaj standardnih primerov grafov in elementarne operacije, ki jih lahko izvajamo na njih, da dobimo nove grafe.

### Standardni primeri

Naj bo $n \in \NN$ in naj bo $\ZZ/n\ZZ$ kvocientna množica množice $\ZZ$ po relaciji $\mod{n}$. Elemente množice $\ZZ/n\ZZ$ lahko torej identificiramo z ostanki pri deljenju z $n$, se pravi s števili $0, 1, \dots, n-1$. Te ostanke lahko tudi seštevamo (po modulu $n$).[^3] S pomočjo množice $\ZZ/n\ZZ$ bomo definirali nekaj osnovnih primerov grafov.

- <span class="definicija">Poln graf</span> $K_n$ ima vozlišča in povezave
  ```{math}
  V = \ZZ/n\ZZ, \quad
      E = \{ \{ u,v \} \mid u,v \in \ZZ/n\ZZ, \ u \neq v \}.
  ```
  Ta graf ima $n$ vozlišč in $\binom{n}{2}$ povezav. Je $(n-1)$-regularen graf.

- <span class="definicija">Pot</span> $P_n$ ima vozlišča in povezave
  ```{math}
  V = \ZZ/n\ZZ, \quad
      E = \{ \{ u, u+1 \} \mid u \in \{ 0, 1, \dots, n-2 \}.
  ```
  Ta graf ima $n$ vozlišč in $n-1$ povezav. Rečemo, da je <span class="definicija">dolžina</span> poti $P_n$ enaka $n-1$.

- <span class="definicija">Cikel</span> $C_n$ (definiran le za $n \geq 3$) ima vozlišča in povezave
  ```{math}
  V = \ZZ/n\ZZ, \quad
      E = \{ \{ u, u+1 \} \mid u \in \ZZ/n\ZZ \}.
  ```
  Ta graf ima $n$ vozlišč in $n$ povezav. Je $2$-regularen graf.

Nekaj dodatnih primerov grafov bomo uvedli s pomočjo naslednje lastnosti grafov. Graf $G = (V,E)$ je <span class="definicija">dvodelen</span>, če lahko množico vozlišč $V$ zapišemo kot disjunktno unijo $V = A \cup B$, $A \cap B = \emptyset$, pri čemer mora za vsako povezavo v $E$ biti eno krajišče v $A$, drugo pa v $B$.[^4]

<div class="zgled">

- Poln graf $K_n$ ni dvodelen graf za $n \geq 3$.

- Pot $P_n$ je dvodelen graf za $n \geq 2$, saj lahko množico $\ZZ/n\ZZ$ zapišemo kot unijo sodih števil ($A$) in lihih števil ($B$) med $0$ in $n-1$, povezave v $P_n$ pa vedno tečejo le med sodimi in lihimi števili.

- Cikel $C_n$ je dvodelen graf, če je $n$ sodo število. V tem primeru lahko namreč uporabimo enak argument kot za pot $P_n$, saj lahko $\ZZ/n\ZZ$ razdelimo na soda in liha števila in vse povezave v $C_n$ tečejo le med sodimi in lihimi števili.

  Ta argument pa ne deluje, ko je $n$ liho število, saj takrat dobimo še dodatno povezavo med sodima številoma $0 \sim n-1$. Prepričajmo se, da cikel $C_n$ za $n$ lih *ni* dvodelen. Res, denimo, da je z razčlenitvijo vozlišč $V = A \cup B$. Brez škode lahko predpostavimo, da je $0 \in A$. Potem je nujno $1 \in B$ in za tem $2 \in A$ in za tem $3 \in B$ in tako dalje vse do $n-1 \in A$, saj je $n$ liho. Ker pa je $0 \sim n-1$ v ciklu $C_n$, dobimo povezavo dveh vozlišč v množici $A$, kar je sprto s predpostavko o dvodelnosti grafa. Lihi cikli torej niso dvodelni.

</div>

Ni se težko prepričati, da je obstoj lihih ciklov v grafu *edina* obstrukcija k dvodelnosti grafa.

<div class="trditev">

Graf je dvodelen natanko tedaj, ko ne vsebuje lihega cikla.

</div>

<div class="dokaz">

$(\Rightarrow)$: Naj bo $G$ dvodelen graf. Tedaj je vsak njegov podgraf tudi dvodelen. Ker lihi cikli niso dvodelni, jih $G$ ne more vsebovati.

$(\Leftarrow)$: Predpostavimo, da $G$ ne vsebuje lihega cikla. Naj bo $v \in V(G)$ poljubno začetno vozlišče. Za vozlišče $u \in V(G)$ naj bo $d(v,u)$ najmanjše število povezav, ki jih potrebujemo, da od vozlišča $v$ pridemo do vozlišča $u$.[^5] Vozlišča $u$, za katera je $d(v,u)$ sodo število, obarvamo z rdečo, vozlišča $u$, za katera je $d(v,u)$ liho število, pa obarvamo z modro.[^6] Naj bo $A$ množica vseh rdečih vozlišč, $B$ pa množica modrih vozlišč.

Predpostavimo, da je $\{ u, w \}$ povezava v $G$, za katero je $u, w \in B$.[^7] Torej sta $d(v,u)$ in $d(v,w)$ oba liha. V grafu $G$ lahko torej pridemo od vozlišča $v$ do $u$ po liho povezavah in prav tako od vozlišča $v$ do $w$ po liho povezavah. V grafu $G$ lahko torej začnemo pri vozlišču $v$ in po liho korakih pridemo do $u$, za tem prečkamo povezavo $uw$ in nato nadaljujemo od $w$ do $v$. Skupaj se sprehodimo po liho mnogo povezavah.[^8] Nekoliko kasneje bomo premislili, da ima vsak graf z obhodom lihe dolžine tudi lih cikel. Ker pa lihih ciklov v $G$ po predpostavki ni, smo dosegli protislovje s predpostavko, da v $G$ obstajajo povezave med vozlišči v množici $B$ oziroma v množici $A$. Takih povezav torej ni in graf $G$ je dvodelen.[^9]

</div>

- <span class="definicija">Poln dvodelni graf</span> $K_{m,n}$ ima vozlišča in povezave
  ```{math}
  V = A \cup B, |A| = m, |B|=n, A \cap B = \emptyset, \quad
      E = \{ \{ u,v\} \mid u \in A, v \in B \}.
  ```
  V tem grafu so torej vsa vozlišča množice $A$ povezana z vsemi vozlišči množice $B$. Ta graf ima $m+n$ vozlišč in $m \cdot n$ povezav.

- Grafom $K_{1,n}$ za $n \geq 3$ pravimo <span class="definicija">zvezde</span>.

- <span class="definicija">Kolo</span> $W_n$ (definiran le za $n \geq 3$) ima vozlišča in povezave
  ```{math}
  V = \ZZ/n\ZZ \cup \{ \infty \}, \quad
      E = \{ \{ u, u+1 \} \mid u \in \ZZ/n\ZZ \} \cup \{ \{ u, \infty \} \mid u \in \ZZ/n\ZZ \}.
  ```
  Ta graf ima $n+1$ vozlišč in $2n$ povezav.

### Operacije

Oglejmo si zdaj še nekaj osnovnih operacij, ki jih lahko izvedemo na danem grafu oziroma grafih.

- <span class="definicija">Odstranjevanje vozlišč</span>. Dan je graf $G = (V,E)$ in $u \in V$. Graf $G - u$ ima vozlišča in povezave
  ```{math}
  V(G - u) = V \backslash \{ u \}, \quad
          E(G - u) = \{ e \in E \mid u \notin e \}.
  ```

- <span class="definicija">Odstranjevanje povezav</span>. Dan je graf $G = (V,E)$ in $e \in E$. Graf $G - e$ ima vozlišča in povezave
  ```{math}
  V(G - e) = V, \quad
          E(G - e) = E \backslash \{ e \}.
  ```

- <span class="definicija">Komplementiran graf</span>. Dan je graf $G = (V,E)$. Graf $\bar G$ ima vozlišča in povezave
  ```{math}
  V(\bar G) = V, \quad
          E(\bar G) = \{ \{ u,v \} \mid u,v \in V, \{ u,v \} \notin E \}.
  ```

- <span class="definicija">Unija grafov</span>. Dana sta grafa $G_1, G_2$. Graf $G_1 \cup G_2$ ima vozlišča in povezave
  ```{math}
  V(G_1 \cup G_2) = V(G_1) \cup V(G_2), \quad 
          E(G_1 \cup G_2) = E(G_1) \cup E(G_2).
  ```

## Invariante grafov

Dana sta grafa $G_1, G_2$, ki sicer na prvi pogled izgledata drugače, a če ustrezno oštevilčimo vozlišča obeh grafov, potem vidimo, da povezave v obeh grafih potekajo med natanko istimi pari vozlišč. V tem primeru lahko *identificiramo* ta dva grafa. Natančneje, preslikava $h \colon V(G_1) \to V(G_2)$ je <span class="definicija">izomorfizem grafov</span>, če je $h$ bijekcija in velja
```{math}
\forall u,v \in V(G_1) \colon 
    \left( \{ u,v \} \in E(G_1) \Leftrightarrow \{ h(u), h(v) \} \in E(G_2) \right).
```
V tem primeru rečemo, da sta grafa $G_1$ in $G_2$ <span class="definicija">izomorfna</span> in pišemo $G_1 \cong G_2$. V posebnem primeru, ko je $G_1 = G_2$, izomorfizmu grafov $h$ pravimo <span class="definicija">avtomorfizem grafa</span> $G_1$.

<div class="zgled">

- Za vsak graf $G$ je preslikava
  ```{math}
  h \colon V(G) \to V(G), \quad 
              u \mapsto u
  ```
  avtomorfizem grafa $G$. Pravimo mu <span class="definicija">trivialni avtomorfizem</span>.

- Naj bo $G = C_n$ cikel dolžine $n$. Ta cikel lahko *zavrtimo* za $1$ v smeri urinega kazalca. Natančneje, definirajmo preslikavo
  ```{math}
  h \colon \ZZ/n\ZZ \to \ZZ/n\ZZ, \quad
              u \mapsto u + 1.
  ```
  Za vsaki vozlišči $u,v \in \ZZ/n\ZZ$ velja
  ```{math}
  \{ u,v \} \in E(C_n) \Leftrightarrow v = u \pm 1 \pmod{n}
  ```
  in
  ```{math}
  \{ h(u), h(v) \} \in E(C_n) \Leftrightarrow h(v) = h(u) \pm 1 \pmod{n}
              \Leftrightarrow v = u \pm 1 \pmod{n}.
  ```
  Preslikava $h$ je torej avtomorfizem grafa $C_n$.

- Naj bo $G_1 = C_6$ cikel dolžine $6$ in $G_2$ graf z vozlišči in povezavami
  ```{math}
  V(G_2) = \{ a,b,c,d,e,f \}, \quad
              E(G_2) = \{ ad, ae, bd, bf, ce, cf \}.
  ```
  Prepričajmo se, da sta grafa $G_1$ in $G_2$ izomorfna. Definirajmo preslikavo
  ```{math}
  h \colon V(G_1) \to V(G_2), \quad
              0 \mapsto d, 1 \mapsto a, 2 \mapsto e, 3 \mapsto c, 4 \mapsto f, 5 \mapsto b.
  ```
  Za vsaka $i,j \in V(G_1)$ velja $i \sim j$, če in samo če $h(i) \sim h(j)$. Preslikava $h$ je torej izomorfizem grafov.

</div>

Kako bi dokazali, da dana grafa *nista* izomorfna? V tem primeru ponavadi uporabimo kakšno lastnost grafov (na primer število povezav, dvodelnost), ki se pri izomorfizmu ohranja. Natančneje, naj bo $\mathcal{L}$ neka lastnost grafov. Rečemo, da je $\mathcal{L}$ <span class="definicija">invarianta grafa</span>, če za vsaka dva izomorfna grafa $G_1, G_2$ velja, da ima $G_1$ lastnost $\mathcal{L}$ natanko tedaj, ko ima $G_2$ lastnost $\mathcal{L}$.

<div class="zgled">

Invariante grafov so število točk, število povezav, dvodelnost, število točk stopnje $3$, število trikotnikov, …

</div>

Če želimo dokazati, da dana grafa nista izomorfna, lahko torej poiščemo kakšno invarianto, v kateri se obravnavana grafa razlikujeta.

<div class="zgled">

- Naj bo $L$ lizika in $C_4$ cikel. Lizika ima vozlišče stopnnje $3$, cikel pa je $2$-regularen. Ta dva grafa torej nista izomorfna.

- Dana sta naslednja grafa $G_1$ in $G_2$.

  <figure>
  <img src="img/grafi-zanimiv-zgled.png" />
  <figcaption>Graf <span class="math inline"><em>G</em><sub>1</sub></span></figcaption>
  </figure>

  <figure>
  <img src="img/grafi-primerjava.png" />
  <figcaption>Graf <span class="math inline"><em>G</em><sub>2</sub></span></figcaption>
  </figure>

  Ali sta $G_1$ in $G_2$ izomorfna? Ujemata se v številu vozlišč in številu povezav. Oba vsebujeta $5$-cikel, zato nista dvodelna. Oba sta kubična grafa. Noben od grafov ne vsebuje trikotnika. Ta dva grafa pa se razlikujeta v dolžini najkrajšnega cikla v grafu, ki ji pravimo <span class="definicija">ožina grafa</span>. Ožina je seveda invarianta grafov. Ožina grafa $G_1$ je $5$, ožina grafa $G_2$ pa je $4$. Ta dva grafa torej nista izomorfna.

</div>

Poglejmo si še nekaj invariant grafov, ki temeljijo na opazovanju *poti*. Naj bo $G = (V,E)$ graf.

- <span class="definicija">Sprehod</span> v $G$ je zaporedje
  ```{math}
  v_0 e_1 v_1 e_2 v_2 \cdots v_{k-1} e_k v_k,
  ```
  kjer je $v_i \in V$, $e_i = \{ v_{i-1}, v_i \} \in E$. Pri tem številu $k$ pravimo <span class="definicija">dolžina sprehoda</span>. Pogosto izpustimo podatke o povezavah in zapišemo le zaporedje vozlišč $v_0 v_1 v_2 \dots v_k$.

- <span class="definicija">Obhod</span> je sklenjen sprehod, se pravi $v_0 = v_k$.

- <span class="definicija">Enostaven sprehod</span> je sprehod, v katerem so vse *povezave* različne med sabo.

- <span class="definicija">Pot</span> je enostaven sprehod, v katerem so vsa *vozlišča* različna med sabo.

- <span class="definicija">Cikel</span> je enostaven obhod, v katerem so vozlišča $v_0, v_1, \dots, v_{k-1}$ različna med sabo.

<div class="zgled">

V naslednjem grafu je označen primer poti in primer cikla.

<figure>
<img src="img/grafi-pot-cikel.png" />
<figcaption>Graf z rdečo potjo in zelenim ciklom</figcaption>
</figure>

</div>

Ni vsak sprehod pot. Je pa povsod, kjer je sprehod, tudi pot.

<div class="trditev">

Če v grafu obstaja sprehod od $u$ do $v$, potem obstaja tudi pot od $u$ do $v$.

</div>

<div class="dokaz">

Dokazujemo z indukcijo na dolžino sprehoda $k$.

Baza indukcije je $k = 1$. V tem primeru je sprehod kar enak $P_2$, kar je pot.

Predpostavimo zdaj, da trditev že velja za vse sprehodi dolžine kvečjemu $k$. Naj bo $v_1 v_1 \dots v_{k+1}$ sprehod dolžine $k+1$. Po indukcijski predpostavki obstaja pot od $v_0$ do $v_k$, označimo jo z $v_0 u_1 u_2 \dots u_{k-1} v_k$.

- Če se $v_{k+1}$ ne pojavi na tej poti, potem je $v_0 u_1 u_2 \dots u_{k-1} v_k v_{k+1}$ pot od $v_0$ do $v_{k+1}$.

- Predpostavimo zdaj, da se $v_{k+1}$ pojavi na tej poti, se pravi $v_{k+1} = u_j$ za nek $1 \leq j \leq k-1$. Tedaj je $v_0 u_1 u_2 \dots u_j$ pot od $v_0$ do $v_{k+1}$.

</div>

<div class="domacanaloga">

Dokaži, da v vsakem grafu, v katerem obstaja sklenjen sprehod lihe dolžine, obstaja tudi cikel lihe dolžine. S tem v dokaz kriterija dvodelnosti grafov vstaviš še zadnji kos sestavljanke.

</div>

S pomočjo koncepta poti na množico vozlišč grafa vpeljemo naslednjo relacijo $R$. Za vozlišči $u,v$ grafa velja $u R v$, če in samo če v grafu obstaja pot od $u$ do $v$. Lahko je preveriti, da je $R$ ekvivalenčna relacija.[^10] Ekvivalenčne razrede $V/R$ imenujemo <span class="definicija">povezane komponente</span> grafa. Število povezanih komponent označimo z $\Omega(G)$. Če je $\Omega(G) = 1$, potem rečemo, da je graf <span class="definicija">povezan</span>. Število povezanih komponent je invariatna grafov.

<div class="zgled">

Lizika je povezan graf. Če liziki odstranimo vozlišče stopnje $3$, dobimo graf, ki je disjunktna unija grafov $P_2$ in izolirane točke. Ta graf ni povezan, ima dve povezani komponenti.

</div>

<span class="definicija">Razdalja</span> med vozliščema $u,v$, ki jo označimo kot $d(u,v)$, je dolžina najkrajše poti med vozliščema $u$ in $v$, če je le $u R v$. V primeru, ko $u$ in $v$ nista v relaciji $R$, definiramo $d(u,v) = \infty$.

<div class="zgled">

V naslednjem grafu za vozlišči $u,v$ na zunanjem ciklu velja $d(u,v)=2$.

<figure>
<img src="img/grafi-razdalja.png" />
<figcaption>Razdalja med vozliščema</figcaption>
</figure>

</div>

<span class="definicija">Premer</span> grafa je
```{math}
\mathrm{diam}(G) = \max_{u,v \in G} d(u,v),
```
se pravi največja možna razdalja med vsakim parom vozlišč. Premer je invarianta grafov.

<div class="domacanaloga">

Prepričaj se, da je premer grafa iz zadnjega zgleda enak $2$. Določi še premer Petersenovega grafa.

</div>

## Drevesa

Grafu, ki ne vsebuje ciklov, pravimo <span class="definicija">gozd</span>. Povezanemu gozdu pravimo <span class="definicija">drevo</span>.

<div class="zgled">

Drevo je povezan graf brez ciklov. Njegova vozlišča stopnje $1$ so listi.

<figure>
<img src="img/grafi-drevo.png" />
<figcaption>Drevo</figcaption>
</figure>

</div>

Ker drevesa nimajo ciklov, so dvodelna. Imajo pa drevesa še veliko drugih čudovitih lastnosti.

<div class="trditev">

Naj bo $T$ drevo.

1.  Če je $|V(T)| > 1$, potem ima $T$ vsaj $2$ lista.

2.  $|E(T)| = |V(T)| - 1$.

3.  Za vsaka $u,v \in V(T)$ obstaja *natanko ena* pot od $u$ do $v$.

</div>

<div class="dokaz">

1\. Naj bo $P$ pot *nadaljše možne dolžine* v drevesu $T$. Naj bo $u$ začetek in $v$ konec poti $P$. Trdimo, da je $d(u) = d(v) = 1$. Uporabimo dokaz s protislovjem. Naj bo $w$ predzadnje vozlišče na poti $P$. Predpostavimo, da velja $d(v) \geq 2$. Torej obstaja vozlišče $x \in V$, $x \neq w$, $x \sim v$. Ker v grafu $T$ ni ciklov, vozlišče $x$ ni na poti $P$. Zato lahko pot $P$ podaljšamo s povezavo $v \sim x$. To je protislovje z izbiro najdaljše možne poti $P$. Torej je res $d(v) = 1$. Podobno dokažemo $d(u) = 1$. Vozlišči $u$ in $v$ sta torej lista drevesa.

2\. Dokazujemo z indukcijo na $n = |V(T)|$. Baza je primer $n = 1$, ko drevo $T$ sestoji iz enega samega vozlišča in nima nič povezav. V tem primeru formula $0 = 1 - 1$ seveda drži. Za indukcijski korak predpostavimo, da formula drži za vsako drevo na $n$ vozliščih in naj bo $T$ drevo na $n+1$ vozliščih. Naj bo $v$ list $T$, ki obstaja po prejšnji točki. Naj bo $T' = T - v$. Tedaj je graf $T'$ brez ciklov in povezan,[^11] torej je $T'$ drevo z $n$ vozlišči. Po indukcijski predpostavki sledi $|E(T')| = n - 1$. Hkrati velja $|E(T)| = |E(T')| + 1$, torej ima drevo $T$ natanko $n$ povezav in formula velja.

3\. Predpostavimo, da obstajata različni poti od nekega vozlišča $u$ do nekega vozlišča $v$, recimo jima $P_1, P_2$. Naj bo $w$ zadnje vozlišče, v katerem se $P_1, P_2$ še ujemata. Naj bo $x$ prvo vozlišče na $P_1$ po $w$, ki je hkrati na $P_2$. Tedaj dobimo cikel $wP_1xP_2w$. To je protislovje, ker je $T$ drevo.

</div>

Drevesa zelo preprosto postanejo nepovezana. Povezava $e$ v povezanem grafu $G$ je <span class="definicija">most</span>, če graf $G - e$ *ni* povezan. Vsaka povezava, ki povezuje list s preostankom drevesa, je most. Res pa je še več.

<div class="trditev">

Vsaka povezava v drevesu je most.

</div>

<div class="dokaz">

Naj bo $T$ drevo. Naj bo $e = \{ u, v \}$ poljubna povezava v $T$. Po zadnji trditvi je ta povezava *edina* pot od $u$ do $v$ v drevesu $T$. Torej v grafu $T - e$ *ne* obstaja pot od $u$ do $v$. To pomeni, da graf $T - e$ ni povezan. Povezava $e$ je torej most.

</div>

Vse te čudovite lastnosti, ki jih imajo drevesa, v resnici *karakterizirajo* drevesa.

<div class="trditev">

Naj bo $G$ graf. Naslednje trditve so ekvivalentne.

1.  $G$ je drevo.

2.  Med vsakima dvema vozliščema v $G$ obstaja natanko ena pot.

3.  $G$ je povezan in $|E(G)| = |V(G)| - 1$.

4.  $G$ je povezan in vsaka njegova povezava je most.

</div>

<div class="dokaz">

Po predzadnji trditvi vemo, da 1. $\Rightarrow$ 2. in 1. $\Rightarrow$ 3. Po zadnji trditvi vemo, da celo 2. $\Rightarrow$ 4.[^12] Dokažimo zdaj še 4. $\Rightarrow$ 1. in 3. $\Rightarrow$ 1.

4\. $\Rightarrow$ 1.: Predpostavimo, da $G$ ni drevo in da v $G$ torej obstaja cikel $C$. Naj bo $e$ povezava na $C$. Tedaj po predpostavki graf $G - e$ *ni* povezan. Naj bosta $x,y$ vozlišči grafa $G$, ki nista povezani v $G - e$. Ker je graf $G$ povezan, obstaja pot $P$ od $x$ do $y$ v $G$. Ta pot nujno prečka povezavo $e$. Nadomestimo to prečkanje povezave $e$ s potjo $C - e$. Torej v grafu $G - e$ obstaja sprehod od $x$ do $y$, zato pa tudi pot. To je protislovje z izbiro vozlišč $x,y$. Torej cikel $C$ v $G$ ne obstaja in $G$ je res drevo.

3\. $\Rightarrow$ 1.: Predpostavimo, da $G$ ni drevo in da v $G$ torej obstaja cikel $C$. Za vsako vozlišče $v \in V(G) \backslash V(C)$ izberimo pot $P_v$ najkrajše možne dolžine od $v$ do cikla $C$. Naj bo $e_v$ prva povezava na poti $P_v$. Trdimo, da za $u \neq v$ velja $e_u \neq e_v$. Res, če je $e_u = e_v$, potem sta $u$ in $v$ nujno povezani vozlišči vozlišče $u$ je povezano s ciklom $C$ s potjo $P_v - e$. Torej je dolžina poti $P_u$, ki je najkrajše možne dolžine, enaka kvečjemu dolžini poti $P_v$ manj $1$. Od tod sledi, da je dolžina poti $P_u - e$ strogo manjša od dolžine poti $P_v$. Torej smo našli pot, ki povezuje $u$ s $C$ in je krajše dolžine kot $P_v$. To je protislovje. Res torej za $u \neq v$ velja $e_u \neq e_v$. Od tod sledi
```{math}
|E(G)| \geq |E(C)| + |\{ e_v \mid v \in V(G) \backslash V(C) \}|
    = |V(C)| + (|V(G)| - |V(C)|)
    = |V(G)|.
```
Dobljeno je sprto s predpostavko $|E(G)| = |V(G)| - 1$. Cikel $C$ v $G$ torej ne obstaja in $G$ je res drevo.

</div>

## Eulerjevi grafi

Sprehod v grafu je <span class="definicija">Eulerjev sprehod</span>, če vsebuje *vsako povezavo* grafa natanko enkrat. <span class="definicija">Eulerjev obhod</span> je obhod, ki je Eulerjev sprehod.

<div class="zgled">

Lizika vsebuje Eulerjev sprehod, cikel $C_5$ vsebuje Eulerjev obhod, poln graf $K_5$ vsebuje Eulerjev obhod.

</div>

Graf je <span class="definicija">Eulerjev</span>, če vsebuje Eulerjev obhod. Za to, da je graf Eulerjev, morata biti izpolnjena naslednja dva pogoja:

- graf je povezan,

- vsa vozlišča so sode stopnje.[^13]

Presenetljivo pa sta ta dva očitna potrebna pogoja tudi zadostna.

<div class="izrek">

Naj bo $G$ povezan graf. Potem je $G$ Eulerjev natanko tedaj, ko so vsa vozlišča sode stopnje.

</div>

<div class="dokaz">

Dokazujemo le implikacijo iz desne v levo. Naj bo $S$ sprehod najdaljše možne dolžine v $G$, ki vsebuje vsako povezavo v $G$ *kvečjemu enkrat*. Naj bo $u$ začetno vozlišče $S$ in $v$ končno vozlišče. Za vsakega soseda $w \sim u$ mora biti tudi povezava $\{ u, w \}$ na $S$, sicer lahko $S$ podaljšamo. Ker je $u$ sode stopnje in se sprehod $S$ začne v $u$, se mora tudi končati v $u$.[^14] Torej je $u = v$ in sprehod $S$ je v resnici *obhod*.

Premislimo, da je ta obhod Eulerjev. Res, če ni, potem izberimo neko povezavo $e = \{ x, y \}$, ki ni na $S$. Naj bo $Q$ neka najkrajša pot od $y$ do sprehoda $S$.[^15], zapišimo $Q = y \cdots z$ za vozlišče $z$ na obhodu $S$. Ker je $Q$ najkrajša, nobeno od njegovih vozlišč razen $z$ ne leži na $S$. Potemtakem je sprehod $xy \cdots z \cdots z$, kjer se najprej sprehodimo od $x$ do $y$ prek $e$, potem od $y$ do $z$ prek $Q$ in nazadnje od $z$ do $z$ prek $S$, daljši od $S$ in vsako povezavo vsebuje kvečjemu enkrat. To je protislovje z izbiro $S$.

</div>

Soroden kriterij imamo na voljo tudi za Eulerjeve sprehode.

<div class="izrek">

Naj bo $G$ povezan graf. Potem ima $G$ Eulerjev sprehod natanko tedaj, ko ima največ $2$ vozlišči lihe stopnje.

</div>

<div class="dokaz">

$(\Rightarrow)$: Vsa vozlišča razen morda začetnega in končnega imajo sodo stopnjo, ker za vsako vhodno povezavo obstaja izhodna.

$(\Leftarrow)$: Število vozlišč lihe stopnje je sodo po lemi o rokovanju, torej je lahko enako le $0$ ali $2$.

- Če je enako $0$, potem so vsa vozlišča sode stopnje, zato obstaja celo Eulerjev obhod.

- Če je enako $2$, potem vozlišči lihe stopnje označimo z $u,v$. Dodajmo povezavo $\{ u, v \}$ grafu $G$. Nov graf $G + uv$ ima vsa vozlišča sode stopnje, torej ima Eulerjev obhod $S$. Tedaj je $S - uv$ Eulerjev sprehod v grafu $G$.

</div>

### Mostovi

Eulerjeva izvirna motivacija za študiranje obhodov v grafih, ki jim danes pravimo Eulerjevi obhodi, je bil <span class="definicija">problem königsberških mostov</span>. Ta vprašuje, ali se je v takratnem mestu Königsberg[^16] bilo mogoče sprehoditi po mestu na tak način, da bi začeli in končali sprehod na isti točki, pri tem pa bi se po vsakem od mostov mesta sprehodili natanko enkrat.[^17]

<figure>
<img src="img/konigsberg.png" />
<figcaption>Mostovi v Königsbergu, vir: Wikipedia</figcaption>
</figure>

Ta problem lahko prevedemo na teorijo grafo na naslednji način. Vsaki zemeljski masi priredimo vozlišče, mostu pa povezavo. Dobimo multigraf s štirimi vozlišči, eno je stopnje $5$, tri pa so stopnje $3$. Po dokazanih izrekih[^18] o obstoju Eulerjeve poti oziroma obhoda sklepamo, da v tem grafu ne obstaja niti Eulerjev sprehod. Želen obhod v mestu torej ni mogoč.

<figure>
<img src="img/grafi-konigsberg.png" />
<figcaption>Graf königsberških mostov</figcaption>
</figure>

Sorodno lahko obravnavamo <span class="definicija">problem ljubljanskih mostov</span>. Ljubljana ima sicer bistveno več mostov kot stari Königsberg, zato se osredotočimo le na centralni del mesta, ki ga severno od gradu omejuje Ljubljanica, južno pa Gruberjev prekop.

<figure>
<img src="img/ljubljana.png" />
<figcaption>Ljubljanski mostovi, vir: OpenStreetMap</figcaption>
</figure>

Imamo torej tri zemeljske mase: severo-zahodno (vključuje FMF), osrednjo (vključuje grad) in južno (vključuje Golovec). Prva je z drugo povezana z $18$ mostovi, druga pa s tretjo z $9$ mostovi. Dobimo torej multigraf s tremi vozlišči stopnje $18$, $27$ in $9$. Po izreku v centralni Ljubljani Eulerjev obhod ne obstaja, obstaja pa Eulerjev sprehod. Pri tem moramo v slednjem začeti in končati sprehod v vozliščih lihe stopnje, torej v posebnem ne na FMF.

### Risanje grafa v eni potezi

Dan je graf. Ali ga lahko narišemo v eni potezi? Se pravi, ali lahko na list papirja narišemo graf tako, da vzamemo v roke pisalo, se z njim dotaknemo papirja, neprekinjeno rišemo povezave grafa (brez da bi večkrat potegnili pisalo čez isto povezavo) in na ta način narišemo vse povezave grafa?

Ta problem je enakovreden temu, da v grafu najdemo Eulerjev sprehod, ki ga lahko neprekinjeno narišemo. Če graf nima Eulerjevega sprehoda, ga torej v eni potezi ne moremo narisati.

<div class="zgled">

Oglejmo si naslednji graf.

<figure>
<img src="img/grafi-enapoteza.png" />
<figcaption>Risanje grafa s čim manj potezami</figcaption>
</figure>

Ta graf je kubičen, zato nima Eulerjevega obhoda in ga ne moremo narisati v eni potezi. Kolikšno je najmanjše število potez, ki zadoščajo, da narišemo ta graf? Na sliki je prikazano, kako ta graf lahko narišemo s $4$ potezami. Vsaka poteza je prikazana s svojo barvo. Prepričajmo se, da pa tega grafa ne moremo narisati z manj kot $4$ potezami. To lahko vidimo tako, da seštejemo stopnje vseh vozlišč v grafu. Po lemi o rokovanju je ta vsota soda. Po drugi strani ima vsaka poteza svoje začetno in končno vozlišče (morda sta to enaki vozlišči), torej skupno prispeva k vsoti stopenj $2$ za vozlišča na sprehodu in $1$ za začetno in končno vozlišče. Graf, narisan v $3$ potezah, bi zato imel kvečjemu $6$ vozlišč lihe stopnje. Obravnavan graf pa ima $8$ vozlišč stopnje $3$.

</div>

Zadnji zgled lahko posplošimo na naslednji način.

<div class="trditev">

Naj bo $G$ povezan graf z $\ell$ vozlišči lihe stopnje. Najmanjše število potez, s katerimi lahko narišemo $G$, je $1$ za $\ell = 0$ in $\ell/2$ za $\ell > 0$.

</div>

<div class="dokaz">

Po lemi o rokovanju je $\ell$ sodo število. Če je $\ell = 0$, po izreku obstaja Eulerjev obhod, torej lahko graf narišemo v eni potezi. Če pa je $\ell > 0$, potem po argumentu v zadnjem zgledu gotovo potrebujemo vsaj $\ell/2$ potez, da narišemo graf $G$. Prepričajmo se, da $\ell/2$ potez tudi zadostuje. Res, naj bodo $u_1, u_2, \dots, u_{\ell/2}$ ter $v_1, v_2, \dots, v_{\ell/2}$ vozlišča lihe stopnje v $G$. Tedaj graf $G + u_1 v_1 + u_2 v_2 + \cdots u_{\ell/2} v_{\ell/2}$ nima vozlišč lihe stopnje, torej ima Eulerjev obhod
```{math}
S = u_1 v_1 \cdots u_2 v_2 \cdots u_{\ell/2} v_{\ell/2} \cdots u_1.
```
To pomeni, da lahko graf $G$ narišemo v $\ell/2$ potezah, in sicer v 1. potezi narišemo del $S$ od $v_1$ do $u_2$, v 2. potezi narišemo del $S$ od $u_2$ do $v_2$, …, v $\ell/2$-ti potezi narišemo del $S$ od $v_{\ell/2}$ do $u_1$.

</div>

## Hamiltonovi grafi

Hamiltonovi grafi so analogni Eulerjevim, kjer le zamenjamo vlogo povezav in vozlišč. Vpeta pot v grafu je <span class="definicija">Hamiltonova pot</span>. Vpeti cikel v grafu je <span class="definicija">Hamiltonov cikel</span>.

<div class="zgled">

- Lizika vsebuje Hamiltonovo pot, poln graf $K_4$ vsebuje Hamiltonov cikel.

- Naslednji grafi vsebujejo Hamiltonove cikle, ki so označeni z rdečo barvo.

  <figure>
  <img src="img/grafi-hamilton.png" />
  <figcaption>Grafi s Hamiltonovim ciklom</figcaption>
  </figure>

- Ali naslednji graf vsebuje Hamiltonov cikel?

  <figure>
  <img src="img/grafi-hamilton-zgled.png" />
  <figcaption>Ali ta graf vsebuje Hamiltonov cikel?</figcaption>
  </figure>

</div>

Graf je <span class="definicija">Hamiltonov</span>, če vsebuje Hamiltonov cikel.

V prejšnjem razdelku smo spoznali, da lahko za poljuben graf zelo hitro ugotovimo, ali je Eulerjev. Za ugotavljanje hamiltonskosti grafa pa ni znan noben preprost postopek, ki bi bil uporaben za vse grafe. Preverjanje hamiltonskosti je običajno bistveno težji problem od preverjanja, ali je graf Eulerjev.[^19] Poznanih pa je nekaj *potrebnih* pogojev in nekaj *zadostnih* pogojev za hamiltonskost.

<div class="izrek">

Naj bo $G$ graf. Predpostavimo, da v $G$ obstaja neprazna podmnožica $S \subseteq V(G)$, za katero velja $\Omega(G-S) > |S|$. Tedaj graf $G$ *ni* Hamiltonov.

</div>

<div class="dokaz">

Predpostavimo, da je $G$ Hamiltonov graf s Hamiltonovim ciklom $C$. Naj bo $S$ neka neprazna množica vozlišč grafa $G$. Ko odstranimo vozlišča $S$ s cikla $C$, ta cikel razpade na kvečjemu $|S|$ komponent (krožnih lokov). Ti loki so prek povezav grafa $G$, ki ne ležijo na ciklu $C$, lahko morda še povezani med sabo. Graf $G - S$ ima zatorej kvečjemu $|S|$ komponent in velja torej $\Omega(G - S) \leq |S|$. S tem je dokaz zaključen.

</div>

<div class="zgled">

Ko liziki odstranimo vozlišče stopnje $3$, razpade na dve komponenti. Lizika torej ni Hamiltonov graf.

</div>

Zabeležimo poseben primer dokazanega izreka za dvodelne grafe.

<div class="posledica">

Naj bo $G$ dvodelen graf z $V(G) = A \cup B$, $A \cap B = \emptyset$, pri čemer ima vsaka povezava v $E(G)$ eno krajišče v $A$, drugo pa v $B$. Če je $|A| \neq |B|$, potem $G$ *ni* Hamiltonov.

</div>

<div class="dokaz">

Brez škode za splošnost lahko predpostavimo, da velja $|A| < |B|$. Vzemimo $S = A$. Ko v grafu $G$ odstranimo vozlišča $A$, nam ostane graf z vozlišči $B$ in brez povezav. Velja torej $\Omega(G-A) = |B| > |A|$. Po izreku graf $G$ zato ni Hamiltonov.

</div>

<div class="zgled">

Vrnimo se k zadnjemu zgledu iz začetka tega razdelka. Obravnavani graf je dvodelen z biparticijo vozlišč $A \cup B$, pri čemer je $|A| = 5$ in $|B| = 6$. Po posledici ta graf zato ni Hamiltonov.

<figure>
<img src="img/grafi-hamilton-zgled-dvodelen.png" />
<figcaption>Dvodelen graf, ki ni Hamiltonov</figcaption>
</figure>

</div>

Analogen potreben pogoj lahko izpeljemo za obstoj Hamiltonove poti.

<div class="izrek">

Naj bo $G$ graf. Predpostavimo, da v $G$ obstaja neprazna podmnožica $S \subseteq V(G)$, za katero velja $\Omega(G-S) > |S| + 1$. Tedaj graf $G$ *nima* Hamiltonove poti.

</div>

<div class="dokaz">

Predpostavimo, da ima $G$ Hamiltonovo pot $P$. Naj bo $S$ neka neprazna množica vozlišč grafa $G$. Ko odstranimo vozlišča $S$ s poti $P$, ta pot razpade na kvečjemu $|S|+1$ komponent (delov poti). Ti deli so prek povezav grafa $G$, ki ne ležijo na poti $P$, lahko morda še povezani med sabo. Graf $G - S$ ima zatorej kvečjemu $|S| + 1$ komponent in velja torej $\Omega(G - S) \leq |S| + 1$. S tem je dokaz zaključen.

</div>

<div class="zgled">

Dvodelen graf iz zadnjega zgleda ni Hamiltonov, saj z odstranitvijo $5$ točk graf razpade na $6$ komponent. Iz tega argumenta pa še ne sledi, da ta graf nima Hamiltonove poti, saj bi za to moral razpasti na vsaj $7$ komponent. V resnici ta graf ima Hamiltonovo pot, kot je prikazano na naslednji sliki.

<figure>
<img src="img/grafi-hamilton-zgled-pot.png" />
<figcaption>Hamiltonova pot v grafu</figcaption>
</figure>

</div>

Zdaj si bomo pogledali še nekaj zadostnih pogojev za hamiltonskost. Naslonili jih bomo na naslednjo lemo.

<div class="lema">

Naj za vozlišči $u,v$ grafa $G$ velja $u \neq v$, $u \not\sim v$, $d(u) + d(v) \geq |V(G)|$. Tedaj je $G$ Hamiltonov, če in samo če je $G + uv$ Hamiltonov.

</div>

<div class="dokaz">

$(\Rightarrow)$: Če je graf $G$ Hamiltonov s Hamiltonovim ciklom $C$, potem je isti cikel $C$ tudi Hamiltonov cikel v grafu $G + uv$.

$(\Leftarrow)$: Naj bo $C$ Hamiltonov cikel v grafu $G + uv$. Privzemimo, da $G$ ni Hamiltonov graf. Torej je povezava $uv$ nujno na ciklu $C$. Graf $G$ zato vsebuje Hamiltonovo pot $C - uv = v_1 v_2 \dots v_n$ z začetkom v $u = v_1$ in koncem v $v = v_n$, pri čemer je $n = |V(G)|$.

Opazujmo sosede vozlišča $u$. Recimo, da za nek $i < n$ velja $u \sim v_{i+1}$. Premislimo, da tedaj vozlišče $v$ ni povezano z neposrednim predhodnikom vozlišča $v_{i+1}$, to je $v_i$. Res, če je $v \sim v_i$, potem v $G$ najdemo Hamiltonov cikel $v_1 \dots v_i v_n \dots v_{i+1} v_1$, ki pa po predpostavki ne obstaja.

Noben od $d(u)$ neposrednih predhodnikov sosedov $u$ torej ni sosed $v$. To pomeni, da je število sosedov $v$ enako kvečjemu $n - 1 - d(u)$, kjer smo upoštevali še, da vozlišče $v$ ni povezano samo s sabo. Od tod sledi $d(v) \leq n - 1 - d(u)$, kar je enakovredno $d(u) + d(v) \leq n -1$. To je sprto s predpostavko $d(u) + d(v) \geq n = |V(G)|$. Graf $G$ je nazadnje torej res Hamiltonov.

</div>

<div class="izrek">

Naj bo $G$ graf z $|V(G)| \geq 3$. Če za vsaki dve vozlišči $u,v \in V(G)$ z lastnostjo $u \neq v$, $u \not\sim v$ velja $d(u) + d(v) \geq |V(G)|$, potem je $G$ Hamiltonov.

</div>

<div class="dokaz">

Grafu $G$ dodajamo povezave, dokler ne dobimo polnega grafa $K_n$. Po lemi je graf $G$ Hamiltonov, če in samo če je $K_n$ Hamiltonov, kar pa je res (za $\geq 3$).

</div>

<div class="zgled">

Za vsaki različni nepovezani vozlišči v naslednjem grafu velja $d(u) + d(v) \geq 7$. Po Orejevem izreku je graf Hamiltonov. Poišči Hamiltonov cikel v njem!

<figure>
<img src="img/grafi-hamilton-ore.png" />
<figcaption>Hamiltonov graf po Orejevem izreku</figcaption>
</figure>

</div>

<div class="izrek">

Naj bo $G$ graf z $|V(G)| \geq 3$. Če je $\delta(G) \geq |V(G)|/2$, potem je $G$ Hamiltonov.

</div>

<div class="dokaz">

Po predpostavki za vsaki vozlišči $u,v \in V(G)$ velja $d(u) + d(v) \geq |V(G)|$. Po Orejevem izreku je graf $G$ zato Hamiltonov.

</div>

<div class="zgled">

Najmanjša stopnja vozlišča v naslednjem grafu je $3$, število vozlišč pa je $6$. Po Diracovem izreku je graf Hamiltonov. Poišči Hamiltonov cikel v njem!

<figure>
<img src="img/grafi-hamilton-dirac.png" />
<figcaption>Hamiltonov graf po Diracovem izreku</figcaption>
</figure>

</div>

Včasih se znajdemo v situaciji, ko nam ob danem grafu niti potrebni niti zadostni pogoji ne odgovorijo na vprašanje, ali je graf Hamiltonov. V tem primeru posežemo po bolj ad hoc tehnikah, kot je prikazano v naslednjem zgledu.

<div class="zgled">

Ali je Petersenov graf Hamiltonov? Na naslednji sliki je prikazana Hamiltonova pot.

<figure>
<img src="img/grafi-petersen-hamilton-pot.png" />
<figcaption>Hamiltonova pot v Petersenovem grafu</figcaption>
</figure>

S protislovjem premislimo, da Hamiltonov cikel ne obstaja. Če bi namreč $C$ bil Hamiltonov cikel, potem bi vseboval $10$ vozlišč Petersenovega grafa in $10$ povezav. Označimo vozlišča na $C$ z $v_1v_2 \dots v_{10}$. Ker ima Petersenov graf $15$ povezav, iščemo torej še $5$ dodatnih tetivnih povezav, ki jih dodamo ciklu $C$, da dobimo Petersenov graf. Vemo, da je Petersenov graf $3$-regularen, zato moramo po eno tako tetivno povezavo dodati vsakemu vozlišči na ciklu $C$. Vemo, da Petersenov graf nima $3$-ciklov in nima $4$-ciklov, hkrati pa ima $5$-cikel. Gotovo torej obstaja vozlišče na $C$, brez škode je to kar $v_1$, ki ima tetivno povezavo do soseda antipodnega vozlišča $v_6$, brez škode je to kar $v_5$. Opazujmo zdaj vozlišče $v_6$. Tudi to vozlišče mora imeti tetivno povezavo do nekega vozlišča na $C$. Ker pa Petersenov graf nima $3$-ciklov in nima $4$-ciklov, taka tetivna povezava ne obstaja. To je protislovje z obstojem Hamiltonovega cikla v Petersenovem grafu.

</div>

### Šahovski konjiček

Opazujmo gibanje šahovskega konjička na šahovnici dimenzij $m \times n$. Ali lahko konjiček z zaporedjem skokov obišče vsako polje šahovnice natanko enkrat in zaključi na začetnem polju? To je problem <span class="definicija">požrešnega šahovskega konjička</span>.

Polja šahovnice si lahko predstavljamo kot vozlišča grafa, možnost skoka konjička iz enega polja na drugega pa predstavimo s povezavo. V tem smislu je problem požrešnega šahovskega konjička enakovreden obstoju Hamiltonovega cikla v tem grafu.

<figure>
<img src="img/grafi-konjicek-graf.png" />
<figcaption>Graf, ki prikazuje možne skoke konjička na šahovski plošči <span class="math inline">8 × 8</span>; v vozliščih so vpisane stopnje, vir: Wikipedia</figcaption>
</figure>

Poglejmo si nekaj posebnih primerov.

<div class="zgled">

- Obravnavajmo šahovnico dimenzij $3 \times 3$. Če konjiček začne v centralnem polju, potem nima kam skočiti, saj je plošča premajhna. Centralno vozlišče prirejenega grafa je torej izolirana točka in graf ni povezan, zato seveda tudi nima Hamiltonovega cikla.

- Obravnavajmo šahovnico dimenzij $5 \times 5$. Dobimo graf na $25$ vozliščih. Če obarvamo vozlišča s črno in belo barvo kot na šahovnici, potem je zaradi dejstva, da konjiček vedno skoči s črnega polja na belo oziroma obratno, prirejeni graf *dvodelen*. Ker ima šahovnica $25$ vozlišč, je število belih vozlišč različno od števila črnih vozlišč. Po izreku ta graf torej ni Hamiltonov. Enak argument deluje za vse šahovnice z lihim številom polj.

</div>

<div class="domacanaloga">

Obravnavaj šahovnico dimenzije $4 \times n$ za $n \geq 4$. Dokaži, da Hamiltonov cikel *ne* obstaja.[^20]

</div>

Izkaže se, da sta po eni strani lihost števila polj in po drugi strani premajhno število vrstic oziroma stolpcev šahovnice *edini* oviri za obstoj Hamiltonovega cikla, a tega ne bomo dokazali.

<div class="izrek">

Konjičkov obhod na šahovnici $m \times n$ obstaja, če je le $m \cdot n$ sodo število in $m, n > 4$.

</div>

V posebnem torej obstaja obhod na standardni šahovnici $8 \times 8$.

<figure>
<img src="img/grafi-konjicek.png" />
<figcaption>Konjičkov obhod na šahovnici <span class="math inline">8 × 8</span>, vir: Wikipedia</figcaption>
</figure>

## Ravninski grafi

Obravnavajmo naslednji izziv, ki je na prvi pogled osnovnošolska naloga. Pred nami so $3$ hiše in $3$ drevesa. S potjo je potrebno povezati vsako hišo z vsakim drevesom, ne da bi se pri tem poti sekale med sabo. Če si vsako hišo oziroma drevo predstavljamo kot vozlišče, pot pa kot povezavo, potem pravzaprav vprašujemo, če lahko graf $K_{3,3}$ narišemo v ravnino tako, da se nobeni dve povezavi med sabo ne sekata (razen v vozliščih). Splošneje se lahko torej vprašamo, ali lahko poljuben graf narišemo v ravnini brez križanja povezav.

<div class="zgled">

Nekatere grafe gotovo lahko narišemo v ravnini brez križanja povezav, na primer liziko, cikle, drevesa. Tudi poln graf $K_4$ lahko narišemo na ta način, kot je prikazano na sliki.

<figure>
<img src="img/grafi-ravninski-k4.png" />
<figcaption>Ravninski graf <span class="math inline"><em>K</em><sub>4</sub></span></figcaption>
</figure>

</div>

Po nekaj poskusih se zdi, da grafa $K_{3,3}$ ne moremo narisati na želeni način v ravnini. Kako bi dokazali, da je to res nemogoče? Preden lahko odgovorimo na to vprašanje, moramo najprej matematično bolj natančno formulirati problem.

<span class="definicija">Vložitev grafa $G$ v ravnino</span> je injektivna preslikava $\phi \colon V(G) \to \RR^2$ skupaj z družino zveznih preslikav $\phi_e \colon [0,1] \to \RR^2$ za vsako povezavo $e \in E(G)$, da velja:

1.  če je $e = \{ u,v \} \in E(G)$, potem je $\{ \phi_e(0), \phi_e(1) \} = \{ \phi(u), \phi(v) \}$,[^21]

2.  za vsak $e \in E(G)$ je $\phi_e|_{(0,1)}$ injektivna,[^22]

3.  za vsaka $e, e' \in E(G)$, $e \neq e'$, velja $\mathrm{im} \phi_e|_{(0,1)} \cap \mathrm{im} \phi_{e'}|_{(0,1)} = \emptyset$,[^23]

4.  za vsak $e \in E(G)$ velja $\mathrm{im} \phi_e|_{(0,1)} \cap \mathrm{im} \phi = \emptyset$.[^24]

Vse podatke o vložitvi grafa v ravnino zberemo v par $(\phi, \{ \phi_e \}_{e \in E(G)})$, ki ga krajše označimo kot $\GG$.[^25]

Graf $G$ je <span class="definicija">ravninski</span>, če ima kakšno vložitev v ravnino. Pri tem seveda lahko obstajajo različne vložitve.

<div class="zgled">

Disjunktno unijo $K_3 \cup K_3$ lahko narišemo v ravnino na dva vsaj načina, in sicer lahko en trikotnik narišemo znotraj drugega ali pa dva trikotnika narišemo enega ob drugem.

<figure>
<img src="img/grafi-ravninski-k3k3.png" style="width:50.0%" />
<figcaption>Dve različni vložitvi grafa <span class="math inline"><em>K</em><sub>3</sub> ∪ <em>K</em><sub>3</sub></span> v ravnino</figcaption>
</figure>

</div>

Vložitev grafa razdeli ravnino na povezane dele, ki jim pravimo <span class="definicija">lica</span> vložitve. Vselej je natanko eno lice neomejeno – imenujemo ga <span class="definicija">zunanje lice</span>.

<div class="zgled">

- Vsaka ravninska vložitev drevesa ima eno samo lice, saj graf nima nobenih ciklov.

- Obe vložitvi grafa $K_3 \cup K_3$ iz zadnjega zgleda imata $3$ lica.

  <figure>
  <img src="img/grafi-ravninski-k3k3-lica.png" style="width:50.0%" />
  <figcaption>Lica vložitev grafa <span class="math inline"><em>K</em><sub>3</sub> ∪ <em>K</em><sub>3</sub></span> v ravnino</figcaption>
  </figure>

</div>

Naj bo $\GG$ vložitev grafa $G$ v ravnino. Označimo množico točk v ravnini, ki predstavljajo vozlišča, povezave in lica:
```{math}
\begin{aligned}
    V(\GG) &= \{ \phi(u) \mid u \in V(G) \} \subseteq \RR^2, \\
    E(\GG) &= \{ \mathrm{im} \phi_e \mid e \in E(G) \}, \\
    F(\GG) &= \{ f \mid \text{$f$ lice vložitve $\GG$}\}.
\end{aligned}
```
<span class="definicija">Dolžina lica</span> $f \in F(\GG)$ je število povezav, ki ležijo na robu lica $f$. Dolžino označimo z $\ell(f)$.

<div class="zgled">

Obravnavajmo ravninski vložitvi $K_3 \cup K_3$ iz zadnjega zgleda. V prvi ravninski vložitvi je dolžina rdečega lica enaka $3$, dolžina modrega je enaka $6$ in dolžina zelenega je enaka $3$. V drugi ravninski vložitvi sta dolžini modrega in rdečega lica enaki $3$, dolžina zelenega pa je enaka $6$.

</div>

<div class="izrek">

Naj bo $G$ graf z ravninsko vložitvijo $\GG$. Potem je
```{math}
\sum_{f \in F(\GG)} \ell(f) = 2 \cdot |E(G)|.
```

</div>

<div class="dokaz">

Pristopimo podobno kot pri dokazu leme o rokovanju. Slika vsake povezave v $E(G)$ pripada robu dveh lic (vsakemu enkrat) ali enega samega lica (dvakrat). Naj bo $E(G) = \{ e_1, e_2, \dots, e_a \}$ in $F(\GG) = \{ f_1, f_2, \dots, f_b \}$. Definirajmo matriko $M = [m_{ij}]_{1 \leq i \leq a, 1 \leq j \leq b}$ razsežnosti $a \times b$ z vnosi
```{math}
m_{ij} = \begin{cases}
        0 & \text{$e_j$ ni na robu $f_i$,} \\
        1 & \text{$e_j$ je na robu $f_i$ (enkrat),} \\
        2 & \text{$e_j$ je na robu $f_i$ (dvakrat).}
    \end{cases}
```
Vsota vseh vnosov matrike $M$ je po eni strani enaka
```{math}
\sum_{i = 1}^a \sum_{j = 1}^b m_{ij} = \sum_{i = 1}^a \ell(f_i) = \sum_{f \in F(\GG)} \ell(f),
```
po drugi strani pa je enaka
```{math}
\sum_{j = 1}^b \sum_{i = 1}^a  m_{ij} = \sum_{j = 1}^b 2 = 2b = 2 \cdot |E(G)|,
```
s čimer je dokaz zaključen.

</div>

Med števili $|V(\GG)|$, $|E(\GG)|$ in $|F(\GG)|$ velja naslednja povezava.

<div class="izrek">

Naj bo $G$ *povezan* graf z ravninsko vložitvijo $\GG$. Tedaj je
```{math}
|V(\GG)| - |E(\GG)| + |F(\GG)| = 2.
```

</div>

<div class="dokaz">

Dokazujemo z indukcijo na število ciklov $c$ v grafu $G$.

Baza indukcije je $c = 0$. V tem primeru je $G$ drevo. Velja torej $|E(\GG)| = |V(\GG)| - 1$ in hkrati $|F(\GG)| = 1$, torej Eulerjeva formula velja.

Privzemimo zdaj, da formula velja za vse grafe z največ $c$ cikli. Naj bo $G$ graf s $c+1$ cikli. Naj bo $C$ nek cikel v $G$ z povezavo $\{ u,v \}$ na $C$. Opazujmo graf $G' = G - uv$. Naj bo $\GG'$ ravninska vložitev tega grafa, ki ga dobimo iz ravninske vložitve $\GG$. Graf $G'$ je povezan in ima manj ciklov kot $G$, zato lahko na njem uporabimo indukcijsko predpostavko. Za ta graf velja $|V(\GG')| = |V(G)|$ in $|E(\GG')| = |E(G)| - 1$, hkrati pa se z odstranitvijo povezave $uv$ lici s skupnim robom $uv$ spojita v eno lice, zato je $|F(\GG')| = |F(\GG)| - 1$. Ker po indukcijski predpostavki velja $|V(\GG')| - |E(\GG')| + |F(\GG')| = 2$, od tod sledi $|V(\GG)| - |E(\GG)| + |F(\GG)| = 2$.

</div>

Eulerjevo formulo lahko posplošimo tudi na nepovezane grafe.

<div class="posledica">

Naj bo $G$ graf z $\Omega$ povezanimi komponentami in z ravninsko vložitvijo $\GG$. Tedaj je
```{math}
|V(\GG)| - |E(\GG)| + |F(\GG)| = 1 + \Omega.
```

</div>

<div class="dokaz">

Naj bodo $G_1, G_2, \dots, G_\Omega$ povezane komponente grafa $G$. Dodajmo povezave $e_1, e_2, \dots, e_{\Omega - 1}$ grafu $G$, da postane povezan in da v vložitvi $\GG$ ne ustvarimo lic (na primer vse komponente grafa $G$ povežemo s prvo). Tedaj za graf $G + e_1 + e_2 + \cdots + e_{\Omega - 1}$ velja Eulerjeva formula. Ta graf ima enako število vozlišč in lic kot $\GG$, hkrati pa ima $\Omega-1$ več povezav. Velja torej
```{math}
|V(\GG)| - (|E(\GG)| + \Omega - 1) + |F(\GG)| = 2,
```
od koder sledi želeno
```{math}
|V(\GG)| - |E(\GG)| + |F(\GG)| = 1 + \Omega.
```

</div>

S pomočjo Eulerjeve formule lahko izpeljemo *potreben* pogoj za ravninskost grafa.

<div class="trditev">

Naj bo $G$ ravninski graf z vsaj tremi vozlišči. Tedaj je
```{math}
|E(G)| \leq 3 \cdot |V(G)| - 6.
```
Če je graf $G$ brez $3$-ciklov, potem je celo
```{math}
|E(G)| \leq 2 \cdot |V(G)| - 4.
```

</div>

<div class="dokaz">

Naj bo $\GG$ ena od vložitev grafa $G$ v ravnino. Ocenimo število lic te vložitve. Vsako lice je dolžine vsaj $3$.[^26] Po lemi o rokovanju za ravninske grafe od tod sledi ocena
```{math}
2 \cdot |E(G)| = \sum_{f \in F(\GG)} \ell(f) \geq \sum_{f \in F(\GG)} 3 = 3 \cdot |F(\GG)|.
```
Število lic lahko torej ocenimo navzgor kot $|F(\GG)| \leq \frac23 |E(G)|$. Iz Eulerjeve formule zdaj sledi
```{math}
2 \leq |V(G)| - |E(G)| + |F(\GG)| \leq |V(G)| - \frac13 |E(G)|,
```
ker je enakovredno želeni neenakosti $|E(G)| \leq 3 \cdot |V(G)| - 6$.

Če graf $G$ nima $3$-ciklov, potem je vsako lice dolžine vsaj $4$. Če torej v prvi neenakosti uporabimo to močnejšo oceno o dolžinah lic, z enakim postopkom dobimo še drugo neenakost v trditvi.

</div>

<div class="zgled">

- Uporabimo zadnjo trditev za to, da dokažemo, da graf $K_{3,3}$, ki smo ga obravnavali na začetku tega razdelka, res ni ravninski. Ta graf ima $6$ vozlišč in $9$ povezav. Ker je dvodelen, ne vsebuje $3$-ciklov. Če bi bil ravninski, bi zanj torej morala veljati neenakost $9 \leq 2 \cdot 6 - 4 = 8$, kar pa ne drži.

- Premislimo, da tudi graf $K_5$ ni ravninski. Ta graf ima $5$ vozlišč in $10$ povezav. Če bi bil ravninski, bi zanj morala veljati neenakost $10 \leq 3 \cdot 5 - 6 = 9$, kar pa ne drži.

</div>

Naj bo $G$ ravninski graf. Če je $H$ *podgraf* grafa $G$, potem je tudi $H$ ravninski, saj lahko iz ravninske vložitve $\GG$ preprosto odstranimo nepotrebna vozlišča in povezave. Na ta način lahko najdemo še več grafov, ki niso ravninski. Poznamo pa še dve malo bolj fleksibilni konstrukciji s podobno lastnostjo.

1.  Graf $H$ je <span class="definicija">minor</span> grafa $G$, če ga lahko konstruiramo iz nekega podgrafa $G$ s *krčenjem nekaterih povezav*.[^27]

    <div class="zgled">

    Če v Petersenovem grafu skrčimo povezave, ki povezujejo zunanji cikel z notranjim, dobimo graf $K_5$. Ta graf je torej minor Petersenovega grafa.

    </div>

    Minor ravninskega grafa je ravninski graf, saj lahko krčenje povezav v ravnini izvedemo tako, da pri tem ne pride do sekanja ostalih povezav.

    <div class="posledica">

    Če graf $G$ vsebuje minor $K_{3,3}$ ali $K_5$, potem ni ravninski.

    </div>

    <div class="zgled">

    Petersenov graf ni ravninski.

    </div>

    <span class="definicija">Wagnerjev izrek</span> nam pove, da velja celo obrat posledice. Če graf $G$ *ne* vsebuje minorja $K_{3,3}$ ali $K_5$, potem *je* ravninski. Dokaz izpustimo.

2.  Graf $H$ je <span class="definicija">subdivizija</span> grafa $G$, če ga lahko konstruiramo iz $G$ tako, da *nekatere povezave nadomestimo s potmi dolžine $2$ ali več*.[^28]

    Subdivizija ravninskega grafa je ravninski graf.

    <div class="posledica">

    Če graf $G$ vsebuje subdivizijo $K_{3,3}$ ali $K_5$, potem ni ravninski.

    </div>

    <span class="definicija">Izrek Kuratowskega</span> nam pove, da velja celo obrat posledice. Če graf $G$ *ne* vsebuje subdivizije $K_{3,3}$ ali $K_5$, potem *je* ravninski. Dokaz izpustimo.

    <div class="domacanaloga">

    Vemo že, da Petersenov graf ni ravninski. Po izreku Kuratowskega torej vsebuje subdivizijo $K_{3,3}$ ali $K_5$. Poišči to subdivizijo!

    </div>

## Barvanja grafov

V tem zaključnem razdelku bomo vzeli v roke barvice in z njimi barvali vozlišča in povezave grafov. Prikazali bomo tudi en zgled uporabe teh barvanj.

### Barvanja vozlišč

Naj bo $G$ graf in $k$ naravno število. Rečemo, da je graf $G$ <span class="definicija">vozliščno $k$-obarvljiv</span>, če obstaja preslikava $c \colon V(G) \to \{ 1,2, \dots, k\}$ z lastnostjo
```{math}
\forall u,v \in V(G) \colon u \sim v \Rightarrow c(u) \neq c(v).
```
Vsaki dve povezani vozlišči moramo torej obarvati z različnima barvama. Preslikavo $c$ imenujemo <span class="definicija">vozliščno $k$-barvanje</span> grafa $G$.

<div class="zgled">

- Liziko lahko obarvamo s $k = 3$ barvami. Vozlišče stopnje $3$ najprej obravamo z barvo $1$, potem pa list in eno od vozlišč stopnje $2$ obarvamo z barvo $2$, drugo vozlišče stopnje $2$ pa z barvo $3$.

- Graf je dvodelen, če in samo če je vozliščno $2$-obarvljiv.

</div>

Predvsem nas zanima, kolikšno je *najmanjše* število barv, ki jih potrebujemo, da obarvamo vozlišča grafa. To število, se pravi
```{math}
\chi(G) = \min \{ k \in \NN \mid \text{$G$ je vozliščno $k$-obarvljiv} \},
```
imenujemo <span class="definicija">kromatično število</span> grafa $G$.

<div class="zgled">

- $\chi(G) = 1$, če in samo če v grafu $G$ ni povezav, se pravi $E(G) = \emptyset$.

- $\chi(G) = 2$, če in samo če je graf $G$ dvodelen.

- Kromatično število cikla $\chi(C_n)$ je $2$, če je $n$ sodo, saj je v tem primeru graf dvodelen. Če je $n$ liho, pa graf ni dvodelen, zato je $\chi(C_n) \geq 3$. Po drugi strani pa $3$ barve zares zadostujejo, da pobarvamo vozlišča lihega cikla.[^29]

- $\chi(K_n) = n$.

</div>

Če je $H$ podgraf grafa $G$, potem je seveda $\chi(H) \leq \chi(G)$, saj lahko uporabimo isto barvanje, zoženo na $V(H)$. Na ta način lahko izpeljemo *spodnjo mejo* za kromatično število grafa $G$. Izberimo poln podgraf v $G$. Takemu podgrafu rečemo <span class="definicija">klika</span>. Število vozlišč največje klike označimo z $\omega(G)$. Za kliko $H$ v grafu $G$ velja $\chi(H) = |V(H)|$, ker je $H$ poln graf. Od tod sklepamo, da je $\omega(G) \leq \chi(G)$. Velikost največje klike nam torej podaja spodnjo mejo za kromatično število.

<div class="zgled">

- Za liziko $L$ velja $\omega(L) = 3$ in hkrati $\chi(L) = 3$.

- Za Petersenov graf $P$ velja $\omega(P) = 2$. Ker $P$ ni dvodelen, velja $\chi(P) \geq 3$. Ni težko najti barvanja grafa $P$ s tremi barvami, zato velja $\chi(P) = 3$.

</div>

Poglejmo si še nekaj *zgornjih* mej za kromatično število. Za ravninske grafe imamo na voljo naslednji presenetljiv in zelo močan rezultat.

<div class="izrek">

Za vsak ravninski graf $G$ je $\chi(G) \leq 4$.

</div>

Dokaz tega izreka je zelo zahteven in vključuje intenzivno uporabo računalnika za pregledovanje posebnih primerov.

<div class="zgled">

Opazujmo zemljevid sveta, na katerem so označene državne meje in meje z morji. Države in morja si predstavljajmo kot vozlišča, obstoj skupne meje pa naj pomeni sosednost vozlišč. Na ta način dobimo graf, ki je ravninski, saj je izvirni zemljevid narisan na ravnino. Po izreku je ta graf vozliščno $4$-obarvljiv. To pomeni, da lahko zemljevid sveta obarvamo s $4$ barvami, pri čemer nobeni dve sosednji državi nista enake barve.

<figure>
<img src="img/obcine.png" />
<figcaption>Barvanje občin v Sloveniji s štirimi barvami, vir: Wikimedia</figcaption>
</figure>

</div>

Za poljubne grafe, ne nujno ravninske, lahko precej preprosto zgornjo mejo za kromatično število dobimo iz maksimalne stopnje vozlišča v $G$, števila $\Delta(G)$.

<div class="trditev">

Za vsak graf $G$ je $\chi(G) \leq \Delta(G) + 1$.

</div>

<div class="dokaz">

Vozlišča barvajmo v poljubnem vrstnem redu. Prvo vozlišče obarvamo z barvo $1$. Vsako naslednje vozlišče obarvamo z najmanjšo od prostih barv. Ker ima vsako vozlišče največ $\Delta(G)$ sosedov, uporabljamo pa množico barv $\{ 1,2, \dots, \Delta(G) \}$, je vedno na voljo vsaj ena prosta barva in postopek se uspešno izvede do konca.

</div>

<div class="zgled">

- Za poln graf $K_n$ velja $\Delta(K_n) = n-1$ in $\chi(K_n) = n$, torej za ta graf velja enakost v zadnji trditvi.

- Za cikel $C_n$ velja $\Delta(C_n) = 2$, kromatično število $\chi(C_n)$ pa je bodisi $2$ za sode $n$ bodisi $3$ za lihe $n$. V primeru sodega cikla je kromatično število torej enako maksimalni stopnji, v primeru lihega cikla pa velja enakost v zadnji trditvi.

</div>

<span class="definicija">Brooksov izrek</span> nam pove, da za povezan graf $G$, ki *ni poln in ni lih cikel*, velja celo nekoliko strožja neenakost od te, ki smo jo dokazali v trditvi, in sicer $\chi(G) \leq \Delta(G)$. Dokaz izpustimo.

<div class="zgled">

Kemična tovarna pri delu uporablja snovi $S_1, S_2, \dots, S_n$. Zaradi nevarnosti eksplozije nekaterih med njimi ne smemo skladiščiti skupaj. Kolikšno je najmanjše potrebno število prostorov za varno skladiščenje teh snovi? Ta problem imenujemo <span class="definicija">problem skladiščenja nevarnih snovi</span>.

Za razrešitev problema definirajmo graf $G$ z vozlišči $V(G) = \{ S_1, S_2, \dots, S_n \}$, pri čemer sta vozlišči $u,v \in V(G)$ povezani, če in samo če snovi $u$ in $v$ *ne* smemo skladiščiti skupaj. Razporeditev snovi po prostorih podamo s funkcijo, ki vsakemu vozlišči priredi številko prostora, se pravi s funkcijo $c \colon V(G) \to \{ 1, 2, \dots, k \}$, za katero pa mora veljati $uv \in E(G) \Rightarrow c(u) \neq c(v)$. Optimalna rešitev problema je torej vozliščno barvanje grafa $G$ s $\chi(G)$ barvami.

</div>

### Barvanja povezav

Naj bo $G$ graf in $k$ naravno število. Rečemo, da je graf $G$ <span class="definicija">povezavno $k$-obarvljiv</span>, če obstaja preslikava $c \colon E(G) \to \{ 1,2, \dots, k\}$ z lastnostjo
```{math}
\forall e,f \in E(G) \colon e \cap f \neq \emptyset \Rightarrow c(e) \neq c(f).
```
Vsaki dve povezavi s skupnim krajišem moramo torej obarvati z različnima barvama. Preslikavo $c$ imenujemo <span class="definicija">povezavno $k$-barvanje</span> grafa $G$.

<div class="zgled">

Liziko $L$ lahko povezavno obarvamo s tremi barvami. Vse tri barve porabimo za $3$-cikel v liziki, z eno od treh povezav pa potem pobarvamo še dodatno povezavo v liziki.

</div>

Kot pri barvanju vozlišč nas predvsem zanima, kolikšno je *najmanjše* število barv, ki jih potrebujemo, da obarvamo povezave grafa. To število, se pravi
```{math}
\chi'(G) = \min \{ k \in \NN \mid \text{$G$ je povezavno $k$-obarvljiv} \},
```
imenujemo <span class="definicija">kromatični indeks</span> grafa $G$.

<div class="zgled">

- $\chi'(G) = 0$, če in samo če v grafu $G$ ni povezav, se pravi $E(G) = \emptyset$.

- Kromatični indeks cikla $\chi'(C_n)$ je $2$, če je $n$ sodo, saj lahko povezave pobarvamo alternirajoče z dvema barvama. Če je $n$ liho, pa je $\chi'(C_n) \geq 3$. Po drugi strani pa $3$ barve zares zadostujejo, da pobarvamo povezave lihega cikla, podobno kot pri barvanju vozlišč.

- $\chi'(K_{1,n}) = n$.

</div>

Opazujmo vozlišče maksimalne stopnje v $G$. Vsaka povezava z enim krajiščem v tem vozlišču mora biti pobarvana s svojo barvo. Velja torej $\chi'(G) \geq \Delta(G)$, kar nam podaja *spodnjo* mejo za kromatični indeks. Za nekatere grafe velja kar enakost v tej neenakosti.

<div class="izrek">

Za *dvodelen* graf $G$ je $\chi'(G) = \Delta(G)$.

</div>

<div class="dokaz">

Dokazujemo z indukcijo na $|E(G)|$.

Baza indukcije je $|E(G)| = 0$. V tem primeru je $\chi'(G) = 0 = \Delta(G)$. 

Naj bo zdaj $G$ dvodelen graf in predpostavimo, da izrek že velja za vse grafe z manj povezavami, kot jih ima $G$. Naj bo $B = \{ 1,2,\dots, \Delta(G)\}$ množica barv, s katerimi želimo pobarvati povezave $G$. Iz grafa $G$ odstranimo neko povezavo $e = uv \in E(G)$. Po indukciji lahko graf $G-e$ obarvamo z barvami iz $B$. Naj bo $c'$ tako barvanje. To barvanje bi radi razširili še na vozlišče $e$.

Naj bo $\pr(x)$ množica prostih barv v vozlišču $x$, torej tistih barv, ki jih barvanje $c'$ ne uporabi pri barvanju povezav z enim krajiščem $x$. V grafu $G - e$ velja $d(u), d(v) < \Delta(G)$, zato je $\pr(u) \neq \emptyset$ in $\pr(v) \neq \emptyset$.

Če je $\pr(u) \cap \pr(v) \neq \emptyset$, potem lahko povezavo $e$ pobarvamo s poljubno barvo iz preseka $\pr(u) \cap \pr(v)$.

Predpostavimo zdaj, da je $\pr(u) \cap \pr(v) = \emptyset$. Izberimo $\alpha \in \pr(u)$ in $\beta \in \pr(v)$. Cilj je zamenjati barvo $\beta$ pri vozlišču $u$ z barvo $\alpha$, nakar bomo povezavo $e$ pobarvali z barvo $\beta$. Kako izvedemo to zamenjavo?

<div class="domacanaloga">

Naj bo $P$ najdaljša možna pot v $G - e$, ki se začne v $u$ in je obarvana le z barvama $\alpha$ in $\beta$. Prepričaj se najprej, da vozlišče $v$ ni na $P$. Za tem na povezavah poti $P$ zamenjaj barvi $\alpha$ in $\beta$ med seboj. Na ta način smo malo spremenili barvanje $c'$ in dosegli, da je $\beta \in \pr(u)$. Ker je tudi $\beta \in \pr(v)$, lahko torej res povezavo $e$ obravamo z $\beta$.

</div>

</div>

<div class="zgled">

Velja $\chi'(K_{m,n}) = \max \{ m, n \}$.

</div>

*Zgornjo* mejo za kromatični indeks pa nam poda naslednji presenetljiv izrek.

<div class="izrek">

Za vsak graf $G$ je $\chi'(G) \leq \Delta(G) + 1$.

</div>

Za kromatični indeks vselej torej velja $\Delta(G) \leq \chi'(G) \leq \Delta(G) + 1$.

<div class="zgled">

Naj bo $P$ Petersenov graf. Velja $\Delta(P) = 3$, zato je $3 \leq \chi'(P) \leq 4$. Povezavnega barvanja s štirimi barvami ni težko najti.

<div class="domacanaloga">

Dokaži, da velja $\chi'(P) = 4$.

</div>

</div>

Vsak graf $G$ torej zadošča bodisi $\chi'(G) = \Delta(G)$ bodisi $\chi'(G) = \Delta(G) + 1$. Grafov, ki zadoščajo prvi enakosti, pravimo grafi <span class="definicija">razreda I</span>, tistim, ki zadoščajo drugi enakosti, pa pravimo grafi <span class="definicija">razreda II</span>.

<div class="zgled">

Dvodelni grafi so razreda I. Petersenov graf je razreda II.

</div>

Oglejmo si še, v kateri razred sodijo polni grafi. Polovico teh grafov lahko obdelamo z naslednjo preprosto trditvijo.

<div class="trditev">

Regularni grafi na *liho* mnogo vozliščih so razreda II.

</div>

<div class="dokaz">

Recimo, da obstaja $d$-regularen graf razreda I na liho mnogo vozliščih. Torej obstaja barvanje povezav $c \colon E(G) \to \{ 1, 2, \dots, d \}$. Naj bo $H$ podgraf grafa $G$ z množico povezav $E(H) = c^{-1}(1)$. Podgraf $H$ torej sestoji iz tistih povezav, ki so obravana z barvo $1$, in njihovih krajišč. Ker je graf $G$ $d$-regularen, v vsakem vozlišču nujno nastopajo vse barve. Torej ima vsako vozlišče kakšno povezavo barve $1$, zato je $V(H) = V(G)$. Podgraf $H$ je torej vpet. Hkrati za vsako vozlišče $u$ velja $d_H(u) = 1$, saj ima $H$ le povezave barve $1$. Po lemi o rokovanju od tod sledi
```{math}
2 |E(H)| = \sum_{v \in V(H)} d(v) = |V(H)| = |V(G)|.
```
Dobljeno je protislovno s predpostavko, da ima $G$ liho mnogo vozlišč.

</div>

<div class="zgled">

- Po trditvi velja $\chi'(K_{2n+1}) = 2n+1$, torej je $K_{2n+1}$ razreda II.

- Velja $\chi'(K_{2n + 2}) = 2n+1$, zato je $K_{2n+2}$ razreda I. Tako barvanje lahko najdemo na naslednji način. Najprej $2n+1$ vozlišč grafa razporedimo v cikel, ki ga narišemo kot pravilen $(2n+1)$-kotnik, zadnje vozlišče pa damo v središče tega cikla. Zunanji cikel je dolžine $2n+1$, ki ga povezavno obarvamo z $2n+1$ različnimi barvami. Zdaj izberemo eno od povezav na zunanjem ciklu, obarvamo z barvo $b$, in povlečemo povezave, vzporedne tej povezavi, vse jih obarvamo z barvo $b$. Nazadnje povlečemo še povezavo med središčnim vozliščem in vozliščem na ciklu, ki je kraji na nobeno od prej opisanih povezav, tudi to zadnjo povezavo obarvamo z barvo $b$. Enako ponovimo za vse povezave na zunanjem ciklu. Na ta način dobimo povezavno $(2n+1)$-barvanje grafa $K_{2n+2}$.

</div>

[^1]: Mi se bomo omejili le na končne grafe, v matematiki pa sicer obravnavamo tudi neskončne grafe.

[^2]: Spomnimo se, da je relacija na množici $V$ podmnožica množice $V \times V$, torej sestoji iz *urejenih* parov elementov iz $V$. Po drugi strani pa množica $E$ sestoji iz *neurejenih parov* elementov iz $V$, se pravi iz podmnožic $V$ z dvema elementoma.

[^3]: Na primer $3 + 7 \equiv 1 \pmod{9}$.

[^4]: Vozlišča grafa lahko torej razdelimo na dva dela, pri čemer povezave v grafu potekajo le med vozlišči iz različnih delov.

[^5]: Kasneje bomo številu $d(v,u)$ rekli tudi dolžina najkrajše poti od $v$ do $u$. Lahko se zgodi, da je od $v$ sploh ne moremo priti do $u$, na primer če je $u$ izolirana točka. V tem primeru definiramo $d(v,u) = \infty$.

[^6]: Če je $d(v,u) = \infty$, potem vozlišča $u$ zaenkrat ne obarvamo.

[^7]: Analogen argument deluje, če sta obe krajišči v $A$.

[^8]: Pri tem morda kakšno vozlišče sicer obiščemo več kot enkrat, zato to morda ni podgraf $G$.

[^9]: Natančneje, podgraf grafa $G$, vpet v vozlišča $u$, za katera velja $d(v,u) < \infty$, je dvodelen. Če obstaja kakšno vozlišče z $d(v,u) = \infty$, zdaj vzamemo to vozlišče za začetno in ponovimo opisan postopek.

[^10]: Tranzitivnost relacije $R$ sledi iz zadnje trditve: če v grafu obstaja pot od $u$ do $v$ in pot od $v$ do $w$, potem v grafu obstaja *sprehod* od $u$ do $w$, zato po trditvi obstaja tudi *pot* od $u$ do $w$.

[^11]: List $v$ je lahko le začetek ali konec poti, zato pot med vozliščema $x,y \in V(T)$, $x,y \neq v$, *ne* vsebuje $v$.

[^12]: V dokazu trditve smo namreč uporabili le lastnost 2. drevesa.

[^13]: Če namreč med Eulerjevim obhodom pridemo v neko vozlišče, moramo iz njega tudi oditi. Enako velja za začetno vozlišče obhoda, ki je enako končnemu.

[^14]: Vsaka povezava, ki je na $S$ in vstopi v $u$ in ni začetna povezava na $S$, mora iz $u$ tudi izstopiti.

[^15]: Taka pot obstaja, ker je graf $G$ povezan.

[^16]: Danes imenovanem Kaliningrad.

[^17]: Ta problem je Euler razrešil leta 1736.

[^18]: Ni se težko prepričati, da ta dva izreka veljata tudi za multigrafe.

[^19]: Hamilton je Hamiltonove grafe opazoval približno sto let po Eulerju.

[^20]: V pomoč ti bo, če vozlišča v vrsticah $1$ in $4$ obarvaš rdeče, vozlišča v vrsticah $2$ in $3$ pa modro. Konjiček lahko sicer skoči iz modrega vozlišča nazaj v modro vozlišče, na primer iz polja $(2,1)$ v $(3,3)$, ampak iz rdečega vozlišča pa konjiček lahko skoči le v modro vozlišče.

[^21]: Preslikava $\phi_e$ torej preslika rob intervala $[0,1]$ v sliki krajišč povezave $e$ s povezavo $\phi$.

[^22]: Pri risanju povezave $e$ ni nobenih samopresečnih točk.

[^23]: Tukaj smo z $\phi_e |_{(0,1)}$ označili zožitev preslikave $\phi_e$ na odprti interval $(0,1)$, z $\mathrm{im} f$ pa smo označili sliko preslikave $f$. Nobeni dve narisani povezavi se torej ne sekata (razen morda v robnih točkah).

[^24]: Narisana povezava lahko prečka narisano vozlišče, če in samo če je to rob narisane povezave.

[^25]: Oznako $G$ torej uporabljamo za abstraktni graf, se pravi $G = (V,E)$, oznako $\GG$ pa uporabljamo za vložitev grafa $G$ v ravnino, se pravi $\GG = (\phi, \{ \phi_e \}_{e \in E})$.

[^26]: Ker ima $G$ vsaj $3$ vozlišča, je vsako lice omejeno s ciklom dolžine vsaj $3$ ali pa s $P_2$ (dvakrat).

[^27]: Predstavljamo si, da izbrane povezave počasi krajšamo, dokler se krajišči ne združita. Po tem morebitne zanke odstranimo in vzporedne povezave identificiramo, da dobimo na koncu tega postopka res graf in ne multigrafa.

[^28]: Določenim povezavam torej dodamo nekaj vozlišč.

[^29]: Najprej prvih $n-1$ vozlišč pobarvamo alternirajoče z dvema barvama, zadnje vozlišče pa pobarvamo s tretjo barvo.
