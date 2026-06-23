# Breeding Revenue Agent Audit

## Original Request

> GA는 기초 정보만 있고, DB에는 유저 유입/활동로그가 있습니다. 현재 매출 분석 agent를 만들었고 구조 점검과 더 효율적인 방식, 광고 데이터 연동, 커뮤니티 키워드 분석 agent가 필요합니다.

## Requirement Card

| 항목 | 내용 |
|---|---|
| 사용자 | 사업/마케팅/데이터 담당자 |
| 목적 | 기존 매출 분석 agent 구조 점검과 고도화 방향 도출 |
| 데이터 | GA, DB 유입/활동 로그, 결제/환불, 광고 데이터, 커뮤니티 원문 |
| 현재 방식 | 일부 agent가 있으나 구조와 검증이 불명확 |
| 원하는 변화 | 더 효율적인 분석 구조, 광고 연동, 키워드 분석 agent |
| 반복성 | 반복 분석과 주기적 리포트 가능 |
| 위험 | session/ip 기준 한계, attribution 오류, 환불 반영 누락 |
| 검증 | 매출/환불 total, UTM/key mapping, 원문 링크 |

## Routing

| 항목 | 선택 |
|---|---|
| 가까운 use case | Datasets and reports, Feedback synthesis, Reusable skills |
| Harness | Agent Audit + Multi-source Analytics + Signal Intelligence |
| 도구 | DB connector, GA, 광고 데이터, browser/search |
| 산출물 | agent 구조 진단표, 개선 구조, 키워드 리포트 |
| 검증 | session/ip 기준 한계, UTM/key 매핑, 매출/환불 total |

## Data + Automation Composition

| Lane | 선택 |
|---|---|
| Data lane | Agent audit, Multi-source revenue analytics, Feedback synthesis |
| Automation lane | Follow a goal, Run verified operations, Signal-to-Action |
| 1회 분석 | 현재 agent의 입력/처리/출력/검증 gap 확인 |
| 자동화 전환 | 반복 매출 리포트, 광고 데이터 연동 점검, 커뮤니티 키워드 queue |
| 승인 경계 | 광고 설정 변경, 고객 메시지 발송, DB write는 승인 필요 |

## Audit Questions

- 유입 출처가 광고, 블로그, 커뮤니티별로 구분되는가?
- session/ip 기준으로 같은 사용자가 분리될 위험은 없는가?
- 결제, 환불, 취소가 매출 분석에 어떻게 반영되는가?
- 퍼널 단계가 유입, 가입, 상담, 구매, 환불로 명확한가?
- 외부 키워드 수집은 원문 링크와 수집 시점을 남기는가?
- 기존 agent는 계산식과 검증 결과를 산출물에 남기는가?

## Prompt Skeleton

```text
현재 매출 분석 agent 구조를 점검하고 개선안을 제안해주세요.

먼저 현재 agent의 입력, 처리 단계, 출력, 검증 단계를 inventory로 정리하세요.
GA, DB, 결제/환불, 광고 데이터, 커뮤니티 신호가 어떻게 연결되는지 표시하세요.
유입, 가입, 활동, 구매, 환불 funnel을 정의하고,
현재 데이터만으로 계산 가능한 metric과 추가 연결이 필요한 metric을 분리하세요.

출력:
- 현재 agent 구조 진단표
- 데이터 소스와 join key 목록
- metric 후보와 계산식
- attribution/환불/session 기준 리스크
- 광고 데이터 연동 설계
- 커뮤니티 키워드 분석 agent 설계
- 우선순위별 개선안

검증:
- 매출과 환불 total을 기준 source와 대조하세요.
- join match rate와 unmatched row를 남기세요.
- 공식 metric이 불명확하면 후보로만 표시하세요.
- 외부 커뮤니티 요약에는 원문 링크 또는 ID를 남기세요.

자동화 전환:
- 개선 전에는 기존 agent의 검증 gap을 먼저 기록하세요.
- 반복 가능한 매출/환불/유입 리포트는 verified operation 후보로 분리하세요.
- 커뮤니티 키워드는 action queue draft로 만들고 자동 발송하지 마세요.
```

## Expected Output

- Agent audit report
- 데이터 연결도
- metric discovery table
- 리스크와 검증 gap
- 다음 구현 backlog
- 반복 리포트와 신호 queue 자동화 후보
