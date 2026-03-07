---

Mini NanoBot

**Mini NanoBot** 是一个使用 Python 实现的轻量级 **LLM Agent 框架**，用于探索和实践现代 AI Agent 的核心架构设计。

项目实现了一个完整的 Agent 系统，包括：

* 大模型调用
* 工具调用（Tool Calling）
* Skill 插件系统
* MCP（Model Context Protocol）工具接入
* 对话记忆（Memory）
* 多渠道输入（CLI / 飞书）

该项目的目标是 **用最少的代码实现一个清晰、可扩展的 Agent 架构**，帮助理解 AI Agent 的核心工作机制。

---

# 项目特点

**模块化架构**

将 Agent 拆分为：

* Provider（模型提供者）
* Tool（工具系统）
* Skill（插件能力）
* MCP（远程工具）
* Memory（记忆系统）
* Channel（交互渠道）

各模块独立设计，方便扩展和维护。

---

**Skill 插件系统**

使用

```
skill.yaml + run.py
```

即可快速扩展 Agent 能力，无需修改核心代码。

---

**MCP 支持**

支持通过 **MCP（Model Context Protocol）** 接入远程工具服务器，实现：

* 动态加载工具
* 工具服务解耦
* 远程能力扩展

---

**多渠道支持**

当前支持：

* CLI 命令行聊天
* 飞书机器人

未来可扩展：

* Web
* Slack
* Telegram

---

# 系统架构

整体系统架构如下：

```
             用户
              │
              ▼
        Channel层
    (CLI / Feishu Bot)
              │
              ▼
            Agent
              │
   ┌──────────┼──────────┐
   │          │          │
   ▼          ▼          ▼
Provider    Tools      Memory
(LLM)      (工具系统)   (记忆系统)
   │
   │
   ▼
Skill Plugins
(YAML + Python)

   │
   ▼
 MCP Manager
   │
   ▼
MCP Server（远程工具）
```

Agent 作为核心调度模块，负责：

* 管理对话
* 调用模型
* 触发工具
* 处理工具结果
* 整合记忆

---

# Agent 工作流程

Agent 的一次完整运行流程如下：

```
用户输入
   │
   ▼
Channel 接收消息
   │
   ▼
Agent 生成 messages
(system prompt + memory + history)
   │
   ▼
调用 LLM Provider
   │
   ▼
模型返回响应
   │
   ├── 普通文本 → 直接返回用户
   │
   └── Tool Call
           │
           ▼
       ToolRegistry 查找工具
           │
           ▼
       执行 Tool.run()
           │
           ▼
       将 Tool 结果写入 session
           │
           ▼
       再次调用 LLM
```

该循环会持续执行，直到：

* 模型返回最终回答
* 或达到最大迭代次数

---

# MCP 工具调用流程

MCP（Model Context Protocol）用于接入远程工具服务器。

工作流程：

```
Agent
 │
 │ 请求工具列表
 ▼
MCP Client
 │
 ▼
MCP Server
 │
 │ 返回 tool schemas
 ▼
Agent ToolRegistry
 │
 │ 注册 MCPTool
 ▼
LLM 触发工具调用
 │
 ▼
MCP Client
 │
 ▼
远程 MCP Server
 │
 ▼
返回工具执行结果
 │
 ▼
Agent 继续推理
```

这种设计可以实现：

* 工具服务解耦
* 多 Agent 共享工具
* 远程能力扩展

---

# 项目目录结构

```
mini_nanobot/
│
├── core/
│   ├── agent.py           # Agent 核心逻辑
│   ├── response.py        # LLM 响应封装
│   ├── prompt_loader.py   # Prompt 模板加载
│   └── message.py         # Message / Session
│
├── channels/
│   ├── base.py            # Channel 接口
│   ├── cli.py             # CLI 聊天
│   └── feishu.py          # 飞书机器人
│
├── providers/
│   ├── base.py            # Provider 抽象类
│   └── zhipu.py           # 智谱AI实现
│
├── tools/
│   ├── base.py            # Tool 抽象类
│   ├── function_tool.py   # Function Tool
│   ├── registry.py        # Tool 注册中心
│   └── builtin/           # 内置工具
│
├── skills/
│   ├── loader.py          # Skill 加载器
│   ├── gold/              # 示例 Skill
│   └── weather/           # 天气 Skill
│       ├── skill.yaml
│       └── run.py
│
├── MCP/
│   ├── client.py          # MCP Client
│   ├── tool.py            # MCP Tool 封装
│   └── manager.py         # MCP 管理器
│
├── memory/
│   ├── base.py            # Memory 抽象
│   └── store.py           # 简单 Memory Store
│
├── templates/
│   └── mcp_server.py      # 示例 MCP Server
│
└── main.py                # 项目入口
```

---

# 快速开始

## 1 安装依赖

```
pip install -r requirements.txt
```

---

## 2 配置 API Key

例如使用智谱：

```
export ZHIPU_API_KEY=your_key
```

---

## 3 启动 CLI

```
python main.py
```

示例：

```
User: 北京天气怎么样？

Agent: 我帮你查询一下...

[调用 weather 工具]

Agent: 北京今天晴天，气温 26℃。
```

---

# 扩展能力

## 添加新 Tool

1. 继承 `Tool`
2. 实现 `run()`
3. 注册到 `ToolRegistry`

---

## 添加新 Skill

创建目录：

```
skills/my_skill
```

添加：

```
skill.yaml
run.py
```

即可自动加载。

---

## 添加新 Provider

实现：

```
providers/base.py
```

即可支持新的模型服务。

---

## 接入 MCP 工具服务器

在 `MCP Manager` 中添加服务器地址即可动态加载远程工具。

---

# 设计目标

Mini NanoBot 主要用于展示 **AI Agent 的核心架构设计**：

* 模块解耦
* 插件化能力
* 工具生态
* 可扩展性

代码尽量保持 **简单、清晰、易理解**，方便学习和扩展。

---

# License

MIT License

---

