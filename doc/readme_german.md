# GermanIndustries Dokumentation

## Konzepte

### Wirtschaftseinstellungen

Die Wirtschaft ist per default stabil. Keine Industrie wird einfach so schließen (abgesehen von extraktiven Industrien, denen das Material zum Fördern ausgeht), aber neue Industrien werden zufällig erzeugt.
Dies kann mittels Parametern beeinflusst werden.

Selbst wenn das Schließen von Industrien erlaubt ist, wird keine Industrie schließen, die aktiv produziert (sie hat Vorräte und es wurde in der jüngsten Vergangenheit etwas produziert).
Nur Industrien, die 12 Monate lang nichts produziert haben und denen die Vorräte ausgegangen sind haben ein kleines Risiko zu schließen.

Unabhängig davon kann man ein realistisches Wirtschaftsmodell per Parameter aktivieren. Das beeinflusst nur die maximale Produktion von Industrien. Historisch betrachtet erreichte z.B. die Kohleförderung
in Deutschland ihren Höchststand bereits in den 1950er Jahren und nahm seitdem ab. Dies ist im Set für extraktive Industrien nachgebildet. Sekundäre Industrien werden nicht beeinflusst, ihre Produktion
hängt nur von der Menge der angelieferten Vorräte ab.

Einige Industrien sind nur innerhalb einer bestimmten Zeit verfügbar. Bergwerke werden zum Beispiel erst ab 1800 errichtet, was der Tatsache Rechnung trägt dass erst die Entwicklung der Dampfmaschine ein konstantes
Abpumpen des Grundwassers und damit tiefere Bergwerksschächte erlaubte.
Bestimmte chemische Industrien sind erst ab Mitte des 19. Jahrhunderts verfügbar, und die Autoproduktion startet 1910. Einige Industrien wurden mit der Zeit aufgegeben, so zum Beispiel im Bergbau.
Das heißt ab bestimmten Spieljahren werden keine neuen Industrien dieser Typen angelegt.

<a name="electricity"></a>
### Elektrizität

Wenn der entsprechende Parameter aktiviert ist benötigen einige Industrien elektrischen Strom für ihre Produktion. Dieser wird von Kraftwerken "produziert".
Strom ist allerdings keine Fracht, die transportiert werden müsste, sondern wird automatisch verteilt.

Jede Industrie gehört zu genau einer Stadt, ebenso die Kraftwerke. Der von einem Kraftwerk produzierte Strom wird über die Stadt verteilt und kann von jeder Industrie dieser Stadt benutzt werden.
Der Strombedarf hängt dabei von der Größe der Stadt (je größer die Stadt, desto mehr Grundbedarf) und der Produktionsmenge der Industrien ab.
Wenn das Kraftwerk genug Strom liefert ist alles prima. Wenn nicht, werden die betroffenen Industrien die Produktion reduziern oder - im schlimmsten Fall - ganz stoppen.
Die notwendigen Informationen dazu werden im Industriefenster angezeigt.

<img src="electricity_power_station_de.png">

Das Kraftwerk zeigt den aktuellen Bedarf und die Produktion. Der Bedarf ist dabei - wie oben erklärt - die Summe des Grundbedarfs der Stadt und der Ansprüche der Industrien der Stadt.

<img src="electricity_no_power_de.png">
<img src="electricity_not_enough_power_de.png">
<img src="electricity_100_de.png">

Diese drei Bilder zeigen die gleiche Industrie in verschiedenen Situationen - kein Strom verfügbar, etwas Strom verfügbar (aber nicht genug für die theoretisch mögliche Produktion) und genug Strom verfügbar.

### Modularität

Das Set ist modular angelegt.
Die grundlegende Industriekette ist relativ simpel und vergleichbar mit den Industrien im Basisspiel.
Allerdings kann man nun zusätzliche Erweiterungen per Parameter aktivieren.
Diese Erweiterungen fügen weitere Industrien und Frachten hin und modifizieren existierende Industrien.
Somit kann sich jeder Spieler das Set nach seinen Vorlieben konfigurieren.
Der eine möchte vielleicht auf einer kleinen Karte mit wenigen Industrien spielen, der nächste will auf einer großen Karte viele verschiedene Industrien, und wiedere andere möchten sich vielleicht auf bestimmte
Industriezweige konzentrieren.
Die meisten Erweiterungen können unabhängig voneinander aktiviert werden.

### Produktionsmengen

Primärindustrien (diejenigen, die keine Rohmaterialien benötigen, also Minen, Farmen, Ölquellen usw.) erhöhen ihre Produktion wenn man genügend produzierte Fracht abtransportiert.
Mit der Zeit wird die Produktion steigen oder sinken und sich so den Transportkapazitäten anpassen.

Industrien, die von angelieferten Rohmaterialien abhängen (siehe [Vorräte](#stockpiling) benutzen bei jedem Produktionsschritt (rund acht Mal im Monat mit den Standardeinstellungen) 10% ihres Vorrates für die Produktion.
Wenn also 100t Material vorrätig sind, wird der nächste Produktionsschritt 10t verbrauchen und somit 90t übrig lassen. Der Schritt danach verbraucht 9t, so dass 81t verbleiben.
Das wiederholt sich, bis die Vorräte erschöpft sind.

Die Produktionsmenge hängt nun von der Menge der eingesetzten Rohmaterialien und von der Art der Industrie ab. Jeder Industrietyp hat einen festen Wert für das Verhältnis zwischen einsetzten Materialien und der resultierenden
Menge an Produkten.
Eine gewisse Menge Abfall ist nun mal bei den meisten Produktionsschritten unvermeidlich.

Darüber hinaus kann die Produktionsmenge auch davon abhängen, wie viele verschiedene Rohmaterialien vorhanden sind. Die Nahrungsmittelfabrik z.B. verarbeitet Getreide, Vieh und Fisch, aber man braucht nicht alle drei
transportieren - die Produktion beginnt, sobald eine dieser Frachten vorrätig ist. Allerdings reduziert sich dabei die Produktmenge. Wenn man hingegen alle drei Frachten vorrätig hat, erhöht sich die Produktion von Nahrung drastisch.

Jede Industrie enthält die notwendigen Informationen im Infofenster.

<img src="industry_any_de.png">

Diese Industrie hängt von mehreren Rohmaterialien ab, beginnt die Produktion aber, sobald eins dieser Materialien vorrätig ist.

<img src="industry_optional_de.png">

Diese Industrie hat optionale Abhängigkeiten. Die in schwarz dargestellten Rohstoffe müssen vorhanden sein, damit produziert werden kann, allerdings ist die Produktionsmenge limitiert, solange die optionalen
Rohstoffe nicht verfügbar sind.

<img src="industry_optional_any_de.png">

Diese Industrie hat optionale Rohstoffe, beginnt aber mit der Produktion sobald einer der zwingend notwendigen Rohstoffe verfügbar ist.
Die Produktionsmenge erhöht sich hier mit der Anzahl der verschiedenen verfügbaren Rohstoffe.

<a name="resource_depletion"></a>
### Erschöpfte Rohstoffe

Extraktive Industrien wie Bergwerke und Ölquellen werden mit einer zufälligen Menge an Rohstoffen generiert, die sie dann abbauen. Im Lauf der Zeit wird also dieser Vorrat immer geringer. Sobald keine Ressourcen
zum Abbauen mehr vorhanden sind wird die Industrie schließen. Das Industriefenster zeigt an, wie viel Rohstoffe noch gefördert werden können und wie lange das voraussichtlich noch dauern wird.

<img src="resource_depletion_de.png">

Das Bild zeigt, wie die relevanten Infos dargestellt werden. Damit sollte der Spieler ausreichend Vorwarnzeit zum Planen haben.

<a name="stockpiling"></a>
### Vorratshaltung

Die meisten Industrien verarbeiten Rohstoffe zu neuen Produkten. Je nach Industrie werden dabei verschiedene Arten von Abhängigkeiten modelliert.
Im einfachsten Fall benötigt die Industrie alle Rohstoffe, um irgendetwas produzieren zu können. Das einfachste Stahlwerk z.B. benötigt Kohle und Eisenerz. Wenn man nur Eisenerz anliefert wird es zwar bevorrated,
aber nichts produziert, solange Kohle fehlt.

Einige Industrien haben optionale Rohstoffe. Diese sind in der Liste in weiß dargestellt. Sie werden nicht zur Produktion benötigt, vergrößern aber die produzierten Mengen.

Die Vorräte können maximal 65.535 Einheiten speichern, das ist eine Limitierung des Spiels. Wenn man dieses Limit erreicht passiert aber nicht viel, die nächste Lieferung wird einfach für die Vorratshaltung ignoriert
(man erhält aber das Geld für die Lieferung). Da die Produktion mit der Menge der Vorräte skaliert sollte es schwierig sein, an diese Limitierungen zu stoßen, wenn man es nicht gerade darauf anlegt, weil man nicht alle notwendigen Rohstoffe bereitstellt.

## Parameter

Das Set enthält eine Reihe von Parametern, mit denen man das Verhalten beeinflussen kann:

 Die Produktionsmenge von extraktiven Industrien (Bergwerke, Ölquellen, ...) kann skaliert werden. Je nach verwendeten Fahrzeugen kann eine mehr oder wenige hohe Produktion sinnvoll sein.
- Das Wirtschaftsmodell (stabil oder realistisch). Das beeinflusst die Produktionsmengen der extraktiven Industrien, da z.B. im Bergbau die maximalen Fördermengen bereits in den 1950er Jahren erreicht wurden.
Mit dem realistischen Modell werden die Produktionsmengen danach abnehmen, egal wie gut man die Industrie bedient.
- Man kann festlegen, ob bestimmte Industrien elektrischen Strom benötigen (siehe [Elektrizität](#electricity).
- Verbieten der Industriegenerierung. Wenn das aktiviert ist werden nach dem Spielstart keine neuen Industrien mehr generiert. Der Spieler kann Industrien weiterhin finanzieren.
- Verbieten von Industrieschließungen. Wenn es aktiviert ist, werden Industrien niemals schließen. Ansonsten laufen Industrien, die 12 Monate lang nichts produziert haben Gefahr zu schließen.
- Erweiterungen an/abschalten. Jede Erweiterung fügt weitere Frachten und Industrien hinzu und verändert die Industrieketten. Siehe [Erweiterungen](#extensions) für eine detaillierte Auflistung.

## Die grundlegende Industriekette

Das Set enthält einige grundlegende Industrien und Frachten. Diese sind im Folgenden aufgelistet:

[Eisenerz](#cargo_IORE) [Fahrzeuge](#cargo_VEHI) [Fisch](#cargo_FISH) [Getreide](#cargo_GRAI) [Holz](#cargo_WOOD) [Kohle](#cargo_COAL) [Kunststoffe](#cargo_PLAS) [Nahrungsmittel](#cargo_FOOD) [Passagiere](#cargo_PASS) [Post](#cargo_MAIL) [Sand](#cargo_SAND) [Schnittholz](#cargo_WDPR) [Stahl](#cargo_STEL) [Vieh](#cargo_LVST) [Waren](#cargo_GOOD) [Öl](#cargo_OIL_) 

[Autofabrik](#industry_10) [Autohaus](#industry_18) [Bauernhof](#industry_20) [Bauhof](#industry_23) [Eisenerzbergwerk](#industry_32) [Fischgründe](#industry_39) [Hafen](#industry_41) [Hotel](#industry_49) [Integriertes Stahlwerk](#industry_51) [Kaufhaus](#industry_58) [Kohlebergwerk](#industry_59) [Kraftwerk](#industry_61) [Kunststofffabrik](#industry_63) [Laden](#industry_75) [Möbelfabrik](#industry_81) [Nahrungsmittelfabrik](#industry_86) [Sägewerk](#industry_102) [Tankstelle](#industry_105) [Wald](#industry_118) [Ölbohrinsel](#industry_121) [Ölquellen](#industry_122) 

<img src="base_industry_chain_de.png" alt="Die grundlegende Industriekette">

Wenn eine Industriebox hier ein Jahr enthält, so ist es das erste Jahr in dem diese Industrie generiert/finanziert werden kann. Wenn die Box zwei Jahreszahlen enthält so sind es Start und Ende des Zeitrahmens, in dem die Industrie verfügbar ist.

Die Farben der Pfeile entsprechen den Farben, die im Wirtschaftsketten-Fenster im Spiel verwendet werden (mit Ausnahme von Elektrizität, die ja keine zu transportierende Fracht ist, siehe [Elektrizität](#electricity)).
Solange nicht anders angegeben, benötigen die Industrien alle angegeben Frachten, um irgendwas produzieren zu können.

<a name="extensions"></a>
## Erweiterungen

<img src="base_industries_with_extensions_de.png" alt="Die Wirtschaftsketten mit Erweiterungen">

Dieses Bild zeigt die Interaktionen zwischen den unterschiedlichen Erweiterungen. Jede Erweiterung benutzt eine andere Farbe. Wenn die Erweiterung nicht aktiviert ist, kann man alle damit verbundenen Pfeile ignorieren.
Eine Fracht in einer farbigen Box ist Teil der Erweiterung der gleichen Farbe, wenn die Erweiterung also nicht aktiv ist, ist auch die Fracht nicht aktiv.
Für jede Erwtierung gibt es ein zusätzliches Diagramm, welches die Verbindungen zwischen den Frachten und Industrien detailliert zeigt.

Das Set enthält 11 Erweiterungen, die nachfolgend aufgelistet sind.

<a name="extension_0"></a>
### Aluminium

Aluminium ist ein Leichtmetall, welches 1825 entdeckt wurde. Am Ende des 19. Jahrhunderts begann die Massenproduktion, und im Verlauf des 20. Jahrhunderts wurde es das wichtigste Nichteisen-Metall für industrielle Zwecke. Es ist leichter als Stahl, ein exzellenter Leiter und kann relativ einfach geformt und bearbeitet werden. Ohne Aluminium ist die Luftfahrt praktisch undenkbar. Aus ähnlichen Gründen wird Aluminium im Automobilbau eingesetzt, und quasi jeder kennt Alufolie und Getränkedosen. Die Herstellung von Aluminium konzentriert sich auf Südostasien und Australien, Norwegen ist der größte Produzent in Europa. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Aluminium](#cargo_ALUM)
* [Bauxit](#cargo_AORE)


### Neue Industrien

* [Aluhütte](#industry_0)
* [Aluhütte](#industry_1)


#### Modifizierte Industrien

* [Aluhütte](#industry_0)
* [Aluhütte](#industry_1)
* [Autofabrik](#industry_11)
* [Autofabrik](#industry_13)
* [Autofabrik](#industry_15)
* [Autofabrik](#industry_17)
* [Hafen](#industry_42)
* [Hafen](#industry_44)
* [Hafen](#industry_46)
* [Hafen](#industry_48)
* [Verpackungsmittelfabrik](#industry_109)
* [Verpackungsmittelfabrik](#industry_111)
* [Verpackungsmittelfabrik](#industry_113)
* [Verpackungsmittelfabrik](#industry_115)


<img src="industry_chain_extension_aluminium_de.png" alt="Industrieketten für Erweiterung Aluminium">

<a name="extension_1"></a>
### Bauindustrie

Die Kunst des Bauens von steineren Wänden und Gebäuden ist eine der ältesten kulturellen Errungenschaften der Menschheit. Aus den Anfängen mit gebrannten Lehmziegeln entstand über Jahrhunderte ein eigener Industriezweig. Im 19. Jahrhundert wurde die industrielle Produktion von Ziegeln notwendig, aus denen man Fabrikhallen baute. Große Steinbrücken wie die Göltzschtalbrücke in Sachsen, die größte Ziegelsteinbrücke der Welt, zeigen eindrucksvoll wie wichtig diese Industriezweige waren. Die Ziegel wurden schließlich weitestgehend durch Zement und Beton verdrängt, was den Bau moderner Wolkenkratzer erst möglich macht. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#e8b810;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Kalkstein](#cargo_LIME)
* [Zement](#cargo_CMNT)
* [Ziegel](#cargo_BDMT)


### Neue Industrien

* [Kalksteinbergwerk](#industry_57)
* [Sandgrube](#industry_98)
* [Zementfabrik](#industry_119)
* [Ziegelei](#industry_120)


#### Modifizierte Industrien

* [Bauhof](#industry_22)
* [Farbenfabrik](#industry_36)
* [Farbenfabrik](#industry_38)
* [Kalksteinbergwerk](#industry_57)
* [Sandgrube](#industry_98)
* [Zementfabrik](#industry_119)
* [Ziegelei](#industry_120)


<img src="industry_chain_extension_building_industries_de.png" alt="Industrieketten für Erweiterung Bauindustrie">

<a name="extension_2"></a>
### Farbindustrie

Über tausende Jahre wurden Farben und Pigmente wie Indigo aus Pflanzen und diversen Pulvern hergestellt, was sie für industrielle Anwendungen schlicht zu teuer machte. Die Produktion künstlicher Farbmittel war eine der ersten wichtigen Anwendungen der noch jungen chemischen Industrie. Einige der wichtigsten chemischen Konzerne Deutschlands gehen auf Farbfabriken zurück, wie Agfa oder BASF (beide führen Teile des Namens auf Anilin zurück, eine Chemikalie, die in der Produktion von Farben eine bedeutende Rolle spielt). 1925 schlossen sich die größten Chemiekonzerne Deutschlands zur IG Farbengesellschaft zusammen und formten so die weltgrößte Chemiefirma. Selbst heute noch sind Farben, Pigmente und Färbemittel wichtige Produkte der Chemieindustrie und haben ein weites Feld von Anwendungen in der Textilindustrie, in der Kunststoffherstellung, im Bauwesen und nicht zuletzt im Automobilsektor. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#bc546c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Farbe](#cargo_COAT)
* [Kupfer](#cargo_COPR)
* [Kupfererz](#cargo_CORE)
* [Ruß](#cargo_CBLK)


### Neue Industrien

* [Farbenfabrik](#industry_35)
* [Farbenfabrik](#industry_36)
* [Farbenfabrik](#industry_37)
* [Farbenfabrik](#industry_38)
* [Kupfererzbergwerk](#industry_71)
* [Kupfererzbergwerk](#industry_72)
* [Kupferhütte](#industry_73)
* [Kupferhütte](#industry_74)
* [Rußfabrik](#industry_95)
* [Rußfabrik](#industry_96)


#### Modifizierte Industrien

* [Autofabrik](#industry_12)
* [Autofabrik](#industry_13)
* [Autofabrik](#industry_16)
* [Autofabrik](#industry_17)
* [Erzschmelze](#industry_34)
* [Farbenfabrik](#industry_35)
* [Farbenfabrik](#industry_36)
* [Farbenfabrik](#industry_37)
* [Farbenfabrik](#industry_38)
* [Hafen](#industry_43)
* [Hafen](#industry_44)
* [Hafen](#industry_47)
* [Hafen](#industry_48)
* [Kunststofffabrik](#industry_65)
* [Kunststofffabrik](#industry_66)
* [Kunststofffabrik](#industry_69)
* [Kunststofffabrik](#industry_70)
* [Kupfererzbergwerk](#industry_71)
* [Kupfererzbergwerk](#industry_72)
* [Kupferhütte](#industry_73)
* [Kupferhütte](#industry_74)
* [Rußfabrik](#industry_95)
* [Rußfabrik](#industry_96)
* [Textilfabrik](#industry_107)


<img src="industry_chain_extension_painting_industries_de.png" alt="Industrieketten für Erweiterung Farbindustrie">

<a name="extension_3"></a>
### Glas

Glas ist ein allgegenwärtiges Material im täglichen Leben. Die Erweiterung fügt Frachten und Industrien hinzu, die für die Herstellung von Glas relevant sind und verändert andere Industrien, so dass sie Glas, in erster Linie für Verpackungen, benötigen. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Branntkalk](#cargo_QLME)
* [Glas](#cargo_GLAS)


### Neue Industrien

* [Glasfabrik](#industry_40)
* [Kalkbrennerei](#industry_55)
* [Kalkbrennerei](#industry_56)


#### Modifizierte Industrien

* [Autofabrik](#industry_14)
* [Autofabrik](#industry_15)
* [Autofabrik](#industry_16)
* [Autofabrik](#industry_17)
* [Brauerei](#industry_27)
* [Glasfabrik](#industry_40)
* [Integriertes Stahlwerk](#industry_52)
* [Integriertes Stahlwerk](#industry_54)
* [Kalkbrennerei](#industry_55)
* [Kalkbrennerei](#industry_56)
* [Verpackungsmittelfabrik](#industry_110)
* [Verpackungsmittelfabrik](#industry_111)
* [Verpackungsmittelfabrik](#industry_114)
* [Verpackungsmittelfabrik](#industry_115)


<img src="industry_chain_extension_glass_de.png" alt="Industrieketten für Erweiterung Glas">

<a name="extension_4"></a>
### Grundlegende Anorganische Chemie

Anorganische Chemie beschäftigt sich mit chemischen Verbindungen, die nicht auf Kohlenstoff basieren. Dazu zählen zahllose Minerale, Säuren, Laugen und natürlich Metalle. Mit dem Fortschritt in der chemischen Forschung und der Entdeckung immer neuer Anwendungen wurden diese Stoffe immer wichtiger. Lange Zeit waren die Produktionsmengen von Schwefelsäure und Chlor wichtige Indikatoren für Aussagen über die Industrialisierung eines Landes. Die Erweiterung führt eine Reihe von grundlegenden Chemikalien und die zugehörigen Industrien ein, die wiederum eine Voraussetzung für andere Erweiterungen sind. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#b8dcc8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Chlor](#cargo_CHLO)
* [Natronlauge](#cargo_LYE_)
* [Salz](#cargo_SALT)
* [Wasserstoff](#cargo_H2__)


### Neue Industrien

* [Arzneimittelfabrik](#industry_2)
* [Arzneimittelfabrik](#industry_3)
* [Arzneimittelfabrik](#industry_4)
* [Arzneimittelfabrik](#industry_5)
* [Arzneimittelfabrik](#industry_6)
* [Arzneimittelfabrik](#industry_7)
* [Arzneimittelfabrik](#industry_8)
* [Arzneimittelfabrik](#industry_9)
* [Chloralkali Elektrolyseanlage](#industry_28)
* [Salzbergwerk](#industry_97)


#### Modifizierte Industrien

* [Aluhütte](#industry_1)
* [Arzneimittelfabrik](#industry_2)
* [Arzneimittelfabrik](#industry_3)
* [Arzneimittelfabrik](#industry_4)
* [Arzneimittelfabrik](#industry_5)
* [Arzneimittelfabrik](#industry_6)
* [Arzneimittelfabrik](#industry_7)
* [Arzneimittelfabrik](#industry_8)
* [Arzneimittelfabrik](#industry_9)
* [Chloralkali Elektrolyseanlage](#industry_28)
* [Kunststofffabrik](#industry_64)
* [Kunststofffabrik](#industry_66)
* [Kunststofffabrik](#industry_68)
* [Kunststofffabrik](#industry_70)
* [Molkerei](#industry_77)
* [Molkerei](#industry_79)
* [Nahrungsmittelfabrik](#industry_87)
* [Nahrungsmittelfabrik](#industry_89)
* [Nahrungsmittelfabrik](#industry_92)
* [Nahrungsmittelfabrik](#industry_93)
* [Salzbergwerk](#industry_97)
* [Säurefabrik](#industry_104)


<img src="industry_chain_extension_basic_inorganic_chemistry_de.png" alt="Industrieketten für Erweiterung Grundlegende Anorganische Chemie">

<a name="extension_5"></a>
### Koks und Schwefel

Koks und Schwefel sind wichtige Chemikalien für die Industrie. Ohne Koks ist keine großtechnische Metallherstellung möglich, und Schwefel bzw. Schwefelsäure ist das Rückgrat zahlloser Industrien. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Koks](#cargo_COKE)
* [Kupferkies](#cargo_PORE)
* [Schwefel](#cargo_SULP)
* [Säure](#cargo_ACID)


### Neue Industrien

* [Erzschmelze](#industry_33)
* [Erzschmelze](#industry_34)
* [Kokerei](#industry_60)
* [Säurefabrik](#industry_103)
* [Säurefabrik](#industry_104)


#### Modifizierte Industrien

* [Arzneimittelfabrik](#industry_6)
* [Arzneimittelfabrik](#industry_7)
* [Arzneimittelfabrik](#industry_8)
* [Arzneimittelfabrik](#industry_9)
* [Erzschmelze](#industry_33)
* [Erzschmelze](#industry_34)
* [Farbenfabrik](#industry_37)
* [Farbenfabrik](#industry_38)
* [Hafen](#industry_45)
* [Hafen](#industry_46)
* [Hafen](#industry_47)
* [Hafen](#industry_48)
* [Integriertes Stahlwerk](#industry_53)
* [Integriertes Stahlwerk](#industry_54)
* [Kalkbrennerei](#industry_56)
* [Kokerei](#industry_60)
* [Kraftwerk](#industry_62)
* [Kupfererzbergwerk](#industry_72)
* [Kupferhütte](#industry_74)
* [Säurefabrik](#industry_103)
* [Säurefabrik](#industry_104)
* [Ölraffinerie](#industry_124)


<img src="industry_chain_extension_coke_sulphur_de.png" alt="Industrieketten für Erweiterung Koks und Schwefel">

<a name="extension_6"></a>
### Lebensmittelindustrie

Die Lebensmittelindustrie sorgt dafür, dass die Supermärkte volle Regale haben. Deutschland ist bekannt für seine große Anzahl von Brotsorten und die hohe Dichte an Brauereien. Die Erweiterung ersetzt die generische Lebensmittelfabrik durch spezialisierte Betriebe, so dass die Transportaufgaben etwas komplexer werden. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#5c9c34;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Milch](#cargo_MILK)


### Neue Industrien

* [Brauerei](#industry_26)
* [Brauerei](#industry_27)
* [Molkerei](#industry_76)
* [Molkerei](#industry_77)
* [Molkerei](#industry_78)
* [Molkerei](#industry_79)
* [Mühle](#industry_84)
* [Mühle](#industry_85)
* [Schlachthof](#industry_99)
* [Schlachthof](#industry_100)
* [Viehzucht](#industry_116)
* [Viehzucht](#industry_117)


#### Modifizierte Industrien

* [Bauernhof](#industry_21)
* [Brauerei](#industry_26)
* [Brauerei](#industry_27)
* [Molkerei](#industry_76)
* [Molkerei](#industry_77)
* [Molkerei](#industry_78)
* [Molkerei](#industry_79)
* [Mühle](#industry_84)
* [Mühle](#industry_85)
* [Nahrungsmittelfabrik](#industry_88)
* [Nahrungsmittelfabrik](#industry_89)
* [Nahrungsmittelfabrik](#industry_91)
* [Nahrungsmittelfabrik](#industry_93)
* [Schlachthof](#industry_99)
* [Schlachthof](#industry_100)
* [Viehzucht](#industry_116)
* [Viehzucht](#industry_117)


<img src="industry_chain_extension_food_industries_de.png" alt="Industrieketten für Erweiterung Lebensmittelindustrie">

<a name="extension_7"></a>
### Organische Chemie

Die organische Chemie beschäftigt sich mit Kohlenwasserstoffen, also Verbindungen aus Kohlenstoff und Wasserstoff. Die Ausgangsstoffe (Kohle und vor allem Erdöl) sind durch Umwandlung organischer Stoffe (z.B. Pflanzen) über Jahrmillionen entstanden. Im 20. Jahrhundert wurde Erdöl zu einem der wichtigsten Rohstoffe der Menschheit, da es für die Produktion von Treibstoffen und Kunststoffen unverzichtbar ist. So werden täglich mehrere Milliarden Liter Erdöl verbraucht. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#787840;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Ethylen](#cargo_C2H4)
* [Naphtha](#cargo_RFPR)
* [Treibstoff](#cargo_PETR)


### Neue Industrien

* [Dampfreformierer](#industry_29)
* [Hydrierwerk](#industry_50)
* [Steamcracker](#industry_101)
* [Ölraffinerie](#industry_123)
* [Ölraffinerie](#industry_124)


#### Modifizierte Industrien

* [Arzneimittelfabrik](#industry_4)
* [Arzneimittelfabrik](#industry_5)
* [Arzneimittelfabrik](#industry_8)
* [Arzneimittelfabrik](#industry_9)
* [Dampfreformierer](#industry_29)
* [Hydrierwerk](#industry_50)
* [Kunststofffabrik](#industry_67)
* [Kunststofffabrik](#industry_68)
* [Kunststofffabrik](#industry_69)
* [Kunststofffabrik](#industry_70)
* [Rußfabrik](#industry_96)
* [Steamcracker](#industry_101)
* [Ölraffinerie](#industry_123)
* [Ölraffinerie](#industry_124)


<img src="industry_chain_extension_organic_chemistry_de.png" alt="Industrieketten für Erweiterung Organische Chemie">

<a name="extension_8"></a>
### Papier

Papier ist ein allgegenwärtiges Material im täglichen Leben. Die Erweiterung fügt Frachten und Industrien hinzu, die für die Herstellung von Papier relevant sind und verändert andere Industrien, so dass sie Papier, in erster Linie für Verpackungen, benötigen. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#fcfcc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Papier](#cargo_PAPR)


### Neue Industrien

* [Druckerei](#industry_30)
* [Druckerei](#industry_31)
* [Papiermühle](#industry_94)


#### Modifizierte Industrien

* [Druckerei](#industry_30)
* [Druckerei](#industry_31)
* [Papiermühle](#industry_94)
* [Verpackungsmittelfabrik](#industry_112)
* [Verpackungsmittelfabrik](#industry_113)
* [Verpackungsmittelfabrik](#industry_114)
* [Verpackungsmittelfabrik](#industry_115)


<img src="industry_chain_extension_paper_de.png" alt="Industrieketten für Erweiterung Papier">

<a name="extension_9"></a>
### Textilindustrie

Die Produktion von Garnen und Stoffen zur Herstellung von Kleidung war eine der ersten Kulturleistungen der Menscheit. Rohstoffe für die Produktion umfassen Wolle von Schafen und anderen Tieren als auch verschiedenste Pflanzenfasern wie Baumwolle. Innovationen der chemischen Industrie im 20. Jahrhundert brachten zusätzlich Kunstfasern wie polyester hervor. 

Die Herstellung von Stoffen war ein arbeitsintensiver Prozess und gehörte zu den ersten Bereichen, die von der Industrialisierung im 18. Jahrhundert erfasst wurden. Deutschland hatte eine große Textilindustrie in Sachsen und Schlesien, die wiederum von der Industrialisierung profitierte. Chemnitz wurde so zum Zentrum des Maschinenbaus mit einem Fokus auf die Herstellung von Textilmaschinen. Allerdings schrumpft die Industrie seit der Mitte des 20. Jahrhunderts, und heutzutage ist der Großteil der Produktion aus Kostengründen nach Asien abgewandert. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#d49480;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Textilien](#cargo_TEXT)
* [Wolle](#cargo_WOOL)


### Neue Industrien

* [Bekleidungsfabrik](#industry_24)
* [Bekleidungsfabrik](#industry_25)
* [Textilfabrik](#industry_106)
* [Textilfabrik](#industry_107)


#### Modifizierte Industrien

* [Bauernhof](#industry_19)
* [Bekleidungsfabrik](#industry_24)
* [Bekleidungsfabrik](#industry_25)
* [Möbelfabrik](#industry_80)
* [Möbelfabrik](#industry_82)
* [Textilfabrik](#industry_106)
* [Textilfabrik](#industry_107)
* [Viehzucht](#industry_117)


<img src="industry_chain_extension_textile_industries_de.png" alt="Industrieketten für Erweiterung Textilindustrie">

<a name="extension_10"></a>
### Verpackungsmittelindustrie

Die Verpackungsmittelindustrie produziert alle Arten von Behältern und Verpackungen, seien es Kartons oder Getränkedosen. Diese Erweiterung fügt damit ein zusätzliches logistisches Element für die Güter- und Nahrungsmittelproduktion hinzu. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Verpackungen](#cargo_MNSP)


### Neue Industrien

* [Verpackungsmittelfabrik](#industry_108)
* [Verpackungsmittelfabrik](#industry_109)
* [Verpackungsmittelfabrik](#industry_110)
* [Verpackungsmittelfabrik](#industry_111)
* [Verpackungsmittelfabrik](#industry_112)
* [Verpackungsmittelfabrik](#industry_113)
* [Verpackungsmittelfabrik](#industry_114)
* [Verpackungsmittelfabrik](#industry_115)


#### Modifizierte Industrien

* [Arzneimittelfabrik](#industry_3)
* [Arzneimittelfabrik](#industry_5)
* [Arzneimittelfabrik](#industry_7)
* [Arzneimittelfabrik](#industry_9)
* [Bekleidungsfabrik](#industry_25)
* [Druckerei](#industry_31)
* [Molkerei](#industry_78)
* [Molkerei](#industry_79)
* [Möbelfabrik](#industry_82)
* [Möbelfabrik](#industry_83)
* [Mühle](#industry_85)
* [Nahrungsmittelfabrik](#industry_90)
* [Nahrungsmittelfabrik](#industry_91)
* [Nahrungsmittelfabrik](#industry_92)
* [Nahrungsmittelfabrik](#industry_93)
* [Schlachthof](#industry_100)
* [Verpackungsmittelfabrik](#industry_108)
* [Verpackungsmittelfabrik](#industry_109)
* [Verpackungsmittelfabrik](#industry_110)
* [Verpackungsmittelfabrik](#industry_111)
* [Verpackungsmittelfabrik](#industry_112)
* [Verpackungsmittelfabrik](#industry_113)
* [Verpackungsmittelfabrik](#industry_114)
* [Verpackungsmittelfabrik](#industry_115)


<img src="industry_chain_extension_packaging_industries_de.png" alt="Industrieketten für Erweiterung Verpackungsmittelindustrie">


## Cargos

Das Set enthält 43 Frachten, die nachfolgend aufgelistet sind.

<a name="cargo_ALUM"></a>
### Aluminium

Aluminium ist ein Leichtmetall, was praktisch überall dort zum Einsatz kommt, wo Stahl zu schwer ist. Man benötigt es zum Bau von Flugzeugen und Autos, aber auch für Haushaltsgegenstände wie Alufolie und Getränkedosen. Allerdings ist die Herstellung von reinem Aluminium ein relativ komplizierter und äußerst energieintensiver Prozess. Die Massenproduktion begann entsprechend erst im späten 19. Jahrhundert. Deutschland ist heute einer der größten Produzenten in Europa (und der größte Verbraucher), obwohl die Energiekosten vergleichsweise hoch liegen. 

Eintrag in der Frachttabelle: ALUM

Teil der Erweiterung: [Aluminium](#extension_0)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Aluhütte](#industry_0) | [Autofabrik](#industry_11) |
| [Aluhütte](#industry_1) | [Autofabrik](#industry_13) |
|  | [Autofabrik](#industry_15) |
|  | [Autofabrik](#industry_17) |
|  | [Verpackungsmittelfabrik](#industry_109) |
|  | [Verpackungsmittelfabrik](#industry_111) |
|  | [Verpackungsmittelfabrik](#industry_113) |
|  | [Verpackungsmittelfabrik](#industry_115) |

<a name="cargo_AORE"></a>
### Bauxit

Bauxit ist ein Erz aus welchem Aluminium hergestellt wird. Deutschland hat keine eigenen Bauxitlagerstätten und ist daher von Importen abhängig. 

Eintrag in der Frachttabelle: AORE

Teil der Erweiterung: [Aluminium](#extension_0)

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#541c10;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_42) | [Aluhütte](#industry_0) |
| [Hafen](#industry_44) | [Aluhütte](#industry_1) |
| [Hafen](#industry_46) |  |
| [Hafen](#industry_48) |  |

<a name="cargo_QLME"></a>
### Branntkalk

Branntkalk ist chemisch gesehen Calciumoxid. Es ist eine sehr instabile Substanz, die schon mit Luftfeuchtigkeit reagiert. Sie reagiert auf gleiche Weise mit der Feuchtigkeit auf der Haut, wodurch gefährliche Verätzungen entstehen, daher wird es auch Ätzkalk genannt. Die Reaktion erzeugt außerdem Wärme, so dass von Branntkalk auch eine gewisse Brandgefahr ausgeht. Branntkalk ist ein wichtiger Betandteil von Mörtel und Zement, wird aber auch als Dünger und Desinfektionsmittel eingesetzt. Die wichtigste Anwendung liegt in der Stahlproduktion, wo er zum Entschwefeln von Roheisen verwendet wird. 

Eintrag in der Frachttabelle: QLME

Teil der Erweiterung: [Glas](#extension_3)

Frachtklassen: Nässeempfindlich, Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcfcc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kalkbrennerei](#industry_55) | [Glasfabrik](#industry_40) |
| [Kalkbrennerei](#industry_56) | [Integriertes Stahlwerk](#industry_52) |
|  | [Integriertes Stahlwerk](#industry_54) |

<a name="cargo_CHLO"></a>
### Chlor

Chlor ist ein sehr reaktionsfreudiges chemisches Element, welches eine große Rolle in der Papierindustrie oder als Desinfektionsmittel spielt. Darüber hinaus wird es für zahllose Prozesse in der chemischen Industrie benötigt, hauptsächlich bei der Produktion von verschiedensten Kunststoffen wie PVC. In höheren Konzentrationen ist Chlor äußerst giftig und wurde in der Vergangenheit auch im Rahmen chemischer Kriegführung eingesetzt. Seit dem frühen 20. Jahrhundert wird Chlor hauptsächlich durch das Spalten von Salzlösungen durch Elektrolyse im sogenannten Chlor-Alkali-Prozess hergestellt. 

Eintrag in der Frachttabelle: CHLO

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_4)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b8dcc8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Chloralkali Elektrolyseanlage](#industry_28) | [Arzneimittelfabrik](#industry_2) |
|  | [Arzneimittelfabrik](#industry_3) |
|  | [Arzneimittelfabrik](#industry_4) |
|  | [Arzneimittelfabrik](#industry_5) |
|  | [Arzneimittelfabrik](#industry_6) |
|  | [Arzneimittelfabrik](#industry_7) |
|  | [Arzneimittelfabrik](#industry_8) |
|  | [Arzneimittelfabrik](#industry_9) |
|  | [Kunststofffabrik](#industry_64) |
|  | [Kunststofffabrik](#industry_66) |
|  | [Kunststofffabrik](#industry_68) |
|  | [Kunststofffabrik](#industry_70) |
|  | [Papiermühle](#industry_94) |
|  | [Säurefabrik](#industry_104) |

<a name="cargo_IORE"></a>
### Eisenerz

Die Menschheit nutzt Eisen seit der, tja, Eisenzeit vor etwa 3000 Jahren. Heutzutage wird Eisenerz quasi ausschließlich zur Produktion von Stahl genutzt, der wiederum eines der wichtigsten Materialien in der Weltwirtschaft darstellt. 

Deutschland hatte niemals große Vorkommen von Eisenerz und war immer auf Importe zum Beispiel aus Schweden angewiesen. 

Eintrag in der Frachttabelle: IORE

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Eisenerzbergwerk](#industry_32) | [Farbenfabrik](#industry_35) |
| [Erzschmelze](#industry_33) | [Farbenfabrik](#industry_36) |
| [Erzschmelze](#industry_34) | [Farbenfabrik](#industry_37) |
| [Hafen](#industry_41) | [Farbenfabrik](#industry_38) |
| [Hafen](#industry_42) | [Integriertes Stahlwerk](#industry_51) |
| [Hafen](#industry_43) | [Integriertes Stahlwerk](#industry_52) |
| [Hafen](#industry_44) | [Integriertes Stahlwerk](#industry_53) |
| [Hafen](#industry_45) | [Integriertes Stahlwerk](#industry_54) |
| [Hafen](#industry_46) |  |
| [Hafen](#industry_47) |  |
| [Hafen](#industry_48) |  |

<a name="cargo_C2H4"></a>
### Ethylen

Ethylen, chemisch korrekt Ethen, ist ein leichter Kohlenwasserstoff, der mit über 100 Millionen Tonnen Jahresproduktion die meistproduzierte organische Grundchemikalie darstellt. Etwa die Hälfte davon wird in der Kunststoffproduktion benötigt. Großtechnisch wird Ethylen heutzutage hauptsächlich durch Steamcracking gewonnen. Andere technische Prozesse wie die Kohleverflüssigung oder Biogasanlagen kommen ebenso zur Anwendung. 

Während Ethylen in der Realität in verschiedenen Fällen durch Pipelines (z.B. zwischen Rotterdam/Antwerpen und Ludwigshafen oder auch zwischen Ludwigshafen und Ingolstadt) transportiert wird, muss der Spieler den Transport selbst sicherstellen. 

Eintrag in der Frachttabelle: C2H4

Teil der Erweiterung: [Organische Chemie](#extension_7)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#787840;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |

<a name="cargo_VEHI"></a>
### Fahrzeuge

Im weitesten Sinne sind Fahrzeuge selbstfahrende Landfahrzeuge zum Transport von Menschen und Gütern. In erster Linie sind damit natürlich Autos gemeint. 

Diese werden in Automobilfabriken gebaut und müssen nun in die Städte und zu den Exporthäfen transportiert werden. Autos sind eines der wichtigsten Exportgüter der deutschen Wirtschaft. Aus Sicht des Transports sind sie auch ein spezieller Fall, denn man braucht dafür besondere Eisenbahnwagen oder Lastwagen. 

Eintrag in der Frachttabelle: VEHI

Frachtklassen: Stückgut, Übergröße

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#bc546c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Autofabrik](#industry_10) | [Autohaus](#industry_18) |
| [Autofabrik](#industry_11) | [Hafen](#industry_41) |
| [Autofabrik](#industry_12) | [Hafen](#industry_42) |
| [Autofabrik](#industry_13) | [Hafen](#industry_43) |
| [Autofabrik](#industry_14) | [Hafen](#industry_44) |
| [Autofabrik](#industry_15) | [Hafen](#industry_45) |
| [Autofabrik](#industry_16) | [Hafen](#industry_46) |
| [Autofabrik](#industry_17) | [Hafen](#industry_47) |
|  | [Hafen](#industry_48) |

<a name="cargo_COAT"></a>
### Farbe

Farben sind so alt wie die Menschheit und wurden schon vor zehntausenden Jahren für Höhlenmalereien benutzt. Zahlreiche verschieden Farben sind seit dem Altertum bekannt. Oftmals waren diese aber sehr teuer, da sie aufwändig aus seltenen Pflanzen gewonnen wurden. Die chemische Industrie hat zahllose künstliche Verbindungen entwickelt, aus denen sich Farben und Färbemittel herstellen lassen, die wiederum vielfältige Anwendungen haben. So werden Farben und Lacke im Automobilbau verwendet, während Färbemittel eine große Rolle in der Textilindustrie spielen, um nur einige zu nennen. Farben werden auch im Haushalt eingesetzt, zum Beispiel zum Streichen der Wände, und Tinte zum Schreiben ist ebenfalls ein Produkt der Farbenindustrie. 

Eintrag in der Frachttabelle: COAT

Teil der Erweiterung: [Farbindustrie](#extension_2)

Frachtklassen: Flüssiggut, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#bc546c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Farbenfabrik](#industry_35) | [Autofabrik](#industry_12) |
| [Farbenfabrik](#industry_36) | [Autofabrik](#industry_13) |
| [Farbenfabrik](#industry_37) | [Autofabrik](#industry_16) |
| [Farbenfabrik](#industry_38) | [Autofabrik](#industry_17) |
|  | [Kunststofffabrik](#industry_65) |
|  | [Kunststofffabrik](#industry_66) |
|  | [Kunststofffabrik](#industry_69) |
|  | [Kunststofffabrik](#industry_70) |
|  | [Textilfabrik](#industry_107) |

<a name="cargo_FISH"></a>
### Fisch

Menschen haben schon seit jeher Fische gefangen. Im Spiel stellt es den Spieler vor interessante Transportaufgaben, da der Fisch im Hafen umgeladen werden muss. 

Eintrag in der Frachttabelle: FISH

Frachtklassen: Expressgut, Kühlfracht

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#8c68fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Fischgründe](#industry_39) | [Nahrungsmittelfabrik](#industry_86) |
|  | [Nahrungsmittelfabrik](#industry_87) |
|  | [Nahrungsmittelfabrik](#industry_88) |
|  | [Nahrungsmittelfabrik](#industry_89) |
|  | [Nahrungsmittelfabrik](#industry_90) |
|  | [Nahrungsmittelfabrik](#industry_91) |
|  | [Nahrungsmittelfabrik](#industry_92) |
|  | [Nahrungsmittelfabrik](#industry_93) |

<a name="cargo_GRAI"></a>
### Getreide

Deutschland ist bekannt für seine Vielfalt in Sachen Brot und Bier, und für beides braucht man Getreide. Deutschland ist einer der größten Getreideproduzenten Europas und kann den Bedarf vollständig selbst decken. Ein Großteil des Getreides wird als Tierfutter genutzt, nur ein Fünftel wird für in der Lebensmittelindustrie genutzt, und etwa 10% werden zum Bierbrauen gebraucht. Darüber hinaus wird viel Getreide, insbesondere Weizen, exportiert. 

Eintrag in der Frachttabelle: GRAI

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcfc00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bauernhof](#industry_19) | [Brauerei](#industry_26) |
| [Bauernhof](#industry_20) | [Brauerei](#industry_27) |
| [Bauernhof](#industry_21) | [Mühle](#industry_84) |
|  | [Mühle](#industry_85) |
|  | [Nahrungsmittelfabrik](#industry_86) |
|  | [Nahrungsmittelfabrik](#industry_87) |
|  | [Nahrungsmittelfabrik](#industry_90) |
|  | [Nahrungsmittelfabrik](#industry_92) |
|  | [Viehzucht](#industry_117) |

<a name="cargo_GLAS"></a>
### Glas

Glas ist der Sammelbegriff für eine Gruppe von Materialien mit speziellen physikalischen Eigenschaften. Die meisten Feststoffe haben eine geordnete molekulare Struktur, eine Art Raster wenn man so will. Glass hingegen hat eine ungeordnete Molekularstruktur, die man sonst nur bei Flüssigkeiten findet. Obwohl die dahinterliegende Physik bis heute nicht vollständig verstanden wurde, wurde Glass schon seit dem Altertum hergestellt. 

Üblicherweise meint man mit dem Wort Glas ein durchsichtiges Material aus Quarzsand. Glas ist chemisch gesehen extrem stabil, womit es sich prima als Material für Behälter für alle Arten von Flüssigkeiten, selbst Säuren, eignet. Tatsächlich ist Glas heutzutage omnipräsent. Man findet es als Fensterscheiben, in Form von Flaschen und Gläsern und natürlich in optischen Anwendungen als Linsen, Spiegel und natürlich als Brillenglas. 

Eintrag in der Frachttabelle: GLAS

Teil der Erweiterung: [Glas](#extension_3)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Glasfabrik](#industry_40) | [Autofabrik](#industry_14) |
|  | [Autofabrik](#industry_15) |
|  | [Autofabrik](#industry_16) |
|  | [Autofabrik](#industry_17) |
|  | [Brauerei](#industry_27) |
|  | [Verpackungsmittelfabrik](#industry_110) |
|  | [Verpackungsmittelfabrik](#industry_111) |
|  | [Verpackungsmittelfabrik](#industry_114) |
|  | [Verpackungsmittelfabrik](#industry_115) |

<a name="cargo_WOOD"></a>
### Holz

Holz wurde bereits von den ersten Menschen verwendet um Speere für die Jagd zu schnitzen oder um Feuer zu machen. Danach folgten Holzhütten, Schiffe, und irgendwann entwickelte man Papier aus Holzfasern. Heute ist Holz nach wie vor ein wichtiger Rohstoff und wird im 21. Jahrhundert wieder bedeutender, da es nachwächst. 

Deutschland ist reich an Wäldern, daher war Holz immer wirtschaftlich relevant. Heute ist Deutschland der größte Papierproduzent in Europa und hat auch eine bedeutsame Möbelindustrie 

Eintrag in der Frachttabelle: WOOD

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#74581c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Wald](#industry_118) | [Papiermühle](#industry_94) |
|  | [Sägewerk](#industry_102) |

<a name="cargo_LIME"></a>
### Kalkstein

Kalkstein besteht in erster Linie aus Kalkverbindungen. Er wird zur Herstellung von Zement benötigt, kann aber auch direkt als Baumaterial benutzt werden. Darüber hinaus ist Kalkstein ein wichtiger Rohstoff in der Chemieindustrie und wichtig in der Produktion von Stahl und Glas. 

Eintrag in der Frachttabelle: LIME

Teil der Erweiterung: [Bauindustrie](#extension_1)

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kalksteinbergwerk](#industry_57) | [Farbenfabrik](#industry_36) |
|  | [Farbenfabrik](#industry_38) |
|  | [Kalkbrennerei](#industry_55) |
|  | [Kalkbrennerei](#industry_56) |
|  | [Zementfabrik](#industry_119) |

<a name="cargo_COAL"></a>
### Kohle

Kohle war der wichtigste Faktor der industriellen Revolution des 19. Jahrhunderts, da es für den Antrieb von Dampfmaschinen gebraucht wird. Mit der Entwicklung von Eisenbahnen und Dampfschiffen und später Kraftwerken stieg der Bedarf an Kohle immer weiter. 

Deutschland hatte in mehreren Gebieten große Kohlevorkommen, diese Gebiete wie eben das Ruhrgebiet oder Schlesien wurden in der Folge Zentren der Industrialisierung. Kohle blieb während des gesamten 20. Jahrhunderts wichtig, wurde aber aus Gründen des Umweltschutzes nach und nach aus verschiedenen Bereichen verdrängt. 

Eintrag in der Frachttabelle: COAL

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_41) | [Hydrierwerk](#industry_50) |
| [Hafen](#industry_42) | [Integriertes Stahlwerk](#industry_51) |
| [Hafen](#industry_43) | [Integriertes Stahlwerk](#industry_52) |
| [Hafen](#industry_44) | [Kokerei](#industry_60) |
| [Hafen](#industry_45) | [Kraftwerk](#industry_61) |
| [Hafen](#industry_46) | [Kraftwerk](#industry_62) |
| [Hafen](#industry_47) | [Rußfabrik](#industry_95) |
| [Hafen](#industry_48) | [Rußfabrik](#industry_96) |
| [Kohlebergwerk](#industry_59) | [Ziegelei](#industry_120) |

<a name="cargo_COKE"></a>
### Koks

Koks ist hochreiner Kohlenstoff, der durch Pyrolyse aus Kohle gewonnen wird. Dabei wird die Kohle unter Sauerstoffabschluss großer Wärme ausgesetzt, wodurch die Kohle nicht verbrennen kann. Dabei werden diverse Verunreinigungen wie Schwefel und verschiedene Kohlenwasserstoffe abgeschieden. Koks wurde erstmals Anfang des 18. Jahrhunderts in England produziert und löste im 19. Jahrhundert die bisher verwendete Holzkohle als Befeuerung von Hochöfen ab. Erst damit war eine effiziente Eisenproduktion im Hochofen in großem Maßstab möglich. 

Eintrag in der Frachttabelle: COKE

Teil der Erweiterung: [Koks und Schwefel](#extension_5)

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kokerei](#industry_60) | [Erzschmelze](#industry_33) |
|  | [Erzschmelze](#industry_34) |
|  | [Integriertes Stahlwerk](#industry_53) |
|  | [Integriertes Stahlwerk](#industry_54) |
|  | [Kalkbrennerei](#industry_56) |

<a name="cargo_PLAS"></a>
### Kunststoffe

Kunststoffe umfassen eine ganze Reihe von synthetischen Materialien, die hauptsächlich aus Öl hergestellt werden. Sie wurden im frühen 20. Jahrhundert entwickelt und boten billige, leichte und haltbare Materialien für quasi jeden vorstellbaren Zweck. Der Großteil wird für Verpackungen benutzt, es gibt aber auch Verwendungen im Bauwesen (Rohrleitungen), in allen Arten von technischen Geräten wie Staubsaugern, aber auch im Möbelbau und als Spielzeug - als Legobaustein zum Beispiel. 

Im Set umfassen Kunststoffe nicht nur synthetische Materialien mit den namensgebenden plastischen Eigenschaften, sondern auch Kunstfasern wie Nylon und Polyester, die in der Textilindustrie relevant sind. 

Eintrag in der Frachttabelle: PLAS

Frachtklassen: Nässeempfindlich, Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kunststofffabrik](#industry_63) | [Autofabrik](#industry_10) |
| [Kunststofffabrik](#industry_64) | [Autofabrik](#industry_11) |
| [Kunststofffabrik](#industry_65) | [Autofabrik](#industry_12) |
| [Kunststofffabrik](#industry_66) | [Autofabrik](#industry_13) |
| [Kunststofffabrik](#industry_67) | [Autofabrik](#industry_14) |
| [Kunststofffabrik](#industry_68) | [Autofabrik](#industry_15) |
| [Kunststofffabrik](#industry_69) | [Autofabrik](#industry_16) |
| [Kunststofffabrik](#industry_70) | [Autofabrik](#industry_17) |
|  | [Möbelfabrik](#industry_80) |
|  | [Möbelfabrik](#industry_81) |
|  | [Möbelfabrik](#industry_82) |
|  | [Möbelfabrik](#industry_83) |
|  | [Textilfabrik](#industry_106) |
|  | [Textilfabrik](#industry_107) |
|  | [Verpackungsmittelfabrik](#industry_108) |
|  | [Verpackungsmittelfabrik](#industry_109) |
|  | [Verpackungsmittelfabrik](#industry_110) |
|  | [Verpackungsmittelfabrik](#industry_111) |
|  | [Verpackungsmittelfabrik](#industry_112) |
|  | [Verpackungsmittelfabrik](#industry_113) |
|  | [Verpackungsmittelfabrik](#industry_114) |
|  | [Verpackungsmittelfabrik](#industry_115) |

<a name="cargo_COPR"></a>
### Kupfer

Kupfer ist ein Metall, welches seit dem Altertum bekannt ist und zu den ersten von Menschen verwendeten Metallen gehört. Es ist leicht zu verarbeiten und hat zahlreiche Anwendungen. Heutzutage wird es hauptsächlich für Kabel und Drähte und alle Arten von elektrischen Bauteilen benutzt. In der Vergangenheit wurde es auch zur Herstellung von Farben und als Material für Dächer benutzt. 

Eintrag in der Frachttabelle: COPR

Teil der Erweiterung: [Farbindustrie](#extension_2)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kupferhütte](#industry_73) | [Farbenfabrik](#industry_35) |
| [Kupferhütte](#industry_74) | [Farbenfabrik](#industry_36) |
|  | [Farbenfabrik](#industry_37) |
|  | [Farbenfabrik](#industry_38) |

<a name="cargo_CORE"></a>
### Kupfererz

Kupfererze kommen in verschiedenen Formen vor, die sich unterschiedlich gut zur Herstellung von Kupfer eignen. Der Abbau von Kupfererzen kann tausende von Jahren bis in die sogenannte Kupferzeit zurückverfolgt werden. Heutzutage ist Kupfererz von ein wichtiger Rohstoff, da Kupfer eines der wichtigsten Metalle für industrielle Zwecke ist. 

Deutschland hat keine bedeutsamen Vorkommen von Kupfererzen, allerdings wurden diese noch bis ins späte 20. Jahrhundert vorwiegend in Ostdeutschland abgebaut, weil man dort keinen Zugang zum Weltmarkt hatte. Allerdings hat Deutschland heute große Kapazitäten zur Produktion von Kupfer und ist ein großer Importeur von entsprechenden Erzen. 

Eintrag in der Frachttabelle: CORE

Teil der Erweiterung: [Farbindustrie](#extension_2)

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Erzschmelze](#industry_34) | [Kupferhütte](#industry_73) |
| [Hafen](#industry_43) | [Kupferhütte](#industry_74) |
| [Hafen](#industry_44) |  |
| [Kupfererzbergwerk](#industry_71) |  |

<a name="cargo_PORE"></a>
### Kupferkies

Kupfer kommt in der Natur quasi nur in Verbindungen mit anderen Stoffen vor. Eine häufige Verbindung ist das Mineral Chalkopyrit, auch als Kupferkies bezeichnet. Das ist eine Verbindung aus Kupfer, Eisen und Schwefel. Es ist aufgrund seines häufigen Vorkommens eines der wirtschaftlich bedeutsamsten Mineralien für die Produktion von Kupfer. 

Eintrag in der Frachttabelle: PORE

Teil der Erweiterung: [Koks und Schwefel](#extension_5)

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcf880;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_45) | [Erzschmelze](#industry_33) |
| [Hafen](#industry_46) | [Erzschmelze](#industry_34) |
| [Hafen](#industry_47) |  |
| [Hafen](#industry_48) |  |
| [Kupfererzbergwerk](#industry_72) |  |

<a name="cargo_MILK"></a>
### Milch

Milch von Kühen und anderen Tieren wird seit Jahrtausenden als Nahrungsmittel genutzt. Sie wird nicht nur getrunken, sondern ist auch die Basis für die Herstellung anderer Lebensmettel wie Käse, Butter, Joghurt oder Eiscreme. 

Eintrag in der Frachttabelle: MILK

Teil der Erweiterung: [Lebensmittelindustrie](#extension_6)

Frachtklassen: Expressgut, Flüssiggut, Kühlfracht

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#e0f4fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Viehzucht](#industry_116) | [Molkerei](#industry_76) |
| [Viehzucht](#industry_117) | [Molkerei](#industry_77) |
|  | [Molkerei](#industry_78) |
|  | [Molkerei](#industry_79) |

<a name="cargo_FOOD"></a>
### Nahrungsmittel

Jeder muss essen, und seitdem Menschen in Städten leben gab den Bedarf, Lebensmittel in die Städte zu transportieren. Selbst heute noch kann man frisches Obst und Gemüse auf dem Wochenmarkt kaufen, während der Großteil der industriell produzierten Lebensmittel von den Fabriken zu Supermärkten transportiert wird. 

Eintrag in der Frachttabelle: FOOD

Frachtklassen: Expressgut, Kühlfracht

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Brauerei](#industry_26) | [Hotel](#industry_49) |
| [Brauerei](#industry_27) | [Laden](#industry_75) |
| [Molkerei](#industry_76) |  |
| [Molkerei](#industry_77) |  |
| [Molkerei](#industry_78) |  |
| [Molkerei](#industry_79) |  |
| [Mühle](#industry_84) |  |
| [Mühle](#industry_85) |  |
| [Nahrungsmittelfabrik](#industry_86) |  |
| [Nahrungsmittelfabrik](#industry_87) |  |
| [Nahrungsmittelfabrik](#industry_88) |  |
| [Nahrungsmittelfabrik](#industry_89) |  |
| [Nahrungsmittelfabrik](#industry_90) |  |
| [Nahrungsmittelfabrik](#industry_91) |  |
| [Nahrungsmittelfabrik](#industry_92) |  |
| [Nahrungsmittelfabrik](#industry_93) |  |
| [Schlachthof](#industry_99) |  |
| [Schlachthof](#industry_100) |  |

<a name="cargo_RFPR"></a>
### Naphtha

Naphtha, auch Rohbenzin genannt, ist ein Produkt aus der Destillation von Erdöl, wie es in Raffinerien stattfindet. Es enthält eine Vielzahl verschiedener Kohlenwasserstoffe, die in weiteren Schritten voneinander getrennt werden. Somit ist es in der chemischen Industrie ein unverzichtbares Zwischenprodukt bei der Herstellung von Kraft- und Schmierstoffen, aber auch bei der Herstellung von Ethylen. 

Eintrag in der Frachttabelle: RFPR

Teil der Erweiterung: [Organische Chemie](#extension_7)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#403c0c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Ölraffinerie](#industry_123) | [Arzneimittelfabrik](#industry_4) |
| [Ölraffinerie](#industry_124) | [Arzneimittelfabrik](#industry_5) |
|  | [Arzneimittelfabrik](#industry_8) |
|  | [Arzneimittelfabrik](#industry_9) |
|  | [Dampfreformierer](#industry_29) |
|  | [Rußfabrik](#industry_96) |
|  | [Steamcracker](#industry_101) |

<a name="cargo_LYE_"></a>
### Natronlauge

Natronlauge ist eine basische Lösung. Sie hat eine große Bedeutung in der Produktion von Waschmitteln und Seifen, aber auch in der Lebensmittelindustrie und in anderen Bereichen. Ein Großteil der Natronlauge wird in der Papierherstellung benötigt, darüber hinaus findet es Anwendung in der Produktion von Färbemitteln und Bleichmachern. Natronlauge wird zusammen mit Chlor aus der elektrolytischen Spaltung von Salzlösungen im sogenannten Chlor-Alkali-Prozess gewonnen. 

Eintrag in der Frachttabelle: LYE_

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_4)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#78a488;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Chloralkali Elektrolyseanlage](#industry_28) | [Aluhütte](#industry_1) |
|  | [Molkerei](#industry_77) |
|  | [Molkerei](#industry_79) |
|  | [Nahrungsmittelfabrik](#industry_87) |
|  | [Nahrungsmittelfabrik](#industry_89) |
|  | [Nahrungsmittelfabrik](#industry_92) |
|  | [Nahrungsmittelfabrik](#industry_93) |
|  | [Papiermühle](#industry_94) |

<a name="cargo_PAPR"></a>
### Papier

Papier besteht aus getrockneten Zellulosefasern und ist seit dem Altertum bekannt. Damals schrieb man bereits auf Papyrus. Es dauerte jedoch bis zum 19. Jahrhundert, um dank der Fortschritte der chemischen Forschung zu verstehen, wie man Zellulose aus Holzfasern gewinnen kann. Dies erlaubte eine industrielle Massenfertigung von allen möglichen Papiersorten. Heute ist Papier omnipräsent, vom hochwertigem Briefpaper über das weitverbreitete Papier für den Drucker im Büro, dünneres Papier für Zeitungsdruck, stabilere Pappe für Verpackungen bis hin zu Toilettenpapier. 

Eintrag in der Frachttabelle: PAPR

Teil der Erweiterung: [Papier](#extension_8)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b8b8b8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Papiermühle](#industry_94) | [Druckerei](#industry_30) |
|  | [Druckerei](#industry_31) |
|  | [Verpackungsmittelfabrik](#industry_112) |
|  | [Verpackungsmittelfabrik](#industry_113) |
|  | [Verpackungsmittelfabrik](#industry_114) |
|  | [Verpackungsmittelfabrik](#industry_115) |

<a name="cargo_PASS"></a>
### Passagiere

Ob es nun Urlaub oder Dienstreise ist - Menschen müssen und wollen verreisen. Jahrhundertelang hieß Reisen Laufen oder Reiten, technische Innovationen beschleunigten das Reisen jedoch erheblich. Man baute Häfen, Straßen und später Eisenbahnen und schließlich Flughäfen. Das Reisen wurde nicht nur schneller, sondern auch preiswerter - und heutzutage sind Reisen möglich, die vor noch gar nicht langer Zeit völlig undenkbar waren. 

Eintrag in der Frachttabelle: PASS

Frachtklassen: Passagiere

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#80c4fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hotel](#industry_49) | [Hotel](#industry_49) |
| [Ölbohrinsel](#industry_121) | [Ölbohrinsel](#industry_121) |

<a name="cargo_MAIL"></a>
### Post

Der Transport von Post war schon immer eine wichtige Aufgabe eines jeden Verkehrsnetzes. Jahrhunderte lang waren Postkutschen im Einsatz, bevor sie von Eisenbahnen und Lastwagen verdrängt wurden. Während die Anzahl der transportierten Briefe und Postkarten im 21. Jahrhundert zurückgeht - man schickt Nachrichten übers Internet - ist der Transport von Paketen heutzutage wichtiger denn je, Onlineshopping sei Dank. 

Eintrag in der Frachttabelle: MAIL

Frachtklassen: Post

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcfcfc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |

<a name="cargo_CBLK"></a>
### Ruß

Ruß ist ein Pulver von praktisch reinem Kohlenstoff. Es wird als schwarzes Pigment für Farben, Tinten und in der Kunststoffherstellung benutzt. Haupteinsatzgebiet ist jedoch die Reifenherstellung für den Automobilbau. 

Eintrag in der Frachttabelle: CBLK

Teil der Erweiterung: [Farbindustrie](#extension_2)

Frachtklassen: Nässeempfindlich, Pulver, Schüttgut, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#343c48;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Rußfabrik](#industry_95) | [Farbenfabrik](#industry_35) |
| [Rußfabrik](#industry_96) | [Farbenfabrik](#industry_36) |
|  | [Farbenfabrik](#industry_37) |
|  | [Farbenfabrik](#industry_38) |

<a name="cargo_SALT"></a>
### Salz

Salz wird seit dem Altertum verwendet, um Nahrungsmittel haltbar zu machen. Bis ins ausgehende Mittelalter wurde Salz als weißes Gold gehandelt und spielte eine entscheidende Rolle im Bereich Handel, Steuerrecht und Wirtschaft im Allgemeinen. Das veränderte sich erst, als Salzbergbau im 19. Jahrhundert technisch möglich und praktikabel wurde. Darüber hinaus wurde Salz durch Fortschritte in der Wissenschaft und Chemie zu dieser Zeit ein grundlegender Rohstoff in der Produktion von Chlor, Natronlauge und Soda, die wiederum zu den wichtigsten Rohstoffen in der chemischen Industrie zählen. Heutzutage werden etwa 80% des in Deutschland geförderten Salzes für industrielle Zwecke genutzt, weniger als 5% werden in der Lebensmittelindustrie eingesetzt. 

Eintrag in der Frachttabelle: SALT

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_4)

Frachtklassen: Nässeempfindlich, Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#d4d4e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Salzbergwerk](#industry_97) | [Chloralkali Elektrolyseanlage](#industry_28) |
|  | [Nahrungsmittelfabrik](#industry_87) |
|  | [Nahrungsmittelfabrik](#industry_89) |
|  | [Nahrungsmittelfabrik](#industry_92) |
|  | [Nahrungsmittelfabrik](#industry_93) |

<a name="cargo_SAND"></a>
### Sand

Sand findet man quasi überall in der Welt. Er besteht hauptsächlich aus Silikatverbindugnen in Partikeln unterschiedlicher Größe. Sand wird maßgeblich in der Bauindustrie benötigt, zum Beispiel bei der Herstellung von Mörtel und Beton, aber auch als Quelle für Silizium, welches wiederum wichtig für elektronische Bauteile ist. 

Eintrag in der Frachttabelle: SAND

Frachtklassen: Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#e8b810;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Sandgrube](#industry_98) | [Bauhof](#industry_22) |
|  | [Glasfabrik](#industry_40) |
|  | [Zementfabrik](#industry_119) |

<a name="cargo_WDPR"></a>
### Schnittholz

Holz in Form von Bäumen kann nicht direkt industriell verwendet werden. Es muss in verschiedene Formen geschnitten werden, so dass es im Bauwesen oder in der Möbelindustrie benutzt werden kann. Im Set bezeichnet Schnittholz alle Arten von vorverarbeitetem Holz in Form von Balken oder Brettern. 

Eintrag in der Frachttabelle: WDPR

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b09c6c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Sägewerk](#industry_102) | [Bauhof](#industry_22) |
|  | [Bauhof](#industry_23) |
|  | [Möbelfabrik](#industry_80) |
|  | [Möbelfabrik](#industry_81) |
|  | [Möbelfabrik](#industry_82) |
|  | [Möbelfabrik](#industry_83) |

<a name="cargo_SULP"></a>
### Schwefel

Schwefel ist bereits seit dem Altertum bekannt. Schon in der Antike wurde es als Brandwaffe verwendet, aber auch zur Desinfektion und zum Schwefeln von Wein. Schwefel ist Teil von Schwarzpulver und spielte ein große Rolle in der Alchemie. Im frühen 19. Jahrhundert wurde mit dem Fortschreiten der Wissenschaft schließlich erkannt, dass Schwefel ein chemisches Element ist. Schwefel ist - wenig überraschend - in Schwefelsäure enthalten, die zahllose Anwendungen in der Industrie hat. Elementarer Schwefel wird heute hauptsächlich für die Vulkanisierung von Kautschuk im Zusammenhang mit der Reifenproduktion verwendet. 

Eintrag in der Frachttabelle: SULP

Teil der Erweiterung: [Koks und Schwefel](#extension_5)

Frachtklassen: Flüssiggut, Nässeempfindlich, Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcd400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Erzschmelze](#industry_33) | [Säurefabrik](#industry_103) |
| [Erzschmelze](#industry_34) | [Säurefabrik](#industry_104) |
| [Kokerei](#industry_60) |  |
| [Kraftwerk](#industry_62) |  |
| [Ölraffinerie](#industry_124) |  |

<a name="cargo_STEL"></a>
### Stahl

Stahl, eine Verbindung aus Eisen und Kohlenstoff, wurde bereits vor über 2000 Jahren in Asien hergestellt. Im 16. und 17. Jahrhundert begann die industrielle Stahlproduktion in Europe, in erster Linie in England. Technische Verbesserungen im 19. Jahrhundert führten schließlich zur billigen Massenproduktion von hochwertigem Stahl. Gleichzeitig stieg der Bedarf exponentiell an, da Stahl für Eisenbahnen gebraucht wurde, Holz als Hauptwerkstoff im Schiffbau ersetzt und natürlich zum Bau von Gebäuden, Brücken und zahllosen anderen Strukturen benötigt wurde. 

Das erste Stahlwerk Deutschlands wurde im frühen 19. Jahrhundert in Essen im Ruhrgebiet gebaut. Aus diesem ging später der Krupp-Konzern hervor. Heute ist Deutschland mit Abstand der größte Stahlproduzent in Europa. 

Eintrag in der Frachttabelle: STEL

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#a8a8a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Integriertes Stahlwerk](#industry_51) | [Autofabrik](#industry_10) |
| [Integriertes Stahlwerk](#industry_52) | [Autofabrik](#industry_11) |
| [Integriertes Stahlwerk](#industry_53) | [Autofabrik](#industry_12) |
| [Integriertes Stahlwerk](#industry_54) | [Autofabrik](#industry_13) |
|  | [Autofabrik](#industry_14) |
|  | [Autofabrik](#industry_15) |
|  | [Autofabrik](#industry_16) |
|  | [Autofabrik](#industry_17) |

<a name="cargo_ACID"></a>
### Säure

Säuren sind eine Klasse von chemischen Verbindungen, die sich in erster Linie dadurch auszeichen, dass sie andere chemische Verbindungen angreifen und zerstören können. Das bedeutet auch, dass sie für den Menschen gefährlich und ggfs. tödlich giftig sein können. So wurde Chlor als Giftgas eingesetzt, welches beim Einatmen zu Salzsäure umgesetzt wird, die die Lunge verätzt. Die starke Ätzwirkung ist in der Industrie jedoch in zahllosen Anwendungen notwendig, zum Beispiel bei der Herstellung von Düngemitteln, Farbstoffen und beim Auflösen von Erzen in der Metallproduktion. Die wichtigste Säure für industrielle Anwendungen ist Schwefelsäure, aber im täglichen Gebrauch trifft man zum Beispiel aber auch Kohlensäure (in diversen Getränken und Mineralwasser) an. 

Eintrag in der Frachttabelle: ACID

Teil der Erweiterung: [Koks und Schwefel](#extension_5)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Säurefabrik](#industry_103) | [Arzneimittelfabrik](#industry_6) |
| [Säurefabrik](#industry_104) | [Arzneimittelfabrik](#industry_7) |
|  | [Arzneimittelfabrik](#industry_8) |
|  | [Arzneimittelfabrik](#industry_9) |
|  | [Farbenfabrik](#industry_37) |
|  | [Farbenfabrik](#industry_38) |
|  | [Kupferhütte](#industry_74) |

<a name="cargo_TEXT"></a>
### Textilien

Textilien sind ein Oberbegriff für alle Arten von faserbasierten Materialien wie Garn, Fäden und Stoffe. Sie werden hauptsächlich zur Produktion von Kleidung verwendet, spielen aber auch bei der Herstellung von Vorhängen, Teppichen und anderen Haushaltsgegenständen eine Rolle. Darüber hinaus gibt es einen großen Bereich industrieller Textilien, wie zum Beispiel für Sicherheitsgurte oder für medizinische Verbände, um nur einige zu nennen. Im Set werden Textilien als Rohstoff für verschiedene andere Industrien eingesetzt. 

Eintrag in der Frachttabelle: TEXT

Teil der Erweiterung: [Textilindustrie](#extension_9)

Frachtklassen: Nässeempfindlich, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#803828;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Textilfabrik](#industry_106) | [Bekleidungsfabrik](#industry_24) |
| [Textilfabrik](#industry_107) | [Bekleidungsfabrik](#industry_25) |
|  | [Möbelfabrik](#industry_80) |
|  | [Möbelfabrik](#industry_82) |

<a name="cargo_PETR"></a>
### Treibstoff

Treibstoff ist im Set der Oberbegriff für alles ist, was man zum Betreiben von Kraftfahrzeugen, Flugzeugen und sonstigen Maschinen benötigt. Hergestellt werden Treibstoffe üblicherweise aus Erdöl, wobei alternative Herstellungsmethoden z.B. aus Biomasse im 21. Jahrhundert an Bedeutung gewinnen. Somit hängt die gesamte Wirtschaft und insbesondere der Transportsektor maßgeblich von der Verfügbarkeit von Erdöl ab. 

Eintrag in der Frachttabelle: PETR

Teil der Erweiterung: [Organische Chemie](#extension_7)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#cccca8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hydrierwerk](#industry_50) | [Tankstelle](#industry_105) |
| [Steamcracker](#industry_101) |  |
| [Ölraffinerie](#industry_123) |  |
| [Ölraffinerie](#industry_124) |  |

<a name="cargo_MNSP"></a>
### Verpackungen

Verpackungen sind ein notwendiges Übel für viele Waren und Lebensmittel. Sie schützen beim Transport, erzeugen aber am Ende auch viel Müll. Im Set sind Verpackungen in erster Linie ein zusätzlicher Baustein für mehr Komplexität in den Transportketten. 

Eintrag in der Frachttabelle: MNSP

Teil der Erweiterung: [Verpackungsmittelindustrie](#extension_10)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b87818;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Verpackungsmittelfabrik](#industry_108) | [Arzneimittelfabrik](#industry_3) |
| [Verpackungsmittelfabrik](#industry_109) | [Arzneimittelfabrik](#industry_5) |
| [Verpackungsmittelfabrik](#industry_110) | [Arzneimittelfabrik](#industry_7) |
| [Verpackungsmittelfabrik](#industry_111) | [Arzneimittelfabrik](#industry_9) |
| [Verpackungsmittelfabrik](#industry_112) | [Bekleidungsfabrik](#industry_25) |
| [Verpackungsmittelfabrik](#industry_113) | [Druckerei](#industry_31) |
| [Verpackungsmittelfabrik](#industry_114) | [Molkerei](#industry_78) |
| [Verpackungsmittelfabrik](#industry_115) | [Molkerei](#industry_79) |
|  | [Möbelfabrik](#industry_82) |
|  | [Möbelfabrik](#industry_83) |
|  | [Mühle](#industry_85) |
|  | [Nahrungsmittelfabrik](#industry_90) |
|  | [Nahrungsmittelfabrik](#industry_91) |
|  | [Nahrungsmittelfabrik](#industry_92) |
|  | [Nahrungsmittelfabrik](#industry_93) |
|  | [Schlachthof](#industry_100) |

<a name="cargo_LVST"></a>
### Vieh

Fleisch war und ist ein wichtiger Teil der menschlichen Nahrung, und dementsprechend ist die Viehhaltung ein wichtiger Teil der Lebensmittelindustrie. Der Transport von Vieh ist auch eine spezielle Herausforderung im Spiel, da man dafür oftmals spezialisierte Fahrzeuge benötigt. 

Eintrag in der Frachttabelle: LVST

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#5c9c34;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bauernhof](#industry_19) | [Nahrungsmittelfabrik](#industry_86) |
| [Bauernhof](#industry_20) | [Nahrungsmittelfabrik](#industry_87) |
| [Viehzucht](#industry_116) | [Nahrungsmittelfabrik](#industry_90) |
| [Viehzucht](#industry_117) | [Nahrungsmittelfabrik](#industry_92) |
|  | [Schlachthof](#industry_99) |
|  | [Schlachthof](#industry_100) |

<a name="cargo_GOOD"></a>
### Waren

Im Spiel stellen Waren eine Abstraktion für praktisch alles dar, was in Fabriken produziert und in Städten verkauft wird. Das können also Möbel, Haushaltsgegenstände, Kleidung oder Spielzeuge sein. 

Eintrag in der Frachttabelle: GOOD

Frachtklassen: Expressgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Arzneimittelfabrik](#industry_2) | [Hafen](#industry_41) |
| [Arzneimittelfabrik](#industry_3) | [Hafen](#industry_42) |
| [Arzneimittelfabrik](#industry_4) | [Hafen](#industry_43) |
| [Arzneimittelfabrik](#industry_5) | [Hafen](#industry_44) |
| [Arzneimittelfabrik](#industry_6) | [Hafen](#industry_45) |
| [Arzneimittelfabrik](#industry_7) | [Hafen](#industry_46) |
| [Arzneimittelfabrik](#industry_8) | [Hafen](#industry_47) |
| [Arzneimittelfabrik](#industry_9) | [Hafen](#industry_48) |
| [Bekleidungsfabrik](#industry_24) | [Kaufhaus](#industry_58) |
| [Bekleidungsfabrik](#industry_25) |  |
| [Druckerei](#industry_30) |  |
| [Druckerei](#industry_31) |  |
| [Möbelfabrik](#industry_80) |  |
| [Möbelfabrik](#industry_81) |  |
| [Möbelfabrik](#industry_82) |  |
| [Möbelfabrik](#industry_83) |  |

<a name="cargo_H2__"></a>
### Wasserstoff

Wasserstoff ist das simpelste und häufigste chemische Element im Universum. Auf der Erde findet man es hauptsächlich in Verbindungen, in erster Linie in Form von Wasser und in Kohlenwasserstoffen wie Öl. Wasserstoff hat zahlreiche Anwendungen in der chemischen Industrie, hauptsächlich bei der Herstellung von Ammoniak. Darüber hinaus wird es als Raketentreibstoff verwendet, aber auch als Kühlmittel. 

Eintrag in der Frachttabelle: H2__

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_4)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#ccd0dc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |

<a name="cargo_WOOL"></a>
### Wolle

Wolle ist eine Textilfaser, die hauptsächlich von Schafen gewonnen wird und zu Garn und weiter zu Textilien verarbeitet wird. 

Eintrag in der Frachttabelle: WOOL

Teil der Erweiterung: [Textilindustrie](#extension_9)

Frachtklassen: Nässeempfindlich, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#a85c4c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bauernhof](#industry_19) | [Textilfabrik](#industry_106) |
| [Viehzucht](#industry_117) | [Textilfabrik](#industry_107) |

<a name="cargo_CMNT"></a>
### Zement

Zement ist ein wesentlicher Bestandteil bei der Herstellung von Mörtel und Beton, die zu den wichtigsten und weitverbreitetsten Resourcen der Welt gehören. Ohne sie könnten keine Wolkenkratzer gebaut werden. 

Eintrag in der Frachttabelle: CMNT

Teil der Erweiterung: [Bauindustrie](#extension_1)

Frachtklassen: Nässeempfindlich, Pulver, Schüttgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#6c7484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Zementfabrik](#industry_119) | [Bauhof](#industry_22) |

<a name="cargo_BDMT"></a>
### Ziegel

Ziegel wurden seit dem Altertum für den Bau von Gebäuden genutzt. Im Zuge der Industrialisierung wuchs der Bedarf nach preiswerten Ziegeln sprunghaft, um daraus Fabrikhallen und Brücken zu bauen. Noch heute sind Ziegelsteine relevant, obwohl man sie aus statischen Gründen nicht für den Bau von Wolkenkratzern nutzen kann. 

Eintrag in der Frachttabelle: BDMT

Teil der Erweiterung: [Bauindustrie](#extension_1)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#cc8060;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Ziegelei](#industry_120) | [Bauhof](#industry_22) |

<a name="cargo_OIL_"></a>
### Öl

Öl war bereits im alten Babylon bekannt. Im 19. Jahrhundert wurde es hauptsächlich verwendet um Petroleum zu erzeugen, welches wiederum als Lampenöl Verwendung fand. Erst mit der Entwicklung von Verbrennungsmotoren und ihrer Abhängigkeit von Treibstoff wurde Erdöl zu dem wirtschaftlichen und politischen Faktor, der es heute ist. 

Neben der simplen Verbrennung als Treibstoff ist Öl natürlich die Basis für das, was heute als Petrochemie bekannt ist. Das begann in den 1920er Jahren mit synthetischem Kautschuk für Reifen, in den späten 30er Jahren wurden Nylonfasern entwickelt, und heutzutage findet man ölbasierte Kunststoffe quasi überall. 

Aufgrund der zahllosen Anwendungsmöglichkeiten stieg der Bedarf immer weiter, und heute hängen weite Teile der deutschen Industrie direkt oder indirekt von Erdölimporten ab, was nicht nur ein wirtschaftlicher Faktor ist, sondern auch politische Relevanz hat. 

Eintrag in der Frachttabelle: OIL_

Frachtklassen: Flüssiggut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_41) | [Kraftwerk](#industry_61) |
| [Hafen](#industry_42) | [Kraftwerk](#industry_62) |
| [Hafen](#industry_43) | [Kunststofffabrik](#industry_63) |
| [Hafen](#industry_44) | [Kunststofffabrik](#industry_64) |
| [Hafen](#industry_45) | [Kunststofffabrik](#industry_65) |
| [Hafen](#industry_46) | [Kunststofffabrik](#industry_66) |
| [Hafen](#industry_47) | [Rußfabrik](#industry_95) |
| [Hafen](#industry_48) | [Ölraffinerie](#industry_123) |
| [Ölbohrinsel](#industry_121) | [Ölraffinerie](#industry_124) |
| [Ölquellen](#industry_122) |  |


## Industries

<a name="industry_0"></a>
### Aluhütte

<img src="aluminium_plant.png" alt="Aluhütte">

Die Aluminiumhütte erzeugt Aluminium aus Bauxit, einem Aluminiumerz. Der Prozess besteht aus zwei Schritten, im ersten wird das Bauxit in einem chemischen Prozess aufgespalten um Verunreinigungen zu entfernen bevor es zu Aluminiumoxid umgewandelt wird. Der zweite Schritte besteht aus der Aufspaltung des Aluminiumoxids durch Elektrolyse. Das erfordert sehr viel elektrischen Strom und erzeugt große Mengen an Kohlendioxid. Damit ist die Produktion eigentlich nur in Gebieten sinnvoll, wo billiger Strom verfügbar ist. 

In Deutschland ist nur eine Firma verblieben, die Aluminium herstellt. Sie betreibt drei Anlagen, die Aluminium hauptsächlich aus Metallschrott recyceln. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Bauxit](#cargo_AORE) | [Aluminium](#cargo_ALUM) |


<a name="industry_1"></a>
### Aluhütte

<img src="aluminium_plant.png" alt="Aluhütte">

Die Aluminiumhütte erzeugt Aluminium aus Bauxit, einem Aluminiumerz. Der Prozess besteht aus zwei Schritten, im ersten wird das Bauxit in einem chemischen Prozess aufgespalten um Verunreinigungen zu entfernen bevor es zu Aluminiumoxid umgewandelt wird. Der zweite Schritte besteht aus der Aufspaltung des Aluminiumoxids durch Elektrolyse. Das erfordert sehr viel elektrischen Strom und erzeugt große Mengen an Kohlendioxid. Damit ist die Produktion eigentlich nur in Gebieten sinnvoll, wo billiger Strom verfügbar ist. 

In Deutschland ist nur eine Firma verblieben, die Aluminium herstellt. Sie betreibt drei Anlagen, die Aluminium hauptsächlich aus Metallschrott recyceln. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Grundlegende Anorganische Chemie](#extension_4) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Bauxit](#cargo_AORE) | [Aluminium](#cargo_ALUM) |
| [Natronlauge](#cargo_LYE_) |  |


<a name="industry_2"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) [Organische Chemie](#extension_7) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |


<a name="industry_3"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_7) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_4"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Organische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_5"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) [Organische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |
| [Verpackungen](#cargo_MNSP) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_6"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) [Organische Chemie](#extension_7) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |


<a name="industry_7"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_7) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_8"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Organische Chemie](#extension_7) [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_9"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) [Organische Chemie](#extension_7) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_10"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_2) [Glas](#extension_3) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Fahrzeuge](#cargo_VEHI) |
| [Stahl](#cargo_STEL) |  |


<a name="industry_11"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) [Glas](#extension_3) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Fahrzeuge](#cargo_VEHI) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_12"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Glas](#extension_3) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Fahrzeuge](#cargo_VEHI) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_13"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_3) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Fahrzeuge](#cargo_VEHI) |
| [Farbe](#cargo_COAT) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_14"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Glas](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Fahrzeuge](#cargo_VEHI) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_15"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Glas](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Fahrzeuge](#cargo_VEHI) |
| [Glas](#cargo_GLAS) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_16"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Glas](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Fahrzeuge](#cargo_VEHI) |
| [Glas](#cargo_GLAS) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_17"></a>
### Autofabrik

<img src="vehicle_factory.png" alt="Autofabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_2) [Glas](#extension_3) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Fahrzeuge](#cargo_VEHI) |
| [Farbe](#cargo_COAT) |  |
| [Glas](#cargo_GLAS) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_18"></a>
### Autohaus

<img src="vehicle_distributor.png" alt="Autohaus">

Autohändler verkaufen Autos in den Städten. Üblicherweise bieten sie auch Services rund ums Auto an, so zum Beispiel Werkstattarbeiten, Ersatzteile oder Reifenwechsel. 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#bce0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fahrzeuge](#cargo_VEHI) |  |


<a name="industry_19"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_6) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_20"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_9) [Lebensmittelindustrie](#extension_6) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |


<a name="industry_21"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Getreide](#cargo_GRAI) |


<a name="industry_22"></a>
### Bauhof

<img src="builders_yard.png" alt="Bauhof">

Der Bauhof stellt Baumaterialien für die Stadt und ihre Bewohner bereit. Damit ist es eigentlich eher ein Baumarkt, in dem die Einwohner der Städte Baumaterial und Werkzeuge kaufen können. Bauhöfe hingegen sind zumindest in Deutschland kommunale Einrichtungen, in denen z.B. Streusand und andere notwendige Materialien gelagert werden. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_1) 


Farbe in der Übersichtskarte:<span style="background-color:#acacc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ziegel](#cargo_BDMT) |  |
| [Zement](#cargo_CMNT) |  |
| [Sand](#cargo_SAND) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_23"></a>
### Bauhof

<img src="builders_yard.png" alt="Bauhof">

Der Bauhof stellt Baumaterialien für die Stadt und ihre Bewohner bereit. Damit ist es eigentlich eher ein Baumarkt, in dem die Einwohner der Städte Baumaterial und Werkzeuge kaufen können. Bauhöfe hingegen sind zumindest in Deutschland kommunale Einrichtungen, in denen z.B. Streusand und andere notwendige Materialien gelagert werden. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Bauindustrie](#extension_1) 


Farbe in der Übersichtskarte:<span style="background-color:#acacc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_24"></a>
### Bekleidungsfabrik

<img src="clothing_plant.png" alt="Bekleidungsfabrik">

Die Bekleidungsfabrik ist der Ort, an dem aus Stoffen Kleidungsstücke gefertigt werden. Europa hat eine reichhaltige Geschichte der Bekleidungsindustrie, die allerdings quasi komplett durch billigere asiatische Konkurrenz ersetzt wurde. Spezialgeschäfte für hochwertige Bekleidung haben noch ihre eigene Nische. Deutschland hatte im 19. Jahrhundert eine bedeutende Bekleidungsindustrie, hauptsächlich in Schlesien und Sachsen. Heute existieren zwar noch viele Firmen, teilweise auch international sehr bekannte wie Boss, Triumph oder adidas, aber die Produktion wurde üblicherweise nach Asien verlagert. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#803828;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Textilien](#cargo_TEXT) | [Waren](#cargo_GOOD) |


<a name="industry_25"></a>
### Bekleidungsfabrik

<img src="clothing_plant.png" alt="Bekleidungsfabrik">

Die Bekleidungsfabrik ist der Ort, an dem aus Stoffen Kleidungsstücke gefertigt werden. Europa hat eine reichhaltige Geschichte der Bekleidungsindustrie, die allerdings quasi komplett durch billigere asiatische Konkurrenz ersetzt wurde. Spezialgeschäfte für hochwertige Bekleidung haben noch ihre eigene Nische. Deutschland hatte im 19. Jahrhundert eine bedeutende Bekleidungsindustrie, hauptsächlich in Schlesien und Sachsen. Heute existieren zwar noch viele Firmen, teilweise auch international sehr bekannte wie Boss, Triumph oder adidas, aber die Produktion wurde üblicherweise nach Asien verlagert. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#803828;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Textilien](#cargo_TEXT) |  |


<a name="industry_26"></a>
### Brauerei

<img src="brewery.png" alt="Brauerei">

Die Erzeugung von Bier ist seit Jahrtausenden belegt. Bier wird oft als flüssiges Brot bezeichnet und ist nach wie vor ein üblicher Teil der Ernährung. Im Mittelalter wurde Bier in erster Linie in Klöstern gebraut. Mit der industriellen Revolution und der Einführung neuer Materialien wie rostfreiem Stahl vergrößerte sich die Anzahl der Brauereien und die Menge des gebrauten Biers dramatisch. Die wichtigste Erfindung in diesem Zusammenhang war die Kältemaschine, die es im 19. Jahrhundert schließlich erlaubte, auch bei sommerlichen Temperaturen Bier zu brauen. Davor wurde Bier im Winter gebraut und anschließend in Kellern gelagert, um es vor der Sommerhitze zu schützen. 

Deutschland hat eine lange Tradition in der Bierbrauerei, und Bier ist ein bekannter Teil der Kultur. Die Deutschen gehören zu den größten Biertrinkern in Europa, entsprechend viel wird produziert. Das bekannte Reinheitsgebot legt fest, dass nur Hopfen, Malz, Wasser und bestimmte Getreidesorten verwendet werden dürfen. Trotzdem gibt es zahllose Brauereien, vor allem in Franken, welches die höchste Dichte an Brauereien weltweit aufweist. Über 5000 Sorten Bier werden von etwa 1500 Brauereien erzeugt, von denen wiederum die Hälfte in Bayern angesiedelt ist. Bierkonsum gehört zu den wichtigsten Tätigkeiten bei zahlreichen Volksfesten wie dem Oktoberfest in München oder der Bergkirchweih in Erlangen. 

Im Set ist Bier trotzdem keine eigene Fracht, sondern zählt einfach als Nahrungsmitel. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_3) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_27"></a>
### Brauerei

<img src="brewery.png" alt="Brauerei">

Die Erzeugung von Bier ist seit Jahrtausenden belegt. Bier wird oft als flüssiges Brot bezeichnet und ist nach wie vor ein üblicher Teil der Ernährung. Im Mittelalter wurde Bier in erster Linie in Klöstern gebraut. Mit der industriellen Revolution und der Einführung neuer Materialien wie rostfreiem Stahl vergrößerte sich die Anzahl der Brauereien und die Menge des gebrauten Biers dramatisch. Die wichtigste Erfindung in diesem Zusammenhang war die Kältemaschine, die es im 19. Jahrhundert schließlich erlaubte, auch bei sommerlichen Temperaturen Bier zu brauen. Davor wurde Bier im Winter gebraut und anschließend in Kellern gelagert, um es vor der Sommerhitze zu schützen. 

Deutschland hat eine lange Tradition in der Bierbrauerei, und Bier ist ein bekannter Teil der Kultur. Die Deutschen gehören zu den größten Biertrinkern in Europa, entsprechend viel wird produziert. Das bekannte Reinheitsgebot legt fest, dass nur Hopfen, Malz, Wasser und bestimmte Getreidesorten verwendet werden dürfen. Trotzdem gibt es zahllose Brauereien, vor allem in Franken, welches die höchste Dichte an Brauereien weltweit aufweist. Über 5000 Sorten Bier werden von etwa 1500 Brauereien erzeugt, von denen wiederum die Hälfte in Bayern angesiedelt ist. Bierkonsum gehört zu den wichtigsten Tätigkeiten bei zahlreichen Volksfesten wie dem Oktoberfest in München oder der Bergkirchweih in Erlangen. 

Im Set ist Bier trotzdem keine eigene Fracht, sondern zählt einfach als Nahrungsmitel. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Glas](#extension_3) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |


<a name="industry_28"></a>
### Chloralkali Elektrolyseanlage

<img src="chloralkali_plant.png" alt="Chloralkali Elektrolyseanlage">

Die Chlor-Alkali-Anlage benutzt Elektrolyse, um Salz in Chlor und Natronlauge aufzuspalten. Als Nebenprodukt entsteht dabei Wasserstoff. Der Prozess wurde im späten 19. Jahrhundert entwickelt und ist einer der wichtigsten grundlegenden technischen Prozesse der Chemieindustrie, da die beiden Hauptprodukte quasi überall benötigt werden. Die Reaktion benötigt große Mengen elektrischer Energie. Die ersten Anlagen dieser Art wurden um 1890 herum in Deutschland, Spanien, Frankreich und Russland gebaut. Heute sind über 20 Analgen in Deutschland in Betrieb, hauptsächlich in den klassischen Zentren der chemischen Industrie wie Ludwigshafen (BASF) und Schkopau (Dow Chemical), wobei sich die größte Anlage im norddeutschen Stade befindet. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b8dcc8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Salz](#cargo_SALT) | [Chlor](#cargo_CHLO) |
|  | [Natronlauge](#cargo_LYE_) |


<a name="industry_29"></a>
### Dampfreformierer

<img src="steamreformer.png" alt="Dampfreformierer">

Die Dampfreformierung geht auf eine Idee von Carl Bosch zurück, der eine preiswerte Möglichkeit suchte, Wasserstoff zu produzieren. Dazu werden Kohlenwasserstoffe, heutzutage in erster Linie Erdgas, durch Zuführen von Wärmeenergie und Wasser in Kohlendioxid und Wasserstoff zerlegt. Heutzutage stammen fast 50% des industriell benötigten Wasserstoffes aus dieser Reaktion. Etwa 60% des Wasserstoffs werden danach für die Synthese von Ammoniak verwendet. 

Da im Set Erdgas keine Rolle spielt, wird stattdessen Rohbenzin, sogenanntes Naphtha, als Ausgansstoff verwendet. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_7) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#403c0c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_30"></a>
### Druckerei

<img src="paper_mill.png" alt="Druckerei">

Der moderne Buchdruck wurde im 16. Jahrhundert in Deutschland erfunden. Im Zuge der Industrialisierung wurden später zahllose Zeitungen gedruckt, das Lesen von Büchern wurde zum Zeitvertreib der gebildeten Bürgerschicht. Heutzutage kann quasi jeder sein eigenes Buch drucken lassen. 

Diese Industrie benötigt Extension: [Papier](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Papier](#cargo_PAPR) | [Waren](#cargo_GOOD) |


<a name="industry_31"></a>
### Druckerei

<img src="paper_mill.png" alt="Druckerei">

Der moderne Buchdruck wurde im 16. Jahrhundert in Deutschland erfunden. Im Zuge der Industrialisierung wurden später zahllose Zeitungen gedruckt, das Lesen von Büchern wurde zum Zeitvertreib der gebildeten Bürgerschicht. Heutzutage kann quasi jeder sein eigenes Buch drucken lassen. 

Diese Industrie benötigt Extension: [Papier](#extension_8) [Verpackungsmittelindustrie](#extension_10) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Papier](#cargo_PAPR) |  |


<a name="industry_32"></a>
### Eisenerzbergwerk

<img src="iron_ore_mine.png" alt="Eisenerzbergwerk">

Eisenerz wurde bereits im Altertum abgebaut und verhüttet. Im Zusammenhang mit der Entwicklung von preiswerten Prozessen zur Stahlherstellung und dem wachsenden Bedarf, zum Beispiel für die Eisenbahn, wurde die Stahlindustrie im 19. Jahrhundert einer der wichtigsten Wirtschaftszweige. 

In Deutschland wurde bis in die Mitte des 20. Jahrhunderts Eisenerz gefördert, aber insgesamt war Deutschland schon immer auf Erzimporte angewiesen. 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#74581c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Eisenerz](#cargo_IORE) |


<a name="industry_33"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfererze enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Erz in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Eisenerz](#cargo_IORE) |
| [Kupferkies](#cargo_PORE) | [Schwefel](#cargo_SULP) |


<a name="industry_34"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfererze enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Erz in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) [Farbindustrie](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Kupfererz](#cargo_CORE) |
| [Kupferkies](#cargo_PORE) | [Eisenerz](#cargo_IORE) |
|  | [Schwefel](#cargo_SULP) |


<a name="industry_35"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Bauindustrie](#extension_1) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Ruß](#cargo_CBLK) | [Farbe](#cargo_COAT) |
| [Kupfer](#cargo_COPR) |  |
| [Eisenerz](#cargo_IORE) |  |


<a name="industry_36"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Bauindustrie](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Ruß](#cargo_CBLK) | [Farbe](#cargo_COAT) |
| [Kupfer](#cargo_COPR) |  |
| [Eisenerz](#cargo_IORE) |  |
| [Kalkstein](#cargo_LIME) |  |


<a name="industry_37"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Bauindustrie](#extension_1) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Farbe](#cargo_COAT) |
| [Ruß](#cargo_CBLK) |  |
| [Kupfer](#cargo_COPR) |  |
| [Eisenerz](#cargo_IORE) |  |


<a name="industry_38"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Bauindustrie](#extension_1) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Farbe](#cargo_COAT) |
| [Ruß](#cargo_CBLK) |  |
| [Kupfer](#cargo_COPR) |  |
| [Eisenerz](#cargo_IORE) |  |
| [Kalkstein](#cargo_LIME) |  |


<a name="industry_39"></a>
### Fischgründe

<img src="fishing_grounds.png" alt="Fischgründe">

Fisch muss auf dem Meer gefangen werden, was im Spiel eine interessante Herausforderung für den Transport darstellt, da man den Fisch von Schiffen aus in Häfen umladen muss. Obwohl Deutschland Zugang zur Nord- und Ostsee hat, wird ein Großteil des Fisches importiert. Deutschland ist sogar einer der größten Importeure für Fisch in Europa. 


Farbe in der Übersichtskarte:<span style="background-color:#9cccdc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Fisch](#cargo_FISH) |


<a name="industry_40"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_3) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Branntkalk](#cargo_QLME) | [Glas](#cargo_GLAS) |
| [Sand](#cargo_SAND) |  |


<a name="industry_41"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_2) [Koks und Schwefel](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_42"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) [Koks und Schwefel](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_43"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Koks und Schwefel](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Kupfererz](#cargo_CORE) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_44"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Kupfererz](#cargo_CORE) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_45"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_46"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_47"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_48"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_2) [Koks und Schwefel](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_49"></a>
### Hotel

<img src="hotel.png" alt="Hotel">

Ob für Urlaub oder Dienstreisen, Hotels sind eine relevante Wirtschaftsgröße. In einigen Regionen wir z.B. an der Ostseeküste ist Tourismus der wichtigste Wirtschaftsfaktor. Große Städte wie Frankfurt oder München haben ebenfalls eine überdurchschnittlich große Zahl an Hotels, da dort Handelsmessen und andere jährliche Festveranstaltungen stattfinden. 

Im set "produzieren" Hotels so viele Passagiere, wie man anliefert, was darstellen soll dass Gäste die dort einchecken irgendwann auch wieder auschecken werden. 


Farbe in der Übersichtskarte:<span style="background-color:#508ca0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Nahrungsmittel](#cargo_FOOD) | [Passagiere](#cargo_PASS) |
| [Passagiere](#cargo_PASS) |  |


<a name="industry_50"></a>
### Hydrierwerk

<img src="coal_liquefaction_plant.png" alt="Hydrierwerk">

Die Herstellung von Treibstoffen durch die Hydrierung von Kohle war eine Spezialität der deutschen Chemiegeschichte. Da Deutschland keine eigenen Ölvorkommen in relevanter Größe besitzt, war man nach dem ersten Weltkrieg bestrebt, Treibstoffe aus heimischer Kohle zu erzeugen. Der erste derartig erzeugte Kraftstoff war das sogenannte Leuna-Benzin, benannt nach dem Standort der Anlage. Für Nazideutschland waren die Anlagen kriegswichtig und wurden entsprechend staatlich gefördert. Nach Kriegsende schwand die Bedeutung des Verfahrens, da Treibstoffe einfacher und billiger aus verfügbarem Erdöl gewonnen werden können. Allerdings steigt im 21. Jahrhundert die Bedeutung des Verfahrens in vielen Ländern wieder, um der Abhängigkeit von importiertem Erdöl entgegenzuwirken. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_7) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#cccca8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Treibstoff](#cargo_PETR) |


<a name="industry_51"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_3) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |


<a name="industry_52"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Branntkalk](#cargo_QLME) |  |


<a name="industry_53"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_3) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |


<a name="industry_54"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_3) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Branntkalk](#cargo_QLME) |  |


<a name="industry_55"></a>
### Kalkbrennerei

<img src="lime_kiln.png" alt="Kalkbrennerei">

In Kalkofen wird für den Prozess der Kalzinierung von Kalkstein genutzt. Diese Reaktion erzeugt Branntkalk, chemisch gesehen wird Calciumcarbonat zu Calciumoxid umgesetzt. Dabei wird der Kalkstein nicht verbrannt, sondern lediglich großer Hitze ausgesetzt. Der Prozess ist seit Jahrtausenden bekannt, und Branntkalk wird seit Ewigkeiten zur Herstellung von Zement verwendet. Der Ofen wird üblicherweise durch das Verbrennen fossiler Brennstoffe erhitzt, was den ohnehin unvermeidlichen Kohlendioxidausstoß weiter erhöht. 

Diese Industrie benötigt Extension: [Glas](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#8c68fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalkstein](#cargo_LIME) | [Branntkalk](#cargo_QLME) |


<a name="industry_56"></a>
### Kalkbrennerei

<img src="lime_kiln.png" alt="Kalkbrennerei">

In Kalkofen wird für den Prozess der Kalzinierung von Kalkstein genutzt. Diese Reaktion erzeugt Branntkalk, chemisch gesehen wird Calciumcarbonat zu Calciumoxid umgesetzt. Dabei wird der Kalkstein nicht verbrannt, sondern lediglich großer Hitze ausgesetzt. Der Prozess ist seit Jahrtausenden bekannt, und Branntkalk wird seit Ewigkeiten zur Herstellung von Zement verwendet. Der Ofen wird üblicherweise durch das Verbrennen fossiler Brennstoffe erhitzt, was den ohnehin unvermeidlichen Kohlendioxidausstoß weiter erhöht. 

Diese Industrie benötigt Extension: [Glas](#extension_3) [Koks und Schwefel](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#8c68fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Branntkalk](#cargo_QLME) |
| [Kalkstein](#cargo_LIME) |  |


<a name="industry_57"></a>
### Kalksteinbergwerk

<img src="limestone_mine.png" alt="Kalksteinbergwerk">

Kalkstein wird bereits seit Jahrhunderten in Deutschland abgebaut, üblicherweise in Steinbrüchen. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcfcc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kalkstein](#cargo_LIME) |


<a name="industry_58"></a>
### Kaufhaus

<img src="department_store.png" alt="Kaufhaus">

Das Kaufhaus steht stellvertretend für sämtliche Läden einer Stadt, in denen man alles kaufen kann, was man so gebrauchen kann, sei es Kleidung, Haushaltsgegenstände wie Waschmaschinen, Spielzeug usw. Kaufhäuser lösen im Set das Problem dass kleine Städte üblicherweise keine Waren akzeptieren, bevor sie nicht auf eine gewisse Größe angewachsen sind. 


Farbe in der Übersichtskarte:<span style="background-color:#fcf4ec;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) |  |


<a name="industry_59"></a>
### Kohlebergwerk

<img src="coal_mine.png" alt="Kohlebergwerk">

Kohlebergbau wurde im Zuge der industriellen Revolution im 19. Jahrhundert einer der wichtigsten Industriezweige, da man die Kohle zum Antrieb der Dampfmaschinen brauchte. Mit Dampfmaschinen wurde quasi alles angetrieben, ob nun Wasserpumpen in den Bergwerken oder Webstühle. Mit der Entwicklung der Eisenbahn und der Einführung der Dampfschiffahrt wuchs der Bedarf nach Kohle noch weiter. 

Der Kohlebergbau begann in Deutschland hautpsächlich im Ruhrgebiet und in Schlesien, aber auch im Saarland. Entsprechend waren diese Gebiete auch die Zentren der Schwerindustrie. Im frühen 20. Jahrhundert stieg die Produktion rasch an, da sich neuartige Technologien wie der Presslufhammer durchsetzten. Zu dieser Zeit war Deutschland einer der größten Kohleproduzenten der Welt. Nach dem Zweiten Weltkrieg war das Produktionsmaximum in den 1950er Jahren erreicht. Die steigenden Kosten machten den Kohlebergbau unprofitable, so dass die Industrie seit den 1960er Jahren schrumpfte und jahrzehntelang subventioniert werden musste. Die letzten Kohlebergwerke stellten den Betrieb 2018 ein. 

Industry ist nur von 1800 bis 1950 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#101010;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kohle](#cargo_COAL) |


<a name="industry_60"></a>
### Kokerei

<img src="coke_oven.png" alt="Kokerei">

Kohle enthält einen gewissen Anteil an Schwefel, der beim Verbrennen frei wird und dann, je nach Verwendungszweck, Probleme verursachen kann. So hat er negativen Einfluss auf die Qualität von Roheisen im Rahmen der Stahlproduktion. Die Lösung ist die Aufwertung von Kohle zu Koks, bei der der Schwefel entfernt wird und hochreiner Kohlenstoff über bleibt. Früher gab es in Deutschland eine ganze Reiher Kokereien, die nicht nur Koks herstellten, sondern als Nebenprodukte auch Schwefel und andere Chemikalien produzieren. Heutzutage sind aufgrund des Strukturwandels seit den 70er Jahren nur noch eine Handvoll Kokereien im Ruhrgebiet in Betrieb. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Koks](#cargo_COKE) |
|  | [Schwefel](#cargo_SULP) |


<a name="industry_61"></a>
### Kraftwerk

<img src="power_plant.png" alt="Kraftwerk">

Kraftwerke erzeugen elektrischen Strom, üblicherweise indem sie Wasser kochen und mit dem Wasserdampf Turbinen antreiben, die wiederum mit Generatoren gekuppelt sind. Das gleiche Prinzip wird auch in Atomkraftwerken angewandt, während Wasserkraftwerke das Wasser direkt auf die Turbinen leiten. Da es im Spiel um den Transport von Frachten geht, konzentriert sich das Set auf fossile Energien und den Transport von Kohle und Öl. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie produziert elektrischen Strom. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) |  |
| [Öl](#cargo_OIL_) |  |


<a name="industry_62"></a>
### Kraftwerk

<img src="power_plant.png" alt="Kraftwerk">

Kraftwerke erzeugen elektrischen Strom, üblicherweise indem sie Wasser kochen und mit dem Wasserdampf Turbinen antreiben, die wiederum mit Generatoren gekuppelt sind. Das gleiche Prinzip wird auch in Atomkraftwerken angewandt, während Wasserkraftwerke das Wasser direkt auf die Turbinen leiten. Da es im Spiel um den Transport von Frachten geht, konzentriert sich das Set auf fossile Energien und den Transport von Kohle und Öl. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie produziert elektrischen Strom. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Schwefel](#cargo_SULP) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_63"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) [Farbindustrie](#extension_2) [Organische Chemie](#extension_7) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Öl](#cargo_OIL_) | [Kunststoffe](#cargo_PLAS) |


<a name="industry_64"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) [Organische Chemie](#extension_7) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Kunststoffe](#cargo_PLAS) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_65"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) [Organische Chemie](#extension_7) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Kunststoffe](#cargo_PLAS) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_66"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_7) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Kunststoffe](#cargo_PLAS) |
| [Farbe](#cargo_COAT) |  |
| [Öl](#cargo_OIL_) |  |


<a name="industry_67"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) [Farbindustrie](#extension_2) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Kunststoffe](#cargo_PLAS) |


<a name="industry_68"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Organische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Kunststoffe](#cargo_PLAS) |


<a name="industry_69"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Organische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Kunststoffe](#cargo_PLAS) |


<a name="industry_70"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Farbindustrie](#extension_2) [Organische Chemie](#extension_7) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Kunststoffe](#cargo_PLAS) |
| [Farbe](#cargo_COAT) |  |


<a name="industry_71"></a>
### Kupfererzbergwerk

<img src="copper_ore_mine.png" alt="Kupfererzbergwerk">

Kupfererze wurden schon seit dem Altertum abgebaut. Im Set sind die Bergwerke, wie alle anderen Bergwerke auch, erst später verfügbar, da man ohne mechanische Unterstützung nicht im großen Maßstab Bergbau betreiben kann. In Europa gab es nur wenige Erzlagerstäten. Kupfererz wurde in Mitteldeutschland abgebaut, aber die Vorräte waren bereits vor Beginn der industriellen Revolution erschöpft. Die letzten Kupfererzbergwerke waren noch bis Mitte des 20. Jahrhunderts in Betrieb, was jedoch gerade in Ostdeutschland politische Gründe hatte, denn man hatte keinen Zugang zum Kupferweltmarkt. Heute wird Kupfererz importiert, während das Recycling von Kupferschrott eine wachsende Bedeutung hat. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kupfererz](#cargo_CORE) |


<a name="industry_72"></a>
### Kupfererzbergwerk

<img src="copper_ore_mine.png" alt="Kupfererzbergwerk">

Kupfererze wurden schon seit dem Altertum abgebaut. Im Set sind die Bergwerke, wie alle anderen Bergwerke auch, erst später verfügbar, da man ohne mechanische Unterstützung nicht im großen Maßstab Bergbau betreiben kann. In Europa gab es nur wenige Erzlagerstäten. Kupfererz wurde in Mitteldeutschland abgebaut, aber die Vorräte waren bereits vor Beginn der industriellen Revolution erschöpft. Die letzten Kupfererzbergwerke waren noch bis Mitte des 20. Jahrhunderts in Betrieb, was jedoch gerade in Ostdeutschland politische Gründe hatte, denn man hatte keinen Zugang zum Kupferweltmarkt. Heute wird Kupfererz importiert, während das Recycling von Kupferschrott eine wachsende Bedeutung hat. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Koks und Schwefel](#extension_5) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_73"></a>
### Kupferhütte

<img src="copper_smelter.png" alt="Kupferhütte">

Die Erzeugung von Kupfer aus Kupfererz ist ein energieintensiver Prozess auf Basis von Elektrolyse. Nebenprodukte sind weitere Metallerze sowie Schwefel, je nach Qualität des verwendeten Kupfererzes. Im Set wird davon ausgegangen, dass Kupfererz hoher Qualität verwendet wird, während schwefelreiche Erze Teil einer anderen Erweiterung sind. Der größte Kupferproduzent Europas ist in Hamburg ansässig und erzeugt dort Kupfer aus importiertem Erz und aus Metallschrott. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Kupfererz](#cargo_CORE) | [Kupfer](#cargo_COPR) |


<a name="industry_74"></a>
### Kupferhütte

<img src="copper_smelter.png" alt="Kupferhütte">

Die Erzeugung von Kupfer aus Kupfererz ist ein energieintensiver Prozess auf Basis von Elektrolyse. Nebenprodukte sind weitere Metallerze sowie Schwefel, je nach Qualität des verwendeten Kupfererzes. Im Set wird davon ausgegangen, dass Kupfererz hoher Qualität verwendet wird, während schwefelreiche Erze Teil einer anderen Erweiterung sind. Der größte Kupferproduzent Europas ist in Hamburg ansässig und erzeugt dort Kupfer aus importiertem Erz und aus Metallschrott. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Kupfer](#cargo_COPR) |
| [Kupfererz](#cargo_CORE) |  |


<a name="industry_75"></a>
### Laden

<img src="general_store.png" alt="Laden">

Der Lebensmittelladen ist im Prinzip eine Darstellung dessen, was heutzutage als Supermarkt bekannt ist. Supermärkte entstanden allerdings erst in der zweiten Hälfte des 20. Jahrhunderts, vorher war der klassische Tante-Emma-Laden oder der Wochenmarkt der Platz, wo man Lebensmittel kaufte. 


Farbe in der Übersichtskarte:<span style="background-color:#fcd8c8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Nahrungsmittel](#cargo_FOOD) |  |


<a name="industry_76"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Milch](#cargo_MILK) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_77"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Grundlegende Anorganische Chemie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Natronlauge](#cargo_LYE_) | [Nahrungsmittel](#cargo_FOOD) |
| [Milch](#cargo_MILK) |  |


<a name="industry_78"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Verpackungsmittelindustrie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Milch](#cargo_MILK) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_79"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Natronlauge](#cargo_LYE_) | [Nahrungsmittel](#cargo_FOOD) |
| [Milch](#cargo_MILK) |  |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_80"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Waren](#cargo_GOOD) |
| [Textilien](#cargo_TEXT) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_81"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Waren](#cargo_GOOD) |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_82"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Textilien](#cargo_TEXT) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_83"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_84"></a>
### Mühle

<img src="flour_mill.png" alt="Mühle">

Getreidemühlen gibt es seit tausenden von Jahren. Sie mahlen Getreide zu Mehl, was eine überaus wichtige Rolle in der Nahrungsmittelproduktion stellt. Das Mahlen fand traditionell auf einem rotierenden Mahlstein statt, der üblicherweise durch Wasser oder Windkraft bewegt wurde. Mühlen waren überall zu finden, so wie der Familienname Müller aus der Berufsbezeichnung abgeleitet wurde. Die Industrialisierung hat den Prozess der Mehlproduktion erheblich verändert, da mit maschinellem Antrieb viel größere Produktionsmengen möglich wurden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#d4bc94;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_85"></a>
### Mühle

<img src="flour_mill.png" alt="Mühle">

Getreidemühlen gibt es seit tausenden von Jahren. Sie mahlen Getreide zu Mehl, was eine überaus wichtige Rolle in der Nahrungsmittelproduktion stellt. Das Mahlen fand traditionell auf einem rotierenden Mahlstein statt, der üblicherweise durch Wasser oder Windkraft bewegt wurde. Mühlen waren überall zu finden, so wie der Familienname Müller aus der Berufsbezeichnung abgeleitet wurde. Die Industrialisierung hat den Prozess der Mehlproduktion erheblich verändert, da mit maschinellem Antrieb viel größere Produktionsmengen möglich wurden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#d4bc94;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_86"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) [Lebensmittelindustrie](#extension_6) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |


<a name="industry_87"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_6) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_88"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_89"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Lebensmittelindustrie](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Natronlauge](#cargo_LYE_) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_90"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) [Lebensmittelindustrie](#extension_6) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_91"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Verpackungsmittelindustrie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_92"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Verpackungsmittelindustrie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_6) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt wenigstens eine der in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_93"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) [Lebensmittelindustrie](#extension_6) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Natronlauge](#cargo_LYE_) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_94"></a>
### Papiermühle

<img src="paper_mill.png" alt="Papiermühle">

Die Papiermühle spaltet Holz durch Chemikalien auf um Zellulosefasern herauszulösen, die wiederum die Basis für die Papierproduktion sind. Der Prozess der Papierherstellung ist seit Tausenden Jahren bekannt, aber die moderne Produktion begann erst im späten 19. Jahrhundert durch verschiedene Fortschritte in der Chemie. Deutschland ist einer der größten Papierproduzenten der Welt, und der größte in Europa. Die Papiermühle im Set ist eine solche moderne Anlage, die Holz auf chemischem Weg spaltet und das Papier später bleicht. 

Diese Industrie benötigt Extension: [Papier](#extension_8) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#9ca0ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Papier](#cargo_PAPR) |
| [Natronlauge](#cargo_LYE_) |  |
| [Holz](#cargo_WOOD) |  |


<a name="industry_95"></a>
### Rußfabrik

<img src="carbon_black_plant.png" alt="Rußfabrik">

Die Rußfabrik spaltet Kohlenstoffverbindungen wie Kohle oder Öl auf und erzeugt daraus quasi reines Kohlenstoffpulver. Üblicherweise werden dafür die schweren Fraktionen der Erdöldestillation, Schweröle als, genutzt, die anderweitig kaum Verwendung haben. Je nach eingesetztem Prozess entsteht bei diesem Prozess eine erhebliche Menge Kohlendioxid. Forschungen in jüngster Zeit haben jedoch zu neuen Ansätzen geführt, bei denen Kohlenwasserstoffe komplett in Kohlenstoff und Wasserstoff zerlegt werden, was den ökologischen Fußabdruck massiv reduziert. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_7) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ruß](#cargo_CBLK) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_96"></a>
### Rußfabrik

<img src="carbon_black_plant.png" alt="Rußfabrik">

Die Rußfabrik spaltet Kohlenstoffverbindungen wie Kohle oder Öl auf und erzeugt daraus quasi reines Kohlenstoffpulver. Üblicherweise werden dafür die schweren Fraktionen der Erdöldestillation, Schweröle als, genutzt, die anderweitig kaum Verwendung haben. Je nach eingesetztem Prozess entsteht bei diesem Prozess eine erhebliche Menge Kohlendioxid. Forschungen in jüngster Zeit haben jedoch zu neuen Ansätzen geführt, bei denen Kohlenwasserstoffe komplett in Kohlenstoff und Wasserstoff zerlegt werden, was den ökologischen Fußabdruck massiv reduziert. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_2) [Organische Chemie](#extension_7) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ruß](#cargo_CBLK) |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_97"></a>
### Salzbergwerk

<img src="salt_mine.png" alt="Salzbergwerk">

Aufgrund von jahrtausende währenden geologischen Prozessen gibt es in Nord- und Mitteldeutschland erhebliche Salzlagerstätten. An einigen Stellen tritt salzhaltiges Wasser an die Oberfläche, dort waren bereits im Mittelalter Salzsieder tätig. Eine wichtige Veränderung war der Beginn des Salzbergbaus im 19. Jahrhundert. Das erste Salzbergwerk entstand 1855 in Staßfurt, welches damals zu Preußen gehörte. Im benachbarten Bernburg wird seit etwa 1920 Salz abgebaut, die gesamte Gegend gehört heute zum entsprechend benannten Salzlandkreis. Weitere Bergwerke existieren in Niedersachsen und in Süddeutschland. Heute ist Deutschland mit Abstand der größte Salzproduzent Europas. Damit ist das Salz mit seiner Bedeutung für die chemische Industrie ein wichtiger Wirtschaftsfaktor. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_4) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d4d4e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Salz](#cargo_SALT) |


<a name="industry_98"></a>
### Sandgrube

<img src="sand_pit.png" alt="Sandgrube">

Sand wird üblicherweise in Sandgruben abgebaut. Aufgrund der geologischen Prozesse, die die Erdoberfläche über Millionen von Jahren formten, findet man Sandgruben hauptsächlich in Norddeutschland, aber auch im Alpenraum. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_1) 


Farbe in der Übersichtskarte:<span style="background-color:#e8b810;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Sand](#cargo_SAND) |


<a name="industry_99"></a>
### Schlachthof

<img src="sand_pit.png" alt="Schlachthof">

Schlachthöfe sind Industrien, in denen Vieh geschlachtet und verarbeitet wird, in erster Linie zu Fleisch für den Verzehr. Obwohl das Schlachten von Tieren seit tausenden Jahren üblich ist, explodierte die Menge des produzierten Fleisches im Zuge der Industrialisierung geradezu. Die Einführung effizienter Kühlung erlaubte den Fleischtransport über lange Strecken, was wiederum zu einer Zentralisierung der Industrien in wenige große Schlachthöfe zur Folge hatte. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#b09c6c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Vieh](#cargo_LVST) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_100"></a>
### Schlachthof

<img src="sand_pit.png" alt="Schlachthof">

Schlachthöfe sind Industrien, in denen Vieh geschlachtet und verarbeitet wird, in erster Linie zu Fleisch für den Verzehr. Obwohl das Schlachten von Tieren seit tausenden Jahren üblich ist, explodierte die Menge des produzierten Fleisches im Zuge der Industrialisierung geradezu. Die Einführung effizienter Kühlung erlaubte den Fleischtransport über lange Strecken, was wiederum zu einer Zentralisierung der Industrien in wenige große Schlachthöfe zur Folge hatte. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Verpackungsmittelindustrie](#extension_10) 


Farbe in der Übersichtskarte:<span style="background-color:#b09c6c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Vieh](#cargo_LVST) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_101"></a>
### Steamcracker

<img src="steamcracker.png" alt="Steamcracker">

In Ölraffinerien fällt in großer Menge Rohbenzin, sogenanntes Naphtha, an. Die chemische Industrie benötigt jedoch Kohlenwasserstoffe, die sich durch Spaltung aus Naphtha erzeugen lassen. Dazu muss das Naphtha auf über 800°C erhitzt werden, so dass es als Gas vorliegt, woher der Name des Prozesses rührt. Als Produkte entstehen verschiedene leichte Kohlenwasserstoffe, die zum Beispiel für die Produktion von Kunststoffen notwendig sind. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_7) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#787840;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Naphtha](#cargo_RFPR) | [Treibstoff](#cargo_PETR) |


<a name="industry_102"></a>
### Sägewerk

<img src="sawmill.png" alt="Sägewerk">

Sägewerke schneiden Holz in normierte Größen und Formen, so dass die resultierenden Balken und Bretter in verschiedensten Industrien verwendet werden können. Damit sind Sägewerke ein notwendiger Zwischenschritt in der Bereitstellung von Rohstoffen für die Bauindustrie, die Möbelindustrie und andere. 


Farbe in der Übersichtskarte:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Holz](#cargo_WOOD) | [Schnittholz](#cargo_WDPR) |


<a name="industry_103"></a>
### Säurefabrik

<img src="acid_plant.png" alt="Säurefabrik">

Schwefelsäure wird in Deutschland in Größenordnungen von mehreren Millionen Tonnen pro Jahr hergestellt und ist damit einer der wichtigsten Grundstoffe der chemischen Industrie. In echten Chemieanlagen werden die Säuren möglichst direkt für weitere Reaktionen verbraucht, um Transporte der gefährlichen Stoffe zu vermeiden. Im Set produziert die Säurefabrik verschiedene Säuren, um dem Spieler mehrere Varianten zu ermöglichen. Aus den akzeptierten Rohstoffen kann man Schwefelsäure produzieren, aber auch Salzsäure. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_4) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Schwefel](#cargo_SULP) | [Säure](#cargo_ACID) |


<a name="industry_104"></a>
### Säurefabrik

<img src="acid_plant.png" alt="Säurefabrik">

Schwefelsäure wird in Deutschland in Größenordnungen von mehreren Millionen Tonnen pro Jahr hergestellt und ist damit einer der wichtigsten Grundstoffe der chemischen Industrie. In echten Chemieanlagen werden die Säuren möglichst direkt für weitere Reaktionen verbraucht, um Transporte der gefährlichen Stoffe zu vermeiden. Im Set produziert die Säurefabrik verschiedene Säuren, um dem Spieler mehrere Varianten zu ermöglichen. Aus den akzeptierten Rohstoffen kann man Schwefelsäure produzieren, aber auch Salzsäure. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_5) [Grundlegende Anorganische Chemie](#extension_4) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Säure](#cargo_ACID) |
| [Schwefel](#cargo_SULP) |  |


<a name="industry_105"></a>
### Tankstelle

<img src="petrol_station.png" alt="Tankstelle">

Die erste Tankstelle der Geschichte war eine Apotheke in Wiesloch in Südwestdeutschland - dort erstand Bertha Benz 1888 bei der ersten Überlandfahrt von Mannheim nach Pforzheim den notwendigen Treibstoff. Die ersten Tankstellen, die von vornherein als solche konzipiert waren, tauchten erst nach dem Ersten Weltkrieg auf, verbreiteten sich dann jedoch rasant. Damals war es noch üblich, dass ein ausgebildeter Tankwart das Auftanken übernahm und bei der Gelegenheit auch gleich noch den Ölstand prüfte und die Scheibe putzte. Heute ist ein flächendeckendes Tankstellennetz eines der wichtigsten Infrastrukturmerkmale eines Industriestaates. 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#78a488;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Treibstoff](#cargo_PETR) |  |


<a name="industry_106"></a>
### Textilfabrik

<img src="textile_mill.png" alt="Textilfabrik">

Die Textilfabrik fasst mehrere Industrien zusammen, die sich mit der Herstellung von Garn und Stoffen beschäftigen. Diese Arbeiten fanden jahrhundertelang hauptsächlich kleingewerblich statt, bevor die Mechanisierung im 18. und 19. Jahrhundert Einzug hielt. Webstühle gehörten damals zu den ersten Geräten, die mechanisch betrieben wurden, um die Produktionszeiten zu verkürzen. Im Set kombiniert diese Industrie sämtliche Schritte der Verarbeitung von Wolle und synthetischen Fasern zu Garn (spinnen), bevor sie z.B. durch Weben zu Stoffen verarbeitet werden. Diese Stoffe werden dann von anderen Industrien verwendet, um verschiedenste Waren zu produzieren. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#a85c4c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Textilien](#cargo_TEXT) |
| [Wolle](#cargo_WOOL) |  |


<a name="industry_107"></a>
### Textilfabrik

<img src="textile_mill.png" alt="Textilfabrik">

Die Textilfabrik fasst mehrere Industrien zusammen, die sich mit der Herstellung von Garn und Stoffen beschäftigen. Diese Arbeiten fanden jahrhundertelang hauptsächlich kleingewerblich statt, bevor die Mechanisierung im 18. und 19. Jahrhundert Einzug hielt. Webstühle gehörten damals zu den ersten Geräten, die mechanisch betrieben wurden, um die Produktionszeiten zu verkürzen. Im Set kombiniert diese Industrie sämtliche Schritte der Verarbeitung von Wolle und synthetischen Fasern zu Garn (spinnen), bevor sie z.B. durch Weben zu Stoffen verarbeitet werden. Diese Stoffe werden dann von anderen Industrien verwendet, um verschiedenste Waren zu produzieren. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_9) [Farbindustrie](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#a85c4c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Textilien](#cargo_TEXT) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Wolle](#cargo_WOOL) |  |


<a name="industry_108"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Glas](#extension_3) [Papier](#extension_8) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Verpackungen](#cargo_MNSP) |


<a name="industry_109"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_3) [Papier](#extension_8) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Verpackungen](#cargo_MNSP) |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_110"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) [Glas](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Papier](#extension_8) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Verpackungen](#cargo_MNSP) |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_111"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) [Aluminium](#extension_0) [Glas](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Papier](#extension_8) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Verpackungen](#cargo_MNSP) |
| [Glas](#cargo_GLAS) |  |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_112"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) [Papier](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Glas](#extension_3) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Papier](#cargo_PAPR) | [Verpackungen](#cargo_MNSP) |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_113"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) [Aluminium](#extension_0) [Papier](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_3) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Verpackungen](#cargo_MNSP) |
| [Papier](#cargo_PAPR) |  |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_114"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) [Glas](#extension_3) [Papier](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Verpackungen](#cargo_MNSP) |
| [Papier](#cargo_PAPR) |  |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_115"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_10) [Aluminium](#extension_0) [Glas](#extension_3) [Papier](#extension_8) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Verpackungen](#cargo_MNSP) |
| [Glas](#cargo_GLAS) |  |
| [Papier](#cargo_PAPR) |  |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_116"></a>
### Viehzucht

<img src="animal_farm.png" alt="Viehzucht">

Viehzuchtbetriebe sind Teil der Landwirtschaft. Sie züchten Vieh und liefern dazugehörige Produkte wie Milch und Wolle. In der Realität sind diese Betriebe heutzutage auf bestimmte Tiere spezialisiert, so dass es Hühnerfarmen oder Schweinemastbetriebe gibt, im Set ist das alles in eine Industrie zusammengefasst. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#90e05c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Vieh](#cargo_LVST) |
|  | [Milch](#cargo_MILK) |


<a name="industry_117"></a>
### Viehzucht

<img src="animal_farm.png" alt="Viehzucht">

Viehzuchtbetriebe sind Teil der Landwirtschaft. Sie züchten Vieh und liefern dazugehörige Produkte wie Milch und Wolle. In der Realität sind diese Betriebe heutzutage auf bestimmte Tiere spezialisiert, so dass es Hühnerfarmen oder Schweinemastbetriebe gibt, im Set ist das alles in eine Industrie zusammengefasst. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_6) [Textilindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#90e05c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Vieh](#cargo_LVST) |
|  | [Milch](#cargo_MILK) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_118"></a>
### Wald

<img src="forest.png" alt="Wald">

Wälder wurden bereits als Quelle für Holz genutzt, als Menschen noch mit Speeren jagten und die ersten Holzhütten bauten. Holz hat diverse industrielle Einsatzgebiete, u.a. in der Papierherstellung, somit sind Wälder ein wichtiger Industriezweig, nicht nur in der Realität, sondern auch im Spiel. Im Gegensatz zu den Kohle oder Öl ist Holz auch ein nachwachsender Rohstoff, so dass Wälder im Set unendlich lange produzieren können. 


Farbe in der Übersichtskarte:<span style="background-color:#68941c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Holz](#cargo_WOOD) |


<a name="industry_119"></a>
### Zementfabrik

<img src="cement_plant.png" alt="Zementfabrik">

Die ersten Zementwerke in Deutschland entstanden im frühen 19. Jahrhundert. In der zweiten Hälfte des Jahrhunderts wurden die Produktionsprozesse und Qualitätsanforderungen vereinheitlicht und standardisiert. Heute ist Deutschland mit über 50 Zementwerken der größte Produzent Europas. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#6c7484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalkstein](#cargo_LIME) | [Zement](#cargo_CMNT) |
| [Sand](#cargo_SAND) |  |


<a name="industry_120"></a>
### Ziegelei

<img src="brick_works.png" alt="Ziegelei">

Die effiziente Massenproduktion von Ziegeln begann im 19. Jahrhundert im Rahmen der industriellen Revolution. Viele neue Industriegebäude mussten gebaut werden, und die neuen Eisenbahnstrecken erforderten große Brücken. 

Ziegel wurden schon seit dem Altertum produziert, üblicherweise wurde Holz verfeuert um die notwendige Hitze zu erzeugen. Im Set wird eine modernere Variante des Ziegelei dargestellt, die Kohle statt Holz benutzt. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#cc8060;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ziegel](#cargo_BDMT) |


<a name="industry_121"></a>
### Ölbohrinsel

<img src="oil_rig.png" alt="Ölbohrinsel">

Ölbohrinseln werden genutzt, um Öl aus Lagerstätten zu fördern, die unter dem Meeresboden liegen. Zahlreiche derartige Lagerstätten wurden in der Nordsee entdeckt, und seit der Mitte der 1980er Jahre fördert auch Deutschland Öl in diesen Gebieten Allerdings ist die Förderung bereits seit den 1990er Jahren rückläufig. 

Im Set produzieren Ölbohrinseln eine konstante Anzahl von Passagieren, was die Arbeiter simuliert, die auf diesen Plattformen arbeiten. 

Industry ist erst ab 1985 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#80c4fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Passagiere](#cargo_PASS) | [Öl](#cargo_OIL_) |
|  | [Passagiere](#cargo_PASS) |


<a name="industry_122"></a>
### Ölquellen

<img src="oil_well.png" alt="Ölquellen">

Es ist ein relativ unbekannter Fakt, dass die ersten Ölbohrungen in den späten 1850er Jahren in Deutschland stattfanden, noch vor dem ersten großen Ölboom in Nordamerika. Eine Ölquellen werden noch heute in Norddeutschland (hauptsächlich in Niedersachsen) betrieben, aber viele Quellen wurden bereits in den 1960er Jahren aufgegeben, da der Import von Öl immer billiger wurde. 

Industry ist nur von 1860 bis 1985 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#80c4fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Öl](#cargo_OIL_) |


<a name="industry_123"></a>
### Ölraffinerie

<img src="oil_refinery.png" alt="Ölraffinerie">

Ölraffinerien spalten Erdöl in verschiedene Bestandteile auf, die wiederum Grundstoffe für die gesamte chemische Industrie darstellen. So erhält man neben diversen Treibstoffen auch diverse Schmierstoffe, Flüssiggase und Heizöl. Darüber hinaus wird das Erdöl auch entschwefelt und von sonstigen Verunreinigungen befreit. In echten Raffinerien sind weitere Produktions- und Veredelungsschritte nachgeschaltet, so dass eine Raffinerie eine ganze Reihe von Produktion erzeugen kann. Im Set sind diese Schritte in eigene Industrien (Dampfreformierer und Steamcracker) ausgelagert, so dass der Spieler selbst die Kontrolle darüber hat, wie viel Treibstoff, Wasserstoff und Ethylen er erzeugen will. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcfc00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Öl](#cargo_OIL_) | [Treibstoff](#cargo_PETR) |
|  | [Naphtha](#cargo_RFPR) |


<a name="industry_124"></a>
### Ölraffinerie

<img src="oil_refinery.png" alt="Ölraffinerie">

Ölraffinerien spalten Erdöl in verschiedene Bestandteile auf, die wiederum Grundstoffe für die gesamte chemische Industrie darstellen. So erhält man neben diversen Treibstoffen auch diverse Schmierstoffe, Flüssiggase und Heizöl. Darüber hinaus wird das Erdöl auch entschwefelt und von sonstigen Verunreinigungen befreit. In echten Raffinerien sind weitere Produktions- und Veredelungsschritte nachgeschaltet, so dass eine Raffinerie eine ganze Reihe von Produktion erzeugen kann. Im Set sind diese Schritte in eigene Industrien (Dampfreformierer und Steamcracker) ausgelagert, so dass der Spieler selbst die Kontrolle darüber hat, wie viel Treibstoff, Wasserstoff und Ethylen er erzeugen will. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_7) [Koks und Schwefel](#extension_5) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcfc00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Öl](#cargo_OIL_) | [Treibstoff](#cargo_PETR) |
|  | [Naphtha](#cargo_RFPR) |
|  | [Schwefel](#cargo_SULP) |


