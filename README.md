# Data Analysis Agent Workbook

자연어 요구사항을 데이터 분석/자동화 에이전트 작업으로 변환하는 교육용 워크북입니다.

이 레포의 핵심 메시지는 간단합니다. 에이전트에게 바로 "분석해줘"라고 시키기 전에, 먼저 일이 어떤 use case인지 분류하고, 그 use case에 맞는 Agent Workflow Harness를 고른 뒤, 데이터, 도구, 검증, 승인 경계를 붙여 실행합니다.

## What You Will Learn

- 사용자 요구사항을 업무 문제로 분해하는 법
- Codex use case와 분석/자동화 harness를 매칭하는 법
- 필요한 스킬, 플러그인, 도구, 데이터 접근 방식을 판단하는 법
- 실행 프롬프트를 작업 명세로 작성하는 법
- 정적 검증 기준과 승인 경계를 설계하는 법
- 반복 가능한 작업을 스킬, 자동화, 대시보드, 리포트 템플릿으로 고정하는 법

## Core Model

```text
Natural request
-> Requirement card
-> Use case matching
-> Agent Workflow Harness
-> Tools and data access
-> Execution prompt
-> Static verification
-> Human approval boundary
-> Reusable skill, automation, dashboard, or report
```

## Focus

이 워크북은 다음 작업에 집중합니다.

- 데이터 분석
- 데이터 정제
- 지표 발굴
- 다중 소스 분석
- 운영 대시보드 자동화
- 비정형 신호 분석
- 기존 agent 구조 점검

Native iOS/macOS 앱 구현 중심 use case는 이번 교육 범위에서 제외합니다.

## How To Use This Workbook

1. [docs/00-introduction.md](docs/00-introduction.md)에서 전체 관점을 읽습니다.
2. [docs/01-natural-request-to-use-case.md](docs/01-natural-request-to-use-case.md)의 요구사항 해부 카드로 사용자 발화를 분해합니다.
3. [docs/02-codex-use-case-map.md](docs/02-codex-use-case-map.md)에서 가까운 Codex use case를 고릅니다.
4. [docs/03-agent-workflow-harness.md](docs/03-agent-workflow-harness.md)에서 작업 harness를 선택합니다.
5. [templates/](templates/)의 양식으로 실행 명세와 검증 기준을 작성합니다.
6. [examples/](examples/)의 예제로 수업 실습을 진행합니다.

## Repository Map

| Path | Purpose |
|---|---|
| [docs/](docs/) | 워크북 본문 챕터 |
| [examples/](examples/) | 수업용 시나리오와 완성 예시 |
| [templates/](templates/) | 요구사항 카드, harness 명세, 실행 프롬프트 양식 |
| [checklists/](checklists/) | 검증과 승인 경계 체크리스트 |
| [prompts/](prompts/) | 바로 실행 가능한 프롬프트 초안 |
| [references/](references/) | 외부 참고 자료 정리 |
| [skills/](skills/) | 반복 워크플로우를 Codex skill로 전환하기 위한 설계 메모 |

## Sources

이 워크북은 다음 공개 자료를 교육용으로 재구성합니다.

- [OpenAI Codex use cases](https://developers.openai.com/codex/use-cases)
- [OpenAI Codex data use cases](https://developers.openai.com/codex/use-cases?category=data)
- [OpenAI Codex automation use cases](https://developers.openai.com/codex/use-cases?category=automation)
- [wquguru/harness-books](https://github.com/wquguru/harness-books)

외부 페이지는 바뀔 수 있으므로, 수업에서는 링크 자체보다 이 레포의 routing, harness, verification 구조를 기준으로 사용합니다.
