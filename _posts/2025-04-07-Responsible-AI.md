---
layout: post
title:  "KI-Risiken aktiv managen: Strategien für den sicheren Einsatz"
date:   2025-04-07
categories: [AI]
excerpt: > #
  Zur effektiven Minderung von KI-Risiken braucht es Datenqualität, robuste Systemarchitekturen und klare Verantwortlichkeiten.
math: false
---

Der Einsatz von KI bringt grundsätzlich Risiken mit sich – etwa das Risiko, dass ein Modell Fehler macht oder in einem ungeeigneten Kontext verwendet wird. Hinzu kommen rechtliche Anforderungen, die nicht nur als Orientierung dienen, sondern verpflichtend einzuhalten sind. Wer diese gesetzlichen Vorgaben nicht erfüllt, riskiert nicht nur operative Fehler, sondern auch empfindliche Sanktionen. Responsible AI ist daher nicht nur ein technisches Ziel, sondern eine strategische Notwendigkeit – angesichts realer technischer und rechtlicher Risiken sowie wachsender gesellschaftlicher Erwartungen.

### Wenn KI irrt: Risiken durch falschen oder fehlenden Output

Ein KI-System, das falsche Informationen liefert, kann massive Schäden verursachen. Gibt ein Chatbot einem Kunden falsche Auskünfte, etwa zu Vertragskonditionen oder Verfügbarkeiten, kann das zur Kündigung oder zum Abbruch des Kaufs führen. Noch gravierender sind Fälle, in denen die KI unhöflich oder beleidigend reagiert – der Imageschaden für das Unternehmen ist oft enorm und nachhaltig. Ebenso kritisch sind automatisierte Workflows mit KI, etwa bei der Extraktion von Werten aus Dokumenten: Werden hier fehlerhafte Daten erkannt und übernommen, können im schlimmsten Fall falsche Summen überwiesen oder inkorrekte Informationen in zentrale IT-Systeme eingepflegt werden – mit direkten finanziellen oder prozessualen Folgen.

<br>

Doch auch **fehlender Output** (z. B. durch technische Fehler oder unzureichende Trainingsdaten) kann kritische Prozesse blockieren. Besonders gefährlich ist dies, wenn ein ganzer Geschäftsprozess auf der Verfügbarkeit der KI aufbaut – etwa ein automatisiertes Ticket-System oder eine KI-basierte Sachbearbeitung. Fällt das System aus, kann es zum Stillstand von Abläufen oder zum Verlust von Service-Level-Agreements führen.

<br>

Im Zeitalter generativer KI treten neue Gefahren hinzu: **Prompt Injection** oder **Prompt Hacking** kann Systeme dazu verleiten, sicherheitskritische Informationen preiszugeben oder schädliche Inhalte zu generieren.

### Anforderungen durch den Gesetzgeber

Angesichts dieser Risiken hat die Gesetzgebung nachgezogen. Bisher war es vor allem im Eigeninteresse der Unternehmen, dass KI-Systeme korrekt funktionieren – um Kosten zu sparen, Effizienz zu steigern oder Schäden zu vermeiden. Es fehlten jedoch klare Rahmenbedingungen dafür, dass der Einsatz von KI auch **fair** erfolgt und **keinen Schaden bei Dritten** anrichtet. Genau hier setzt der **EU AI Act** an: Er verfolgt einen risikobasierten Ansatz, bei dem KI-Systeme je nach Einsatzgebiet und potenzieller Gefährdung unterschiedlich reguliert werden. Hochrisikoanwendungen unterliegen umfassenden Pflichten: von technischer Robustheit über Daten-Governance bis hin zu **Dokumentation**, **Transparenzpflichten** und Maßnahmen zur Vermeidung gesellschaftlicher Risiken. Bestimmte KI-Anwendungen mit besonders hohem Schadenspotenzial – etwa solche zur biometrischen Massenüberwachung im öffentlichen Raum – werden **komplett verboten**. Auch **urheberrechtliche Aspekte** werden relevant, wenn generative KI Inhalte erstellt. Gleichzeitig gelten Grundprinzipien wie Datenschutz (DSGVO), Fairness, Nachvollziehbarkeit und menschliche Aufsicht.

### Was bedeutet „richtiger“ Output bei KI-Modellen?

Was ein „richtiger“ Output ist, hängt stark davon ab, welche Art von Modell betrachtet wird – und wie es eingesetzt wird. Bei numerischen Vorhersagen, etwa zur Umsatz- oder Nachfrageprognose, lässt sich der Fehler relativ einfach quantifizieren – etwa über die durchschnittliche Abweichung vom tatsächlichen Wert. Komplexer ist die Bewertung bei generativer KI, z. B. bei automatisch erstellten Texten oder Zusammenfassungen. Hier genügt es nicht, nur die faktische Korrektheit zu prüfen – auch der **Ton** des Outputs spielt eine Rolle. Ein Chatbot, der zwar korrekt, aber schnippisch oder unhöflich antwortet, erfüllt oftmals nicht die gewünschten Qualitätskriterien. Für Klassifikationsmodelle, etwa zur Erkennung bestimmter Merkmale in medizinischen Bildern, geht es häufig um Ja-/Nein-Entscheidungen. Hier wird die Modellqualität meist über Metriken wie Accuracy gemessen. Fehler können darüber hinaus in zwei Gruppen eingeteilt werden – Fehler 1. Art (falsch positiv) oder Fehler 2. Art (falsch negativ). Welche Art von Fehler schwerer wiegt, hängt maßgeblich vom Anwendungskontext ab: In der Tumorerkennung kann ein falsch negativer Befund (Tumor übersehen) schwerwiegender sein als ein falsch positiver (fälschlich angenommener Tumor). Diese Beispiele verdeutlichen: Die Qualität und Risikoeinschätzung eines Modells ist **nicht nur von den Daten und Metriken**, sondern wesentlich vom **Einsatzgebiet** abhängig. Ein falsch erkannter Zifferndreher in einer Telefonnummer ist ärgerlich – bei einem Rechnungsbetrag oder einem Diagnosesystem aber potenziell folgenschwer.

<br>

Modelle müssen nicht nur korrekte Antworten generieren. Auch **Erklärbarkeit** ist oftmals ein zentrales Qualitätsmerkmal – insbesondere, wenn Modelle in sensiblen Bereichen Entscheidungen vorbereiten oder beeinflussen. Außerdem ist es hilfreich, wenn Modelle nicht nur eine Vorhersage oder Klassifizierung geben, sondern zusätzlich auch noch eine Einschätzung liefern, wie hoch sie die eigene Verlässlichkeit sehen.

<br>

Ein Beispiel: Bei der automatisierten Erkennung von Daten aus eingescannten Dokumenten mittels OCR (Optical Character Recognition) kann das KI-System nicht nur die extrahierten Inhalte liefern, sondern auch eine Angabe zur eigenen Erkennungsgenauigkeit bereitstellen – etwa in Form eines Vertrauenswertes. So kann etwa ein Rechnungsbetrag mit einer Verlässlichkeit von 98 % erkannt werden, während ein handschriftlicher Vermerk nur mit 60 % erkannt wurde. Solche Hinweise ermöglichen es, gezielt manuelle Nachprüfungen dort durchzuführen, wo die KI unsicher ist – und erhöhen so die Gesamtsicherheit des Prozesses.

### Wie Fehler entstehen – und wie man sie verhindert

Zunächst gilt: Auch ein grundsätzlich gut trainiertes Modell wird nicht in jedem Einzelfall korrekt vorhersagen. Das liegt in der Natur probabilistischer Systeme, deren Entscheidungen auf Wahrscheinlichkeiten beruhen. Je nach eingesetzter Metrik – etwa der Accuracy – ist mit einer gewissen Fehlerrate zu rechnen. Diese lässt sich nur verringern, wenn das Modell gezielt weiterentwickelt oder mit zusätzlichen Daten verbessert wird. Das ist jedoch nicht immer möglich oder wirtschaftlich sinnvoll.

<br>

Eine weitere verbreitete Fehlerquelle liegt im falschen Einsatzkontext. Ein Modell, das unter bestimmten Bedingungen gut funktioniert, kann versagen, wenn sich die Rahmenbedingungen verändern. Häufig tritt dies auf, wenn die Verteilung der Daten im Produktivbetrieb von der im Training abweicht. Ein Beispiel: Ein Bilderkennungsmodell, das ausschließlich mit Tageslichtaufnahmen trainiert wurde, wird bei Bildern in der Dämmerung fehleranfällig. Selbst bei konstanten Lichtverhältnissen kann ein verändertes Vorkommen bestimmter Objekte die Leistung beeinträchtigen – etwa wenn ein Modell Hunde im Training kaum gesehen hat, im Betrieb aber täglich viele erkennen soll. Die tatsächliche Modellleistung fällt dann oft deutlich hinter die ursprünglich gemessene Accuracy zurück. Ein **verantwortungsvolles KI-System** muss daher über ein robustes Qualitätsmanagement verfügen.

### AI-Systemarchitektur als Schlüssel zur Verantwortung

Ein durchdachtes KI-System besteht nicht nur aus einem trainierten Modell, sondern aus einer ganzheitlichen Architektur, in der jede Komponente eine spezifische Rolle für die Sicherheit, Robustheit und Vertrauenswürdigkeit des Systems spielt.

<br>

Den Anfang machen die **Daten**: Sie bilden das Fundament jeder KI-Anwendung. Ihre sorgfältige Auswahl, die Sicherstellung der Herkunft und die Prüfung auf Verzerrungen (Bias) entscheiden maßgeblich über die Fairness und Verlässlichkeit der späteren Vorhersagen.

<br>

In der **Trainingsphase** werden geeignete Modelle mit diesen Daten trainiert. Die Auswahl des Modells, die Optimierungsstrategie und die Definition geeigneter Metriken sind entscheidend dafür, ob das Modell die gewünschten Aufgaben zuverlässig erfüllen kann.

<br>

Der Schritt in die produktive Umgebung erfolgt im **Deployment**. Gerade in dieser Phase zeigt sich die Bedeutung von **MLOps** (Machine Learning Operations): Ein strukturierter MLOps-Prozess stellt sicher, dass Modelle zuverlässig, skalierbar und sicher in den Produktivbetrieb überführt und dort dauerhaft betreut werden können. Dazu gehören unter anderem automatisierte Tests, kontinuierliche Integration und Deployment (CI/CD) und das Management von Modellversionen.

<br>

Während der **Inferenz**, also der eigentlichen Anwendung des Modells, geht es um die zuverlässige Generierung von Ausgaben. Diese sollten durch kontinuierliches **Monitoring** auf Anomalien oder Abweichungen vom erwarteten Verhalten geprüft werden. Eine **Output-Validierung** – z. B. durch zusätzliche Prüfmodelle – kann dabei helfen, Fehler frühzeitig zu erkennen. Ein Beispiel: Bei generativer KI kann ein Sprachmodell einen Textvorschlag für eine Kunden-E-Mail erzeugen, während ein nachgelagertes KI-Modell diesen Text hinsichtlich Tonalität, Verständlichkeit oder Marken-Compliance überprüft, bevor er freigegeben wird. So wird sichergestellt, dass die Ausgabe nicht nur inhaltlich korrekt, sondern auch stilistisch und kommunikativ passend ist.

<br>

**Guardrails** dienen dazu, das System im Live-Betrieb abzusichern. Sie können zum Beispiel in Form von Moderationsmechanismen oder Filtersystemen auftreten, die verhindern, dass gefährliche oder unpassende Inhalte entstehen – insbesondere bei generativen KI-Systemen. Ein generatives KI-System kann durch inhaltliche Guardrails abgesichert werden, die bestimmte Begriffe blockieren, bei ethisch sensiblen Themen eine menschliche Freigabe erzwingen oder gezielt verhindern, dass das System zu rechtlichen oder medizinischen Fragen Stellung nimmt. So wird vermieden, dass die KI unbeabsichtigt fehlerhafte oder haftungsrelevante Inhalte generiert.

<br>

**Feedback-Mechanismen** ermöglichen es, aus echten Nutzungsszenarien zu lernen. Nutzerfeedback, Log-Analysen oder explizite Bewertungssignale können genutzt werden, um das Modell schrittweise zu verbessern oder gezielt neu zu trainieren. Der Mehrwert eines solchen weiteren Trainings liegt darin, dass das Modell besser an reale Anforderungen und Veränderungen im Nutzungskontext angepasst werden kann. Bei einem OCR-System, das automatisch Informationen aus eingescannten Formularen extrahiert, kann das System durch weiteres Training mit neueren oder besser annotierten Beispieldokumenten lernen, auch schwer lesbare Handschriften oder neue Formularlayouts besser zu erkennen. So steigt die Erkennungsgenauigkeit kontinuierlich – insbesondere in Anwendungsfällen, in denen die Dokumente stark variieren oder regelmäßig neue Formate hinzukommen.

<br>

Schließlich sind **Eskalationsmechanismen** notwendig, um in kritischen Situationen angemessen reagieren zu können – etwa wenn das Modell mit geringer Konfidenz operiert oder sensible Entscheidungen anstehen. In solchen Fällen muss definiert sein, wann ein Mensch eingreift oder zusätzliche Prüfungen erforderlich sind. Ein Beispiel ist ein OCR-System zur automatisierten Erkennung von Rechnungsbeträgen. Ist der erkannte Betrag höher als ein vordefinierter Schwellenwert – etwa 10.000 € – wird die automatische Verarbeitung gestoppt, und ein manueller Freigabeprozess durch einen Mitarbeitenden angestoßen. So lassen sich finanzielle Risiken minimieren und sensible Vorgänge zusätzlich absichern.

<br>

Nur durch das Zusammenspiel all dieser Komponenten kann ein KI-System entstehen, funktional leistungsfähig, robust und vertrauenswürdig ist.

### Der Lebenszyklus eines Modells: Verantwortung endet nicht beim Deployment

Responsible AI bedeutet auch: Verantwortung über die Zeit hinweg zu übernehmen – und zwar entlang des gesamten Lebenszyklus eines Modells. Dieser beginnt mit der **Definition und Risikobewertung**: Hier werden die Ziele, Einsatzbereiche und potenziellen Risiken des KI-Systems analysiert. Es ist essenziell, frühzeitig zu bewerten, ob der geplante Anwendungsfall sensible Daten, hohe Auswirkungen auf Individuen oder regulatorische Anforderungen mit sich bringt.

<br>

Darauf folgt die **Datenbeschaffung und das Modelltraining**. In dieser Phase ist besonders auf die Qualität, Herkunft und Repräsentativität der Trainingsdaten zu achten. Verzerrte oder unvollständige Daten können später zu diskriminierenden oder schlichtweg falschen Ergebnissen führen. Auch die Wahl des Modells und die Trainingsmethodik müssen zum Ziel und zum Einsatzkontext passen.

<br>

Anschließend erfolgt die **Test- und Validierungsphase**. Hier wird das Modell unter kontrollierten Bedingungen geprüft: Wie gut funktioniert es mit realitätsnahen Daten? Werden Schwächen – etwa bei bestimmten Gruppen oder in Grenzfällen – sichtbar? Fairness, Robustheit und Transparenz sollten zentrale Bewertungskriterien sein.

<br>

Mit dem **Deployment**, also der Einführung in die Praxis, beginnt die produktive Nutzung. Um Risiken zu minimieren, braucht es ein Monitoring-System, das nicht nur technische Kennzahlen überwacht, sondern auch auf unerwartete Verhaltensweisen oder Anomalien reagiert.

<br>

In der Phase des **kontinuierlichen Lernens und Feedbacks** wird geprüft, wie das Modell im Alltag performt – und wo Optimierungspotenzial besteht. Nutzerfeedback, Systemmetriken und neue Daten sollten genutzt werden, um Anpassungen oder Re-Trainings zu planen.

<br>

Schließlich darf auch die **Stilllegung oder das geplante Re-Training** eines Modells nicht vergessen werden. Ein Modell, das auf veralteten Annahmen oder Daten basiert, kann zum Risiko werden. Deshalb braucht es klare Kriterien, wann ein System abgeschaltet oder grundlegend überarbeitet werden muss.

<br>

Nur wenn alle diese Phasen durchdacht und mit geeigneten Prozessen abgesichert sind, kann ein KI-System als verantwortungsvoll betrieben gelten.

### Verantwortung braucht klare Ownership

Um Risiken im Umgang mit KI systematisch zu minimieren, sind spezifische Rollen mit klaren Zuständigkeiten erforderlich. Eine mögliche Aufteilung dieser Verantwortlichkeiten könnte wie folgt aussehen:

<br>

- Der **Model Owner** verantwortet die Leistungsfähigkeit und Robustheit des KI-Modells. Er sorgt für korrektes Training, zuverlässigen Betrieb und regelmäßige Überprüfungen.
- Der **Data Owner** wacht über Qualität, Vollständigkeit und Repräsentativität der Daten. Er stellt sicher, dass die Daten aus vertrauenswürdigen Quellen stammen, keine Verzerrungen aufweisen und rechtmäßig genutzt werden.
- Der **Business Owner** definiert den Anwendungsfall, trägt die Verantwortung für Nutzen sowie Geschäftsrisiken und entscheidet über Anpassungen oder die Stilllegung des Modells.
- Der **Legal & Compliance Owner** prüft die Einhaltung regulatorischer Vorgaben (z. B. DSGVO, EU AI Act) und gewährleistet, dass alle Dokumentations- und Nachweispflichten erfüllt sind.

<br>

Diese Rollenverteilung dient als Beispiel. Die konkrete Ausgestaltung variiert je nach Organisation und Einsatzgebiet. Entscheidend ist jedoch: Zuständigkeiten müssen klar geregelt und organisatorisch verankert sein. Nur so lassen sich Verantwortlichkeiten im Fehlerfall nachvollziehen, notwendige Kontrollen effektiv umsetzen und eine dauerhaft vertrauenswürdige Nutzung von KI sicherstellen.



