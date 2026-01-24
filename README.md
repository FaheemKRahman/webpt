# Web Application Vulnerability Scanner

## Overview

This project is a **web application penetration testing tool** designed to go beyond simply running automated scanners.  
Instead of relying on external tools, this scanner demonstrates **how common web vulnerabilities can be identified programmatically** by crawling a target application, analysing its attack surface, and actively testing for security flaws.

The goal of this project is both **educational** and **practical**:
- To understand how real-world vulnerability scanners work internally
- To showcase security engineering, automation, and documentation skills

---

## Problem Statement

Modern web applications often contain vulnerabilities such as:

- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)

While many automated tools exist, they are often treated as **black boxes**, making it difficult for junior security professionals to understand:
- How vulnerabilities are actually discovered
- Why false positives occur
- How findings should be prioritised and reported

This project addresses that gap by implementing a **transparent, modular scanner** that clearly shows each step of the testing process.

---

## What This Tool Solves

This tool:

- Automatically discovers pages and forms in a web application
- Identifies potential input points attackers can abuse
- Tests for common web vulnerabilities
- Assigns severity scores to findings
- Generates a structured vulnerability report with remediation guidance

It helps demonstrate **how an attacker thinks**, while also producing output that resembles **real penetration testing reports**.

---

## How the Tool Works

The scanner follows a structured, multi-stage workflow:

### Crawling
- Starts from a target URL
- Crawls internal links to discover additional pages
- Builds a list of reachable URLs within the application

### Form Discovery
- Parses each discovered page
- Identifies HTML forms and their input fields
- Treats forms as the primary attack surface

### Vulnerability Testing
Each discovered form is tested using dedicated scanner modules:

#### SQL Injection
- Attempts basic injection payloads
- Compares responses to identify anomalous behaviour

#### Reflected XSS
- Injects JavaScript payloads into inputs
- Checks for reflection in responses

#### CSRF
- Checks for missing or weak CSRF protections
- Flags forms without anti-CSRF tokens

Each scanner module is isolated and independent, making the system easy to extend.

---

### Severity Scoring
- Each finding is assigned:
  - A severity level (Low / Medium / High)
  - A numeric risk score
- Findings are prioritised based on potential impact

---

###  Report Generation
- All findings are consolidated into a single report
- The report includes:
  - Vulnerability type
  - Affected URL and parameter
  - Evidence
  - Impact explanation
  - Remediation recommendations
- Findings are ordered by severity to reflect real-world pentest reports

---

## Architecture & Design

The tool is intentionally designed to be **modular**:

Each component has a single responsibility:

- `crawler.py` → URL discovery  
- `form_parser.py` → Attack surface identification  
- `scanners/` → Vulnerability detection  
- `severity.py` → Risk scoring  
- `report.py` → Output generation  

This mirrors the architecture of professional security tools and allows easy future expansion.

---

## Technologies Used

- **Python 3**
- `requests` – HTTP communication
- `BeautifulSoup` – HTML parsing
- `json` – Structured reporting

No external scanning frameworks are used — everything is implemented from scratch to maximise learning.

---

## Business Value

From a business and security perspective, this tool demonstrates:

- **Early vulnerability discovery**  
  Identifying issues before deployment reduces breach risk and remediation cost.

- **Risk prioritisation**  
  Severity scoring helps teams focus on the most critical issues first.

- **Actionable remediation guidance**  
  Findings include clear recommendations, reducing back-and-forth between security and development teams.

- **Security awareness**  
  Helps developers and stakeholders understand how vulnerabilities arise and why they matter.

Although not intended to replace commercial scanners, this tool reflects the **core logic used by professional penetration testing tools**.

---

## Future Improvements

Planned enhancements include:

- False-positive reduction using baseline response analysis
- Stored XSS detection
- Authentication-aware scanning
- HTML and PDF report generation
- Command-line interface (CLI)
- Rate limiting and crawl depth controls

---

## Disclaimer

This tool is intended **for educational and authorised testing only**.  
Only scan applications you own or have explicit permission to test.

---

## Author

Built as a learning and portfolio project to develop hands-on skills in:

- Web security
- Penetration testing
- Security tooling
- Technical documentation


