# Backend Folder Structure

```
multi-agent-dev/
├── cmd/
│ └── orchestrator/
│ └── main.go # Entry point (run agents, task loop)
│
├── internal/
│ ├── agent/
│ │ ├── agent.go # Core Agent interface
│ │ ├── roles/
│ │ │ ├── architect.go # System design agent
│ │ │ ├── coder.go # Implementation agent
│ │ │ ├── reviewer.go # Code review / critique agent
│ │ │ ├── tester.go # Test-writing agent
│ │ │ └── optimizer.go # Performance / refactor agent
│ │ └── state.go # Agent memory / context
│ │
│ ├── task/
│ │ ├── task.go # Task interface
│ │ ├── coding.go # Coding task
│ │ ├── design.go # Architecture task
│ │ └── refactor.go # Refactor task
│ │
│ ├── debate/
│ │ ├── debate.go # Debate controller
│ │ ├── turn.go # Single interaction turn
│ │ ├── critique.go # Structured critiques
│ │ └── consensus.go # Consensus resolution
│ │
│ ├── artifact/
│ │ ├── artifact.go # Shared artifact interface
│ │ ├── code.go # Code artifacts
│ │ ├── diff.go # Diffs / patches
│ │ └── doc.go # Design docs
│ │
│ ├── workspace/
│ │ ├── fs.go # File system abstraction
│ │ ├── repo.go # Git-like repo abstraction
│ │ └── snapshot.go # Versioned state
│ │
│ ├── llm/
│ │ ├── client.go # LLM interface
│ │ ├── openai.go
│ │ └── mock.go
│ │
│ ├── evaluation/
│ │ ├── compile.go # Does code compile?
│ │ ├── tests.go # Test pass/fail
│ │ ├── lint.go # Static analysis
│ │ └── score.go # Overall solution score
│ │
│ └── config/
│ └── config.go
│
├── pkg/
│ ├── schema/
│ │ ├── message.go # Agent messages
│ │ ├── proposal.go # Agent proposals
│ │ └── decision.go # Consensus decisions
│ │
│ └── utils/
│ └── diff.go
│
├── examples/
│ └── rag_project/
│ ├── task.yaml # “Build a multi-agent RAG system”
│ └── expected/
│
├── test/
│ ├── debate_test.go
│ ├── agent_roles_test.go
│ └── consensus_test.go
│
├── go.mod
├── go.sum
└── README.md
```
