---
title: OpenClaw - CLI AI Agent 安装配置
date: 2026-03-10
tags:
  - AI
  - Vibe-coding
  - CLI
  - Agent
---
## 前提
```
apt install mailcap xdg-utils
```

## 安装
```
curl -fsSL https://openclaw.ai/install.sh | bash
```

## 交互配置
```
The lobster has landed. Your terminal will never be the same.

· Starting setup


🦞 OpenClaw 2026.3.8 (3caab92) — One CLI to rule them all, and one more restart because you changed the port.

▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
██░▄▄▄░██░▄▄░██░▄▄▄██░▀██░██░▄▄▀██░████░▄▄▀██░███░██
██░███░██░▀▀░██░▄▄▄██░█░█░██░█████░████░▀▀░██░█░█░██
██░▀▀▀░██░█████░▀▀▀██░██▄░██░▀▀▄██░▀▀░█░██░██▄▀▄▀▄██
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
                  🦞 OPENCLAW 🦞                    
 
┌  OpenClaw onboarding
│
◇  Security ─────────────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│  Security warning — please read.                                                           │
│                                                                                            │
│  OpenClaw is a hobby project and still in beta. Expect sharp edges.                        │
│  By default, OpenClaw is a personal agent: one trusted operator boundary.                  │
│  This bot can read files and run actions if tools are enabled.                             │
│  A bad prompt can trick it into doing unsafe things.                                       │
│                                                                                            │
│  OpenClaw is not a hostile multi-tenant boundary by default.                               │
│  If multiple users can message one tool-enabled agent, they share that delegated tool      │
│  authority.                                                                                │
│                                                                                            │
│  If you’re not comfortable with security hardening and access control, don’t run           │
│  OpenClaw.                                                                                 │
│  Ask someone experienced to help before enabling tools or exposing it to the internet.     │
│                                                                                            │
│  Recommended baseline:                                                                     │
│  - Pairing/allowlists + mention gating.                                                    │
│  - Multi-user/shared inbox: split trust boundaries (separate gateway/credentials, ideally  │
│    separate OS users/hosts).                                                               │
│  - Sandbox + least-privilege tools.                                                        │
│  - Shared inboxes: isolate DM sessions (`session.dmScope: per-channel-peer`) and keep      │
│    tool access minimal.                                                                    │
│  - Keep secrets out of the agent’s reachable filesystem.                                   │
│  - Use the strongest available model for any bot with tools or untrusted inboxes.          │
│                                                                                            │
│  Run regularly:                                                                            │
│  openclaw security audit --deep                                                            │
│  openclaw security audit --fix                                                             │
│                                                                                            │
│  Must read: https://docs.openclaw.ai/gateway/security                                      │
│                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────╯
│
◇  I understand this is personal-by-default and shared/multi-user use requires lock-down. Continue?
│  Yes
│
◇  Onboarding mode
│  QuickStart
│
◇  QuickStart ─────────────────────────╮
│                                      │
│  Gateway port: 18789                 │
│  Gateway bind: Loopback (127.0.0.1)  │
│  Gateway auth: Token (default)       │
│  Tailscale exposure: Off             │
│  Direct to chat channels.            │
│                                      │
├──────────────────────────────────────╯
│
◇  Model/auth provider
│  Custom Provider （倒数第二项，自定义供应商）
│
◇  API Base URL
│  https://apis.iflow.cn/v1
│
◇  How do you want to provide this API key?
│  Paste API key now  （选择这一项）
│
◇  API Key (leave blank if not required)
│  sk-xxxx (粘贴api key)
│
◇  Endpoint compatibility
│  OpenAI-compatible （选择这一项）
│
◇  Model ID
│  qwen3-coder-plus （填写模型id）
│
◇  Verification successful.
│
◇  Endpoint ID
│  custom-apis-iflow-cn （默认不用改）
│
◇  Model alias (optional)
│  qwen （自定义）
Configured custom provider: custom-apis-iflow-cn/qwen3-coder-plus
│
◇  Channel status ────────────────────────────╮
│                                             │
│  Telegram: needs token                      │
│  WhatsApp (default): not linked             │
│  Discord: needs token                       │
│  Slack: needs tokens                        │
│  Signal: needs setup                        │
│  signal-cli: missing (signal-cli)           │
│  iMessage: needs setup                      │
│  imsg: missing (imsg)                       │
│  IRC: not configured                        │
│  Google Chat: not configured                │
│  LINE: not configured                       │
│  Feishu: install plugin to enable           │
│  Google Chat: install plugin to enable      │
│  Nostr: install plugin to enable            │
│  Microsoft Teams: install plugin to enable  │
│  Mattermost: install plugin to enable       │
│  Nextcloud Talk: install plugin to enable   │
│  Matrix: install plugin to enable           │
│  BlueBubbles: install plugin to enable      │
│  LINE: install plugin to enable             │
│  Zalo: install plugin to enable             │
│  Zalo Personal: install plugin to enable    │
│  Synology Chat: install plugin to enable    │
│  Tlon: install plugin to enable             │
│                                             │
├─────────────────────────────────────────────╯
│
◇  How channels work ───────────────────────────────────────────────────────────────────────╮
│                                                                                           │
│  DM security: default is pairing; unknown DMs get a pairing code.                         │
│  Approve with: openclaw pairing approve <channel> <code>                                  │
│  Public DMs require dmPolicy="open" + allowFrom=["*"].                                    │
│  Multi-user DMs: run: openclaw config set session.dmScope "per-channel-peer" (or          │
│  "per-account-channel-peer" for multi-account channels) to isolate sessions.              │
│  Docs: channels/pairing              │
│                                                                                           │
│  Telegram: simplest way to get started — register a bot with @BotFather and get going.    │
│  WhatsApp: works with your own number; recommend a separate phone + eSIM.                 │
│  Discord: very well supported right now.                                                  │
│  IRC: classic IRC networks with DM/channel routing and pairing controls.                  │
│  Google Chat: Google Workspace Chat app with HTTP webhook.                                │
│  Slack: supported (Socket Mode).                                                          │
│  Signal: signal-cli linked device; more setup (David Reagans: "Hop on Discord.").         │
│  iMessage: this is still a work in progress.                                              │
│  LINE: LINE Messaging API webhook bot.                                                    │
│  Feishu: 飞书/Lark enterprise messaging with doc/wiki/drive tools.                        │
│  Nostr: Decentralized protocol; encrypted DMs via NIP-04.                                 │
│  Microsoft Teams: Bot Framework; enterprise support.                                      │
│  Mattermost: self-hosted Slack-style chat; install the plugin to enable.                  │
│  Nextcloud Talk: Self-hosted chat via Nextcloud Talk webhook bots.                        │
│  Matrix: open protocol; install the plugin to enable.                                     │
│  BlueBubbles: iMessage via the BlueBubbles mac app + REST API.                            │
│  Zalo: Vietnam-focused messaging platform with Bot API.                                   │
│  Zalo Personal: Zalo personal account via QR code login.                                  │
│  Synology Chat: Connect your Synology NAS Chat to OpenClaw with full agent capabilities.  │
│  Tlon: decentralized messaging on Urbit; install the plugin to enable.                    │
│                                                                                           │
├───────────────────────────────────────────────────────────────────────────────────────────╯
│
◇  Select channel (QuickStart)
│  Skip for now
Updated ~/.openclaw/openclaw.json
Workspace OK: ~/.openclaw/workspace
Sessions OK: ~/.openclaw/agents/main/sessions
│
◇  Web search ────────────────────────────────────────╮
│                                                     │
│  Web search lets your agent look things up online.  │
│  Choose a provider and paste your API key.          │
│  Docs: https://docs.openclaw.ai/tools/web           │
│                                                     │
├─────────────────────────────────────────────────────╯
│
◇  Search provider
│  Skip for now
│
◇  Skills status ─────────────╮
│                             │
│  Eligible: 4                │
│  Missing requirements: 40   │
│  Unsupported on this OS: 7  │
│  Blocked by allowlist: 0    │
│                             │
├─────────────────────────────╯
│
◇  Configure skills now? (recommended)
│  No
│
◇  Hooks ──────────────────────────────────────────────────────────────────╮
│                                                                          │
│  Hooks let you automate actions when agent commands are issued.          │
│  Example: Save session context to memory when you issue /new or /reset.  │
│                                                                          │
│  Learn more: https://docs.openclaw.ai/automation/hooks                   │
│                                                                          │
├──────────────────────────────────────────────────────────────────────────╯
│
◇  Enable hooks?
│  Skip for now
Config overwrite: /root/.openclaw/openclaw.json (sha256 39aa6769dcc87ada89872047409f1d99d3f5ad5b93f9cd55f7e754a4ea510eae -> 0c754d9c9b62e5770935e4887508209fa8c19d6038ed59883979d1659ffc0cf1, backup=/root/.openclaw/openclaw.json.bak)
│
◇  Systemd ───────────────────────────────────────────────────────────────────────────────╮
│                                                                                         │
│  Systemd user services are unavailable. Skipping lingering checks and service install.  │
│                                                                                         │
├─────────────────────────────────────────────────────────────────────────────────────────╯

│

◇  
Health check failed: gateway closed (1006 abnormal closure (no close frame)): no close reason
  Gateway target: ws://127.0.0.1:18789
  Source: local loopback
  Config: /root/.openclaw/openclaw.json
  Bind: loopback
│
◇  Health check help ────────────────────────────────╮
│                                                    │
│  Docs:                                             │
│  https://docs.openclaw.ai/gateway/health           │
│  https://docs.openclaw.ai/gateway/troubleshooting  │
│                                                    │
├────────────────────────────────────────────────────╯
│
◇  Optional apps ────────────────────────╮
│                                        │
│  Add nodes for extra features:         │
│  - macOS app (system + notifications)  │
│  - iOS app (camera/canvas)             │
│  - Android app (camera/canvas)         │
│                                        │
├────────────────────────────────────────╯
│
◇  Control UI ───────────────────────────────────────────────────────────────────────────────╮
│                                                                                            │
│  Web UI: http://127.0.0.1:18789/                                                           │
│  Web UI (with token):                                                                      │
│  http://127.0.0.1:18789/#token=e1f1e2abc031c4a4a03f7d9d8735f4e963d4ef7011eb09b5            │
│  Gateway WS: ws://127.0.0.1:18789                                                          │
│  Gateway: not detected (gateway closed (1006 abnormal closure (no close frame)): no close  │
│  reason)                                                                                   │
│  Docs: https://docs.openclaw.ai/web/control-ui                                             │
│                                                                                            │
├────────────────────────────────────────────────────────────────────────────────────────────╯
│
◇  Workspace backup ────────────────────────────────────────╮
│                                                           │
│  Back up your agent workspace.                            │
│  Docs: https://docs.openclaw.ai/concepts/agent-workspace  │
│                                                           │
├───────────────────────────────────────────────────────────╯
│
◇  Security ──────────────────────────────────────────────────────╮
│                                                                 │
│  Running agents on your computer is risky — harden your setup:  │
│  https://docs.openclaw.ai/security                              │
│                                                                 │
├─────────────────────────────────────────────────────────────────╯
│
◇  Shell completion ────────────────────────────────────────────────────────╮
│                                                                           │
│  Shell completion installed. Restart your shell or run: source ~/.bashrc  │
│                                                                           │
├───────────────────────────────────────────────────────────────────────────╯
│
◇  Dashboard ready （重要，需要查看下方的token）────────────────────────────────────────────────────────────────╮
│                                                                                  │
│  Dashboard link (with token):                                                    │
│  http://127.0.0.1:18789/#token=e1f1e2abc031c4a4a03f7d9d8735f4e963d4ef7011eb09b5  │
│  Copy/paste this URL in a browser on this machine to control OpenClaw.           │
│  No GUI detected. Open from your computer:                                       │
│  ssh -N -L 18789:127.0.0.1:18789 root@<host>                                     │
│  Then open:                                                                      │
│  http://localhost:18789/                                                         │
│  http://localhost:18789/#token=e1f1e2abc031c4a4a03f7d9d8735f4e963d4ef7011eb09b5  │
│  Docs:                                                                           │
│  https://docs.openclaw.ai/gateway/remote                                         │
│  https://docs.openclaw.ai/web/control-ui                                         │
│                                                                                  │
├──────────────────────────────────────────────────────────────────────────────────╯
│
◇  Web search ───────────────────────────────────────╮
│                                                    │
│  Web search was skipped. You can enable it later:  │
│    openclaw configure --section web                │
│                                                    │
│  Docs: https://docs.openclaw.ai/tools/web          │
│                                                    │
├────────────────────────────────────────────────────╯
│
◇  What now ─────────────────────────────────────────────────────────────╮
│                                                                        │
│  What now: https://openclaw.ai/showcase ("What People Are Building").  │
│                                                                        │
├────────────────────────────────────────────────────────────────────────╯
│
└  Onboarding complete. Use the dashboard link above to control OpenClaw.

```

## 本地运行
### 端口转发
```
ssh -N -L 18789:127.0.0.1:18789 root@服务器ip
```
### 访问
```
http://localhost:18789/
http://localhost:18789/#token=e1f1e2abc031c4a4a03f7d9d8735f4e963d4ef7011eb09b5
```
