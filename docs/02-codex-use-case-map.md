# 02. Codex Use Case Map

이 장은 OpenAI Codex use case를 데이터 분석과 자동화 교육 관점으로 재구성한다.

확인일: 2026-06-23

## Source Categories

공식 Codex use case 페이지의 Data 필터에는 데이터 정제, 표 데이터 질의, 데이터셋 분석과 리포트, 재무 workbook, 피드백 synthesis 등이 포함된다.

Automation 필터에는 inbox triage, bug triage, Computer Use 기반 QA, 목표 추적, Slack action item, verified operations, meeting follow-up 등이 포함된다.

이 워크북은 이 중 데이터 분석, 자동화, 지식 작업, 통합, 검증에 가까운 항목을 수업용 harness로 묶는다.

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

## Decision Rules

| 질문 | Yes라면 |
|---|---|
| 원천 데이터가 파일 또는 표인가? | Data Analysis 또는 Data Cleaning |
| 여러 소스의 join이 필요한가? | Multi-source Analytics |
| metric 정의가 불명확한가? | Metric Discovery |
| 결과물이 계속 갱신되어야 하는가? | Dashboard Automation 또는 Monitoring Automation |
| 외부 앱을 클릭하거나 조작해야 하는가? | Computer Use 또는 Browser/Chrome harness |
| 이미 만든 agent의 구조가 문제인가? | Agent Audit |

## Teaching Note

공식 use case 이름을 그대로 외우게 하지 않는다. 학생이 해야 할 일은 요구사항을 업무 패턴으로 읽고, 그 패턴에 맞는 harness를 선택하는 것이다.

## References

- https://developers.openai.com/codex/use-cases
- https://developers.openai.com/codex/use-cases?category=data
- https://developers.openai.com/codex/use-cases?category=automation
