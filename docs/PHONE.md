# Contribute from your phone

Work directly in a ChatGPT conversation from your phone, including with ChatGPT Pro. Claude and Codex offer GitHub connection options too.

## 1. Join

[Request contributor access](../CONTRIBUTING.md#join-and-start), then accept the GitHub invitation to GettysburgResearch.

## 2. Connect

In ChatGPT or Claude, install or connect the GitHub plugin/connector and sign in with the GitHub account you used to join. You can ask your assistant to help you connect it.

Direct connection links: [ChatGPT/Codex](https://github.com/apps/chatgpt-codex-connector/installations/select_target) · [Claude](https://github.com/apps/claude/installations/select_target).

If prompted, choose GettysburgResearch. The organization's existing installation may already cover the repositories, so you may not need to select them again.

## 3. Test and contribute

Start a new chat and try:

```text
Open GettysburgResearch/riemann and read README.md, AGENTS.md and
CONTRIBUTING.md from main. Tell me which commit you read.
Work on [my question], checking relevant work and overlapping PRs.
Use a new branch, state the contribution's status and checks actually run,
and open a draft PR. Return its link and commit SHA.
```

Open the returned PR link to check your contribution. Explore your own idea, review a result, run computations to discover mechanisms, or ask your agent to suggest a starting point. See [shared review](REVIEWING.md) when you're ready for feedback.

<details>
<summary>Connection trouble?</summary>

Confirm you're connected with the GitHub account that joined the organization. If access needs approval, ask a maintainer to check the app's repository access under organization Settings → Third-party Access → GitHub Apps; OAuth app approval is a separate setting. A working read does not establish write access: if your connection cannot create a PR, use an authoring environment such as Codex or Claude Code with authenticated Git/GitHub CLI access.

[ChatGPT plugin help](https://learn.chatgpt.com/docs/plugins) · [Claude GitHub help](https://support.claude.com/en/articles/10167454-use-the-github-integration).

</details>
