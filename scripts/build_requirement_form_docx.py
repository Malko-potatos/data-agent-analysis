from pathlib import Path

from docx import Document
from docx.enum.section import WD_SECTION
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT, WD_ROW_HEIGHT_RULE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "templates" / "data-analysis-agent-requirement-form.docx"

BLUE = "2E74B5"
DARK_BLUE = "1F4D78"
INK = "1F2937"
MUTED = "667085"
LIGHT_BLUE_GRAY = "E8EEF5"
LIGHT_GRAY = "F2F4F7"
CALLOUT = "F4F6F9"
BORDER = "C9D3DF"
WHITE = "FFFFFF"


def set_cell_shading(cell, fill):
    tc_pr = cell._tc.get_or_add_tcPr()
    shd = tc_pr.find(qn("w:shd"))
    if shd is None:
        shd = OxmlElement("w:shd")
        tc_pr.append(shd)
    shd.set(qn("w:fill"), fill)


def set_cell_text(cell, text, bold=False, color=INK, size=10.5):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(text)
    run.bold = bold
    run.font.name = "Calibri"
    run.font.size = Pt(size)
    run.font.color.rgb = RGBColor.from_string(color)


def set_table_geometry(table, widths, indent_dxa=120, cell_margin=120):
    tbl = table._tbl
    tbl_pr = tbl.tblPr

    tbl_w = tbl_pr.find(qn("w:tblW"))
    if tbl_w is None:
        tbl_w = OxmlElement("w:tblW")
        tbl_pr.append(tbl_w)
    tbl_w.set(qn("w:type"), "dxa")
    tbl_w.set(qn("w:w"), str(sum(widths)))

    tbl_ind = tbl_pr.find(qn("w:tblInd"))
    if tbl_ind is None:
        tbl_ind = OxmlElement("w:tblInd")
        tbl_pr.append(tbl_ind)
    tbl_ind.set(qn("w:type"), "dxa")
    tbl_ind.set(qn("w:w"), str(indent_dxa))

    tbl_layout = tbl_pr.find(qn("w:tblLayout"))
    if tbl_layout is None:
        tbl_layout = OxmlElement("w:tblLayout")
        tbl_pr.append(tbl_layout)
    tbl_layout.set(qn("w:type"), "fixed")

    cell_mar = tbl_pr.find(qn("w:tblCellMar"))
    if cell_mar is None:
        cell_mar = OxmlElement("w:tblCellMar")
        tbl_pr.append(cell_mar)
    for side, value in (("top", 80), ("bottom", 80), ("start", cell_margin), ("end", cell_margin)):
        child = cell_mar.find(qn(f"w:{side}"))
        if child is None:
            child = OxmlElement(f"w:{side}")
            cell_mar.append(child)
        child.set(qn("w:w"), str(value))
        child.set(qn("w:type"), "dxa")

    grid = tbl.tblGrid
    if grid is None:
        grid = OxmlElement("w:tblGrid")
        tbl.insert(0, grid)
    for child in list(grid):
        grid.remove(child)
    for width in widths:
        col = OxmlElement("w:gridCol")
        col.set(qn("w:w"), str(width))
        grid.append(col)

    for row in table.rows:
        row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
        for idx, cell in enumerate(row.cells):
            cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER
            tc_pr = cell._tc.get_or_add_tcPr()
            tc_w = tc_pr.find(qn("w:tcW"))
            if tc_w is None:
                tc_w = OxmlElement("w:tcW")
                tc_pr.append(tc_w)
            tc_w.set(qn("w:type"), "dxa")
            tc_w.set(qn("w:w"), str(widths[idx]))


def set_table_borders(table, color=BORDER):
    tbl_pr = table._tbl.tblPr
    borders = tbl_pr.find(qn("w:tblBorders"))
    if borders is None:
        borders = OxmlElement("w:tblBorders")
        tbl_pr.append(borders)
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        elem = borders.find(qn(f"w:{edge}"))
        if elem is None:
            elem = OxmlElement(f"w:{edge}")
            borders.append(elem)
        elem.set(qn("w:val"), "single")
        elem.set(qn("w:sz"), "4")
        elem.set(qn("w:space"), "0")
        elem.set(qn("w:color"), color)


def mark_first_row_as_header(table):
    row = table.rows[0]
    tr_pr = row._tr.get_or_add_trPr()
    tbl_header = tr_pr.find(qn("w:tblHeader"))
    if tbl_header is None:
        tbl_header = OxmlElement("w:tblHeader")
        tr_pr.append(tbl_header)
    tbl_header.set(qn("w:val"), "true")


def add_spacer(doc, pts=4):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(pts)
    p.paragraph_format.space_before = Pt(0)
    return p


def add_title(doc):
    p = doc.add_paragraph()
    p.paragraph_format.space_after = Pt(3)
    run = p.add_run("데이터 분석 에이전트 요구사항 카드")
    run.font.name = "Calibri"
    run.font.size = Pt(22)
    run.font.bold = True
    run.font.color.rgb = RGBColor.from_string(DARK_BLUE)

    p = doc.add_paragraph()
    p.style = "Subtitle"
    p.add_run("자연어 요구를 use case, workflow harness, 검증 기준, 승인 경계로 정리하는 실습 양식")


def add_note_box(doc, title, body):
    table = doc.add_table(rows=1, cols=1)
    table.style = "Table Grid"
    set_table_geometry(table, [9360], indent_dxa=120)
    set_table_borders(table, color="D6DEE8")
    mark_first_row_as_header(table)
    cell = table.cell(0, 0)
    set_cell_shading(cell, CALLOUT)
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(3)
    title_run = p.add_run(title)
    title_run.bold = True
    title_run.font.name = "Calibri"
    title_run.font.size = Pt(10.5)
    title_run.font.color.rgb = RGBColor.from_string(DARK_BLUE)
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    run = p.add_run(body)
    run.font.name = "Calibri"
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor.from_string(INK)
    add_spacer(doc, 6)


def add_label_detail_table(doc, rows, widths=(1850, 7510), header=None):
    extra = 1 if header else 0
    table = doc.add_table(rows=len(rows) + extra, cols=2)
    table.style = "Table Grid"
    set_table_geometry(table, list(widths), indent_dxa=120)
    set_table_borders(table)
    mark_first_row_as_header(table)

    start = 0
    if header:
        cell = table.cell(0, 0).merge(table.cell(0, 1))
        set_cell_shading(cell, LIGHT_BLUE_GRAY)
        set_cell_text(cell, header, bold=True, color=DARK_BLUE, size=10.5)
        start = 1

    for idx, (label, guide) in enumerate(rows, start=start):
        left, right = table.cell(idx, 0), table.cell(idx, 1)
        set_cell_shading(left, LIGHT_GRAY)
        set_cell_text(left, label, bold=True, color=DARK_BLUE, size=10)
        set_cell_text(right, guide, color=MUTED, size=10)

    add_spacer(doc, 8)
    return table


def add_three_col_table(doc, headers, rows, widths, header_fill=LIGHT_BLUE_GRAY):
    table = doc.add_table(rows=len(rows) + 1, cols=3)
    table.style = "Table Grid"
    set_table_geometry(table, widths, indent_dxa=120)
    set_table_borders(table)
    mark_first_row_as_header(table)
    for idx, header in enumerate(headers):
        cell = table.cell(0, idx)
        set_cell_shading(cell, header_fill)
        set_cell_text(cell, header, bold=True, color=DARK_BLUE, size=10)
    for r_idx, row in enumerate(rows, start=1):
        for c_idx, text in enumerate(row):
            cell = table.cell(r_idx, c_idx)
            set_cell_text(cell, text, color=MUTED if c_idx > 0 else INK, size=9.8)
    add_spacer(doc, 8)
    return table


def add_checklist_table(doc, title, items):
    table = doc.add_table(rows=len(items) + 1, cols=2)
    table.style = "Table Grid"
    set_table_geometry(table, [520, 8840], indent_dxa=120)
    set_table_borders(table)
    mark_first_row_as_header(table)
    header = table.cell(0, 0).merge(table.cell(0, 1))
    set_cell_shading(header, LIGHT_BLUE_GRAY)
    set_cell_text(header, title, bold=True, color=DARK_BLUE, size=10.5)
    for idx, item in enumerate(items, start=1):
        set_cell_text(table.cell(idx, 0), "[ ]", color=DARK_BLUE, size=10)
        table.cell(idx, 0).paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_cell_text(table.cell(idx, 1), item, color=INK, size=10)
    add_spacer(doc, 8)


def add_response_box(doc, title, guide, height_rows=4):
    table = doc.add_table(rows=2, cols=1)
    table.style = "Table Grid"
    set_table_geometry(table, [9360], indent_dxa=120)
    set_table_borders(table)
    mark_first_row_as_header(table)
    set_cell_shading(table.cell(0, 0), LIGHT_BLUE_GRAY)
    set_cell_text(table.cell(0, 0), title, bold=True, color=DARK_BLUE, size=10.5)
    cell = table.cell(1, 0)
    set_cell_text(cell, guide, color=MUTED, size=10)
    for _ in range(height_rows):
        p = cell.add_paragraph()
        p.paragraph_format.space_after = Pt(0)
        p.add_run(" ")
    add_spacer(doc, 8)


def add_page_break(doc):
    doc.add_page_break()


def configure_styles(doc):
    section = doc.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)
    section.header_distance = Inches(0.492)
    section.footer_distance = Inches(0.492)

    styles = doc.styles
    normal = styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(11)
    normal.font.color.rgb = RGBColor.from_string(INK)
    normal.paragraph_format.space_after = Pt(6)
    normal.paragraph_format.line_spacing = 1.25

    subtitle = styles["Subtitle"]
    subtitle.font.name = "Calibri"
    subtitle.font.size = Pt(11)
    subtitle.font.color.rgb = RGBColor.from_string(MUTED)
    subtitle.paragraph_format.space_after = Pt(10)

    for style_name, size, color, before, after in [
        ("Heading 1", 16, BLUE, 18, 10),
        ("Heading 2", 13, BLUE, 14, 7),
        ("Heading 3", 12, DARK_BLUE, 10, 5),
    ]:
        style = styles[style_name]
        style.font.name = "Calibri"
        style.font.size = Pt(size)
        style.font.bold = True
        style.font.color.rgb = RGBColor.from_string(color)
        style.paragraph_format.space_before = Pt(before)
        style.paragraph_format.space_after = Pt(after)
        style.paragraph_format.keep_with_next = True

    header = section.header.paragraphs[0]
    header.text = "Data Analysis Agent Workbook"
    header.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    header.runs[0].font.name = "Calibri"
    header.runs[0].font.size = Pt(9)
    header.runs[0].font.color.rgb = RGBColor.from_string(MUTED)

    footer = section.footer.paragraphs[0]
    footer.text = "Requirement Card · Harness Spec · Verification Boundary"
    footer.alignment = WD_ALIGN_PARAGRAPH.CENTER
    footer.runs[0].font.name = "Calibri"
    footer.runs[0].font.size = Pt(8.5)
    footer.runs[0].font.color.rgb = RGBColor.from_string(MUTED)


def build():
    doc = Document()
    configure_styles(doc)
    add_title(doc)
    add_note_box(
        doc,
        "사용 방법",
        "이 문서는 에이전트 실행 전 사용자의 자연어 요구를 정리하고, 실행 후 검증 기준으로 다시 확인하기 위한 양식입니다. "
        "빈칸을 모두 채우는 것보다 확인된 사실, 추정, 확인 필요 사항을 분리하는 것이 더 중요합니다.",
    )

    add_label_detail_table(
        doc,
        [
            ("프로젝트", "프로젝트명 또는 분석 주제"),
            ("작성자", "작성자 이름"),
            ("검토자", "데이터/도메인/승인 담당자"),
            ("작성일", "YYYY-MM-DD"),
            ("버전", "v0.1"),
        ],
        header="0. 문서 정보",
    )

    add_response_box(
        doc,
        "1. 원 요구 기록",
        "사용자 발화를 가능한 한 원문 그대로 붙여넣습니다. 요약하지 말고, 모호한 표현도 보존합니다.",
        height_rows=5,
    )

    doc.add_heading("2. 요구사항 카드", level=1)
    add_label_detail_table(
        doc,
        [
            ("사용자", "누가 결과를 보는가? 예: 경영진, 재무 담당, 마케팅 담당, 운영자"),
            ("목적", "무엇을 알고 싶거나 개선하고 싶은가?"),
            ("데이터", "데이터는 어디 있는가? DB, GA, 광고 플랫폼, 어드민, CSV, 커뮤니티 등"),
            ("현재 방식", "지금은 어떻게 처리하는가? 수동 집계, export, 기존 agent, 대시보드 등"),
            ("원하는 변화", "무엇이 달라지길 원하는가? 자동화, 대시보드, 리포트, 개선안 등"),
            ("반복성", "일회성인가 반복 업무인가? 매일, 매주, 월간, 상시 모니터링 등"),
            ("위험", "민감정보, 잘못된 집계, 외부 발송, DB 변경, 비용 발생 등"),
            ("검증", "무엇과 대조하면 맞았다고 볼 수 있는가? 어드민 export, DB total, 기존 dashboard 등"),
        ],
        widths=(1620, 7740),
        header="요구사항 카드 작성란",
    )

    add_three_col_table(
        doc,
        ["구분", "내용", "메모"],
        [
            ("확인된 사실", "이미 사용자 또는 source로부터 확인한 내용", ""),
            ("추정", "그럴 가능성이 있으나 아직 확인되지 않은 내용", ""),
            ("확인 필요", "실행 전에 물어봐야 하는 질문", ""),
        ],
        widths=[1560, 4680, 3120],
    )

    add_page_break(doc)
    doc.add_heading("3. Use Case 라우팅", level=1)
    add_label_detail_table(
        doc,
        [
            ("가까운 Codex use case", "예: Analyze datasets and ship reports, Query tabular data, Clean and prepare messy data"),
            ("선택한 Harness", "예: Data Analysis, Data Cleaning, Metric Discovery, Dashboard Automation, Agent Audit"),
            ("선택 이유", "요구사항 카드의 어떤 항목 때문에 이 harness가 맞는가?"),
            ("제외한 Harness", "비슷하지만 이번에는 선택하지 않은 harness와 이유"),
            ("필요 도구", "spreadsheet, DB connector, browser/chrome, Gmail/Slack, automation 등"),
        ],
        header="라우팅 결정",
    )

    add_checklist_table(
        doc,
        "라우팅 점검",
        [
            "결과물이 일회성 분석인지 반복 대시보드인지 구분했다.",
            "데이터 정제가 먼저 필요한지 판단했다.",
            "공식 metric이 있는지, metric discovery가 필요한지 판단했다.",
            "외부 발송, 삭제, 배포, DB write 같은 승인 action을 확인했다.",
            "모르는 내용은 추정하지 않고 확인 필요로 남겼다.",
        ],
    )

    doc.add_heading("4. Harness Spec", level=1)
    add_response_box(doc, "Goal", "최종적으로 무엇이 완성되어야 하는가?", height_rows=2)
    add_three_col_table(
        doc,
        ["Input Source", "위치/권한", "기간/필터/Grain"],
        [
            ("", "", ""),
            ("", "", ""),
            ("", "", ""),
        ],
        widths=[2600, 3220, 3540],
    )
    add_three_col_table(
        doc,
        ["Tool / Skill / Plugin", "사용 목적", "권한 경계"],
        [
            ("", "", ""),
            ("", "", ""),
            ("", "", ""),
        ],
        widths=[2700, 3660, 3000],
    )

    add_page_break(doc)
    doc.add_heading("5. 실행 절차와 제약", level=1)
    add_three_col_table(
        doc,
        ["Step", "작업", "완료 기준"],
        [
            ("1", "데이터 inventory", ""),
            ("2", "품질 점검 또는 정제", ""),
            ("3", "metric 정의 또는 discovery", ""),
            ("4", "분석/자동화/대시보드 설계", ""),
            ("5", "검증과 산출물 정리", ""),
        ],
        widths=[820, 4440, 4100],
    )
    add_checklist_table(
        doc,
        "제약 조건",
        [
            "원본 데이터와 기존 코드를 임의로 수정하지 않는다.",
            "기본 데이터 접근은 read-only로 둔다.",
            "민감정보는 필요한 범위만 사용하고 외부 전송하지 않는다.",
            "발송, 삭제, 배포, 권한 변경, DB write는 승인 전 실행하지 않는다.",
            "실패하면 실패 단계, 입력 범위, 마지막 성공 상태를 남긴다.",
        ],
    )

    doc.add_heading("6. 정적 검증 기준", level=1)
    add_checklist_table(
        doc,
        "검증 체크리스트",
        [
            "사용한 파일, DB, API, 화면, 문서를 기록했다.",
            "분석 기간과 필터를 기록했다.",
            "row count와 total/subtotal을 source와 대조했다.",
            "계산식의 분자, 분모, 제외 조건을 명시했다.",
            "join key, match rate, unmatched row를 기록했다.",
            "샘플 row를 수동 검산하거나 계산식을 설명했다.",
            "확인한 사실, 추정, 사람 확인 필요 사항을 분리했다.",
            "사람이 리뷰 가능한 산출물로 남겼다.",
        ],
    )

    add_page_break(doc)
    doc.add_heading("7. 승인 경계", level=1)
    add_checklist_table(
        doc,
        "승인 없이 실행하지 않을 Action",
        [
            "이메일, Slack, DM, 댓글, 게시글 발송",
            "파일 삭제 또는 원본 덮어쓰기",
            "DB write, schema 변경, 권한 변경",
            "외부 배포 또는 비용 발생 action",
            "민감정보가 포함된 데이터 외부 반출",
        ],
    )
    add_label_detail_table(
        doc,
        [
            ("Action", "실행하려는 일"),
            ("Target", "수신자, 시스템, 파일, DB, 서비스"),
            ("Payload", "발송문, 변경 내용, query, 배포 대상 등"),
            ("Risk", "실패/오류/민감정보/비용 위험"),
            ("Rollback", "되돌리기 또는 중지 계획"),
            ("Approval", "승인자와 승인 시각"),
        ],
        header="승인 요청 양식",
    )

    doc.add_heading("8. 실행 프롬프트 초안", level=1)
    for title, guide in [
        ("목표", "무엇을 알고 싶거나 완성하고 싶은가?"),
        ("입력", "파일, URL, 앱, API, DB, Slack/Gmail/GitHub 등 출처는 무엇인가?"),
        ("역할", "분석가, 데이터 감사자, 구현자, QA 담당 등"),
        ("절차", "먼저 inventory를 하고, 그 다음 정제/분석/작성/검증으로 진행한다."),
        ("제약", "원본 보존, 외부 전송 금지, read-only, 승인 필요 action 등"),
        ("검증", "row count, total, sample check, screenshot, source link 등"),
        ("출력", "표, 리포트, dashboard spec, action queue, 확인 질문 등"),
    ]:
        add_response_box(doc, title, guide, height_rows=2)

    add_page_break(doc)
    doc.add_heading("9. 검토 결정", level=1)
    add_checklist_table(
        doc,
        "실행 전 최종 확인",
        [
            "요구사항 카드가 사용자 의도와 맞는다.",
            "선택한 harness와 제외한 harness의 이유가 설명되어 있다.",
            "필요 데이터와 접근 권한이 확인되었다.",
            "검증 기준이 최소 L2 이상이다.",
            "승인 필요한 action이 분리되어 있다.",
        ],
    )
    add_label_detail_table(
        doc,
        [
            ("결정", "실행 / 보류 / 추가 질문 / 다른 harness로 변경"),
            ("이유", "결정 근거"),
            ("다음 작업", "에이전트 실행, 데이터 요청, 검토 회의, 자동화 설계 등"),
        ],
        header="리뷰 결과",
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUT)
    print(OUT)


if __name__ == "__main__":
    build()
