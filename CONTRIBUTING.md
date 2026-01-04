# Contributing Guidelines

Thank you for your interest in contributing to this project.  
This repository is maintained in my spare time, so please understand that response times for
issues and pull requests may vary.

The goal of this project is to provide a clean, minimal, and reproducible Python 3 / PySide6
examples for Windows, Linux and Raspberry Pi. Contributions are welcome as long as they align with
that goal.

---

## Supported platforms

This project exclusively supports:
- Windows (x64)
- Linux (x86_64 and ARM, including Raspberry Pi OS)

Other platforms, including macOS, are not supported. Pull requests aimed at adding support for 
unsupported platforms will be closed without further review.

## 🐞 Reporting Issues

Before opening an issue, please:

1. Make sure you are using the latest version of the repository.
2. Check whether the issue already exists.

When reporting a bug, **a complete and minimal testcase is required**.  

Minimal testcases help ensure issues can be reproduced and fixed efficiently.

A good testcase includes:

- A clear description of the problem  
- The expected behavior  
- The actual behavior  
- A minimal code snippet or steps to reproduce  
- Your environment details:
  - Output of `pip freeze`, including::
    - Python version
    - PySide6 version
  - Windows/Linux/Raspberry OS version
  - VSCode or PyCharm version

Issues without a reproducible testcase may be closed without investigation.

---

## 🔧 Accepted Pull Requests

Pull requests are welcome, but please follow these guidelines:

- Keep PRs focused and easy to review.
- Avoid large refactors, formatting-only changes, or unrelated modifications.
- Explain the purpose of the change clearly.
- Ensure the project still executes cleanly on Windows and Linux.

If your PR fixes a bug, include the testcase in the PR description.

### Not Accepted Pull Requests

- No deployment tooling
- No macOS support
- No type‑hint‑only refactors
- No formatting‑only PRs
- No new external dependencies or submodules

---

## 🎯 Project Scope

This project intentionally aims to be:

- Minimal  
- Reproducible  
- Windows/Linux/RaspberryPi OS focused  
- Free of submodules  
- Free of external dependencies  

Contributions that add complexity, multi-platform layers, or unnecessary abstractions are unlikely
to be accepted.

---

## 🙏 Thank You

Even if I cannot respond immediately, contributions, ideas, and improvements are appreciated.
