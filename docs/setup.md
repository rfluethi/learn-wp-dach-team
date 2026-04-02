# Setup-Anleitung (Admin)

Diese Anleitung beschreibt die einmalige Einrichtung des Repositories für neue Instanzen oder nach einem Repository-Transfer.

---

## Voraussetzungen

- GitHub-Account mit Admin-Rechten auf dem Repository
- [GitHub CLI](https://cli.github.com) installiert (`brew install gh`) und eingeloggt (`gh auth login`)
- Git installiert

---

## Schritt 1: Repository erstellen

1. GitHub.com → **New repository**
2. Name: `learn-wp-dach-team`
3. Sichtbarkeit: **Private** (zum Testen) oder **Public** (nach Teamentscheid)
4. README: Ja (ankreuzen)
5. **Create repository**

---

## Schritt 2: Issue-Vorlagen einfügen

```bash
# Repository klonen
git clone https://github.com/DEIN-USERNAME/learn-wp-dach-team.git
cd learn-wp-dach-team

# Ordner erstellen
mkdir -p .github/ISSUE_TEMPLATE
```

Die drei Vorlagen-Dateien in `.github/ISSUE_TEMPLATE/` ablegen:

- `sitzung.yml`
- `traktandum.yml`
- `aufgabe.yml`

```bash
git add .github/
git commit -m "Issue-Vorlagen für Sitzungen, Traktanden und Aufgaben"
git push
```

**Prüfen:** Issues → **New issue** → Alle drei Vorlagen erscheinen.

---

## Schritt 3: Labels erstellen

```bash
REPO="DEIN-USERNAME/learn-wp-dach-team"

gh label create "sitzung"         --repo "$REPO" --color "0075ca" --description "Monatliches Team-Meeting (Traktanden + Protokoll)" --force
gh label create "traktandum"      --repo "$REPO" --color "e4e669" --description "Vorgeschlagenes Diskussionsthema für nächste Sitzung" --force
gh label create "aufgabe"         --repo "$REPO" --color "f4a261" --description "Action Item / Task aus einer Sitzung" --force
gh label create "beschluss"       --repo "$REPO" --color "0e8a16" --description "Entscheidung gefällt" --force
gh label create "blockiert"       --repo "$REPO" --color "d73a4a" --description "Aufgabe hat einen Blocker oder Abhängigkeit" --force
gh label create "nächste-sitzung" --repo "$REPO" --color "bfd4f2" --description "Vertagt – kommt in die nächste Sitzung" --force
gh label create "lerngruppe"      --repo "$REPO" --color "7057ff" --description "Thema rund um Lerngruppen" --force
gh label create "webseite"        --repo "$REPO" --color "cfd3d7" --description "Thema rund um learn-wp-dach.org" --force
gh label create "übersetzung"     --repo "$REPO" --color "006b75" --description "Übersetzungsprojekte" --force
gh label create "organisation"    --repo "$REPO" --color "e99695" --description "Organisatorische Aufgaben" --force
```

**Prüfen:** Issues → **Labels** → 10 Labels sichtbar.

---

## Schritt 4: GitHub Project (Kanban Board) erstellen

1. GitHub → Tab **Projects** → **New project**
2. Vorlage: **Board**
3. Name: `Learn WP DACH – Aufgaben`
4. Spalten erstellen (Traktanden, Offen, In Arbeit, Blockiert, Erledigt):

   | Spalte | Beschreibung |
   | --- | --- |
   | Traktanden | Vorgeschlagene Diskussionsthemen |
   | Offen | Aufgaben, noch nicht begonnen |
   | In Arbeit | Aufgaben aktiv in Bearbeitung |
   | Blockiert | Aufgaben mit Blocker |
   | Erledigt | Abgeschlossene Aufgaben |

5. Automation einrichten: Project → **`...`** → **Workflows**
   - *Item added to project* → Status: **Offen**
   - *Item closed* → Status: **Erledigt**
   - *Item reopened* → Status: **Offen**
6. Feld **Estimate** erstellen: Project → **`...`** → **Settings** → **Custom fields** → **Add field**
   - Typ: **Number**
   - Name: `Estimate`
   - Dieses Feld nimmt den geschätzten Zeitbedarf pro Traktandum in Minuten auf und erlaubt eine Gesamtschätzung der Sitzungsdauer.

---

## Schritt 5: Automatischen Protokoll-Index einrichten

Der Workflow `.github/workflows/protokoll-index.yml` aktualisiert die `README.md` automatisch, sobald ein Sitzungs-Issue geschlossen wird.

```bash
mkdir -p .github/workflows
# Datei protokoll-index.yml in diesen Ordner legen
git add .github/workflows/protokoll-index.yml
git commit -m "Automatischer Protokoll-Index via GitHub Actions"
git push
```

**Workflow-Inhalt** (entspricht `.github/workflows/protokoll-index.yml`)**:**

> Hinweis: Der Workflow benötigt das Secret `GH_PAT` (siehe Schritt 6b), um offene Sitzungen nach Board-Status zu filtern und nach Jahr zu gruppieren. Manueller Start: Repository → **Actions** → **Protokoll-Index aktualisieren** → **Run workflow**.

```yaml
name: Protokoll-Index aktualisieren

on:
  issues:
    types: [closed]
  workflow_dispatch:

jobs:
  update-index:
    if: github.event_name == 'workflow_dispatch' || contains(github.event.issue.labels.*.name, 'sitzung')
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: read

    steps:
      - uses: actions/checkout@v4

      - name: Protokoll-Index in README.md aktualisieren
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GH_PAT_TOKEN: ${{ secrets.GH_PAT }}
        run: |
          # Abgeschlossene Sitzungen – nach Jahr gruppiert
          gh issue list \
            --repo ${{ github.repository }} \
            --label sitzung \
            --state closed \
            --limit 100 \
            --json number,title,closedAt,url \
            --jq '
              sort_by(.title) | reverse |
              group_by(.title | split(" ")[1] | split("-")[0]) | reverse |
              .[] |
              (.[0].title | split(" ")[1] | split("-")[0]) as $year |
              (
                ["#### " + $year, "", "| Sitzung | Datum |", "| --- | --- |"] +
                [.[] | "| [" + .title + "](" + .url + ") | " + (.closedAt | split("T")[0]) + " |"] +
                [""]
              ) | .[]
            ' \
            > /tmp/protokolle.txt

          # Offene Sitzungen – nach Board-Status in Nächste/In-Bearbeitung aufgeteilt
          GH_TOKEN="$GH_PAT_TOKEN" gh api graphql -f query='
            query {
              user(login: "rfluethi") {
                projectV2(number: 11) {
                  items(first: 50) {
                    nodes {
                      content {
                        ... on Issue {
                          title
                          url
                          state
                          labels(first: 10) {
                            nodes { name }
                          }
                        }
                      }
                      fieldValues(first: 20) {
                        nodes {
                          ... on ProjectV2ItemFieldSingleSelectValue {
                            name
                            field {
                              ... on ProjectV2SingleSelectField {
                                name
                              }
                            }
                          }
                        }
                      }
                    }
                  }
                }
              }
            }
          ' | jq -r '
            .data.user.projectV2.items.nodes[] |
            select(.content != null) |
            select(.content.state == "OPEN") |
            select(.content.labels.nodes | map(.name) | index("sitzung") != null) |
            (.fieldValues.nodes | map(select(.field != null) | select(.field.name == "Status") | .name) | .[0]) as $status |
            if ($status == "In Arbeit" or $status == "Blockiert") then
              "in-arbeit\t| [" + .content.title + "](" + .content.url + ") |"
            elif ($status == null or $status == "Offen") then
              "naechste\t| [" + .content.title + "](" + .content.url + ") |"
            else empty end
          ' | tee >(grep "^in-arbeit" | cut -f2 > /tmp/in-arbeit.txt) | grep "^naechste" | cut -f2 > /tmp/naechste.txt || true

          {
            echo "# Learn WP DACH – Team Repository"
            echo ""
            echo "Dieses Repository enthält die Sitzungsprotokolle, Traktanden und Aufgaben des **Learn WP DACH Teams**. Das monatliche Meeting findet jeweils am letzten Dienstag des Monats um 20:00 Uhr statt."
            echo ""
            echo "## Sitzungen"
            echo ""
            if [ -s /tmp/naechste.txt ]; then
              echo "### Nächste Sitzung"
              echo ""
              echo "| Sitzung |"
              echo "| --- |"
              cat /tmp/naechste.txt
              echo ""
            fi
            if [ -s /tmp/in-arbeit.txt ]; then
              echo "### In Bearbeitung"
              echo ""
              echo "| Sitzung |"
              echo "| --- |"
              cat /tmp/in-arbeit.txt
              echo ""
            fi
            echo "### Protokolle"
            echo ""
            cat /tmp/protokolle.txt
            echo "## Links"
            echo ""
            echo "| | |"
            echo "| --- | --- |"
            echo "| [Aufgaben-Board](https://github.com/users/rfluethi/projects/11) | Kanban Board mit allen offenen Aufgaben |"
            echo "| [Alle Issues](https://github.com/${{ github.repository }}/issues) | Sitzungen, Traktanden und Aufgaben |"
            echo ""
            echo "## Dokumentation"
            echo ""
            echo "| Dokument | Beschreibung |"
            echo "| --- | --- |"
            echo "| [Konzept](docs/konzept.md) | Übersicht über das System |"
            echo "| [Benutzeranleitung](docs/benutzeranleitung.md) | Schritt-für-Schritt für alle Teammitglieder |"
            echo "| [Setup-Anleitung](docs/setup.md) | Technische Einrichtung (Admin) |"
            echo ""
            echo "## Mitmachen"
            echo ""
            echo "- [Wie du dich beteiligen kannst](CONTRIBUTING.md)"
            echo "- [Verhaltenskodex](CODE_OF_CONDUCT.md)"
            echo ""
            echo "## Lizenz"
            echo ""
            echo "Dieses Repository steht unter der [CC BY 4.0 Lizenz](LICENSE). Inhalte dürfen geteilt und bearbeitet werden, sofern die Urheberschaft angegeben wird."
            echo ""
            echo "Zuletzt aktualisiert: $(date '+%Y-%m-%d')"
          } > README.md

      - name: Änderungen committen und pushen
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git diff --staged --quiet || git commit -m "Protokoll-Index aktualisiert: ${{ github.event.issue.title }}"
          git push
```

---

## Schritt 6: Traktandum-Workflow einrichten

Dieser Workflow verschiebt Issues mit dem Label `traktandum` automatisch in die Spalte **Traktanden** des Kanban Boards.

### 6a: Personal Access Token (PAT) erstellen

Das normale `GITHUB_TOKEN` hat keinen Zugriff auf user-level Projects. Deshalb braucht es einen PAT mit zwei Scopes:

1. GitHub.com → Avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. **Generate new token (classic)**
3. Note: z.B. `learn-wp-dach-team board`
4. Scopes aktivieren:
   - **`repo`** (vollständig ankreuzen) – für Zugriff auf Issue-IDs
   - **`project`** – für Zugriff auf GitHub Projects
5. **Generate token** → Token kopieren

### 6b: Token als Repository-Secret speichern

1. Repository → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**
3. Name: `GH_PAT` (genau so)
4. Secret: den kopierten Token einfügen
5. **Add secret**

> Den Token nie in den Code oder in einen Chat einfügen – immer nur als Secret speichern.

### 6c: Workflow-Datei einfügen

```bash
# Datei traktandum-board.yml in .github/workflows/ ablegen
git add .github/workflows/traktandum-board.yml
git commit -m "Workflow: Traktandum automatisch ins Board einordnen"
git push
```

**Prüfen:** Ein neues Issue mit Vorlage "Traktandum" erstellen → erscheint nach ca. 30 Sekunden in der Spalte **Traktanden**.

---

## Schritt 7: Copilot Coding Agent deaktivieren

> **Wichtig:** Ohne diese Einstellung übernimmt der Copilot Coding Agent Issues und verschiebt sie ins Kanban Board.

1. GitHub.com → Avatar → **Settings**
2. **Copilot** → **Coding agent**
3. **Repository access** → **"Selected repositories"**
4. `learn-wp-dach-team` **nicht** aufnehmen

---

## Schritt 8: Copilot-Training deaktivieren *(bei öffentlichem Repo)*

1. GitHub.com → Avatar → **Settings**
2. **Copilot** → **Features**
3. Abschnitt **Privacy** → **"Allow GitHub to use my data for AI model training"** → **Disabled**

> Bei privaten Repositories nicht zwingend nötig.

---

## Schritt 9: Teammitglieder einladen

Repository → **Settings** → **Collaborators** → **Add people**

Alle Teammitglieder brauchen einen GitHub-Account.

> Alle neuen Teammitglieder sollten [CONTRIBUTING.md](../CONTRIBUTING.md) und [CODE_OF_CONDUCT.md](../CODE_OF_CONDUCT.md) lesen, bevor sie aktiv werden.

---

## Schritt 10: Branch-Protection einrichten *(optional)*

> **Hinweis:** Die GitHub Actions Workflows committen direkt auf `main`. Branch-Protection-Rules müssen daher so konfiguriert werden, dass `github-actions[bot]` Pushes bypassen darf.

1. Repository → **Settings** → **Branches** → **Add branch ruleset**
2. Regelname: `main protection`
3. Target: `main`
4. Regeln aktivieren:
   - **Require a pull request before merging** *(für manuelle Änderungen)*
   - **Allow specified actors to bypass** → `github-actions[bot]` hinzufügen
5. **Save changes**

---

## Troubleshooting

### Workflow schlägt fehl

**Symptom:** GitHub Actions zeigt roten Fehler beim `protokoll-index.yml` oder `traktandum-board.yml`.

**Vorgehen:**

1. Repository → **Actions** → fehlgeschlagenen Run öffnen → Fehlermeldung lesen
2. Häufige Ursachen:

| Fehlermeldung | Ursache | Lösung |
| --- | --- | --- |
| `Could not resolve to a node with the global id` | PAT hat nicht den Scope `repo` oder `project` | PAT neu erstellen mit beiden Scopes, Secret `GH_PAT` aktualisieren |
| `Resource not accessible by integration` | `GH_PAT` Secret fehlt oder ist abgelaufen | Repository → Settings → Secrets → `GH_PAT` prüfen oder neu setzen |
| `Projekt nicht gefunden` | Project-Nummer in Workflow stimmt nicht | Workflow-Datei: `projectV2(number: ...)` auf aktuelle Nummer prüfen |
| `jq: error` | Unerwartete API-Antwort | Run nochmals manuell starten; falls Problem anhält, API-Response im Log prüfen |

1. Manuell testen: Repository → **Actions** → **Protokoll-Index aktualisieren** → **Run workflow**

### PAT erneuern

1. GitHub.com → Avatar → **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Bestehenden Token wählen → **Regenerate token**
3. Token kopieren → Repository → **Settings** → **Secrets and variables** → **Actions** → `GH_PAT` → **Update secret**

---

## Repository transferieren

Sobald der Zielort feststeht (z.B. DE-WordPress-GitHub):

Repository → **Settings** → **Danger Zone** → **Transfer ownership**

Folgendes bleibt vollständig erhalten:

- Alle Issues (inkl. Kommentare, Labels, Assignees)
- GitHub Projects / Kanban Board
- Labels, Milestones, Issue-Vorlagen
- Alle Links werden automatisch weitergeleitet
