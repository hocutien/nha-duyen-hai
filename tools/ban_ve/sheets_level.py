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
    v.rect(0.5, ROAD - .4, 0.7, 0.80, fill=(.8, .8, .8), edge=GRN_, lw=.45); v.text(0.75, 0.85, 'gờ BT +0,80 chỉ đoạn a0–23 (trước ao không làm), có thép chờ = móng tường rào đợt 2', 1.6, col=GRN_)
    v.poly([(0.9, -0.12), (2.5, -0.09), (2.5, -0.05), (0.9, -0.08)], fill=CONC, edge=GRN_, lw=.35); v.text(1.0, YARD + .12, 'sân dốc ~2% RA XA nhà', 1.5, col=GRN_)
    v.poly([(0.7, -0.08), (0.8, -0.17), (0.9, -0.08)], fill=(1, 1, 1), edge=GRN_, lw=.45); v.text(0.6, -.62, 'rãnh hở chữ V láng vữa chân gờ, đáy −0,15 → −0,20, dốc 0,3% chảy ngang (trục a) ra ao; cửa xả ≥ −0,22 (> triều −0,30)', 1.6, col=GRN_)
    v.rect(5.48, 0, 5.72, .05, fill=GRN_, edge=GRN_, lw=.2); v.text(5.8, .1, 'ngạch D1 +0,05', 1.5, col=GRN_)
    arrow(v, (2.3, -0.02), (1.0, -0.05), GRN_)
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
        'ĐỢT 1 (làm ngay, ~3–5tr): (1) gờ BT 200×300 cao hơn lộ 10cm CHỈ đoạn a0–23 (a23–52,6 là ao giáp lộ, nước vào ao không sao), có thép chờ để đợt 2 xây tường rào lên trên, khỏi đập; cổng có gờ dốc lượn; (2) sân dốc ~2% RA XA nhà, về phía gờ; (3) rãnh hở chữ V láng vữa ở chân gờ, dốc 0,3% chảy ngang theo trục a ra ao (a 8→23 hạ ~5cm), không cần rãnh B200 nắp song, hố ga hay ống Ø114 dài; (4) ngạch cửa D1, D7 +0,05; (5) KHÔNG CẦN BƠM: cửa xả ra ao ≥ −0,22 (cao hơn triều cao nhất −0,30), đoạn ống ngắn 1–2m qua bờ ao + van lật (~0,5tr).',
        'ĐỢT 2 (như kế hoạch): nền +0,45, sân +0,40; tường rào kín 2,6m mặt tiền xây chân đặc cao +0,80 làm luôn tường chắn nước; cổng có gờ +0,80.',
        'Xe vào bằng CỔNG PHỤ 4,5m (1 dốc duy nhất): từ lộ +0,70 qua gờ +0,80 xuống sân −0,05 chênh 0,85m → dốc ~14% dài ~6m (sedan qua được, có đoạn chuyển tiếp). Cổng chính chỉ cho người đi bộ: lối 1,2m, 4–5 bậc cao ≤170 + tay vịn. Đợt 2 sân +0,40 → dốc ~8%.',
        'Bể tự hoại (nắp nhô +0,35) nằm sau cổng chính, không có xe đi qua [12] nên không cần ụ chắn bánh, không đắp dốc lên bể. Tấm lót đáy bể 2,0×2,8×0,20m (≈1,1m³, ~15kN ngập nước) + 2 đai neo: đủ giữ bể rỗng khi nước ngầm ở −0,3 (lực đẩy nổi ~11kN; tấm 0,1m cũ chỉ ~5,5kN).',
        'Kiểm tra tự chảy: sân −0,05 → đáy rãnh −0,15 (đầu a8) → −0,20 (a23) → cửa xả −0,22, vẫn cao hơn triều cao nhất −0,30. Rãnh V miệng 200 sâu 70, dốc 0,3% thoát ~2,4 L/s, gấp ~3 lần mưa 50mm/h trên ~60m² sân (0,8 L/s). Nước mưa mái dẫn riêng ra ao bằng ống Ø90 đi nổi.',
        'Bãi thấm bể tự hoại (ống −0,10, đáy đá −0,30) trùng mức triều cao nhất: gần như chắc thấm kém. Làm hố thử thấm + đo mực nước ngầm mùa mưa TRƯỚC; chưa mua ống, vải địa khi chưa có kết quả. Nếu không đạt: ụ thấm đắp nổi trên sân, giữ ống tràn ra mương có van một chiều.',
    ], 62, 1.8)


