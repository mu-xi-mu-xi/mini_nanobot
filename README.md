---

# Mini NanoBot

A lightweight, extensible **LLM Agent framework** built in Python.

Mini NanoBot demonstrates how to build a modular AI agent from scratch with support for:

* Tool calling
* MCP (Model Context Protocol)
* Memory
* Skill plugins
* Multiple channels (CLI / Feishu)
* Provider abstraction

The goal of this project is to provide a **clear and minimal architecture** for learning how modern AI agents work.

---

# Features

* **LLM Provider abstraction**
  Easily integrate different model providers.

* **Tool system**
  Built-in tools and function-based tools.

* **Skill plugins**
  YAML + Python based skill definition.

* **MCP support**
  Connect to external MCP tool servers.

* **Memory system**
  Simple pluggable memory storage.

* **Prompt management**
  Prompt templates managed separately.

* **Multiple channels**

  * CLI
  * Feishu bot

---

# Project Structure

```
mini_nanobot/
│
├── core/
│   ├── agent.py           # Main agent logic
│   ├── response.py        # LLM response wrapper
│   ├── prompt_loader.py   # Prompt template loader
│   └── message.py         # Message and session classes
│
├── channels/
│   ├── base.py            # Channel interface
│   ├── cli.py             # CLI interface
│   └── feishu.py          # Feishu bot integration
│
├── providers/
│   ├── base.py            # LLM provider interface
│   └── zhipu.py           # ZhipuAI provider implementation
│
├── tools/
│   ├── base.py            # Tool base class
│   ├── function_tool.py   # Function-based tool wrapper
│   ├── registry.py        # Tool registry
│   └── builtin/           # Built-in tools
│
├── skills/
│   ├── loader.py          # Skill loader
│   ├── gold/              # Example skill
│   └── weather/           # Weather skill example
│       ├── skill.yaml
│       └── run.py
│
├── MCP/
│   ├── client.py          # MCP client
│   ├── tool.py            # MCP tool wrapper
│   └── manager.py         # MCP manager
│
├── memory/
│   ├── base.py            # Memory interface
│   └── store.py           # Simple memory store
│
├── templates/
│   └── mcp_server.py      # Example MCP server
│
└── main.py                # Application entry point
```

---

# Architecture Overview

The system is composed of several modular components:

```
User
 │
 ▼
Channel (CLI / Feishu)
 │
 ▼
Agent
 │
 ├── Provider (LLM)
 ├── Tools
 ├── Skills
 ├── Memory
 └── MCP Tools
```

The agent orchestrates interaction between the user, the LLM provider, and external tools.

---

# Core Components

## Agent

The `Agent` is responsible for:

* managing conversation session
* calling LLM providers
* handling tool calls
* integrating memory
* coordinating skills and MCP tools

---

## Providers

Providers abstract different LLM services.

Example:

```
providers/
 ├── base.py
 └── zhipu.py
```

Adding a new provider only requires implementing the provider interface.

---

## Tools

Tools allow the agent to interact with external functions.

Supported tool types:

* built-in tools
* function tools
* MCP remote tools

Example structure:

```
tools/
 ├── base.py
 ├── function_tool.py
 ├── registry.py
 └── builtin/
```

---

## Skills

Skills are lightweight plugins defined using:

* `skill.yaml`
* `run.py`

Example:

```
skills/weather/
 ├── skill.yaml
 └── run.py
```

This allows new capabilities to be added without modifying core code.

---

## MCP (Model Context Protocol)

The project includes a simple MCP client that can connect to external MCP servers and dynamically load tools.

Example structure:

```
MCP/
 ├── client.py
 ├── tool.py
 └── manager.py
```

A sample MCP server implementation is provided:

```
templates/mcp_server.py
```

---

## Memory

The memory system provides simple conversation memory storage.

```
memory/
 ├── base.py
 └── store.py
```

This can be extended to support vector databases or long-term memory systems.

---

# Getting Started

## 1 Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2 Configure provider

Set your LLM API key (example for ZhipuAI):

```bash
export ZHIPU_API_KEY=your_api_key
```

---

## 3 Run the CLI agent

```bash
python main.py
```

You should now be able to chat with NanoBot in the terminal.

---

# Example Interaction

```
User: What's the weather in Beijing?

Agent: Let me check that for you...

[Tool: weather]

Agent: The weather in Beijing is sunny.
```

---

# Extending NanoBot

## Add a new tool

1. Create a tool implementation
2. Register it in `ToolRegistry`

---

## Add a new skill

Create a new folder:

```
skills/my_skill/
```

Add:

```
skill.yaml
run.py
```

---

## Add a new provider

Implement the provider interface:

```
providers/base.py
```

---

## Connect an MCP server

Add a new MCP server URL to the MCP manager.

The agent will automatically load remote tools.

---

# Design Goals

Mini NanoBot aims to demonstrate a clean architecture for LLM agents:

* simple
* modular
* extensible
* easy to understand

The codebase intentionally avoids heavy frameworks to help developers learn the underlying mechanisms of AI agents.

---

# License

MIT License

---

如果你愿意，我还可以帮你 **把 README 再升级成一个更“GitHub 爆款风格”的版本**，会增加：

* 架构图
* Agent workflow 图
* MCP 工作流程图
* 示例 GIF
* 技术亮点

