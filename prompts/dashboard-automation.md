# Dashboard Automation Prompt

```text
운영 대시보드 자동화 설계를 만들어주세요.

목표:
- 수동 export와 집계를 줄이고, 운영자가 반복적으로 볼 수 있는 자동 갱신 dashboard spec을 만듭니다.

입력:
- 현재 어드민 export
- DB table 또는 API 후보
- 업무 규칙
- 기존 dashboard 또는 수동 리포트

절차:
1. 현재 수동 workflow를 단계별로 정리하세요.
2. DB/API source와 어드민 export column을 mapping하세요.
3. dashboard에서 볼 metric과 계산식을 정의하세요.
4. 업무 규칙은 rule table로 분리하세요.
5. 자동 업데이트 주기와 실패 로그 구조를 설계하세요.
6. 사람이 확인해야 할 예외 queue를 정의하세요.

제약:
- 기본은 read-only로 설계하세요.
- DB write, 배포, 권한 변경은 하지 마세요.
- 민감정보는 표시 필요성과 마스킹 기준을 검토하세요.

검증:
- 어드민 export total과 DB 집계를 비교하세요.
- subtotal이 total과 맞는지 확인하세요.
- sample row 상태를 수동 확인하세요.
- 마지막 갱신 시각과 실패 상태를 dashboard에 표시하도록 설계하세요.

출력:
- dashboard metric spec
- source mapping table
- rule table
- 자동화 실행 주기
- 실패/복구 정책
- 검증 계획
```
