# 09. Data Automation Playbook

이 장은 이 워크북의 핵심 흐름을 명확히 한다. 사용자가 원하는 것은 단순한 데이터 분석만도 아니고, 맥락 없는 자동화만도 아니다. 대부분의 실무 요청은 **데이터 분석 use case와 자동화 use case의 결합**이다.

## Core Question

항상 두 가지를 함께 묻는다.

```text
1. 무엇을 분석해야 하는가?
2. 그 분석 결과를 어떻게 반복 실행, 알림, 검토 queue, 승인 흐름으로 만들 것인가?
```

## Two-lane Model

| Lane | 묻는 질문 | 예시 |
|---|---|---|
| Data lane | 어떤 데이터를 분석/정제/요약/검증하는가? | 매출 분석, 광고 성과, 수업 진행률, 커뮤니티 불만 |
| Automation lane | 그 결과를 어떤 운영 흐름으로 반복할 것인가? | 매주 리포트, dashboard refresh, Slack queue, meeting follow-up |
| Verification lane | 반복 실행이 맞았는지 무엇으로 확인하는가? | row count, source total, 어드민 export, 원문 링크, sample check |
| Approval lane | 사람이 승인해야 할 action은 무엇인가? | 발송, 삭제, DB write, 권한 변경, 외부 공유 |

## Composition Patterns

| Pattern | Data use case | Automation use case | 산출물 |
|---|---|---|---|
| Recurring Report | Analyze datasets and ship reports | Run verified operations | 주간/월간 리포트, 검증 로그 |
| Dashboard Refresh | Query tabular data, Datasets and reports | Run verified operations | 자동 갱신 대시보드, 실패 상태 |
| Metric Monitor | Metric discovery, Dataset analysis | Slack action triage, bug triage | 이상 후보 queue, 알림 draft |
| Signal-to-Action | Turn feedback into actions | Prioritize Slack action items | 키워드/불만 queue, 담당자별 action |
| Meeting-to-Analysis | Knowledge work + data request | Turn meetings into follow-ups | 분석 backlog, 자료 요청 목록 |
| Long-running Analysis | Multi-source analytics | Follow a goal | 장기 목표 추적, 단계별 검증 기록 |
| UI-backed Verification | Report/dashboard analysis | QA with Computer Use | 어드민/대시보드 화면 대조 기록 |
| Inbox-to-Report | Inbox/request triage | Manage your inbox | 데이터 요청 분류, 답변 draft, 리포트 링크 |

## Recommended Workflow

```text
비개발자 요청 카드 작성
-> Data lane 선택
-> Automation lane 선택
-> 1회 분석으로 metric/검증 기준 확정
-> 반복 trigger와 주기 결정
-> 알림/queue/draft/대시보드 산출물 설계
-> 승인 경계 설정
-> 실패 로그와 복구 규칙 설계
-> skill, template, automation으로 고정
```

## Teaching Flow

수업에서는 학생에게 automation을 처음부터 만들게 하지 않는다.

1. 먼저 한 번의 분석을 완성한다.
2. 분석 결과가 맞는지 source total, sample row, 기존 보고서와 대조한다.
3. 반복성이 있는지 묻는다.
4. 반복성이 있으면 automation lane을 고른다.
5. 자동화가 직접 action을 실행해야 하는지, draft/queue만 만들어야 하는지 나눈다.
6. 사람 승인 경계를 붙인다.

## Example: Marketing

원 요구:

> 유료 광고, 무료 바이럴, 유입 데이터, 평판 데이터를 분석하고 개선안을 찾고 싶어요.

조합:

| Lane | 선택 |
|---|---|
| Data lane | Multi-source marketing analysis, Feedback synthesis |
| Automation lane | Recurring Report, Signal-to-Action, Slack action triage |
| Verification | 광고비 total, 전환 total, 매출 total, 원문 링크 |
| Approval | 캠페인 변경, 외부 발송, 광고비 조정은 승인 필요 |

실행 흐름:

```text
1회 통합 분석
-> channel별 metric과 평판 키워드 확인
-> 검증 기준 확정
-> 매주 리포트 자동 생성
-> 반복 불만/기회 키워드를 action queue로 전환
-> 캠페인 변경은 draft로만 남기고 사람 승인 요청
```

## Example: Class Program Dashboard

원 요구:

> 프로그램별 수업 진행상황이 자동 업데이트되어 대시보드로 보이면 좋겠습니다.

조합:

| Lane | 선택 |
|---|---|
| Data lane | Query tabular data, Dataset/report analysis |
| Automation lane | Dashboard Refresh, Run verified operations |
| Verification | 어드민 export total, 프로그램별 subtotal, sample household check |
| Approval | DB write, 상태 변경, 담당자 메시지 발송은 승인 필요 |

실행 흐름:

```text
수동 export와 DB 집계 비교
-> rule table로 완료 기준 확정
-> dashboard metric 정의
-> 자동 refresh 주기 설정
-> 마지막 갱신 시각과 실패 로그 표시
-> 지연 위험 알림은 draft 또는 queue로 생성
```

## Prompt Block

```text
이 요청을 데이터 분석 use case와 자동화 use case로 나눠 라우팅해주세요.

먼저 어떤 데이터를 분석/정제/요약해야 하는지 Data lane을 고르세요.
그 다음 분석 결과를 반복 실행, 알림, queue, dashboard, meeting follow-up 중 어떤 자동화 흐름으로 만들지 Automation lane을 고르세요.
처음에는 1회 분석으로 metric과 검증 기준을 확정하고,
반복성이 확인된 뒤 자동화 trigger, 주기, 실패 로그, 승인 경계를 설계하세요.

출력:
- Data lane
- Automation lane
- 결합된 workflow
- 필요한 데이터와 도구
- 검증 기준
- 승인 필요한 action
- 1회 분석 단계와 자동화 전환 단계
```
