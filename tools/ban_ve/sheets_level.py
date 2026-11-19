from common import *
from section import CONC

# ------------------------------------------------------------------ PT-03 CAO DO
ROAD, YARD = ROAD_Z, YARD_Z  # chu nha do 19/11/2026 (so voi nen nha chinh ±0)
RED_ = (.8, .1, .1); BLUE_ = (.1, .35, .75); GRN_ = (.1, .5, .2)


def arrow(v, p, q, col, lw=.4):
    v.line([p, q], lw, col)
    X0, Y0 = v.P(*p); X1, Y1 = v.P(*q); import math
    a = math.atan2(Y1 - Y0, X1 - X0)
    v.sh.poly([(X1, Y1), (X1 - 2.2 * math.cos(a - .4), Y1 - 2.2 * math.sin(a - .4)), (X1 - 2.2 * math.cos(a + .4), Y1 - 2.2 * math.sin(a + .4))], fill=col, edge=col, lw=.1)


def house(v, f):
    """nha chinh cat doc tai a=16: hien b2.5-5.5, tuong truoc + cua D1 tai b5.5; f = cao do nen"""
    v.rect(2.5, f - .12, 8.5, f, fill=CONC, edge=BLK, lw=.35); v.hatch(2.5, f - .12, 8.5, f, sp=1.4, col=GRY)
    if f > 0: v.rect(2.5, -.12, 8.5, f - .12, fill=(.97, .94, .85), edge=BLK, lw=.2); v.text(6.5, f / 2 - .1, f'đắp cát nâng nền +{f:.2f}'.replace('.', ','), 1.6, anc='c', va='m', col=GRY)
    v.rect(2.5, -.12, 2.75, 3.6, fill=(1, 1, 1), edge=BLK, lw=.3)                       # cot hien
    v.rect(5.5, 3.0, 5.7, 3.6, fill=(.88, .88, .88), edge=BLK, lw=.35)                  # tuong tren cua D1
    v.line([(5.6, f), (5.6, 3.0)], .2, GRY, [1.5, 1]); v.text(5.75, 1.5, 'D1', 1.8, col=BLU)
    v.line([(5.7, 3.3), (8.5, 3.3)], .35); v.text(7.1, 3.36, f'trần +3,30 → còn {3.3 - f:.2f}m'.replace('.', ','), 1.6, anc='c')


def road(v):
    v.rect(-1.5, ROAD - .15, 0.5, ROAD, fill=(.35, .35, .35), edge=BLK, lw=.3)
    v.line([(-1.5, -.5), (8.5, -.5)], .1, GRY, [1, 1])


def sheet_level(sh):
    sh.text(30, 280, 'CAO ĐỘ LỘ – SÂN – NỀN & THOÁT NƯỚC MẶT (số liệu chủ nhà đo 19/11/2026)', 4, bold=True)
    sh.text(30, 274, 'Mặt lộ cao hơn nền nhà chính 0,70m · sân xi măng thấp hơn nền nhà chính 0,05m · cửa sắt D1 → mép lộ ~5,0m.', 2.1)
    # --- hien trang ---
    v = View(sh, 40, 172, 50, -1.5, 0)
    road(v); house(v, 0.0)
    v.line([(0.5, ROAD - .15), (0.8, YARD)], .3, BLK, [1.2, .8]); v.text(0.0, .3, 'bậc/taluy ~0,75', 1.5, col=GRY)
    v.rect(0.8, YARD - .1, 2.5, YARD, fill=CONC, edge=BLK, lw=.3)
    arrow(v, (-1.2, ROAD + .25), (0.6, ROAD + .1), RED_); arrow(v, (0.9, YARD + .25), (2.3, YARD + .2), RED_); arrow(v, (2.8, .2), (5.3, .15), RED_)
    v.text(1.0, 1.15, 'Mưa lớn: nước mặt lộ đổ xuống sân; nền chỉ cao hơn sân 5cm → nước dâng quá 5cm là vào hiên', 1.8, col=RED_)
    for x, z, t in [(-1.3, ROAD, '+0,70 lộ'), (1.0, YARD, '−0,05 sân'), (3.0, 0, '±0,00 nền')]: v.level(x, z, t, 1.8)
    v.dim_chain([0.5, 2.5, 5.5], -0.35, True, -1)
    v.dim_chain([YARD, 0, ROAD], 8.3, False, -1)
    view_title(sh, 40, 262, 'A. HIỆN TRẠNG – CẮT DỌC QUA NHÀ CHÍNH (từ lộ vào)', '1:50')
    # --- de xuat ---
    v = View(sh, 40, 70, 50, -1.5, 0)
    road(v); house(v, 0.0)
    v.rect(0.5, ROAD - .4, 0.7, 0.80, fill=(.8, .8, .8), edge=GRN_, lw=.45); v.text(0.75, 0.85, 'gờ/bó vỉa chắn nước +0,80 (đợt 2: chân tường rào kín)', 1.6, col=GRN_)
    v.poly([(0.7, YARD - .1), (2.3, -0.17), (2.3, -0.07), (0.7, YARD)], fill=CONC, edge=GRN_, lw=.35); v.text(1.0, YARD + .12, 'láng lại dốc 4% về rãnh', 1.5, col=GRN_)
    v.rect(2.3, -.17, 2.5, -.07, fill=(1, 1, 1), edge=GRN_, lw=.45); v.text(2.0, -.62, 'rãnh nông B200 nắp song, đáy −0,17 → ống Ø114 dốc 0,5–1% → xả ao ở −0,22 (> triều −0,30)', 1.6, col=GRN_)
    v.rect(5.48, 0, 5.72, .05, fill=GRN_, edge=GRN_, lw=.2); v.text(5.8, .1, 'ngạch D1 +0,05', 1.5, col=GRN_)
    arrow(v, (1.0, YARD + .05), (2.25, 0.02), GRN_)
    # dot 2 net dut
    v.line([(2.5, .45), (8.5, .45)], .5, BLUE_, [2, 1]); v.line([(0.7, .43), (2.3, .40)], .5, BLUE_, [2, 1])
    v.text(5.9, .55, 'Đợt 2: nền +0,45 (cả nhà chính + nhà phụ)', 1.6, col=BLUE_); v.text(-1.4, .1, 'Đợt 2: sân +0,40 (thấp hơn nền 5cm)', 1.6, col=BLUE_)
    for x, z, t in [(-1.3, ROAD, '+0,70 lộ'), (3.0, 0, '±0,00 nền')]: v.level(x, z, t, 1.8)
    view_title(sh, 40, 152, 'B. ĐỀ XUẤT – ĐỢT 1 (xanh lá) + ĐỢT 2 (xanh dương nét đứt)', '1:50')
    y = notes(sh, 255, 262, 'ĐÁNH GIÁ', [
        'Lô đất là chỗ trũng: nền nhà thấp hơn lộ 0,70m (không phải 0,50m như giả định) → mọi nước mặt lộ đổ về sân. Nền chỉ cao hơn sân 5cm → mưa lớn nước đọng quá 5cm là tràn vào hiên. Đây là việc phải xử lý NGAY đợt 1, trước cả cửa sổ.',
        'Không thể nâng nền lên bằng lộ: nâng +0,75 thì trần nhà chính còn 2,55m, mép mái nhà phụ còn 2,15m, cửa nhà phụ (lanh tô +2,65) còn 1,90m → phải làm lại mái + cửa. Không đáng.',
    ], 62, 1.8)
    sh.text(255, y - 1, 'SO SÁNH PHƯƠNG ÁN CAO ĐỘ', 2.4, bold=True)
    y = table(sh, 255, y - 3, [('PA', 13), ('Nền', 16), ('Trần nhà chính', 22), ('Chống nước', 52), ('Đánh giá', 47)], [
        ['1', '±0', '3,30', 'gờ +0,80 + rãnh nông tự chảy ra ao', 'rẻ nhất; nền chỉ cao hơn sân 5cm, rãnh phải thông'],
        ['2', '+0,45', '2,85', 'tường rào kín + gờ cổng +0,80, sân +0,40, rãnh', 'KHUYẾN NGHỊ – giữ nguyên các cao độ chừa sẵn'],
        ['3', '+0,75', '2,55', 'nền cao hơn lộ 5cm', 'phải nâng mái + làm lại cửa nhà phụ, đắp ~100m³'],
    ], 1.7, 4.0)
    notes(sh, 255, y - 4, 'GIẢI PHÁP ĐỀ XUẤT', [
        'ĐỢT 1 (làm ngay, ~6–10tr): (1) gờ/bó vỉa BT cao hơn lộ 10cm dọc ranh mặt tiền, cổng có gờ dốc lượn; (2) láng lại sân dốc 2–4% RA XA nhà; (3) rãnh B200 nắp song dọc mép hiên + trước nhà phụ → hố ga → ống Ø114 ra mương/ao; (4) ngạch cửa D1, D7 +0,05; (5) KHÔNG CẦN BƠM nếu cửa xả ra ao đặt ≥ −0,22 (cao hơn triều cao nhất −0,30 ≥8cm): rãnh nông + ống Ø114 dốc 0,5–1%, đường ống ngắn nhất ra ao; van lật ở cửa xả phòng triều vượt mức (~0,5tr).',
        'ĐỢT 2 (như kế hoạch): nền +0,45, sân +0,40; tường rào kín 2,6m mặt tiền xây chân đặc cao +0,80 làm luôn tường chắn nước; cổng có gờ +0,80.',
        'Lối xe vào cổng chính: từ lộ +0,70 qua gờ +0,80 xuống sân −0,05 chênh 0,85m → dốc ~14% dài ~6m (sedan qua được, có đoạn chuyển tiếp; 5m thì 17% là quá dốc). Đợt 2 sân +0,40 → dốc ~8%.',
        'Nắp bể tự hoại (nhô +0,35) nằm trên đường dốc: nâng cổ nắp theo mặt dốc, ụ chắn bánh [12] giữ nguyên.',
        'Kiểm tra tự chảy: sân −0,05 → đáy rãnh −0,17 → cửa xả −0,22 vẫn cao hơn triều cao nhất −0,30. Ống Ø114 dốc 1% thoát ~6 L/s, gấp ~7 lần mưa 50mm/h trên ~60m² sân (0,8 L/s). Điều kiện: đường ống ra ao ≤15m (dài hơn thì dốc 0,5%). Nước mưa mái dẫn riêng ra ao.',
        'Bãi thấm bể tự hoại (đáy −0,10) chỉ cao hơn triều 20cm: lúc triều cường thấm kém – giữ ống tràn ra mương có van một chiều.',
    ], 62, 1.8)


