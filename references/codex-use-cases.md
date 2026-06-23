# Codex Use Cases Reference

확인일: 2026-06-23

이 파일은 OpenAI Codex use case 페이지를 수업용으로 재분류한 메모다. 공식 페이지의 항목과 설명은 변경될 수 있으므로, 수업에서는 링크와 확인일을 함께 남긴다.

## Official Links

- Codex use cases: https://developers.openai.com/codex/use-cases
- Data use cases: https://developers.openai.com/codex/use-cases?category=data
- Automation use cases: https://developers.openai.com/codex/use-cases?category=automation
- Analyze datasets and ship reports: https://developers.openai.com/codex/use-cases/datasets-and-reports
- Manage your inbox: https://developers.openai.com/codex/use-cases/manage-your-inbox
- Use your computer with Codex: https://developers.openai.com/codex/use-cases/use-your-computer-with-codex
- Follow a goal: https://developers.openai.com/codex/use-cases/follow-goals

## Data-Oriented Items To Watch

- Analyze datasets and ship reports
- Query tabular data
- Clean and prepare messy data
- Turn feedback into actions
- Forecast cash flow
- Model a DCF valuation
- Review budget vs. actuals

## Automation-Oriented Items To Watch

- Manage your inbox
- Automate bug triage
- QA your app with Computer Use
- Follow a goal
- Prioritize Slack action items
- Run verified operations
- Turn meetings into follow-ups

## Workbook Mapping

| Official use case direction | Workbook concept |
|---|---|
| Tabular data questions | Data Analysis Harness |
| Messy data preparation | Data Cleaning Harness |
| Reports and visualizations | Data Analysis Harness |
| Feedback synthesis | Signal Intelligence Harness |
| Repeated verified workflows | Monitoring/Dashboard Automation |
| Long-running goal | Goal-based work loop |
| Computer Use | App/browser action harness with approval boundary |

## Data + Automation Composition

이 워크북의 핵심 라우팅은 한 개 use case를 고르는 것이 아니라 Data lane과 Automation lane을 조합하는 것이다.

| Data lane | Automation lane | Workbook pattern |
|---|---|---|
| Analyze datasets and ship reports | Run verified operations | Recurring Report Automation |
| Query tabular data | Run verified operations | Dashboard Refresh Automation |
| Clean and prepare messy data | Run verified operations | Repeatable Cleaning Workflow |
| Turn feedback into actions | Prioritize Slack action items | Signal-to-Action Queue |
| Dataset/report analysis | Follow a goal | Long-running Analysis Loop |
| Report/dashboard verification | QA with Computer Use | UI-backed Verification |
| Meeting or inbox requests with data needs | Manage inbox, Turn meetings into follow-ups | Request-to-Analysis Queue |

## Teaching Boundary

공식 use case는 routing 참고 자료다. 이 워크북의 교육 단위는 공식 페이지 이름이 아니라 다음 세 가지다.

- 요구사항 해부 카드
- Agent Workflow Harness
- Static verification and approval boundary
