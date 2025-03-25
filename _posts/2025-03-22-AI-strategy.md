---
layout: post
title:  "Künstliche Intelligenz mit Plan: So gelingt die Umsetzung im Unternehmen"
date:   2025-03-22
categories: [AI]
excerpt: > #
  Was Unternehmen über KI wissen müssen – und wie sie Technologie, Menschen und Prozesse zusammenbringen, um echte Wirkung zu erzielen.
math: false
---

Das Thema KI beschäftigt aktuell alle Unternehmen. Zum einen, weil es beeindruckende Fortschritte gibt, bspw. Fähigkeiten wie autonomes Fahren, leistungsstarke Sprachmodelle oder beeindruckende Bilderzeugung. Zum anderen, weil Studien existieren, die hohe Erwartungen schüren, weil erhebliche Produktivitätsgewinne durch KI prognostiziert werden. Auf der anderen Seite beschäftigt es aber auch Mitarbeiter, die beispielsweise Sorgen haben, dass KI bestehende Jobprofile verändern oder sogar ersetzen könnte.


## Definition und Grundlagen der Künstlichen Intelligenz

Als erstes: **Was ist Künstliche Intelligenz?** Die Definition des Europäischen Parlaments lautet: *Künstliche Intelligenz ist die Fähigkeit einer Maschine, menschliche Fähigkeiten wie logisches Denken, Lernen, Planen und Kreativität zu imitieren.*

<br>

Drei zentrale Faktoren bestimmen die Leistungsfähigkeit von KI:

- **Algorithmen** – die mathematischen Modelle, die das Lernen ermöglichen.
- **Daten** – die Erfahrungen, mit denen das Modell trainiert wird. Je besser und strukturierter die Daten, desto leistungsfähiger die KI. Aber auch die Daten, die bei der Inferenz genutzt werden.
- **Rechenleistung** – Hochleistungsprozessoren und GPUs sind notwendig, um Modelle effizient zu trainieren.

<br>

Ein fertiges KI-Modell entsteht, indem ein bestimmter Algorithmus oder eine Modellarchitektur mit geeigneten Daten trainiert wird. Dabei gilt: Selbst wenn der Algorithmus identisch ist, kann das resultierende Modell sehr unterschiedlich ausfallen – je nachdem, mit welchen Daten es trainiert wurde.

<br>

Wie sieht das Training eines KI-Modells aus? In der Regel erfolgt es im sogenannten Supervised Learning. Dabei werden dem Modell für gegebene Eingabedaten die erwarteten Ausgaben mitgegeben – zum Beispiel Bilder mit den zugehörigen Kategorien wie "Katze" oder "Hund" oder Audioaufnahmen mit dem entsprechenden Text. Die Parameter im Modell werden dann so angepasst, dass es möglichst zuverlässig die gewünschten Ausgaben liefert. Dabei ist es entscheidend zu verstehen, mit welchen Daten das Modell trainiert wurde: Ein Modell, das nur Katzen und Hunde gesehen hat, kann einen Eisbären nicht erkennen. Und ein Modell, das nur englische Sprache kennt, wird kein Chinesisch verstehen. Nur wer die Trainingsdaten kennt, kann auch realistisch einschätzen, wozu ein Modell fähig ist – und wozu nicht.

<br>

**Arten von KI-Algorithmen**

- **Traditionelles Machine Learning:** Diese Modelle arbeiten meist mit strukturierten Daten und erklärenden Variablen. Ein Beispiel ist die Vorhersage der Fußball-Weltmeisterschaftssieger, bei der relevante Einflussfaktoren gesucht und ihr Einfluss automatisch berechnet wird. Typische Einflussvariablen, mit deren Hilfe die Fähigkeiten von Teams bestimmt werden können, sind bspw die Anzahl an Champions-League-Spielern im Kader einer Mannschaft, die insgesamt gewonnenen Titel einer Mannschaft, die maximale Anzahl von Spielern aus dem gleichen Verein oder auch die Anzahl der Spieler, die in der Vorsaison im Champions-League-Halbfinale standen. Besonders wichtig sind aber auch Wettquoten, die oft als aggregierte Einschätzung vieler Experten betrachtet werden können. Der Algorithmus soll letztlich erkennen, welche Einflussgrößen überhaupt relevant sind, den Einfluss der einzelnen Variablen bestimmen und nutzen, um den Forecast zu verbessern.
- **Neuronale Netzwerke:** Inspiriert vom menschlichen Gehirn bestehen sie aus mehreren Schichten von Knotenpunkten, die Informationen verarbeiten. Jeder Knoten führt einfache mathematische Operationen durch und leitet das Ergebnis an die nächste Schicht weiter. Mit zunehmender Tiefe und Größe dieser Netzwerke steigt auch die Komplexität ihres Verhaltens. Ab einer gewissen Anzahl an Schichten spricht man von "Deep Learning". KI-Systeme, die solche tiefen neuronalen Netze mit Daten trainieren, bezeichnet man typischerweise als Deep-Learning-Modelle.
- **Generative KI:** Während traditionellere KI-Modelle vor allem strukturierte Outputs wie Zahlen (z. B. Umsatzprognosen oder Spielergebnisse) oder Klassifikationen (z. B. Hund oder Katze) liefern, erzeugt generative KI komplexe Inhalte wie Texte, Bilder oder Musik. Bekannte Beispiele sind Sprachmodelle wie ChatGPT oder Bildgeneratoren wie FLUX. Diese Modelle sind in der Regel sehr groß und werden daher als Unterkategorie des Deep Learning betrachtet. Aufgrund ihrer Größe zeigen sie teilweise sogenannte emergente Fähigkeiten, also überraschend komplexe Verhaltensweisen, die nicht explizit einprogrammiert wurden.

<br>

Werfen wir einen kurzen Blick auf die Entstehung von Sprachmodellen, um diese emergenten Fähigkeiten besser zu verstehen. Klassisches Supervised Learning ist hier schwer anwendbar. Wenn man etwa einem Modell einen Text vorgibt und eine Zusammenfassung erwartet, stellt sich die Frage: Wie misst man, ob die Zusammenfassung gut ist? Es gibt unzählige legitime Formulierungen, die alle korrekt sein könnten. Eine manuelle Bewertung jedes einzelnen Beispiels wäre unrealistisch und kaum skalierbar.

<br>

Ein Trick zur Schulung solcher Modelle besteht darin, künstlich einen Datensatz zu erzeugen: Aus vollständigen Sätzen wird jeweils ein Wort entfernt, und das Modell wird darauf trainiert, dieses fehlende Wort vorherzusagen. Mit der Zeit lernt die KI beispielsweise, dass in einem Satz wie "Das Lieblingseis der Deutschen ist ..." wahrscheinlicher "Erdbeere" oder "Pistazie" folgen sollte als "Haus" oder "Baum". Auf diese Weise entwickelt das Modell ein Sprachverständnis. Voraussetzung dafür ist allerdings ein sehr großer und vielfältiger Trainingsdatensatz.

<br>

Zusätzlich wird das Verhalten des Modells gezielt durch menschliches Feedback trainiert. Ohne dieses Training würde das Modell unter Umständen auf eine Frage einfach mit einer weiteren Frage antworten – schließlich wurde es ursprünglich nur darauf trainiert, Texte fortzusetzen. Wenn im Trainingsdatensatz beispielsweise häufig mehrere Fragen hintereinander vorkommen, etwa in Multiple-Choice-Tests, lernt das Modell, dass dies eine übliche Fortsetzung ist. Um dieses Verhalten zu steuern und realistischere Dialoge zu ermöglichen, kommt sogenanntes Reinforcement Learning mit menschlichem Feedback zum Einsatz. Erst dadurch wird aus einem reinen Sprachmodell ein echtes Chat- oder Instruktionsmodell.

<br>

Mit Reinforcement Learning lässt sich das Verhalten eines Modells gezielt beeinflussen – etwa dahingehend, dass es auf Fragen antwortet oder einen freundlichen, respektvollen Stil pflegt. Schwieriger ist es jedoch, einem Modell auf diesem Weg neues Faktenwissen oder zusätzliche fachliche Fähigkeiten beizubringen.

<br>

Erstaunlicherweise zeigen Deep-Learning-Modelle sogenannte "emergente" Fähigkeiten: Sie können verständliche Zusammenfassungen erstellen, Gedichte verfassen, Sprachen übersetzen, einfache Rechenaufgaben lösen und zum Teil logische Schlüsse ziehen. Diese Fähigkeiten wurden dem Modell nicht explizit beigebracht, sondern ergeben sich aus der Kombination von Datenmenge, Modellgröße und Trainingsverfahren. Dennoch ist Vorsicht geboten: Wenn bestimmte Fähigkeiten nicht gezielt trainiert wurden, sind sie oft unzuverlässig. Das zeigt sich in bekannten Schwächen, etwa bei komplexen Rechenaufgaben, logischen Tests oder scheinbar einfachen Zählaufgaben – wie der Frage, wie oft der Buchstabe "r" in "strawberry" vorkommt.

<br>

Wichtig ist also zu verstehen, welche Aufgaben sich für ein Sprachmodell wirklich eignen. Sollte ich einem solchen Modell unternehmerische Entscheidungen überlassen oder Aktienprognosen anvertrauen? Klare Antwort: Nein. Das sind keine Aufgaben, für die das Modell konzipiert oder trainiert wurde. Ein fundierter Einsatz setzt voraus, dass man die Stärken und Grenzen der Technologie kennt.

### Inferenz

Jetzt sind wir bei der Frage angekommen, wie KI-Modelle konkret genutzt werden können, um Aufgaben zu lösen. Sobald ein Modell trainiert wurde, kann es zur sogenannten Inferenz verwendet werden – das bedeutet, es wird ein Input übergeben und ein entsprechender Output erzeugt. Diese Art der Nutzung ist heute für zahlreiche Datentypen möglich, sowohl für den Input als auch für den Output:

- **Text-to-Speech**: Ein geschriebener Text wird in gesprochene Sprache umgewandelt (z. B. digitale Assistenten).
- **Speech-to-Text**: Gesprochene Sprache wird automatisch in Text umgewandelt (z. B. Transkriptionsdienste).
- **Text-to-Image**: Aus einem Textprompt wird ein Bild generiert (z. B. bei der Produktgestaltung oder im Marketing).
- **Image-to-Text**: Bilder werden beschrieben oder Inhalte ausgelesen (z. B. automatisierte Bildbeschriftung, OCR).
- **Numerische Daten zu Vorhersagen**: Aus Sensordaten oder Tabellenwerten werden Vorhersagen generiert (z. B. Energieverbrauch, Maschinenausfall).

Die Vielfalt dieser Inferenzmöglichkeiten zeigt, wie flexibel moderne KI-Modelle bereits einsetzbar sind.

### Daten

Doch so flexibel KI-Modelle heute einsetzbar sind – ihre Wirksamkeit hängt stark vom Zugang zu den richtigen Daten ab. Dabei muss man zwischen zwei Phasen unterscheiden: dem **Training** eines Modells und der **Inferenz**, also der Nutzung des Modells im Alltag.

<br>

Für das Training großer Sprachmodelle, wie GPT, werden enorme Datenmengen benötigt – Milliarden von Textbeispielen aus unterschiedlichsten Quellen. Diese Art des Trainings ist äußerst aufwändig und für einzelne Unternehmen kaum realistisch umzusetzen. Deshalb fällt hier meist eine klare **Buy-Entscheidung**: Man greift auf bestehende, vortrainierte Modelle zurück.

<br>

Anders sieht es bei der Inferenz aus: Bei einfachen Anwendungsfällen, wie dem Formulieren einer E-Mail, reicht es oft aus, dem Modell ein paar Stichpunkte zu geben. Es greift dann auf sein bereits trainiertes Wissen zurück – ohne dass zusätzliche Daten oder Systemanbindungen notwendig wären. Hier ist die Nutzung sehr niedrigschwellig.

<br>

Bei vielen geschäftlichen Use Cases hingegen reichen die allgemeinen Fähigkeiten eines Modells nicht mehr aus. Wenn beispielsweise User Stories oder Epics automatisch erstellt werden sollen, braucht das Modell zusätzlichen **Kontext zum Projekt** – etwa Ziele, Anforderungen oder bisherige Arbeitspakete. Ebenso beim Beantworten von Ausschreibungen: Hier werden spezifische Informationen über das **ausschreibende Unternehmen**, die **Anforderungen** und die **eigenen Fähigkeiten** benötigt. Diese Daten sind nicht Teil des Trainings, sondern müssen **bei der Inferenz** bereitgestellt werden – etwa über eine Anbindung an SharePoint, CRM-Systeme oder andere Datenquellen. Die Herausforderung besteht hier also nicht im Training, sondern in der **intelligenten Integration der Unternehmensdaten** in den Inferenzprozess. Ob diese Integration intern aufgebaut wird („make“) oder über fertige Lösungen erfolgt („buy“), ist oft eine strategische Entscheidung. Kann aber auch vom einzelnen Anwendungsfall abhängen.

<br>

Besonders deutlich wird diese Komplexität bei fortgeschrittenen Architekturen wie **Retrieval-Augmented Generation (RAG)** oder sogenannten **Agentic Systems**. Diese nutzen ein vortrainiertes Sprachmodell im Kern, erweitern es jedoch durch eine umgebende Logik, die Informationen aus externen Quellen einbindet und den Prozess steuert. Bei einem RAG-System beispielsweise gibt es zahlreiche Stellschrauben: das gewählte **Embedding-Modell**, die **Chunk-Größe** für Dokumente, die **Retriever-Strategie**, der Einsatz eines **Re-Rankers** oder die Gestaltung des finalen Prompts. Um die **Güte des Gesamtsystems** zu bewerten, benötigt man wiederum **Validierungsdaten** – etwa Fragen mit bekannten, idealen Antworten – um testen zu können, ob das System zuverlässig funktioniert. Möchte man die Performance weiter optimieren, müssen oft eigene **Datensätze zur Feineinstellung** erstellt werden. Diese sind in der Regel stark **use-case-spezifisch**, was eine pauschale „Buy“-Lösung meist ausschließt. Hier ist ein gezieltes „Make“ gefragt – zumindest für das System-Design und die Evaluation.

<br>

Daneben gibt es Use Cases, bei denen das Modell selbst nochmals an spezifische Daten angepasst werden muss. Bei generischen Aufgaben mit spezialisierten Ausprägungen – etwa der **Extraktion von Werten aus bestimmten Dokumenttypen** – kann ein bereits vortrainiertes Modell durch sogenanntes **Fine-Tuning** angepasst werden. Manche Anbieter erlauben sogar ein solches Fine-Tuning über Schnittstellen, was diese Szenarien in Richtung „Buy mit Anpassungsmöglichkeit“ verschiebt. Ein Beispiel dafür sind KI-gestützte Dokumentenverarbeitungsdienste, bei denen benutzerdefinierte Extraktionsmodelle trainiert werden können. Anders sieht es aus, wenn ein Modell für eine verwandte aber **abweichende Aufgabenstellung** eingesetzt werden soll, etwa zur Image Segmentation von **Satellitenbildern**, obwohl es ursprünglich als Klassifikationsmodell von Objekten trainiert wurde. In solchen Fällen handelt es sich typischerweise um ein zu spezifisches Thema, sodass oftmals keine sinnvolle generische API dafür verfügbar ist. 

<br>

Und schließlich gibt es Anwendungsbereiche, für die es **keine vortrainierten Modelle** gibt – beispielsweise bei der **Analyse von Kundenverhalten** oder bei **personalisierenden Empfehlungssystemen (Recommender Systems)**. Hier existiert für gewöhnliche keine generell vortrainierte Abstraktion des zugrundeliegenden Problems, sodass Unternehmen gezwungen sind, komplett eigene Lösungen zu entwickeln – von der Datenaufbereitung über das Modelltraining bis zur Integration.


## KI-Anwendungsbeispiele

Wenn ein KI-Modell einmal trainiert ist, bringt es eine spezifische Fähigkeit mit – etwa das Erkennen von Mustern, das Generieren von Texten oder das Treffen von Vorhersagen. Die entscheidende Frage ist dann: Wie kann ich diese Fähigkeit sinnvoll einsetzen, um einen konkreten Mehrwert für mein Unternehmen zu schaffen? Genau hier beginnt die Suche nach geeigneten Anwendungsfällen, den sogenannten Use Cases.

Lassen Sie uns exemplarisch einige Anwendungsfälle betrachten und analysieren, in welchen Bereichen der konkrete Mehrwert der Technologie liegt.

### Autonomes Fahren

Der Einsatz autonomer Fahrzeuge zeigt exemplarisch, wie KI sowohl zur Erschließung neuer Märkte als auch zur Optimierung bestehender Prozesse beitragen kann.

<br>

Zunächst ergeben sich neue Einkommensquellen, insbesondere für Automobilhersteller: Der direkte Verkauf autonomer Fahrzeuge stellt ein zukunftsträchtiges Produktsegment dar – mit dem Potenzial, die bestehende Angebotspalette erheblich zu erweitern. Ergänzend entstehen neue Mobilitätsdienste, etwa fahrerlose Car-Sharing-Angebote, die zusätzliche Geschäftsmodelle erschließen und neue Kundengruppen ansprechen.

<br>

Darüber hinaus profitieren zahlreiche Branchen von Effizienzgewinnen durch den Einsatz autonomer Fahrzeuge im operativen Betrieb. Logistikunternehmen wie DHL senken ihre Zustellkosten durch selbstfahrende Lieferfahrzeuge. Öffentliche Verkehrsbetriebe reduzieren Personalkosten durch autonome Busse. Industrieunternehmen nutzen KI-gesteuerte Transporte innerhalb ihrer Produktionsstätten zur Optimierung des internen Materialflusses. Auch an Flughäfen kommen autonome Fahrzeuge zum Einsatz – etwa beim Gepäcktransport oder als Shuttle-Service – und helfen dabei, den laufenden Betrieb wirtschaftlicher zu gestalten.

<br>

Während einige Unternehmen die Entwicklung der zugrunde liegenden KI-Technologien selbst vorantreiben und diese als eigenes Produkt vermarkten, liegt der Fokus für viele Anwenderunternehmen – etwa in der Logistik – auf dem gezielten Einsatz fertiger Lösungen. Hier steht nicht die Eigenentwicklung im Mittelpunkt, sondern der effiziente Einsatz zur Kostensenkung. In solchen Fällen fällt die strategische Entscheidung in der Regel zugunsten eines „Buy“-Ansatzes – da der Aufwand einer Eigenentwicklung in keinem sinnvollen Verhältnis zum angestrebten Nutzen steht.

### Einsatzmöglichkeiten im Büro und in Geschäftsprozessen

**Produktivitätssteigerung im Büroalltag:**

Sprach-zu-Text-Technologien ermöglichen es, Meetings – etwa in Microsoft Teams oder Zoom – automatisch zu protokollieren und damit die Nachbereitung deutlich zu vereinfachen. Textgenerierungssysteme wie Microsoft 365 Copilot unterstützen beim Verfassen von E-Mails, Zusammenfassungen oder Präsentationen. Auch kreative Aufgaben wie die Gestaltung von Bildern oder Grafiken – etwa mit FLUX oder Microsoft Designer – lassen sich effizienter gestalten.

<br>

Diese Anwendungen betreffen potenziell alle Mitarbeitenden eines Unternehmens. Entsprechend groß ist der Hebel – gleichzeitig aber auch der Bedarf an begleitenden Maßnahmen: Schulungen zur effektiven Nutzung (z. B. durch gezieltes Prompting), der verantwortungsvolle Umgang mit generierten Inhalten und die Einhaltung von Compliance-Vorgaben – etwa bei Bildgenerierung, Markenschutz oder Corporate Identity – sind zentrale Erfolgsfaktoren.

<br>

Ein zusätzlicher Mehrwert entsteht durch die Integration in bestehende IT-Landschaften. KI-gestützte Systeme, die mit internen Datenquellen verknüpft sind – etwa durch semantische Suche oder eingebettete Wissensdatenbanken – eröffnen ganz neue Möglichkeiten der Informationsbeschaffung. Eigene Assistenten mit vordefinierten Rollen und Systemprompts ermöglichen so eine iterative, kontextbasierte Nutzung unternehmensinterner Informationen.

<br>

**Automatisierung strukturierter Geschäftsprozesse:**

Auch in klar definierten Prozessen lässt sich KI wirkungsvoll einsetzen – insbesondere im Dokumentenmanagement und in Supportprozessen. Durch Kombination von OCR-Technologien und KI-Modellen können Dokumente automatisiert analysiert, Inhalte extrahiert und in weiterverwendbare Formate überführt werden. Typische Workflows beinhalten den Upload einer Datei, die automatische Prüfung und Weiterleitung, eine optionale manuelle Freigabe, die strukturierte Ablage sowie Eskalationsmechanismen bei Unklarheiten. Erfolgreiche Implementierung solcher Prozesse erfordert nicht nur die technische Umsetzung, sondern auch die Qualifizierung der Mitarbeitenden zur effektiven Nutzung des neuen Workflows.

<br>

**Kundenservice und Support:**

Ein besonders sichtbarer Anwendungsbereich ist die Automatisierung im Kundenservice. KI kann entlang des gesamten Anfrageprozesses Mehrwert schaffen: durch die Früherkennung kritischer Anliegen, die automatische Klassifikation und Weiterleitung an die richtige Stelle, die kontextuelle Informationsbeschaffung aus CRM-Systemen oder Bestellhistorien sowie die Erstellung von Antwortentwürfen. Bei einfachen Anliegen kann sogar eine vollständig automatisierte Bearbeitung erfolgen – über E-Mail oder Chat.


### Ausblick: Agentenbasierte Assistenzsysteme

Mit dem Fortschritt in der multimodalen und kontextbasierten KI-Entwicklung rückt ein neues Paradigma in den Fokus: autonome, agentenbasierte Assistenzsysteme. Solche Systeme sind in der Lage, komplexe Aufgaben in Echtzeit zu lösen – mit Zugriff auf unterschiedliche Datenquellen, logischer Entscheidungsstruktur und dynamischer Kommunikation.

<br>

Ein Beispiel aus dem E-Commerce: Ein Kunde fragt bei einem Online-Händler wie Zalando nach dem Status seiner Rückerstattung. Der KI-Agent identifiziert den Kunden, erkennt die Intention hinter der Nachricht, prüft den Status der Retoure in der Datenbank und generiert eine passende Antwort. Dabei kombiniert der Agent Sprachverarbeitung, Datenzugriff, Business-Logik und Prozesswissen – Fähigkeiten, die ihn in die Nähe eines digitalen Mitarbeitenden rücken.

### Datenbasierte Intelligenz und systematische Mustererkennung

Neben Anwendungsfällen, bei denen KI menschliche Tätigkeiten unterstützt oder automatisiert, gibt es Szenarien, in denen KI-Systeme nicht nur schneller, sondern auch objektiv leistungsfähiger sind. Denn: KI kann enorme Datenmengen auswerten, systematische Muster identifizieren und daraus Erkenntnisse ableiten, die für Menschen – ohne datengetriebene Herangehensweise – kaum zugänglich wären. In diesen Anwendungsbereichen verschwimmen die Grenzen zur klassischen Datenanalyse und Data Science zunehmend.

<br>

**Vorhersagemodelle (Predictive Modeling):**

Ein typisches Beispiel sind Wetterprognosen. Während früher Erfahrungsregeln wie *„Wenn die Schwalben tief fliegen, gibt es Regen“* herangezogen wurden, arbeiten heutige Vorhersagesysteme mit hochauflösenden numerischen Modellen, gespeist aus Satellitendaten, Sensoren und Wetterstationen weltweit. Der technologische Fortschritt hat dazu geführt, dass maschinelle Vorhersagen mittlerweile deutlich präziser sind als menschliche Einschätzungen.

<br>

Auch in anderen Bereichen – etwa bei Sportanalysen oder Fußballwetten – liefern KI-Modelle oft treffsicherere Prognosen. Durch die systematische Auswertung von Spielerstatistiken, Taktiken, Verletzungshistorien und früheren Ergebnissen können Maschinen Wahrscheinlichkeiten objektiver und umfassender berechnen als menschliche Experten.

<br>

**Empfehlungssysteme (Recommender Systems):**

Online-Plattformen wie Netflix, Spotify oder Amazon setzen konsequent auf KI-basierte Empfehlungssysteme, um Nutzererlebnisse zu personalisieren und Umsätze zu steigern. Die zugrunde liegenden Algorithmen analysieren Milliarden von Interaktionen, um gezielt passende Inhalte vorzuschlagen:

<br>

- Netflix empfiehlt Filme, basierend auf Ähnlichkeiten zu bereits angesehenen Titeln und dem Verhalten ähnlicher Nutzerprofile.
- Amazon erkennt Muster im Kaufverhalten und schlägt beispielsweise automatisch Staubsaugerbeutel vor, sobald ein Staubsauger im Warenkorb liegt.
- Auch im Finanzbereich helfen KI-basierte Empfehlungen dabei, individuell passende Anlageprodukte zu identifizieren – abgestimmt auf Verhalten, Vorlieben und Risikoprofile der Kundinnen und Kunden.

<br>

**Anomalieerkennung (Anomaly Detection):**

Ein weiteres starkes Einsatzfeld ist die automatisierte Erkennung von Abweichungen in großen Datenströmen – also Ereignisse, die vom erwarteten „Normalzustand“ abweichen und oft auf Probleme, Risiken oder Chancen hinweisen.

<br>

In der *Predictive Maintenance* etwa analysieren KI-Modelle Sensordaten von Maschinen und erkennen kleinste Veränderungen im Verhalten – zum Beispiel wenn ein Aufzug ungewöhnlich oft seine Tür schließt oder nicht mehr exakt auf Stockwerkhöhe stoppt. Solche Frühindikatoren erlauben eine proaktive Wartung und verhindern ungeplante Ausfälle.

<br>

Auch im Bereich *Cybersecurity* ist die Fähigkeit zur Anomalieerkennung essenziell. Hier analysieren KI-Systeme kontinuierlich Telemetriedaten, um verdächtige Aktivitäten zu identifizieren – etwa ungewöhnlich viele Datei-Downloads, Anmeldungen aus fremden Regionen oder auffällige Abweichungen vom gewohnten Nutzerverhalten. Frühzeitig erkannt, ermöglichen solche Muster eine sofortige Reaktion auf potenzielle Sicherheitsvorfälle.

<br>

**"Make or Buy?" – Wer hat die besseren Daten?**

Die Entscheidung, ob Unternehmen solche KI-Lösungen selbst entwickeln oder auf externe Anbieter zurückgreifen, hängt maßgeblich von der verfügbaren Datenbasis ab.

<br>

Bei Predictive-Maintenance-Anwendungen haben Hersteller wie Schindler oder Otis einen klaren Vorteil: Sie verfügen über Daten aus tausenden verbauten Systemen weltweit – und damit über eine viel bessere Grundlage für präzise Vorhersagemodelle als einzelne Betreiber. In solchen Fällen ist der Zukauf externer Lösungen sinnvoll.

<br>

Im Bereich Cybersecurity profitieren Anbieter wie Avira von der Auswertung von Millionen angeschlossener Clients. Sie erkennen neue Bedrohungen schneller und umfassender als einzelne Unternehmen es je könnten – ein klarer Vorteil für externe Anbieter.

<br>

Anders sieht es aus, wenn die eingesetzten Systeme stark unternehmensspezifisch sind – etwa bei der Telemetrie innerhalb individueller IT-Landschaften. Hier spielen Faktoren wie interne Softwarekonfigurationen, typische Arbeitsabläufe oder spezifische Sicherheitsrichtlinien eine große Rolle. Maßgeschneiderte, intern entwickelte Lösungen sind in solchen Fällen oft besser geeignet, da sie auf den konkreten Kontext zugeschnitten sind und die Besonderheiten der eigenen Umgebung gezielt berücksichtigen können.

<br>

**Fazit:**

Die Nutzung von KI bringt nicht per se einen Mehrwert – sie entfaltet ihr Potenzial erst durch den gezielten, durchdachten Einsatz in konkreten Use Cases. Unternehmen, die den Schritt von der reinen Technologiebegeisterung hin zur strategischen Anwendung schaffen, erschließen sich damit neue Geschäftsmodelle, steigern ihre Effizienz und verbessern nachhaltig ihre Wettbewerbsfähigkeit.


## Systematische Identifikation und Bewertung von KI-Anwendungsfällen

Nachdem konkrete Anwendungsbeispiele gezeigt haben, wie vielseitig KI in Unternehmen eingesetzt werden kann, stellt sich die zentrale Frage: Wie lassen sich geeignete Use Cases systematisch identifizieren, bewerten und priorisieren? Der gezielte Umgang mit dieser Frage entscheidet darüber, ob Unternehmen ihre Ressourcen wirkungsvoll einsetzen und ob KI-Initiativen über Einzelprojekte hinaus strategischen Mehrwert entfalten können.

<br>

Der Einstieg in die Identifikation geeigneter Anwendungsfälle erfolgt typischerweise auf zwei Wegen. Zum einen entstehen Ideen direkt in den Fachbereichen. Mitarbeitende erleben alltägliche Herausforderungen, entdecken Engpässe oder haben konkrete Vorstellungen, wie KI Prozesse verbessern oder Aufgaben erleichtern könnte. Diese Bottom-up-Perspektive ist besonders nah an der Praxis und führt häufig zu schnell umsetzbaren Lösungen mit direktem Nutzen. Zum anderen verfolgen viele Unternehmen einen strukturierten Top-down-Ansatz. Hier analysieren zentrale Stellen wie Business-Analysten oder KI-Verantwortliche systematisch Prozesse, führen Interviews oder untersuchen bereichsübergreifende Potenziale. Gerade in Bereichen mit wenig direktem Kundenkontakt – etwa in der Verwaltung oder im Backoffice – lassen sich so Potenziale identifizieren, die aus der Einzelperspektive leicht übersehen werden. Beide Herangehensweisen können sich ergänzen: Während Bottom-up den Blick für konkrete, oft kreative Ideen öffnet, stellt Top-down sicher, dass keine relevanten Potenziale übersehen werden und die Ausrichtung strategisch bleibt.

<br>

Sind potenzielle Anwendungsfälle einmal identifiziert, stellt sich die Frage nach ihrer Bewertung. Dabei geht es nicht nur um den erwarteten wirtschaftlichen Nutzen – etwa durch Kostensenkung, Umsatzsteigerung oder Qualitätsverbesserung –, sondern auch um die Umsetzbarkeit. Eine tragfähige Einschätzung berücksichtigt unter anderem die Verfügbarkeit und Qualität der zugrunde liegenden Daten, den technischen Reifegrad im Unternehmen, die Einhaltung regulatorischer Vorgaben – etwa im Hinblick auf Datenschutz oder den AI Act – sowie die Frage, ob eine Lösung intern entwickelt oder besser extern bezogen werden sollte. Auch organisatorische Aspekte spielen eine Rolle: Welche Veränderungen in Rollen, Prozessen oder Kompetenzen sind notwendig? Welche Zielgruppen werden betroffen sein, und wie groß ist der Schulungs- oder Change-Aufwand?

<br>

Erst auf dieser Basis lässt sich eine sinnvolle Priorisierung vornehmen. Nicht alle Use Cases sind gleich relevant, realistisch oder strategisch bedeutsam. Manche versprechen schnelle Erfolge mit geringem Aufwand, andere stehen für langfristige Innovation und grundlegende Veränderung. Eine fundierte Priorisierung betrachtet daher sowohl den erwarteten Return on Investment als auch potenzielle Unsicherheiten, Risiken und Abhängigkeiten. Auch Synergien zwischen verschiedenen Anwendungsfällen spielen eine Rolle – etwa wenn mehrere Projekte auf dieselben Datenquellen oder Plattformen zugreifen können. Letztlich geht es darum, eine ausgewogene Mischung zu finden: zwischen kurzfristig realisierbaren Lösungen mit direktem Nutzen und ambitionierten Leuchtturmprojekten, die das Unternehmen strategisch weiterentwickeln.

<br>

Besonders wirksam wird dieser Prozess, wenn er zentral koordiniert wird. Eine übergeordnete Steuerung schafft Transparenz darüber, welche KI-Systeme im Unternehmen im Einsatz sind – ein wichtiger Aspekt, nicht zuletzt aus regulatorischer Sicht. Gleichzeitig lassen sich technologische Synergien besser heben, etwa durch die gemeinsame Nutzung von Dateninfrastrukturen, Schnittstellen oder KI-Komponenten. Vor allem aber ermöglicht die zentrale Steuerung eine bewusste strategische Ausrichtung: Unternehmen können gezielt die Use Cases fördern, die zu ihrer Positionierung und ihren Zielen passen. Ein Händler wie Walmart, der sich über niedrige Preise differenziert, wird andere Prioritäten setzen als ein Unternehmen, das sich über Premium-Service oder Innovationsführerschaft positioniert. In beiden Fällen sollte die Auswahl von Use Cases eng mit der übergeordneten Unternehmens- und Datenstrategie abgestimmt sein.

<br>

Die Auswahl geeigneter KI-Anwendungsfälle ist damit nicht nur eine operative Aufgabe, sondern ein strategischer Gestaltungsprozess – und eine zentrale Voraussetzung, um aus technologischen Möglichkeiten konkreten unternehmerischen Mehrwert zu machen.

## Erfolgsfaktoren für die nachhaltige Einführung und Skalierung von KI

Der erfolgreiche Einsatz von KI ist weit mehr als ein Technologieprojekt – er ist ein unternehmensweiter Transformationsprozess. Während viele Unternehmen bereits erste Erfahrungen mit KI sammeln, stellt sich die zentrale Frage: **Wie wird aus ersten Piloten ein systematischer, skalierbarer Mehrwert?** Um diesen nächsten Reifegrad zu erreichen, braucht es gezielte Investitionen – nicht nur in Technologie, sondern auch in Strukturen, Kompetenzen und Kultur.

### 1. Eine strategische Vision und realistische Standortbestimmung

Am Anfang steht eine **klare KI-Vision**, die beschreibt, welche Rolle KI künftig im Unternehmen spielen soll: Will man mit dem Wettbewerb Schritt halten oder gezielt Innovationsführer werden? Diese Vision muss greifbar sein – und kompatibel mit der Gesamtstrategie des Unternehmens. Eine überzeugende KI-Vision dient dabei nicht nur als strategischer Nordstern, sondern auch als Motivationsanker für Mitarbeitende.

<br>

Gleichzeitig braucht es eine ehrliche Standortbestimmung: **Wie KI-ready ist das Unternehmen wirklich?** Ein strukturiertes **KI-Reifegradmodell** hilft dabei, die Ausgangslage zu bewerten – etwa hinsichtlich Datenverfügbarkeit, Technologiekompetenz, Organisationsstruktur oder kultureller Offenheit. Diese Einschätzung bildet die Grundlage, um geeignete nächste Schritte zu planen.

### 2. Strukturen schaffen: KI-Roadmap, Technologie-Radar und Center of Excellence

Wer langfristig erfolgreich sein will, braucht **strukturierte Steuerungsinstrumente**. Eine **KI-Roadmap** hilft, Anwendungsfälle zu priorisieren, Projekte sinnvoll zu sequenzieren und Fortschritte transparent zu machen. Gleichzeitig unterstützt ein **Technologie-Radar** dabei, neue Entwicklungen im Blick zu behalten – etwa neue Open-Source-Modelle, API-Angebote oder disruptive Trends wie Agenten-Frameworks oder multimodale KI.

<br>

Eine bewährte organisatorische Maßnahme ist der Aufbau eines **KI-Kompetenzzentrums (Center of Excellence, CoE)**. Dieses fungiert als zentrale Anlaufstelle für Use Case Management, Wissenstransfer, Projektbegleitung und Governance – idealerweise interdisziplinär besetzt und eng angebunden an das Top-Management.

### 3. Kompetenzen fördern: KI-Literacy, Trainings und Community Building

KI verändert nicht nur Prozesse, sondern auch Rollen, Kompetenzen und Verantwortlichkeiten. Die wichtigste Ressource bleibt dabei der Mensch. Es braucht **Mitarbeitende, die KI verstehen, einordnen und wirksam einsetzen können**. Deshalb ist der Aufbau von **KI-Kompetenzen** auf allen Ebenen entscheidend: von der Geschäftsführung über Fachbereiche bis hin zu IT und Datenverantwortlichen.

- **KI-Literacy** bedeutet, grundlegende Konzepte, Chancen und Risiken zu verstehen.
- **Trainings und Workshops** vermitteln anwendungsbezogenes Wissen – etwa zu Prompt Engineering, Datenintegration oder Compliance-Themen.
- **AI Ambassador-Programme** identifizieren und fördern engagierte Mitarbeitende, die als Multiplikatoren wirken und andere mitziehen.

Besonders wirksam ist der Aufbau einer unternehmensinternen **KI-Community** – also einer Plattform für Austausch, Erfahrungstransfer und gegenseitige Unterstützung. So wird KI vom isolierten Projekt zum kollektiven Lernprozess.

### 4. Kommunikation und Kultur gezielt gestalten

KI verändert Arbeitsweisen, Entscheidungsprozesse und Verantwortlichkeiten – und das kann Unsicherheit auslösen. Umso wichtiger ist eine **proaktive, transparente Kommunikation**, die Ängste ernst nimmt, Nutzen aufzeigt und Raum für Beteiligung schafft.

<br>

Eine offene **KI-Kultur** fördert Neugier, Experimentierfreude und verantwortungsbewussten Umgang mit neuen Technologien. Wichtig ist dabei auch, typische Missverständnisse auszuräumen – etwa die Erwartung, dass KI automatisch besser, schneller oder objektiver ist. Nur wer KI wirklich versteht, kann sie sinnvoll einsetzen.

<br>

Ebenso entscheidend ist die frühzeitige Einbindung zentraler Stakeholder – etwa der Fachbereiche, der IT, des Betriebsrats und der Rechtsabteilung. Wer von Anfang an transparent kommuniziert und die Veränderung gemeinsam gestaltet, erhöht die Akzeptanz deutlich.

### 5. Skalierung ermöglichen: von Leuchtturmprojekten zur Breitenwirksamkeit

Viele Unternehmen starten mit erfolgreichen Prototypen oder Pilotprojekten – der nächste Schritt ist jedoch die **skalierte Umsetzung in der Breite**. Dafür braucht es standardisierte Methoden, wiederverwendbare Komponenten (z. B. Prompt-Vorlagen, Datenanbindungen, UI-Bausteine, Architektur Blueprints), aber auch einheitliche Qualitäts- und Sicherheitsstandards. Wichtig: Skalierung ist kein Selbstläufer – sie muss aktiv geplant, begleitet und gemanagt werden.

<br>

Dabei helfen **Make-or-Buy-Entscheidungen** auf Systemebene, um zu klären, welche Lösungen unternehmensspezifisch entwickelt und welche zugekauft werden sollten. In vielen Fällen bieten **externe Kooperationen** wertvolle Impulse – etwa mit Universitäten, Start-ups, Beratungen oder KI-Initiativen. Wer Teil eines aktiven **Ökosystems** ist, profitiert nicht nur von technischem Fortschritt, sondern auch von neuen Ideen, Talenten und Synergien.

### 6. Governance und Ethik von Anfang an mitdenken

Technologieeinsatz braucht Vertrauen – sowohl intern als auch extern. Deshalb sollten ethische Leitlinien, regulatorische Anforderungen (z. B. AI Act, DSGVO) und Fragen der Verantwortlichkeit von Anfang an berücksichtigt werden. Ziel ist eine **verlässliche, transparente und faire Nutzung von KI**, die sowohl rechtlich als auch gesellschaftlich tragfähig ist. Wie will das Unternehmen mit KI umgehen? Wo liegen rote Linien? Welche Prinzipien gelten beim Einsatz sensibler Technologien? 

### Fazit: Eine ganzheitliche und skalierbare KI-Strategie ist der Schlüssel zum Erfolg

Die erfolgreiche Einführung von KI erfordert weit mehr als nur die Implementierung einzelner Tools oder Algorithmen. Sie ist ein umfassender Prozess, der klare strategische Ziele, eine angepasste Infrastruktur, den Aufbau von Kompetenzen und eine enge Zusammenarbeit mit externen Partnern umfasst. Unternehmen, die KI nicht nur als Technologie, sondern als ganzheitlichen Veränderungsprozess begreifen, können nicht nur ihre Effizienz steigern und neue Geschäftsmodelle entwickeln, sondern sich auch als zukunftsfähige und innovative Organisationen positionieren. **KI ist kein Selbstläufer, sondern ein strategisches Asset**, das langfristig gestaltet werden muss – Schritt für Schritt, mit klarer Vision und der Bereitschaft, kontinuierlich zu lernen und zu adaptieren.
