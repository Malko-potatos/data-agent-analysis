# 03. Agent Workflow Harness

Agent Workflow Harness는 에이전트가 어떤 일을 어떤 경계 안에서 수행해야 하는지 정하는 실행 구조다.

프롬프트가 "무엇을 해줘"에 가깝다면, harness는 "어떤 순서로, 어떤 도구로, 어떤 승인과 검증을 거쳐, 어떤 실패 복구 규칙으로 해줘"에 가깝다.

이 워크북에서 harness는 보통 두 lane을 결합한다.

```text
Data lane: 무엇을 분석/정제/요약/검증할 것인가?
Automation lane: 그 결과를 어떻게 반복 실행, 알림, queue, follow-up으로 만들 것인가?
```

## Harness Components

| 구성요소 | 질문 |
|---|---|
| Goal | 최종적으로 무엇이 완성되어야 하는가? |
| Data Lane | 어떤 데이터 분석 use case에 해당하는가? |
| Automation Lane | 어떤 자동화 use case와 결합하는가? |
| Inputs | 어떤 파일, DB, API, 앱, 화면, 문서를 사용할 수 있는가? |
| Tools | 어떤 스킬, 플러그인, CLI, 브라우저, 커넥터가 필요한가? |
| Procedure | 어떤 순서로 inventory, cleaning, analysis, reporting을 할 것인가? |
| Constraints | 원본 보존, read-only, 외부 발송 금지 같은 제약은 무엇인가? |
| Verification | row count, total, sample check, screenshot, source link 중 무엇으로 맞춤을 확인하는가? |
| Human Approval | 발송, 삭제, 배포, 권한 변경 전에 누가 승인하는가? |
| Recovery | 실패하면 어디에 로그를 남기고 어떤 상태로 되돌아가는가? |
| Reuse | 반복 가능하면 skill, automation, template 중 무엇으로 고정하는가? |

## Harness Families

| Harness | When To Use |
|---|---|
| Data Analysis | 깨끗하거나 어느 정도 정리된 데이터를 분석해 리포트/차트를 만들 때 |
| Data Cleaning | 분석 전에 결측, 중복, 타입, 이상치를 정리해야 할 때 |
| Metric Discovery | 공식 metric이 없고 원천 컬럼만 있을 때 |
| Multi-source Analytics | 광고, GA, DB, 커뮤니티 등 여러 출처를 연결할 때 |
| Dashboard Automation | 운영 지표를 반복 갱신하고 화면으로 보여줘야 할 때 |
| Signal Intelligence | 커뮤니티, 이메일, Slack, 리뷰 등 비정형 신호를 수집/분류할 때 |
| Monitoring Automation | 주기적으로 이상 징후를 찾고 알림 또는 queue를 만들 때 |
| Agent Audit | 이미 만든 agent 구조와 검증 계층을 점검할 때 |

## Combined Harness Examples

| Combined Harness | Data Lane | Automation Lane |
|---|---|---|
| Recurring Report Automation | Dataset/report analysis | Run verified operations |
| Dashboard Refresh Automation | Query tabular data | Verified dashboard refresh |
| Signal-to-Action Automation | Feedback synthesis | Slack/inbox action queue |
| Meeting-to-Analysis Queue | Meeting notes and data requests | Follow-up automation |
| Goal-based Analysis Loop | Multi-step data analysis | Follow a goal |

## Output Contract

모든 harness는 최소한 다음 산출물을 남긴다.

- 사용한 입력 목록
- 수행 절차
- 계산식 또는 분류 규칙
- 검증 기준과 결과
- 사람이 판단해야 할 항목
- 다음 반복 시 재사용할 템플릿 또는 자동화 후보

## Anti-patterns

- 자연어 요구를 그대로 긴 프롬프트로만 바꾸는 것
- 원본 데이터를 덮어쓰는 것
- 계산식을 설명하지 않고 차트만 만드는 것
- 검증 없는 자동화를 만드는 것
- 발송, 삭제, 배포 같은 외부 action을 승인 없이 실행하는 것
