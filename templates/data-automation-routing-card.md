# Data Automation Routing Card

데이터 분석과 자동화를 함께 설계할 때 사용하는 라우팅 카드다.

## 1. 사용자 요청

> 원문을 그대로 붙여넣는다.

## 2. Data Lane

| 질문 | 답 |
|---|---|
| 어떤 데이터를 분석/정제/요약해야 하는가? |  |
| 데이터 source는 어디인가? |  |
| 주요 metric 또는 질문은 무엇인가? |  |
| 먼저 1회 분석으로 확인해야 할 것은 무엇인가? |  |

선택한 Data use case:

- [ ] Analyze datasets and ship reports
- [ ] Query tabular data
- [ ] Clean and prepare messy data
- [ ] Turn feedback into actions
- [ ] Metric discovery
- [ ] Multi-source analytics

## 3. Automation Lane

| 질문 | 답 |
|---|---|
| 반복 실행이 필요한가? |  |
| trigger 또는 주기는 무엇인가? |  |
| 결과는 어디로 가야 하는가? | dashboard / report / Slack queue / inbox draft / issue / meeting follow-up |
| 실패하면 누가 어떻게 알아야 하는가? |  |

선택한 Automation use case:

- [ ] Run verified operations
- [ ] Follow a goal
- [ ] Prioritize Slack action items
- [ ] Manage your inbox
- [ ] Turn meetings into follow-ups
- [ ] QA with Computer Use
- [ ] Monitoring or bug triage

## 4. Verification Lane

- [ ] row count
- [ ] source total/subtotal
- [ ] sample row check
- [ ] join match rate
- [ ] 원문 링크/ID
- [ ] dashboard/export 대조
- [ ] 마지막 실행 시각과 실패 로그

## 5. Approval Lane

승인 없이 하지 않을 일:

- [ ] 이메일, Slack, DM, 게시글 발송
- [ ] 파일 삭제 또는 원본 덮어쓰기
- [ ] DB write 또는 권한 변경
- [ ] 외부 배포
- [ ] 광고비, 캠페인, 비용 발생 action 변경

## 6. Combined Workflow

```text
1회 분석
-> 검증 기준 확정
-> 반복 trigger/주기 결정
-> 자동 산출물 생성
-> 실패 로그와 승인 queue 운영
```
