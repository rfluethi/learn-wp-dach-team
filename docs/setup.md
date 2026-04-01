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
```

**Prüfen:** Issues → **Labels** → 9 Labels sichtbar.

---

## Schritt 4: GitHub Project (Kanban Board) erstellen

1. GitHub → Tab **Projects** → **New project**
2. Vorlage: **Board**
3. Name: `Learn WP DACH – Aufgaben`
4. Spalten erstellen:

| Spalte | Beschreibung |
|---|---|
| Traktanden | Vorgeschlagene Diskussionsthemen |
| Offen | Aufgaben, noch nicht begonnen |
| In Arbeit | Aufgaben aktiv in Bearbeitung |
| Blockiert | Aufgaben mit Blocker |
| Erledigt | Abgeschlossene Aufgaben |

5. Automation einrichten: Project → **`...`** → **Workflows**
   - *Item added to project* → Status: **Offen**
   - *Item closed* → Status: **Erledigt**
   - *Item reopened* → Status: **Offen**

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

**Workflow-Inhalt:**

```yaml
name: Protokoll-Index aktualisieren
on:
  issues:
    types: [closed]
jobs:
  update-index:
    if: contains(github.event.issue.labels.*.name, 'sitzung')
    runs-on: ubuntu-latest
    permissions:
      contents: write
      issues: read
    steps:
      - uses: actions/checkout@v4
      - name: Protokoll-Index in README.md aktualisieren
        env:
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          gh issue list \
            --repo ${{ github.repository }} \
            --label sitzung \
            --state closed \
            --limit 100 \
            --json number,title,closedAt,url \
            --jq 'sort_by(.title) | reverse | .[] |
              "| [" + .title + "](" + .url + ") | " + (.closedAt | split("T")[0]) + " |"' \
            > /tmp/protokolle.txt
          {
            echo "# Learn WP DACH – Team Repository"
            echo ""
            echo "Dieses Repository enthält die Sitzungsprotokolle, Traktanden und Aufgaben des **Learn WP DACH Teams**."
            echo ""
            echo "- [Aufgaben-Board](../../projects/1)"
            echo "- [Alle Issues](../../issues)"
            echo "- [Slack: #training (dewp.slack.com)](https://dewp.slack.com)"
            echo ""
            echo "## Protokolle"
            echo ""
            echo "| Sitzung | Datum |"
            echo "|---|---|"
            cat /tmp/protokolle.txt
            echo ""
            echo "_Zuletzt aktualisiert: $(date '+%Y-%m-%d')_"
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

## Schritt 6: Copilot Coding Agent deaktivieren

> **Wichtig:** Ohne diese Einstellung übernimmt der Copilot Coding Agent Issues und verschiebt sie ins Kanban Board.

1. GitHub.com → Avatar → **Settings**
2. **Copilot** → **Coding agent**
3. **Repository access** → **"Selected repositories"**
4. `learn-wp-dach-team` **nicht** aufnehmen

---

## Schritt 7: Copilot-Training deaktivieren *(bei öffentlichem Repo)*

1. GitHub.com → Avatar → **Settings**
2. **Copilot** → **Features**
3. Abschnitt **Privacy** → **"Allow GitHub to use my data for AI model training"** → **Disabled**

> Bei privaten Repositories nicht zwingend nötig.

---

## Schritt 8: Teammitglieder einladen

Repository → **Settings** → **Collaborators** → **Add people**

Alle Teammitglieder brauchen einen GitHub-Account.

---

## Repository transferieren

Sobald der Zielort feststeht (z.B. DE-WordPress-GitHub):

Repository → **Settings** → **Danger Zone** → **Transfer ownership**

Folgendes bleibt vollständig erhalten:
- Alle Issues (inkl. Kommentare, Labels, Assignees)
- GitHub Projects / Kanban Board
- Labels, Milestones, Issue-Vorlagen
- Alle Links werden automatisch weitergeleitet
