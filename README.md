# LyfeOS

LyfeOS is a personal automation project focused on self-hosted workflows. The
`docs` directory contains a detailed guide for setting up the **Liberation
Stack** using n8n, Docker, and a Telegram bot.

For full installation instructions and workflow descriptions, see
[docs/liberation-stack-guide.md](docs/liberation-stack-guide.md).



## Quick Start

Copy `.env.example` to `.env` and fill in your secrets (see `docs/liberation-stack-guide.md` for variables) then run:

```bash
docker compose up -d
```

The `labs` directory contains helper scripts used by the NyxLab sidecar:

- `sentiment.py` – offline sentiment analysis
- `embed.py` – generate text embeddings
- `encrypt_tables.py` – nightly DuckDB encryption example
- `report.py` – simple weekly report generator
- `yubigate.go` – placeholder for YubiKey PR approval
