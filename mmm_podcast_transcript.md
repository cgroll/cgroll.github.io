---
layout: page
title: "Automatisierte Geldanlage"
permalink: /2022/01/Automation_asset_management/mmm_german_podcast_transcript.html
---

<p>0:00:09 - 0:00:30: Tobias
</p>
<br>

<p> Guten Tag, ich begrüße Sie wieder ganz herzlich zum Scalable
Capital Podcast. Ich bin Tobias Aigner und ich möchte Sie heute gerne
mitnehmen in die Welt der künstlichen Intelligenz und des sogenannten
Machine Learning. Konkret wollen wir darüber sprechen, wie viel
Automatisierung die Geldanlage eigentlich verträgt und ob zum Beispiel
der Anlagealgorithmus von Scalable seine Investmentregeln selbst
lernt. Unser Experte für dieses Thema ist Christian Groll, der Head of
Quantitative Investment Strategy von Scalable und der sitzt heute hier
bei mir. Hallo Christian, schön, dass du da bist.

</p>
<br>

<p>0:00:30 - 0:00:31: Christian
</p>
<br>

<p>
Hi. 
</p>
<br>

<p>0:00:31 - 0:00:50: Tobias
</p>
<br>

<p>
Christian, vielleicht erzählst du erst mal kurz ein bisschen was über dich
selbst. Wie bist du denn zu Scalable gekommen und was machst du hier
genau? 

</p>
<br>
<p>0:00:50 - 0:01:56: Christian
</p>
<br>

<p> Ja, sehr gerne. Also studiert habe ich Wirtschaftsmathematik in
München, danach habe ich in Statistik promoviert am Lehrstuhl von
Professor Stefan Mittnik, der ja eben einer der Gründer von Scalable
Capital ist. Als ich dann eben durch Stefan gesehen habe, dass mit
Scalable Capital eine Möglichkeit besteht, mein akademisches Wissen
auch in der Praxis zur Anwendung zu bringen, habe ich 2015 bei
Scalable angeheuert. Mit Stefan waren wir hier schon immer sehr
akademisch aufgestellt und Forschung und quantitative Modellierung
sind hier im Prinzip ebenso Teil des Alltags wie damals an der
Universität. Die Motivation und im Prinzip auch eben unsere
Hauptaufgabe ist, das Ziel, den Finanzmarkt möglichst gut zu verstehen
und zu modellieren. Und da sind wir glaube ich von der Motivation auch
nicht weit von der Uni weg. Darüber hinaus sehe ich aber auch Teil
unserer Aufgabe, möglichst transparent nach außen zu sein. Wir haben
ja auch einen Quant Blog, wo wir nach und nach Komponenten des
Algorithmus beschreiben und für die Modellierung relevante
Finanzmarkthemen aufarbeiten.


</p>
<br>
<p>0:01:58 - 0:02:04: Tobias
</p>
<br>

<p> Steigen wir mal ins Thema ein. Wie würdest du denn das
Anlagemodell von Scalable Capital beschreiben?


</p>
<br>
<p>0:02:05 - 0:02:38: Christian
</p>
<br>

<p> Ja, ich würde sagen, die wichtigsten Säulen des Modells sind ein
global und über mehrere Anlageklassen, diversifiziertes
Anlageuniversum mit geringen Produktkosten, wir benutzen daher ETFs,
ein automatisiertes und regelbasiertes und dynamisches
Risikomanagement, eine individuelle Portfolioüberwachung und Anpassung
und wichtig auch, ja ich würde sagen, die feste Überzeugung, dass
jegliche Anlageentscheidungen auf möglichst soliden empirischen Daten
basieren sollten.


</p>
<br>
<p>0:02:38 - 0:02:46: Tobias
</p>
<br>

<p> Und wenn du jetzt sagst automatisiert, bedeutet das dann, dass der
Computer die Entscheidungen wirklich selbst trifft? Kann man das so
sagen? 


</p>
<br>
<p>0:02:46 - 0:05:40: Christian
</p>
<br>

<p> Ja, da muss ich glaube ich erst mal etwas weiter ausholen.
Automatisierung ist ja nicht gleich Automatisierung. Da gibt es schon
extreme Unterschiede, was sich hinter dem Begriff alles verbergen
kann. In den Medien ist ja immer recht pauschal irgendwie gleich von
künstlicher Intelligenz und maschinellem Lernen die Rede, obwohl
eigentlich niemals jemals irgendwer sauber definiert, was man darunter
zu verstehen hat. Insbesondere glaube ich eben, ist es sehr wichtig zu
verstehen, wie hoch der Grad des menschlichen Einflusses bei einer
automatisierten Allokationsentscheidung ist. Also ich versuche es mal
anhand von dem Beispiel zu skizzieren, das ich neuerlich in einem
didaktisch wirklich tollen Artikel von AQR, das ein US Hedge Fund
gelesen habe. Und zwar ist da die Idee, also man will einen
Algorithmus implementieren, der zu einem gegebenen Textinput, also
eine Zeichenkette bestehend aus Buchstaben, Ziffern und Sonderzeichen
selbst entscheidet, ob es sich dabei um eine valide E-Mail-Adresse
handelt oder nicht. So die erste Variante ist, ich schaue einfach
selber alle festgelegten Regeln für E-Mail-Adressen nach und übergebe
sie dann schon fertig dem Computer. Also ich kann beispielsweise
definieren, dass eine valide E-Mail-Adresse immer ein "@" Zeichen
haben muss, keine Leerzeichen haben darf und nicht mehr als 253
Zeichen haben darf. Das Regelwerk kann ich jetzt dem Computer einfach
als eine Abfolge von Wenn-Dann-Checks übergeben. Also im Prinzip
testet er dann quasi jede von mir definierte Anforderung und schaut
halt, ob sie erfüllt ist oder nicht. Und wenn auch nur eine
Anforderung nicht erfüllt ist, würde dann die vorliegende Zeichenkette
als nicht valide E-Mail-Adresse klassifiziert werden. Der Computer hat
jetzt also keinerlei Entscheidungsfreiheit im Prinzip, also er
exekutiert einfach nur stur die von mir vorgegebenen Regeln. Aber
nichtsdestotrotz habe ich am Ende des Tages natürlich einen
Algorithmus gebaut, der voll automatisiert für mich arbeitet. Zu
gegebenen Inputs werden die von mir vorgegebenen Regeln angewandt und
der entsprechende Output produziert. So und auf dem anderen Ende des
Spektrums gab es jetzt eine völlig andere Herangehensweise. Und zwar
gebe ich dem Computer keine Regeln mehr vor, sondern gebe mir im
Endeffekt einfach nur eine umfassende Sammlung an
Input-Output-Kombinationen vor. Also in unserem Beispiel bedeutet das
jetzt, ja sagen wir mal, wir übergeben dem Computer fünf Millionen
Input- Zeichenketten, für die wir jeweils schon klassifiziert haben,
ob es eine valide E-Mail-Adresse ist oder nicht. So basierend auf dem
Beispiel-Datensatz sucht sich der Computer dann eben die Regeln
selbst, mit denen er zukünftige E-Mail-Adressen klassifizieren wird.
Also statt dem fachspezifischen Expertenwissen bzw. den Annahmen, die
wir selbst in ein Regelwerk übersetzen müssen, brauchen wir als
Voraussetzung im Prinzip einfach nur noch diese Sammlung an schon
ausgewerteten Beispieldaten. "Nur" aber in Anführungszeichen, was
nämlich überhaupt keine Selbstverständlichkeit ist, dass derlei Daten
schon verfügbar sind. Irgendwer muss ja die fünf Millionen
Test-Zeichenketten schon klassifiziert haben, ob es jeweils eine
valide E-Mail-Adresse ist oder nicht.


</p>
<br>
<p>0:05:41 - 0:05:47: Tobias
</p>
<br>

<p> So beide Varianten skizziert. Die spannende Frage ist jetzt
natürlich, welche ist denn die bessere oder welche sollte man
bevorzugen? 


</p>
<br>
<p>0:05:48 - 0:07:57: Christian
</p>
<br>

<p> Ja, bevor wir uns das überlegen, lassen wir uns erstmal noch mal
kurz über die potenziellen Schwachstellen der beiden Ansätze sprechen.
Klar, in der traditionellen Herangehensweise sind wir natürlich
hochgradig davon abhängig, ob die vom Experten vorgegebenen Regeln
auch wirklich stimmen. Das ist natürlich relativ eindeutig. Beim
zweiten Ansatz kann man ja in gewisser Weise von künstlicher
Intelligenz sprechen und die Probleme mit den gefundenen Regeln sind
da schon immer so ein bisschen schwieriger aufzudecken. Ich nenne mal
vielleicht ein paar Beispiele, was da schiefgehen könnte. Erstens, ja,
nehmen wir an, der Computer sieht sich auf einmal mit einem Input
konfrontiert, der im bisherigen Beispiel Datensatz noch nicht
aufgetreten ist. Also in unserem Beispiel jetzt kommt auf einmal das
erste Mal eine Testadresse mit einem Leerzeichen daher. Wenn jetzt so
ein derartiger Input bisher nicht in den Daten vorkam, muss der
Computer also letztlich ohne irgendeinen Orientierungspunkt
entscheiden, was hier die beste Regel ist. Er muss also extrapolieren
und eine Regel über die bestehende Menge an beobachteten Inputs hinaus
anwenden. Zweitens, und das ist natürlich generell ein Problem der
Statistik, bestehende Zusammenhänge können sich immer ändern.
Historische Daten könnten eventuell nicht mehr aussagekräftig für die
Gegenwart sein. Früher zum Beispiel mussten E-Mail-Adressen ja immer
auf Domains enden wie .com oder .de etc. Mittlerweile sind da die
Restriktionen ja geringer. Also meine Arbeits-E-Mail endet
beispielsweise auf @scalable.capital. Wenn es jetzt im Beispiel
Datensatz noch nicht abgebildet war, dann arbeitet der Computer
natürlich mit veralterten Regeln. Und ja, drittens, die vom Computer
gefundenen Regeln sind für den Menschen eben oftmals extrem
intransparent und schwer nachzuvollziehen. Also was genau den Computer
letztlich dazu bewogen hat, eine E-Mail als Invalide zu
klassifizieren, ist meistens unklar. Dadurch kann es dann durchaus
passieren, dass eine E-Mail zwar richtig klassifiziert wurde, aber
eigentlich nur zufällig durch Anwenden einer eigentlich falschen
Regel. Sowas mag anfangs eben extrem schwer auffallen, weil die
Klassifikation auf den Beispiel Datensatz war korrekt. Aber bei der
Anwendung dann auf neue Daten merkt man dann irgendwann recht schnell,
dass im Hintergrund wohl falsche Regeln erlernt wurden. 


</p>
<br>
<p>0:07:58 - 0:08:07: Tobias
</p>
<br>

<p> Im Endeffekt heißt es doch, welche Herangehensweise besser ist,
entscheidet sich daran, ob man den Regeln des Computers oder des
Experten mehr vertraut, oder? 


</p>
<br>
<p>0:08:07 - 0:09:55: Christian
</p>
<br>

<p> Ja, so könnte man es im Allgemeinen durchaus formulieren oder
jetzt speziell nur auf die Regeln des Computers übersetzt. Die
Vertrauenswürdigkeit ergibt sich letztendlich daraus, wie umfassend
und repräsentativ der Beispiel Datensatz ist und eben inwieweit
ausgeschlossen werden kann, dass der Computer nicht versehentlich
Muster in den Daten aufgreift, die eigentlich gar nicht existieren.
Der statistische Fachbegriff hierfür ist das sogenannte Overfitting.
Eine meiner Lieblingsanekdoten zur Veranschaulichung der Problematik
hat ich neulich ja auch schon in einem deiner Texte gelesen. Also für
eine Anwendung sollten in digitalen Bildern automatisiert vom Computer
Panzer erkannt werden. Die Grundidee war also, dass man irgendwie mit
künstlicher Intelligenz einen Algorithmus erstellt, der selber
erkennt, ob in dem vorgegebenen Bild ein Panzer beinhaltet ist oder
nicht. So, dafür wurde dann eben der Computer mit Beispiel Daten
gefüttert, damit er sich ein Regelwerk erlernen kann und auf dem
Beispiel Datensatz selbst hat es auch überragend funktioniert. Als der
Algorithmus dann aber in der Realität eingesetzt wurde, ist es im
Prinzip eben kläglich gescheitert. Und der Grund dafür war, dass der
Computer in Wirklichkeit gar nicht gelernt hatte, einen Panzer zu
erkennen, sondern im Beispiel Datensatz waren einfach nur alle
Panzerbilder im Sonnenschein aufgenommen worden. Und was der Computer
also eigentlich erkannt hatte, war einfach nur der Sonnenschein in den
Bildern. Er hat also im Prinzip dann jedes Sonnenscheinbild als
Panzerbild identifiziert, weil er ein völlig falsches Regelwerk gebaut
hatte, das auf dem Beispiel Daten aber zufällig trotzdem funktioniert
hatte. Aber out of sample, also außerhalb des bekannten Beispiel
Datensatzes, hat es eben nicht mehr funktioniert. Und die Vermeidung
von Overfitting, also dieses Vermeiden von fälschlicherweise
aufgegriffenen Mustern in den Daten, das ist sicherlich eine der
größten Herausforderungen bei der Anwendung künstlicher Intelligenz. 


</p>
<br>
<p>0:09:55 - 0:10:02: Tobias
</p>
<br>

<p> Kommen wir mal zum Algorithmus von scalable. Inwieweit spielt denn
da jetzt künstliche Intelligenz wirklich eine Rolle? 


</p>
<br>
<p>0:10:02 - 0:11:22: Christian
</p>
<br>

<p> Ja, bislang hatten wir uns ja nur mit eher extremen Beispielen von
Algorithmen beschäftigt, um hoffentlich einigermaßen verständlich zu
machen, wie unterschiedlich eben die Herangehensweise an
Automatisierung sein können und was man sich ungefähr unter
künstlicher Intelligenz vorstellen kann. In der Realität gibt es aber
natürlich keinerlei Grund, sich da irgendwie so einem extremen
Schwarz-Weiß-Denken zu unterwerfen. Also wieso sollte man nicht
einfach versuchen, das Beste aus beiden Welten zu vereinen? Nochmal
aufs Beispiel der E-Mail-Adressen jetzt vielleicht bezogen. Selbst
wenn ich mir als Experte nicht sicher bin, welche Sonderzeichen
tatsächlich erlaubt sind, kann ich mir Algorithmus ja schon mal mit
auf den Weg geben, dass er ein besonderes Augenmerk drauflegen soll,
um dann am Ende halt ein passendes Regelwerk zu erstellen. Oder ich
kann auch einfach festlegen, ein @-Symbol ist zwingend erforderlich
und es gibt irgendeine Maximumlänge an zugelassenen Zeichen und so
weiter. Mit den Hilfestellungen kann der selbstlernende Teil des
Algorithmus dann die bestehenden Beispieldaten gleich deutlich
effizienter nutzen, was im Endeffekt einfach die Gefahr potenzieller
falscher Interpretation schon mal wesentlich reduziert. Also
übertragen auf die Finanzwelt würde es dann beispielsweise bedeuten,
dass ich dem Algorithmus gleich mit auf den Weg gebe, wie er am besten
Risiko berechnen soll. Man könnte ihn dann aber immer noch erlernen
lassen, wie er mit dieser Information am besten umgeht. 


</p>
<br>
<p>0:11:23 - 0:11:53: Tobias
</p>
<br>

<p> Jetzt ist das dynamische Risikomanagement von Scalable ja darauf
ausgerichtet, das Risiko im Portfolio zu ermitteln und dann daraus
Handlungsentscheidungen abzuleiten. Also zum Beispiel, ob man die
Aktienquote reduzieren soll oder Rohstoffe aufstocken oder Anleihen
aufstocken, was auch immer. So soll ja die Risikovorgabe des Kunden
stets eingehalten werden. Das ist die Idee dahinter. Ist es denn jetzt
tatsächlich so, dass ich mir dieses Risikomanagement so vorstellen
muss, dass es einen Teil der Regeln von euch bekommt und den anderen
Teil sich selbst austüffelt? Kann man das so sagen? 

</p>
<br>
<p>0:11:53 - 0:15:14: Christian
</p>
<br>

<p> Ja, auch hier würde ich wieder sagen, es gibt sehr viele
unterschiedliche Abstufungen, wie viel Spielraum ich dem Computer
selbst überlassen könnte, auf ein berechnetes Risikolevel zu
reagieren. Und ich würde eben sagen, aus vielerlei Gründen haben wir
da die Daumenschrauben schon eher eng angezogen. Der Algorithmus kann
sich da sicherlich nicht einfach seine komplett eigenen Regeln
erstellen. Aber ein gewisses Maß an Freiheit sollte man
sinnvollerweise schon zulassen, um zu gewährleisten, dass das
Anlagemodell auch im Einklang des historischen Finanzmarktdaten ist.
Kleines Beispiel vielleicht dazu, was ich meine, also nehmen wir
einfach mal an, wir sind der Überzeugung, dass ein Anstieg von
Finanzmarktrisiken generell ein eher unerwünschtes Phänomen ist, auf
das wir mit einer bestimmten Art und Weise mit Umschichtung reagieren
wollen. Also sagen wir der Einfachheit halber, die erwünschte Reaktion
wäre, den Anteil risikoreicher Wertpapiere im Portfolio zu verringern
und den Anteil risikoarmer Wertpapiere zu erhöhen. Das ist zwar
festgelegt, in welcher Art und Weise ich reagieren will, aber eben
noch nicht wie stark. Also mit anderen Worten, für eine gegebene
Steigerung des Risikos könnte ich jetzt immer noch entweder nur eher
leicht umschichten oder gleich komplett alle risikoreichen Wertpapiere
verkaufen. Welche Reaktion optimal ist, hängt davon ab, wie nachhaltig
der Anstieg des Risikos ist. Und um hier eben das richtige Maß zu
finden, macht es durchaus Sinn, den Computer mit Hilfe historischer
Daten erlernen zu lassen, welches Maß an Reaktion sich in der
Vergangenheit als sinnvoll erwiesen hatte. Nur würde ich meinem Gefühl
nach hier jetzt normalerweise nicht von maschinellem Lernen sprechen.
Im Prinzip wird hier einfach ganz klassisch ein statistisches Modell
mit Daten geschätzt. Der Begriff Lernen bedeutet letztendlich nicht
wirklich was anderes, wurde aber glaube ich einfach mal eingeführt, um
dem ganzen noch mal einen speziell extravaganten Touch zu geben.
Jedenfalls gibt es im Portfolio-Management, glaube ich, jede Menge
Möglichkeiten, ein ökonomisch motiviertes, vorgegebenes Regelwerk vom
Computer mit Hilfe historischer Daten noch mal verfeinern zu lassen,
um dann hoffentlich zu einer optimalen Anlageentscheidung zu kommen.
Das ist ja quasi schon jeher auch der Gedanke der Ökonomie bzw. der
Finanzökonomie, einfach die Symbiose von ökonomischer Theorie mit
empirischer Modellierung. Und ein weiteres Beispiel, wo man dem
Computer durchaus Spielraum zugestehen würde, sind sowas wie
Zielkonflikte, die man lösen muss. Also im Allgemeinen bevorzugt der
Investor, sage ich mal, hohe Renditen, wenig Risiko und geringe
Transaktionskosten. Ein Zielkonflikt besteht dann, wenn eine
Verbesserung in einer der drei Zielgrößen immer auch automatisch eine
Verschlechterung in mindestens einer der anderen Zielgrößen nach sich
zieht. Also mehr Rendite lässt sich im Allgemeinen ja nur mit mehr
Risiko erwirtschaften bzw. anders gesagt dann wieder, wenn ich jeden
Tag ein bezüglich Rendite und Risiko optimal aufgestelltes Portfolio
haben wollen würde, dann müsste ich fortlaufend Transaktionen machen,
was wiederum im Prinzip dann die Kosten in die Höhe springen lässt.
Also auch in solchen Fällen kann der Computer dann helfen, den
sozusagen ja Sweet Spot, also den optimalen Punkt im Zielkonflikt zu
bestimmen. Ich denke aber insgesamt schon, dass man gerade in der
Finanzwelt extrem vorsichtig sein sollte, wo man bzw. wie viel
Spielraum man dem Computer überlässt, seine eigenen Regeln festzulegen.


</p>
<br>
<p>0:15:14 - 0:15:22: Tobias
</p>
<br>

<p> Du sagst gerade in der Finanzwelt, was meinst du damit, inwiefern
unterscheidet sich denn die Finanzwelt von anderen Bereichen?


</p>
<br>
<p>0:15:22 - 0:18:58: Christian
</p>
<br>

<p> Ich würde sagen, naja, das Signal-to-Noise-Ratio, also das
Verhältnis von relevanten Mustern in den Daten zu einfachen,
zufälligen und letztlich für die weitere Modellierung bedeutungslosen
Mustern ist extrem gering bei Finanzdaten. Nehmen wir mal irgendwie
zum Vergleich die Vorhersage von Fußballergebnissen. Angenommen jetzt,
wir betrachten ein KO-Spiel von zwei x-beliebigen Mannschaften, dann
gibt es ja nur zwei mögliche Outcomes. Entweder kommt Team A weiter
oder Team B. Wenn ich jetzt absolut nichts über beide Teams weiß, dann
ist mein bester Tipp letztlich, naja, dass die Wahrscheinlichkeit für
beide Teams weiterzukommen 50-50 ist. Wir können also im Prinzip
nichts anderes machen als zu raten. Wenn ich jetzt aber weiß, dass
Team A die doch recht erfolgreiche deutsche Nationalmannschaft ist und
Team B ist ein absoluter Underdog, dann könnte quasi jeder mit nur
bisschen Fußballkenntnis vorhersagen, dass vermutlich die deutsche
Nationalmannschaft weiterkommt. Klar, damit hat man selbstverständlich
auch nicht immer recht, aber sagen wir mal, in acht aus zehn Fällen
liegen wir schon mal richtig. Weil der strukturelle
Qualitätsunterschied zwischen den beiden Teams einfach so deutlich
ist, dass er den Zufall, der im Spiel ja durchaus auch besteht,
überlagert. Also in Spielen mit relativ unausgeglichenen Gegnern ist
es, glaube ich, recht einfach eine Vorhersage zu machen, die deutlich
besser klappt als 50-50. Wenn man jetzt aber zum Vergleich den
Aktienmarkt anschaut, also selbst über Jahrzehnte hinweg erfolgreiche
systematische Strategien haben an einem beliebig ausgewählten Tag eine
Wahrscheinlichkeit für eine positive Rendite von minimal über 50
Prozent. Die Vorhersagekraft liegt also nahezu bei der Präzision eines
Münzwurfs und da macht sich ein Wissensvorsprung, macht sich erst über
richtig lange Zeit bemerkbar. Ja, dann ist die Frage eben, wieso ist
das so? Ich denke, der springende Punkt beim Finanzmarkt ist, dass er
ein adaptives System ist, bei dem die Entwicklung von Preisen, von den
Vorhersagen und auch Ansichten der einzelnen Marktteilnehmer
beeinflusst wird. Also wenn ich einen Wissensvorsprung am Finanzmarkt
habe, dann bedeutet das ja immer auch, dass sich eine Chance auf eine
gewinnbringende Investition ergibt. Und wenn man jetzt davon ausgeht,
dass Marktteilnehmer generell Profit maximieren, denken und handeln,
dann wäre sie natürlich immer auch ein Anreiz haben zu versuchen,
diesen Wissensvorsprung auch in Geld zu verwandeln. So, und jetzt sind
aber Marktpreise letztendlich ja auch nur das Resultat von Angebot und
Nachfrage. Wenn sich jetzt also ausgelöst durch einen gewissen
Wissensvorsprung die Nachfrage nach einem Wertpapier steigert, wird
automatisch auch der Marktpreis verändert. Und zwar so lange, bis mit
dem ursprünglichen Wissensvorsprung am Ende nichts
mehr zu holen ist. Das zumindest besagt die Hypothese vom effizienten
Finanzmarkt, für die der amerikanische Ökonom Eugene Fama auch den
Nobelpreis erhielt. Durch Profitmaximierung und eben das
Zusammenspiegel von Angebot und Nachfrage haben Vorhersagen also
letztendlich einen direkten Einfluss auf die Marktpreise selbst, also
auf die Größe, die man ja eigentlich vorhersagen wollte. Das ist ein
fundamentaler Unterschied zu anderen Wissenschaftsfeldern und
insbesondere auch bei maschinellem Lernen ein Problem. Ich habe da
neulich eine ganz lustige Anekdote von auch wieder von AQR dazu
gehört, die die Vorhersage am Finanzmarkt verglichen haben mit der
Erkennung von Katzen auf Fotos. Die Aussage war da ungefähr, ja,
Katzen fangen nicht an sich in Hunde zu verwandeln, sobald der
Algorithmus zu gut darin wird, Katzen zu erkennen. Deshalb spielt
maschinelles Lernen und künstliche Intelligenz in der Bilderkennung
eben eine größere Rolle als im adaptiven Finanzmarkt.


</p>
<br>
<p>0:18:58 - 0:19:07: Tobias
</p>
<br>

<p> Okay, aber unterm Strich heißt es doch dann, in der Finanzwelt
sollte man einfach viel stärker auf vorgegebene Regeln setzen und dem
Computer nicht zu viel Spielraum lassen.


</p>
<br>
<p>0:19:07 - 0:20:46: Christian
</p>
<br>

<p> Ja, ich denke schon, dass empirische Untersuchungen derzeit noch
eher darauf hindeuten, dass weniger Spielraum für den Computer
durchaus empfehlenswert ist. Also das Risiko, andernfalls eventuell
falschen Mustern in den Daten aufzusitzen, ist einfach enorm hoch und
würde der Anlageentscheidung sonst eine zusätzliche und unnötig
gefährliche Komponente hinzufügen. Die Anforderungen an ein gutes
Regelwerk sollten sein, dass es sich bezüglich mehrerer Dimensionen
als robust erweisen sollte. Was meine ich damit? Erstens, ja, es
sollte beständig sein. Also über einen längeren Zeitraum und
idealerweise über verschiedene Anlageuniversen hinweg sollten
nachweisbar positive Ergebnisse erzielt worden sein. Es sollte robust
sein. Also wenn ich jetzt irgendwelche leichten Änderungen an den
Parametern mache, dann sollte das Ganze sich stabil verhalten. Also
wenn ich jetzt beispielsweise das Modell zur Bestimmung von Risiken
nur marginal verändere, sollten natürlich nicht fundamental
unterschiedliche Anlageentscheidungen herauskommen. Und drittens, es
sollte plausibel sein. Also im Großen und Ganzen im Einklang mit
bestehender ökonomischer Theorie sein. Und mit so manchem Algorithmus,
wie er halt in der künstlichen Intelligenz besteht, erhält man am Ende
normalerweise eher eine sogenannte Black Box. Also im Prinzip ein
Regelwerk, das zwar Entscheidungen trifft, aber ohne große Einblicke
zu geben, wie diese Entscheidungen zustande kommen. Und
dementsprechend lassen sich die vom Computer gewählten Regeln auch
nicht unmittelbar in für Menschen verständliche und interpretierbare
Regeln übersetzen. Das schließt natürlich automatisch dann schon
bisschen den Abgleich mit bestehender ökonomischer Theorie aus.


</p>
<br>
<p>0:20:47 - 0:21:14: Tobias
</p>
<br>

<p> Jetzt haben wir ja eine Menge gesprochen über neuartige
Algorithmen. Was mich jetzt auch noch interessiert, was bekannt ist,
sind ja zum Beispiel neuartige Datenquellen. Also zum Beispiel
Satellitenbildern von Parkplätzen vor Supermärkten, die eingesetzt
werden, um Entscheidungen zu treffen oder Informationen
zusammenzustellen. Social Media Comments, Smartphone Geolocation
Daten, um das Konsumentenverhalten herauszubekommen.
Internet-Suchmaschiendaten, diese ganzen Sachen. Was hältst du davon?


</p>
<br>
<p>0:21:14 - 0:21:46: Christian
</p>
<br>

<p> Ja, die Frage passt hier hervorragend. Da kann ich nämlich gleich
nochmal ungefähr das Gleiche antworten. Auch hier wäre nämlich immer
mein erster Hinweis, ja, festgelegte Regeln sollten beständig sein,
also über einen längeren Zeitraum überprüfbar sein. So, jetzt nehmen
wir an, ich nutze neuartige Datenquellen, um daraus irgendwelche
Anlageentscheidungen abzuleiten. Egal, ob die Regeln von Fachexperten
kommen oder vom Computer. Wenn ich die dafür nötigen Datenquellen nur
über einen sehr begrenzten Zeitraum in die Vergangenheit zurück habe,
dann lassen sich die Regeln und der daraus resultierende Nutzen
natürlich nur sehr bedingt empirisch überprüfen.


</p>
<br>
<p>0:21:47 - 0:21:49: Tobias
</p>
<br>
<p> Warum ist das so gefährlich oder wozu führt das? 


</p>
<br>
<p>0:21:50 - 0:23:52: Christian
</p>
<br>

<p> Naja, das volle Risikoprofil einer Anlagestrategie kann man nunmal
erst erahnen, wenn man sie mindestens über einen vollen
Wirtschaftszyklus hinweg beobachtet hat. Selbst nach einem solchen
vollen Wirtschaftszyklus oder sogar mehreren ist es auch möglich, dass
man von gewissen extremen Ereignissen auch immer noch keine
Beobachtung hat, weil die eventuell nur einmal in 100 Jahren oder so
was auftreten. Im Idealfall hat man also möglichst lange
Beobachtungszeiträume und nach Möglichkeit auch Beobachtungen aus
mehreren unterschiedlichen Rahmenbedingungen von globaler Wirtschaft
und Finanzmarkt. Erst dann lässt sich auch mit hinreichender
Überzeugung sagen, dass ein Regelwerk auf lange Sicht auch wirklich
einen positiven Mehrwert erzeugen wird. Die klassische Metapher
hierfür ist die Zeitreihe eines Truthans vor Thanksgiving. In den
Monaten vor Thanksgiving bekommt er immer ausreichend zu essen. Wer
basierend auf den Erfahrungen aber jetzt extrapoliert, dass der
Truthan auch nach Thanksgiving noch bester Gesundheit und wohl genährt
ist, der würde natürlich kaum stärker daneben liegen können. Man
braucht schon Daten von allen Umweltzuständen, also sowohl der Zeit
des Mästens als auch der Zeit der Schlachtung, um sich über das
Risikoprofil im Klaren zu sein. Ist eine sehr kurze Historie bei
diesen innovativen Datenquellen jetzt ein Ausschlusskriterium? Nein,
das selbstverständlich nicht. Und auch wir halten da den Trend zu
immer mehr verfügbaren und unterschiedlichen Datenquellen für
vielversprechend. Aber man muss glaube ich schon aufpassen, dass
gewisse innovative Datenquellen, so was wie Social Media Beiträge,
Smartphone, Geo Locations oder so etwas, ja eben eigentlich erst seit
wenigen Jahren zur Verfügung stehen. Und da muss man halt einfach
immer im Hinterkopf behalten. In der Zeit hatten wir einfach keine
großen Verwerfungen an den Aktienmärkten und wir hatten auch ein, sag
ich mal, äußerst außergewöhnliches Zinsumfeld seitdem. Also der
vermeintliche Nutzen von den innovativen Datenquellen lässt sich
bisher also nicht ohne weiteres auch auf andere Finanzmarktumfelder
gleich übertragen.


</p>
<br>
<p>0:23:52 - 0:24:03: Tobias
</p>
<br>

<p> Kommen wir am Schluss nach den
ganzen Algorithmen nochmal zum Thema Mensch, nämlich zum
Portfolio-Manager beim Investieren. Was macht für dich einen guten
Portfolio-Manager aus?


</p>
<br>
<p>0:24:04 - 0:25:24: Christian
</p>
<br>

<p> Bescheidenheit und die Ehrlichkeit sich selbst gegenüber
vergangene Entscheidungen schonungslos zu analysieren. Also jede
erfolgreiche Investmentstrategie benötigt meiner Meinung nach zwei
Dinge. Erstens eine gute Einschätzung der Marktlage und zweitens man
muss aber auch die richtigen Schlüsse daraus ziehen. Und
Overconfidence, also zu deutsch Selbstüberschätzung, ist ein massives
Risiko für den Anlageerfolg. Kleines Beispiel nehmen wir an jemand
kann einen Münzwurf mit 55 Prozent Wahrscheinlichkeit richtig
prognostizieren. Das ist eine überragende Fähigkeit letztlich, kann
kein Menschen, keine Person der Welt. Wenn die Person jetzt aber
denkt, er läge statt in 55 Prozent der Fälle in 100 Prozent der Fälle
richtig, also wenn er sich quasi selbst überschätzen würde, dann wäre
er halt geneigt dazu, dass er nahezu all sein Geld auf einen einzigen
Münzwurf setzt. Er denkt ja, dass er mit 100 Prozent
Wahrscheinlichkeit das Richtige trifft. In Wirklichkeit wäre er dann
aber mit 45 Prozent Wahrscheinlichkeit Bankrott. Und ja, unter anderem
deshalb bin ich halt eben großer Fan von quantitativen regelgebundenen
Investmentstrategien. Zahlen lügen nicht und die Wahrscheinlichkeit
von Fehleinschätzungen bekommt man bei der Überprüfung von dem
bestehenden Regelwerk mit historischen Daten quasi schwarz auf weiß.
Das ist meiner Meinung nach das beste Mittel gegen
Selbstüberschätzung.



</p>
<br>
<p>0:25:24 - 0:25:37: Tobias
</p>
<br>

<p> Sehr interessant, da sage ich doch in aller
Bescheidenheit, vielen Dank für das Gespräch, Christian.

</p>
<br>
<p>0:25:37 - 0:25:39: Christian
</p>
<br>

<p>
Danke auch.

</p>
<br>
<p>0:25:39 - 0:25:47: Tobias
</p>
<br>

<p>
Das war unsere Podcast Folge zum Thema Automatisierung in der
Geldanlage. Wenn Sie dazu noch weitere Informationen wünschen, finden
Sie die auf unserer Webseite oder Sie schicken uns eine Mail an
podcast@scalable.capital. Vielen Dank fürs Zuhören.


</p>
<br>
<p>0:25:52 - 0:26:18: Risk Disclaimer
</p>
<br>

<p> Scalable Capital Vermögensverwaltung GmbH, erbringt keine Anlage-,
Rechts- und oder Steuerberatung. Sollte dieser Podcast Informationen
über den Kapitalmarkt, Finanzinstrumente und oder sonstige für die
Vermögensanlage relevante Themen enthalten, so dienen diese
Informationen ausschließlich der Erläuterung der erbrachten
Dienstleistungen. Die Kapitalanlage ist mit Risiken verbunden. Bitte
beachten Sie hierzu die Hinweise auf unsere Internetseite.


</p>
<br>