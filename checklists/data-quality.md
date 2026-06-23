# Data Quality Checklist

## Source

- [ ] 원본 파일 또는 source location을 기록했다.
- [ ] 데이터 기간과 필터를 기록했다.
- [ ] row 하나의 grain을 설명할 수 있다.

## Structure

- [ ] 컬럼명과 타입을 확인했다.
- [ ] primary key 또는 unique key 후보를 확인했다.
- [ ] grouping key와 join key를 분리했다.

## Completeness

- [ ] 결측치 비율을 확인했다.
- [ ] 필수 컬럼의 결측 row를 따로 기록했다.
- [ ] 수집 누락 가능성이 있는 기간을 확인했다.

## Duplicates

- [ ] 중복 기준을 정의했다.
- [ ] 중복 row 수를 기록했다.
- [ ] 제거 또는 보류 기준을 기록했다.

## Outliers

- [ ] 숫자형 컬럼의 극단값을 확인했다.
- [ ] 날짜 범위 밖 row를 확인했다.
- [ ] 음수, 0, 비정상 값의 업무 의미를 확인했다.

## Preservation

- [ ] raw data를 수정하지 않았다.
- [ ] cleaned copy 또는 별도 tab을 만들었다.
- [ ] 변경 내역을 기록했다.
