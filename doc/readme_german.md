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

Die Vorräte können maximal 60.000 Einheiten speichern. Was passiert wenn man dieses Limit erreicht, hängt von den Einstellungen des Sets ab. Wenn das Verhalten auf "Verwerfen" gestellt ist, wird Fracht oberhalb des Limits einfach weggeworfen. Man kann weiterhin liefern und wird dafür bezahlt, die Fracht ist dann aber einfach weg.
Wenn man die Option auf "Annahme verweigern" stellt, wird die Industrie die Annahme der Fracht verweigern. Das bedeutet dann, dass auch der Bahnhof/Haltestelle neben der Industrie die Fracht nicht mehr akzeptiert. Man kann nun seine Fahrzeuge mittels bedingter Sprünge in der Auftragsliste zu anderen Industrien schicken. Sobald der Vorrat bei der Industrie gesunken ist, wird sie die Fracht auch wieder akzeptieren.

Da die Produktion mit der Menge der Vorräte skaliert sollte es schwierig sein, an diese Limitierungen zu stoßen, wenn man es nicht gerade darauf anlegt, weil man nicht alle notwendigen Rohstoffe bereitstellt.

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

[Autohaus](#industry_22) [Bauernhof](#industry_25) [Bauhof](#industry_37) [Eisenerzbergwerk](#industry_54) [Fahrzeugfabrik](#industry_64) [Fischgründe](#industry_89) [Hafen](#industry_104) [Hotel](#industry_120) [Integriertes Stahlwerk](#industry_123) [Kaufhaus](#industry_150) [Kohlebergwerk](#industry_151) [Kraftwerk](#industry_154) [Kunststofffabrik](#industry_158) [Laden](#industry_174) [Möbelfabrik](#industry_186) [Nahrungsmittelfabrik](#industry_191) [Sägewerk](#industry_235) [Tankstelle](#industry_241) [Wald](#industry_256) [Ölbohrinsel](#industry_265) [Ölquellen](#industry_266) 

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

Das Set enthält 17 Erweiterungen, die nachfolgend aufgelistet sind.

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
* [Aluhütte](#industry_2)
* [Aluhütte](#industry_3)


#### Modifizierte Industrien

* [Aluhütte](#industry_0)
* [Aluhütte](#industry_1)
* [Aluhütte](#industry_2)
* [Aluhütte](#industry_3)
* [Drahtwalzwerk](#industry_47)
* [Drahtwalzwerk](#industry_49)
* [Fahrzeugfabrik](#industry_65)
* [Fahrzeugfabrik](#industry_67)
* [Fahrzeugfabrik](#industry_69)
* [Fahrzeugfabrik](#industry_71)
* [Gießerei/Schmiede](#industry_93)
* [Gießerei/Schmiede](#industry_95)
* [Hafen](#industry_105)
* [Hafen](#industry_107)
* [Hafen](#industry_109)
* [Hafen](#industry_111)
* [Hafen](#industry_113)
* [Hafen](#industry_115)
* [Hafen](#industry_117)
* [Hafen](#industry_119)
* [Karosseriefabrik](#industry_146)
* [Karosseriefabrik](#industry_147)
* [Motorenwerk](#industry_182)
* [Motorenwerk](#industry_184)
* [Sprengstofffabrik](#industry_229)
* [Sprengstofffabrik](#industry_231)
* [Verpackungsmittelfabrik](#industry_245)
* [Verpackungsmittelfabrik](#industry_247)
* [Verpackungsmittelfabrik](#industry_249)
* [Verpackungsmittelfabrik](#industry_251)
* [Walzwerk](#industry_259)
* [Walzwerk](#industry_261)


<img src="industry_chain_extension_aluminium_de.png" alt="Industrieketten für Erweiterung Aluminium">

<a name="extension_1"></a>
### Ammoniak

Ammoniak, eine Verbindung aus Stickstoff und Wasserstoff, ist eine der wichtigsten Chemikalien überhaupt. Ohne ihn ist die moderne Landwirtschaft undenkbar, da Ammoniak essentiell für die Herstellung von Düngemitteln ist. Die Entwicklung einer technischen Synthese von Ammoniak nach dem Haber-Bosch-Verfahren war daher ein Meilenstein der Chemie und wurde mit dem Nobelpreis bedacht. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#508ca0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Ammoniak](#cargo_NH3_)
* [Sauerstoff](#cargo_O2__)
* [Soda](#cargo_SASH)
* [Stickstoff](#cargo_N2__)


### Neue Industrien

* [Ammoniakreaktor](#industry_4)
* [Luftzerleger](#industry_176)
* [Reinigungsmittelfabrik](#industry_209)
* [Reinigungsmittelfabrik](#industry_210)
* [Reinigungsmittelfabrik](#industry_211)
* [Reinigungsmittelfabrik](#industry_212)
* [Reinigungsmittelfabrik](#industry_213)
* [Reinigungsmittelfabrik](#industry_214)
* [Reinigungsmittelfabrik](#industry_215)
* [Reinigungsmittelfabrik](#industry_216)
* [Sodafabrik](#industry_227)


#### Modifizierte Industrien

* [Ammoniakreaktor](#industry_4)
* [Arzneimittelfabrik](#industry_14)
* [Arzneimittelfabrik](#industry_15)
* [Arzneimittelfabrik](#industry_16)
* [Arzneimittelfabrik](#industry_17)
* [Arzneimittelfabrik](#industry_18)
* [Arzneimittelfabrik](#industry_19)
* [Arzneimittelfabrik](#industry_20)
* [Arzneimittelfabrik](#industry_21)
* [Erzschmelze](#industry_58)
* [Erzschmelze](#industry_59)
* [Erzschmelze](#industry_62)
* [Erzschmelze](#industry_63)
* [Glasfabrik](#industry_97)
* [Glasfabrik](#industry_99)
* [Glasfabrik](#industry_101)
* [Glasfabrik](#industry_103)
* [Integriertes Stahlwerk](#industry_127)
* [Integriertes Stahlwerk](#industry_128)
* [Integriertes Stahlwerk](#industry_129)
* [Integriertes Stahlwerk](#industry_130)
* [Integriertes Stahlwerk](#industry_135)
* [Integriertes Stahlwerk](#industry_136)
* [Integriertes Stahlwerk](#industry_137)
* [Integriertes Stahlwerk](#industry_138)
* [Luftzerleger](#industry_176)
* [Reinigungsmittelfabrik](#industry_209)
* [Reinigungsmittelfabrik](#industry_210)
* [Reinigungsmittelfabrik](#industry_211)
* [Reinigungsmittelfabrik](#industry_212)
* [Reinigungsmittelfabrik](#industry_213)
* [Reinigungsmittelfabrik](#industry_214)
* [Reinigungsmittelfabrik](#industry_215)
* [Reinigungsmittelfabrik](#industry_216)
* [Rußfabrik](#industry_219)
* [Rußfabrik](#industry_220)
* [Sodafabrik](#industry_227)
* [Säurefabrik](#industry_239)
* [Säurefabrik](#industry_240)


<img src="industry_chain_extension_ammonia_de.png" alt="Industrieketten für Erweiterung Ammoniak">

<a name="extension_2"></a>
### Automobilbau

Automobilbau ist einer der wichtigsten Wirtschaftszweige Deutschlands. Immerhin wurden hier nicht nur das Automobil, sondern auch zahllose damit verbundene Technologien entwickelt. Namen wie Carl Benz, Rudolf Diesel oder Ferdinand Porsche - neben vielen anderen - haben Technikgeschichte geschrieben. Firmen wie Mercedes, BMW, Audi oder Porsche sind in aller Welt bekannt und sorgten für den guten Ruf von Fahrzeugen aus Deutschland. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Fahrzeugteile](#cargo_VPTS)
* [Karosserien](#cargo_VBOD)
* [Kautschuk](#cargo_RUBR)
* [Motoren](#cargo_VENG)
* [Reifen](#cargo_TYRE)
* [Zink](#cargo_ZINC)


### Neue Industrien

* [Fahrzeugteilefabrik](#industry_77)
* [Fahrzeugteilefabrik](#industry_78)
* [Fahrzeugteilefabrik](#industry_79)
* [Fahrzeugteilefabrik](#industry_80)
* [Fahrzeugteilefabrik](#industry_81)
* [Fahrzeugteilefabrik](#industry_82)
* [Fahrzeugteilefabrik](#industry_83)
* [Fahrzeugteilefabrik](#industry_84)
* [Karosseriefabrik](#industry_144)
* [Karosseriefabrik](#industry_145)
* [Karosseriefabrik](#industry_146)
* [Karosseriefabrik](#industry_147)
* [Karosseriefabrik](#industry_148)
* [Karosseriefabrik](#industry_149)
* [Motorenwerk](#industry_181)
* [Motorenwerk](#industry_182)
* [Motorenwerk](#industry_183)
* [Motorenwerk](#industry_184)
* [Reifenfabrik](#industry_207)
* [Reifenfabrik](#industry_208)
* [Synthesekautschukfabrik](#industry_233)
* [Synthesekautschukfabrik](#industry_234)


#### Modifizierte Industrien

* [Autohaus](#industry_23)
* [Erzschmelze](#industry_60)
* [Erzschmelze](#industry_61)
* [Erzschmelze](#industry_62)
* [Erzschmelze](#industry_63)
* [Fahrzeugfabrik](#industry_76)
* [Fahrzeugteilefabrik](#industry_77)
* [Fahrzeugteilefabrik](#industry_78)
* [Fahrzeugteilefabrik](#industry_79)
* [Fahrzeugteilefabrik](#industry_80)
* [Fahrzeugteilefabrik](#industry_81)
* [Fahrzeugteilefabrik](#industry_82)
* [Fahrzeugteilefabrik](#industry_83)
* [Fahrzeugteilefabrik](#industry_84)
* [Hafen](#industry_112)
* [Hafen](#industry_113)
* [Hafen](#industry_114)
* [Hafen](#industry_115)
* [Hafen](#industry_116)
* [Hafen](#industry_117)
* [Hafen](#industry_118)
* [Hafen](#industry_119)
* [Karosseriefabrik](#industry_144)
* [Karosseriefabrik](#industry_145)
* [Karosseriefabrik](#industry_146)
* [Karosseriefabrik](#industry_147)
* [Karosseriefabrik](#industry_148)
* [Karosseriefabrik](#industry_149)
* [Motorenwerk](#industry_181)
* [Motorenwerk](#industry_182)
* [Motorenwerk](#industry_183)
* [Motorenwerk](#industry_184)
* [Reifenfabrik](#industry_207)
* [Reifenfabrik](#industry_208)
* [Synthesekautschukfabrik](#industry_233)
* [Synthesekautschukfabrik](#industry_234)


<img src="industry_chain_extension_vehicle_de.png" alt="Industrieketten für Erweiterung Automobilbau">

<a name="extension_3"></a>
### Bauindustrie

Die Kunst des Bauens von steineren Wänden und Gebäuden ist eine der ältesten kulturellen Errungenschaften der Menschheit. Aus den Anfängen mit gebrannten Lehmziegeln entstand über Jahrhunderte ein eigener Industriezweig. Im 19. Jahrhundert wurde die industrielle Produktion von Ziegeln notwendig, aus denen man Fabrikhallen baute. Große Steinbrücken wie die Göltzschtalbrücke in Sachsen, die größte Ziegelsteinbrücke der Welt, zeigen eindrucksvoll wie wichtig diese Industriezweige waren. Die Ziegel wurden schließlich weitestgehend durch Zement und Beton verdrängt, was den Bau moderner Wolkenkratzer erst möglich macht. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#e8b810;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Kalkstein](#cargo_LIME)
* [Zement](#cargo_CMNT)
* [Ziegel](#cargo_BDMT)


### Neue Industrien

* [Kalksteinbergwerk](#industry_142)
* [Kalksteinbergwerk](#industry_143)
* [Sandgrube](#industry_223)
* [Zementfabrik](#industry_263)
* [Ziegelei](#industry_264)


#### Modifizierte Industrien

* [Bauhof](#industry_36)
* [Farbenfabrik](#industry_86)
* [Farbenfabrik](#industry_88)
* [Kalksteinbergwerk](#industry_142)
* [Kalksteinbergwerk](#industry_143)
* [Sandgrube](#industry_223)
* [Zementfabrik](#industry_263)
* [Ziegelei](#industry_264)


<img src="industry_chain_extension_building_industries_de.png" alt="Industrieketten für Erweiterung Bauindustrie">

<a name="extension_4"></a>
### Farbindustrie

Über tausende Jahre wurden Farben und Pigmente wie Indigo aus Pflanzen und diversen Pulvern hergestellt, was sie für industrielle Anwendungen schlicht zu teuer machte. Die Produktion künstlicher Farbmittel war eine der ersten wichtigen Anwendungen der noch jungen chemischen Industrie. Einige der wichtigsten chemischen Konzerne Deutschlands gehen auf Farbfabriken zurück, wie Agfa oder BASF (beide führen Teile des Namens auf Anilin zurück, eine Chemikalie, die in der Produktion von Farben eine bedeutende Rolle spielt). 1925 schlossen sich die größten Chemiekonzerne Deutschlands zur IG Farbengesellschaft zusammen und formten so die weltgrößte Chemiefirma. Selbst heute noch sind Farben, Pigmente und Färbemittel wichtige Produkte der Chemieindustrie und haben ein weites Feld von Anwendungen in der Textilindustrie, in der Kunststoffherstellung, im Bauwesen und nicht zuletzt im Automobilsektor. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#bc546c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Farbe](#cargo_COAT)
* [Kupfer](#cargo_COPR)
* [Kupfererz](#cargo_CORE)
* [Ruß](#cargo_CBLK)


### Neue Industrien

* [Farbenfabrik](#industry_85)
* [Farbenfabrik](#industry_86)
* [Farbenfabrik](#industry_87)
* [Farbenfabrik](#industry_88)
* [Kupfererzbergwerk](#industry_166)
* [Kupfererzbergwerk](#industry_167)
* [Kupfererzbergwerk](#industry_168)
* [Kupfererzbergwerk](#industry_169)
* [Kupferhütte](#industry_170)
* [Kupferhütte](#industry_171)
* [Kupferhütte](#industry_172)
* [Kupferhütte](#industry_173)
* [Rußfabrik](#industry_217)
* [Rußfabrik](#industry_218)
* [Rußfabrik](#industry_219)
* [Rußfabrik](#industry_220)


#### Modifizierte Industrien

* [Erzschmelze](#industry_57)
* [Erzschmelze](#industry_59)
* [Erzschmelze](#industry_61)
* [Erzschmelze](#industry_63)
* [Fahrzeugfabrik](#industry_66)
* [Fahrzeugfabrik](#industry_67)
* [Fahrzeugfabrik](#industry_70)
* [Fahrzeugfabrik](#industry_71)
* [Fahrzeugfabrik](#industry_73)
* [Fahrzeugfabrik](#industry_75)
* [Farbenfabrik](#industry_85)
* [Farbenfabrik](#industry_86)
* [Farbenfabrik](#industry_87)
* [Farbenfabrik](#industry_88)
* [Hafen](#industry_106)
* [Hafen](#industry_107)
* [Hafen](#industry_110)
* [Hafen](#industry_111)
* [Hafen](#industry_114)
* [Hafen](#industry_115)
* [Hafen](#industry_118)
* [Hafen](#industry_119)
* [Karosseriefabrik](#industry_145)
* [Karosseriefabrik](#industry_147)
* [Karosseriefabrik](#industry_149)
* [Kunststofffabrik](#industry_160)
* [Kunststofffabrik](#industry_161)
* [Kunststofffabrik](#industry_164)
* [Kunststofffabrik](#industry_165)
* [Kupfererzbergwerk](#industry_166)
* [Kupfererzbergwerk](#industry_167)
* [Kupfererzbergwerk](#industry_168)
* [Kupfererzbergwerk](#industry_169)
* [Kupferhütte](#industry_170)
* [Kupferhütte](#industry_171)
* [Kupferhütte](#industry_172)
* [Kupferhütte](#industry_173)
* [Reifenfabrik](#industry_208)
* [Rußfabrik](#industry_217)
* [Rußfabrik](#industry_218)
* [Rußfabrik](#industry_219)
* [Rußfabrik](#industry_220)
* [Textilfabrik](#industry_243)


<img src="industry_chain_extension_painting_industries_de.png" alt="Industrieketten für Erweiterung Farbindustrie">

<a name="extension_5"></a>
### Früchte und Bioenergie

Nachwachsende Rohstoffe werden seit der zweiten Hälfte des 20. Jahrhunderts immer bedeutsamer. Dementsprechend wird die Verwertung von Biomasse immer bedeutsamer. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#80a82c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Biomasse](#cargo_BIOM)
* [Früchte](#cargo_FRUT)


### Neue Industrien

* [Bioraffinerie](#industry_40)
* [Obstplantage](#industry_203)
* [Obstplantage](#industry_204)


#### Modifizierte Industrien

* [Bauernhof](#industry_27)
* [Bauernhof](#industry_28)
* [Bauernhof](#industry_29)
* [Bauernhof](#industry_33)
* [Bauernhof](#industry_34)
* [Bauernhof](#industry_35)
* [Bioraffinerie](#industry_40)
* [Dampfreformierer](#industry_45)
* [Hotel](#industry_121)
* [Kraftwerk](#industry_156)
* [Kraftwerk](#industry_157)
* [Laden](#industry_175)
* [Nahrungsmittelfabrik](#industry_199)
* [Nahrungsmittelfabrik](#industry_200)
* [Nahrungsmittelfabrik](#industry_201)
* [Nahrungsmittelfabrik](#industry_202)
* [Obstplantage](#industry_203)
* [Obstplantage](#industry_204)
* [Sägewerk](#industry_236)
* [Viehzucht](#industry_254)
* [Viehzucht](#industry_255)


<img src="industry_chain_extension_fruits_de.png" alt="Industrieketten für Erweiterung Früchte und Bioenergie">

<a name="extension_6"></a>
### Glas

Glas ist ein allgegenwärtiges Material im täglichen Leben. Die Erweiterung fügt Frachten und Industrien hinzu, die für die Herstellung von Glas relevant sind und verändert andere Industrien, so dass sie Glas, in erster Linie für Verpackungen, benötigen. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Branntkalk](#cargo_QLME)
* [Glas](#cargo_GLAS)


### Neue Industrien

* [Glasfabrik](#industry_96)
* [Glasfabrik](#industry_97)
* [Glasfabrik](#industry_98)
* [Glasfabrik](#industry_99)
* [Glasfabrik](#industry_100)
* [Glasfabrik](#industry_101)
* [Glasfabrik](#industry_102)
* [Glasfabrik](#industry_103)
* [Kalkbrennerei](#industry_140)
* [Kalkbrennerei](#industry_141)
* [Wertstoffhof](#industry_262)


#### Modifizierte Industrien

* [Brauerei](#industry_42)
* [Düngemittelfabrik](#industry_53)
* [Fahrzeugfabrik](#industry_68)
* [Fahrzeugfabrik](#industry_69)
* [Fahrzeugfabrik](#industry_70)
* [Fahrzeugfabrik](#industry_71)
* [Fahrzeugfabrik](#industry_74)
* [Fahrzeugfabrik](#industry_75)
* [Fahrzeugteilefabrik](#industry_79)
* [Fahrzeugteilefabrik](#industry_80)
* [Fahrzeugteilefabrik](#industry_83)
* [Fahrzeugteilefabrik](#industry_84)
* [Glasfabrik](#industry_96)
* [Glasfabrik](#industry_97)
* [Glasfabrik](#industry_98)
* [Glasfabrik](#industry_99)
* [Glasfabrik](#industry_100)
* [Glasfabrik](#industry_101)
* [Glasfabrik](#industry_102)
* [Glasfabrik](#industry_103)
* [Integriertes Stahlwerk](#industry_124)
* [Integriertes Stahlwerk](#industry_126)
* [Integriertes Stahlwerk](#industry_128)
* [Integriertes Stahlwerk](#industry_130)
* [Integriertes Stahlwerk](#industry_132)
* [Integriertes Stahlwerk](#industry_134)
* [Integriertes Stahlwerk](#industry_136)
* [Integriertes Stahlwerk](#industry_138)
* [Kalkbrennerei](#industry_140)
* [Kalkbrennerei](#industry_141)
* [Verpackungsmittelfabrik](#industry_246)
* [Verpackungsmittelfabrik](#industry_247)
* [Verpackungsmittelfabrik](#industry_250)
* [Verpackungsmittelfabrik](#industry_251)
* [Wertstoffhof](#industry_262)


<img src="industry_chain_extension_glass_de.png" alt="Industrieketten für Erweiterung Glas">

<a name="extension_7"></a>
### Grundlegende Anorganische Chemie

Anorganische Chemie beschäftigt sich mit chemischen Verbindungen, die nicht auf Kohlenstoff basieren. Dazu zählen zahllose Minerale, Säuren, Laugen und natürlich Metalle. Mit dem Fortschritt in der chemischen Forschung und der Entdeckung immer neuer Anwendungen wurden diese Stoffe immer wichtiger. Lange Zeit waren die Produktionsmengen von Schwefelsäure und Chlor wichtige Indikatoren für Aussagen über die Industrialisierung eines Landes. Die Erweiterung führt eine Reihe von grundlegenden Chemikalien und die zugehörigen Industrien ein, die wiederum eine Voraussetzung für andere Erweiterungen sind. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#b8dcc8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Chlor](#cargo_CHLO)
* [Natronlauge](#cargo_LYE_)
* [Salz](#cargo_SALT)
* [Wasserstoff](#cargo_H2__)


### Neue Industrien

* [Arzneimittelfabrik](#industry_6)
* [Arzneimittelfabrik](#industry_7)
* [Arzneimittelfabrik](#industry_8)
* [Arzneimittelfabrik](#industry_9)
* [Arzneimittelfabrik](#industry_10)
* [Arzneimittelfabrik](#industry_11)
* [Arzneimittelfabrik](#industry_12)
* [Arzneimittelfabrik](#industry_13)
* [Arzneimittelfabrik](#industry_14)
* [Arzneimittelfabrik](#industry_15)
* [Arzneimittelfabrik](#industry_16)
* [Arzneimittelfabrik](#industry_17)
* [Arzneimittelfabrik](#industry_18)
* [Arzneimittelfabrik](#industry_19)
* [Arzneimittelfabrik](#industry_20)
* [Arzneimittelfabrik](#industry_21)
* [Chloralkali Elektrolyseanlage](#industry_43)
* [Salzbergwerk](#industry_221)
* [Salzbergwerk](#industry_222)


#### Modifizierte Industrien

* [Aluhütte](#industry_1)
* [Aluhütte](#industry_3)
* [Arzneimittelfabrik](#industry_6)
* [Arzneimittelfabrik](#industry_7)
* [Arzneimittelfabrik](#industry_8)
* [Arzneimittelfabrik](#industry_9)
* [Arzneimittelfabrik](#industry_10)
* [Arzneimittelfabrik](#industry_11)
* [Arzneimittelfabrik](#industry_12)
* [Arzneimittelfabrik](#industry_13)
* [Arzneimittelfabrik](#industry_14)
* [Arzneimittelfabrik](#industry_15)
* [Arzneimittelfabrik](#industry_16)
* [Arzneimittelfabrik](#industry_17)
* [Arzneimittelfabrik](#industry_18)
* [Arzneimittelfabrik](#industry_19)
* [Arzneimittelfabrik](#industry_20)
* [Arzneimittelfabrik](#industry_21)
* [Chloralkali Elektrolyseanlage](#industry_43)
* [Kunststofffabrik](#industry_159)
* [Kunststofffabrik](#industry_161)
* [Kunststofffabrik](#industry_163)
* [Kunststofffabrik](#industry_165)
* [Molkerei](#industry_178)
* [Molkerei](#industry_180)
* [Nahrungsmittelfabrik](#industry_192)
* [Nahrungsmittelfabrik](#industry_194)
* [Nahrungsmittelfabrik](#industry_197)
* [Nahrungsmittelfabrik](#industry_198)
* [Nahrungsmittelfabrik](#industry_199)
* [Nahrungsmittelfabrik](#industry_200)
* [Nahrungsmittelfabrik](#industry_201)
* [Nahrungsmittelfabrik](#industry_202)
* [Salzbergwerk](#industry_221)
* [Salzbergwerk](#industry_222)
* [Säurefabrik](#industry_238)
* [Säurefabrik](#industry_240)


<img src="industry_chain_extension_basic_inorganic_chemistry_de.png" alt="Industrieketten für Erweiterung Grundlegende Anorganische Chemie">

<a name="extension_8"></a>
### Koks und Schwefel

Koks und Schwefel sind wichtige Chemikalien für die Industrie. Ohne Koks ist keine großtechnische Metallherstellung möglich, und Schwefel bzw. Schwefelsäure ist das Rückgrat zahlloser Industrien. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Koks](#cargo_COKE)
* [Kupferkies](#cargo_PORE)
* [Schwefel](#cargo_SULP)
* [Säure](#cargo_ACID)


### Neue Industrien

* [Erzschmelze](#industry_56)
* [Erzschmelze](#industry_57)
* [Erzschmelze](#industry_58)
* [Erzschmelze](#industry_59)
* [Erzschmelze](#industry_60)
* [Erzschmelze](#industry_61)
* [Erzschmelze](#industry_62)
* [Erzschmelze](#industry_63)
* [Kokerei](#industry_153)
* [Säurefabrik](#industry_237)
* [Säurefabrik](#industry_238)
* [Säurefabrik](#industry_239)
* [Säurefabrik](#industry_240)


#### Modifizierte Industrien

* [Arzneimittelfabrik](#industry_10)
* [Arzneimittelfabrik](#industry_11)
* [Arzneimittelfabrik](#industry_12)
* [Arzneimittelfabrik](#industry_13)
* [Arzneimittelfabrik](#industry_18)
* [Arzneimittelfabrik](#industry_19)
* [Arzneimittelfabrik](#industry_20)
* [Arzneimittelfabrik](#industry_21)
* [Erzschmelze](#industry_56)
* [Erzschmelze](#industry_57)
* [Erzschmelze](#industry_58)
* [Erzschmelze](#industry_59)
* [Erzschmelze](#industry_60)
* [Erzschmelze](#industry_61)
* [Erzschmelze](#industry_62)
* [Erzschmelze](#industry_63)
* [Farbenfabrik](#industry_87)
* [Farbenfabrik](#industry_88)
* [Hafen](#industry_108)
* [Hafen](#industry_109)
* [Hafen](#industry_110)
* [Hafen](#industry_111)
* [Hafen](#industry_116)
* [Hafen](#industry_117)
* [Hafen](#industry_118)
* [Hafen](#industry_119)
* [Integriertes Stahlwerk](#industry_125)
* [Integriertes Stahlwerk](#industry_126)
* [Integriertes Stahlwerk](#industry_129)
* [Integriertes Stahlwerk](#industry_130)
* [Integriertes Stahlwerk](#industry_133)
* [Integriertes Stahlwerk](#industry_134)
* [Integriertes Stahlwerk](#industry_137)
* [Integriertes Stahlwerk](#industry_138)
* [Kalkbrennerei](#industry_141)
* [Kokerei](#industry_153)
* [Kraftwerk](#industry_155)
* [Kraftwerk](#industry_157)
* [Kupfererzbergwerk](#industry_167)
* [Kupfererzbergwerk](#industry_169)
* [Kupferhütte](#industry_171)
* [Kupferhütte](#industry_173)
* [Reinigungsmittelfabrik](#industry_210)
* [Reinigungsmittelfabrik](#industry_212)
* [Reinigungsmittelfabrik](#industry_214)
* [Reinigungsmittelfabrik](#industry_216)
* [Säurefabrik](#industry_237)
* [Säurefabrik](#industry_238)
* [Säurefabrik](#industry_239)
* [Säurefabrik](#industry_240)
* [Ölraffinerie](#industry_268)


<img src="industry_chain_extension_coke_sulphur_de.png" alt="Industrieketten für Erweiterung Koks und Schwefel">

<a name="extension_9"></a>
### Lebensmittelindustrie

Die Lebensmittelindustrie sorgt dafür, dass die Supermärkte volle Regale haben. Deutschland ist bekannt für seine große Anzahl von Brotsorten und die hohe Dichte an Brauereien. Die Erweiterung ersetzt die generische Lebensmittelfabrik durch spezialisierte Betriebe, so dass die Transportaufgaben etwas komplexer werden. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#5c9c34;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Milch](#cargo_MILK)


### Neue Industrien

* [Brauerei](#industry_41)
* [Brauerei](#industry_42)
* [Molkerei](#industry_177)
* [Molkerei](#industry_178)
* [Molkerei](#industry_179)
* [Molkerei](#industry_180)
* [Mühle](#industry_189)
* [Mühle](#industry_190)
* [Schlachthof](#industry_224)
* [Schlachthof](#industry_225)
* [Viehzucht](#industry_252)
* [Viehzucht](#industry_253)
* [Viehzucht](#industry_254)
* [Viehzucht](#industry_255)


#### Modifizierte Industrien

* [Bauernhof](#industry_26)
* [Bauernhof](#industry_29)
* [Bauernhof](#industry_32)
* [Bauernhof](#industry_35)
* [Brauerei](#industry_41)
* [Brauerei](#industry_42)
* [Molkerei](#industry_177)
* [Molkerei](#industry_178)
* [Molkerei](#industry_179)
* [Molkerei](#industry_180)
* [Mühle](#industry_189)
* [Mühle](#industry_190)
* [Nahrungsmittelfabrik](#industry_193)
* [Nahrungsmittelfabrik](#industry_194)
* [Nahrungsmittelfabrik](#industry_196)
* [Nahrungsmittelfabrik](#industry_198)
* [Nahrungsmittelfabrik](#industry_200)
* [Nahrungsmittelfabrik](#industry_202)
* [Schlachthof](#industry_224)
* [Schlachthof](#industry_225)
* [Viehzucht](#industry_252)
* [Viehzucht](#industry_253)
* [Viehzucht](#industry_254)
* [Viehzucht](#industry_255)


<img src="industry_chain_extension_food_industries_de.png" alt="Industrieketten für Erweiterung Lebensmittelindustrie">

<a name="extension_10"></a>
### Metallurgie

Metallverarbeitung war schon im Altertum wichtig. Schmiede fertigten Werkzeuge und Waffen an. Mit der Industrialisierung stieg der Bedarf an hochwertigen Metallteilen, seien es Eisenbahnschienen, Zahnräder oder Motorenblöcke. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#8c6c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Bleche](#cargo_STSH)
* [Draht/Kabel](#cargo_STWR)
* [Maschinenteile](#cargo_ENSP)


### Neue Industrien

* [Drahtwalzwerk](#industry_46)
* [Drahtwalzwerk](#industry_47)
* [Drahtwalzwerk](#industry_48)
* [Drahtwalzwerk](#industry_49)
* [Gerätewerk](#industry_90)
* [Gerätewerk](#industry_91)
* [Gießerei/Schmiede](#industry_92)
* [Gießerei/Schmiede](#industry_93)
* [Gießerei/Schmiede](#industry_94)
* [Gießerei/Schmiede](#industry_95)
* [Walzwerk](#industry_258)
* [Walzwerk](#industry_259)
* [Walzwerk](#industry_260)
* [Walzwerk](#industry_261)


#### Modifizierte Industrien

* [Drahtwalzwerk](#industry_46)
* [Drahtwalzwerk](#industry_47)
* [Drahtwalzwerk](#industry_48)
* [Drahtwalzwerk](#industry_49)
* [Fahrzeugfabrik](#industry_72)
* [Fahrzeugfabrik](#industry_73)
* [Fahrzeugfabrik](#industry_74)
* [Fahrzeugfabrik](#industry_75)
* [Fahrzeugteilefabrik](#industry_81)
* [Fahrzeugteilefabrik](#industry_82)
* [Fahrzeugteilefabrik](#industry_83)
* [Fahrzeugteilefabrik](#industry_84)
* [Gerätewerk](#industry_90)
* [Gerätewerk](#industry_91)
* [Gießerei/Schmiede](#industry_92)
* [Gießerei/Schmiede](#industry_93)
* [Gießerei/Schmiede](#industry_94)
* [Gießerei/Schmiede](#industry_95)
* [Karosseriefabrik](#industry_148)
* [Karosseriefabrik](#industry_149)
* [Motorenwerk](#industry_183)
* [Motorenwerk](#industry_184)
* [Walzwerk](#industry_258)
* [Walzwerk](#industry_259)
* [Walzwerk](#industry_260)
* [Walzwerk](#industry_261)


<img src="industry_chain_extension_metallurgy_de.png" alt="Industrieketten für Erweiterung Metallurgie">

<a name="extension_11"></a>
### Organische Chemie

Die organische Chemie beschäftigt sich mit Kohlenwasserstoffen, also Verbindungen aus Kohlenstoff und Wasserstoff. Die Ausgangsstoffe (Kohle und vor allem Erdöl) sind durch Umwandlung organischer Stoffe (z.B. Pflanzen) über Jahrmillionen entstanden. Im 20. Jahrhundert wurde Erdöl zu einem der wichtigsten Rohstoffe der Menschheit, da es für die Produktion von Treibstoffen und Kunststoffen unverzichtbar ist. So werden täglich mehrere Milliarden Liter Erdöl verbraucht. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#787840;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Ethylen](#cargo_C2H4)
* [Naphtha](#cargo_RFPR)
* [Treibstoff](#cargo_PETR)


### Neue Industrien

* [Dampfreformierer](#industry_44)
* [Dampfreformierer](#industry_45)
* [Hydrierwerk](#industry_122)
* [Steamcracker](#industry_232)
* [Ölraffinerie](#industry_267)
* [Ölraffinerie](#industry_268)


#### Modifizierte Industrien

* [Arzneimittelfabrik](#industry_8)
* [Arzneimittelfabrik](#industry_9)
* [Arzneimittelfabrik](#industry_12)
* [Arzneimittelfabrik](#industry_13)
* [Arzneimittelfabrik](#industry_16)
* [Arzneimittelfabrik](#industry_17)
* [Arzneimittelfabrik](#industry_20)
* [Arzneimittelfabrik](#industry_21)
* [Dampfreformierer](#industry_44)
* [Dampfreformierer](#industry_45)
* [Hydrierwerk](#industry_122)
* [Kunststofffabrik](#industry_162)
* [Kunststofffabrik](#industry_163)
* [Kunststofffabrik](#industry_164)
* [Kunststofffabrik](#industry_165)
* [Rußfabrik](#industry_218)
* [Rußfabrik](#industry_220)
* [Sprengstofffabrik](#industry_230)
* [Sprengstofffabrik](#industry_231)
* [Steamcracker](#industry_232)
* [Synthesekautschukfabrik](#industry_234)
* [Ölraffinerie](#industry_267)
* [Ölraffinerie](#industry_268)


<img src="industry_chain_extension_organic_chemistry_de.png" alt="Industrieketten für Erweiterung Organische Chemie">

<a name="extension_12"></a>
### Papier

Papier ist ein allgegenwärtiges Material im täglichen Leben. Die Erweiterung fügt Frachten und Industrien hinzu, die für die Herstellung von Papier relevant sind und verändert andere Industrien, so dass sie Papier, in erster Linie für Verpackungen, benötigen. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#fcfcc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Papier](#cargo_PAPR)


### Neue Industrien

* [Druckerei](#industry_50)
* [Druckerei](#industry_51)
* [Papiermühle](#industry_205)
* [Papiermühle](#industry_206)
* [Wertstoffhof](#industry_262)


#### Modifizierte Industrien

* [Druckerei](#industry_50)
* [Druckerei](#industry_51)
* [Papiermühle](#industry_205)
* [Papiermühle](#industry_206)
* [Verpackungsmittelfabrik](#industry_248)
* [Verpackungsmittelfabrik](#industry_249)
* [Verpackungsmittelfabrik](#industry_250)
* [Verpackungsmittelfabrik](#industry_251)
* [Wertstoffhof](#industry_262)


<img src="industry_chain_extension_paper_de.png" alt="Industrieketten für Erweiterung Papier">

<a name="extension_13"></a>
### Produktionsboost

Bergwerke benötigen ebenso wie landwirtschaftliche Betriebe verschiedene Rohstoffe. Ohne Düngemittel ist moderne Landwirtschaft undenkbar, gleiches gilt für den Bergbau und die Verwendung von Sprengstoffen. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#fc907c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Ammoniumnitrat](#cargo_NHNO)
* [Düngemittel](#cargo_FERT)
* [Kalisalz](#cargo_POTA)
* [Sprengstoff](#cargo_BOOM)


### Neue Industrien

* [Ammoniumnitratfabrik](#industry_5)
* [Düngemittelfabrik](#industry_52)
* [Düngemittelfabrik](#industry_53)
* [Kalisalzbergwerk](#industry_139)
* [Sprengstofffabrik](#industry_228)
* [Sprengstofffabrik](#industry_229)
* [Sprengstofffabrik](#industry_230)
* [Sprengstofffabrik](#industry_231)


#### Modifizierte Industrien

* [Ammoniumnitratfabrik](#industry_5)
* [Bauernhof](#industry_30)
* [Bauernhof](#industry_31)
* [Bauernhof](#industry_32)
* [Bauernhof](#industry_33)
* [Bauernhof](#industry_34)
* [Bauernhof](#industry_35)
* [Düngemittelfabrik](#industry_52)
* [Düngemittelfabrik](#industry_53)
* [Eisenerzbergwerk](#industry_55)
* [Glasfabrik](#industry_100)
* [Glasfabrik](#industry_101)
* [Glasfabrik](#industry_102)
* [Glasfabrik](#industry_103)
* [Kalisalzbergwerk](#industry_139)
* [Kalksteinbergwerk](#industry_143)
* [Kohlebergwerk](#industry_152)
* [Kupfererzbergwerk](#industry_168)
* [Kupfererzbergwerk](#industry_169)
* [Obstplantage](#industry_204)
* [Reinigungsmittelfabrik](#industry_213)
* [Reinigungsmittelfabrik](#industry_214)
* [Reinigungsmittelfabrik](#industry_215)
* [Reinigungsmittelfabrik](#industry_216)
* [Salzbergwerk](#industry_222)
* [Sprengstofffabrik](#industry_228)
* [Sprengstofffabrik](#industry_229)
* [Sprengstofffabrik](#industry_230)
* [Sprengstofffabrik](#industry_231)
* [Wald](#industry_257)


<img src="industry_chain_extension_production_boost_de.png" alt="Industrieketten für Erweiterung Produktionsboost">

<a name="extension_14"></a>
### Recycling

Die erneute Verwendung von Wertstoffen in einer Art Kreislauf - eben Recycling - wurde in der zweiten Hälfte des 20. Jahrhunderts immer bedeutsamer. Einerseits reduziert man damit die Menge an Müll, andererseits aber auch die Menge an notwendigen teuren und/oder knappen Rohstoffen. In einigen Industriezweigen wie der Glas- oder Papierindustrie ist Recycling Standard. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#90e05c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Metallschrott](#cargo_SCMT)
* [Wertstoffe](#cargo_RCYC)


### Neue Industrien

* [Schrottplatz](#industry_226)
* [Wertstoffhof](#industry_262)


#### Modifizierte Industrien

* [Aluhütte](#industry_2)
* [Aluhütte](#industry_3)
* [Drahtwalzwerk](#industry_48)
* [Drahtwalzwerk](#industry_49)
* [Gießerei/Schmiede](#industry_94)
* [Gießerei/Schmiede](#industry_95)
* [Glasfabrik](#industry_98)
* [Glasfabrik](#industry_99)
* [Glasfabrik](#industry_102)
* [Glasfabrik](#industry_103)
* [Integriertes Stahlwerk](#industry_131)
* [Integriertes Stahlwerk](#industry_132)
* [Integriertes Stahlwerk](#industry_133)
* [Integriertes Stahlwerk](#industry_134)
* [Integriertes Stahlwerk](#industry_135)
* [Integriertes Stahlwerk](#industry_136)
* [Integriertes Stahlwerk](#industry_137)
* [Integriertes Stahlwerk](#industry_138)
* [Kupferhütte](#industry_172)
* [Kupferhütte](#industry_173)
* [Papiermühle](#industry_206)
* [Schrottplatz](#industry_226)
* [Walzwerk](#industry_260)
* [Walzwerk](#industry_261)
* [Wertstoffhof](#industry_262)


<img src="industry_chain_extension_recycling_de.png" alt="Industrieketten für Erweiterung Recycling">

<a name="extension_15"></a>
### Textilindustrie

Die Produktion von Garnen und Stoffen zur Herstellung von Kleidung war eine der ersten Kulturleistungen der Menscheit. Rohstoffe für die Produktion umfassen Wolle von Schafen und anderen Tieren als auch verschiedenste Pflanzenfasern wie Baumwolle. Innovationen der chemischen Industrie im 20. Jahrhundert brachten zusätzlich Kunstfasern wie polyester hervor. 

Die Herstellung von Stoffen war ein arbeitsintensiver Prozess und gehörte zu den ersten Bereichen, die von der Industrialisierung im 18. Jahrhundert erfasst wurden. Deutschland hatte eine große Textilindustrie in Sachsen und Schlesien, die wiederum von der Industrialisierung profitierte. Chemnitz wurde so zum Zentrum des Maschinenbaus mit einem Fokus auf die Herstellung von Textilmaschinen. Allerdings schrumpft die Industrie seit der Mitte des 20. Jahrhunderts, und heutzutage ist der Großteil der Produktion aus Kostengründen nach Asien abgewandert. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#d49480;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Textilien](#cargo_TEXT)
* [Wolle](#cargo_WOOL)


### Neue Industrien

* [Bekleidungsfabrik](#industry_38)
* [Bekleidungsfabrik](#industry_39)
* [Textilfabrik](#industry_242)
* [Textilfabrik](#industry_243)


#### Modifizierte Industrien

* [Bauernhof](#industry_24)
* [Bauernhof](#industry_27)
* [Bauernhof](#industry_30)
* [Bauernhof](#industry_33)
* [Bekleidungsfabrik](#industry_38)
* [Bekleidungsfabrik](#industry_39)
* [Fahrzeugteilefabrik](#industry_78)
* [Fahrzeugteilefabrik](#industry_80)
* [Fahrzeugteilefabrik](#industry_82)
* [Fahrzeugteilefabrik](#industry_84)
* [Möbelfabrik](#industry_185)
* [Möbelfabrik](#industry_187)
* [Textilfabrik](#industry_242)
* [Textilfabrik](#industry_243)
* [Viehzucht](#industry_253)
* [Viehzucht](#industry_255)


<img src="industry_chain_extension_textile_industries_de.png" alt="Industrieketten für Erweiterung Textilindustrie">

<a name="extension_16"></a>
### Verpackungsmittelindustrie

Die Verpackungsmittelindustrie produziert alle Arten von Behältern und Verpackungen, seien es Kartons oder Getränkedosen. Diese Erweiterung fügt damit ein zusätzliches logistisches Element für die Güter- und Nahrungsmittelproduktion hinzu. 

Farbe in Industriediagrammen auf dieser Seite:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

#### Frachten

* [Verpackungen](#cargo_MNSP)


### Neue Industrien

* [Verpackungsmittelfabrik](#industry_244)
* [Verpackungsmittelfabrik](#industry_245)
* [Verpackungsmittelfabrik](#industry_246)
* [Verpackungsmittelfabrik](#industry_247)
* [Verpackungsmittelfabrik](#industry_248)
* [Verpackungsmittelfabrik](#industry_249)
* [Verpackungsmittelfabrik](#industry_250)
* [Verpackungsmittelfabrik](#industry_251)


#### Modifizierte Industrien

* [Arzneimittelfabrik](#industry_7)
* [Arzneimittelfabrik](#industry_9)
* [Arzneimittelfabrik](#industry_11)
* [Arzneimittelfabrik](#industry_13)
* [Arzneimittelfabrik](#industry_15)
* [Arzneimittelfabrik](#industry_17)
* [Arzneimittelfabrik](#industry_19)
* [Arzneimittelfabrik](#industry_21)
* [Bekleidungsfabrik](#industry_39)
* [Druckerei](#industry_51)
* [Gerätewerk](#industry_91)
* [Molkerei](#industry_179)
* [Molkerei](#industry_180)
* [Möbelfabrik](#industry_187)
* [Möbelfabrik](#industry_188)
* [Mühle](#industry_190)
* [Nahrungsmittelfabrik](#industry_195)
* [Nahrungsmittelfabrik](#industry_196)
* [Nahrungsmittelfabrik](#industry_197)
* [Nahrungsmittelfabrik](#industry_198)
* [Nahrungsmittelfabrik](#industry_201)
* [Nahrungsmittelfabrik](#industry_202)
* [Reinigungsmittelfabrik](#industry_211)
* [Reinigungsmittelfabrik](#industry_212)
* [Reinigungsmittelfabrik](#industry_215)
* [Reinigungsmittelfabrik](#industry_216)
* [Schlachthof](#industry_225)
* [Verpackungsmittelfabrik](#industry_244)
* [Verpackungsmittelfabrik](#industry_245)
* [Verpackungsmittelfabrik](#industry_246)
* [Verpackungsmittelfabrik](#industry_247)
* [Verpackungsmittelfabrik](#industry_248)
* [Verpackungsmittelfabrik](#industry_249)
* [Verpackungsmittelfabrik](#industry_250)
* [Verpackungsmittelfabrik](#industry_251)


<img src="industry_chain_extension_packaging_industries_de.png" alt="Industrieketten für Erweiterung Verpackungsmittelindustrie">


## Cargos

Das Set enthält 64 Frachten, die nachfolgend aufgelistet sind.

<a name="cargo_ALUM"></a>
### Aluminium

Aluminium ist ein Leichtmetall, was praktisch überall dort zum Einsatz kommt, wo Stahl zu schwer ist. Man benötigt es zum Bau von Flugzeugen und Autos, aber auch für Haushaltsgegenstände wie Alufolie und Getränkedosen. Allerdings ist die Herstellung von reinem Aluminium ein relativ komplizierter und äußerst energieintensiver Prozess. Die Massenproduktion begann entsprechend erst im späten 19. Jahrhundert. Deutschland ist heute einer der größten Produzenten in Europa (und der größte Verbraucher), obwohl die Energiekosten vergleichsweise hoch liegen. 

Eintrag in der Frachttabelle: ALUM

Teil der Erweiterung: [Aluminium](#extension_0)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Aluhütte](#industry_0) | [Drahtwalzwerk](#industry_47) |
| [Aluhütte](#industry_1) | [Drahtwalzwerk](#industry_49) |
| [Aluhütte](#industry_2) | [Fahrzeugfabrik](#industry_65) |
| [Aluhütte](#industry_3) | [Fahrzeugfabrik](#industry_67) |
|  | [Fahrzeugfabrik](#industry_69) |
|  | [Fahrzeugfabrik](#industry_71) |
|  | [Gießerei/Schmiede](#industry_93) |
|  | [Gießerei/Schmiede](#industry_95) |
|  | [Karosseriefabrik](#industry_146) |
|  | [Karosseriefabrik](#industry_147) |
|  | [Motorenwerk](#industry_182) |
|  | [Motorenwerk](#industry_184) |
|  | [Sprengstofffabrik](#industry_229) |
|  | [Sprengstofffabrik](#industry_231) |
|  | [Verpackungsmittelfabrik](#industry_245) |
|  | [Verpackungsmittelfabrik](#industry_247) |
|  | [Verpackungsmittelfabrik](#industry_249) |
|  | [Verpackungsmittelfabrik](#industry_251) |
|  | [Walzwerk](#industry_259) |
|  | [Walzwerk](#industry_261) |

<a name="cargo_NH3_"></a>
### Ammoniak

Ammoniak ist eine chemische Verbindung von Wasserstoff und Stickstoff. Es ist ein Grundstoff der chemischen Industrie und unerlässlich für die Produktion von Düngemitteln. Dies wurde bereits im 19. Jahrhundert erkannt, es dauerte jedoch bis ins frühe 20. Jahrhundert, dass eine großtechnische Herstellung möglich wurde. Heute zählt Ammoniak zu den meistproduzierten Chemikalien der Welt und wird hauptsächlich zur Herstellung von Düngemitteln dient. Darüber hinaus wird aus Ammoniak Harnstoff hergestellt, welcher neben seiner Bedeutung als Düngemittel auch in der Abgasreinigung von Dieselmotoren benutzt wird. 

Eintrag in der Frachttabelle: NH3_

Teil der Erweiterung: [Ammoniak](#extension_1)

Frachtklassen: Flüssiggut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#508ca0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Ammoniakreaktor](#industry_4) | [Ammoniumnitratfabrik](#industry_5) |
|  | [Arzneimittelfabrik](#industry_14) |
|  | [Arzneimittelfabrik](#industry_15) |
|  | [Arzneimittelfabrik](#industry_16) |
|  | [Arzneimittelfabrik](#industry_17) |
|  | [Arzneimittelfabrik](#industry_18) |
|  | [Arzneimittelfabrik](#industry_19) |
|  | [Arzneimittelfabrik](#industry_20) |
|  | [Arzneimittelfabrik](#industry_21) |
|  | [Düngemittelfabrik](#industry_52) |
|  | [Düngemittelfabrik](#industry_53) |
|  | [Sodafabrik](#industry_227) |
|  | [Säurefabrik](#industry_239) |
|  | [Säurefabrik](#industry_240) |

<a name="cargo_NHNO"></a>
### Ammoniumnitrat

Ammoniumnitrat ist eine Stickstoffverbindung, die aus Ammoniak gewonnen wird. Sie hat eine immense Bedeutung als Düngemittel, ist gleichzeitig aber auch eine sehr labile Verbindung. Damit eignet es sich auch als Grundstoff für die Produktion von Sprengstoff. In der Geschichte führte Ammoniumnitrat zu diversen großen Unglücksfällen, so in Ludwigshafen 1921, in Texas City 1947 oder in Beirut 2020. Diese zählen zu den größten Explosionskatastrophen der Geschichte. 

Im Spiel wird das nicht so eng gesehen, es geht ja um den Transport, nicht um die richtige Handhabung von Gefahrgut. 

Eintrag in der Frachttabelle: NHNO

Teil der Erweiterung: [Produktionsboost](#extension_13)

Frachtklassen: Gefahrgut, Massengut, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b87818;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Ammoniumnitratfabrik](#industry_5) | [Düngemittelfabrik](#industry_52) |
|  | [Düngemittelfabrik](#industry_53) |
|  | [Sprengstofffabrik](#industry_228) |
|  | [Sprengstofffabrik](#industry_229) |
|  | [Sprengstofffabrik](#industry_230) |
|  | [Sprengstofffabrik](#industry_231) |

<a name="cargo_AORE"></a>
### Bauxit

Bauxit ist ein Erz aus welchem Aluminium hergestellt wird. Deutschland hat keine eigenen Bauxitlagerstätten und ist daher von Importen abhängig. 

Eintrag in der Frachttabelle: AORE

Teil der Erweiterung: [Aluminium](#extension_0)

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#541c10;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_105) | [Aluhütte](#industry_0) |
| [Hafen](#industry_107) | [Aluhütte](#industry_1) |
| [Hafen](#industry_109) | [Aluhütte](#industry_2) |
| [Hafen](#industry_111) | [Aluhütte](#industry_3) |
| [Hafen](#industry_113) |  |
| [Hafen](#industry_115) |  |
| [Hafen](#industry_117) |  |
| [Hafen](#industry_119) |  |

<a name="cargo_BIOM"></a>
### Biomasse

Biomasse, zumindest im Kontext des Sets, bezeichnet alle Arten von organischen Stoffen, die sich zur Gewinnung von Energie oder Chemikalien nutzen lassen. Dazu zählen in erster Linie organische Abfälle aus der Land- und Forstwirtschaft. 

Eintrag in der Frachttabelle: BIOM

Teil der Erweiterung: [Früchte und Bioenergie](#extension_5)

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#80a82c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bauernhof](#industry_27) | [Bioraffinerie](#industry_40) |
| [Bauernhof](#industry_28) | [Dampfreformierer](#industry_45) |
| [Bauernhof](#industry_29) | [Kraftwerk](#industry_156) |
| [Bauernhof](#industry_33) | [Kraftwerk](#industry_157) |
| [Bauernhof](#industry_34) |  |
| [Bauernhof](#industry_35) |  |
| [Sägewerk](#industry_236) |  |
| [Viehzucht](#industry_254) |  |
| [Viehzucht](#industry_255) |  |

<a name="cargo_STSH"></a>
### Bleche

Bleche sind ein gewalztes Produkt der Metallindustrie und werden in erster Linie in großer Menge in der Automobilindustrie benötigt. 

Eintrag in der Frachttabelle: STSH

Teil der Erweiterung: [Metallurgie](#extension_10)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Walzwerk](#industry_258) | [Fahrzeugfabrik](#industry_72) |
| [Walzwerk](#industry_259) | [Fahrzeugfabrik](#industry_73) |
| [Walzwerk](#industry_260) | [Fahrzeugfabrik](#industry_74) |
| [Walzwerk](#industry_261) | [Fahrzeugfabrik](#industry_75) |
|  | [Karosseriefabrik](#industry_148) |
|  | [Karosseriefabrik](#industry_149) |

<a name="cargo_QLME"></a>
### Branntkalk

Branntkalk ist chemisch gesehen Calciumoxid. Es ist eine sehr instabile Substanz, die schon mit Luftfeuchtigkeit reagiert. Sie reagiert auf gleiche Weise mit der Feuchtigkeit auf der Haut, wodurch gefährliche Verätzungen entstehen, daher wird es auch Ätzkalk genannt. Die Reaktion erzeugt außerdem Wärme, so dass von Branntkalk auch eine gewisse Brandgefahr ausgeht. Branntkalk ist ein wichtiger Betandteil von Mörtel und Zement, wird aber auch als Dünger und Desinfektionsmittel eingesetzt. Die wichtigste Anwendung liegt in der Stahlproduktion, wo er zum Entschwefeln von Roheisen verwendet wird. 

Eintrag in der Frachttabelle: QLME

Teil der Erweiterung: [Glas](#extension_6)

Frachtklassen: Massengut, Nässeempfindlich

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcfcc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kalkbrennerei](#industry_140) | [Düngemittelfabrik](#industry_53) |
| [Kalkbrennerei](#industry_141) | [Glasfabrik](#industry_96) |
|  | [Glasfabrik](#industry_97) |
|  | [Glasfabrik](#industry_98) |
|  | [Glasfabrik](#industry_99) |
|  | [Glasfabrik](#industry_100) |
|  | [Glasfabrik](#industry_101) |
|  | [Glasfabrik](#industry_102) |
|  | [Glasfabrik](#industry_103) |
|  | [Integriertes Stahlwerk](#industry_124) |
|  | [Integriertes Stahlwerk](#industry_126) |
|  | [Integriertes Stahlwerk](#industry_128) |
|  | [Integriertes Stahlwerk](#industry_130) |
|  | [Integriertes Stahlwerk](#industry_132) |
|  | [Integriertes Stahlwerk](#industry_134) |
|  | [Integriertes Stahlwerk](#industry_136) |
|  | [Integriertes Stahlwerk](#industry_138) |

<a name="cargo_CHLO"></a>
### Chlor

Chlor ist ein sehr reaktionsfreudiges chemisches Element, welches eine große Rolle in der Papierindustrie oder als Desinfektionsmittel spielt. Darüber hinaus wird es für zahllose Prozesse in der chemischen Industrie benötigt, hauptsächlich bei der Produktion von verschiedensten Kunststoffen wie PVC. In höheren Konzentrationen ist Chlor äußerst giftig und wurde in der Vergangenheit auch im Rahmen chemischer Kriegführung eingesetzt. Seit dem frühen 20. Jahrhundert wird Chlor hauptsächlich durch das Spalten von Salzlösungen durch Elektrolyse im sogenannten Chlor-Alkali-Prozess hergestellt. 

Eintrag in der Frachttabelle: CHLO

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_7)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b8dcc8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Chloralkali Elektrolyseanlage](#industry_43) | [Arzneimittelfabrik](#industry_6) |
|  | [Arzneimittelfabrik](#industry_7) |
|  | [Arzneimittelfabrik](#industry_8) |
|  | [Arzneimittelfabrik](#industry_9) |
|  | [Arzneimittelfabrik](#industry_10) |
|  | [Arzneimittelfabrik](#industry_11) |
|  | [Arzneimittelfabrik](#industry_12) |
|  | [Arzneimittelfabrik](#industry_13) |
|  | [Arzneimittelfabrik](#industry_14) |
|  | [Arzneimittelfabrik](#industry_15) |
|  | [Arzneimittelfabrik](#industry_16) |
|  | [Arzneimittelfabrik](#industry_17) |
|  | [Arzneimittelfabrik](#industry_18) |
|  | [Arzneimittelfabrik](#industry_19) |
|  | [Arzneimittelfabrik](#industry_20) |
|  | [Arzneimittelfabrik](#industry_21) |
|  | [Kunststofffabrik](#industry_159) |
|  | [Kunststofffabrik](#industry_161) |
|  | [Kunststofffabrik](#industry_163) |
|  | [Kunststofffabrik](#industry_165) |
|  | [Papiermühle](#industry_205) |
|  | [Papiermühle](#industry_206) |
|  | [Säurefabrik](#industry_238) |
|  | [Säurefabrik](#industry_240) |

<a name="cargo_STWR"></a>
### Draht/Kabel

Kabel und Drähte sind aus modernen elektrischen Geräten nicht wegzudenken. In Autos sind ebenfalls zahlreiche elektrische Komponenten verbaut, daher werden auch dort kilometerweise Kabel benötigt. 

Eintrag in der Frachttabelle: STWR

Teil der Erweiterung: [Metallurgie](#extension_10)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#8c6c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Drahtwalzwerk](#industry_46) | [Fahrzeugfabrik](#industry_72) |
| [Drahtwalzwerk](#industry_47) | [Fahrzeugfabrik](#industry_73) |
| [Drahtwalzwerk](#industry_48) | [Fahrzeugfabrik](#industry_74) |
| [Drahtwalzwerk](#industry_49) | [Fahrzeugfabrik](#industry_75) |
|  | [Fahrzeugteilefabrik](#industry_81) |
|  | [Fahrzeugteilefabrik](#industry_82) |
|  | [Fahrzeugteilefabrik](#industry_83) |
|  | [Fahrzeugteilefabrik](#industry_84) |
|  | [Gerätewerk](#industry_90) |
|  | [Gerätewerk](#industry_91) |
|  | [Motorenwerk](#industry_183) |
|  | [Motorenwerk](#industry_184) |

<a name="cargo_FERT"></a>
### Düngemittel

Die Verwendung von Düngemitteln in der Landwirtschaft ist so alt wie die Menschheit selbst. Während lange Zeit nur natürlicher Dünger genutzt wurde - Bauern kippen noch heute Gülle auf die Felder - wurden erst im frühen 20. Jahrhundert große Mengen künstlich hergestellter Düngemittel verfügbar. Diese basieren meist auf Stickstoffverbindungen, enthalten aber auch andere wichtige Chemikalien. 

Im Set dienen Düngemittel der Produktionssteigerung diverser landwirtschaftlicher Industrien. 

Eintrag in der Frachttabelle: FERT

Teil der Erweiterung: [Produktionsboost](#extension_13)

Frachtklassen: Massengut, Nässeempfindlich, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fc907c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Düngemittelfabrik](#industry_52) | [Bauernhof](#industry_30) |
| [Düngemittelfabrik](#industry_53) | [Bauernhof](#industry_31) |
|  | [Bauernhof](#industry_32) |
|  | [Bauernhof](#industry_33) |
|  | [Bauernhof](#industry_34) |
|  | [Bauernhof](#industry_35) |
|  | [Obstplantage](#industry_204) |
|  | [Wald](#industry_257) |

<a name="cargo_IORE"></a>
### Eisenerz

Die Menschheit nutzt Eisen seit der, tja, Eisenzeit vor etwa 3000 Jahren. Heutzutage wird Eisenerz quasi ausschließlich zur Produktion von Stahl genutzt, der wiederum eines der wichtigsten Materialien in der Weltwirtschaft darstellt. 

Deutschland hatte niemals große Vorkommen von Eisenerz und war immer auf Importe zum Beispiel aus Schweden angewiesen. 

Eintrag in der Frachttabelle: IORE

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Eisenerzbergwerk](#industry_54) | [Farbenfabrik](#industry_85) |
| [Eisenerzbergwerk](#industry_55) | [Farbenfabrik](#industry_86) |
| [Erzschmelze](#industry_56) | [Farbenfabrik](#industry_87) |
| [Erzschmelze](#industry_57) | [Farbenfabrik](#industry_88) |
| [Erzschmelze](#industry_58) | [Integriertes Stahlwerk](#industry_123) |
| [Erzschmelze](#industry_59) | [Integriertes Stahlwerk](#industry_124) |
| [Erzschmelze](#industry_60) | [Integriertes Stahlwerk](#industry_125) |
| [Erzschmelze](#industry_61) | [Integriertes Stahlwerk](#industry_126) |
| [Erzschmelze](#industry_62) | [Integriertes Stahlwerk](#industry_127) |
| [Erzschmelze](#industry_63) | [Integriertes Stahlwerk](#industry_128) |
| [Hafen](#industry_104) | [Integriertes Stahlwerk](#industry_129) |
| [Hafen](#industry_105) | [Integriertes Stahlwerk](#industry_130) |
| [Hafen](#industry_106) | [Integriertes Stahlwerk](#industry_131) |
| [Hafen](#industry_107) | [Integriertes Stahlwerk](#industry_132) |
| [Hafen](#industry_108) | [Integriertes Stahlwerk](#industry_133) |
| [Hafen](#industry_109) | [Integriertes Stahlwerk](#industry_134) |
| [Hafen](#industry_110) | [Integriertes Stahlwerk](#industry_135) |
| [Hafen](#industry_111) | [Integriertes Stahlwerk](#industry_136) |
| [Hafen](#industry_112) | [Integriertes Stahlwerk](#industry_137) |
| [Hafen](#industry_113) | [Integriertes Stahlwerk](#industry_138) |
| [Hafen](#industry_114) |  |
| [Hafen](#industry_115) |  |
| [Hafen](#industry_116) |  |
| [Hafen](#industry_117) |  |
| [Hafen](#industry_118) |  |
| [Hafen](#industry_119) |  |

<a name="cargo_C2H4"></a>
### Ethylen

Ethylen, chemisch korrekt Ethen, ist ein leichter Kohlenwasserstoff, der mit über 100 Millionen Tonnen Jahresproduktion die meistproduzierte organische Grundchemikalie darstellt. Etwa die Hälfte davon wird in der Kunststoffproduktion benötigt. Großtechnisch wird Ethylen heutzutage hauptsächlich durch Steamcracking gewonnen. Andere technische Prozesse wie die Kohleverflüssigung oder Biogasanlagen kommen ebenso zur Anwendung. 

Während Ethylen in der Realität in verschiedenen Fällen durch Pipelines (z.B. zwischen Rotterdam/Antwerpen und Ludwigshafen oder auch zwischen Ludwigshafen und Ingolstadt) transportiert wird, muss der Spieler den Transport selbst sicherstellen. 

Eintrag in der Frachttabelle: C2H4

Teil der Erweiterung: [Organische Chemie](#extension_11)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#787840;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bioraffinerie](#industry_40) | [Arzneimittelfabrik](#industry_8) |
| [Hydrierwerk](#industry_122) | [Arzneimittelfabrik](#industry_9) |
| [Steamcracker](#industry_232) | [Arzneimittelfabrik](#industry_12) |
|  | [Arzneimittelfabrik](#industry_13) |
|  | [Arzneimittelfabrik](#industry_16) |
|  | [Arzneimittelfabrik](#industry_17) |
|  | [Arzneimittelfabrik](#industry_20) |
|  | [Arzneimittelfabrik](#industry_21) |
|  | [Kunststofffabrik](#industry_162) |
|  | [Kunststofffabrik](#industry_163) |
|  | [Kunststofffabrik](#industry_164) |
|  | [Kunststofffabrik](#industry_165) |
|  | [Synthesekautschukfabrik](#industry_234) |

<a name="cargo_VEHI"></a>
### Fahrzeuge

Im weitesten Sinne sind Fahrzeuge selbstfahrende Landfahrzeuge zum Transport von Menschen und Gütern. In erster Linie sind damit natürlich Autos gemeint. 

Diese werden in Automobilfabriken gebaut und müssen nun in die Städte und zu den Exporthäfen transportiert werden. Autos sind eines der wichtigsten Exportgüter der deutschen Wirtschaft. Aus Sicht des Transports sind sie auch ein spezieller Fall, denn man braucht dafür besondere Eisenbahnwagen oder Lastwagen. 

Eintrag in der Frachttabelle: VEHI

Frachtklassen: Stückgut, Übergröße

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#bc546c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Fahrzeugfabrik](#industry_64) | [Autohaus](#industry_22) |
| [Fahrzeugfabrik](#industry_65) | [Autohaus](#industry_23) |
| [Fahrzeugfabrik](#industry_66) | [Hafen](#industry_104) |
| [Fahrzeugfabrik](#industry_67) | [Hafen](#industry_105) |
| [Fahrzeugfabrik](#industry_68) | [Hafen](#industry_106) |
| [Fahrzeugfabrik](#industry_69) | [Hafen](#industry_107) |
| [Fahrzeugfabrik](#industry_70) | [Hafen](#industry_108) |
| [Fahrzeugfabrik](#industry_71) | [Hafen](#industry_109) |
| [Fahrzeugfabrik](#industry_72) | [Hafen](#industry_110) |
| [Fahrzeugfabrik](#industry_73) | [Hafen](#industry_111) |
| [Fahrzeugfabrik](#industry_74) | [Hafen](#industry_112) |
| [Fahrzeugfabrik](#industry_75) | [Hafen](#industry_113) |
| [Fahrzeugfabrik](#industry_76) | [Hafen](#industry_114) |
|  | [Hafen](#industry_115) |
|  | [Hafen](#industry_116) |
|  | [Hafen](#industry_117) |
|  | [Hafen](#industry_118) |
|  | [Hafen](#industry_119) |

<a name="cargo_VPTS"></a>
### Fahrzeugteile

Fahrzeugteile können alles sein, was in Autos verbaut wird, vom Anlasser über Batterie, Getriebe, Sitze, Lenkräder bis hin zu allen Arten von elektronischen Bauteilen. 

Eintrag in der Frachttabelle: VPTS

Teil der Erweiterung: [Automobilbau](#extension_2)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Fahrzeugteilefabrik](#industry_77) | [Autohaus](#industry_23) |
| [Fahrzeugteilefabrik](#industry_78) | [Fahrzeugfabrik](#industry_76) |
| [Fahrzeugteilefabrik](#industry_79) |  |
| [Fahrzeugteilefabrik](#industry_80) |  |
| [Fahrzeugteilefabrik](#industry_81) |  |
| [Fahrzeugteilefabrik](#industry_82) |  |
| [Fahrzeugteilefabrik](#industry_83) |  |
| [Fahrzeugteilefabrik](#industry_84) |  |

<a name="cargo_COAT"></a>
### Farbe

Farben sind so alt wie die Menschheit und wurden schon vor zehntausenden Jahren für Höhlenmalereien benutzt. Zahlreiche verschieden Farben sind seit dem Altertum bekannt. Oftmals waren diese aber sehr teuer, da sie aufwändig aus seltenen Pflanzen gewonnen wurden. Die chemische Industrie hat zahllose künstliche Verbindungen entwickelt, aus denen sich Farben und Färbemittel herstellen lassen, die wiederum vielfältige Anwendungen haben. So werden Farben und Lacke im Automobilbau verwendet, während Färbemittel eine große Rolle in der Textilindustrie spielen, um nur einige zu nennen. Farben werden auch im Haushalt eingesetzt, zum Beispiel zum Streichen der Wände, und Tinte zum Schreiben ist ebenfalls ein Produkt der Farbenindustrie. 

Eintrag in der Frachttabelle: COAT

Teil der Erweiterung: [Farbindustrie](#extension_4)

Frachtklassen: Flüssiggut, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#bc546c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Farbenfabrik](#industry_85) | [Fahrzeugfabrik](#industry_66) |
| [Farbenfabrik](#industry_86) | [Fahrzeugfabrik](#industry_67) |
| [Farbenfabrik](#industry_87) | [Fahrzeugfabrik](#industry_70) |
| [Farbenfabrik](#industry_88) | [Fahrzeugfabrik](#industry_71) |
|  | [Fahrzeugfabrik](#industry_73) |
|  | [Fahrzeugfabrik](#industry_75) |
|  | [Karosseriefabrik](#industry_145) |
|  | [Karosseriefabrik](#industry_147) |
|  | [Karosseriefabrik](#industry_149) |
|  | [Kunststofffabrik](#industry_160) |
|  | [Kunststofffabrik](#industry_161) |
|  | [Kunststofffabrik](#industry_164) |
|  | [Kunststofffabrik](#industry_165) |
|  | [Textilfabrik](#industry_243) |

<a name="cargo_FISH"></a>
### Fisch

Menschen haben schon seit jeher Fische gefangen. Im Spiel stellt es den Spieler vor interessante Transportaufgaben, da der Fisch im Hafen umgeladen werden muss. 

Eintrag in der Frachttabelle: FISH

Frachtklassen: Expressgut, Kühlfracht

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#8c68fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Fischgründe](#industry_89) | [Nahrungsmittelfabrik](#industry_191) |
|  | [Nahrungsmittelfabrik](#industry_192) |
|  | [Nahrungsmittelfabrik](#industry_193) |
|  | [Nahrungsmittelfabrik](#industry_194) |
|  | [Nahrungsmittelfabrik](#industry_195) |
|  | [Nahrungsmittelfabrik](#industry_196) |
|  | [Nahrungsmittelfabrik](#industry_197) |
|  | [Nahrungsmittelfabrik](#industry_198) |
|  | [Nahrungsmittelfabrik](#industry_199) |
|  | [Nahrungsmittelfabrik](#industry_200) |
|  | [Nahrungsmittelfabrik](#industry_201) |
|  | [Nahrungsmittelfabrik](#industry_202) |

<a name="cargo_FRUT"></a>
### Früchte

Obst ist ein fester Bestandteil der Nahrung und muss als leicht verderbliche Ware besonders schnell transportiert werden. Der Transport von Südfrüchten wie Bananen erforderte beispielsweise besondere Kühlfahrzeuge. 

Eintrag in der Frachttabelle: FRUT

Teil der Erweiterung: [Früchte und Bioenergie](#extension_5)

Frachtklassen: Expressgut, Kühlfracht, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#306004;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Obstplantage](#industry_203) | [Bioraffinerie](#industry_40) |
| [Obstplantage](#industry_204) | [Hotel](#industry_121) |
|  | [Laden](#industry_175) |
|  | [Nahrungsmittelfabrik](#industry_199) |
|  | [Nahrungsmittelfabrik](#industry_200) |
|  | [Nahrungsmittelfabrik](#industry_201) |
|  | [Nahrungsmittelfabrik](#industry_202) |

<a name="cargo_GRAI"></a>
### Getreide

Deutschland ist bekannt für seine Vielfalt in Sachen Brot und Bier, und für beides braucht man Getreide. Deutschland ist einer der größten Getreideproduzenten Europas und kann den Bedarf vollständig selbst decken. Ein Großteil des Getreides wird als Tierfutter genutzt, nur ein Fünftel wird für in der Lebensmittelindustrie genutzt, und etwa 10% werden zum Bierbrauen gebraucht. Darüber hinaus wird viel Getreide, insbesondere Weizen, exportiert. 

Eintrag in der Frachttabelle: GRAI

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcfc00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bauernhof](#industry_24) | [Brauerei](#industry_41) |
| [Bauernhof](#industry_25) | [Brauerei](#industry_42) |
| [Bauernhof](#industry_26) | [Mühle](#industry_189) |
| [Bauernhof](#industry_27) | [Mühle](#industry_190) |
| [Bauernhof](#industry_28) | [Nahrungsmittelfabrik](#industry_191) |
| [Bauernhof](#industry_29) | [Nahrungsmittelfabrik](#industry_192) |
| [Bauernhof](#industry_30) | [Nahrungsmittelfabrik](#industry_195) |
| [Bauernhof](#industry_31) | [Nahrungsmittelfabrik](#industry_197) |
| [Bauernhof](#industry_32) | [Nahrungsmittelfabrik](#industry_199) |
| [Bauernhof](#industry_33) | [Nahrungsmittelfabrik](#industry_201) |
| [Bauernhof](#industry_34) | [Viehzucht](#industry_252) |
| [Bauernhof](#industry_35) | [Viehzucht](#industry_253) |
|  | [Viehzucht](#industry_254) |
|  | [Viehzucht](#industry_255) |

<a name="cargo_GLAS"></a>
### Glas

Glas ist der Sammelbegriff für eine Gruppe von Materialien mit speziellen physikalischen Eigenschaften. Die meisten Feststoffe haben eine geordnete molekulare Struktur, eine Art Raster wenn man so will. Glass hingegen hat eine ungeordnete Molekularstruktur, die man sonst nur bei Flüssigkeiten findet. Obwohl die dahinterliegende Physik bis heute nicht vollständig verstanden wurde, wurde Glass schon seit dem Altertum hergestellt. 

Üblicherweise meint man mit dem Wort Glas ein durchsichtiges Material aus Quarzsand. Glas ist chemisch gesehen extrem stabil, womit es sich prima als Material für Behälter für alle Arten von Flüssigkeiten, selbst Säuren, eignet. Tatsächlich ist Glas heutzutage omnipräsent. Man findet es als Fensterscheiben, in Form von Flaschen und Gläsern und natürlich in optischen Anwendungen als Linsen, Spiegel und natürlich als Brillenglas. 

Eintrag in der Frachttabelle: GLAS

Teil der Erweiterung: [Glas](#extension_6)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Glasfabrik](#industry_96) | [Brauerei](#industry_42) |
| [Glasfabrik](#industry_97) | [Fahrzeugfabrik](#industry_68) |
| [Glasfabrik](#industry_98) | [Fahrzeugfabrik](#industry_69) |
| [Glasfabrik](#industry_99) | [Fahrzeugfabrik](#industry_70) |
| [Glasfabrik](#industry_100) | [Fahrzeugfabrik](#industry_71) |
| [Glasfabrik](#industry_101) | [Fahrzeugfabrik](#industry_74) |
| [Glasfabrik](#industry_102) | [Fahrzeugfabrik](#industry_75) |
| [Glasfabrik](#industry_103) | [Fahrzeugteilefabrik](#industry_79) |
|  | [Fahrzeugteilefabrik](#industry_80) |
|  | [Fahrzeugteilefabrik](#industry_83) |
|  | [Fahrzeugteilefabrik](#industry_84) |
|  | [Verpackungsmittelfabrik](#industry_246) |
|  | [Verpackungsmittelfabrik](#industry_247) |
|  | [Verpackungsmittelfabrik](#industry_250) |
|  | [Verpackungsmittelfabrik](#industry_251) |

<a name="cargo_WOOD"></a>
### Holz

Holz wurde bereits von den ersten Menschen verwendet um Speere für die Jagd zu schnitzen oder um Feuer zu machen. Danach folgten Holzhütten, Schiffe, und irgendwann entwickelte man Papier aus Holzfasern. Heute ist Holz nach wie vor ein wichtiger Rohstoff und wird im 21. Jahrhundert wieder bedeutender, da es nachwächst. 

Deutschland ist reich an Wäldern, daher war Holz immer wirtschaftlich relevant. Heute ist Deutschland der größte Papierproduzent in Europa und hat auch eine bedeutsame Möbelindustrie 

Eintrag in der Frachttabelle: WOOD

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#74581c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Wald](#industry_256) | [Papiermühle](#industry_205) |
| [Wald](#industry_257) | [Papiermühle](#industry_206) |
|  | [Sägewerk](#industry_235) |
|  | [Sägewerk](#industry_236) |

<a name="cargo_POTA"></a>
### Kalisalz

Kalisalze sind Verbindungen auf der Basis von Kalium, während das handelsübliche Salz eine Natriumverbindung ist. Während Speisesalz schon seit dem Altertum bekannt ist und teilweise in Gold aufgewogen wurde, wurde die Bedeutung von Kalisalzen erst im 19. Jahrhundert erkannt. Seither erfolgte der Abbau, ausgehend von den ersten Schächten im damals preußischen Staßfurt. Bis nach dem ersten Weltkrieg hatte Deutschland das weltweite Monopol auf Kalisalze, noch heute ist Deutschland mit Abstand der größte Produzent in Europa. 

Das geförderte Salz wird quasi ausschließlich für die Düngemittelindustrie verwendet. 

Eintrag in der Frachttabelle: POTA

Teil der Erweiterung: [Produktionsboost](#extension_13)

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b88888;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kalisalzbergwerk](#industry_139) | [Düngemittelfabrik](#industry_52) |
|  | [Düngemittelfabrik](#industry_53) |
|  | [Glasfabrik](#industry_100) |
|  | [Glasfabrik](#industry_101) |
|  | [Glasfabrik](#industry_102) |
|  | [Glasfabrik](#industry_103) |
|  | [Reinigungsmittelfabrik](#industry_213) |
|  | [Reinigungsmittelfabrik](#industry_214) |
|  | [Reinigungsmittelfabrik](#industry_215) |
|  | [Reinigungsmittelfabrik](#industry_216) |

<a name="cargo_LIME"></a>
### Kalkstein

Kalkstein besteht in erster Linie aus Kalkverbindungen. Er wird zur Herstellung von Zement benötigt, kann aber auch direkt als Baumaterial benutzt werden. Darüber hinaus ist Kalkstein ein wichtiger Rohstoff in der Chemieindustrie und wichtig in der Produktion von Stahl und Glas. 

Eintrag in der Frachttabelle: LIME

Teil der Erweiterung: [Bauindustrie](#extension_3)

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kalksteinbergwerk](#industry_142) | [Farbenfabrik](#industry_86) |
| [Kalksteinbergwerk](#industry_143) | [Farbenfabrik](#industry_88) |
|  | [Kalkbrennerei](#industry_140) |
|  | [Kalkbrennerei](#industry_141) |
|  | [Sodafabrik](#industry_227) |
|  | [Zementfabrik](#industry_263) |

<a name="cargo_VBOD"></a>
### Karosserien

Karosserien sind die Hülle der Autos, in die dann die notwendige Technik eingebaut wird, um diese Hülle zum Fahren zu bringen. 

Eintrag in der Frachttabelle: VBOD

Teil der Erweiterung: [Automobilbau](#extension_2)

Frachtklassen: Stückgut, Übergröße

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#ccf0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Karosseriefabrik](#industry_144) | [Fahrzeugfabrik](#industry_76) |
| [Karosseriefabrik](#industry_145) |  |
| [Karosseriefabrik](#industry_146) |  |
| [Karosseriefabrik](#industry_147) |  |
| [Karosseriefabrik](#industry_148) |  |
| [Karosseriefabrik](#industry_149) |  |

<a name="cargo_RUBR"></a>
### Kautschuk

Kautschuk ist ein Naturprodukt, welches in erster Linie für die Herstellung von Gummi benötigt wird. Daraus lassen sich wiederum Reifen herstellen, wodurch Kautschuk wirtschaftlich bedeutsam ist. Da Naturkautschuk bei weitem nicht ausreicht, um den Bedarf der Industrie zu decken, wird er auch künstlich hergestellt. 

Eintrag in der Frachttabelle: RUBR

Teil der Erweiterung: [Automobilbau](#extension_2)

Frachtklassen: Flüssiggut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#081858;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_112) | [Reifenfabrik](#industry_207) |
| [Hafen](#industry_113) | [Reifenfabrik](#industry_208) |
| [Hafen](#industry_114) |  |
| [Hafen](#industry_115) |  |
| [Hafen](#industry_116) |  |
| [Hafen](#industry_117) |  |
| [Hafen](#industry_118) |  |
| [Hafen](#industry_119) |  |
| [Synthesekautschukfabrik](#industry_233) |  |
| [Synthesekautschukfabrik](#industry_234) |  |

<a name="cargo_COAL"></a>
### Kohle

Kohle war der wichtigste Faktor der industriellen Revolution des 19. Jahrhunderts, da es für den Antrieb von Dampfmaschinen gebraucht wird. Mit der Entwicklung von Eisenbahnen und Dampfschiffen und später Kraftwerken stieg der Bedarf an Kohle immer weiter. 

Deutschland hatte in mehreren Gebieten große Kohlevorkommen, diese Gebiete wie eben das Ruhrgebiet oder Schlesien wurden in der Folge Zentren der Industrialisierung. Kohle blieb während des gesamten 20. Jahrhunderts wichtig, wurde aber aus Gründen des Umweltschutzes nach und nach aus verschiedenen Bereichen verdrängt. 

Eintrag in der Frachttabelle: COAL

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_104) | [Hydrierwerk](#industry_122) |
| [Hafen](#industry_105) | [Integriertes Stahlwerk](#industry_123) |
| [Hafen](#industry_106) | [Integriertes Stahlwerk](#industry_124) |
| [Hafen](#industry_107) | [Integriertes Stahlwerk](#industry_127) |
| [Hafen](#industry_108) | [Integriertes Stahlwerk](#industry_128) |
| [Hafen](#industry_109) | [Integriertes Stahlwerk](#industry_131) |
| [Hafen](#industry_110) | [Integriertes Stahlwerk](#industry_132) |
| [Hafen](#industry_111) | [Integriertes Stahlwerk](#industry_135) |
| [Hafen](#industry_112) | [Integriertes Stahlwerk](#industry_136) |
| [Hafen](#industry_113) | [Kokerei](#industry_153) |
| [Hafen](#industry_114) | [Kraftwerk](#industry_154) |
| [Hafen](#industry_115) | [Kraftwerk](#industry_155) |
| [Hafen](#industry_116) | [Kraftwerk](#industry_156) |
| [Hafen](#industry_117) | [Kraftwerk](#industry_157) |
| [Hafen](#industry_118) | [Rußfabrik](#industry_217) |
| [Hafen](#industry_119) | [Rußfabrik](#industry_218) |
| [Kohlebergwerk](#industry_151) | [Rußfabrik](#industry_219) |
| [Kohlebergwerk](#industry_152) | [Rußfabrik](#industry_220) |
|  | [Ziegelei](#industry_264) |

<a name="cargo_COKE"></a>
### Koks

Koks ist hochreiner Kohlenstoff, der durch Pyrolyse aus Kohle gewonnen wird. Dabei wird die Kohle unter Sauerstoffabschluss großer Wärme ausgesetzt, wodurch die Kohle nicht verbrennen kann. Dabei werden diverse Verunreinigungen wie Schwefel und verschiedene Kohlenwasserstoffe abgeschieden. Koks wurde erstmals Anfang des 18. Jahrhunderts in England produziert und löste im 19. Jahrhundert die bisher verwendete Holzkohle als Befeuerung von Hochöfen ab. Erst damit war eine effiziente Eisenproduktion im Hochofen in großem Maßstab möglich. 

Eintrag in der Frachttabelle: COKE

Teil der Erweiterung: [Koks und Schwefel](#extension_8)

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kokerei](#industry_153) | [Erzschmelze](#industry_56) |
|  | [Erzschmelze](#industry_57) |
|  | [Erzschmelze](#industry_58) |
|  | [Erzschmelze](#industry_59) |
|  | [Erzschmelze](#industry_60) |
|  | [Erzschmelze](#industry_61) |
|  | [Erzschmelze](#industry_62) |
|  | [Erzschmelze](#industry_63) |
|  | [Gießerei/Schmiede](#industry_92) |
|  | [Gießerei/Schmiede](#industry_93) |
|  | [Gießerei/Schmiede](#industry_94) |
|  | [Gießerei/Schmiede](#industry_95) |
|  | [Integriertes Stahlwerk](#industry_125) |
|  | [Integriertes Stahlwerk](#industry_126) |
|  | [Integriertes Stahlwerk](#industry_129) |
|  | [Integriertes Stahlwerk](#industry_130) |
|  | [Integriertes Stahlwerk](#industry_133) |
|  | [Integriertes Stahlwerk](#industry_134) |
|  | [Integriertes Stahlwerk](#industry_137) |
|  | [Integriertes Stahlwerk](#industry_138) |
|  | [Kalkbrennerei](#industry_141) |

<a name="cargo_PLAS"></a>
### Kunststoffe

Kunststoffe umfassen eine ganze Reihe von synthetischen Materialien, die hauptsächlich aus Öl hergestellt werden. Sie wurden im frühen 20. Jahrhundert entwickelt und boten billige, leichte und haltbare Materialien für quasi jeden vorstellbaren Zweck. Der Großteil wird für Verpackungen benutzt, es gibt aber auch Verwendungen im Bauwesen (Rohrleitungen), in allen Arten von technischen Geräten wie Staubsaugern, aber auch im Möbelbau und als Spielzeug - als Legobaustein zum Beispiel. 

Im Set umfassen Kunststoffe nicht nur synthetische Materialien mit den namensgebenden plastischen Eigenschaften, sondern auch Kunstfasern wie Nylon und Polyester, die in der Textilindustrie relevant sind. 

Eintrag in der Frachttabelle: PLAS

Frachtklassen: Massengut, Nässeempfindlich

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kunststofffabrik](#industry_158) | [Fahrzeugfabrik](#industry_64) |
| [Kunststofffabrik](#industry_159) | [Fahrzeugfabrik](#industry_65) |
| [Kunststofffabrik](#industry_160) | [Fahrzeugfabrik](#industry_66) |
| [Kunststofffabrik](#industry_161) | [Fahrzeugfabrik](#industry_67) |
| [Kunststofffabrik](#industry_162) | [Fahrzeugfabrik](#industry_68) |
| [Kunststofffabrik](#industry_163) | [Fahrzeugfabrik](#industry_69) |
| [Kunststofffabrik](#industry_164) | [Fahrzeugfabrik](#industry_70) |
| [Kunststofffabrik](#industry_165) | [Fahrzeugfabrik](#industry_71) |
|  | [Fahrzeugfabrik](#industry_72) |
|  | [Fahrzeugfabrik](#industry_73) |
|  | [Fahrzeugfabrik](#industry_74) |
|  | [Fahrzeugfabrik](#industry_75) |
|  | [Fahrzeugteilefabrik](#industry_77) |
|  | [Fahrzeugteilefabrik](#industry_78) |
|  | [Fahrzeugteilefabrik](#industry_79) |
|  | [Fahrzeugteilefabrik](#industry_80) |
|  | [Fahrzeugteilefabrik](#industry_81) |
|  | [Fahrzeugteilefabrik](#industry_82) |
|  | [Fahrzeugteilefabrik](#industry_83) |
|  | [Fahrzeugteilefabrik](#industry_84) |
|  | [Gerätewerk](#industry_90) |
|  | [Gerätewerk](#industry_91) |
|  | [Möbelfabrik](#industry_185) |
|  | [Möbelfabrik](#industry_186) |
|  | [Möbelfabrik](#industry_187) |
|  | [Möbelfabrik](#industry_188) |
|  | [Textilfabrik](#industry_242) |
|  | [Textilfabrik](#industry_243) |
|  | [Verpackungsmittelfabrik](#industry_244) |
|  | [Verpackungsmittelfabrik](#industry_245) |
|  | [Verpackungsmittelfabrik](#industry_246) |
|  | [Verpackungsmittelfabrik](#industry_247) |
|  | [Verpackungsmittelfabrik](#industry_248) |
|  | [Verpackungsmittelfabrik](#industry_249) |
|  | [Verpackungsmittelfabrik](#industry_250) |
|  | [Verpackungsmittelfabrik](#industry_251) |

<a name="cargo_COPR"></a>
### Kupfer

Kupfer ist ein Metall, welches seit dem Altertum bekannt ist und zu den ersten von Menschen verwendeten Metallen gehört. Es ist leicht zu verarbeiten und hat zahlreiche Anwendungen. Heutzutage wird es hauptsächlich für Kabel und Drähte und alle Arten von elektrischen Bauteilen benutzt. In der Vergangenheit wurde es auch zur Herstellung von Farben und als Material für Dächer benutzt. 

Eintrag in der Frachttabelle: COPR

Teil der Erweiterung: [Farbindustrie](#extension_4)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Kupferhütte](#industry_170) | [Drahtwalzwerk](#industry_46) |
| [Kupferhütte](#industry_171) | [Drahtwalzwerk](#industry_47) |
| [Kupferhütte](#industry_172) | [Drahtwalzwerk](#industry_48) |
| [Kupferhütte](#industry_173) | [Drahtwalzwerk](#industry_49) |
|  | [Farbenfabrik](#industry_85) |
|  | [Farbenfabrik](#industry_86) |
|  | [Farbenfabrik](#industry_87) |
|  | [Farbenfabrik](#industry_88) |

<a name="cargo_CORE"></a>
### Kupfererz

Kupfererze kommen in verschiedenen Formen vor, die sich unterschiedlich gut zur Herstellung von Kupfer eignen. Der Abbau von Kupfererzen kann tausende von Jahren bis in die sogenannte Kupferzeit zurückverfolgt werden. Heutzutage ist Kupfererz von ein wichtiger Rohstoff, da Kupfer eines der wichtigsten Metalle für industrielle Zwecke ist. 

Deutschland hat keine bedeutsamen Vorkommen von Kupfererzen, allerdings wurden diese noch bis ins späte 20. Jahrhundert vorwiegend in Ostdeutschland abgebaut, weil man dort keinen Zugang zum Weltmarkt hatte. Allerdings hat Deutschland heute große Kapazitäten zur Produktion von Kupfer und ist ein großer Importeur von entsprechenden Erzen. 

Eintrag in der Frachttabelle: CORE

Teil der Erweiterung: [Farbindustrie](#extension_4)

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Erzschmelze](#industry_57) | [Kupferhütte](#industry_170) |
| [Erzschmelze](#industry_59) | [Kupferhütte](#industry_171) |
| [Erzschmelze](#industry_61) | [Kupferhütte](#industry_172) |
| [Erzschmelze](#industry_63) | [Kupferhütte](#industry_173) |
| [Hafen](#industry_106) |  |
| [Hafen](#industry_107) |  |
| [Hafen](#industry_114) |  |
| [Hafen](#industry_115) |  |
| [Kupfererzbergwerk](#industry_166) |  |
| [Kupfererzbergwerk](#industry_168) |  |

<a name="cargo_PORE"></a>
### Kupferkies

Kupfer kommt in der Natur quasi nur in Verbindungen mit anderen Stoffen vor. Eine häufige Verbindung ist das Mineral Chalkopyrit, auch als Kupferkies bezeichnet. Das ist eine Verbindung aus Kupfer, Eisen und Schwefel. Es ist aufgrund seines häufigen Vorkommens eines der wirtschaftlich bedeutsamsten Mineralien für die Produktion von Kupfer. 

Eintrag in der Frachttabelle: PORE

Teil der Erweiterung: [Koks und Schwefel](#extension_8)

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcf880;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hafen](#industry_108) | [Erzschmelze](#industry_56) |
| [Hafen](#industry_109) | [Erzschmelze](#industry_57) |
| [Hafen](#industry_110) | [Erzschmelze](#industry_58) |
| [Hafen](#industry_111) | [Erzschmelze](#industry_59) |
| [Hafen](#industry_116) | [Erzschmelze](#industry_60) |
| [Hafen](#industry_117) | [Erzschmelze](#industry_61) |
| [Hafen](#industry_118) | [Erzschmelze](#industry_62) |
| [Hafen](#industry_119) | [Erzschmelze](#industry_63) |
| [Kupfererzbergwerk](#industry_167) |  |
| [Kupfererzbergwerk](#industry_169) |  |

<a name="cargo_ENSP"></a>
### Maschinenteile

Mit der Entwicklung komplexer technischer Geräte wie Dampfmaschinen, Motoren, elektrischer Haushaltsgeräte oder des Automobils entwickelte sich auch eine spezialisierte Industrie zur Herstellung von Bauteilen. Egal ob Zahnräder, Ventile oder spezieller Baugruppen, kaum ein technisches Gerät kommt ohne diese Bauteile aus. 

Eintrag in der Frachttabelle: ENSP

Teil der Erweiterung: [Metallurgie](#extension_10)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#701020;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Gießerei/Schmiede](#industry_92) | [Fahrzeugfabrik](#industry_72) |
| [Gießerei/Schmiede](#industry_93) | [Fahrzeugfabrik](#industry_73) |
| [Gießerei/Schmiede](#industry_94) | [Fahrzeugfabrik](#industry_74) |
| [Gießerei/Schmiede](#industry_95) | [Fahrzeugfabrik](#industry_75) |
|  | [Gerätewerk](#industry_90) |
|  | [Gerätewerk](#industry_91) |
|  | [Motorenwerk](#industry_183) |
|  | [Motorenwerk](#industry_184) |

<a name="cargo_SCMT"></a>
### Metallschrott

Metallschrott fällt in vielen Varianten ab, sei es als Abfallprodukt beim Drehen und Fräsen, oder auch in großen Mengen auf Schrottplätzen. Dieser Metallschrott ist ein wichtiger Rohstoff in der metallproduzierenden Industrie. 

Eintrag in der Frachttabelle: SCMT

Teil der Erweiterung: [Recycling](#extension_14)

Frachtklassen: Massengut, Nicht schüttbar

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#404064;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Drahtwalzwerk](#industry_48) | [Aluhütte](#industry_2) |
| [Drahtwalzwerk](#industry_49) | [Aluhütte](#industry_3) |
| [Gießerei/Schmiede](#industry_94) | [Integriertes Stahlwerk](#industry_131) |
| [Gießerei/Schmiede](#industry_95) | [Integriertes Stahlwerk](#industry_132) |
| [Schrottplatz](#industry_226) | [Integriertes Stahlwerk](#industry_133) |
| [Walzwerk](#industry_260) | [Integriertes Stahlwerk](#industry_134) |
| [Walzwerk](#industry_261) | [Integriertes Stahlwerk](#industry_135) |
|  | [Integriertes Stahlwerk](#industry_136) |
|  | [Integriertes Stahlwerk](#industry_137) |
|  | [Integriertes Stahlwerk](#industry_138) |
|  | [Kupferhütte](#industry_172) |
|  | [Kupferhütte](#industry_173) |

<a name="cargo_MILK"></a>
### Milch

Milch von Kühen und anderen Tieren wird seit Jahrtausenden als Nahrungsmittel genutzt. Sie wird nicht nur getrunken, sondern ist auch die Basis für die Herstellung anderer Lebensmettel wie Käse, Butter, Joghurt oder Eiscreme. 

Eintrag in der Frachttabelle: MILK

Teil der Erweiterung: [Lebensmittelindustrie](#extension_9)

Frachtklassen: Expressgut, Flüssiggut, Kühlfracht

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#e0f4fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Viehzucht](#industry_252) | [Molkerei](#industry_177) |
| [Viehzucht](#industry_253) | [Molkerei](#industry_178) |
| [Viehzucht](#industry_254) | [Molkerei](#industry_179) |
| [Viehzucht](#industry_255) | [Molkerei](#industry_180) |

<a name="cargo_VENG"></a>
### Motoren

Motoren sind das Herzstück von Fahrzeugen, insbesondere Autos. Sowohl Otto- als auch Dieselmotoren wurden in Deutschland erfunden. 

Eintrag in der Frachttabelle: VENG

Teil der Erweiterung: [Automobilbau](#extension_2)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Motorenwerk](#industry_181) | [Fahrzeugfabrik](#industry_76) |
| [Motorenwerk](#industry_182) |  |
| [Motorenwerk](#industry_183) |  |
| [Motorenwerk](#industry_184) |  |

<a name="cargo_FOOD"></a>
### Nahrungsmittel

Jeder muss essen, und seitdem Menschen in Städten leben gab den Bedarf, Lebensmittel in die Städte zu transportieren. Selbst heute noch kann man frisches Obst und Gemüse auf dem Wochenmarkt kaufen, während der Großteil der industriell produzierten Lebensmittel von den Fabriken zu Supermärkten transportiert wird. 

Eintrag in der Frachttabelle: FOOD

Frachtklassen: Expressgut, Kühlfracht

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Brauerei](#industry_41) | [Hotel](#industry_120) |
| [Brauerei](#industry_42) | [Hotel](#industry_121) |
| [Molkerei](#industry_177) | [Laden](#industry_174) |
| [Molkerei](#industry_178) | [Laden](#industry_175) |
| [Molkerei](#industry_179) |  |
| [Molkerei](#industry_180) |  |
| [Mühle](#industry_189) |  |
| [Mühle](#industry_190) |  |
| [Nahrungsmittelfabrik](#industry_191) |  |
| [Nahrungsmittelfabrik](#industry_192) |  |
| [Nahrungsmittelfabrik](#industry_193) |  |
| [Nahrungsmittelfabrik](#industry_194) |  |
| [Nahrungsmittelfabrik](#industry_195) |  |
| [Nahrungsmittelfabrik](#industry_196) |  |
| [Nahrungsmittelfabrik](#industry_197) |  |
| [Nahrungsmittelfabrik](#industry_198) |  |
| [Nahrungsmittelfabrik](#industry_199) |  |
| [Nahrungsmittelfabrik](#industry_200) |  |
| [Nahrungsmittelfabrik](#industry_201) |  |
| [Nahrungsmittelfabrik](#industry_202) |  |
| [Schlachthof](#industry_224) |  |
| [Schlachthof](#industry_225) |  |

<a name="cargo_RFPR"></a>
### Naphtha

Naphtha, auch Rohbenzin genannt, ist ein Produkt aus der Destillation von Erdöl, wie es in Raffinerien stattfindet. Es enthält eine Vielzahl verschiedener Kohlenwasserstoffe, die in weiteren Schritten voneinander getrennt werden. Somit ist es in der chemischen Industrie ein unverzichtbares Zwischenprodukt bei der Herstellung von Kraft- und Schmierstoffen, aber auch bei der Herstellung von Ethylen. 

Eintrag in der Frachttabelle: RFPR

Teil der Erweiterung: [Organische Chemie](#extension_11)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#403c0c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Ölraffinerie](#industry_267) | [Arzneimittelfabrik](#industry_8) |
| [Ölraffinerie](#industry_268) | [Arzneimittelfabrik](#industry_9) |
|  | [Arzneimittelfabrik](#industry_12) |
|  | [Arzneimittelfabrik](#industry_13) |
|  | [Arzneimittelfabrik](#industry_16) |
|  | [Arzneimittelfabrik](#industry_17) |
|  | [Arzneimittelfabrik](#industry_20) |
|  | [Arzneimittelfabrik](#industry_21) |
|  | [Dampfreformierer](#industry_44) |
|  | [Dampfreformierer](#industry_45) |
|  | [Rußfabrik](#industry_218) |
|  | [Rußfabrik](#industry_220) |
|  | [Steamcracker](#industry_232) |

<a name="cargo_LYE_"></a>
### Natronlauge

Natronlauge ist eine basische Lösung. Sie hat eine große Bedeutung in der Produktion von Waschmitteln und Seifen, aber auch in der Lebensmittelindustrie und in anderen Bereichen. Ein Großteil der Natronlauge wird in der Papierherstellung benötigt, darüber hinaus findet es Anwendung in der Produktion von Färbemitteln und Bleichmachern. Natronlauge wird zusammen mit Chlor aus der elektrolytischen Spaltung von Salzlösungen im sogenannten Chlor-Alkali-Prozess gewonnen. 

Eintrag in der Frachttabelle: LYE_

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_7)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#78a488;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Chloralkali Elektrolyseanlage](#industry_43) | [Aluhütte](#industry_1) |
|  | [Aluhütte](#industry_3) |
|  | [Drahtwalzwerk](#industry_46) |
|  | [Drahtwalzwerk](#industry_47) |
|  | [Drahtwalzwerk](#industry_48) |
|  | [Drahtwalzwerk](#industry_49) |
|  | [Molkerei](#industry_178) |
|  | [Molkerei](#industry_180) |
|  | [Nahrungsmittelfabrik](#industry_192) |
|  | [Nahrungsmittelfabrik](#industry_194) |
|  | [Nahrungsmittelfabrik](#industry_197) |
|  | [Nahrungsmittelfabrik](#industry_198) |
|  | [Nahrungsmittelfabrik](#industry_199) |
|  | [Nahrungsmittelfabrik](#industry_200) |
|  | [Nahrungsmittelfabrik](#industry_201) |
|  | [Nahrungsmittelfabrik](#industry_202) |
|  | [Papiermühle](#industry_205) |
|  | [Papiermühle](#industry_206) |
|  | [Walzwerk](#industry_258) |
|  | [Walzwerk](#industry_259) |
|  | [Walzwerk](#industry_260) |
|  | [Walzwerk](#industry_261) |

<a name="cargo_PAPR"></a>
### Papier

Papier besteht aus getrockneten Zellulosefasern und ist seit dem Altertum bekannt. Damals schrieb man bereits auf Papyrus. Es dauerte jedoch bis zum 19. Jahrhundert, um dank der Fortschritte der chemischen Forschung zu verstehen, wie man Zellulose aus Holzfasern gewinnen kann. Dies erlaubte eine industrielle Massenfertigung von allen möglichen Papiersorten. Heute ist Papier omnipräsent, vom hochwertigem Briefpaper über das weitverbreitete Papier für den Drucker im Büro, dünneres Papier für Zeitungsdruck, stabilere Pappe für Verpackungen bis hin zu Toilettenpapier. 

Eintrag in der Frachttabelle: PAPR

Teil der Erweiterung: [Papier](#extension_12)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b8b8b8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Papiermühle](#industry_205) | [Druckerei](#industry_50) |
| [Papiermühle](#industry_206) | [Druckerei](#industry_51) |
|  | [Verpackungsmittelfabrik](#industry_248) |
|  | [Verpackungsmittelfabrik](#industry_249) |
|  | [Verpackungsmittelfabrik](#industry_250) |
|  | [Verpackungsmittelfabrik](#industry_251) |

<a name="cargo_PASS"></a>
### Passagiere

Ob es nun Urlaub oder Dienstreise ist - Menschen müssen und wollen verreisen. Jahrhundertelang hieß Reisen Laufen oder Reiten, technische Innovationen beschleunigten das Reisen jedoch erheblich. Man baute Häfen, Straßen und später Eisenbahnen und schließlich Flughäfen. Das Reisen wurde nicht nur schneller, sondern auch preiswerter - und heutzutage sind Reisen möglich, die vor noch gar nicht langer Zeit völlig undenkbar waren. 

Eintrag in der Frachttabelle: PASS

Frachtklassen: Passagiere

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#80c4fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Hotel](#industry_120) | [Hotel](#industry_120) |
| [Hotel](#industry_121) | [Hotel](#industry_121) |
| [Ölbohrinsel](#industry_265) | [Ölbohrinsel](#industry_265) |

<a name="cargo_MAIL"></a>
### Post

Der Transport von Post war schon immer eine wichtige Aufgabe eines jeden Verkehrsnetzes. Jahrhunderte lang waren Postkutschen im Einsatz, bevor sie von Eisenbahnen und Lastwagen verdrängt wurden. Während die Anzahl der transportierten Briefe und Postkarten im 21. Jahrhundert zurückgeht - man schickt Nachrichten übers Internet - ist der Transport von Paketen heutzutage wichtiger denn je, Onlineshopping sei Dank. 

Eintrag in der Frachttabelle: MAIL

Frachtklassen: Post

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcfcfc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |

<a name="cargo_TYRE"></a>
### Reifen

Reifen sind ein relevanter Bestandteil für Autos, Lastwagen, Fahrräder und andere Fahrzeuge. Milliarden Reifen werden pro Jahr produziert. 

Eintrag in der Frachttabelle: TYRE

Teil der Erweiterung: [Automobilbau](#extension_2)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#14347c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Reifenfabrik](#industry_207) | [Autohaus](#industry_23) |
| [Reifenfabrik](#industry_208) | [Fahrzeugfabrik](#industry_76) |

<a name="cargo_CBLK"></a>
### Ruß

Ruß ist ein Pulver von praktisch reinem Kohlenstoff. Es wird als schwarzes Pigment für Farben, Tinten und in der Kunststoffherstellung benutzt. Haupteinsatzgebiet ist jedoch die Reifenherstellung für den Automobilbau. 

Eintrag in der Frachttabelle: CBLK

Teil der Erweiterung: [Farbindustrie](#extension_4)

Frachtklassen: Massengut, Nässeempfindlich, Pulver, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#343c48;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Rußfabrik](#industry_217) | [Farbenfabrik](#industry_85) |
| [Rußfabrik](#industry_218) | [Farbenfabrik](#industry_86) |
| [Rußfabrik](#industry_219) | [Farbenfabrik](#industry_87) |
| [Rußfabrik](#industry_220) | [Farbenfabrik](#industry_88) |
|  | [Reifenfabrik](#industry_208) |

<a name="cargo_SALT"></a>
### Salz

Salz wird seit dem Altertum verwendet, um Nahrungsmittel haltbar zu machen. Bis ins ausgehende Mittelalter wurde Salz als weißes Gold gehandelt und spielte eine entscheidende Rolle im Bereich Handel, Steuerrecht und Wirtschaft im Allgemeinen. Das veränderte sich erst, als Salzbergbau im 19. Jahrhundert technisch möglich und praktikabel wurde. Darüber hinaus wurde Salz durch Fortschritte in der Wissenschaft und Chemie zu dieser Zeit ein grundlegender Rohstoff in der Produktion von Chlor, Natronlauge und Soda, die wiederum zu den wichtigsten Rohstoffen in der chemischen Industrie zählen. Heutzutage werden etwa 80% des in Deutschland geförderten Salzes für industrielle Zwecke genutzt, weniger als 5% werden in der Lebensmittelindustrie eingesetzt. 

Eintrag in der Frachttabelle: SALT

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_7)

Frachtklassen: Massengut, Nässeempfindlich

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#d4d4e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Salzbergwerk](#industry_221) | [Chloralkali Elektrolyseanlage](#industry_43) |
| [Salzbergwerk](#industry_222) | [Nahrungsmittelfabrik](#industry_192) |
|  | [Nahrungsmittelfabrik](#industry_194) |
|  | [Nahrungsmittelfabrik](#industry_197) |
|  | [Nahrungsmittelfabrik](#industry_198) |
|  | [Nahrungsmittelfabrik](#industry_199) |
|  | [Nahrungsmittelfabrik](#industry_200) |
|  | [Nahrungsmittelfabrik](#industry_201) |
|  | [Nahrungsmittelfabrik](#industry_202) |
|  | [Sodafabrik](#industry_227) |

<a name="cargo_SAND"></a>
### Sand

Sand findet man quasi überall in der Welt. Er besteht hauptsächlich aus Silikatverbindugnen in Partikeln unterschiedlicher Größe. Sand wird maßgeblich in der Bauindustrie benötigt, zum Beispiel bei der Herstellung von Mörtel und Beton, aber auch als Quelle für Silizium, welches wiederum wichtig für elektronische Bauteile ist. 

Eintrag in der Frachttabelle: SAND

Frachtklassen: Massengut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#e8b810;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Sandgrube](#industry_223) | [Bauhof](#industry_36) |
|  | [Glasfabrik](#industry_96) |
|  | [Glasfabrik](#industry_97) |
|  | [Glasfabrik](#industry_98) |
|  | [Glasfabrik](#industry_99) |
|  | [Glasfabrik](#industry_100) |
|  | [Glasfabrik](#industry_101) |
|  | [Glasfabrik](#industry_102) |
|  | [Glasfabrik](#industry_103) |
|  | [Zementfabrik](#industry_263) |

<a name="cargo_O2__"></a>
### Sauerstoff

Sauerstoff ist eines der häufigsten und am weitesten verbreiteten chemischen Elemente. Er ist Teil der Luft und kommt darüber hinaus in zahllosen Verbindungen vor, insbesondere als Wasser. Für Lebewesen ist Sauerstoff lebensnotwendig. Industriell hat Sauerstoff große Bedeutung: Er ist essentiell für Verbrennungsprozesse, bei denen hohe Temperaturen erreicht werden müssen. Dementsprechend findet er weite Anwendung in der Metallurgie, aber auch in diversen chemischen Prozessen wie der Herstellung von Säuren. 

Eintrag in der Frachttabelle: O2__

Teil der Erweiterung: [Ammoniak](#extension_1)

Frachtklassen: Flüssiggut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#0060d4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Luftzerleger](#industry_176) | [Arzneimittelfabrik](#industry_14) |
|  | [Arzneimittelfabrik](#industry_15) |
|  | [Arzneimittelfabrik](#industry_16) |
|  | [Arzneimittelfabrik](#industry_17) |
|  | [Arzneimittelfabrik](#industry_18) |
|  | [Arzneimittelfabrik](#industry_19) |
|  | [Arzneimittelfabrik](#industry_20) |
|  | [Arzneimittelfabrik](#industry_21) |
|  | [Erzschmelze](#industry_58) |
|  | [Erzschmelze](#industry_59) |
|  | [Erzschmelze](#industry_62) |
|  | [Erzschmelze](#industry_63) |
|  | [Integriertes Stahlwerk](#industry_127) |
|  | [Integriertes Stahlwerk](#industry_128) |
|  | [Integriertes Stahlwerk](#industry_129) |
|  | [Integriertes Stahlwerk](#industry_130) |
|  | [Integriertes Stahlwerk](#industry_135) |
|  | [Integriertes Stahlwerk](#industry_136) |
|  | [Integriertes Stahlwerk](#industry_137) |
|  | [Integriertes Stahlwerk](#industry_138) |
|  | [Rußfabrik](#industry_219) |
|  | [Rußfabrik](#industry_220) |
|  | [Säurefabrik](#industry_239) |
|  | [Säurefabrik](#industry_240) |

<a name="cargo_WDPR"></a>
### Schnittholz

Holz in Form von Bäumen kann nicht direkt industriell verwendet werden. Es muss in verschiedene Formen geschnitten werden, so dass es im Bauwesen oder in der Möbelindustrie benutzt werden kann. Im Set bezeichnet Schnittholz alle Arten von vorverarbeitetem Holz in Form von Balken oder Brettern. 

Eintrag in der Frachttabelle: WDPR

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b09c6c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Sägewerk](#industry_235) | [Bauhof](#industry_36) |
| [Sägewerk](#industry_236) | [Bauhof](#industry_37) |
|  | [Möbelfabrik](#industry_185) |
|  | [Möbelfabrik](#industry_186) |
|  | [Möbelfabrik](#industry_187) |
|  | [Möbelfabrik](#industry_188) |

<a name="cargo_SULP"></a>
### Schwefel

Schwefel ist bereits seit dem Altertum bekannt. Schon in der Antike wurde es als Brandwaffe verwendet, aber auch zur Desinfektion und zum Schwefeln von Wein. Schwefel ist Teil von Schwarzpulver und spielte ein große Rolle in der Alchemie. Im frühen 19. Jahrhundert wurde mit dem Fortschreiten der Wissenschaft schließlich erkannt, dass Schwefel ein chemisches Element ist. Schwefel ist - wenig überraschend - in Schwefelsäure enthalten, die zahllose Anwendungen in der Industrie hat. Elementarer Schwefel wird heute hauptsächlich für die Vulkanisierung von Kautschuk im Zusammenhang mit der Reifenproduktion verwendet. 

Eintrag in der Frachttabelle: SULP

Teil der Erweiterung: [Koks und Schwefel](#extension_8)

Frachtklassen: Flüssiggut, Massengut, Nässeempfindlich

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fcd400;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Erzschmelze](#industry_56) | [Reifenfabrik](#industry_207) |
| [Erzschmelze](#industry_57) | [Reifenfabrik](#industry_208) |
| [Erzschmelze](#industry_58) | [Säurefabrik](#industry_237) |
| [Erzschmelze](#industry_59) | [Säurefabrik](#industry_238) |
| [Erzschmelze](#industry_60) | [Säurefabrik](#industry_239) |
| [Erzschmelze](#industry_61) | [Säurefabrik](#industry_240) |
| [Erzschmelze](#industry_62) |  |
| [Erzschmelze](#industry_63) |  |
| [Kokerei](#industry_153) |  |
| [Kraftwerk](#industry_155) |  |
| [Kraftwerk](#industry_157) |  |
| [Ölraffinerie](#industry_268) |  |

<a name="cargo_SASH"></a>
### Soda

Soda bezeichnet umgangssprachlich verschiedene Natriumverbindungen. In diesem Set bezieht sich der Begriff auf sogenanntes Waschsoda, chemisch gesehen Natriumcarbonat. Dieses ist eine essentielle Chemikalie bei der Herstellung von Glas und Seife. Die technische Herstellung von Soda gehört zu den frühesten Entwicklungen der technischen Chemie. Soda ist heute eine der wichtigsten Grundchemikalien, allein in Deutschland wird es in Größenordnungen von Millionen Tonnen jährlich produziert. Es hat zahlreiche Anwendungen in der Herstellung von Glas, aber auch in der Stahlindustrie und als Grundlage zahlreicher Reinigungsmittel. 

Eintrag in der Frachttabelle: SASH

Teil der Erweiterung: [Ammoniak](#extension_1)

Frachtklassen: Massengut, Nässeempfindlich

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#104060;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Sodafabrik](#industry_227) | [Glasfabrik](#industry_97) |
|  | [Glasfabrik](#industry_99) |
|  | [Glasfabrik](#industry_101) |
|  | [Glasfabrik](#industry_103) |
|  | [Reinigungsmittelfabrik](#industry_209) |
|  | [Reinigungsmittelfabrik](#industry_210) |
|  | [Reinigungsmittelfabrik](#industry_211) |
|  | [Reinigungsmittelfabrik](#industry_212) |
|  | [Reinigungsmittelfabrik](#industry_213) |
|  | [Reinigungsmittelfabrik](#industry_214) |
|  | [Reinigungsmittelfabrik](#industry_215) |
|  | [Reinigungsmittelfabrik](#industry_216) |

<a name="cargo_BOOM"></a>
### Sprengstoff

Sprengstoffe sind, neben der militärischen Verwendung, für zahlreiche zivile Anwendungen notwendig. Sowohl im Bauwesen beim Abreißen von Gebäuden als auch beim Tunnelbau und selbstverständlich im Bergbau wird Sprengstoff benötigt. Verschiedenste explosive Stoffe wurden entwickelt, Stichworte sind hier Dynamit, TNT und Nitroglycerin. Für verschiedene Anwendungen existieren unterschiedlichste Sprengstoffe. 

Im Set gibt es hingegen einen Universalsprengstoff für alle Bergwerke. 

Eintrag in der Frachttabelle: BOOM

Teil der Erweiterung: [Produktionsboost](#extension_13)

Frachtklassen: Gefahrgut, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#d43434;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Sprengstofffabrik](#industry_228) | [Eisenerzbergwerk](#industry_55) |
| [Sprengstofffabrik](#industry_229) | [Kalisalzbergwerk](#industry_139) |
| [Sprengstofffabrik](#industry_230) | [Kalksteinbergwerk](#industry_143) |
| [Sprengstofffabrik](#industry_231) | [Kohlebergwerk](#industry_152) |
|  | [Kupfererzbergwerk](#industry_168) |
|  | [Kupfererzbergwerk](#industry_169) |
|  | [Salzbergwerk](#industry_222) |

<a name="cargo_STEL"></a>
### Stahl

Stahl, eine Verbindung aus Eisen und Kohlenstoff, wurde bereits vor über 2000 Jahren in Asien hergestellt. Im 16. und 17. Jahrhundert begann die industrielle Stahlproduktion in Europe, in erster Linie in England. Technische Verbesserungen im 19. Jahrhundert führten schließlich zur billigen Massenproduktion von hochwertigem Stahl. Gleichzeitig stieg der Bedarf exponentiell an, da Stahl für Eisenbahnen gebraucht wurde, Holz als Hauptwerkstoff im Schiffbau ersetzt und natürlich zum Bau von Gebäuden, Brücken und zahllosen anderen Strukturen benötigt wurde. 

Das erste Stahlwerk Deutschlands wurde im frühen 19. Jahrhundert in Essen im Ruhrgebiet gebaut. Aus diesem ging später der Krupp-Konzern hervor. Heute ist Deutschland mit Abstand der größte Stahlproduzent in Europa. 

Eintrag in der Frachttabelle: STEL

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#a8a8a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Integriertes Stahlwerk](#industry_123) | [Fahrzeugfabrik](#industry_64) |
| [Integriertes Stahlwerk](#industry_124) | [Fahrzeugfabrik](#industry_65) |
| [Integriertes Stahlwerk](#industry_125) | [Fahrzeugfabrik](#industry_66) |
| [Integriertes Stahlwerk](#industry_126) | [Fahrzeugfabrik](#industry_67) |
| [Integriertes Stahlwerk](#industry_127) | [Fahrzeugfabrik](#industry_68) |
| [Integriertes Stahlwerk](#industry_128) | [Fahrzeugfabrik](#industry_69) |
| [Integriertes Stahlwerk](#industry_129) | [Fahrzeugfabrik](#industry_70) |
| [Integriertes Stahlwerk](#industry_130) | [Fahrzeugfabrik](#industry_71) |
| [Integriertes Stahlwerk](#industry_131) | [Fahrzeugteilefabrik](#industry_77) |
| [Integriertes Stahlwerk](#industry_132) | [Fahrzeugteilefabrik](#industry_78) |
| [Integriertes Stahlwerk](#industry_133) | [Fahrzeugteilefabrik](#industry_79) |
| [Integriertes Stahlwerk](#industry_134) | [Fahrzeugteilefabrik](#industry_80) |
| [Integriertes Stahlwerk](#industry_135) | [Fahrzeugteilefabrik](#industry_81) |
| [Integriertes Stahlwerk](#industry_136) | [Fahrzeugteilefabrik](#industry_82) |
| [Integriertes Stahlwerk](#industry_137) | [Fahrzeugteilefabrik](#industry_83) |
| [Integriertes Stahlwerk](#industry_138) | [Fahrzeugteilefabrik](#industry_84) |
|  | [Gießerei/Schmiede](#industry_92) |
|  | [Gießerei/Schmiede](#industry_93) |
|  | [Gießerei/Schmiede](#industry_94) |
|  | [Gießerei/Schmiede](#industry_95) |
|  | [Karosseriefabrik](#industry_144) |
|  | [Karosseriefabrik](#industry_145) |
|  | [Karosseriefabrik](#industry_146) |
|  | [Karosseriefabrik](#industry_147) |
|  | [Motorenwerk](#industry_181) |
|  | [Motorenwerk](#industry_182) |
|  | [Motorenwerk](#industry_183) |
|  | [Motorenwerk](#industry_184) |
|  | [Walzwerk](#industry_258) |
|  | [Walzwerk](#industry_259) |
|  | [Walzwerk](#industry_260) |
|  | [Walzwerk](#industry_261) |

<a name="cargo_N2__"></a>
### Stickstoff

Stickstoff ist ein chemisches Element und Hauptbestandteil der Luft. Er ist essentiell für Lebewesen, so benötigen Pflanzen große Mengen an Stickstoff für das Wachstum. Dies führte ab dem 19. Jahrhundert zur Entwicklung von Stickstoffdüngemitteln. Darüber hinaus ist Stickstoff Teil der Salpetersäure und hat zahlreiche Anwendungen bei der Herstellung von Sprengstoffen. Andererseits ist Stickstoff inert - er reagiert nicht mit anderen Chemikalien. Daher dient er als Füllgas in Umgebungen, in denen keine Brände entstehen dürfen, z.B. bei Flugzeugreifen oder in Lampen. 

Eintrag in der Frachttabelle: N2__

Teil der Erweiterung: [Ammoniak](#extension_1)

Frachtklassen: Flüssiggut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#3890e8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Luftzerleger](#industry_176) | [Ammoniakreaktor](#industry_4) |

<a name="cargo_ACID"></a>
### Säure

Säuren sind eine Klasse von chemischen Verbindungen, die sich in erster Linie dadurch auszeichen, dass sie andere chemische Verbindungen angreifen und zerstören können. Das bedeutet auch, dass sie für den Menschen gefährlich und ggfs. tödlich giftig sein können. So wurde Chlor als Giftgas eingesetzt, welches beim Einatmen zu Salzsäure umgesetzt wird, die die Lunge verätzt. Die starke Ätzwirkung ist in der Industrie jedoch in zahllosen Anwendungen notwendig, zum Beispiel bei der Herstellung von Düngemitteln, Farbstoffen und beim Auflösen von Erzen in der Metallproduktion. Die wichtigste Säure für industrielle Anwendungen ist Schwefelsäure, aber im täglichen Gebrauch trifft man zum Beispiel aber auch Kohlensäure (in diversen Getränken und Mineralwasser) an. 

Eintrag in der Frachttabelle: ACID

Teil der Erweiterung: [Koks und Schwefel](#extension_8)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Säurefabrik](#industry_237) | [Ammoniumnitratfabrik](#industry_5) |
| [Säurefabrik](#industry_238) | [Arzneimittelfabrik](#industry_10) |
| [Säurefabrik](#industry_239) | [Arzneimittelfabrik](#industry_11) |
| [Säurefabrik](#industry_240) | [Arzneimittelfabrik](#industry_12) |
|  | [Arzneimittelfabrik](#industry_13) |
|  | [Arzneimittelfabrik](#industry_18) |
|  | [Arzneimittelfabrik](#industry_19) |
|  | [Arzneimittelfabrik](#industry_20) |
|  | [Arzneimittelfabrik](#industry_21) |
|  | [Drahtwalzwerk](#industry_46) |
|  | [Drahtwalzwerk](#industry_47) |
|  | [Drahtwalzwerk](#industry_48) |
|  | [Drahtwalzwerk](#industry_49) |
|  | [Düngemittelfabrik](#industry_52) |
|  | [Düngemittelfabrik](#industry_53) |
|  | [Farbenfabrik](#industry_87) |
|  | [Farbenfabrik](#industry_88) |
|  | [Karosseriefabrik](#industry_144) |
|  | [Karosseriefabrik](#industry_145) |
|  | [Karosseriefabrik](#industry_146) |
|  | [Karosseriefabrik](#industry_147) |
|  | [Karosseriefabrik](#industry_148) |
|  | [Karosseriefabrik](#industry_149) |
|  | [Kupferhütte](#industry_171) |
|  | [Kupferhütte](#industry_173) |
|  | [Reinigungsmittelfabrik](#industry_210) |
|  | [Reinigungsmittelfabrik](#industry_212) |
|  | [Reinigungsmittelfabrik](#industry_214) |
|  | [Reinigungsmittelfabrik](#industry_216) |
|  | [Sprengstofffabrik](#industry_228) |
|  | [Sprengstofffabrik](#industry_229) |
|  | [Sprengstofffabrik](#industry_230) |
|  | [Sprengstofffabrik](#industry_231) |
|  | [Walzwerk](#industry_258) |
|  | [Walzwerk](#industry_259) |
|  | [Walzwerk](#industry_260) |
|  | [Walzwerk](#industry_261) |

<a name="cargo_TEXT"></a>
### Textilien

Textilien sind ein Oberbegriff für alle Arten von faserbasierten Materialien wie Garn, Fäden und Stoffe. Sie werden hauptsächlich zur Produktion von Kleidung verwendet, spielen aber auch bei der Herstellung von Vorhängen, Teppichen und anderen Haushaltsgegenständen eine Rolle. Darüber hinaus gibt es einen großen Bereich industrieller Textilien, wie zum Beispiel für Sicherheitsgurte oder für medizinische Verbände, um nur einige zu nennen. Im Set werden Textilien als Rohstoff für verschiedene andere Industrien eingesetzt. 

Eintrag in der Frachttabelle: TEXT

Teil der Erweiterung: [Textilindustrie](#extension_15)

Frachtklassen: Nässeempfindlich, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#803828;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Textilfabrik](#industry_242) | [Bekleidungsfabrik](#industry_38) |
| [Textilfabrik](#industry_243) | [Bekleidungsfabrik](#industry_39) |
|  | [Fahrzeugteilefabrik](#industry_78) |
|  | [Fahrzeugteilefabrik](#industry_80) |
|  | [Fahrzeugteilefabrik](#industry_82) |
|  | [Fahrzeugteilefabrik](#industry_84) |
|  | [Möbelfabrik](#industry_185) |
|  | [Möbelfabrik](#industry_187) |

<a name="cargo_PETR"></a>
### Treibstoff

Treibstoff ist im Set der Oberbegriff für alles ist, was man zum Betreiben von Kraftfahrzeugen, Flugzeugen und sonstigen Maschinen benötigt. Hergestellt werden Treibstoffe üblicherweise aus Erdöl, wobei alternative Herstellungsmethoden z.B. aus Biomasse im 21. Jahrhundert an Bedeutung gewinnen. Somit hängt die gesamte Wirtschaft und insbesondere der Transportsektor maßgeblich von der Verfügbarkeit von Erdöl ab. 

Eintrag in der Frachttabelle: PETR

Teil der Erweiterung: [Organische Chemie](#extension_11)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#cccca8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bioraffinerie](#industry_40) | [Sprengstofffabrik](#industry_230) |
| [Hydrierwerk](#industry_122) | [Sprengstofffabrik](#industry_231) |
| [Steamcracker](#industry_232) | [Tankstelle](#industry_241) |
| [Ölraffinerie](#industry_267) |  |
| [Ölraffinerie](#industry_268) |  |

<a name="cargo_MNSP"></a>
### Verpackungen

Verpackungen sind ein notwendiges Übel für viele Waren und Lebensmittel. Sie schützen beim Transport, erzeugen aber am Ende auch viel Müll. Im Set sind Verpackungen in erster Linie ein zusätzlicher Baustein für mehr Komplexität in den Transportketten. 

Eintrag in der Frachttabelle: MNSP

Teil der Erweiterung: [Verpackungsmittelindustrie](#extension_16)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#b87818;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Verpackungsmittelfabrik](#industry_244) | [Arzneimittelfabrik](#industry_7) |
| [Verpackungsmittelfabrik](#industry_245) | [Arzneimittelfabrik](#industry_9) |
| [Verpackungsmittelfabrik](#industry_246) | [Arzneimittelfabrik](#industry_11) |
| [Verpackungsmittelfabrik](#industry_247) | [Arzneimittelfabrik](#industry_13) |
| [Verpackungsmittelfabrik](#industry_248) | [Arzneimittelfabrik](#industry_15) |
| [Verpackungsmittelfabrik](#industry_249) | [Arzneimittelfabrik](#industry_17) |
| [Verpackungsmittelfabrik](#industry_250) | [Arzneimittelfabrik](#industry_19) |
| [Verpackungsmittelfabrik](#industry_251) | [Arzneimittelfabrik](#industry_21) |
|  | [Bekleidungsfabrik](#industry_39) |
|  | [Druckerei](#industry_51) |
|  | [Gerätewerk](#industry_91) |
|  | [Molkerei](#industry_179) |
|  | [Molkerei](#industry_180) |
|  | [Möbelfabrik](#industry_187) |
|  | [Möbelfabrik](#industry_188) |
|  | [Mühle](#industry_190) |
|  | [Nahrungsmittelfabrik](#industry_195) |
|  | [Nahrungsmittelfabrik](#industry_196) |
|  | [Nahrungsmittelfabrik](#industry_197) |
|  | [Nahrungsmittelfabrik](#industry_198) |
|  | [Nahrungsmittelfabrik](#industry_201) |
|  | [Nahrungsmittelfabrik](#industry_202) |
|  | [Reinigungsmittelfabrik](#industry_211) |
|  | [Reinigungsmittelfabrik](#industry_212) |
|  | [Reinigungsmittelfabrik](#industry_215) |
|  | [Reinigungsmittelfabrik](#industry_216) |
|  | [Schlachthof](#industry_225) |

<a name="cargo_LVST"></a>
### Vieh

Fleisch war und ist ein wichtiger Teil der menschlichen Nahrung, und dementsprechend ist die Viehhaltung ein wichtiger Teil der Lebensmittelindustrie. Der Transport von Vieh ist auch eine spezielle Herausforderung im Spiel, da man dafür oftmals spezialisierte Fahrzeuge benötigt. 

Eintrag in der Frachttabelle: LVST

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#5c9c34;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bauernhof](#industry_24) | [Nahrungsmittelfabrik](#industry_191) |
| [Bauernhof](#industry_25) | [Nahrungsmittelfabrik](#industry_192) |
| [Bauernhof](#industry_27) | [Nahrungsmittelfabrik](#industry_195) |
| [Bauernhof](#industry_28) | [Nahrungsmittelfabrik](#industry_197) |
| [Bauernhof](#industry_30) | [Nahrungsmittelfabrik](#industry_199) |
| [Bauernhof](#industry_31) | [Nahrungsmittelfabrik](#industry_201) |
| [Bauernhof](#industry_33) | [Schlachthof](#industry_224) |
| [Bauernhof](#industry_34) | [Schlachthof](#industry_225) |
| [Viehzucht](#industry_252) |  |
| [Viehzucht](#industry_253) |  |
| [Viehzucht](#industry_254) |  |
| [Viehzucht](#industry_255) |  |

<a name="cargo_GOOD"></a>
### Waren

Im Spiel stellen Waren eine Abstraktion für praktisch alles dar, was in Fabriken produziert und in Städten verkauft wird. Das können also Möbel, Haushaltsgegenstände, Kleidung oder Spielzeuge sein. 

Eintrag in der Frachttabelle: GOOD

Frachtklassen: Expressgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Arzneimittelfabrik](#industry_6) | [Hafen](#industry_104) |
| [Arzneimittelfabrik](#industry_7) | [Hafen](#industry_105) |
| [Arzneimittelfabrik](#industry_8) | [Hafen](#industry_106) |
| [Arzneimittelfabrik](#industry_9) | [Hafen](#industry_107) |
| [Arzneimittelfabrik](#industry_10) | [Hafen](#industry_108) |
| [Arzneimittelfabrik](#industry_11) | [Hafen](#industry_109) |
| [Arzneimittelfabrik](#industry_12) | [Hafen](#industry_110) |
| [Arzneimittelfabrik](#industry_13) | [Hafen](#industry_111) |
| [Arzneimittelfabrik](#industry_14) | [Hafen](#industry_112) |
| [Arzneimittelfabrik](#industry_15) | [Hafen](#industry_113) |
| [Arzneimittelfabrik](#industry_16) | [Hafen](#industry_114) |
| [Arzneimittelfabrik](#industry_17) | [Hafen](#industry_115) |
| [Arzneimittelfabrik](#industry_18) | [Hafen](#industry_116) |
| [Arzneimittelfabrik](#industry_19) | [Hafen](#industry_117) |
| [Arzneimittelfabrik](#industry_20) | [Hafen](#industry_118) |
| [Arzneimittelfabrik](#industry_21) | [Hafen](#industry_119) |
| [Bekleidungsfabrik](#industry_38) | [Kaufhaus](#industry_150) |
| [Bekleidungsfabrik](#industry_39) |  |
| [Druckerei](#industry_50) |  |
| [Druckerei](#industry_51) |  |
| [Gerätewerk](#industry_90) |  |
| [Gerätewerk](#industry_91) |  |
| [Möbelfabrik](#industry_185) |  |
| [Möbelfabrik](#industry_186) |  |
| [Möbelfabrik](#industry_187) |  |
| [Möbelfabrik](#industry_188) |  |
| [Reinigungsmittelfabrik](#industry_209) |  |
| [Reinigungsmittelfabrik](#industry_210) |  |
| [Reinigungsmittelfabrik](#industry_211) |  |
| [Reinigungsmittelfabrik](#industry_212) |  |
| [Reinigungsmittelfabrik](#industry_213) |  |
| [Reinigungsmittelfabrik](#industry_214) |  |
| [Reinigungsmittelfabrik](#industry_215) |  |
| [Reinigungsmittelfabrik](#industry_216) |  |

<a name="cargo_H2__"></a>
### Wasserstoff

Wasserstoff ist das simpelste und häufigste chemische Element im Universum. Auf der Erde findet man es hauptsächlich in Verbindungen, in erster Linie in Form von Wasser und in Kohlenwasserstoffen wie Öl. Wasserstoff hat zahlreiche Anwendungen in der chemischen Industrie, hauptsächlich bei der Herstellung von Ammoniak. Darüber hinaus wird es als Raketentreibstoff verwendet, aber auch als Kühlmittel. 

Eintrag in der Frachttabelle: H2__

Teil der Erweiterung: [Grundlegende Anorganische Chemie](#extension_7)

Frachtklassen: Flüssiggut, Gefahrgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#ccd0dc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Chloralkali Elektrolyseanlage](#industry_43) | [Ammoniakreaktor](#industry_4) |
| [Dampfreformierer](#industry_44) | [Arzneimittelfabrik](#industry_6) |
| [Dampfreformierer](#industry_45) | [Arzneimittelfabrik](#industry_7) |
|  | [Arzneimittelfabrik](#industry_8) |
|  | [Arzneimittelfabrik](#industry_9) |
|  | [Arzneimittelfabrik](#industry_10) |
|  | [Arzneimittelfabrik](#industry_11) |
|  | [Arzneimittelfabrik](#industry_12) |
|  | [Arzneimittelfabrik](#industry_13) |
|  | [Arzneimittelfabrik](#industry_14) |
|  | [Arzneimittelfabrik](#industry_15) |
|  | [Arzneimittelfabrik](#industry_16) |
|  | [Arzneimittelfabrik](#industry_17) |
|  | [Arzneimittelfabrik](#industry_18) |
|  | [Arzneimittelfabrik](#industry_19) |
|  | [Arzneimittelfabrik](#industry_20) |
|  | [Arzneimittelfabrik](#industry_21) |
|  | [Hydrierwerk](#industry_122) |
|  | [Säurefabrik](#industry_238) |
|  | [Säurefabrik](#industry_240) |

<a name="cargo_RCYC"></a>
### Wertstoffe

Wertstoffe sind nicht einfach nur Abfälle, sondern können als Rohstoffe für die Industrie erneut verwendet werden. Die typischen Beispiele sind Altglas und Altpapier. Das Recycling dieser Wertstoffe spart erhebliche Ressourcen bei der Produktion. 

Eintrag in der Frachttabelle: RCYC

Teil der Erweiterung: [Recycling](#extension_14)

Frachtklassen: Massengut, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#646488;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Wertstoffhof](#industry_262) | [Glasfabrik](#industry_98) |
|  | [Glasfabrik](#industry_99) |
|  | [Glasfabrik](#industry_102) |
|  | [Glasfabrik](#industry_103) |
|  | [Papiermühle](#industry_206) |

<a name="cargo_WOOL"></a>
### Wolle

Wolle ist eine Textilfaser, die hauptsächlich von Schafen gewonnen wird und zu Garn und weiter zu Textilien verarbeitet wird. 

Eintrag in der Frachttabelle: WOOL

Teil der Erweiterung: [Textilindustrie](#extension_15)

Frachtklassen: Nässeempfindlich, Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#a85c4c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Bauernhof](#industry_24) | [Textilfabrik](#industry_242) |
| [Bauernhof](#industry_27) | [Textilfabrik](#industry_243) |
| [Bauernhof](#industry_30) |  |
| [Bauernhof](#industry_33) |  |
| [Viehzucht](#industry_253) |  |
| [Viehzucht](#industry_255) |  |

<a name="cargo_CMNT"></a>
### Zement

Zement ist ein wesentlicher Bestandteil bei der Herstellung von Mörtel und Beton, die zu den wichtigsten und weitverbreitetsten Resourcen der Welt gehören. Ohne sie könnten keine Wolkenkratzer gebaut werden. 

Eintrag in der Frachttabelle: CMNT

Teil der Erweiterung: [Bauindustrie](#extension_3)

Frachtklassen: Massengut, Nässeempfindlich, Pulver

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#6c7484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Zementfabrik](#industry_263) | [Bauhof](#industry_36) |

<a name="cargo_BDMT"></a>
### Ziegel

Ziegel wurden seit dem Altertum für den Bau von Gebäuden genutzt. Im Zuge der Industrialisierung wuchs der Bedarf nach preiswerten Ziegeln sprunghaft, um daraus Fabrikhallen und Brücken zu bauen. Noch heute sind Ziegelsteine relevant, obwohl man sie aus statischen Gründen nicht für den Bau von Wolkenkratzern nutzen kann. 

Eintrag in der Frachttabelle: BDMT

Teil der Erweiterung: [Bauindustrie](#extension_3)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#cc8060;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Ziegelei](#industry_264) | [Bauhof](#industry_36) |

<a name="cargo_ZINC"></a>
### Zink

Zink ist ein unedles Metall, welches industriell eine große Rolle spielt, da es in großen Mengen zum Rostschutz (Verzinkung von Blechen) eingesetzt wird. 

Eintrag in der Frachttabelle: ZINC

Teil der Erweiterung: [Automobilbau](#extension_2)

Frachtklassen: Stückgut

Farbe in der Wirtschaftsketten-Übersicht:<span style="background-color:#285ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Produziert von | Benötigt von |
| -- | -- |
| [Erzschmelze](#industry_60) | [Karosseriefabrik](#industry_144) |
| [Erzschmelze](#industry_61) | [Karosseriefabrik](#industry_145) |
| [Erzschmelze](#industry_62) | [Karosseriefabrik](#industry_146) |
| [Erzschmelze](#industry_63) | [Karosseriefabrik](#industry_147) |
|  | [Karosseriefabrik](#industry_148) |
|  | [Karosseriefabrik](#industry_149) |

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
| [Hafen](#industry_104) | [Kraftwerk](#industry_154) |
| [Hafen](#industry_105) | [Kraftwerk](#industry_155) |
| [Hafen](#industry_106) | [Kraftwerk](#industry_156) |
| [Hafen](#industry_107) | [Kraftwerk](#industry_157) |
| [Hafen](#industry_108) | [Kunststofffabrik](#industry_158) |
| [Hafen](#industry_109) | [Kunststofffabrik](#industry_159) |
| [Hafen](#industry_110) | [Kunststofffabrik](#industry_160) |
| [Hafen](#industry_111) | [Kunststofffabrik](#industry_161) |
| [Hafen](#industry_112) | [Rußfabrik](#industry_217) |
| [Hafen](#industry_113) | [Rußfabrik](#industry_219) |
| [Hafen](#industry_114) | [Synthesekautschukfabrik](#industry_233) |
| [Hafen](#industry_115) | [Ölraffinerie](#industry_267) |
| [Hafen](#industry_116) | [Ölraffinerie](#industry_268) |
| [Hafen](#industry_117) |  |
| [Hafen](#industry_118) |  |
| [Hafen](#industry_119) |  |
| [Ölbohrinsel](#industry_265) |  |
| [Ölquellen](#industry_266) |  |


## Industries

<a name="industry_0"></a>
### Aluhütte

<img src="aluminium_plant.png" alt="Aluhütte">

Die Aluminiumhütte erzeugt Aluminium aus Bauxit, einem Aluminiumerz. Der Prozess besteht aus zwei Schritten, im ersten wird das Bauxit in einem chemischen Prozess aufgespalten um Verunreinigungen zu entfernen bevor es zu Aluminiumoxid umgewandelt wird. Der zweite Schritte besteht aus der Aufspaltung des Aluminiumoxids durch Elektrolyse. Das erfordert sehr viel elektrischen Strom und erzeugt große Mengen an Kohlendioxid. Damit ist die Produktion eigentlich nur in Gebieten sinnvoll, wo billiger Strom verfügbar ist. 

In Deutschland ist nur eine Firma verblieben, die Aluminium herstellt. Sie betreibt drei Anlagen, die Aluminium hauptsächlich aus Metallschrott recyceln. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Bauxit](#cargo_AORE) | [Aluminium](#cargo_ALUM) |


<a name="industry_1"></a>
### Aluhütte

<img src="aluminium_plant.png" alt="Aluhütte">

Die Aluminiumhütte erzeugt Aluminium aus Bauxit, einem Aluminiumerz. Der Prozess besteht aus zwei Schritten, im ersten wird das Bauxit in einem chemischen Prozess aufgespalten um Verunreinigungen zu entfernen bevor es zu Aluminiumoxid umgewandelt wird. Der zweite Schritte besteht aus der Aufspaltung des Aluminiumoxids durch Elektrolyse. Das erfordert sehr viel elektrischen Strom und erzeugt große Mengen an Kohlendioxid. Damit ist die Produktion eigentlich nur in Gebieten sinnvoll, wo billiger Strom verfügbar ist. 

In Deutschland ist nur eine Firma verblieben, die Aluminium herstellt. Sie betreibt drei Anlagen, die Aluminium hauptsächlich aus Metallschrott recyceln. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Grundlegende Anorganische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Bauxit](#cargo_AORE) | [Aluminium](#cargo_ALUM) |
| [Natronlauge](#cargo_LYE_) |  |


<a name="industry_2"></a>
### Aluhütte

<img src="aluminium_plant.png" alt="Aluhütte">

Die Aluminiumhütte erzeugt Aluminium aus Bauxit, einem Aluminiumerz. Der Prozess besteht aus zwei Schritten, im ersten wird das Bauxit in einem chemischen Prozess aufgespalten um Verunreinigungen zu entfernen bevor es zu Aluminiumoxid umgewandelt wird. Der zweite Schritte besteht aus der Aufspaltung des Aluminiumoxids durch Elektrolyse. Das erfordert sehr viel elektrischen Strom und erzeugt große Mengen an Kohlendioxid. Damit ist die Produktion eigentlich nur in Gebieten sinnvoll, wo billiger Strom verfügbar ist. 

In Deutschland ist nur eine Firma verblieben, die Aluminium herstellt. Sie betreibt drei Anlagen, die Aluminium hauptsächlich aus Metallschrott recyceln. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Bauxit](#cargo_AORE) | [Aluminium](#cargo_ALUM) |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_3"></a>
### Aluhütte

<img src="aluminium_plant.png" alt="Aluhütte">

Die Aluminiumhütte erzeugt Aluminium aus Bauxit, einem Aluminiumerz. Der Prozess besteht aus zwei Schritten, im ersten wird das Bauxit in einem chemischen Prozess aufgespalten um Verunreinigungen zu entfernen bevor es zu Aluminiumoxid umgewandelt wird. Der zweite Schritte besteht aus der Aufspaltung des Aluminiumoxids durch Elektrolyse. Das erfordert sehr viel elektrischen Strom und erzeugt große Mengen an Kohlendioxid. Damit ist die Produktion eigentlich nur in Gebieten sinnvoll, wo billiger Strom verfügbar ist. 

In Deutschland ist nur eine Firma verblieben, die Aluminium herstellt. Sie betreibt drei Anlagen, die Aluminium hauptsächlich aus Metallschrott recyceln. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Grundlegende Anorganische Chemie](#extension_7) [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d8d8d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Bauxit](#cargo_AORE) | [Aluminium](#cargo_ALUM) |
| [Natronlauge](#cargo_LYE_) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_4"></a>
### Ammoniakreaktor

<img src="ammonia_plant.png" alt="Ammoniakreaktor">

Die industrielle Herstellung von Ammoniak war erst mit der Entwicklung des Haber-Bosch-Verfahrens im frühen 20. Jahrhundert möglich. Im Zuge des Ersten Weltkrieges und der Bedeutung von Ammoniak für die Herstellung von Sprengstoff wurde dies für Deutschland politisch bedeutsam. Mit staatlicher Unterstützung wurden die ersten Ammoniakreaktoren von BASF an den Standorten Ludwigshafen, Leuna und Bitterfeld gebaut. Nach dem Ende des Krieges wurden entsprechende Fabriken auch im Rest der Welt erbaut. In den Zwischenkriegsjahren war die I.G. Farben der größte Ammoniakproduzent der Welt. Noch heute ist Deutschland einer der größten Ammoniakproduzenten Europas. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#286078;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Wasserstoff](#cargo_H2__) | [Ammoniak](#cargo_NH3_) |
| [Stickstoff](#cargo_N2__) |  |


<a name="industry_5"></a>
### Ammoniumnitratfabrik

<img src="ammonium_nitrate_plant.png" alt="Ammoniumnitratfabrik">

Die Ammoniumnitratfabrik verarbeitet Ammoniak und Säure zu Ammoniumnitrat. 

In Deutschland gibt es heute mehrere große Chemiebetriebe, die neben Ammoniak auch Ammoniumnitrat produzieren, so zum Beispiel die Stickstoffwerke Piesteritz bei Wittenberg. Das BASF-Werk in Ludwigshafen bzw. Oppau wurde 1921 durch eine Explosion schwer beschädigt, bei der Ammoniumnitratverbindungen explodiert waren. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b87818;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Ammoniumnitrat](#cargo_NHNO) |
| [Ammoniak](#cargo_NH3_) |  |


<a name="industry_6"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |
| [Wasserstoff](#cargo_H2__) |  |


<a name="industry_7"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_8"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_9"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_10"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |


<a name="industry_11"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_12"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Ethylen](#cargo_C2H4) |  |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_13"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Ethylen](#cargo_C2H4) |  |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_14"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |
| [Wasserstoff](#cargo_H2__) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |


<a name="industry_15"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Waren](#cargo_GOOD) |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |


<a name="industry_16"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Organische Chemie](#extension_11) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_17"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_18"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |


<a name="industry_19"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |


<a name="industry_20"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Ethylen](#cargo_C2H4) |  |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_21"></a>
### Arzneimittelfabrik

<img src="pharmaceutical_plant.png" alt="Arzneimittelfabrik">

Pharmazeutische Produkte wie Arzneimittel und Impfstoffe sind eine wichtiger Bestandteil der deutschen Wirtschaft. Das geht auf das 19. Jahrhundert zurück, als Durchbrüche in der Chemieforschung die Herstellung neuartiger Medikamente erlaubte. Eins der bekanntesten Beispiele ist die Firma Bayer, die als Hersteller von Färbemitteln begann und später Aspirin entwickelte und heute einer der größten Pharmahersteller der Welt ist. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#e8d0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Ethylen](#cargo_C2H4) |  |
| [Chlor](#cargo_CHLO) |  |
| [Wasserstoff](#cargo_H2__) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_22"></a>
### Autohaus

<img src="vehicle_distributor.png" alt="Autohaus">

Autohändler verkaufen Autos in den Städten. Üblicherweise bieten sie auch Services rund ums Auto an, so zum Beispiel Werkstattarbeiten, Ersatzteile oder Reifenwechsel. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Automobilbau](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#bce0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fahrzeuge](#cargo_VEHI) |  |


<a name="industry_23"></a>
### Autohaus

<img src="vehicle_distributor.png" alt="Autohaus">

Autohändler verkaufen Autos in den Städten. Üblicherweise bieten sie auch Services rund ums Auto an, so zum Beispiel Werkstattarbeiten, Ersatzteile oder Reifenwechsel. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#bce0fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Reifen](#cargo_TYRE) |  |
| [Fahrzeuge](#cargo_VEHI) |  |
| [Fahrzeugteile](#cargo_VPTS) |  |


<a name="industry_24"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_25"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |


<a name="industry_26"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Getreide](#cargo_GRAI) |


<a name="industry_27"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Biomasse](#cargo_BIOM) |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_28"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Lebensmittelindustrie](#extension_9) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Biomasse](#cargo_BIOM) |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |


<a name="industry_29"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Biomasse](#cargo_BIOM) |
|  | [Getreide](#cargo_GRAI) |


<a name="industry_30"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_31"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |


<a name="industry_32"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Getreide](#cargo_GRAI) |


<a name="industry_33"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) [Früchte und Bioenergie](#extension_5) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Biomasse](#cargo_BIOM) |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_34"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Lebensmittelindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Biomasse](#cargo_BIOM) |
|  | [Getreide](#cargo_GRAI) |
|  | [Vieh](#cargo_LVST) |


<a name="industry_35"></a>
### Bauernhof

<img src="farm.png" alt="Bauernhof">

Bauernhöfe sind die wichtigste landwirtschaftliche Industrie im Set, denn sie produzieren Getreide und Vieh. Beides sind relevante Rohstoffe für die Lebensmittelindustrie. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#ec9ca4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Biomasse](#cargo_BIOM) |
|  | [Getreide](#cargo_GRAI) |


<a name="industry_36"></a>
### Bauhof

<img src="builders_yard.png" alt="Bauhof">

Der Bauhof stellt Baumaterialien für die Stadt und ihre Bewohner bereit. Damit ist es eigentlich eher ein Baumarkt, in dem die Einwohner der Städte Baumaterial und Werkzeuge kaufen können. Bauhöfe hingegen sind zumindest in Deutschland kommunale Einrichtungen, in denen z.B. Streusand und andere notwendige Materialien gelagert werden. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_3) 


Farbe in der Übersichtskarte:<span style="background-color:#acacc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ziegel](#cargo_BDMT) |  |
| [Zement](#cargo_CMNT) |  |
| [Sand](#cargo_SAND) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_37"></a>
### Bauhof

<img src="builders_yard.png" alt="Bauhof">

Der Bauhof stellt Baumaterialien für die Stadt und ihre Bewohner bereit. Damit ist es eigentlich eher ein Baumarkt, in dem die Einwohner der Städte Baumaterial und Werkzeuge kaufen können. Bauhöfe hingegen sind zumindest in Deutschland kommunale Einrichtungen, in denen z.B. Streusand und andere notwendige Materialien gelagert werden. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Bauindustrie](#extension_3) 


Farbe in der Übersichtskarte:<span style="background-color:#acacc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_38"></a>
### Bekleidungsfabrik

<img src="clothing_plant.png" alt="Bekleidungsfabrik">

Die Bekleidungsfabrik ist der Ort, an dem aus Stoffen Kleidungsstücke gefertigt werden. Europa hat eine reichhaltige Geschichte der Bekleidungsindustrie, die allerdings quasi komplett durch billigere asiatische Konkurrenz ersetzt wurde. Spezialgeschäfte für hochwertige Bekleidung haben noch ihre eigene Nische. Deutschland hatte im 19. Jahrhundert eine bedeutende Bekleidungsindustrie, hauptsächlich in Schlesien und Sachsen. Heute existieren zwar noch viele Firmen, teilweise auch international sehr bekannte wie Boss, Triumph oder adidas, aber die Produktion wurde üblicherweise nach Asien verlagert. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#803828;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Textilien](#cargo_TEXT) | [Waren](#cargo_GOOD) |


<a name="industry_39"></a>
### Bekleidungsfabrik

<img src="clothing_plant.png" alt="Bekleidungsfabrik">

Die Bekleidungsfabrik ist der Ort, an dem aus Stoffen Kleidungsstücke gefertigt werden. Europa hat eine reichhaltige Geschichte der Bekleidungsindustrie, die allerdings quasi komplett durch billigere asiatische Konkurrenz ersetzt wurde. Spezialgeschäfte für hochwertige Bekleidung haben noch ihre eigene Nische. Deutschland hatte im 19. Jahrhundert eine bedeutende Bekleidungsindustrie, hauptsächlich in Schlesien und Sachsen. Heute existieren zwar noch viele Firmen, teilweise auch international sehr bekannte wie Boss, Triumph oder adidas, aber die Produktion wurde üblicherweise nach Asien verlagert. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#803828;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Textilien](#cargo_TEXT) |  |


<a name="industry_40"></a>
### Bioraffinerie

<img src="biorefinery.png" alt="Bioraffinerie">

Aus verfaulenden Früchten und Biomasse kann man grundlegende Chemikalien gewinnen. Die so gewonnenen Chemikalien sind erheblich besser für die Umwelt, verglichen mit der herkömmlichen Gewinnung aus Erdöl. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#80a82c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Biomasse](#cargo_BIOM) | [Ethylen](#cargo_C2H4) |
| [Früchte](#cargo_FRUT) | [Treibstoff](#cargo_PETR) |


<a name="industry_41"></a>
### Brauerei

<img src="brewery.png" alt="Brauerei">

Die Erzeugung von Bier ist seit Jahrtausenden belegt. Bier wird oft als flüssiges Brot bezeichnet und ist nach wie vor ein üblicher Teil der Ernährung. Im Mittelalter wurde Bier in erster Linie in Klöstern gebraut. Mit der industriellen Revolution und der Einführung neuer Materialien wie rostfreiem Stahl vergrößerte sich die Anzahl der Brauereien und die Menge des gebrauten Biers dramatisch. Die wichtigste Erfindung in diesem Zusammenhang war die Kältemaschine, die es im 19. Jahrhundert schließlich erlaubte, auch bei sommerlichen Temperaturen Bier zu brauen. Davor wurde Bier im Winter gebraut und anschließend in Kellern gelagert, um es vor der Sommerhitze zu schützen. 

Deutschland hat eine lange Tradition in der Bierbrauerei, und Bier ist ein bekannter Teil der Kultur. Die Deutschen gehören zu den größten Biertrinkern in Europa, entsprechend viel wird produziert. Das bekannte Reinheitsgebot legt fest, dass nur Hopfen, Malz, Wasser und bestimmte Getreidesorten verwendet werden dürfen. Trotzdem gibt es zahllose Brauereien, vor allem in Franken, welches die höchste Dichte an Brauereien weltweit aufweist. Über 5000 Sorten Bier werden von etwa 1500 Brauereien erzeugt, von denen wiederum die Hälfte in Bayern angesiedelt ist. Bierkonsum gehört zu den wichtigsten Tätigkeiten bei zahlreichen Volksfesten wie dem Oktoberfest in München oder der Bergkirchweih in Erlangen. 

Im Set ist Bier trotzdem keine eigene Fracht, sondern zählt einfach als Nahrungsmitel. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_42"></a>
### Brauerei

<img src="brewery.png" alt="Brauerei">

Die Erzeugung von Bier ist seit Jahrtausenden belegt. Bier wird oft als flüssiges Brot bezeichnet und ist nach wie vor ein üblicher Teil der Ernährung. Im Mittelalter wurde Bier in erster Linie in Klöstern gebraut. Mit der industriellen Revolution und der Einführung neuer Materialien wie rostfreiem Stahl vergrößerte sich die Anzahl der Brauereien und die Menge des gebrauten Biers dramatisch. Die wichtigste Erfindung in diesem Zusammenhang war die Kältemaschine, die es im 19. Jahrhundert schließlich erlaubte, auch bei sommerlichen Temperaturen Bier zu brauen. Davor wurde Bier im Winter gebraut und anschließend in Kellern gelagert, um es vor der Sommerhitze zu schützen. 

Deutschland hat eine lange Tradition in der Bierbrauerei, und Bier ist ein bekannter Teil der Kultur. Die Deutschen gehören zu den größten Biertrinkern in Europa, entsprechend viel wird produziert. Das bekannte Reinheitsgebot legt fest, dass nur Hopfen, Malz, Wasser und bestimmte Getreidesorten verwendet werden dürfen. Trotzdem gibt es zahllose Brauereien, vor allem in Franken, welches die höchste Dichte an Brauereien weltweit aufweist. Über 5000 Sorten Bier werden von etwa 1500 Brauereien erzeugt, von denen wiederum die Hälfte in Bayern angesiedelt ist. Bierkonsum gehört zu den wichtigsten Tätigkeiten bei zahlreichen Volksfesten wie dem Oktoberfest in München oder der Bergkirchweih in Erlangen. 

Im Set ist Bier trotzdem keine eigene Fracht, sondern zählt einfach als Nahrungsmitel. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Glas](#extension_6) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |


<a name="industry_43"></a>
### Chloralkali Elektrolyseanlage

<img src="chloralkali_plant.png" alt="Chloralkali Elektrolyseanlage">

Die Chlor-Alkali-Anlage benutzt Elektrolyse, um Salz in Chlor und Natronlauge aufzuspalten. Als Nebenprodukt entsteht dabei Wasserstoff. Der Prozess wurde im späten 19. Jahrhundert entwickelt und ist einer der wichtigsten grundlegenden technischen Prozesse der Chemieindustrie, da die beiden Hauptprodukte quasi überall benötigt werden. Die Reaktion benötigt große Mengen elektrischer Energie. Die ersten Anlagen dieser Art wurden um 1890 herum in Deutschland, Spanien, Frankreich und Russland gebaut. Heute sind über 20 Analgen in Deutschland in Betrieb, hauptsächlich in den klassischen Zentren der chemischen Industrie wie Ludwigshafen (BASF) und Schkopau (Dow Chemical), wobei sich die größte Anlage im norddeutschen Stade befindet. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b8dcc8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Salz](#cargo_SALT) | [Chlor](#cargo_CHLO) |
|  | [Wasserstoff](#cargo_H2__) |
|  | [Natronlauge](#cargo_LYE_) |


<a name="industry_44"></a>
### Dampfreformierer

<img src="steamreformer.png" alt="Dampfreformierer">

Die Dampfreformierung geht auf eine Idee von Carl Bosch zurück, der eine preiswerte Möglichkeit suchte, Wasserstoff zu produzieren. Dazu werden Kohlenwasserstoffe, heutzutage in erster Linie Erdgas, durch Zuführen von Wärmeenergie und Wasser in Kohlendioxid und Wasserstoff zerlegt. Heutzutage stammen fast 50% des industriell benötigten Wasserstoffes aus dieser Reaktion. Etwa 60% des Wasserstoffs werden danach für die Synthese von Ammoniak verwendet. 

Da im Set Erdgas keine Rolle spielt, wird stattdessen Rohbenzin, sogenanntes Naphtha, als Ausgansstoff verwendet. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#403c0c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Naphtha](#cargo_RFPR) | [Wasserstoff](#cargo_H2__) |


<a name="industry_45"></a>
### Dampfreformierer

<img src="steamreformer.png" alt="Dampfreformierer">

Die Dampfreformierung geht auf eine Idee von Carl Bosch zurück, der eine preiswerte Möglichkeit suchte, Wasserstoff zu produzieren. Dazu werden Kohlenwasserstoffe, heutzutage in erster Linie Erdgas, durch Zuführen von Wärmeenergie und Wasser in Kohlendioxid und Wasserstoff zerlegt. Heutzutage stammen fast 50% des industriell benötigten Wasserstoffes aus dieser Reaktion. Etwa 60% des Wasserstoffs werden danach für die Synthese von Ammoniak verwendet. 

Da im Set Erdgas keine Rolle spielt, wird stattdessen Rohbenzin, sogenanntes Naphtha, als Ausgansstoff verwendet. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_11) [Früchte und Bioenergie](#extension_5) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#403c0c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Biomasse](#cargo_BIOM) | [Wasserstoff](#cargo_H2__) |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_46"></a>
### Drahtwalzwerk

<img src="wire_mill.png" alt="Drahtwalzwerk">

Die Herstellung von Drähten, Kabeln und ähnlichem war schon vor der Entwicklung elektrischer Geräte eine wichtige Anwendung. Der Begriff des Drahtziehers geht auf diesen Berufszweig zurück. Im Set fertigt das Drahtwalzwerk Materialien für elektrische Geräte und für die Autoindustrie. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Draht/Kabel](#cargo_STWR) |
| [Kupfer](#cargo_COPR) |  |
| [Natronlauge](#cargo_LYE_) |  |


<a name="industry_47"></a>
### Drahtwalzwerk

<img src="wire_mill.png" alt="Drahtwalzwerk">

Die Herstellung von Drähten, Kabeln und ähnlichem war schon vor der Entwicklung elektrischer Geräte eine wichtige Anwendung. Der Begriff des Drahtziehers geht auf diesen Berufszweig zurück. Im Set fertigt das Drahtwalzwerk Materialien für elektrische Geräte und für die Autoindustrie. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Draht/Kabel](#cargo_STWR) |
| [Aluminium](#cargo_ALUM) |  |
| [Kupfer](#cargo_COPR) |  |
| [Natronlauge](#cargo_LYE_) |  |


<a name="industry_48"></a>
### Drahtwalzwerk

<img src="wire_mill.png" alt="Drahtwalzwerk">

Die Herstellung von Drähten, Kabeln und ähnlichem war schon vor der Entwicklung elektrischer Geräte eine wichtige Anwendung. Der Begriff des Drahtziehers geht auf diesen Berufszweig zurück. Im Set fertigt das Drahtwalzwerk Materialien für elektrische Geräte und für die Autoindustrie. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Metallschrott](#cargo_SCMT) |
| [Kupfer](#cargo_COPR) | [Draht/Kabel](#cargo_STWR) |
| [Natronlauge](#cargo_LYE_) |  |


<a name="industry_49"></a>
### Drahtwalzwerk

<img src="wire_mill.png" alt="Drahtwalzwerk">

Die Herstellung von Drähten, Kabeln und ähnlichem war schon vor der Entwicklung elektrischer Geräte eine wichtige Anwendung. Der Begriff des Drahtziehers geht auf diesen Berufszweig zurück. Im Set fertigt das Drahtwalzwerk Materialien für elektrische Geräte und für die Autoindustrie. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Aluminium](#extension_0) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Metallschrott](#cargo_SCMT) |
| [Aluminium](#cargo_ALUM) | [Draht/Kabel](#cargo_STWR) |
| [Kupfer](#cargo_COPR) |  |
| [Natronlauge](#cargo_LYE_) |  |


<a name="industry_50"></a>
### Druckerei

<img src="paper_mill.png" alt="Druckerei">

Der moderne Buchdruck wurde im 16. Jahrhundert in Deutschland erfunden. Im Zuge der Industrialisierung wurden später zahllose Zeitungen gedruckt, das Lesen von Büchern wurde zum Zeitvertreib der gebildeten Bürgerschicht. Heutzutage kann quasi jeder sein eigenes Buch drucken lassen. 

Diese Industrie benötigt Extension: [Papier](#extension_12) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Papier](#cargo_PAPR) | [Waren](#cargo_GOOD) |


<a name="industry_51"></a>
### Druckerei

<img src="paper_mill.png" alt="Druckerei">

Der moderne Buchdruck wurde im 16. Jahrhundert in Deutschland erfunden. Im Zuge der Industrialisierung wurden später zahllose Zeitungen gedruckt, das Lesen von Büchern wurde zum Zeitvertreib der gebildeten Bürgerschicht. Heutzutage kann quasi jeder sein eigenes Buch drucken lassen. 

Diese Industrie benötigt Extension: [Papier](#extension_12) [Verpackungsmittelindustrie](#extension_16) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Papier](#cargo_PAPR) |  |


<a name="industry_52"></a>
### Düngemittelfabrik

<img src="fertilizer_plant.png" alt="Düngemittelfabrik">

Die Düngemittelfabrik verarbeitet verschiedenste Chemikalien zu Düngemitteln. In erster Linie sind dafür Stickstoffverbindungen notwendig, aber auch Kaliumverbindungen und Kalk spielen eine große Rolle. 

Die Anfänge der großtechnischen Düngemittelindustrie liegen im ersten Weltkrieg, als man die technische Ammoniaksynthese entwickelte. Nach Kriegsende wurden in vielen Staaten Düngemittelfabriken gebaut, wodurch die Landwirtschaft überhaupt erst die rasant wachsende Weltbevölkerung ernähren konnte. Die Produktion von Düngemitteln ist in Deutschland heutzutage auf einige wenige spezialisierte Firmen konzentriert. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc907c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Düngemittel](#cargo_FERT) |
| [Ammoniak](#cargo_NH3_) |  |
| [Ammoniumnitrat](#cargo_NHNO) |  |
| [Kalisalz](#cargo_POTA) |  |


<a name="industry_53"></a>
### Düngemittelfabrik

<img src="fertilizer_plant.png" alt="Düngemittelfabrik">

Die Düngemittelfabrik verarbeitet verschiedenste Chemikalien zu Düngemitteln. In erster Linie sind dafür Stickstoffverbindungen notwendig, aber auch Kaliumverbindungen und Kalk spielen eine große Rolle. 

Die Anfänge der großtechnischen Düngemittelindustrie liegen im ersten Weltkrieg, als man die technische Ammoniaksynthese entwickelte. Nach Kriegsende wurden in vielen Staaten Düngemittelfabriken gebaut, wodurch die Landwirtschaft überhaupt erst die rasant wachsende Weltbevölkerung ernähren konnte. Die Produktion von Düngemitteln ist in Deutschland heutzutage auf einige wenige spezialisierte Firmen konzentriert. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) [Glas](#extension_6) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc907c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Düngemittel](#cargo_FERT) |
| [Ammoniak](#cargo_NH3_) |  |
| [Ammoniumnitrat](#cargo_NHNO) |  |
| [Kalisalz](#cargo_POTA) |  |
| [Branntkalk](#cargo_QLME) |  |


<a name="industry_54"></a>
### Eisenerzbergwerk

<img src="iron_ore_mine.png" alt="Eisenerzbergwerk">

Eisenerz wurde bereits im Altertum abgebaut und verhüttet. Im Zusammenhang mit der Entwicklung von preiswerten Prozessen zur Stahlherstellung und dem wachsenden Bedarf, zum Beispiel für die Eisenbahn, wurde die Stahlindustrie im 19. Jahrhundert einer der wichtigsten Wirtschaftszweige. 

In Deutschland wurde bis in die Mitte des 20. Jahrhunderts Eisenerz gefördert, aber insgesamt war Deutschland schon immer auf Erzimporte angewiesen. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#74581c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Eisenerz](#cargo_IORE) |


<a name="industry_55"></a>
### Eisenerzbergwerk

<img src="iron_ore_mine.png" alt="Eisenerzbergwerk">

Eisenerz wurde bereits im Altertum abgebaut und verhüttet. Im Zusammenhang mit der Entwicklung von preiswerten Prozessen zur Stahlherstellung und dem wachsenden Bedarf, zum Beispiel für die Eisenbahn, wurde die Stahlindustrie im 19. Jahrhundert einer der wichtigsten Wirtschaftszweige. 

In Deutschland wurde bis in die Mitte des 20. Jahrhunderts Eisenerz gefördert, aber insgesamt war Deutschland schon immer auf Erzimporte angewiesen. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#74581c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Sprengstoff](#cargo_BOOM) | [Eisenerz](#cargo_IORE) |


<a name="industry_56"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Ammoniak](#extension_1) [Automobilbau](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Eisenerz](#cargo_IORE) |
| [Kupferkies](#cargo_PORE) | [Schwefel](#cargo_SULP) |


<a name="industry_57"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) [Automobilbau](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Kupfererz](#cargo_CORE) |
| [Kupferkies](#cargo_PORE) | [Eisenerz](#cargo_IORE) |
|  | [Schwefel](#cargo_SULP) |


<a name="industry_58"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Automobilbau](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Eisenerz](#cargo_IORE) |
| [Sauerstoff](#cargo_O2__) | [Schwefel](#cargo_SULP) |
| [Kupferkies](#cargo_PORE) |  |


<a name="industry_59"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Farbindustrie](#extension_4) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Automobilbau](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Kupfererz](#cargo_CORE) |
| [Sauerstoff](#cargo_O2__) | [Eisenerz](#cargo_IORE) |
| [Kupferkies](#cargo_PORE) | [Schwefel](#cargo_SULP) |


<a name="industry_60"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Eisenerz](#cargo_IORE) |
| [Kupferkies](#cargo_PORE) | [Schwefel](#cargo_SULP) |
|  | [Zink](#cargo_ZINC) |


<a name="industry_61"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Farbindustrie](#extension_4) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Kupfererz](#cargo_CORE) |
| [Kupferkies](#cargo_PORE) | [Eisenerz](#cargo_IORE) |
|  | [Schwefel](#cargo_SULP) |
|  | [Zink](#cargo_ZINC) |


<a name="industry_62"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Eisenerz](#cargo_IORE) |
| [Sauerstoff](#cargo_O2__) | [Schwefel](#cargo_SULP) |
| [Kupferkies](#cargo_PORE) | [Zink](#cargo_ZINC) |


<a name="industry_63"></a>
### Erzschmelze

<img src="ore_smelter.png" alt="Erzschmelze">

Kupfermineralien enthalten Beimengungen anderer Stoffe wie Schwefel und Eisen, die abgetrennt werden müssen, um reines Kupfer zu erzeugen. Dies geschieht durch Schmelzen und Rösten des Erzes. Dabei wird das Mineral in seine Bestandteile aufgetrennt, übrig bleiben Eisen-Schwefel-Verbindungen und Rohkupfer, welches in einem weiteren Schritt durch Elektrolyse zu reinem Kupfer weiterverarbeitet wird. In der echten Kupferherstellung sind beide Schritte in einer Anlage zusammengefasst, um möglichst energiesparend arbeiten zu können. Im Spiel sind die Schritte in einzelne Industrien aufgeteilt, um die verschiedenen Transportaufgaben darstellen zu können. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Farbindustrie](#extension_4) [Ammoniak](#extension_1) [Automobilbau](#extension_2) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Kupfererz](#cargo_CORE) |
| [Sauerstoff](#cargo_O2__) | [Eisenerz](#cargo_IORE) |
| [Kupferkies](#cargo_PORE) | [Schwefel](#cargo_SULP) |
|  | [Zink](#cargo_ZINC) |


<a name="industry_64"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Glas](#extension_6) [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Fahrzeuge](#cargo_VEHI) |
| [Stahl](#cargo_STEL) |  |


<a name="industry_65"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Glas](#extension_6) [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Fahrzeuge](#cargo_VEHI) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_66"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Glas](#extension_6) [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Fahrzeuge](#cargo_VEHI) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_67"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

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


<a name="industry_68"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Fahrzeuge](#cargo_VEHI) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_69"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

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


<a name="industry_70"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

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


<a name="industry_71"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Metallurgie](#extension_10) [Automobilbau](#extension_2) 

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


<a name="industry_72"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Glas](#extension_6) [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Maschinenteile](#cargo_ENSP) | [Fahrzeuge](#cargo_VEHI) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Bleche](#cargo_STSH) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_73"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Fahrzeuge](#cargo_VEHI) |
| [Maschinenteile](#cargo_ENSP) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Bleche](#cargo_STSH) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_74"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Maschinenteile](#cargo_ENSP) | [Fahrzeuge](#cargo_VEHI) |
| [Glas](#cargo_GLAS) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Bleche](#cargo_STSH) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_75"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Glas](#extension_6) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Fahrzeuge](#cargo_VEHI) |
| [Maschinenteile](#cargo_ENSP) |  |
| [Glas](#cargo_GLAS) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Bleche](#cargo_STSH) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_76"></a>
### Fahrzeugfabrik

<img src="vehicle_factory.png" alt="Fahrzeugfabrik">

Deutschland ist weltbekannt für seine Automobilindustrie. Zahlreiche bahnbrechende Erfindungen auf dem Weg zur Erfindung des Automobils wurden in der zweiten Hälfte des 19. Jahrhunderts in Deutschland gemacht. Die Massenmotorisierung begann allerdings erst nach dem Zweiten Weltkrieg, hauptsächlich in Form des VW Käfer, einem der meistproduzierten Autos aller Zeiten. Heutzutage sind Fahrzeuge nach wie vor ein Exportschlager der deutschen Industrie. Mit Marken wie Mercedes-Benz, Audi, BMW oder Porsche ist die Autoindustrie weltbekannt und einer der wichtigsten Wirtschaftszweige überhaupt. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#002484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Reifen](#cargo_TYRE) | [Fahrzeuge](#cargo_VEHI) |
| [Karosserien](#cargo_VBOD) |  |
| [Motoren](#cargo_VENG) |  |
| [Fahrzeugteile](#cargo_VPTS) |  |


<a name="industry_77"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Glas](#extension_6) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Stahl](#cargo_STEL) |  |


<a name="industry_78"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Textilindustrie](#extension_15) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Stahl](#cargo_STEL) |  |
| [Textilien](#cargo_TEXT) |  |


<a name="industry_79"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_80"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Textilindustrie](#extension_15) [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |
| [Textilien](#cargo_TEXT) |  |


<a name="industry_81"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Glas](#extension_6) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Stahl](#cargo_STEL) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_82"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Textilindustrie](#extension_15) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Stahl](#cargo_STEL) |  |
| [Draht/Kabel](#cargo_STWR) |  |
| [Textilien](#cargo_TEXT) |  |


<a name="industry_83"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Glas](#extension_6) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_84"></a>
### Fahrzeugteilefabrik

<img src="vehicle_parts_plant.png" alt="Fahrzeugteilefabrik">

Die Autozulieferindustrie liefert alle Arten von Bauteilen, seien es Sitze, Lenkräder, Getriebe oder Elektronik. Die Fahrzeugteilefabrik steht stellvertretend für alle Arten von Automobilzulieferern, die gerade in Deutschland wirtschaftlich relevant sind. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Textilindustrie](#extension_15) [Glas](#extension_6) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#84bcd8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Fahrzeugteile](#cargo_VPTS) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Stahl](#cargo_STEL) |  |
| [Draht/Kabel](#cargo_STWR) |  |
| [Textilien](#cargo_TEXT) |  |


<a name="industry_85"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Bauindustrie](#extension_3) [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Ruß](#cargo_CBLK) | [Farbe](#cargo_COAT) |
| [Kupfer](#cargo_COPR) |  |
| [Eisenerz](#cargo_IORE) |  |


<a name="industry_86"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Bauindustrie](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

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


<a name="industry_87"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Bauindustrie](#extension_3) 

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


<a name="industry_88"></a>
### Farbenfabrik

<img src="paint_factory.png" alt="Farbenfabrik">

Die Herstellung von Farben, Pigmenten, Färbemitteln und ähnlichen Produkten waren schon immer ein wichtiger Teil der deutschen Chemieindustrie. Einige der bekanntesten deutschen Chemiefirmen (z.B. Agfa, BASF, Bayer, Hoechst) begannen als Produzenten von Farben oder haben zumindest ein großes Sortiment an entsprechenden Produkten im Angebot. Diese Firmen gehör(t)en auch zu den größten Chemiefirmen der Welt und sind entsprechend relevant für die deutsche Wirtschaft. Dementsprechend musste eine Farbenfabrik im Set enthalten sein. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Bauindustrie](#extension_3) [Koks und Schwefel](#extension_8) 

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


<a name="industry_89"></a>
### Fischgründe

<img src="fishing_grounds.png" alt="Fischgründe">

Fisch muss auf dem Meer gefangen werden, was im Spiel eine interessante Herausforderung für den Transport darstellt, da man den Fisch von Schiffen aus in Häfen umladen muss. Obwohl Deutschland Zugang zur Nord- und Ostsee hat, wird ein Großteil des Fisches importiert. Deutschland ist sogar einer der größten Importeure für Fisch in Europa. 


Farbe in der Übersichtskarte:<span style="background-color:#9cccdc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Fisch](#cargo_FISH) |


<a name="industry_90"></a>
### Gerätewerk

<img src="appliance_factory.png" alt="Gerätewerk">

Elektrische Haushaltsgeräte wie Waschmaschinen, Kühlschränke oder Fernsehgeräte sind seit dem mittleren 20. Jahrhundert aus keinem Haushalt mehr wegzudenken. Hergestellt werden sie im Gerätewerk. Zur Herstellung werden dementsprechend verschiedene Materialien benötigt, die ihrerseits erst gefertigt werden müssen. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#744428;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Maschinenteile](#cargo_ENSP) | [Waren](#cargo_GOOD) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_91"></a>
### Gerätewerk

<img src="appliance_factory.png" alt="Gerätewerk">

Elektrische Haushaltsgeräte wie Waschmaschinen, Kühlschränke oder Fernsehgeräte sind seit dem mittleren 20. Jahrhundert aus keinem Haushalt mehr wegzudenken. Hergestellt werden sie im Gerätewerk. Zur Herstellung werden dementsprechend verschiedene Materialien benötigt, die ihrerseits erst gefertigt werden müssen. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Verpackungsmittelindustrie](#extension_16) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#744428;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Maschinenteile](#cargo_ENSP) | [Waren](#cargo_GOOD) |
| [Verpackungen](#cargo_MNSP) |  |
| [Kunststoffe](#cargo_PLAS) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_92"></a>
### Gießerei/Schmiede

<img src="foundry_forge.png" alt="Gießerei/Schmiede">

Gießen und Schmieden sind zwei Techniken, um Metall in teilweise komplexe Formen für technische Anwendungen zu bringen. Während Schmieden seit Hunderten Jahren insbesondere im Bereich der Waffenkunst bekannt ist, ist Metallguss vergleichsweise neu. Heutzutage werden zum Beispiel Motorblöcke gegossen. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#701020;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Maschinenteile](#cargo_ENSP) |
| [Stahl](#cargo_STEL) |  |


<a name="industry_93"></a>
### Gießerei/Schmiede

<img src="foundry_forge.png" alt="Gießerei/Schmiede">

Gießen und Schmieden sind zwei Techniken, um Metall in teilweise komplexe Formen für technische Anwendungen zu bringen. Während Schmieden seit Hunderten Jahren insbesondere im Bereich der Waffenkunst bekannt ist, ist Metallguss vergleichsweise neu. Heutzutage werden zum Beispiel Motorblöcke gegossen. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#701020;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Maschinenteile](#cargo_ENSP) |
| [Koks](#cargo_COKE) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_94"></a>
### Gießerei/Schmiede

<img src="foundry_forge.png" alt="Gießerei/Schmiede">

Gießen und Schmieden sind zwei Techniken, um Metall in teilweise komplexe Formen für technische Anwendungen zu bringen. Während Schmieden seit Hunderten Jahren insbesondere im Bereich der Waffenkunst bekannt ist, ist Metallguss vergleichsweise neu. Heutzutage werden zum Beispiel Motorblöcke gegossen. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#701020;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Maschinenteile](#cargo_ENSP) |
| [Stahl](#cargo_STEL) | [Metallschrott](#cargo_SCMT) |


<a name="industry_95"></a>
### Gießerei/Schmiede

<img src="foundry_forge.png" alt="Gießerei/Schmiede">

Gießen und Schmieden sind zwei Techniken, um Metall in teilweise komplexe Formen für technische Anwendungen zu bringen. Während Schmieden seit Hunderten Jahren insbesondere im Bereich der Waffenkunst bekannt ist, ist Metallguss vergleichsweise neu. Heutzutage werden zum Beispiel Motorblöcke gegossen. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Aluminium](#extension_0) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#701020;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Maschinenteile](#cargo_ENSP) |
| [Koks](#cargo_COKE) | [Metallschrott](#cargo_SCMT) |
| [Stahl](#cargo_STEL) |  |


<a name="industry_96"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) [Recycling](#extension_14) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Branntkalk](#cargo_QLME) | [Glas](#cargo_GLAS) |
| [Sand](#cargo_SAND) |  |


<a name="industry_97"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Branntkalk](#cargo_QLME) | [Glas](#cargo_GLAS) |
| [Sand](#cargo_SAND) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_98"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Branntkalk](#cargo_QLME) | [Glas](#cargo_GLAS) |
| [Wertstoffe](#cargo_RCYC) |  |
| [Sand](#cargo_SAND) |  |


<a name="industry_99"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Ammoniak](#extension_1) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Branntkalk](#cargo_QLME) | [Glas](#cargo_GLAS) |
| [Wertstoffe](#cargo_RCYC) |  |
| [Sand](#cargo_SAND) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_100"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) [Recycling](#extension_14) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalisalz](#cargo_POTA) | [Glas](#cargo_GLAS) |
| [Branntkalk](#cargo_QLME) |  |
| [Sand](#cargo_SAND) |  |


<a name="industry_101"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Ammoniak](#extension_1) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalisalz](#cargo_POTA) | [Glas](#cargo_GLAS) |
| [Branntkalk](#cargo_QLME) |  |
| [Sand](#cargo_SAND) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_102"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Recycling](#extension_14) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalisalz](#cargo_POTA) | [Glas](#cargo_GLAS) |
| [Branntkalk](#cargo_QLME) |  |
| [Wertstoffe](#cargo_RCYC) |  |
| [Sand](#cargo_SAND) |  |


<a name="industry_103"></a>
### Glasfabrik

<img src="glass_works.png" alt="Glasfabrik">

Glas wird durch das Erzeugen einer flüssigen Mischung verschiedener Materialien, das Formen und das kontrollierte Abkühlen erzeugt. Je nach Form des Produktes wie zum Beispiel Flachglas für Fenster oder in Form von Behältern wie Flaschen ist die Produktion hochgradig automatisiert. Einige Spezialformen werden noch heute von Hand durch Glasbläserei erzeugt. Die Eigenschaften des Glases hängen maßgeblich von der Mischung der verwendeten Rohmaterialien ab. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Ammoniak](#extension_1) [Recycling](#extension_14) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#5840ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalisalz](#cargo_POTA) | [Glas](#cargo_GLAS) |
| [Branntkalk](#cargo_QLME) |  |
| [Wertstoffe](#cargo_RCYC) |  |
| [Sand](#cargo_SAND) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_104"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_105"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_106"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Kupfererz](#cargo_CORE) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_107"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Kupfererz](#cargo_CORE) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |


<a name="industry_108"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_109"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_110"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_111"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_112"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_113"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_114"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Koks und Schwefel](#extension_8) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Kupfererz](#cargo_CORE) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_115"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Kupfererz](#cargo_CORE) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_116"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Farbindustrie](#extension_4) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_117"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_118"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Kohle](#cargo_COAL) |
| [Fahrzeuge](#cargo_VEHI) | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_119"></a>
### Hafen

<img src="port.png" alt="Hafen">

Häfen sind Handelszentren, und da die deutsche Wirtschaft schon immer Rohstoffe importiert und zahlreiche Güter exportiert, sind Häfen natürlich auch in diesem Set vertreten. Die deutschen Häfen an Nord- und Ostsee spielten schon im Mittelalter eine wichtige Rolle, als Städte wie Hamburg und Lübeck über die Hanse wirtschaftliche und politische Macht besaßen. Heutzutage ist Hamburg noch immer der geschäftigste Hafen Deutschlands. 

Im Set steigt die maximale Produktion von Häfen nach und nach immer weiter. Das simuliert die Tatsache, dass Schiffe immer größere werden und Innovationen wie die Einführugn von Containern die Menge der umgeschlagenen Güter verfielfachten. 

Diese Industrie benötigt Extension: [Aluminium](#extension_0) [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) [Automobilbau](#extension_2) 


Farbe in der Übersichtskarte:<span style="background-color:#fc6c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) | [Bauxit](#cargo_AORE) |
| [Fahrzeuge](#cargo_VEHI) | [Kohle](#cargo_COAL) |
|  | [Eisenerz](#cargo_IORE) |
|  | [Öl](#cargo_OIL_) |
|  | [Kupferkies](#cargo_PORE) |
|  | [Kautschuk](#cargo_RUBR) |


<a name="industry_120"></a>
### Hotel

<img src="hotel.png" alt="Hotel">

Ob für Urlaub oder Dienstreisen, Hotels sind eine relevante Wirtschaftsgröße. In einigen Regionen wir z.B. an der Ostseeküste ist Tourismus der wichtigste Wirtschaftsfaktor. Große Städte wie Frankfurt oder München haben ebenfalls eine überdurchschnittlich große Zahl an Hotels, da dort Handelsmessen und andere jährliche Festveranstaltungen stattfinden. 

Im set "produzieren" Hotels so viele Passagiere, wie man anliefert, was darstellen soll dass Gäste die dort einchecken irgendwann auch wieder auschecken werden. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#508ca0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Nahrungsmittel](#cargo_FOOD) | [Passagiere](#cargo_PASS) |
| [Passagiere](#cargo_PASS) |  |


<a name="industry_121"></a>
### Hotel

<img src="hotel.png" alt="Hotel">

Ob für Urlaub oder Dienstreisen, Hotels sind eine relevante Wirtschaftsgröße. In einigen Regionen wir z.B. an der Ostseeküste ist Tourismus der wichtigste Wirtschaftsfaktor. Große Städte wie Frankfurt oder München haben ebenfalls eine überdurchschnittlich große Zahl an Hotels, da dort Handelsmessen und andere jährliche Festveranstaltungen stattfinden. 

Im set "produzieren" Hotels so viele Passagiere, wie man anliefert, was darstellen soll dass Gäste die dort einchecken irgendwann auch wieder auschecken werden. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#508ca0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Nahrungsmittel](#cargo_FOOD) | [Passagiere](#cargo_PASS) |
| [Früchte](#cargo_FRUT) |  |
| [Passagiere](#cargo_PASS) |  |


<a name="industry_122"></a>
### Hydrierwerk

<img src="coal_liquefaction_plant.png" alt="Hydrierwerk">

Die Herstellung von Treibstoffen durch die Hydrierung von Kohle war eine Spezialität der deutschen Chemiegeschichte. Da Deutschland keine eigenen Ölvorkommen in relevanter Größe besitzt, war man nach dem ersten Weltkrieg bestrebt, Treibstoffe aus heimischer Kohle zu erzeugen. Der erste derartig erzeugte Kraftstoff war das sogenannte Leuna-Benzin, benannt nach dem Standort der Anlage. Für Nazideutschland waren die Anlagen kriegswichtig und wurden entsprechend staatlich gefördert. Nach Kriegsende schwand die Bedeutung des Verfahrens, da Treibstoffe einfacher und billiger aus verfügbarem Erdöl gewonnen werden können. Allerdings steigt im 21. Jahrhundert die Bedeutung des Verfahrens in vielen Ländern wieder, um der Abhängigkeit von importiertem Erdöl entgegenzuwirken. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_11) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#cccca8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ethylen](#cargo_C2H4) |
| [Wasserstoff](#cargo_H2__) | [Treibstoff](#cargo_PETR) |


<a name="industry_123"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |


<a name="industry_124"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Branntkalk](#cargo_QLME) |  |


<a name="industry_125"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Ammoniak](#extension_1) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |


<a name="industry_126"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Branntkalk](#cargo_QLME) |  |


<a name="industry_127"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Koks und Schwefel](#extension_8) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |


<a name="industry_128"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Branntkalk](#cargo_QLME) |  |


<a name="industry_129"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |


<a name="industry_130"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Branntkalk](#cargo_QLME) |  |


<a name="industry_131"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_132"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Branntkalk](#cargo_QLME) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_133"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_134"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Koks und Schwefel](#extension_8) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Branntkalk](#cargo_QLME) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_135"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_136"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Ammoniak](#extension_1) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Branntkalk](#cargo_QLME) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_137"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_138"></a>
### Integriertes Stahlwerk

<img src="integrated_steel_mill.png" alt="Integriertes Stahlwerk">

Die Stahlproduktion war einer der Kernfaktoren der Industrialisierung im 19. Jahrhundert, insbesondere im Zusammenhang mit der Entwicklung der Eisenbahn. In Deutschland hatte die Stahlindustrie ihre Zentren im Ruhrgebiet und im Saarland, wo ausreichend Kohle verfügbar war, während das Eisenerz importiert wurde. Heutzutage ist die Stahlproduktion noch immer relevant, das Eisenerz wird von den Häfen an der Nordsee zu den Stahlwerken im Ruhrgebiet und in Niedersachsen transportiert. 

Es gibt verschiedene Varianten von Stahlwerken auf Basis unterschiedlicher Prozesse, das Set modelliert aber nur ein modernes hochintegriertes Hüttenwerk. Die verschiedenen Schritte der Stahlerzeugung aus Eisenerz, angefangen mit geschmolzenem Roheisen aus dem Hochofen, finden alle innerhalb des Stahlwerks statt und sind daher für ein Transportspiel nicht relevant. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#949594;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Stahl](#cargo_STEL) |
| [Eisenerz](#cargo_IORE) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Branntkalk](#cargo_QLME) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_139"></a>
### Kalisalzbergwerk

<img src="potash_mine.png" alt="Kalisalzbergwerk">

Kalisalze erlangten seit der Mitte des 19. Jahrhundert eine immense Bedeutung für die Produktion von Düngemitteln. Wie schon beim Salzbergbau liegt die Wiege des Kalisalzbergbaus in Mitteldeutschland. In den Bergwerken Staßfurts fand man 1857 Kalisalze. Heute ist Deutschland mit großem Abstand der größte Produzent Europas. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b88888;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Sprengstoff](#cargo_BOOM) | [Kalisalz](#cargo_POTA) |


<a name="industry_140"></a>
### Kalkbrennerei

<img src="lime_kiln.png" alt="Kalkbrennerei">

In Kalkofen wird für den Prozess der Kalzinierung von Kalkstein genutzt. Diese Reaktion erzeugt Branntkalk, chemisch gesehen wird Calciumcarbonat zu Calciumoxid umgesetzt. Dabei wird der Kalkstein nicht verbrannt, sondern lediglich großer Hitze ausgesetzt. Der Prozess ist seit Jahrtausenden bekannt, und Branntkalk wird seit Ewigkeiten zur Herstellung von Zement verwendet. Der Ofen wird üblicherweise durch das Verbrennen fossiler Brennstoffe erhitzt, was den ohnehin unvermeidlichen Kohlendioxidausstoß weiter erhöht. 

Diese Industrie benötigt Extension: [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 


Farbe in der Übersichtskarte:<span style="background-color:#8c68fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalkstein](#cargo_LIME) | [Branntkalk](#cargo_QLME) |


<a name="industry_141"></a>
### Kalkbrennerei

<img src="lime_kiln.png" alt="Kalkbrennerei">

In Kalkofen wird für den Prozess der Kalzinierung von Kalkstein genutzt. Diese Reaktion erzeugt Branntkalk, chemisch gesehen wird Calciumcarbonat zu Calciumoxid umgesetzt. Dabei wird der Kalkstein nicht verbrannt, sondern lediglich großer Hitze ausgesetzt. Der Prozess ist seit Jahrtausenden bekannt, und Branntkalk wird seit Ewigkeiten zur Herstellung von Zement verwendet. Der Ofen wird üblicherweise durch das Verbrennen fossiler Brennstoffe erhitzt, was den ohnehin unvermeidlichen Kohlendioxidausstoß weiter erhöht. 

Diese Industrie benötigt Extension: [Glas](#extension_6) [Koks und Schwefel](#extension_8) 


Farbe in der Übersichtskarte:<span style="background-color:#8c68fc;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Koks](#cargo_COKE) | [Branntkalk](#cargo_QLME) |
| [Kalkstein](#cargo_LIME) |  |


<a name="industry_142"></a>
### Kalksteinbergwerk

<img src="limestone_mine.png" alt="Kalksteinbergwerk">

Kalkstein wird bereits seit Jahrhunderten in Deutschland abgebaut, üblicherweise in Steinbrüchen. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_3) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcfcc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kalkstein](#cargo_LIME) |


<a name="industry_143"></a>
### Kalksteinbergwerk

<img src="limestone_mine.png" alt="Kalksteinbergwerk">

Kalkstein wird bereits seit Jahrhunderten in Deutschland abgebaut, üblicherweise in Steinbrüchen. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_3) [Produktionsboost](#extension_13) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcfcc0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Sprengstoff](#cargo_BOOM) | [Kalkstein](#cargo_LIME) |


<a name="industry_144"></a>
### Karosseriefabrik

<img src="vehicle_body_plant.png" alt="Karosseriefabrik">

Im modernen Automobilbau werden Karosserien oft in spezialisierten Fabriken hergestellt, die großteils automatisiert sind. Roboter schweißen und kleben Bleche zusammen, die dann verzinkt und lackiert die Karosserie ergeben. Diese Karosserien werden dann zur Endmontage in die Automobilfabrik transportiert. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Aluminium](#extension_0) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Karosserien](#cargo_VBOD) |
| [Stahl](#cargo_STEL) |  |
| [Zink](#cargo_ZINC) |  |


<a name="industry_145"></a>
### Karosseriefabrik

<img src="vehicle_body_plant.png" alt="Karosseriefabrik">

Im modernen Automobilbau werden Karosserien oft in spezialisierten Fabriken hergestellt, die großteils automatisiert sind. Roboter schweißen und kleben Bleche zusammen, die dann verzinkt und lackiert die Karosserie ergeben. Diese Karosserien werden dann zur Endmontage in die Automobilfabrik transportiert. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Karosserien](#cargo_VBOD) |
| [Farbe](#cargo_COAT) |  |
| [Stahl](#cargo_STEL) |  |
| [Zink](#cargo_ZINC) |  |


<a name="industry_146"></a>
### Karosseriefabrik

<img src="vehicle_body_plant.png" alt="Karosseriefabrik">

Im modernen Automobilbau werden Karosserien oft in spezialisierten Fabriken hergestellt, die großteils automatisiert sind. Roboter schweißen und kleben Bleche zusammen, die dann verzinkt und lackiert die Karosserie ergeben. Diese Karosserien werden dann zur Endmontage in die Automobilfabrik transportiert. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Karosserien](#cargo_VBOD) |
| [Aluminium](#cargo_ALUM) |  |
| [Stahl](#cargo_STEL) |  |
| [Zink](#cargo_ZINC) |  |


<a name="industry_147"></a>
### Karosseriefabrik

<img src="vehicle_body_plant.png" alt="Karosseriefabrik">

Im modernen Automobilbau werden Karosserien oft in spezialisierten Fabriken hergestellt, die großteils automatisiert sind. Roboter schweißen und kleben Bleche zusammen, die dann verzinkt und lackiert die Karosserie ergeben. Diese Karosserien werden dann zur Endmontage in die Automobilfabrik transportiert. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Farbindustrie](#extension_4) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Karosserien](#cargo_VBOD) |
| [Aluminium](#cargo_ALUM) |  |
| [Farbe](#cargo_COAT) |  |
| [Stahl](#cargo_STEL) |  |
| [Zink](#cargo_ZINC) |  |


<a name="industry_148"></a>
### Karosseriefabrik

<img src="vehicle_body_plant.png" alt="Karosseriefabrik">

Im modernen Automobilbau werden Karosserien oft in spezialisierten Fabriken hergestellt, die großteils automatisiert sind. Roboter schweißen und kleben Bleche zusammen, die dann verzinkt und lackiert die Karosserie ergeben. Diese Karosserien werden dann zur Endmontage in die Automobilfabrik transportiert. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Karosserien](#cargo_VBOD) |
| [Bleche](#cargo_STSH) |  |
| [Zink](#cargo_ZINC) |  |


<a name="industry_149"></a>
### Karosseriefabrik

<img src="vehicle_body_plant.png" alt="Karosseriefabrik">

Im modernen Automobilbau werden Karosserien oft in spezialisierten Fabriken hergestellt, die großteils automatisiert sind. Roboter schweißen und kleben Bleche zusammen, die dann verzinkt und lackiert die Karosserie ergeben. Diese Karosserien werden dann zur Endmontage in die Automobilfabrik transportiert. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Farbindustrie](#extension_4) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Karosserien](#cargo_VBOD) |
| [Farbe](#cargo_COAT) |  |
| [Bleche](#cargo_STSH) |  |
| [Zink](#cargo_ZINC) |  |


<a name="industry_150"></a>
### Kaufhaus

<img src="department_store.png" alt="Kaufhaus">

Das Kaufhaus steht stellvertretend für sämtliche Läden einer Stadt, in denen man alles kaufen kann, was man so gebrauchen kann, sei es Kleidung, Haushaltsgegenstände wie Waschmaschinen, Spielzeug usw. Kaufhäuser lösen im Set das Problem dass kleine Städte üblicherweise keine Waren akzeptieren, bevor sie nicht auf eine gewisse Größe angewachsen sind. 


Farbe in der Übersichtskarte:<span style="background-color:#fcf4ec;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Waren](#cargo_GOOD) |  |


<a name="industry_151"></a>
### Kohlebergwerk

<img src="coal_mine.png" alt="Kohlebergwerk">

Kohlebergbau wurde im Zuge der industriellen Revolution im 19. Jahrhundert einer der wichtigsten Industriezweige, da man die Kohle zum Antrieb der Dampfmaschinen brauchte. Mit Dampfmaschinen wurde quasi alles angetrieben, ob nun Wasserpumpen in den Bergwerken oder Webstühle. Mit der Entwicklung der Eisenbahn und der Einführung der Dampfschiffahrt wuchs der Bedarf nach Kohle noch weiter. 

Der Kohlebergbau begann in Deutschland hautpsächlich im Ruhrgebiet und in Schlesien, aber auch im Saarland. Entsprechend waren diese Gebiete auch die Zentren der Schwerindustrie. Im frühen 20. Jahrhundert stieg die Produktion rasch an, da sich neuartige Technologien wie der Presslufhammer durchsetzten. Zu dieser Zeit war Deutschland einer der größten Kohleproduzenten der Welt. Nach dem Zweiten Weltkrieg war das Produktionsmaximum in den 1950er Jahren erreicht. Die steigenden Kosten machten den Kohlebergbau unprofitable, so dass die Industrie seit den 1960er Jahren schrumpfte und jahrzehntelang subventioniert werden musste. Die letzten Kohlebergwerke stellten den Betrieb 2018 ein. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 

Industry ist nur von 1800 bis 1950 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#101010;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kohle](#cargo_COAL) |


<a name="industry_152"></a>
### Kohlebergwerk

<img src="coal_mine.png" alt="Kohlebergwerk">

Kohlebergbau wurde im Zuge der industriellen Revolution im 19. Jahrhundert einer der wichtigsten Industriezweige, da man die Kohle zum Antrieb der Dampfmaschinen brauchte. Mit Dampfmaschinen wurde quasi alles angetrieben, ob nun Wasserpumpen in den Bergwerken oder Webstühle. Mit der Entwicklung der Eisenbahn und der Einführung der Dampfschiffahrt wuchs der Bedarf nach Kohle noch weiter. 

Der Kohlebergbau begann in Deutschland hautpsächlich im Ruhrgebiet und in Schlesien, aber auch im Saarland. Entsprechend waren diese Gebiete auch die Zentren der Schwerindustrie. Im frühen 20. Jahrhundert stieg die Produktion rasch an, da sich neuartige Technologien wie der Presslufhammer durchsetzten. Zu dieser Zeit war Deutschland einer der größten Kohleproduzenten der Welt. Nach dem Zweiten Weltkrieg war das Produktionsmaximum in den 1950er Jahren erreicht. Die steigenden Kosten machten den Kohlebergbau unprofitable, so dass die Industrie seit den 1960er Jahren schrumpfte und jahrzehntelang subventioniert werden musste. Die letzten Kohlebergwerke stellten den Betrieb 2018 ein. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 

Industry ist nur von 1800 bis 1950 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#101010;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Sprengstoff](#cargo_BOOM) | [Kohle](#cargo_COAL) |


<a name="industry_153"></a>
### Kokerei

<img src="coke_oven.png" alt="Kokerei">

Kohle enthält einen gewissen Anteil an Schwefel, der beim Verbrennen frei wird und dann, je nach Verwendungszweck, Probleme verursachen kann. So hat er negativen Einfluss auf die Qualität von Roheisen im Rahmen der Stahlproduktion. Die Lösung ist die Aufwertung von Kohle zu Koks, bei der der Schwefel entfernt wird und hochreiner Kohlenstoff über bleibt. Früher gab es in Deutschland eine ganze Reiher Kokereien, die nicht nur Koks herstellten, sondern als Nebenprodukte auch Schwefel und andere Chemikalien produzieren. Heutzutage sind aufgrund des Strukturwandels seit den 70er Jahren nur noch eine Handvoll Kokereien im Ruhrgebiet in Betrieb. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#444c5c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Koks](#cargo_COKE) |
|  | [Schwefel](#cargo_SULP) |


<a name="industry_154"></a>
### Kraftwerk

<img src="power_plant.png" alt="Kraftwerk">

Kraftwerke erzeugen elektrischen Strom, üblicherweise indem sie Wasser kochen und mit dem Wasserdampf Turbinen antreiben, die wiederum mit Generatoren gekuppelt sind. Das gleiche Prinzip wird auch in Atomkraftwerken angewandt, während Wasserkraftwerke das Wasser direkt auf die Turbinen leiten. Da es im Spiel um den Transport von Frachten geht, konzentriert sich das Set auf fossile Energien und den Transport von Kohle und Öl. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Früchte und Bioenergie](#extension_5) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) |  |
| [Öl](#cargo_OIL_) |  |


<a name="industry_155"></a>
### Kraftwerk

<img src="power_plant.png" alt="Kraftwerk">

Kraftwerke erzeugen elektrischen Strom, üblicherweise indem sie Wasser kochen und mit dem Wasserdampf Turbinen antreiben, die wiederum mit Generatoren gekuppelt sind. Das gleiche Prinzip wird auch in Atomkraftwerken angewandt, während Wasserkraftwerke das Wasser direkt auf die Turbinen leiten. Da es im Spiel um den Transport von Frachten geht, konzentriert sich das Set auf fossile Energien und den Transport von Kohle und Öl. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Schwefel](#cargo_SULP) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_156"></a>
### Kraftwerk

<img src="power_plant.png" alt="Kraftwerk">

Kraftwerke erzeugen elektrischen Strom, üblicherweise indem sie Wasser kochen und mit dem Wasserdampf Turbinen antreiben, die wiederum mit Generatoren gekuppelt sind. Das gleiche Prinzip wird auch in Atomkraftwerken angewandt, während Wasserkraftwerke das Wasser direkt auf die Turbinen leiten. Da es im Spiel um den Transport von Frachten geht, konzentriert sich das Set auf fossile Energien und den Transport von Kohle und Öl. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Biomasse](#cargo_BIOM) |  |
| [Kohle](#cargo_COAL) |  |
| [Öl](#cargo_OIL_) |  |


<a name="industry_157"></a>
### Kraftwerk

<img src="power_plant.png" alt="Kraftwerk">

Kraftwerke erzeugen elektrischen Strom, üblicherweise indem sie Wasser kochen und mit dem Wasserdampf Turbinen antreiben, die wiederum mit Generatoren gekuppelt sind. Das gleiche Prinzip wird auch in Atomkraftwerken angewandt, während Wasserkraftwerke das Wasser direkt auf die Turbinen leiten. Da es im Spiel um den Transport von Frachten geht, konzentriert sich das Set auf fossile Energien und den Transport von Kohle und Öl. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Früchte und Bioenergie](#extension_5) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fc0000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Biomasse](#cargo_BIOM) | [Schwefel](#cargo_SULP) |
| [Kohle](#cargo_COAL) |  |
| [Öl](#cargo_OIL_) |  |


<a name="industry_158"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Farbindustrie](#extension_4) [Organische Chemie](#extension_11) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Öl](#cargo_OIL_) | [Kunststoffe](#cargo_PLAS) |


<a name="industry_159"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) [Organische Chemie](#extension_11) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Kunststoffe](#cargo_PLAS) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_160"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Organische Chemie](#extension_11) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Kunststoffe](#cargo_PLAS) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_161"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Kunststoffe](#cargo_PLAS) |
| [Farbe](#cargo_COAT) |  |
| [Öl](#cargo_OIL_) |  |


<a name="industry_162"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Farbindustrie](#extension_4) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Kunststoffe](#cargo_PLAS) |


<a name="industry_163"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Kunststoffe](#cargo_PLAS) |
| [Chlor](#cargo_CHLO) |  |


<a name="industry_164"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Kunststoffe](#cargo_PLAS) |
| [Farbe](#cargo_COAT) |  |


<a name="industry_165"></a>
### Kunststofffabrik

<img src="plastics_plant.png" alt="Kunststofffabrik">

Kunststoffe umfassen alle Arten von künstlich hergestellten Materialien wie PVC oder Polyethylen. In Deutschland begann die Kunststoffproduktion mit künstlichem Kautschuk unter dem Namen Buna in den 1930er Jahren. Die Buna-Werke in Schkopau existieren noch heute und produzieren nach wie vor, gehören allerdings inzwischen zu Dow Chemical. BASF, einer der größten Chemiekonzerne der Welt, entwickelte im Verlauf des 20. Jahrhunderts ebenfalls verschiedene Arten von Kunststoffen. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Farbindustrie](#extension_4) [Organische Chemie](#extension_11) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcc000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Kunststoffe](#cargo_PLAS) |
| [Chlor](#cargo_CHLO) |  |
| [Farbe](#cargo_COAT) |  |


<a name="industry_166"></a>
### Kupfererzbergwerk

<img src="copper_ore_mine.png" alt="Kupfererzbergwerk">

Kupfererze wurden schon seit dem Altertum abgebaut. Im Set sind die Bergwerke, wie alle anderen Bergwerke auch, erst später verfügbar, da man ohne mechanische Unterstützung nicht im großen Maßstab Bergbau betreiben kann. In Europa gab es nur wenige Erzlagerstäten. Kupfererz wurde in Mitteldeutschland abgebaut, aber die Vorräte waren bereits vor Beginn der industriellen Revolution erschöpft. Die letzten Kupfererzbergwerke waren noch bis Mitte des 20. Jahrhunderts in Betrieb, was jedoch gerade in Ostdeutschland politische Gründe hatte, denn man hatte keinen Zugang zum Kupferweltmarkt. Heute wird Kupfererz importiert, während das Recycling von Kupferschrott eine wachsende Bedeutung hat. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Produktionsboost](#extension_13) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kupfererz](#cargo_CORE) |


<a name="industry_167"></a>
### Kupfererzbergwerk

<img src="copper_ore_mine.png" alt="Kupfererzbergwerk">

Kupfererze wurden schon seit dem Altertum abgebaut. Im Set sind die Bergwerke, wie alle anderen Bergwerke auch, erst später verfügbar, da man ohne mechanische Unterstützung nicht im großen Maßstab Bergbau betreiben kann. In Europa gab es nur wenige Erzlagerstäten. Kupfererz wurde in Mitteldeutschland abgebaut, aber die Vorräte waren bereits vor Beginn der industriellen Revolution erschöpft. Die letzten Kupfererzbergwerke waren noch bis Mitte des 20. Jahrhunderts in Betrieb, was jedoch gerade in Ostdeutschland politische Gründe hatte, denn man hatte keinen Zugang zum Kupferweltmarkt. Heute wird Kupfererz importiert, während das Recycling von Kupferschrott eine wachsende Bedeutung hat. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Kupferkies](#cargo_PORE) |


<a name="industry_168"></a>
### Kupfererzbergwerk

<img src="copper_ore_mine.png" alt="Kupfererzbergwerk">

Kupfererze wurden schon seit dem Altertum abgebaut. Im Set sind die Bergwerke, wie alle anderen Bergwerke auch, erst später verfügbar, da man ohne mechanische Unterstützung nicht im großen Maßstab Bergbau betreiben kann. In Europa gab es nur wenige Erzlagerstäten. Kupfererz wurde in Mitteldeutschland abgebaut, aber die Vorräte waren bereits vor Beginn der industriellen Revolution erschöpft. Die letzten Kupfererzbergwerke waren noch bis Mitte des 20. Jahrhunderts in Betrieb, was jedoch gerade in Ostdeutschland politische Gründe hatte, denn man hatte keinen Zugang zum Kupferweltmarkt. Heute wird Kupfererz importiert, während das Recycling von Kupferschrott eine wachsende Bedeutung hat. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Sprengstoff](#cargo_BOOM) | [Kupfererz](#cargo_CORE) |


<a name="industry_169"></a>
### Kupfererzbergwerk

<img src="copper_ore_mine.png" alt="Kupfererzbergwerk">

Kupfererze wurden schon seit dem Altertum abgebaut. Im Set sind die Bergwerke, wie alle anderen Bergwerke auch, erst später verfügbar, da man ohne mechanische Unterstützung nicht im großen Maßstab Bergbau betreiben kann. In Europa gab es nur wenige Erzlagerstäten. Kupfererz wurde in Mitteldeutschland abgebaut, aber die Vorräte waren bereits vor Beginn der industriellen Revolution erschöpft. Die letzten Kupfererzbergwerke waren noch bis Mitte des 20. Jahrhunderts in Betrieb, was jedoch gerade in Ostdeutschland politische Gründe hatte, denn man hatte keinen Zugang zum Kupferweltmarkt. Heute wird Kupfererz importiert, während das Recycling von Kupferschrott eine wachsende Bedeutung hat. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) [Produktionsboost](#extension_13) 

Industry ist nur von 1800 bis 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#501c04;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Sprengstoff](#cargo_BOOM) | [Kupferkies](#cargo_PORE) |


<a name="industry_170"></a>
### Kupferhütte

<img src="copper_smelter.png" alt="Kupferhütte">

Die Erzeugung von Kupfer aus Kupfererz ist ein energieintensiver Prozess auf Basis von Elektrolyse. Nebenprodukte sind weitere Metallerze sowie Schwefel, je nach Qualität des verwendeten Kupfererzes. Im Set wird davon ausgegangen, dass Kupfererz hoher Qualität verwendet wird, während schwefelreiche Erze Teil einer anderen Erweiterung sind. Der größte Kupferproduzent Europas ist in Hamburg ansässig und erzeugt dort Kupfer aus importiertem Erz und aus Metallschrott. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Kupfererz](#cargo_CORE) | [Kupfer](#cargo_COPR) |


<a name="industry_171"></a>
### Kupferhütte

<img src="copper_smelter.png" alt="Kupferhütte">

Die Erzeugung von Kupfer aus Kupfererz ist ein energieintensiver Prozess auf Basis von Elektrolyse. Nebenprodukte sind weitere Metallerze sowie Schwefel, je nach Qualität des verwendeten Kupfererzes. Im Set wird davon ausgegangen, dass Kupfererz hoher Qualität verwendet wird, während schwefelreiche Erze Teil einer anderen Erweiterung sind. Der größte Kupferproduzent Europas ist in Hamburg ansässig und erzeugt dort Kupfer aus importiertem Erz und aus Metallschrott. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Kupfer](#cargo_COPR) |
| [Kupfererz](#cargo_CORE) |  |


<a name="industry_172"></a>
### Kupferhütte

<img src="copper_smelter.png" alt="Kupferhütte">

Die Erzeugung von Kupfer aus Kupfererz ist ein energieintensiver Prozess auf Basis von Elektrolyse. Nebenprodukte sind weitere Metallerze sowie Schwefel, je nach Qualität des verwendeten Kupfererzes. Im Set wird davon ausgegangen, dass Kupfererz hoher Qualität verwendet wird, während schwefelreiche Erze Teil einer anderen Erweiterung sind. Der größte Kupferproduzent Europas ist in Hamburg ansässig und erzeugt dort Kupfer aus importiertem Erz und aus Metallschrott. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Kupfererz](#cargo_CORE) | [Kupfer](#cargo_COPR) |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_173"></a>
### Kupferhütte

<img src="copper_smelter.png" alt="Kupferhütte">

Die Erzeugung von Kupfer aus Kupfererz ist ein energieintensiver Prozess auf Basis von Elektrolyse. Nebenprodukte sind weitere Metallerze sowie Schwefel, je nach Qualität des verwendeten Kupfererzes. Im Set wird davon ausgegangen, dass Kupfererz hoher Qualität verwendet wird, während schwefelreiche Erze Teil einer anderen Erweiterung sind. Der größte Kupferproduzent Europas ist in Hamburg ansässig und erzeugt dort Kupfer aus importiertem Erz und aus Metallschrott. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Koks und Schwefel](#extension_8) [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#8c4c40;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie elektrischen Strom zur Production. Siehe [Elektrizität](#electricity).

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Kupfer](#cargo_COPR) |
| [Kupfererz](#cargo_CORE) |  |
| [Metallschrott](#cargo_SCMT) |  |


<a name="industry_174"></a>
### Laden

<img src="general_store.png" alt="Laden">

Der Lebensmittelladen ist im Prinzip eine Darstellung dessen, was heutzutage als Supermarkt bekannt ist. Supermärkte entstanden allerdings erst in der zweiten Hälfte des 20. Jahrhunderts, vorher war der klassische Tante-Emma-Laden oder der Wochenmarkt der Platz, wo man Lebensmittel kaufte. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd8c8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Nahrungsmittel](#cargo_FOOD) |  |


<a name="industry_175"></a>
### Laden

<img src="general_store.png" alt="Laden">

Der Lebensmittelladen ist im Prinzip eine Darstellung dessen, was heutzutage als Supermarkt bekannt ist. Supermärkte entstanden allerdings erst in der zweiten Hälfte des 20. Jahrhunderts, vorher war der klassische Tante-Emma-Laden oder der Wochenmarkt der Platz, wo man Lebensmittel kaufte. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd8c8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Nahrungsmittel](#cargo_FOOD) |  |
| [Früchte](#cargo_FRUT) |  |


<a name="industry_176"></a>
### Luftzerleger

<img src="cryo_plant.png" alt="Luftzerleger">

Für viele industrielle Anwendungen wird reiner Sauerstoff bzw. reiner Stickstoff benötigt. Dies wird seit Beginn des 20. Jahrhunderts durch die Gastrennung von Luft umgesetzt. Dabei wird die Luft im sogenannten Linde-Verfahren so stark abgekühlt, dass sie sich verflüssigt. Danach lassen sich die Bestandteile durch Ausnutzen der unterschiedlichen Siedetemperaturen voneinander trennen. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#0060d4;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Stickstoff](#cargo_N2__) |
|  | [Sauerstoff](#cargo_O2__) |


<a name="industry_177"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Milch](#cargo_MILK) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_178"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Grundlegende Anorganische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Natronlauge](#cargo_LYE_) | [Nahrungsmittel](#cargo_FOOD) |
| [Milch](#cargo_MILK) |  |


<a name="industry_179"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Milch](#cargo_MILK) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_180"></a>
### Molkerei

<img src="dairy.png" alt="Molkerei">

Eine Molkerei ist ein Betrieb, der Milchprodukte wie Butter und Käse herstellt. Die Milch wiederum stammt aus Viehzuchtbetrieben. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#fcd898;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Natronlauge](#cargo_LYE_) | [Nahrungsmittel](#cargo_FOOD) |
| [Milch](#cargo_MILK) |  |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_181"></a>
### Motorenwerk

<img src="vehicle_engine_plant.png" alt="Motorenwerk">

Motoren werden heute in vielen Fällen in eigenen Fabriken hergestellt und dann zur Endmontage der Fahrzeuge weitertransportiert. Geschichtlich gab es in Deutschland außerdem spezialisierte Motorenfabriken, beispielsweise für Flugzeugmotoren oder große Industriemaschinen. Die Maschinenfabrik Augsburg-Nürnberg (heute bekannt als MAN) beispielsweise gilt als Geburtsstätte des Dieselmotors, in München gab es im frühen 20. Jahrhundert mehrere Flugmotorenwerke, aus denen die heute als BMW bekannte Firma hervorging. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Stahl](#cargo_STEL) | [Motoren](#cargo_VENG) |


<a name="industry_182"></a>
### Motorenwerk

<img src="vehicle_engine_plant.png" alt="Motorenwerk">

Motoren werden heute in vielen Fällen in eigenen Fabriken hergestellt und dann zur Endmontage der Fahrzeuge weitertransportiert. Geschichtlich gab es in Deutschland außerdem spezialisierte Motorenfabriken, beispielsweise für Flugzeugmotoren oder große Industriemaschinen. Die Maschinenfabrik Augsburg-Nürnberg (heute bekannt als MAN) beispielsweise gilt als Geburtsstätte des Dieselmotors, in München gab es im frühen 20. Jahrhundert mehrere Flugmotorenwerke, aus denen die heute als BMW bekannte Firma hervorging. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Motoren](#cargo_VENG) |
| [Stahl](#cargo_STEL) |  |


<a name="industry_183"></a>
### Motorenwerk

<img src="vehicle_engine_plant.png" alt="Motorenwerk">

Motoren werden heute in vielen Fällen in eigenen Fabriken hergestellt und dann zur Endmontage der Fahrzeuge weitertransportiert. Geschichtlich gab es in Deutschland außerdem spezialisierte Motorenfabriken, beispielsweise für Flugzeugmotoren oder große Industriemaschinen. Die Maschinenfabrik Augsburg-Nürnberg (heute bekannt als MAN) beispielsweise gilt als Geburtsstätte des Dieselmotors, in München gab es im frühen 20. Jahrhundert mehrere Flugmotorenwerke, aus denen die heute als BMW bekannte Firma hervorging. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Maschinenteile](#cargo_ENSP) | [Motoren](#cargo_VENG) |
| [Stahl](#cargo_STEL) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_184"></a>
### Motorenwerk

<img src="vehicle_engine_plant.png" alt="Motorenwerk">

Motoren werden heute in vielen Fällen in eigenen Fabriken hergestellt und dann zur Endmontage der Fahrzeuge weitertransportiert. Geschichtlich gab es in Deutschland außerdem spezialisierte Motorenfabriken, beispielsweise für Flugzeugmotoren oder große Industriemaschinen. Die Maschinenfabrik Augsburg-Nürnberg (heute bekannt als MAN) beispielsweise gilt als Geburtsstätte des Dieselmotors, in München gab es im frühen 20. Jahrhundert mehrere Flugmotorenwerke, aus denen die heute als BMW bekannte Firma hervorging. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Aluminium](#extension_0) [Metallurgie](#extension_10) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#4898d8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Motoren](#cargo_VENG) |
| [Maschinenteile](#cargo_ENSP) |  |
| [Stahl](#cargo_STEL) |  |
| [Draht/Kabel](#cargo_STWR) |  |


<a name="industry_185"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Waren](#cargo_GOOD) |
| [Textilien](#cargo_TEXT) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_186"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Waren](#cargo_GOOD) |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_187"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Textilien](#cargo_TEXT) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_188"></a>
### Möbelfabrik

<img src="furniture_factory.png" alt="Möbelfabrik">

Deutschland hat eine vergleichsweise große Möbelindustrie, wobei IKEA der Marktführer ist. In aller Regel werden Möbel von spezialisierten Händlern vertrieben, die zahllose Möbelgeschäfte im ganzen Land betreiben. Die klassische Möbelherstellung durch Tischler hat hingegen kaum noch eine Relevanz. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) 


Farbe in der Übersichtskarte:<span style="background-color:#a888e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Schnittholz](#cargo_WDPR) |  |


<a name="industry_189"></a>
### Mühle

<img src="flour_mill.png" alt="Mühle">

Getreidemühlen gibt es seit tausenden von Jahren. Sie mahlen Getreide zu Mehl, was eine überaus wichtige Rolle in der Nahrungsmittelproduktion stellt. Das Mahlen fand traditionell auf einem rotierenden Mahlstein statt, der üblicherweise durch Wasser oder Windkraft bewegt wurde. Mühlen waren überall zu finden, so wie der Familienname Müller aus der Berufsbezeichnung abgeleitet wurde. Die Industrialisierung hat den Prozess der Mehlproduktion erheblich verändert, da mit maschinellem Antrieb viel größere Produktionsmengen möglich wurden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#d4bc94;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_190"></a>
### Mühle

<img src="flour_mill.png" alt="Mühle">

Getreidemühlen gibt es seit tausenden von Jahren. Sie mahlen Getreide zu Mehl, was eine überaus wichtige Rolle in der Nahrungsmittelproduktion stellt. Das Mahlen fand traditionell auf einem rotierenden Mahlstein statt, der üblicherweise durch Wasser oder Windkraft bewegt wurde. Mühlen waren überall zu finden, so wie der Familienname Müller aus der Berufsbezeichnung abgeleitet wurde. Die Industrialisierung hat den Prozess der Mehlproduktion erheblich verändert, da mit maschinellem Antrieb viel größere Produktionsmengen möglich wurden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#d4bc94;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_191"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |


<a name="industry_192"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_193"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_194"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Natronlauge](#cargo_LYE_) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_195"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Lebensmittelindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_196"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_197"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_198"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Natronlauge](#cargo_LYE_) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_199"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Früchte](#cargo_FRUT) |  |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_200"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Früchte](#cargo_FRUT) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_201"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Verpackungsmittelindustrie](#extension_16) [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Lebensmittelindustrie](#extension_9) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Früchte](#cargo_FRUT) |  |
| [Getreide](#cargo_GRAI) |  |
| [Vieh](#cargo_LVST) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_202"></a>
### Nahrungsmittelfabrik

<img src="food_processor.png" alt="Nahrungsmittelfabrik">

Die Nahrungsmittelfabrik fasst verschiedenste Industrien zusammen, die Lebensmittel herstellen. Ob es nun eine Bäckereiprodukte sind, Dosenfisch oder Fleisch, alles wird hier hergestellt, um in die Supermarktregale transportiert zu werden. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#a00000;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Fisch](#cargo_FISH) | [Nahrungsmittel](#cargo_FOOD) |
| [Früchte](#cargo_FRUT) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Verpackungen](#cargo_MNSP) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_203"></a>
### Obstplantage

<img src="fruit_plantation.png" alt="Obstplantage">

Obstplantagen sind gerade in Norddeutschland weit verbreitet. Trotzdem werden große Mengen Obst aus südlicheren Ländern importiert, die einfach bessere Wachstumsbedingungen bieten. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#306004;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Früchte](#cargo_FRUT) |


<a name="industry_204"></a>
### Obstplantage

<img src="fruit_plantation.png" alt="Obstplantage">

Obstplantagen sind gerade in Norddeutschland weit verbreitet. Trotzdem werden große Mengen Obst aus südlicheren Ländern importiert, die einfach bessere Wachstumsbedingungen bieten. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#306004;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Früchte](#cargo_FRUT) |


<a name="industry_205"></a>
### Papiermühle

<img src="paper_mill.png" alt="Papiermühle">

Die Papiermühle spaltet Holz durch Chemikalien auf um Zellulosefasern herauszulösen, die wiederum die Basis für die Papierproduktion sind. Der Prozess der Papierherstellung ist seit Tausenden Jahren bekannt, aber die moderne Produktion begann erst im späten 19. Jahrhundert durch verschiedene Fortschritte in der Chemie. Deutschland ist einer der größten Papierproduzenten der Welt, und der größte in Europa. Die Papiermühle im Set ist eine solche moderne Anlage, die Holz auf chemischem Weg spaltet und das Papier später bleicht. 

Diese Industrie benötigt Extension: [Papier](#extension_12) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#9ca0ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Papier](#cargo_PAPR) |
| [Natronlauge](#cargo_LYE_) |  |
| [Holz](#cargo_WOOD) |  |


<a name="industry_206"></a>
### Papiermühle

<img src="paper_mill.png" alt="Papiermühle">

Die Papiermühle spaltet Holz durch Chemikalien auf um Zellulosefasern herauszulösen, die wiederum die Basis für die Papierproduktion sind. Der Prozess der Papierherstellung ist seit Tausenden Jahren bekannt, aber die moderne Produktion begann erst im späten 19. Jahrhundert durch verschiedene Fortschritte in der Chemie. Deutschland ist einer der größten Papierproduzenten der Welt, und der größte in Europa. Die Papiermühle im Set ist eine solche moderne Anlage, die Holz auf chemischem Weg spaltet und das Papier später bleicht. 

Diese Industrie benötigt Extension: [Papier](#extension_12) [Recycling](#extension_14) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#9ca0ac;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Papier](#cargo_PAPR) |
| [Natronlauge](#cargo_LYE_) |  |
| [Wertstoffe](#cargo_RCYC) |  |
| [Holz](#cargo_WOOD) |  |


<a name="industry_207"></a>
### Reifenfabrik

<img src="tyre_plant.png" alt="Reifenfabrik">

Schon die ersten Autos waren gummibereift, und parallel zur Autoindustrie boomte entsprechend auch die Reifenindustrie. Heute werden jährlich Milliarden von Reifen produziert, wobei sich aus den Anfängen der ersten Erfinder (Charles Goodyear erfand die Vulkanisation und Édouard Michelin den wirtschaftlich erfolgreichen Schlauchreifen) zugleich heute noch existierende Großkonzerne entwickelten. Einer der großen Namen im Reifengeschäft ist die in Deutschland ansässige Continental AG, die 1904 die ersten Profilreifen für Automobile auf den Markt brachten. Die Lego Group ist hingegen nach Stückzahl mit großem Abstand der weltgrößte Reifenproduzent überhaupt - für ihre Spielzeuge produzieren sie viermal so viele Reifen wie der Bridgestone-Konzern. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#14347c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kautschuk](#cargo_RUBR) | [Reifen](#cargo_TYRE) |
| [Schwefel](#cargo_SULP) |  |


<a name="industry_208"></a>
### Reifenfabrik

<img src="tyre_plant.png" alt="Reifenfabrik">

Schon die ersten Autos waren gummibereift, und parallel zur Autoindustrie boomte entsprechend auch die Reifenindustrie. Heute werden jährlich Milliarden von Reifen produziert, wobei sich aus den Anfängen der ersten Erfinder (Charles Goodyear erfand die Vulkanisation und Édouard Michelin den wirtschaftlich erfolgreichen Schlauchreifen) zugleich heute noch existierende Großkonzerne entwickelten. Einer der großen Namen im Reifengeschäft ist die in Deutschland ansässige Continental AG, die 1904 die ersten Profilreifen für Automobile auf den Markt brachten. Die Lego Group ist hingegen nach Stückzahl mit großem Abstand der weltgrößte Reifenproduzent überhaupt - für ihre Spielzeuge produzieren sie viermal so viele Reifen wie der Bridgestone-Konzern. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Farbindustrie](#extension_4) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#14347c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ruß](#cargo_CBLK) | [Reifen](#cargo_TYRE) |
| [Kautschuk](#cargo_RUBR) |  |
| [Schwefel](#cargo_SULP) |  |


<a name="industry_209"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Verpackungsmittelindustrie](#extension_16) [Produktionsboost](#extension_13) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Soda](#cargo_SASH) | [Waren](#cargo_GOOD) |


<a name="industry_210"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) [Produktionsboost](#extension_13) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Soda](#cargo_SASH) |  |


<a name="industry_211"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Produktionsboost](#extension_13) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Soda](#cargo_SASH) |  |


<a name="industry_212"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Koks und Schwefel](#extension_8) [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Verpackungen](#cargo_MNSP) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_213"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) [Verpackungsmittelindustrie](#extension_16) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kalisalz](#cargo_POTA) | [Waren](#cargo_GOOD) |
| [Soda](#cargo_SASH) |  |


<a name="industry_214"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Koks und Schwefel](#extension_8) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Kalisalz](#cargo_POTA) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_215"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Verpackungsmittelindustrie](#extension_16) [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Verpackungen](#cargo_MNSP) | [Waren](#cargo_GOOD) |
| [Kalisalz](#cargo_POTA) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_216"></a>
### Reinigungsmittelfabrik

<img src="cleaning_products_factory.png" alt="Reinigungsmittelfabrik">

Reinigungsmittel wie Seifen und Waschmittel gehörten zu den ersten kommerziellen Produkten der noch jungen chemischen Industrie. So gründeten sich bereits in der zweiten Hälfte des 19. Jahrhunderts spezialisierte Waschmittelhersteller in Deutschland, die teilweise heute als Großkonzerne international tätig sind, man denke nur an Henkel. Zahlreiche Entwicklungen in diesem Bereich wurden in Deutschland angestoßen, so zum Beispiel die Erfindung von synthetischen Vollwaschmitteln in den 1930er Jahren. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) [Koks und Schwefel](#extension_8) [Verpackungsmittelindustrie](#extension_16) [Produktionsboost](#extension_13) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#7044a8;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Waren](#cargo_GOOD) |
| [Verpackungen](#cargo_MNSP) |  |
| [Kalisalz](#cargo_POTA) |  |
| [Soda](#cargo_SASH) |  |


<a name="industry_217"></a>
### Rußfabrik

<img src="carbon_black_plant.png" alt="Rußfabrik">

Die Rußfabrik spaltet Kohlenstoffverbindungen wie Kohle oder Öl auf und erzeugt daraus quasi reines Kohlenstoffpulver. Üblicherweise werden dafür die schweren Fraktionen der Erdöldestillation, Schweröle als, genutzt, die anderweitig kaum Verwendung haben. Je nach eingesetztem Prozess entsteht bei diesem Prozess eine erhebliche Menge Kohlendioxid. Forschungen in jüngster Zeit haben jedoch zu neuen Ansätzen geführt, bei denen Kohlenwasserstoffe komplett in Kohlenstoff und Wasserstoff zerlegt werden, was den ökologischen Fußabdruck massiv reduziert. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) [Ammoniak](#extension_1) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ruß](#cargo_CBLK) |
| [Öl](#cargo_OIL_) |  |


<a name="industry_218"></a>
### Rußfabrik

<img src="carbon_black_plant.png" alt="Rußfabrik">

Die Rußfabrik spaltet Kohlenstoffverbindungen wie Kohle oder Öl auf und erzeugt daraus quasi reines Kohlenstoffpulver. Üblicherweise werden dafür die schweren Fraktionen der Erdöldestillation, Schweröle als, genutzt, die anderweitig kaum Verwendung haben. Je nach eingesetztem Prozess entsteht bei diesem Prozess eine erhebliche Menge Kohlendioxid. Forschungen in jüngster Zeit haben jedoch zu neuen Ansätzen geführt, bei denen Kohlenwasserstoffe komplett in Kohlenstoff und Wasserstoff zerlegt werden, was den ökologischen Fußabdruck massiv reduziert. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ruß](#cargo_CBLK) |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_219"></a>
### Rußfabrik

<img src="carbon_black_plant.png" alt="Rußfabrik">

Die Rußfabrik spaltet Kohlenstoffverbindungen wie Kohle oder Öl auf und erzeugt daraus quasi reines Kohlenstoffpulver. Üblicherweise werden dafür die schweren Fraktionen der Erdöldestillation, Schweröle als, genutzt, die anderweitig kaum Verwendung haben. Je nach eingesetztem Prozess entsteht bei diesem Prozess eine erhebliche Menge Kohlendioxid. Forschungen in jüngster Zeit haben jedoch zu neuen Ansätzen geführt, bei denen Kohlenwasserstoffe komplett in Kohlenstoff und Wasserstoff zerlegt werden, was den ökologischen Fußabdruck massiv reduziert. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ruß](#cargo_CBLK) |
| [Sauerstoff](#cargo_O2__) |  |
| [Öl](#cargo_OIL_) |  |


<a name="industry_220"></a>
### Rußfabrik

<img src="carbon_black_plant.png" alt="Rußfabrik">

Die Rußfabrik spaltet Kohlenstoffverbindungen wie Kohle oder Öl auf und erzeugt daraus quasi reines Kohlenstoffpulver. Üblicherweise werden dafür die schweren Fraktionen der Erdöldestillation, Schweröle als, genutzt, die anderweitig kaum Verwendung haben. Je nach eingesetztem Prozess entsteht bei diesem Prozess eine erhebliche Menge Kohlendioxid. Forschungen in jüngster Zeit haben jedoch zu neuen Ansätzen geführt, bei denen Kohlenwasserstoffe komplett in Kohlenstoff und Wasserstoff zerlegt werden, was den ökologischen Fußabdruck massiv reduziert. 

Diese Industrie benötigt Extension: [Farbindustrie](#extension_4) [Organische Chemie](#extension_11) [Ammoniak](#extension_1) 

Industry ist erst ab 1850 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#626562;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ruß](#cargo_CBLK) |
| [Sauerstoff](#cargo_O2__) |  |
| [Naphtha](#cargo_RFPR) |  |


<a name="industry_221"></a>
### Salzbergwerk

<img src="salt_mine.png" alt="Salzbergwerk">

Aufgrund von jahrtausende währenden geologischen Prozessen gibt es in Nord- und Mitteldeutschland erhebliche Salzlagerstätten. An einigen Stellen tritt salzhaltiges Wasser an die Oberfläche, dort waren bereits im Mittelalter Salzsieder tätig. Eine wichtige Veränderung war der Beginn des Salzbergbaus im 19. Jahrhundert. Das erste Salzbergwerk entstand 1855 in Staßfurt, welches damals zu Preußen gehörte. Im benachbarten Bernburg wird seit etwa 1920 Salz abgebaut, die gesamte Gegend gehört heute zum entsprechend benannten Salzlandkreis. Weitere Bergwerke existieren in Niedersachsen und in Süddeutschland. Heute ist Deutschland mit Abstand der größte Salzproduzent Europas. Damit ist das Salz mit seiner Bedeutung für die chemische Industrie ein wichtiger Wirtschaftsfaktor. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d4d4e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Salz](#cargo_SALT) |


<a name="industry_222"></a>
### Salzbergwerk

<img src="salt_mine.png" alt="Salzbergwerk">

Aufgrund von jahrtausende währenden geologischen Prozessen gibt es in Nord- und Mitteldeutschland erhebliche Salzlagerstätten. An einigen Stellen tritt salzhaltiges Wasser an die Oberfläche, dort waren bereits im Mittelalter Salzsieder tätig. Eine wichtige Veränderung war der Beginn des Salzbergbaus im 19. Jahrhundert. Das erste Salzbergwerk entstand 1855 in Staßfurt, welches damals zu Preußen gehörte. Im benachbarten Bernburg wird seit etwa 1920 Salz abgebaut, die gesamte Gegend gehört heute zum entsprechend benannten Salzlandkreis. Weitere Bergwerke existieren in Niedersachsen und in Süddeutschland. Heute ist Deutschland mit Abstand der größte Salzproduzent Europas. Damit ist das Salz mit seiner Bedeutung für die chemische Industrie ein wichtiger Wirtschaftsfaktor. 

Diese Industrie benötigt Extension: [Grundlegende Anorganische Chemie](#extension_7) [Produktionsboost](#extension_13) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d4d4e0;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
| [Sprengstoff](#cargo_BOOM) | [Salz](#cargo_SALT) |


<a name="industry_223"></a>
### Sandgrube

<img src="sand_pit.png" alt="Sandgrube">

Sand wird üblicherweise in Sandgruben abgebaut. Aufgrund der geologischen Prozesse, die die Erdoberfläche über Millionen von Jahren formten, findet man Sandgruben hauptsächlich in Norddeutschland, aber auch im Alpenraum. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_3) 


Farbe in der Übersichtskarte:<span style="background-color:#e8b810;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie wird mit endlichen Ressourcen generiert und schließt sobald diese erschöpft sind. Siehe [Ressourcen](#resource_depletion).

| Benötigt | Produziert |
| -- | -- |
|  | [Sand](#cargo_SAND) |


<a name="industry_224"></a>
### Schlachthof

<img src="sand_pit.png" alt="Schlachthof">

Schlachthöfe sind Industrien, in denen Vieh geschlachtet und verarbeitet wird, in erster Linie zu Fleisch für den Verzehr. Obwohl das Schlachten von Tieren seit tausenden Jahren üblich ist, explodierte die Menge des produzierten Fleisches im Zuge der Industrialisierung geradezu. Die Einführung effizienter Kühlung erlaubte den Fleischtransport über lange Strecken, was wiederum zu einer Zentralisierung der Industrien in wenige große Schlachthöfe zur Folge hatte. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#b09c6c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Vieh](#cargo_LVST) | [Nahrungsmittel](#cargo_FOOD) |


<a name="industry_225"></a>
### Schlachthof

<img src="sand_pit.png" alt="Schlachthof">

Schlachthöfe sind Industrien, in denen Vieh geschlachtet und verarbeitet wird, in erster Linie zu Fleisch für den Verzehr. Obwohl das Schlachten von Tieren seit tausenden Jahren üblich ist, explodierte die Menge des produzierten Fleisches im Zuge der Industrialisierung geradezu. Die Einführung effizienter Kühlung erlaubte den Fleischtransport über lange Strecken, was wiederum zu einer Zentralisierung der Industrien in wenige große Schlachthöfe zur Folge hatte. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Verpackungsmittelindustrie](#extension_16) 


Farbe in der Übersichtskarte:<span style="background-color:#b09c6c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Vieh](#cargo_LVST) | [Nahrungsmittel](#cargo_FOOD) |
| [Verpackungen](#cargo_MNSP) |  |


<a name="industry_226"></a>
### Schrottplatz

<img src="scrap_yard.png" alt="Schrottplatz">

Am Schrottplatz sammelt sich Altmetall, welches eine bedeutende Rolle für die Industrie besitzt, denn man kann es einschmelzen und so erneut benutzen. Gerade für Aluminium und Kupfer senkt dies die Herstellungskosten erheblich. 

Diese Industrie benötigt Extension: [Recycling](#extension_14) 


Farbe in der Übersichtskarte:<span style="background-color:#404064;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Metallschrott](#cargo_SCMT) |


<a name="industry_227"></a>
### Sodafabrik

<img src="soda_plant.png" alt="Sodafabrik">

Die Herstellung von Soda in industriellem Maßstab war einer der ersten Durchbrüche der technischen Chemie und datiert bis ins späte 18. Jahrhundert zurück. Der bis heute genutzte Standardprozess ist das 1860 entwickelte Solvay-Verfahren, nach dem auch der Solvay-Konzern benannt ist, der das Patent auf das Verfahren hielt. Im späten 19. Jahrhundert hatte sich dieser Prozess etabliert und entsprechende Fabriken wurden in aller Welt erbaut. Andere Firmen wurden ebenso gegründet, so steht das S in BASF für Soda. Die Sodafabrik im mitteldeutschen Bernburg war vor dem Zweiten Weltkrieg die größte der Welt, im benachbarten Staßfurt steht ebenfalls eine Sodafabrik, beide gehören heute zu den größten Produzenten in Europa. 

Diese Industrie benötigt Extension: [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#104060;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Industrie benötigt die in schwarz dargestellten Rohmaterialien zur Produktion. In weiß dargestellte Materialien erhöhen die maximale Produktion.

| Benötigt | Produziert |
| -- | -- |
| [Kalkstein](#cargo_LIME) | [Soda](#cargo_SASH) |
| [Ammoniak](#cargo_NH3_) |  |
| [Salz](#cargo_SALT) |  |


<a name="industry_228"></a>
### Sprengstofffabrik

<img src="explosives_factory.png" alt="Sprengstofffabrik">

Die Sprengstofffabrik produziert, man ahnt es, Sprengstoffe. Diese werden im Bergbau eingesetzt, um die Produktionsmengen zu erhöhen. 

Wesentlicher Rohstoff bei der Produktion ist Ammoniumnitrat. In der Realität werden verschiedenste Chemikalien als Zusätze benutzt, um Sprengstoffe für unterschiedlichste Anwendungen zu erhalten. Im Set wird dies durch Säure und Treibstoff simuliert. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) [Aluminium](#extension_0) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d43434;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Sprengstoff](#cargo_BOOM) |
| [Ammoniumnitrat](#cargo_NHNO) |  |


<a name="industry_229"></a>
### Sprengstofffabrik

<img src="explosives_factory.png" alt="Sprengstofffabrik">

Die Sprengstofffabrik produziert, man ahnt es, Sprengstoffe. Diese werden im Bergbau eingesetzt, um die Produktionsmengen zu erhöhen. 

Wesentlicher Rohstoff bei der Produktion ist Ammoniumnitrat. In der Realität werden verschiedenste Chemikalien als Zusätze benutzt, um Sprengstoffe für unterschiedlichste Anwendungen zu erhalten. Im Set wird dies durch Säure und Treibstoff simuliert. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d43434;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Sprengstoff](#cargo_BOOM) |
| [Aluminium](#cargo_ALUM) |  |
| [Ammoniumnitrat](#cargo_NHNO) |  |


<a name="industry_230"></a>
### Sprengstofffabrik

<img src="explosives_factory.png" alt="Sprengstofffabrik">

Die Sprengstofffabrik produziert, man ahnt es, Sprengstoffe. Diese werden im Bergbau eingesetzt, um die Produktionsmengen zu erhöhen. 

Wesentlicher Rohstoff bei der Produktion ist Ammoniumnitrat. In der Realität werden verschiedenste Chemikalien als Zusätze benutzt, um Sprengstoffe für unterschiedlichste Anwendungen zu erhalten. Im Set wird dies durch Säure und Treibstoff simuliert. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d43434;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Sprengstoff](#cargo_BOOM) |
| [Ammoniumnitrat](#cargo_NHNO) |  |
| [Treibstoff](#cargo_PETR) |  |


<a name="industry_231"></a>
### Sprengstofffabrik

<img src="explosives_factory.png" alt="Sprengstofffabrik">

Die Sprengstofffabrik produziert, man ahnt es, Sprengstoffe. Diese werden im Bergbau eingesetzt, um die Produktionsmengen zu erhöhen. 

Wesentlicher Rohstoff bei der Produktion ist Ammoniumnitrat. In der Realität werden verschiedenste Chemikalien als Zusätze benutzt, um Sprengstoffe für unterschiedlichste Anwendungen zu erhalten. Im Set wird dies durch Säure und Treibstoff simuliert. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) [Organische Chemie](#extension_11) [Aluminium](#extension_0) 

Industry ist erst ab 1880 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#d43434;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Sprengstoff](#cargo_BOOM) |
| [Aluminium](#cargo_ALUM) |  |
| [Ammoniumnitrat](#cargo_NHNO) |  |
| [Treibstoff](#cargo_PETR) |  |


<a name="industry_232"></a>
### Steamcracker

<img src="steamcracker.png" alt="Steamcracker">

In Ölraffinerien fällt in großer Menge Rohbenzin, sogenanntes Naphtha, an. Die chemische Industrie benötigt jedoch Kohlenwasserstoffe, die sich durch Spaltung aus Naphtha erzeugen lassen. Dazu muss das Naphtha auf über 800°C erhitzt werden, so dass es als Gas vorliegt, woher der Name des Prozesses rührt. Als Produkte entstehen verschiedene leichte Kohlenwasserstoffe, die zum Beispiel für die Produktion von Kunststoffen notwendig sind. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_11) 

Industry ist erst ab 1900 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#787840;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Naphtha](#cargo_RFPR) | [Ethylen](#cargo_C2H4) |
|  | [Treibstoff](#cargo_PETR) |


<a name="industry_233"></a>
### Synthesekautschukfabrik

<img src="synthetic_rubber_plant.png" alt="Synthesekautschukfabrik">

Kautschuk kommt zwar in der Natur vor, kann aber nur in Südamerika und Südostasien angebaut werden. Für Deutschland war er daher seit jeher ein strategisch wichtiges Importgut. Bereits im frühen 20. Jahrhundert wurden daher Forschungen durchgeführt, um Kautschuk künstlich zu erzeugen. Dies gelang Ende der 1920er Jahre mit dem sogenannten Buna-Kautschuk auf Basis von Kohlenwasserstoffen, wie sie in der chemischen Industrie leicht verfügbar sind. 

Heute werden zwei Drittel des globalen Bedarfs durch Synthesekautschuk gedeckt. Hauptabnehmer ist die Reifenindustrie. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Organische Chemie](#extension_11) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#081858;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Öl](#cargo_OIL_) | [Kautschuk](#cargo_RUBR) |


<a name="industry_234"></a>
### Synthesekautschukfabrik

<img src="synthetic_rubber_plant.png" alt="Synthesekautschukfabrik">

Kautschuk kommt zwar in der Natur vor, kann aber nur in Südamerika und Südostasien angebaut werden. Für Deutschland war er daher seit jeher ein strategisch wichtiges Importgut. Bereits im frühen 20. Jahrhundert wurden daher Forschungen durchgeführt, um Kautschuk künstlich zu erzeugen. Dies gelang Ende der 1920er Jahre mit dem sogenannten Buna-Kautschuk auf Basis von Kohlenwasserstoffen, wie sie in der chemischen Industrie leicht verfügbar sind. 

Heute werden zwei Drittel des globalen Bedarfs durch Synthesekautschuk gedeckt. Hauptabnehmer ist die Reifenindustrie. 

Diese Industrie benötigt Extension: [Automobilbau](#extension_2) [Organische Chemie](#extension_11) 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#081858;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ethylen](#cargo_C2H4) | [Kautschuk](#cargo_RUBR) |


<a name="industry_235"></a>
### Sägewerk

<img src="sawmill.png" alt="Sägewerk">

Sägewerke schneiden Holz in normierte Größen und Formen, so dass die resultierenden Balken und Bretter in verschiedensten Industrien verwendet werden können. Damit sind Sägewerke ein notwendiger Zwischenschritt in der Bereitstellung von Rohstoffen für die Bauindustrie, die Möbelindustrie und andere. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Holz](#cargo_WOOD) | [Schnittholz](#cargo_WDPR) |


<a name="industry_236"></a>
### Sägewerk

<img src="sawmill.png" alt="Sägewerk">

Sägewerke schneiden Holz in normierte Größen und Formen, so dass die resultierenden Balken und Bretter in verschiedensten Industrien verwendet werden können. Damit sind Sägewerke ein notwendiger Zwischenschritt in der Bereitstellung von Rohstoffen für die Bauindustrie, die Möbelindustrie und andere. 

Diese Industrie benötigt Extension: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#fc9c00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Holz](#cargo_WOOD) | [Biomasse](#cargo_BIOM) |
|  | [Schnittholz](#cargo_WDPR) |


<a name="industry_237"></a>
### Säurefabrik

<img src="acid_plant.png" alt="Säurefabrik">

Schwefelsäure wird in Deutschland in Größenordnungen von mehreren Millionen Tonnen pro Jahr hergestellt und ist damit einer der wichtigsten Grundstoffe der chemischen Industrie. In echten Chemieanlagen werden die Säuren möglichst direkt für weitere Reaktionen verbraucht, um Transporte der gefährlichen Stoffe zu vermeiden. Im Set produziert die Säurefabrik je nach verfügbaren Rohmaterialien verschiedene Arten von Säure, die aber alle als Säure zusammengefasst werden. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Schwefel](#cargo_SULP) | [Säure](#cargo_ACID) |


<a name="industry_238"></a>
### Säurefabrik

<img src="acid_plant.png" alt="Säurefabrik">

Schwefelsäure wird in Deutschland in Größenordnungen von mehreren Millionen Tonnen pro Jahr hergestellt und ist damit einer der wichtigsten Grundstoffe der chemischen Industrie. In echten Chemieanlagen werden die Säuren möglichst direkt für weitere Reaktionen verbraucht, um Transporte der gefährlichen Stoffe zu vermeiden. Im Set produziert die Säurefabrik je nach verfügbaren Rohmaterialien verschiedene Arten von Säure, die aber alle als Säure zusammengefasst werden. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Grundlegende Anorganische Chemie](#extension_7) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Säure](#cargo_ACID) |
| [Wasserstoff](#cargo_H2__) |  |
| [Schwefel](#cargo_SULP) |  |


<a name="industry_239"></a>
### Säurefabrik

<img src="acid_plant.png" alt="Säurefabrik">

Schwefelsäure wird in Deutschland in Größenordnungen von mehreren Millionen Tonnen pro Jahr hergestellt und ist damit einer der wichtigsten Grundstoffe der chemischen Industrie. In echten Chemieanlagen werden die Säuren möglichst direkt für weitere Reaktionen verbraucht, um Transporte der gefährlichen Stoffe zu vermeiden. Im Set produziert die Säurefabrik je nach verfügbaren Rohmaterialien verschiedene Arten von Säure, die aber alle als Säure zusammengefasst werden. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Ammoniak](#extension_1) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Grundlegende Anorganische Chemie](#extension_7) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Ammoniak](#cargo_NH3_) | [Säure](#cargo_ACID) |
| [Sauerstoff](#cargo_O2__) |  |
| [Schwefel](#cargo_SULP) |  |


<a name="industry_240"></a>
### Säurefabrik

<img src="acid_plant.png" alt="Säurefabrik">

Schwefelsäure wird in Deutschland in Größenordnungen von mehreren Millionen Tonnen pro Jahr hergestellt und ist damit einer der wichtigsten Grundstoffe der chemischen Industrie. In echten Chemieanlagen werden die Säuren möglichst direkt für weitere Reaktionen verbraucht, um Transporte der gefährlichen Stoffe zu vermeiden. Im Set produziert die Säurefabrik je nach verfügbaren Rohmaterialien verschiedene Arten von Säure, die aber alle als Säure zusammengefasst werden. 

Diese Industrie benötigt Extension: [Koks und Schwefel](#extension_8) [Grundlegende Anorganische Chemie](#extension_7) [Ammoniak](#extension_1) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#b4cc7c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Chlor](#cargo_CHLO) | [Säure](#cargo_ACID) |
| [Wasserstoff](#cargo_H2__) |  |
| [Ammoniak](#cargo_NH3_) |  |
| [Sauerstoff](#cargo_O2__) |  |
| [Schwefel](#cargo_SULP) |  |


<a name="industry_241"></a>
### Tankstelle

<img src="petrol_station.png" alt="Tankstelle">

Die erste Tankstelle der Geschichte war eine Apotheke in Wiesloch in Südwestdeutschland - dort erstand Bertha Benz 1888 bei der ersten Überlandfahrt von Mannheim nach Pforzheim den notwendigen Treibstoff. Die ersten Tankstellen, die von vornherein als solche konzipiert waren, tauchten erst nach dem Ersten Weltkrieg auf, verbreiteten sich dann jedoch rasant. Damals war es noch üblich, dass ein ausgebildeter Tankwart das Auftanken übernahm und bei der Gelegenheit auch gleich noch den Ölstand prüfte und die Scheibe putzte. Heute ist ein flächendeckendes Tankstellennetz eines der wichtigsten Infrastrukturmerkmale eines Industriestaates. 

Industry ist erst ab 1910 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#78a488;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Treibstoff](#cargo_PETR) |  |


<a name="industry_242"></a>
### Textilfabrik

<img src="textile_mill.png" alt="Textilfabrik">

Die Textilfabrik fasst mehrere Industrien zusammen, die sich mit der Herstellung von Garn und Stoffen beschäftigen. Diese Arbeiten fanden jahrhundertelang hauptsächlich kleingewerblich statt, bevor die Mechanisierung im 18. und 19. Jahrhundert Einzug hielt. Webstühle gehörten damals zu den ersten Geräten, die mechanisch betrieben wurden, um die Produktionszeiten zu verkürzen. Im Set kombiniert diese Industrie sämtliche Schritte der Verarbeitung von Wolle und synthetischen Fasern zu Garn (spinnen), bevor sie z.B. durch Weben zu Stoffen verarbeitet werden. Diese Stoffe werden dann von anderen Industrien verwendet, um verschiedenste Waren zu produzieren. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Farbindustrie](#extension_4) 


Farbe in der Übersichtskarte:<span style="background-color:#a85c4c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Textilien](#cargo_TEXT) |
| [Wolle](#cargo_WOOL) |  |


<a name="industry_243"></a>
### Textilfabrik

<img src="textile_mill.png" alt="Textilfabrik">

Die Textilfabrik fasst mehrere Industrien zusammen, die sich mit der Herstellung von Garn und Stoffen beschäftigen. Diese Arbeiten fanden jahrhundertelang hauptsächlich kleingewerblich statt, bevor die Mechanisierung im 18. und 19. Jahrhundert Einzug hielt. Webstühle gehörten damals zu den ersten Geräten, die mechanisch betrieben wurden, um die Produktionszeiten zu verkürzen. Im Set kombiniert diese Industrie sämtliche Schritte der Verarbeitung von Wolle und synthetischen Fasern zu Garn (spinnen), bevor sie z.B. durch Weben zu Stoffen verarbeitet werden. Diese Stoffe werden dann von anderen Industrien verwendet, um verschiedenste Waren zu produzieren. 

Diese Industrie benötigt Extension: [Textilindustrie](#extension_15) [Farbindustrie](#extension_4) 


Farbe in der Übersichtskarte:<span style="background-color:#a85c4c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Farbe](#cargo_COAT) | [Textilien](#cargo_TEXT) |
| [Kunststoffe](#cargo_PLAS) |  |
| [Wolle](#cargo_WOOL) |  |


<a name="industry_244"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Glas](#extension_6) [Papier](#extension_12) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Kunststoffe](#cargo_PLAS) | [Verpackungen](#cargo_MNSP) |


<a name="industry_245"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) [Papier](#extension_12) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Verpackungen](#cargo_MNSP) |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_246"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Papier](#extension_12) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Glas](#cargo_GLAS) | [Verpackungen](#cargo_MNSP) |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_247"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) [Aluminium](#extension_0) [Glas](#extension_6) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Papier](#extension_12) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Verpackungen](#cargo_MNSP) |
| [Glas](#cargo_GLAS) |  |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_248"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) [Papier](#extension_12) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Glas](#extension_6) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Papier](#cargo_PAPR) | [Verpackungen](#cargo_MNSP) |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_249"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) [Aluminium](#extension_0) [Papier](#extension_12) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Glas](#extension_6) 

Industry ist erst ab 1930 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#804408;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

Die Industrie beginnt mit der Produktion sobald irgendein Rohstoff verfügbar ist. Die maximale Produktion erhöht sich mit der Anzahl der verfügbaren verschiedenen Rohstoffe.

| Benötigt | Produziert |
| -- | -- |
| [Aluminium](#cargo_ALUM) | [Verpackungen](#cargo_MNSP) |
| [Papier](#cargo_PAPR) |  |
| [Kunststoffe](#cargo_PLAS) |  |


<a name="industry_250"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) [Glas](#extension_6) [Papier](#extension_12) 

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


<a name="industry_251"></a>
### Verpackungsmittelfabrik

<img src="packaging_plant.png" alt="Verpackungsmittelfabrik">

Die Verpackungsfabrik produziert alle Arten von Verpackungen aus verschiedensten Materialien, seien es Kunststoffe oder Aluminium. Damit ist diese Anlage ein elementarer Bestandteil der Transportkette, denn ohne Verpackungen reduziert sich die Produktion vieler anderer Industrien. 

Diese Industrie benötigt Extension: [Verpackungsmittelindustrie](#extension_16) [Aluminium](#extension_0) [Glas](#extension_6) [Papier](#extension_12) 

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


<a name="industry_252"></a>
### Viehzucht

<img src="animal_farm.png" alt="Viehzucht">

Viehzuchtbetriebe sind Teil der Landwirtschaft. Sie züchten Vieh und liefern dazugehörige Produkte wie Milch und Wolle. In der Realität sind diese Betriebe heutzutage auf bestimmte Tiere spezialisiert, so dass es Hühnerfarmen oder Schweinemastbetriebe gibt, im Set ist das alles in eine Industrie zusammengefasst. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#90e05c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Vieh](#cargo_LVST) |
|  | [Milch](#cargo_MILK) |


<a name="industry_253"></a>
### Viehzucht

<img src="animal_farm.png" alt="Viehzucht">

Viehzuchtbetriebe sind Teil der Landwirtschaft. Sie züchten Vieh und liefern dazugehörige Produkte wie Milch und Wolle. In der Realität sind diese Betriebe heutzutage auf bestimmte Tiere spezialisiert, so dass es Hühnerfarmen oder Schweinemastbetriebe gibt, im Set ist das alles in eine Industrie zusammengefasst. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Textilindustrie](#extension_15) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#90e05c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Vieh](#cargo_LVST) |
|  | [Milch](#cargo_MILK) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_254"></a>
### Viehzucht

<img src="animal_farm.png" alt="Viehzucht">

Viehzuchtbetriebe sind Teil der Landwirtschaft. Sie züchten Vieh und liefern dazugehörige Produkte wie Milch und Wolle. In der Realität sind diese Betriebe heutzutage auf bestimmte Tiere spezialisiert, so dass es Hühnerfarmen oder Schweinemastbetriebe gibt, im Set ist das alles in eine Industrie zusammengefasst. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Früchte und Bioenergie](#extension_5) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Textilindustrie](#extension_15) 


Farbe in der Übersichtskarte:<span style="background-color:#90e05c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Biomasse](#cargo_BIOM) |
|  | [Vieh](#cargo_LVST) |
|  | [Milch](#cargo_MILK) |


<a name="industry_255"></a>
### Viehzucht

<img src="animal_farm.png" alt="Viehzucht">

Viehzuchtbetriebe sind Teil der Landwirtschaft. Sie züchten Vieh und liefern dazugehörige Produkte wie Milch und Wolle. In der Realität sind diese Betriebe heutzutage auf bestimmte Tiere spezialisiert, so dass es Hühnerfarmen oder Schweinemastbetriebe gibt, im Set ist das alles in eine Industrie zusammengefasst. 

Diese Industrie benötigt Extension: [Lebensmittelindustrie](#extension_9) [Textilindustrie](#extension_15) [Früchte und Bioenergie](#extension_5) 


Farbe in der Übersichtskarte:<span style="background-color:#90e05c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Getreide](#cargo_GRAI) | [Biomasse](#cargo_BIOM) |
|  | [Vieh](#cargo_LVST) |
|  | [Milch](#cargo_MILK) |
|  | [Wolle](#cargo_WOOL) |


<a name="industry_256"></a>
### Wald

<img src="forest.png" alt="Wald">

Wälder wurden bereits als Quelle für Holz genutzt, als Menschen noch mit Speeren jagten und die ersten Holzhütten bauten. Holz hat diverse industrielle Einsatzgebiete, u.a. in der Papierherstellung, somit sind Wälder ein wichtiger Industriezweig, nicht nur in der Realität, sondern auch im Spiel. Im Gegensatz zu den Kohle oder Öl ist Holz auch ein nachwachsender Rohstoff, so dass Wälder im Set unendlich lange produzieren können. 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#68941c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Holz](#cargo_WOOD) |


<a name="industry_257"></a>
### Wald

<img src="forest.png" alt="Wald">

Wälder wurden bereits als Quelle für Holz genutzt, als Menschen noch mit Speeren jagten und die ersten Holzhütten bauten. Holz hat diverse industrielle Einsatzgebiete, u.a. in der Papierherstellung, somit sind Wälder ein wichtiger Industriezweig, nicht nur in der Realität, sondern auch im Spiel. Im Gegensatz zu den Kohle oder Öl ist Holz auch ein nachwachsender Rohstoff, so dass Wälder im Set unendlich lange produzieren können. 

Diese Industrie benötigt Extension: [Produktionsboost](#extension_13) 


Farbe in der Übersichtskarte:<span style="background-color:#68941c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Düngemittel](#cargo_FERT) | [Holz](#cargo_WOOD) |


<a name="industry_258"></a>
### Walzwerk

<img src="sheet_mill.png" alt="Walzwerk">

Im Walzwerk werden Bleche hergestellt, die für die Autoindustrie bestimmt sind. Diese können aus Stahl oder Aluminium gefertigt werden. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Bleche](#cargo_STSH) |
| [Natronlauge](#cargo_LYE_) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_259"></a>
### Walzwerk

<img src="sheet_mill.png" alt="Walzwerk">

Im Walzwerk werden Bleche hergestellt, die für die Autoindustrie bestimmt sind. Diese können aus Stahl oder Aluminium gefertigt werden. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Aluminium](#extension_0) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Bleche](#cargo_STSH) |
| [Aluminium](#cargo_ALUM) |  |
| [Natronlauge](#cargo_LYE_) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_260"></a>
### Walzwerk

<img src="sheet_mill.png" alt="Walzwerk">

Im Walzwerk werden Bleche hergestellt, die für die Autoindustrie bestimmt sind. Diese können aus Stahl oder Aluminium gefertigt werden. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Recycling](#extension_14) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Aluminium](#extension_0) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Metallschrott](#cargo_SCMT) |
| [Natronlauge](#cargo_LYE_) | [Bleche](#cargo_STSH) |
| [Stahl](#cargo_STEL) |  |


<a name="industry_261"></a>
### Walzwerk

<img src="sheet_mill.png" alt="Walzwerk">

Im Walzwerk werden Bleche hergestellt, die für die Autoindustrie bestimmt sind. Diese können aus Stahl oder Aluminium gefertigt werden. 

Diese Industrie benötigt Extension: [Metallurgie](#extension_10) [Aluminium](#extension_0) [Recycling](#extension_14) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#58340c;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Säure](#cargo_ACID) | [Metallschrott](#cargo_SCMT) |
| [Aluminium](#cargo_ALUM) | [Bleche](#cargo_STSH) |
| [Natronlauge](#cargo_LYE_) |  |
| [Stahl](#cargo_STEL) |  |


<a name="industry_262"></a>
### Wertstoffhof

<img src="recycling_depot.png" alt="Wertstoffhof">

Im Wertstoffhof werden Wertstoffe gesammelt, die kein Abfall sind, sondern aufbereitet und erneut verarbeitet werden können, wie zum Beispiel Glas oder Altpapier. Die Produktion des Wertstoffhofs hängt von der Größe der Stadt ab, je größer die Stadt, desto höher seine Produktion. 

Diese Industrie benötigt Extension: [Recycling](#extension_14) [Glas](#extension_6) [Papier](#extension_12) 


Farbe in der Übersichtskarte:<span style="background-color:#646488;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
|  | [Wertstoffe](#cargo_RCYC) |


<a name="industry_263"></a>
### Zementfabrik

<img src="cement_plant.png" alt="Zementfabrik">

Die ersten Zementwerke in Deutschland entstanden im frühen 19. Jahrhundert. In der zweiten Hälfte des Jahrhunderts wurden die Produktionsprozesse und Qualitätsanforderungen vereinheitlicht und standardisiert. Heute ist Deutschland mit über 50 Zementwerken der größte Produzent Europas. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_3) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#6c7484;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kalkstein](#cargo_LIME) | [Zement](#cargo_CMNT) |
| [Sand](#cargo_SAND) |  |


<a name="industry_264"></a>
### Ziegelei

<img src="brick_works.png" alt="Ziegelei">

Die effiziente Massenproduktion von Ziegeln begann im 19. Jahrhundert im Rahmen der industriellen Revolution. Viele neue Industriegebäude mussten gebaut werden, und die neuen Eisenbahnstrecken erforderten große Brücken. 

Ziegel wurden schon seit dem Altertum produziert, üblicherweise wurde Holz verfeuert um die notwendige Hitze zu erzeugen. Im Set wird eine modernere Variante des Ziegelei dargestellt, die Kohle statt Holz benutzt. 

Diese Industrie benötigt Extension: [Bauindustrie](#extension_3) 

Industry ist erst ab 1800 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#cc8060;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Kohle](#cargo_COAL) | [Ziegel](#cargo_BDMT) |


<a name="industry_265"></a>
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


<a name="industry_266"></a>
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


<a name="industry_267"></a>
### Ölraffinerie

<img src="oil_refinery.png" alt="Ölraffinerie">

Ölraffinerien spalten Erdöl in verschiedene Bestandteile auf, die wiederum Grundstoffe für die gesamte chemische Industrie darstellen. So erhält man neben diversen Treibstoffen auch diverse Schmierstoffe, Flüssiggase und Heizöl. Darüber hinaus wird das Erdöl auch entschwefelt und von sonstigen Verunreinigungen befreit. In echten Raffinerien sind weitere Produktions- und Veredelungsschritte nachgeschaltet, so dass eine Raffinerie eine ganze Reihe von Produktion erzeugen kann. Im Set sind diese Schritte in eigene Industrien (Dampfreformierer und Steamcracker) ausgelagert, so dass der Spieler selbst die Kontrolle darüber hat, wie viel Treibstoff, Wasserstoff und Ethylen er erzeugen will. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_11) 

Diese Industrie ist nicht aktiv wenn folgende Erweiterungen aktiv sind: [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcfc00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Öl](#cargo_OIL_) | [Treibstoff](#cargo_PETR) |
|  | [Naphtha](#cargo_RFPR) |


<a name="industry_268"></a>
### Ölraffinerie

<img src="oil_refinery.png" alt="Ölraffinerie">

Ölraffinerien spalten Erdöl in verschiedene Bestandteile auf, die wiederum Grundstoffe für die gesamte chemische Industrie darstellen. So erhält man neben diversen Treibstoffen auch diverse Schmierstoffe, Flüssiggase und Heizöl. Darüber hinaus wird das Erdöl auch entschwefelt und von sonstigen Verunreinigungen befreit. In echten Raffinerien sind weitere Produktions- und Veredelungsschritte nachgeschaltet, so dass eine Raffinerie eine ganze Reihe von Produktion erzeugen kann. Im Set sind diese Schritte in eigene Industrien (Dampfreformierer und Steamcracker) ausgelagert, so dass der Spieler selbst die Kontrolle darüber hat, wie viel Treibstoff, Wasserstoff und Ethylen er erzeugen will. 

Diese Industrie benötigt Extension: [Organische Chemie](#extension_11) [Koks und Schwefel](#extension_8) 

Industry ist erst ab 1860 verfügbar.
Diese Beschränkung betrifft auch das Finanzieren der Industrie.

Farbe in der Übersichtskarte:<span style="background-color:#fcfc00;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span>

| Benötigt | Produziert |
| -- | -- |
| [Öl](#cargo_OIL_) | [Treibstoff](#cargo_PETR) |
|  | [Naphtha](#cargo_RFPR) |
|  | [Schwefel](#cargo_SULP) |


