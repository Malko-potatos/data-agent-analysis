# Dashboard Automation Checklist

## Scope

- [ ] dashboard 사용자가 명확하다.
- [ ] dashboard가 답해야 하는 질문이 명확하다.
- [ ] 자동 업데이트 주기가 정해져 있다.

## Data

- [ ] DB 테이블과 필드 mapping이 있다.
- [ ] query 또는 export 기준이 저장되어 있다.
- [ ] read-only 권한을 기본으로 한다.
- [ ] 민감정보 표시 여부를 검토했다.

## Rules

- [ ] 업무 규칙이 rule table로 분리되어 있다.
- [ ] 상태 분류 우선순위가 있다.
- [ ] row가 중복 상태로 분류되지 않는다.

## Display

- [ ] 마지막 갱신 시각이 표시된다.
- [ ] 데이터 기간과 필터가 표시된다.
- [ ] 실패 상태가 표시된다.
- [ ] 사람이 drill-down할 수 있는 기준 row 또는 링크가 있다.

## Verification

- [ ] 어드민 export 또는 기존 dashboard와 total을 비교했다.
- [ ] subtotal이 total과 맞는다.
- [ ] sample row 상태를 수동 확인했다.
- [ ] 실패 로그를 확인할 수 있다.
