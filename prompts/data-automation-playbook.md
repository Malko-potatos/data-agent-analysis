# Data Automation Playbook Prompt

```text
이 요청을 데이터 분석 use case와 자동화 use case의 결합으로 설계해주세요.

목표:
- 먼저 어떤 데이터 분석이 필요한지 Data lane을 고르고,
  그 분석 결과를 어떤 반복 실행/알림/queue/대시보드/후속 작업 자동화로 만들지 Automation lane을 고릅니다.

입력:
- 사용자 요청 카드
- 사용 가능한 데이터 source
- 기존 보고서, dashboard, 어드민 export 또는 기준 숫자
- 알림/공유/후속 작업이 필요한 채널

절차:
1. 사용자 요청을 비개발자 언어로 다시 요약하세요.
2. Data lane을 선택하고 이유를 설명하세요.
3. Automation lane을 선택하고 이유를 설명하세요.
4. 처음 1회 분석에서 확인해야 할 metric과 검증 기준을 정하세요.
5. 반복 실행이 필요한 경우 trigger, 주기, 실패 로그, 마지막 갱신 시각을 설계하세요.
6. 결과물이 report, dashboard, Slack queue, inbox draft, meeting follow-up 중 어디로 가야 하는지 정하세요.
7. 사람이 승인해야 할 action을 분리하세요.

제약:
- 원본 데이터는 수정하지 마세요.
- 자동 발송, 삭제, DB write, 권한 변경, 비용 발생 action은 하지 마세요.
- 불명확한 metric은 공식 KPI처럼 단정하지 마세요.

검증:
- row count, source total/subtotal, sample row check를 포함하세요.
- 여러 source를 join하면 join key, match rate, unmatched row를 기록하세요.
- 비정형 신호는 원문 링크 또는 ID를 남기세요.
- 자동화에는 마지막 실행 시각, 성공/실패 상태, 실패 로그를 포함하세요.

출력:
- 요청 요약
- Data lane
- Automation lane
- 결합 workflow
- 필요한 자료와 도구
- 1회 분석 단계
- 자동화 전환 단계
- 검증 기준
- 승인 필요한 action
```
