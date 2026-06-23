# 07. Skills, Plugins, Tools

도구 선택은 "가장 강력한 도구"를 고르는 일이 아니다. 요구사항, 데이터 위치, 위험, 검증 방식에 맞는 최소 도구 묶음을 고르는 일이다.

## Selection Table

| 상황 | 불러야 할 것 |
|---|---|
| CSV, XLSX, Google Sheet 분석 | spreadsheet / google-sheets |
| 보고서, 문서 산출물 | docs / pdf / data report |
| DB, API 직접 연결 | DB connector, API tool, agent-friendly CLI |
| 브라우저 대시보드 확인 | browser / chrome |
| 데스크톱 앱 조작 | computer-use |
| Slack/Gmail/Drive/Calendar | 해당 connector |
| 외부 커뮤니티 조사 | browser + search + feedback synthesis |
| 반복 실행 | automation |
| 기존 agent 점검 | code review + eval + verification checklist |
| 장시간 목표 | goal / long-running loop |

## Tool Choice Questions

- 데이터가 파일인가, 앱 화면인가, DB인가?
- 로그인이 필요한가?
- 원본을 수정할 위험이 있는가?
- 결과물이 표인가, 리포트인가, 대시보드인가?
- 반복 실행이 필요한가?
- 사람이 승인해야 하는 action이 포함되는가?

## Minimal Tooling Principle

처음부터 복잡한 pipeline을 만들지 않는다.

1. 한 번 분석으로 요구사항과 metric을 확정한다.
2. 검증 기준이 생기면 query/script/template으로 고정한다.
3. 반복성이 확인되면 automation 또는 skill로 전환한다.
4. 운영자가 매번 봐야 하면 dashboard로 만든다.

## Tool Notes

| 도구군 | 좋은 용도 | 조심할 점 |
|---|---|---|
| Spreadsheet | 빠른 정제, 표 검산, workbook 산출 | 수식/필터가 숨겨질 수 있음 |
| Python/R | 반복 가능한 분석, 대량 데이터 처리 | 환경과 의존성 기록 필요 |
| DB Connector | 최신 운영 데이터 접근 | read-only 권한과 query 검증 필요 |
| Browser/Chrome | 실제 dashboard/웹앱 확인 | 세션 상태와 화면 증거 기록 필요 |
| Computer Use | 앱 간 이동 작업 | 승인 없는 외부 action 금지 |
| Gmail/Slack | 메시지 triage와 draft | 발송 전 승인 필수 |
| Automation | 반복 실행 | 실패 로그와 중지 조건 필요 |
