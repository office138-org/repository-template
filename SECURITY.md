# Security Policy

## Reporting

Do not disclose secrets, credentials, private runtime evidence, or sensitive customer information in public issues or pull requests.

For a suspected security issue, notify the repository owner privately and provide the minimum evidence necessary to reproduce the problem.

## Repository safety baseline

The standard CI rejects common sensitive tracked paths such as `.env`, private key files, password files, `runs.jsonl`, and `docs/exports/` artifacts.

Never weaken or bypass repository-safety checks to make CI pass.
