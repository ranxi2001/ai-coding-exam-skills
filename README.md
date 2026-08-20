# AI Coding Exam Skills

[![Validate Skills](https://github.com/ranxi2001/ai-coding-exam-skills/actions/workflows/validate.yml/badge.svg)](https://github.com/ranxi2001/ai-coding-exam-skills/actions/workflows/validate.yml)
[![Release](https://img.shields.io/github/v/release/ranxi2001/ai-coding-exam-skills)](https://github.com/ranxi2001/ai-coding-exam-skills/releases)
[![License](https://img.shields.io/github/license/ranxi2001/ai-coding-exam-skills)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ranxi2001/ai-coding-exam-skills?style=flat)](https://github.com/ranxi2001/ai-coding-exam-skills/stargazers)

**面向 AI Coding 笔试和工程型技术评测的开源 Skills。**

[English README](README_EN.md) · [Latest Release](https://github.com/ranxi2001/ai-coding-exam-skills/releases/latest) · [Issues](https://github.com/ranxi2001/ai-coding-exam-skills/issues)

AI Coding Exam Skills 把一份长 README 变成可执行的工程交付流程：锁定契约，建立 SDD 规范，分解最小主链，指导能力较弱的 Coding 模型逐轮实现，用攻击性测试暴露问题，再以最小修复和回归测试收口。

> 仅用于明确允许 AI 辅助的考试、训练和面试场景。本项目不提供任何公司的官方题库、隐藏用例或内部评分规则。

## Why

AI Coding 笔试考察的不只是“能否生成代码”，还包括：

- 从需求文档提取精确验收标准
- 在时间限制内做出合理的范围取舍
- 让模型遵守字段、状态、接口和错误契约
- 设计能攻击当前实现的边界测试
- 根据真实失败日志进行小范围修复和回归
- 保留稳定版本，并能解释自己的工程决策

## What's Included

### `prompt-solving`

当前唯一发布的 Skill，支持三种工作模式：

| Mode | 适用场景 |
| --- | --- |
| **Direct** | 能直接访问题目仓库，由 Agent 分析、修改和验证代码 |
| **Relay** | 候选人在另一个窗口操作弱模型，每轮获得一个可复制 Prompt |
| **Analysis** | 只蒸馏题目、解法、失败模式、测试和 Prompt，不修改代码 |

内置参考覆盖：

- 多端状态机与订单系统
- 网页数据清洗管线
- LLM 批量推理控制台
- 异构 Excel 账单解析
- 内存态治理、预算与幂等服务
- 安全漏洞审计与最小修复

## Core Workflow

```text
Read the task
    -> Lock the exact contract
    -> Create SDD artifacts
    -> Plan a minimal vertical slice
    -> Implement one verifiable block
    -> Generate adversarial tests
    -> Apply the smallest valid fix
    -> Run regression checks
    -> Save a stable checkpoint
    -> Audit the final delivery
```

核心原则：**规范先行、一次一件事、测试与实现分离、证据优先、可回滚交付。**

## Quick Start

```bash
git clone https://github.com/ranxi2001/ai-coding-exam-skills.git
cd ai-coding-exam-skills
```

安装到 Codex 用户级 Skills：

```bash
cp -R skills/prompt-solving ~/.codex/skills/prompt-solving
```

安装到 Claude Code 用户级 Skills：

```bash
cp -R skills/prompt-solving ~/.claude/skills/prompt-solving
```

也可以将 `skills/prompt-solving` 放入对应工具支持的项目级 Skill 目录。

## Use It

显式调用：

```text
Use $prompt-solving to analyze this AI Coding exam task and guide the coding model through implementation, testing, and correction.
```

中文示例：

```text
使用 $prompt-solving 阅读当前 README，先不要写代码。提取硬约束、验收标准和隐藏测试风险，再给我第一轮可以发给考场模型的 Prompt。
```

Relay 模式下，每一轮都会保持如下结构，方便直接复制到考场模型：

```text
Current phase:
Observed evidence:
Likely mistake or risk:
Prompt to send next:
[one copy-ready prompt]
Expected proof:
Rollback condition:
```

## Repository Map

```text
ai-coding-exam-skills/
├── skills/
│   └── prompt-solving/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
├── references/              # Research notes and source records
├── scripts/                 # Local repository checks
└── .github/workflows/       # CI validation
```

## Validate Locally

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

CI also runs the official Skill validator and the repository reference checks on every push and pull request.

## Roadmap

- [x] `prompt-solving` v0.1.0
- [ ] More distilled engineering question patterns
- [ ] Reusable task-spec and test-case templates
- [ ] `mock-coding-exam` project for local practice
- [ ] Optional strong-model Judge and trajectory scoring

模拟笔试项目和 Judge 不属于当前版本，避免在解题 Skill 尚未稳定前过早引入执行环境和评分复杂度。

## Contributing

欢迎提交公开题型、低能力模型失败案例、Prompt 模板、边界测试和文档改进。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)：不要提交保密题面、隐藏答案、个人信息、Token 或密钥，也不要把个人复盘表述为企业官方规则。

## License

[MIT](LICENSE) © 2026 ranxi2001

