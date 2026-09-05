# Contribute from your phone

You can use ChatGPT's connected GitHub tools to read the project and prepare contributions from your phone. You do not need a local checkout for that workflow. Running experiments or Lean checks additionally needs an available execution environment.

**Walkthrough status:** prepared for the project maintainer's phone check. The maintainer reports using the organization connection route below; this written walkthrough has not yet been tested end to end. Button names and available actions can vary by account and app version.

## 1. Get repository access

Follow [Join and start](../CONTRIBUTING.md#join-and-start). For the direct organization workflow, accept your GitHub invitation and make sure you can open [GettysburgResearch/riemann](https://github.com/GettysburgResearch/riemann) while signed in to the intended GitHub account.

When the repository is public, reading it and contributing through a fork do not require organization membership. Membership is the convenient route for shared repository branches.

## 2. Connect GitHub in ChatGPT

1. In ChatGPT on your phone, find the GitHub plugin or connection, install it if needed, and complete the GitHub connection prompt. Use the same GitHub account that has repository access.
2. Open the project's [GitHub connector installation selector](https://github.com/apps/chatgpt-codex-connector/installations/select_target). Choose GettysburgResearch if offered, then follow the available authorization or repository access steps.
3. If GitHub asks for organization-owner approval, submit the request and let a maintainer handle it. An ordinary member may not be able to install or change an organization app. Organization installation and your personal connection are separate; joining the organization alone does not finish both.
4. Return to ChatGPT and start a new chat with GitHub tools available. Confirm that the repository is accessible before asking for a write.

The organization currently has the connector installed for all its repositories. That installation does not grant a person access they do not otherwise have. If you cannot see the repository, check the GitHub account, accepted invitation, personal connection, and organization approval before reinstalling anything.

Reference: [ChatGPT plugins, including mobile availability](https://learn.chatgpt.com/docs/plugins) and [GitHub app installation and authorization](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party).

## 3. Check the connection

Paste this into a new chat:

```text
Use the connected GitHub tools to open GettysburgResearch/riemann.
Read README.md, AGENTS.md, and CONTRIBUTING.md from main.
Tell me the main commit you read, summarize one research direction,
and identify one small contribution I could make. Do not change files yet.
If you cannot access the repository, say which capability is missing.
```

If it cannot read the repository, complete the connection steps above. If it can read but cannot create branches or PRs, the connected tool may be read-only or lack the necessary authorization. Use the available GitHub/Codex environment with write tools, or save the proposed contribution and submit it through GitHub's web interface. Do not assume that a chat saying it created a PR is enough: open the returned PR link.

## 4. Make your first contribution

Choose the question yourself, or select one suggested in the first chat. Then adapt this prompt:

```text
Work on [my question] in GettysburgResearch/riemann.
Read the relevant program files and check overlapping open PRs.
Follow AGENTS.md and CONTRIBUTING.md. Use a new branch for this task.
Prepare a small research note, counterexample, literature connection,
or review. State its status, scope, exact dependencies, what was
actually run, and smallest remaining gap. Distinguish conjecture,
proof, and numerical evidence. Do not invent execution results.
Open a PR against main and give me its link and commit SHA.
Leave main and other contributors' branches to the integrators.
```

Read the PR yourself. Check that its claim matches what you intended and that it contains no private information. You can ask another contributor to review it using [the review guide](REVIEWING.md). Small, explicit contributions are easier to build on than large bundles of unrelated claims.

## Maintainer's phone check

- A newly invited member can accept access and open the repository.
- The member can connect the installed GitHub app without needing owner privileges; approval requests, if any, reach an owner.
- The reading prompt returns the actual repository files and commit.
- The writing prompt creates a branch and a real PR with the intended account and tools.
- Record any account-specific limitation and update this tutorial before advertising that path as tested.
