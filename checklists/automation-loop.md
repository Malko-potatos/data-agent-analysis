# Automation Loop Checklist

데이터 분석 결과를 자동화로 전환하기 전 확인한다.

## Before Automation

- [ ] 1회 분석 결과가 검증되었다.
- [ ] metric 정의와 계산식이 문서화되었다.
- [ ] source total 또는 기존 export와 대조했다.
- [ ] 반복 실행할 가치가 있는 업무인지 확인했다.
- [ ] 자동화가 만들 산출물의 독자가 명확하다.

## Trigger And Schedule

- [ ] 실행 주기 또는 trigger가 정해져 있다.
- [ ] 데이터 갱신 시각과 자동화 실행 시각이 맞는다.
- [ ] 실패 시 재시도 기준이 있다.
- [ ] 마지막 성공 시각을 표시한다.

## Verification

- [ ] row count를 기록한다.
- [ ] total/subtotal을 source와 대조한다.
- [ ] sample row check를 한다.
- [ ] join match rate와 unmatched row를 기록한다.
- [ ] 비정형 신호는 원문 링크 또는 ID를 남긴다.

## Human Approval

- [ ] 자동화가 직접 action을 실행하는지, draft/queue만 만드는지 구분했다.
- [ ] 발송, 삭제, DB write, 권한 변경은 승인 전 실행하지 않는다.
- [ ] 승인 요청에는 대상, payload, 위험, 되돌리기 방안이 포함된다.

## Failure Recovery

- [ ] 실패 단계가 기록된다.
- [ ] 실패 원인이 기록된다.
- [ ] 마지막 성공 결과와 비교할 수 있다.
- [ ] 사람이 처리해야 할 queue가 남는다.
