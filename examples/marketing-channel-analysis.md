# Marketing Channel Analysis

## Original Request

> 저는 마케팅 데이터를 분석하고 싶어요. 유료 비용 태우는 곳, 무료 바이럴, 유입 데이터나 평판 데이터를 분석하고 개선안을 찾고 싶어요.

## Requirement Card

| 항목 | 내용 |
|---|---|
| 사용자 | 마케팅 담당자, 경영진 |
| 목적 | 유료/무료 채널별 성과와 개선안 도출 |
| 데이터 | 광고 플랫폼 export/API, GA, DB, 커뮤니티/리뷰 원문 |
| 현재 방식 | 채널별로 흩어진 데이터 수동 확인 |
| 원하는 변화 | 통합 성과표, 평판 키워드, 우선순위 action |
| 반복성 | 월간 또는 주간 리포트 가능 |
| 위험 | attribution 오류, 비용/매출 기간 불일치, 원문 없는 평판 요약 |
| 검증 | 광고비 total, 전환 total, 매출 total, 원문 링크 |

## Routing

| 항목 | 선택 |
|---|---|
| 가까운 use case | Datasets and reports, Feedback synthesis |
| Harness | Multi-source Analytics + Signal Intelligence |
| 도구 | 광고 export/API, GA/DB, browser/search, report |
| 산출물 | 채널별 성과표, 평판 키워드, 개선안 |
| 검증 | 비용 total, 전환 total, 원문 링크, 기간/필터 |

## Prompt Skeleton

```text
유료 광고와 무료 바이럴 채널의 마케팅 성과를 통합 분석해주세요.

먼저 데이터 소스별 수집 가능한 항목을 정리하고,
유료 채널과 무료/바이럴 채널을 구분하세요.
채널별 유입, 전환, 매출, 비용, 평판 신호를 비교하세요.
CTR, CVR, CPA, ROAS 등 계산 가능한 지표는 계산하되,
정의가 불명확하면 지표 후보로 표시하세요.
평판 데이터는 원문 링크와 함께 키워드, 긍정/부정 맥락, 반복 불만을 요약하세요.

출력:
- 데이터 인벤토리
- 채널별 성과 비교표
- 유료/무료 채널별 개선안
- 평판 키워드 요약
- 우선순위 액션 리스트
- 확인 필요 데이터와 한계

검증:
- 각 소스의 기간과 필터를 기록하세요.
- 광고비, 전환, 매출 total을 source total과 대조하세요.
- join key와 unmatched row를 기록하세요.
- 평판 요약에는 원문 링크 또는 ID를 남기세요.
```

## Expected Output

- 1페이지 executive summary
- 채널별 KPI table
- 유료/무료 채널 비교
- 평판 키워드와 원문 링크
- 다음 실험 후보
- 데이터 한계와 확인 질문
