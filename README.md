# Deadline-Notifier

---

A smart, zero-config service that watches your Gmail for deadlines or scheduled events and instantly creates Google Calendar entries via Composio + LangChain.

## Features

* 🤖 **Automated triggers** – uses Composio MCP to fire on every new Gmail message
* 📧 **Deadline extraction** – LLM agent identifies dates/times in your email body
* 📅 **Calendar integration** – automatically creates a Google Calendar event when a deadline or meeting is found
* 🔧 **One-step run scripts** –

  * `runserver.py` to bootstrap MCP connection
  * `run_code.py` to spin up your FastAPI webhook


## Quickstart

### 1. Clone & install

```bash
git clone https://github.com/your-org/deadline-notifier.git
cd deadline-notifier
pip install -r requirements.txt
```

### 2. Configure your API keys

Create a `.env` in the project root:

```dotenv
COMPOSIO_API_KEY=your_composio_key
```

### 3. Enable the Gmail trigger

```bash
python mcp_client.py
# You should see: "enabled"
```

### 4. Run your server & expose via ngrok

**Step A :**

```bash
# Start your webhook & ngrok in separate terminals
ngrok http 8000
```

1. Copy the `https://…ngrok.io` URL.
2. Paste it into your Composio dashboard under your Gmail trigger’s “webhook URL.”
3. Restart `python run_code.py`.

**Step B :**

```bash
python run_code.py
```

### 5. Send yourself a test email

Include a phrase like:

> “Let’s meet March 14 at 3 PM to review the Q1 plan.”

Within seconds you’ll see in your console:

```
[MCP] { … }
[APP] 📧 Message ID: abc123…
[APP] Event created successfully on Google Calendar
```

## File Overview

* **app.py** — FastAPI webhook that listens for Gmail-new-message events
* **gmail\_service.py** — LangChain agent to fetch & parse email content
* **calendar\_service.py** — LangChain agent to create Google Calendar events
* **mcp\_client.py** — Enables the Gmail trigger in your Composio entity
* **runserver.py** — Convenience script: runs `mcp_client.py` then `ngrok http 8000`
* **run\_code.py** — Convenience script: runs `uvicorn` on your FastAPI app

