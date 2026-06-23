# 04. Data Analysis Harness

Data Analysis Harness는 데이터를 분석해 의사결정에 쓸 수 있는 표, 차트, 리포트, 대시보드 초안을 만드는 구조다.

## Flow

```text
데이터 인벤토리
-> 품질 점검
-> 지표 정의
-> 분석/시각화
-> 해석
-> 리포트 생성
-> 검증
```

## Required Inputs

- 데이터 파일, DB query, API export, Google Sheet, dashboard export 중 하나 이상
- 분석 기간과 필터
- 핵심 질문
- 결과물을 볼 사람
- 검증에 사용할 기준 데이터

## Data Inventory

| 확인 항목 | 기록할 내용 |
|---|---|
| Source | 파일명, 테이블명, API endpoint, Sheet URL |
| Grain | row 하나가 의미하는 단위 |
| Period | 데이터 기간 |
| Key Columns | join, grouping, unique check에 쓸 컬럼 |
| Metrics | 계산 가능한 지표 후보 |
| Limits | 빠진 컬럼, 신뢰도 낮은 값, 정의 불명확한 값 |

## Quality Checks

- row count
- column type
- missing values
- duplicate keys
- outlier
- join key uniqueness
- source total과 subtotal

## Analysis Output

좋은 분석 산출물은 다음을 분리한다.

- 관측된 사실
- 계산된 지표
- 해석 또는 추정
- 확인 필요 사항
- 권장 action

## Data Cleaning Variant

데이터가 지저분하면 분석 전에 Data Cleaning Harness로 전환한다.

```text
원본 보존
-> 컬럼/타입 확인
-> 결측/중복/이상치 탐지
-> 정제 규칙 제안
-> cleaned copy 생성
-> 변경 내역 기록
```

원본 파일은 수정하지 않는다. 정제 결과는 별도 파일이나 별도 tab으로 만든다.

## Metric Discovery Variant

공식 KPI가 없으면 metric을 단정하지 않는다. 후보, 계산식, 신뢰도, 확인 필요 사항을 분리한다.

| 지표 후보 | 계산식 | 신뢰도 | 확인 필요 |
|---|---|---|---|
| CTR | clicks / impressions | 높음 | impressions 정의 |
| CVR | conversions / clicks | 중간 | conversion 기준 |
| CPA | spend / conversions | 중간 | 비용 세금 포함 여부 |
| ROAS | revenue / spend | 중간 | revenue가 내부 실매출인지 |
| CAC | ad spend / new customers | 낮음 | 신규 고객 식별 컬럼 |

## Verification

- 총합과 부분합이 맞는가?
- 샘플 row를 손으로 계산했을 때 같은 결과가 나오는가?
- join match rate와 unmatched row가 기록되어 있는가?
- 기간과 필터가 명시되어 있는가?
- 불확실한 해석이 사실처럼 쓰이지 않았는가?
