# 05. Automation Harness

Automation Harness는 한 번의 분석이 아니라 반복되는 업무를 안정적으로 실행하도록 설계한다.

자동화의 핵심은 빠르게 돌리는 것이 아니라, 실패했을 때 어디서 멈췄는지 알고 사람이 승인해야 할 action을 분리하는 것이다.

## Automation Use Case Families

공식 Codex automation use case는 이 워크북에서 다음 운영 패턴으로 재해석한다.

| Automation use case | 워크북에서의 의미 | 데이터 분석과 결합되는 지점 |
|---|---|---|
| Manage your inbox | 요청, 회신, 후속 작업을 triage한다. | 분석 리포트 공유 후 들어오는 질문을 분류한다. |
| Automate bug triage | 이상 후보를 분류하고 담당 queue로 보낸다. | 지표 급락, 수집 실패, dashboard 이상을 triage한다. |
| QA with Computer Use | 실제 앱/대시보드를 클릭해 확인한다. | 계산 결과가 어드민 화면과 맞는지 검증한다. |
| Follow a goal | 오래 걸리는 목표를 여러 turn에 걸쳐 추적한다. | 데이터 수집, 정제, 분석, 리포트 개선을 장기 루프로 실행한다. |
| Prioritize Slack action items | 메시지와 thread를 action queue로 바꾼다. | 분석 결과나 고객 신호를 담당자별 next step으로 분류한다. |
| Run verified operations | 반복 workflow를 실행하고 결과를 검증한다. | 매일/매주 같은 query, report, dashboard refresh를 검증 포함 실행한다. |
| Turn meetings into follow-ups | 회의 내용을 후속 작업으로 바꾼다. | 회의에서 나온 데이터 요청을 분석 backlog로 만든다. |

## Data Analysis + Automation Flow

```text
분석 질문 정의
-> 데이터 source와 metric 확인
-> 1회 분석 실행
-> 검증 기준 확정
-> 반복 실행 조건 결정
-> 자동화 trigger/주기/알림 설계
-> 사람 승인 경계 설정
-> 실패 로그와 복구 규칙 설계
```

처음부터 자동화하지 않는다. 먼저 한 번의 분석으로 metric과 검증 기준을 안정화한 뒤, 같은 일이 반복된다는 증거가 생기면 자동화한다.

## Dashboard Automation

목적:

- 운영자가 매번 수동 집계하지 않고 현재 상태를 볼 수 있게 한다.

흐름:

```text
업무 규칙 정의
-> DB 테이블/필드 매핑
-> 집계 로직 작성
-> 대시보드 지표 정의
-> 자동 업데이트 주기 설정
-> 실패/누락 알림 설계
```

검증:

- 어드민 export와 DB 집계 비교
- rule table 검증
- 마지막 갱신 시각 표시
- 실패 로그 표시

## Monitoring Automation

목적:

- 매일 또는 매주 이상 징후를 찾아 검토 queue를 만든다.

흐름:

```text
기준 지표 정의
-> 임계값 또는 비교 기간 설정
-> 자동 수집
-> 이상 후보 탐지
-> 사람이 볼 요약 생성
-> 승인된 action만 실행
```

검증:

- 알림 기준이 문서화되어 있는가?
- false positive를 검토할 수 있는 sample이 있는가?
- action과 notification이 분리되어 있는가?

## Signal-to-Action Automation

목적:

- 분석된 신호를 사람이 실행할 수 있는 action queue로 바꾼다.

흐름:

```text
신호 수집
-> 중복 제거
-> 주제/감정/위험 분류
-> 담당자/우선순위 매핑
-> Slack/Gmail/issue queue draft 생성
-> 사람 승인 후 전달
```

검증:

- 원문 링크 또는 ID가 남아 있는가?
- action item이 원문 근거와 연결되는가?
- 자동 발송이 아니라 draft 또는 approval queue로 남는가?

## Meeting-to-Analysis Queue

목적:

- 회의나 메시지에서 나온 데이터 요청을 분석 backlog로 바꾼다.

흐름:

```text
회의/메시지 요약
-> 데이터 요청 후보 추출
-> 필요한 source와 owner 표시
-> 분석 질문으로 재작성
-> 우선순위와 마감일 부여
-> 분석 task 또는 dashboard request로 전환
```

## Signal Intelligence

목적:

- 커뮤니티, Slack, Gmail, 리뷰, 이슈 등 비정형 신호를 분석한다.

흐름:

```text
수집 범위 정의
-> 원문 링크/ID 보존
-> 키워드/주제 추출
-> 반복 언급/감정/리스크 분류
-> action item 생성
-> 주기적 리포팅
```

검증:

- 원문 링크
- 수집 기간
- 중복 제거 기준
- 샘플 원문 확인

## Direct Data Pipeline

목적:

- 어드민 다운로드를 줄이고 DB/API/CLI에서 직접 읽어 반복 가능한 분석을 만든다.

기본 원칙:

- 기본은 read-only다.
- 쿼리와 파라미터를 저장한다.
- 결과 row count와 query timestamp를 남긴다.
- 외부 전송이나 DB 변경은 별도 승인 action으로 분리한다.

## Automation Output Contract

자동화 산출물에는 다음 정보가 있어야 한다.

- 마지막 실행 시각
- 사용한 데이터 범위
- 성공/실패 상태
- 실패 원인과 재시도 여부
- 사람이 검토해야 할 항목
- 승인 없이 실행하지 않은 action 목록
