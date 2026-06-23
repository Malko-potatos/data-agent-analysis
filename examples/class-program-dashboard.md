# Class Program Dashboard

## Original Request

> 프로그램별 수업 진행상황이 자동 업데이트되어 대시보드로 보이면 좋겠습니다. 데이터는 DB에 있고 어드민에서 다운받아 분석하고 있습니다. DB와 연결되어 자동 업데이트되면 좋겠습니다.

## Requirement Card

| 항목 | 내용 |
|---|---|
| 사용자 | 운영자, 프로그램 매니저 |
| 목적 | 프로그램별/선생님별 수업 진행률과 지연 위험 파악 |
| 데이터 | DB, 기존 어드민 export |
| 현재 방식 | 어드민 다운로드 후 수동 분석 |
| 원하는 변화 | DB 연결 자동 업데이트 대시보드 |
| 반복성 | 매일 또는 상시 |
| 위험 | 프로그램별 완료 기준 차이, 중복 분류, 일정 미입력 |
| 검증 | 어드민 export와 DB 집계 비교 |

## Routing

| 항목 | 선택 |
|---|---|
| 가까운 use case | Datasets and reports, Verified operations |
| Harness | Dashboard Automation |
| 도구 | DB connector, dashboard/report, automation |
| 산출물 | 프로그램별/선생님별 진행률 대시보드 |
| 검증 | 어드민 export와 DB 집계 비교 |

## Rule Table Example

| 영역 | 지표 |
|---|---|
| 프로그램별 | 총 가구 수, 완료 가구 수, 미완료 가구 수, 완료율 |
| 진행상태별 | 수업일 미입력, 1회차만 완료, 2회차만 완료, 3회차 완료 |
| 선생님별 | 배정 수업 수, 완료 수업 수, 남은 수업 수, 진행률 |
| 위험 관리 | 11월 내 완료 위험 가구, 일정 미입력 가구, 지연 프로그램 |

## Prompt Skeleton

```text
DB 데이터를 기반으로 프로그램별 수업 진행률 자동 대시보드 설계를 만들어주세요.

먼저 현재 어드민 export와 DB 테이블/필드 후보를 inventory로 정리하세요.
프로그램별 완료 기준을 rule table로 분리하고,
가구별 상태가 하나의 상태로만 분류되도록 우선순위 규칙을 제안하세요.
프로그램별, 선생님별, 진행상태별, 위험관리 지표를 정의하세요.

출력:
- 데이터 소스 inventory
- 프로그램별 완료 기준 rule table
- 지표 정의와 계산식
- 대시보드 화면 구성
- 자동 업데이트 주기와 실패 로그 설계
- 어드민 export 대조 검증 계획

검증:
- 프로그램별 총 신청 가구 수와 수업 수를 어드민 export와 비교하세요.
- 가구별 상태가 중복 없이 하나로만 분류되는지 확인하세요.
- 선생님별 합계가 전체 집계와 맞는지 확인하세요.
- 마지막 갱신 시각과 실패 상태를 dashboard에 표시하세요.
```

## Expected Output

- Dashboard metric spec
- DB mapping table
- Rule table
- Verification plan
- Automation failure policy
