# 02. Codex Use Case Map

이 장은 OpenAI Codex use case를 데이터 분석과 자동화 교육 관점으로 재구성한다.

확인일: 2026-06-23

## Source Categories

공식 Codex use case 페이지의 Data 필터에는 데이터 정제, 표 데이터 질의, 데이터셋 분석과 리포트, 재무 workbook, 피드백 synthesis 등이 포함된다.

Automation 필터에는 inbox triage, bug triage, Computer Use 기반 QA, 목표 추적, Slack action item, verified operations, meeting follow-up 등이 포함된다.

이 워크북은 이 중 데이터 분석, 자동화, 지식 작업, 통합, 검증에 가까운 항목을 수업용 harness로 묶는다. 중요한 점은 데이터 use case와 자동화 use case를 하나만 고르는 것이 아니라, 대부분의 실무 요청에서 둘을 조합한다는 것이다.

## Two-axis Routing

분석/자동화 요청은 두 번 라우팅한다.

```text
사용자 요청
-> Data use case: 무엇을 분석/정제/요약/검증할 것인가?
-> Automation use case: 이 결과를 어떻게 반복 실행, 알림, queue, 승인 흐름으로 만들 것인가?
-> Combined harness: 분석 산출물과 자동화 운영 규칙을 함께 설계한다.
```

| Data lane | Automation lane | 결합된 작업 |
|---|---|---|
| Analyze datasets and ship reports | Run verified operations | 매주 같은 쿼리/리포트를 실행하고 total, row count, sample check를 검증한다. |
| Query tabular data | Follow a goal | 장시간 목표를 두고 여러 데이터 질문을 순차적으로 해결한다. |
| Clean and prepare messy data | Run verified operations | 원본 보존, 정제 copy 생성, 변경 내역 기록을 반복 workflow로 고정한다. |
| Turn feedback into actions | Prioritize Slack action items 또는 meeting follow-up | 리뷰/커뮤니티/회의 신호를 action queue로 바꾼다. |
| Analyze datasets and ship reports | Manage your inbox 또는 Slack action triage | 리포트를 만든 뒤 공유/후속 요청/응답 queue를 관리한다. |
| Data quality or dashboard metric check | QA with Computer Use | 브라우저/어드민 화면에서 숫자와 상태를 직접 확인한다. |

## Mapping Table

| 사용자 요구 유형 | 가까운 Codex use case | 선택할 교육용 Harness |
|---|---|---|
| CSV, Excel, DB 데이터를 분석하고 싶다 | Analyze datasets and ship reports, Query tabular data | Data Analysis Harness |
| 데이터가 지저분하다 | Clean and prepare messy data | Data Cleaning Harness |
| 지표가 정의되지 않은 원천 데이터만 있다 | Clean messy data, Datasets and reports | Metric Discovery Harness |
| 광고, 유입, 매출, 환불을 연결하고 싶다 | Datasets and reports, Spreadsheet/finance analysis | Multi-source Analytics Harness |
| 커뮤니티 키워드와 평판을 보고 싶다 | Feedback synthesis, Signal triage | Signal Intelligence Harness |
| 수동 다운로드 없이 DB와 연결하고 싶다 | Agent-friendly CLI, Verified operations | Direct Data Pipeline Harness |
| 운영 대시보드가 자동 업데이트되면 좋겠다 | Datasets and reports, Automation | Dashboard Automation Harness |
| 매일/매주 이상 징후를 보고 싶다 | Automation bug triage, Slack action triage | Monitoring Automation Harness |
| 기존 agent 구조를 점검하고 싶다 | Reusable skills, Evals, Verified operations | Agent Audit Harness |

## Combined Mapping Table

| 사용자 요구 | Data use case | Automation use case | 선택할 Combined Harness |
|---|---|---|---|
| 매주 매출 데이터를 분석하고 요약을 받고 싶다 | Analyze datasets and ship reports | Run verified operations | Recurring Report Automation |
| 광고/유입/매출 데이터를 연결하고 이상 징후를 알림받고 싶다 | Multi-source dataset analysis | Slack action triage, verified operations | Multi-source Monitoring Automation |
| 커뮤니티 글에서 반복 불만을 뽑아 담당자에게 넘기고 싶다 | Turn feedback into actions | Prioritize Slack action items | Signal-to-Action Automation |
| 어드민 다운로드 없이 DB 기준 대시보드를 업데이트하고 싶다 | Query tabular data, datasets and reports | Verified operations | Dashboard Refresh Automation |
| 회의에서 나온 데이터 요청을 follow-up으로 만들고 싶다 | Knowledge work + data report | Turn meetings into follow-ups | Meeting-to-Analysis Queue |
| 긴 분석 목표를 며칠에 걸쳐 추적하고 싶다 | Dataset/report analysis | Follow a goal | Goal-based Analysis Loop |

## Decision Rules

| 질문 | Yes라면 |
|---|---|
| 원천 데이터가 파일 또는 표인가? | Data Analysis 또는 Data Cleaning |
| 여러 소스의 join이 필요한가? | Multi-source Analytics |
| metric 정의가 불명확한가? | Metric Discovery |
| 결과물이 계속 갱신되어야 하는가? | Data lane을 먼저 고른 뒤 Dashboard Automation 또는 Monitoring Automation과 결합 |
| 결과를 누군가에게 전달하거나 action queue로 만들 것인가? | Signal-to-Action, Inbox/Slack/Meeting follow-up 자동화와 결합 |
| 외부 앱을 클릭하거나 조작해야 하는가? | Computer Use 또는 Browser/Chrome harness |
| 이미 만든 agent의 구조가 문제인가? | Agent Audit |

## Teaching Note

공식 use case 이름을 그대로 외우게 하지 않는다. 학생이 해야 할 일은 요구사항을 업무 패턴으로 읽고, 그 패턴에 맞는 harness를 선택하는 것이다.

## References

- https://developers.openai.com/codex/use-cases
- https://developers.openai.com/codex/use-cases?category=data
- https://developers.openai.com/codex/use-cases?category=automation
