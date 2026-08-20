# AI Coding Exam Skills

Open-source skills for AI-assisted coding exams and project-based technical assessments.

面向 AI Coding 笔试的开源 Skills。帮助候选人从长需求中锁定验收契约，使用规范驱动开发拆解任务，并通过明确 Prompt、攻击性测试、最小修复和版本 checkpoint 驾驭能力较弱的考场模型。

> 本项目仅适用于明确允许使用 AI 辅助工具的考试、训练和面试场景。

## v0.1.0

首个版本提供 `prompt-solving`：

- 从 README、题面或现有仓库提取环境、契约、规则和验收清单
- 建立 `spec.md`、`design.md`、`tasks.md` 规范工件
- 规划最小可运行纵向主链
- 为能力较弱的 Coding 模型生成单轮、窄范围、可验证 Prompt
- 主动识别模型擅自改名、扩大范围、破坏既有逻辑等错误
- 让模型先写测试攻击当前实现，再根据完整失败输出做最小修复
- 执行失败用例、边界用例和全量回归
- 使用稳定 checkpoint、干净上下文和提交前契约审计控制风险

暂不包含模拟笔试项目、自动评分器或强模型 Judge。这些能力计划在后续版本单独设计。

## 工作流

```text
阅读题面
  -> 锁定精确契约
  -> 建立 SDD 规范
  -> 拆分可验收功能块
  -> 跑通最小主链
  -> 生成攻击性测试
  -> 最小修复并回归
  -> 保存稳定 checkpoint
  -> 提交前逐项验收
```

## 安装

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

## 使用

```text
Use $prompt-solving to analyze this AI Coding exam task and guide the coding model through implementation, testing, and correction.
```

中文示例：

```text
使用 $prompt-solving 阅读当前 README，先不要写代码。提取硬约束、验收标准和隐藏测试风险，再给我第一轮可以发给考场模型的 Prompt。
```

Skill 支持三种模式：

- **Direct**：能够访问仓库时直接分析、修改和验证
- **Relay**：候选人在另一个窗口操作弱模型，Skill 每轮提供一个可复制 Prompt
- **Analysis**：只蒸馏题目、解法、失败模式、Prompt 和测试，不修改代码

## 第一批题型

- 多端状态机与订单系统
- 网页数据清洗管线
- LLM 批量推理控制台
- 异构 Excel 账单解析
- 内存态治理、预算与幂等服务
- 安全漏洞审计与最小修复

这些内容是可迁移的训练模式，不是任何公司的官方题库或标准答案。实际字段、路由、状态码和边界始终以当场题面为准。

## 项目结构

```text
ai-coding-exam-skills/
├── skills/
│   └── prompt-solving/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
├── references/              # 研究材料与来源记录
├── scripts/                 # 仓库校验工具
└── .github/workflows/       # 持续校验
```

## 验证

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

## 贡献

欢迎提交新的公开题型、失败案例、Prompt 模板和测试策略。请先阅读 [CONTRIBUTING.md](CONTRIBUTING.md)，不得提交保密题面、个人信息或违反考试规则获得的材料。

## License

[MIT](LICENSE)

