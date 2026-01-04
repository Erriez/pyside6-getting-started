# Security Policy

## Supported Versions
This project is a simple Python 3 / PySide6 example application with no external runtime 
dependencies. It is maintained on a best‑effort basis.

| Version | Supported |
|---------|-----------|
| main    | ✔ Active (best effort) |

## Security Model
This project has a minimal security surface. Specifically:

- It contains only local Python and PySide6 UI logic.
- It does **not** perform network communication.
- It does **not** depend on third‑party packages beyond PySide6.
- It does **not** execute dynamic or untrusted code.
- It does **not** store or process sensitive data.
- It is intended for local development, experimentation, and learning.
- **Creating standalone executables or deployment packages (e.g., via PyInstaller,
  Nuitka, cx_Freeze, or similar tools) is outside the scope of this project.**

As a result, the likelihood of security vulnerabilities is low.

## Reporting a Vulnerability
This project does **not** provide a private or confidential reporting channel.

If you believe you have found a security issue, please open a **public GitHub Issue**.
Do **not** include sensitive information in your report, as all issues are visible to the public.

A helpful report includes:

- A clear description of the issue  
- Steps to reproduce  
- Expected vs. actual behavior  
- Any relevant context or impact assessment  

Reports will be reviewed and addressed on a best‑effort basis. Response time of the developer may
vary.

## Contribution Guidelines
When contributing to this project, please ensure that:

- No unnecessary external dependencies are introduced  
- No network or remote‑execution features are added  
- Code follows Python best practices and avoids unsafe patterns  
- UI logic remains deterministic and local  
- **No executable‑packaging or deployment tooling is added**  

## Disclosure Policy
- All vulnerability reports are handled publicly via GitHub Issues.  
- Confirmed issues will be fixed as appropriate.  
- This project does **not** participate in the CVE assignment process.  
