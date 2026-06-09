# Market Manager

![Status](https://img.shields.io/badge/status-in%20development-yellow)

> Event-driven supermarket operations management system — powered by Python, Flask, and smart badge devices (ESP).

## Overview

**Market Manager** is a modular backend application built with **Python + Flask** focused on retail operational automation. The system receives events from **ESP smart badge devices** and processes them to generate **automatic corrective actions** such as team notifications, response time tracking, and productivity analysis.

Communication is **event-driven**, with services decoupled across multiple layers for easy maintenance and scaling.

## Architecture

The system follows an **N-Tier + Event-Driven** architecture, composed of independent modules connected through the main entry point, which handles dependency injection between services. Each layer has well-defined responsibilities — ingestion, orchestration, persistence, interface, and analytics.

### Folder Structure

```
project_root/
│
├── src/
│   ├── ingest/                # Data ingestion and validation (entry point)
│   │   ├── api/               # HTTP listener for ESP device events
│   │   ├── ingest_controller/ # Controls the full flow depending on event type
│   │   ├── ingest_dispatcher/ # Sends requests upstream to the Orchestrator
│   │   ├── validation/        # ESP authentication and payload validation
│   │   └── errors/            # Error handling, messages, and retry logic
│   │
│   ├── orchestrator/          # Core processing and decision engine
│   │   ├── controller/        # Coordinates rules based on event type
│   │   ├── service/           # Business logic for processing controller requests
│   │   ├── dispatcher/        # Sends responses back to ESP devices
│   │   └── repository/        # DB connection, data persistence, and event logs
│   │
│   ├── admin_ui/              # Admin interface (management and logs)
│   ├── logs/                  # Event and metrics logging
│   ├── core/                  # Config, utilities, and environment variables
│   └── dashboards/            # Log-to-metrics transformation and visualization
│
└── test/                      # Unit and integration tests
```

## Tech Stack

- **Language:** Python 3.11+
- **Web Framework:** Flask
- **Database:** SQLite (dev) / PostgreSQL (prod)
- **Package Manager:** uv
- **Communication Protocol:** HTTP
- **Admin Interface:** React or Streamlit *(in development)*
- **Architecture:** N-Tier + Event-Driven

## Event Pipeline

```
ESP Device
  → [1] Event received (audio + image?)
  → [2] Ingest Service — validates and formats data
  → [3] Orchestrator/Controller — decides the action
  → [4] Orchestrator/Service — builds response payload
  → [5] Repository — validates and persists data
  → [6] Dispatcher — routes action to the right collaborator
  → [7] Logging — records event_id, actor, result
  → [8] Dashboard — converts logs into performance metrics
```

**Edge cases:**
- Event may arrive **without an image**.
- If audio processing fails, the event is saved as **incomplete** and flagged for retry.
- If the target device is offline, the dispatcher retries with configurable timeout.

## Getting Started

### Prerequisites

- [uv](https://docs.astral.sh/uv/)
- SQLite (development) or PostgreSQL (production)

### Installation

```bash
git clone https://github.com/Klein-Lucas/Market_Manager.git
cd Market_Manager

uv venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

uv sync
```

### Environment Configuration

Create a `.env` file inside `src/core/`:

```env
DB_URL=sqlite:///./database/dev.db
MAX_FILE_SIZE_MB=10
AUDIO_FOLDER=./data/audio
IMAGE_FOLDER=./data/images
```

### Run

```bash
uv run flask run
```

## Roadmap

- [ ] Complete Orchestrator layer
- [ ] Implement Admin UI (Streamlit or React)
- [ ] Add AI-powered log analysis for automatic insights
- [ ] Integrate camera monitoring with computer vision
- [ ] Expand to cover Purchasing, Receiving, and Cashier workflows
- [ ] Build fair and personalized performance metrics per collaborator

## License

MIT