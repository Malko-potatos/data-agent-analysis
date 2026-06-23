# Marketing Data Analysis Prompt

```text
유료 광고와 무료 바이럴 채널의 마케팅 성과를 통합 분석해주세요.

목표:
- 채널별 유입, 전환, 매출, 비용, 평판 신호를 비교하고 개선안을 도출합니다.

입력:
- 광고 플랫폼 export/API
- GA 또는 analytics export
- 내부 DB 유입/전환/매출 데이터
- 커뮤니티, 리뷰, 검색 결과 등 평판 데이터

절차:
1. 데이터 소스별 inventory를 작성하세요.
2. 유료 채널과 무료/바이럴 채널을 구분하세요.
3. join key, 기간, 필터, grain을 확인하세요.
4. CTR, CVR, CPA, ROAS 등 계산 가능한 지표를 계산하세요.
5. 정의가 불명확한 지표는 metric 후보로 표시하세요.
6. 평판 데이터는 원문 링크와 함께 키워드와 맥락을 요약하세요.
7. 개선안을 impact, confidence, effort 기준으로 우선순위화하세요.

제약:
- 원본 데이터는 수정하지 마세요.
- 외부 발송이나 광고 캠페인 변경은 하지 마세요.

검증:
- 광고비 total, 전환 total, 매출 total을 source와 대조하세요.
- join match rate와 unmatched row를 기록하세요.
- 샘플 row 3개 이상을 계산식 기준으로 검산하세요.
- 확인한 사실, 추정, 사람 확인 필요 사항을 분리하세요.

출력:
- 데이터 inventory
- 채널별 성과 비교표
- 평판 키워드 요약
- 우선순위 action list
- 데이터 한계와 확인 질문
```
