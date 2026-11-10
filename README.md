<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="Lunga Ngaka, aspiring SOC analyst. A terminal shows ATT&CK-mapped alerts from soc-log-triage." src="assets/banner-dark.svg" width="100%">
</picture>

<p align="center">
  <a href="https://www.linkedin.com/in/lunga-ngaka-22132b35b"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Lunga%20Ngaka-0A66C2?style=flat-square&logo=linkedin&logoColor=white"></a>
  <img alt="Location" src="https://img.shields.io/badge/Johannesburg-South%20Africa-2ea043?style=flat-square&logo=googlemaps&logoColor=white">
  <img alt="Open to" src="https://img.shields.io/badge/Open%20to-SOC%20Analyst%20roles-8957e5?style=flat-square">
</p>

## About me

I'm a Computer Science student at the University of Fort Hare working towards a **SOC Analyst** role. I learn security by building the tools an analyst uses: detection rules, log parsers and triage reports, each tested against realistic attack data and documented with its blind spots.

- **Focus:** detection engineering, log analysis, incident triage and Windows / Active Directory attacks
- **How I work:** every detection is mapped to MITRE ATT&CK, has tests for what it should *and should not* catch, and runs in CI
- **Now learning:** Elastic Stack, Kerberos attack paths, and writing detections as Sigma rules

## Featured security projects

<table>
<tr>
<td width="50%" valign="top">

### [soc-log-triage](https://github.com/1ungaka/soc-log-triage)
Turns Linux `auth.log` / auditd, Windows Security, Sysmon, domain controller and web server logs into **ATT&CK-mapped alerts**. Detects brute force, password spraying, Kerberoasting, AS-REP roasting, encoded PowerShell, Office macros spawning shells, backdoor admins, log clearing, web path traversal and scanning.

`16 detections` `131 tests` `Sigma rules validated in CI`

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Sigma](https://img.shields.io/badge/-Sigma-1f6feb?style=flat-square) ![MITRE ATT&CK](https://img.shields.io/badge/-MITRE%20ATT%26CK-c62828?style=flat-square)

</td>
<td width="50%" valign="top">

### [phishing-analyser](https://github.com/1ungaka/phishing-analyser)
Analyses suspicious `.eml` files and explains every point of its 0 to 100 risk score: SPF / DKIM / DMARC verdicts, lookalike and homoglyph domains (including South African banks and SARS), deceptive links, risky attachments and social engineering language.

`web app + CLI` `explainable scoring`

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Email security](https://img.shields.io/badge/-Email%20security-6e40c9?style=flat-square)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### [statistical-baseline-alerting](https://github.com/1ungaka/statistical-baseline-alerting)
Finds anomalous login behaviour with **statistics instead of signatures**: z-scores and IQR fences on hourly event volume, failures and unique source IPs, combined into a severity-ranked alert queue in an interactive dashboard.

`anomaly detection` `no threat feeds needed`

![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

</td>
<td width="50%" valign="top">

### [AfriSafety](https://github.com/1ungaka/AfriSafety)
A privacy-first safety and location-sharing app for South Africa. Locations are **end-to-end encrypted** with libsodium, so the server cannot see where anyone is, and access is enforced with Postgres row-level security.

`privacy by design` `E2E encryption`

![Flutter](https://img.shields.io/badge/-Flutter-02569B?style=flat-square&logo=flutter&logoColor=white) ![Supabase](https://img.shields.io/badge/-Supabase-3ECF8E?style=flat-square&logo=supabase&logoColor=white)

</td>
</tr>
</table>

## Detection coverage

What my detections in [soc-log-triage](https://github.com/1ungaka/soc-log-triage) cover, by ATT&CK tactic (ATT&CK v20.1):

| Tactic | Techniques I detect |
|---|---|
| Reconnaissance | T1595.002 Vulnerability Scanning · T1595.003 Wordlist Scanning |
| Initial Access | T1566.001 Spearphishing Attachment · T1190 Exploit Public-Facing Application |
| Execution | T1059.001 PowerShell · T1204.002 Malicious File |
| Persistence | T1136.001 Create Local Account · T1098 Account Manipulation |
| Privilege Escalation | T1098 Account Manipulation (privileged groups) |
| Stealth | T1027 Obfuscated Files or Information |
| Defense Impairment | T1685.005 Clear Windows Event Logs |
| Credential Access | T1110.001 Password Guessing · T1110.003 Password Spraying · T1558.003 Kerberoasting · T1558.004 AS-REP Roasting |
| Command and Control | T1105 Ingress Tool Transfer · T1071.001 Web Protocols |

## Toolkit

**Security** &nbsp; ![MITRE ATT&CK](https://img.shields.io/badge/MITRE%20ATT%26CK-c62828?style=flat-square) ![Sigma](https://img.shields.io/badge/Sigma-1f6feb?style=flat-square) ![Sysmon](https://img.shields.io/badge/Sysmon-0078D4?style=flat-square&logo=windows&logoColor=white) ![Elastic Stack](https://img.shields.io/badge/Elastic%20Stack-005571?style=flat-square&logo=elastic&logoColor=white) ![Microsoft Azure](https://img.shields.io/badge/Microsoft%20Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white)

**Languages** &nbsp; ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white) ![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black) ![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white) ![Dart](https://img.shields.io/badge/Dart-0175C2?style=flat-square&logo=dart&logoColor=white)

**Data & tooling** &nbsp; ![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black) ![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white) ![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)

## Certifications in progress

![CompTIA Security+, in progress](https://img.shields.io/badge/CompTIA%20Security%2B-in%20progress-C8202F?style=for-the-badge) ![Microsoft AZ-900, in progress](https://img.shields.io/badge/Microsoft%20AZ--900-in%20progress-0078D4?style=for-the-badge&logo=microsoftazure&logoColor=white)

Studying for CompTIA Security+ and Microsoft Azure Fundamentals (AZ-900).

## Beyond security

I also enjoy reproducible data work: a [probabilistic forecast of hung councils](https://github.com/1ungaka/za-metro-councils-2026) in five South African metros for the 2026 local elections, and a [pre-registered audit](https://github.com/1ungaka/ec-lge2026-scenario-audit) of how well election scenarios predicted Eastern Cape results.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/1ungaka/1ungaka/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/1ungaka/1ungaka/output/github-snake.svg">
  <img alt="Animation of my GitHub contribution graph" src="https://raw.githubusercontent.com/1ungaka/1ungaka/output/github-snake.svg" width="100%">
</picture>
