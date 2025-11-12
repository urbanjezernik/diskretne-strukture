```{raw} html
<div class="naslov">
```

# Diskretne strukture

```{raw} html
  <strong>Urban Jezernik<br>
  Univerza v Ljubljani, Fakulteta za matematiko in fiziko</strong><br>

  Zadnja posodobitev: 12. 11. 2025
</div>
```

## Kratek opis predmeta

Pri predmetu se bomo najprej naučili, kaj točno so *izjave* in kako jih matematično *formalizirati*. Eden pomembnih ciljev tega je eksakten opis *sklepanja*, ki ga uporabljamo počez matematike. Te koncepte bomo najprej razvili v osnovnem *izjavnem računu*, nato pa ga bomo še posplošili do *predikatnega računa*, s katerim bomo podrobneje raziskali matematične izjave.

<div class="zgled">

Nepridipravi so razbili vhodna vrata FMF. Glavni osumljenci so študenti Ana, Bor in Cveto. Ko jih vprašamo, kdo je kriv, odgovorijo z naslednjimi izjavami:

- Ana: “Bor je kriv, Cveto pa ne.”

- Bor: “Če je kriva Ana, je kriv tudi Cveto.”

- Cveto: “Jaz nisem kriv, toda vsaj eden od drugih dveh je kriv.”

Pri predmetu se bomo naučili, kako lahko na *sistematičen način* odkrijemo, kdo je lagal, če krivi lažejo, nedolžni pa govorijo resnico.

</div>

Za tem bomo pri predmetu spoznali nekaj osnovnih diskretnih struktur, po katerih se ta predmet imenuje. Najprej bomo raziskali *relacije*, s katerimi opisujemo odnose med elementi dane množice. Pomemben poseben primer teh so *urejenosti*, ki posplošujejo običajne ureditve števil po velikosti. Najbolj podrobno si bomo ogledali *grafe*, s katerimi lahko abstraktno predstavimo mnogo pomembnih primerov relacij.

<div class="zgled">

Graf je diskretna struktura, pri kateri dano množico *vozlišč* povežemo s *povezavami*. Z grafi lahko opišemo veliko različnih vrst omrežij, na primer internetno omrežje, omrežje prijateljskih povezav na Facebooku, omrežja veriženja blokov (kriptovalute) …

Konkreten graf na spodnji sliki se imenuje Petersenov graf. Ta graf bomo tekom predmeta večkrat srečali. Na koncu predmeta bomo znali *dokazati*, da se tega grafa ne da narisati v ravnini, brez da bi se vsaj dve povezavi sekali.

<figure>
<img src="img/opis-petersen.png" />
<figcaption>Petersenov graf</figcaption>
</figure>

</div>

## Literatura

- G. Fijavž, [*Diskretne strukture*](http://matematika.fri.uni-lj.si/ds/ds.pdf), elektronska knjiga, 2015.

- M. Juvan in P. Potočnik, [*Teorija grafov in kombinatorika*](http://www.dmfa-zaloznistvo.si/ipmr/1662.htm), DMFA-založništvo, Ljubljana 2000.

- N. Prijatelj, *Osnove matematične logike I*, DMFA-založništvo, Ljubljana, 1992.

```{raw} html
<script defer>
  document.addEventListener('DOMContentLoaded', () => {
    if (!/intro\.html$/.test(window.location.pathname)) return;
    document
      .querySelectorAll('a.headerlink[href="#teorija-upodobitev"][title="Link to this heading"]')
      .forEach(el => el.remove());
    document.querySelectorAll('h2').forEach(h2 => {
      const h3 = document.createElement('h3');
      Array.from(h2.attributes).forEach(({name, value}) =>
        h3.setAttribute(name, value)
      );
      h3.innerHTML = h2.innerHTML;
      h2.replaceWith(h3);
    });
  });
</script>
```
