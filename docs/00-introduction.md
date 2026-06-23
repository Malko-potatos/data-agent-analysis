# 00. Introduction

이 워크북은 학생들이 자연어 요구사항을 곧바로 프롬프트로 쓰지 않고, 데이터 분석과 자동화 작업으로 라우팅하는 방법을 연습하도록 만든다.

좋은 agent 활용은 "말을 잘 거는 기술"에 머물지 않는다. 사용자의 목적, 데이터 위치, 반복성, 위험, 검증 기준을 분해하고, 그 일을 안정적으로 수행할 수 있는 workflow harness를 설계하는 능력이 필요하다.

## Learning Outcomes

이 워크북을 마치면 학생은 다음을 할 수 있어야 한다.

- 사용자 발화를 요구사항 카드로 분해한다.
- 데이터 분석 use case와 자동화 use case를 각각 찾고 결합한다.
- 데이터 접근 방식과 필요한 스킬/도구를 고른다.
- 실행 프롬프트를 목표, 입력, 절차, 제약, 검증, 출력으로 나눈다.
- 정적 검증 기준과 승인 경계를 별도 계층으로 작성한다.
- 반복 작업을 템플릿, 체크리스트, 자동화, skill 후보로 정리한다.

## Core Principle

```text
프롬프트는 단독 산출물이 아니다.
프롬프트는 도구, 권한, 상태, 복구, 검증과 함께 설계되는 control plane의 일부다.
```

## Workbook Scope

포함하는 작업:

- CSV, Excel, DB, Google Sheet 분석
- 데이터 정제와 품질 점검
- KPI와 metric discovery
- 광고, 유입, 매출, 환불, 평판의 다중 소스 분석
- 운영 대시보드 자동화
- 분석 결과의 반복 리포트, 알림, 검토 queue, meeting follow-up 전환
- 커뮤니티, 이메일, Slack, 리뷰 등 비정형 신호 분석
- 이미 만든 agent 구조 점검

제외하는 작업:

- Native iOS/macOS 앱 구현 중심 use case
- 모델 API 세부 구현 튜토리얼
- 특정 회사의 내부 데이터 구조에 종속된 분석

## Student Workflow

1. 자연어 요구사항을 받는다.
2. 요구사항 해부 카드에 맞춰 정보를 채운다.
3. Data lane에서 가까운 분석 use case를 고른다.
4. Automation lane에서 반복 실행, 알림, queue, follow-up, verified operation 중 무엇이 필요한지 고른다.
5. 두 lane을 결합한 Agent Workflow Harness를 선택한다.
6. 필요한 데이터, 도구, 권한, 스킬을 적는다.
7. 실행 프롬프트를 작업 명세로 쓴다.
8. 검증 기준과 승인 경계를 붙인다.
9. 반복 작업이면 자동화나 skill 후보로 정리한다.
