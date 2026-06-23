# Agent Audit Prompt

```text
기존 데이터 분석 agent의 구조를 점검해주세요.

목표:
- 현재 agent의 입력, 처리, 출력, 검증 구조를 파악하고 개선안을 제안합니다.

입력:
- agent 코드 또는 설정
- agent가 사용하는 데이터 source
- 기존 출력물 또는 로그
- 기대하는 업무 목적

절차:
1. agent의 입력 source와 권한을 inventory로 정리하세요.
2. 처리 단계와 계산식을 추적하세요.
3. 출력물이 어떤 의사결정에 쓰이는지 정리하세요.
4. 검증 단계가 있는지 확인하세요.
5. 실패 가능성과 승인 경계를 찾으세요.
6. 반복 가능하면 skill, automation, dashboard 후보로 분리하세요.

제약:
- 승인 없이 코드 변경, 배포, DB write를 하지 마세요.
- 실제 외부 발송이나 삭제 action을 실행하지 마세요.

검증:
- 입력 누락 가능성을 확인하세요.
- 계산식 오류 가능성을 확인하세요.
- source total과 output total 대조 여부를 확인하세요.
- 실패/복구 로그가 있는지 확인하세요.

출력:
- 현재 agent 구조표
- 검증 gap 목록
- 위험도별 문제
- 개선 architecture
- 우선순위 action list
- skill/automation 전환 후보
```
