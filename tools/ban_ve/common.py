from engine import *
from model import *

PROJECT = 'CẢI TẠO NHÀ Ở – NHÀ DUYÊN HẢI'
SUB = 'Gói đợt 1 "dọn vào ở" + chừa sẵn đợt 2'
SITE = 'Thửa 320, tờ bản đồ 51 – Duyên Hải, tỉnh Vĩnh Long'
OWNER = 'Nguyễn Mạnh Tiến'
DATE = '19/11/2026'
VER = 'v1.1'
FX0, FY0, FX1, FY1 = 25, 10, 410, 287
TBX = 250  # mep trai khung ten
TBY = 62   # mep tren khung ten


def frame(sh, total):
    sh.rect(5, 5, 415, 292, edge=BLK, lw=.2, layer='KHUNG')
    sh.rect(FX0, FY0, FX1, FY1, edge=BLK, lw=.7, layer='KHUNG')
    # khung ten
    x0, y0, x1, y1 = TBX, FY0, FX1, TBY
    sh.rect(x0, y0, x1, y1, fill=(1, 1, 1), edge=BLK, lw=.5, layer='KHUNG')
    L = lambda pts, lw=.25: sh.line(pts, lw, BLK, None, 'KHUNG')
    L([(x0, 50), (x1, 50)]); L([(x0, 38), (x1, 38)]); L([(x0, 22), (x1, 22)])
    L([(330, 10), (330, 38)]); L([(370, 10), (370, 22)]); L([(290, 10), (290, 22)])
    t = lambda x, y, s, h=2.0, **k: sh.text(x, y, s, h, layer='KHUNG', **k)
    t(x0 + 2, 57.5, 'CÔNG TRÌNH', 1.6, col=GRY); t(x0 + 2, 52.5, PROJECT, 3.0, bold=True)
    t(x1 - 2, 57.5, SUB, 1.7, anc='r', col=GRY)
    t(x0 + 2, 46, 'Địa điểm: ' + SITE, 1.9); t(x0 + 2, 41, 'Chủ nhà: ' + OWNER, 1.9)
    t(x1 - 2, 41, 'Đơn vị đo: mm · Cao độ: m', 1.7, anc='r', col=GRY)
    t(x0 + 2, 34.5, 'TÊN BẢN VẼ', 1.6, col=GRY)
    for i, ln in enumerate(wrap(sh.title, 40)[:2]): t(x0 + 2, 29.5 - i * 4.2, ln, 2.8, bold=True)
    t(332, 34.5, 'KÝ HIỆU', 1.6, col=GRY); t(370, 26, sh.no, 6, anc='c', bold=True)
    t(332, 24, f'Tờ {sh.idx}/{total}', 1.8)
    t(x0 + 2, 18, 'TỈ LỆ', 1.6, col=GRY); t(x0 + 2, 12.5, sh.scale, 2.6, bold=True)
    t(292, 18, 'NGÀY · PHIÊN BẢN', 1.6, col=GRY); t(292, 12.5, f'{DATE} · {VER}', 2.2)
    t(332, 18, 'LẬP BẢN VẼ', 1.6, col=GRY); t(332, 12.8, 'Claude (AI) cho chủ nhà', 1.7)
    t(372, 18, 'KS KIỂM TRA / KÝ', 1.6, col=GRY); t(372, 12.5, '..............................', 1.8, col=GRY)
    # dong canh bao
    sh.text(FX0 + 2, 6.6, 'Bản vẽ lập từ mô hình 3D + thuyết minh 17/11/2026 và ảnh hiện trạng. Kích thước hiện trạng là ước tính – đo kiểm tại chỗ trước khi thi công. Phần kết cấu cần kỹ sư có chứng chỉ kiểm tra, ký.', 1.7, col=GRY, layer='KHUNG')


def view_title(sh, x, y, t, scale, h=3.2):
    sh.text(x, y, t, h, 'l', 'b', bold=True, layer='CHU')
    w = stringWidth(t, 'FB', fs(h)) / MM
    sh.line([(x, y - 1.2), (x + w, y - 1.2)], .5, BLK, None, 'CHU'); sh.line([(x, y - 2.0), (x + w, y - 2.0)], .15, BLK, None, 'CHU')
    if scale and scale != '–': sh.text(x + w + 3, y, 'TL ' + scale, 2.4, layer='CHU')


def notes(sh, x, y, title, lines, width=60, h=2.0, gap=1.45, title_h=2.6, col=BLK):
    sh.text(x, y, title, title_h, bold=True, col=col)
    y -= title_h + 2
    for ln in lines:
        first = True
        for w in wrap(ln, width):
            sh.text(x + (0 if first else 3), y, w, h, col=col); y -= h * gap; first = False
        y -= .6
    return y


def table(sh, x, y, cols, rows, h=1.9, rh=4.4, head_fill=(.9, .9, .9), wraps=None):
    """cols: [(tieu de, rong mm)]; rows: list of list str. Tra ve y cuoi."""
    W = sum(c[1] for c in cols)
    sh.rect(x, y - rh, x + W, y, fill=head_fill, edge=BLK, lw=.3)
    cx = x
    for t, w in cols:
        sh.rect(cx, y - rh, cx + w, y, edge=BLK, lw=.2)
        sh.text(cx + 1.2, y - rh + 1.3, t, h, bold=True); cx += w
    y -= rh
    for r in rows:
        lines = []
        for i, (t, w) in enumerate(cols):
            n = max(4, int((w - 2) / (h * .8)))
            lines.append(wrap(str(r[i]), n) if r[i] != '' else [''])
        nl = max(len(l) for l in lines); hh = rh + (nl - 1) * h * 1.35
        sh.rect(x, y - hh, x + W, y, edge=BLK, lw=.2)
        cx = x
        for i, (t, w) in enumerate(cols):
            sh.rect(cx, y - hh, cx + w, y, edge=BLK, lw=.15)
            for j, ln in enumerate(lines[i]):
                sh.text(cx + 1.2, y - 1.3 - h - j * h * 1.35, ln, h)
            cx += w
        y -= hh
    cx = x
    for t, w in cols[:-1]:
        cx += w
    # duong doc
    return y


def col_lines(sh, x, ytop, ybot, cols):
    cx = x
    for t, w in cols[:-1]:
        cx += w; sh.line([(cx, ytop), (cx, ybot)], .2, BLK)


def north(sh, X, Y, ang_deg, r=7):
    """mui ten Bac. ang_deg: goc huong Bac tren giay (do, tu truc +x nguoc chieu kim dong ho)."""
    a = math.radians(ang_deg)
    tip = (X + r * math.cos(a), Y + r * math.sin(a)); tail = (X - r * math.cos(a), Y - r * math.sin(a))
    l = (X + r * .45 * math.cos(a + 2.5), Y + r * .45 * math.sin(a + 2.5)); rr = (X + r * .45 * math.cos(a - 2.5), Y + r * .45 * math.sin(a - 2.5))
    sh.circle(X, Y, r * 1.05, edge=BLK, lw=.25, layer='CHU')
    sh.poly([tip, l, (X, Y), rr], fill=BLK, edge=BLK, lw=.2, layer='CHU')
    sh.poly([tail, l, (X, Y)], fill=None, edge=BLK, lw=.2, layer='CHU')
    sh.text(tip[0] + 2.5 * math.cos(a), tip[1] + 2.5 * math.sin(a), 'B', 3, 'c', 'm', bold=True, layer='CHU')


# huong: mat tien (canh mot lo, truc +b) huong Dong Bac (thuyet minh: "mat tien huong Dong Bac, phia song Tay Nam").
# Tren mat bang truc +b huong len -> phia lo (b nho) la Dong Bac => huong Bac tren giay ~ goc 270+45 = 315 do... (Bac = lech 45 do sang trai so voi huong ra lo)
NORTH_PLAN = 319.67  # lo (duoi giay) = Dong Bac -> Bac chi xuong-phai; hong phai = Tay Bac, phia song = Tay Nam (khop thuyet minh)
