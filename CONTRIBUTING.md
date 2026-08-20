# Contributing

感谢参与 AI Coding Exam Skills。

## 可以贡献什么

- 可公开验证的 AI Coding 工程题型
- 低能力模型的真实失败模式和纠偏 Prompt
- 边界测试、协议测试和回归策略
- SDD、时间管理和版本 checkpoint 实践
- 文档修正和跨平台兼容改进

## 内容边界

- 不提交受保密协议、考试规则或版权限制保护的完整题面。
- 不提交候选人姓名、账号、录屏、Token、密钥或其他个人信息。
- 不将个人复盘描述为企业官方规则或固定题库。
- 所有 Prompt 和案例必须服务于明确允许 AI 辅助的场景。
- 尽量抽象可迁移方法，不围绕泄露隐藏答案进行优化。

## 修改 Skill

1. 保持 `SKILL.md` 精简，详细题型和模板放入 `references/`。
2. 新参考文件应从 `SKILL.md` 直接链接，不创建多层引用链。
3. 超过 100 行的参考文件应包含目录。
4. 不在 Skill 目录中添加 README、CHANGELOG 或安装文档。
5. Frontmatter 只包含 `name` 和 `description`。

## 提交前验证

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate_skills.py
```

提交说明应简洁描述行为变化，例如：

```text
docs: add state-machine failure patterns
feat: add contract audit prompt
fix: preserve passed tests during repair loop
```

