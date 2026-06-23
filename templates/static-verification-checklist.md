# Static Verification Checklist

## Input Boundary

- [ ] 사용한 파일, DB, API, 화면, 문서가 명시되어 있다.
- [ ] 분석 기간과 필터가 명시되어 있다.
- [ ] 원본 데이터는 보존되어 있다.

## Calculation

- [ ] 지표 정의가 있다.
- [ ] 계산식의 분자와 분모가 명시되어 있다.
- [ ] 제외 조건이 명시되어 있다.
- [ ] total/subtotal이 source와 대조되었다.

## Join

- [ ] join key가 명시되어 있다.
- [ ] key uniqueness를 확인했다.
- [ ] match rate를 기록했다.
- [ ] unmatched row를 기록했다.
- [ ] 중복 row 처리 기준이 있다.

## Interpretation

- [ ] 확인한 사실과 추정을 분리했다.
- [ ] 사람이 판단해야 할 항목을 분리했다.
- [ ] 한계와 누락 데이터를 적었다.

## Approval

- [ ] 발송, 삭제, 배포, 권한 변경을 승인 없이 하지 않았다.
- [ ] 승인이 필요한 action을 별도 목록으로 남겼다.

## Artifact

- [ ] 사람이 리뷰 가능한 산출물로 남겼다.
- [ ] query, script, prompt, template 중 재사용 가능한 요소를 남겼다.
