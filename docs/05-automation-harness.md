# 05. Automation Harness

Automation Harness는 한 번의 분석이 아니라 반복되는 업무를 안정적으로 실행하도록 설계한다.

자동화의 핵심은 빠르게 돌리는 것이 아니라, 실패했을 때 어디서 멈췄는지 알고 사람이 승인해야 할 action을 분리하는 것이다.

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
