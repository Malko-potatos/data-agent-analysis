# Harness Books Notes

참고 저장소: https://github.com/wquguru/harness-books

이 메모는 harness-books의 관점을 데이터 분석/자동화 agent 교육에 맞게 요약한 것이다.

## Useful Ideas For This Workbook

- 프롬프트는 control plane의 일부다.
- 도구, 권한, 상태, 복구, 검증, 팀 규칙을 함께 설계해야 한다.
- 모델의 실수는 예외가 아니라 runtime에서 다룰 정상 가능성으로 본다.
- 검증은 에이전트 내부 자기 평가가 아니라 별도 계층으로 분리한다.
- 반복 작업은 개인 팁이 아니라 skill, checklist, template, automation으로 제도화한다.

## Applied To Data Analysis Agents

| Harness idea | Data analysis translation |
|---|---|
| Tool boundary | DB/API/file 접근 권한을 명확히 한다. |
| Permission system | 발송, 삭제, 배포, DB write를 승인 action으로 분리한다. |
| Context governance | 분석 기간, 필터, source, metric 정의를 산출물에 남긴다. |
| Recovery | 실패 단계와 마지막 성공 상태를 기록한다. |
| Verification | row count, total, sample check, join match rate를 별도 검증한다. |
| Institution | 반복 작업을 template, checklist, skill로 고정한다. |

## Student Takeaway

분석 agent를 잘 쓰는 학생은 "좋은 문장"만 쓰지 않는다. 어떤 작업을 어느 경계 안에서 실행하고, 어떤 증거로 맞았다고 볼지 설계한다.
