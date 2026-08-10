---
layout: post
title:  "Einführung in Agentic Systems: Wie KI lernt zu denken, zu planen und Werkzeuge einzusetzen"
date:   2025-05-09
categories: [AI]
excerpt: > #
  Wie Agentic Systems durch schrittweises Denken, adaptive Planung und die Orchestrierung von Werkzeugen komplexe, mehrstufige Aufgaben lösen können.
math: true
---

Stell dir vor, du hättest einen super-intelligenten Assistenten, der menschenähnlichen Text verstehen und generieren kann. Das ist im Wesentlichen die Funktionsweise eines Großen Sprachmodells (LLM). Aber über das bloße Ausspucken von Wörtern hinaus können LLMs angeleitet werden, Probleme *schlussfolgernd* zu lösen und sogar *Werkzeuge* zu nutzen, um komplexe Aufgaben zu bewältigen und mit der Außenwelt zu interagieren.

## Schrittweises Denken: Chain of Thought

Manchmal liefert die direkte Befragung eines LLMs zu einer komplexen Frage nicht das beste Ergebnis. Es ist, als würde man jemanden bitten, eine komplizierte mathematische Aufgabe im Kopf zu lösen, ohne einen richtigen Lösungsansatz zu verwenden. Die "Chain of Thought" (CoT) Technik ermutigt das LLM, das Problem in kleinere, logische Schritte zu zerlegen und seine Überlegungen dabei zu erläutern. Dies führt oft zu genaueren Antworten und schafft zusätzliche Transparenz.

**Beispiel, ohne chain of thought**

*Nutzer:* Schreibe eine Python-Funktion, um zu überprüfen, ob eine gegebene Zeichenkette ein Palindrom ist.

*LLM:*
```python
def ist_palindrom(s):
  return s == s[::-1]
```

Obwohl die Funktion für einfache Fälle richtige Ausgaben macht, ist sie insbesondere für Fälle mit Berücksichtigung von Groß- und Kleinschreibung nicht korrekt. Außerdem gibt sie keinerlei Einblicke in den Denkprozess zur besseren Nachvollziehbarkeit der Lösung.

**Beispiel, mit chain of thought**

*Nutzer:* Schreibe eine Python-Funktion, um zu überprüfen, ob eine gegebene Zeichenkette ein Palindrom ist. Erkläre deine Schritte.

*LLM:*
Okay, lass uns Schritt für Schritt denken. Um zu überprüfen, ob eine Zeichenkette ein Palindrom ist, muss sie vorwärts und rückwärts gleich gelesen werden können.

1. Zuerst muss ich die Groß- und Kleinschreibung ignorieren. Also sollte ich die Eingabezeichenkette in Kleinbuchstaben umwandeln.
2. Als Nächstes muss ich nicht-alphanumerische Zeichen wie Leerzeichen und Satzzeichen ignorieren. Ich kann eine neue Zeichenkette erstellen, die nur Buchstaben und Zahlen enthält.
3. Dann kann ich diese verarbeitete Zeichenkette mit ihrer Umkehrung vergleichen. Wenn sie identisch sind, ist die ursprüngliche Zeichenkette ein Palindrom.
4. Hier ist der Python-Code, der diese Schritte implementiert:

```python
import re

def ist_palindrom(text):
  """Überprüft, ob eine gegebene Zeichenkette ein Palindrom ist, wobei Groß-/Kleinschreibung und nicht-alphanumerische Zeichen ignoriert werden."""
  processed_text = ''.join(re.findall(r'[a-zA-Z0-9]', text)).lower()
  return processed_text == processed_text[::-1]
```

Hier sieht man, wie der CoT-Ansatz nicht nur den Code liefert, sondern auch die Begründung für jeden Schritt erklärt, wodurch die Lösung verständlicher und robuster wird.

## Verkettungen von LLM-Aufrufen (Chaining)

Oft reicht ein einzelner LLM-Aufruf nicht aus, um ein vielschichtiges Problem zu lösen. Wir müssen möglicherweise eine größere Aufgabe in eine Abfolge kleinerer, miteinander verbundener Schritte zerlegen und die Ausgabe eines LLM-Aufrufs als Eingabe für den nächsten verwenden. Das ist die Idee hinter "Chains".

**Beispiel: Von Stichpunkten zum mehrsprachigen LinkedIn-Post**

**Schritt 1:** Vom Stichpunkt zur Textausformulierung (LLM-Aufruf 1): Der Nutzer gibt Stichpunkte für einen LinkedIn-Post ein. Das LLM formuliert daraus einen zusammenhängenden Text.

*Nutzer-Eingabe:*
```
- Neues Feature veröffentlicht
- Bessert Nutzererfahrung auf
- Steigert Produktivität um 15%
- Mehr dazu im Blog (Link folgt)
```

*LLM-Ausgabe 1:*

"Wir freuen uns, die Veröffentlichung eines brandneuen Features bekannt zu geben! Dieses Update wurde entwickelt, um Ihre Nutzererfahrung deutlich zu verbessern. Erste Tests zeigen eine Steigerung der Produktivität um beeindruckende 15%. Erfahren Sie alle Details in unserem neuesten Blogbeitrag (Link folgt)."

**Schritt 2:** Anpassung für LinkedIn (LLM-Aufruf 2): Der generierte Text wird für die LinkedIn-Plattform optimiert (z.B. Hinzufügen von relevanten Hashtags, prägnantere Formulierungen).

*LLM-Ausgabe 2:*

"🚀 Spannende Neuigkeiten! Wir haben gerade ein brandneues Feature gelauncht, das eure Nutzererfahrung auf ein neues Level hebt und die Produktivität um 15% steigert! 🔥 Neugierig? Alle Infos gibt's im Blog: [Link folgt] #innovation #produktivität #userexperience #software #update"

**Schritt 3:** Übersetzung ins Englische (LLM-Aufruf 3): Der für LinkedIn optimierte Text wird ins Englische übersetzt.

LLM-Ausgabe 3:

"🚀 Exciting news! We've just launched a brand-new feature designed to elevate your user experience and boost productivity by 15%! 🔥 Curious? Find all the details on our blog: [Link follows] #innovation #productivity #userexperience #software #update"

![LLM Chain diagram](/assets/images/llm_tools_reasoning_chain_1.png)

## Jenseits von Text: LLMs mit Werkzeugen befähigen

LLMs sind leistungsstarke Textverarbeiter, aber ihre Fähigkeiten erweitern sich dramatisch, wenn sie über "Werkzeuge" mit der Außenwelt interagieren können. Man kann sich Werkzeuge als externe Funktionen oder Dienste vorstellen, die das LLM nutzen kann, um Informationen zu sammeln, Aktionen auszuführen oder mit Systemen zu interagieren.

**Wie funktioniert Tool Usage?**

- **Werkzeugbeschreibung:** Jedes Werkzeug hat eine Beschreibung, die dem LLM mitteilt, was es tut, welche Parameter es benötigt und welche Ausgabe es erwartet.
- **Werkzeugaufruf:** Wenn das LLM feststellt, dass ein Werkzeug benötigt wird, um eine Nutzeranfrage zu erfüllen, generiert es einen "Tool Call". Dieser Aufruf spezifiziert, welches Werkzeug verwendet werden soll und welche Werte für seine Parameter gelten.
- **Orchestrierungslayer:** Dies ist eine entscheidende Komponente, die zwischen dem LLM und den Werkzeugen sitzt. Sie empfängt den Tool Call vom LLM, führt das eigentliche Werkzeug aus (z.B. führt ein Python-Skript aus, macht einen API-Aufruf) und erhält das Ergebnis.
- **Ergebnisverständnis:** Der Orchestrierungslayer speist das Ergebnis des Werkzeugs zurück an das LLM.
- **Finale Ausgabe:** Das LLM versteht das Ergebnis des Werkzeugs und verwendet es, um eine abschließende, umfassende Antwort an den Nutzer zu generieren.

**Werkzeuge können "side effects" haben:**

Es ist wichtig zu beachten, dass Werkzeuge nicht nur zum Abrufen von Informationen dienen. Sie können auch Aktionen ausführen, die "side effects" haben, d.h. den Zustand eines Systems verändern.

**Beispiel: Tool Usage mit Wetterabfrage per JSON**

Folgender System Prompt (nur ein Auszug) zeigt, wie einem LLM die Verwendung eines Werkzeuges per Instruktion beigebracht werden kann:

```
Du hast Zugriff auf ein Tool namens "get_weather".

### Tool-Beschreibung: 
Ruft die aktuellen Wetterdaten für einen bestimmten Ort ab.

### Parameter:
- location: (string, erforderlich) Der Ort, für den die Wetterdaten abgerufen werden soll (z.B. "München", "Berlin").
- unit: (string, optional, Standard: "metric") Die Einheit der Temperatur ("metric" für Celsius, "imperial" für Fahrenheit).

### Beispiele für die Übersetzung von Nutzeranfragen in JSON-Tool-Aufrufe:

Nutzeranfrage: "Wie ist das Wetter in Hamburg?"
JSON-Tool-Aufruf: {"tool_name": "get_weather", "parameters": {"location": "Hamburg"}}

Nutzeranfrage: "Zeig mir das Wetter in New York in Fahrenheit."
JSON-Tool-Aufruf: {"tool_name": "get_weather", "parameters": {"location": "New York", "unit": "imperial"}}

Antworte dem Nutzer immer in der Sprache des Nutzers. Nutze das Tool, wenn die Anfrage nach Wetterinformationen für einen bestimmten Ort fragt.

```

**Beispielhafter Ablauf:**

**1. Nutzer-Anfrage:** "Wie ist das Wetter in München?"

**2. LLM-Analyse:** Das LLM erkennt die Anfrage nach Wetterinformationen für "München".

**3. Tool-Aufruf (JSON):** Das LLM generiert einen Tool-Aufruf im JSON-Format:

```
{"tool_name": "get_weather", "parameters": {"location": "München"}}
```

**4. Orchestrierungsebene:**

- Der Orchestrierungslayer empfängt diesen JSON-Aufruf.
- Er extrahiert den Tool-Namen ("get_weather") und die Parameter ({"location": "München"}).
- Er führt den eigentlichen API-Aufruf an den Wetterdienst mit dem Ort "München" durch.
- Er empfängt die Antwort vom Wetterdienst (z.B. im JSON-Format mit Temperatur, Windgeschwindigkeit etc.).
- Er gibt das Ergebnis der Wetter-API zurück an das LLM.

**5. LLM-Antwort:** Das LLM verarbeitet das Ergebnis der Wetter-API und generiert eine Antwort für den Nutzer in deutscher Sprache:

"Das Wetter in München ist aktuell 15 Grad Celsius, mit leichtem Wind." (basierend auf der Antwort der Wetter-API).

Das folgende Diagramm veranschaulicht diesen Ablauf:

![Sequence diagram](/assets/images/llm_tools_reasoning_react_2.png)

### Weitere mögliche Tools

Die Palette an möglichen Tools für LLMs ist breit gefächert. Hier einige Beispiele:

- **Code-Interpreter:** Ermöglicht das Ausführen von Code (z.B. Python, JavaScript) direkt durch das LLM, um Ergebnisse zu verifizieren oder dynamische Inhalte zu generieren.
- **Dateisystem-Interaktion:** Tools zum Lesen und Schreiben von Dateien, nützlich für die Bearbeitung von Konfigurationsdateien, Protokollen etc.
- **Versionskontrollsysteme (z.B. Git):** Tools zum Interagieren mit Git-Repositories, wie das Anzeigen von Commits, Erstellen von Branches oder sogar das Einreichen von Änderungen.
- **API-Clients:** Generische Tools zum Aufrufen beliebiger APIs, um Daten abzurufen oder Aktionen auszuführen (wie im Wetterbeispiel).
- **Datenbank-Konnektoren:** Tools zur Interaktion mit Datenbanken, um Daten abzufragen oder zu manipulieren.
- **Planungs- und Projektmanagement-Tools:** Tools zum Erstellen und Verwalten von Aufgaben, Zuweisen von Verantwortlichkeiten etc.
- **Visualisierungstools:** Tools zur Erstellung von Diagrammen oder anderen visuellen Darstellungen von Daten oder Strukturen (bspw. mittels Mermaid.js).

## Intelligente und Nicht-Deterministische Lösungspfade

Moderne LLM-basierte Anwendungen entwickeln sich über einfache, lineare Aufgabenabfolgen hinaus. Um komplexere Probleme zu lösen und flexibler auf Nutzeranfragen reagieren zu können, werden Mechanismen für intelligente und nicht-deterministische Lösungspfade implementiert. Das bedeutet, dass der genaue Ablauf der Informationsverarbeitung und Werkzeugnutzung nicht starr vorgegeben ist, sondern sich dynamisch an die jeweilige Situation anpasst. Im Folgenden betrachten wir den Agenten "KnowledgeAssistant", der zur Informationsbeschaffung dient und über folgende Werkzeuge verfügt:

- **search_internal_knowledge_base:** Durchsucht interne Firmendokumente (z.B. Richtlinien, Projektdokumentationen).
- **search_public_internet:** Findet öffentliche Nachrichten, allgemeine Informationen und externe Daten.
- **interact_with_company_database:** Greift auf strukturierte Firmendaten zu (z.B. Kundendaten, Produktinformationen, Lagerbestände).

Zwei Kernkonzepte für solche intelligenten Pfade sind die situationsabhängige Auswahl von Werkzeugen (Routing) und die iterative Verbesserung durch Selbstreflexion.

### Intelligente Pfadauswahl durch Tool-Routing

Beim Tool-Routing analysiert der Agent die Nutzeranfrage und entscheidet, welches seiner verfügbaren Werkzeuge oder welcher vordefinierte Unterprozess am besten geeignet ist, um die Anfrage zu beantworten. Dies führt zu einer Verzweigung im Lösungspfad.

**Beispiel A:** Interne Information benötigt

- **Nutzeranfrage:** "Wie lautet unsere aktuelle Unternehmensrichtlinie zum Thema ‘Mobiles Arbeiten’?"
- **Gedankengang des Agenten:** Die Schlüsselwörter "unsere" und "Unternehmensrichtlinie" deuten klar auf ein internes Dokument hin.
- **Resultierender Pfad/Aktion:** Der Agent wählt das Werkzeug search_internal_knowledge_base und sucht mit relevanten Stichwörtern nach der entsprechenden Richtlinie.

**Beispiel B:** Öffentliche Information benötigt

- **Nutzeranfrage:** "Was sind die neuesten Nachrichten und Produktankündigungen von ‘FutureGadgets Inc.’?"
- **Gedankengang des Agenten:** "Neueste Nachrichten" und "Produktankündigungen" eines externen Unternehmens erfordern eine Recherche im öffentlichen Raum.
- **Resultierender Pfad/Aktion:** Der Agent wählt das Werkzeug search_public_internet und formuliert eine Suchanfrage, um aktuelle Informationen über ‘FutureGadgets Inc.’ zu finden.

In diesen Fällen wählt der Agent basierend auf der initialen Analyse einen von mehreren möglichen Pfaden.

![Routing](/assets/images/llm_tools_reasoning_routing_3.png)

### Selbstreflexion für iterative Lösungsfindung

Selbstreflexion ermöglicht es dem Agenten, die Ergebnisse seiner Aktionen zu bewerten und seinen Plan bei Bedarf anzupassen. Wenn eine erste Aktion nicht zum gewünschten Ergebnis führt, kann der Agent seine Strategie ändern und es erneut versuchen. Die Anzahl der Iterationen ist dabei nicht vorbestimmt.

**Beispiel:** Iterative Informationssuche mit Qualitätsprüfung

- **Nutzeranfrage:** "Ich suche spezifische technische Studien zur Effizienzsteigerung durch Robotik in der Intralogistik, publiziert nach 2022."
- **Gedankengang/Prozess des Agenten:**
  - **Versuch 1 (Aktion & Beobachtung):** Der Agent startet mit einer breiteren Suche über search_public_internet, z.B. "Robotik Intralogistik Effizienz Studien". Er stellt fest, dass viele Ergebnisse zu allgemein sind oder vor 2022 publiziert wurden.
  - **Versuch 1 (Selbstreflexion & Kritik):** "Ergebnis unzureichend. Suchanfrage war zu breit und hat die zeitliche Einschränkung sowie den Fokus auf 'technische Studien' nicht präzise genug abgebildet."
  - **Versuch 2 (Anpassung & Aktion):** Der Agent verfeinert die Suchanfrage für search_public_internet zu "technische Studie Robotik Effizienz Intralogistik" und fügt einen Filter für Publikationen nach 2022 hinzu.
  - **Versuch 2 (Beobachtung & Selbstreflexion):** Die Ergebnisse sind nun deutlich relevanter und spezifischer. Der Agent befindet sie als ausreichend für die Beantwortung der Anfrage. (Falls nicht, könnte eine weitere Iteration folgen).
- **Resultierender Pfad/Aktion(en):** Eine variable Anzahl von Aufrufen des Werkzeugs search_public_internet, wobei jede Suchanfrage auf den Erkenntnissen der vorherigen Iteration basiert.

![Reflection](/assets/images/llm_tools_reasoning_reflection_4.png)

Durch diese Mechanismen können LLM-basierte Systeme flexibler und "intelligenter" agieren. Sie wählen nicht nur situationsgerecht Werkzeuge aus, sondern können auch ihre eigenen Strategien anpassen, um auch bei komplexen oder unklar formulierten Anfragen zu besseren Ergebnissen zu gelangen. Der Lösungsweg ist somit nicht starr, sondern passt sich dynamisch den Erfordernissen an.

## Alternative Tool Frameworks und Model Context Protocol (MCP)

LLM-Anwendungen nutzen oft Ketten von Verarbeitungsschritten, in denen das LLM mit externen Werkzeugen und Diensten interagiert. Während JSON-basierte Tools hierfür üblich sind, können die einzelnen Komponenten in solchen Abläufen deutlich vielfältiger sein und über einfache, durch JSON definierte API-Aufrufe hinausgehen.

### Die Bandbreite der Komponenten in Verarbeitungsketten

1.  **Direkte Code-Ausführung (z.B. Python):**
    Eine Komponente kann direkt Code, etwa Python, ausführen. Statt dass das LLM nur JSON für einen Tool-Aufruf generiert, könnte es Code-Snippets erzeugen, die von einer spezialisierten Komponente sicher ausgeführt werden, oder diese kapselt als vordefinierte Funktion bereits komplexe Logik.

2.  **Andere Agents als autonome Komponenten:**
    Ein Verarbeitungsschritt kann auch durch einen eigenständigen Agenten bearbeitet werden – möglicherweise ein weiteres LLM mit eigener Logik, eigenem Speicher und Werkzeugen, das komplexe Teilaufgaben löst und Ergebnisse an den Hauptprozess liefert.

3.  **JSON-basierte Werkzeuge:**
    Natürlich bleiben auch die bewährten JSON-basierten Werkzeugaufrufe wichtig, besonders für die Anbindung an klar definierte externe APIs.

Diese Vielfalt an möglichen Komponenten – von JSON-Tools über Code-Module bis hin zu Sub-Agenten – ist sehr mächtig, erfordert aber eine standardisierte Methode zur Zusammenarbeit und Steuerung.

### Das Model Context Protocol (MCP) als vereinheitlichende Ebene

Hier setzt das **Model Context Protocol (MCP)** an. MCP ist kein spezifisches Werkzeug, sondern ein **standardisiertes Kommunikationsprotokoll**. Es definiert eine gemeinsame "Sprache" für die Interaktion zwischen einem zentralen Orchestrator und den unterschiedlichen Komponenten einer Kette.

Die Kernidee: Eine MCP-konforme Komponente kann intern verschiedenste Funktionalitäten umsetzen (ein JSON-Tool wrappen, Code ausführen, einen ganzen Agenten darstellen oder einen anderen spezialisierten Dienst bereitstellen), während sie nach außen über das MCP-Protokoll einheitlich angesprochen wird. Der Orchestrator sendet Anfragen und Kontext über MCP und erhält Ergebnisse zurück, unabhängig von der internen Implementierung der jeweiligen Komponente.

**Vorteile dieses Ansatzes durch MCP**

Diese Vereinheitlichung durch MCP bietet klare Vorteile:

* **Modularität:** Komponenten können unabhängig entwickelt und einfach ausgetauscht werden.
* **Flexibilität:** Komplexe Systeme lassen sich aus diversen, optimal passenden Bausteinen zusammensetzen.
* **Vereinfachte Integration:** Der Orchestrator interagiert mit allen Komponenten über eine einheitliche Schnittstelle, was die Gesamtkomplexität reduziert.

MCP schafft somit eine wichtige Abstraktionsebene, die den Aufbau robusterer, anpassungsfähigerer und letztlich intelligenterer LLM-basierter Anwendungen ermöglicht.

## Agentic Systems

Der nächste Schritt in der Entwicklung intelligenter Systeme besteht darin, aus der reichhaltigen Menge an möglichen Knoten (Tools, Agenten, MCP-Server) die richtigen für eine bestimmte Aufgabe auszuwählen und deren Interaktion und Abfolge optimal zu gestalten.

Betrachten wir als illustratives Beispiel die Beantwortung einer Frage, für die mehrere Suchanfragen und Verarbeitungsschritte erforderlich sind: 

"Wer war deutscher Bundeskanzler, als Oliver Bierhoff das Golden Goal schoss?"

**1. LLM (Reasoning):** "Um diese Frage zu beantworten, benötige ich zwei Informationen: Wann hat Oliver Bierhoff das Golden Goal geschossen und wer war zu diesem Zeitpunkt Bundeskanzler. Ich kann dafür ein Suchwerkzeug verwenden."

**2. Orchestrierungsebene (Act - Tool Call 1):**

```
{"tool_name": "search", "parameters": {"query": "Oliver Bierhoff Golden Goal Datum"}}
```

**3. Orchestrierungsebene (Observation 1):** Das Suchwerkzeug liefert das Ergebnis: "Oliver Bierhoff schoss das Golden Goal im Finale der Fußball-Europameisterschaft 1996 am 30. Juni 1996."

**4. LLM (Reason):** "Jetzt weiß ich das Datum. Nun muss ich herausfinden, wer am 30. Juni 1996 Bundeskanzler war. Ich verwende erneut das Suchwerkzeug."

**5. Orchestrierungsebene (Act - Tool Call 2):**

```
{"tool_name": "search", "parameters": {"query": "Bundeskanzler Deutschland 30. Juni 1996"}}
```

**6. Orchestrierungsebene (Observation 2):** Das Suchwerkzeug liefert das Ergebnis: "Helmut Kohl war von 1982 bis 1998 Bundeskanzler der Bundesrepublik Deutschland."

**7. LLM (Reason):** "Ich habe beide Informationen gefunden. Ich kann nun die finale Antwort formulieren."

**8. LLM (Final Answer):** "Als Oliver Bierhoff das Golden Goal schoss (am 30. Juni 1996), war Helmut Kohl Bundeskanzler der Bundesrepublik Deutschland."

![Agentic system diagram](/assets/images/llm_tools_reasoning_agentic_system_5.png)

In komplexeren Szenarien könnte ein Agent einen detaillierten Plan erstellen, welche Tools oder andere Agenten in welcher Reihenfolge und mit welchen Parametern aufgerufen werden müssen, um das Ziel zu erreichen. Dieser Planungsprozess kann iterativ sein, wobei der Plan nicht bereits von Anfang an feststeht sondern basierend auf den Ergebnissen der einzelnen Schritte angepasst wird. Frameworks wie ReAct helfen dabei, diesen iterativen Prozess aus Reasoning und Aktionen zu strukturieren.

**Disclaimer**: Dieser Beitrag ist ein Gemeinschaftsprojekt von mir und der KI. Die Ideen zum Thema, die Struktur und die hoffentlich anschaulichen Beispiele stammen allesamt aus meiner eigenen kleinen Denkfabrik und lagen schon als Folien bereit. Weil mein Gehirn aber manchmal eher auf "Diashow" als auf "fließender Text" gepolt ist, hat mir eine freundliche KI dabei geholfen, das Ganze in diese Blog-Post-Form zu gießen. Ich habe dann noch hier und da den Feinschliff übernommen, damit auch alles sitzt. Teamwork makes the dream work, oder so ähnlich!