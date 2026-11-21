from sheets_sec import *
from sheets_plan import *

TREES = [(24.5, 4, .9, 'Mù u'), (25, 12.5, .95, 'Mù u'), (33, 8, 1, 'Còng'), (17.5, 26.5, .9, 'Mù u'), (25, 25.5, .85, 'Còng'),
         (30, 69.5, 1.1, 'Còng'), (45, 67.5, 1, 'Mù u')]
TREES_L = [(3.4, 8.9, 'C1'), (4.3, 12.4, 'C2'), (5.2, 16.0, 'C3')]  # cay tan cao ben trai nha phu, cach ranh trai 1,2m
PALMS = [(20.4, 6.8, 'Cau'), (20.2, 12.4, 'Cau'), (20.5, 16.8, 'Cau'), (5.8, 21.6, 'Chà là'), (14.8, 24.6, 'Chà là'), (21.3, 20.8, 'Chà là'), (7.4, 25.8, 'Chà là')]


# ------------------------------------------------------------------ KT-01 TONG MAT BANG
def sheet_site(sh):
    v = View(sh, 45, 17, 300, -2, -5)
    # duong
    v.rect(-3, -4.6, 57, -0.3, fill=(.82, .82, .82), edge=None, layer='NEN')
    v.line([(-3, -0.3), (57, -0.3)], .35, BLK); v.text(30, -3.6, 'ĐƯỜNG NHỰA (mặt lộ +0.700)', 2.4, anc='c', bold=True)
    v.poly(POND, fill=(.85, .92, .97), edge=(.3, .5, .7), lw=.25, layer='NEN'); v.text(40, 35, 'AO HIỆN TRẠNG', 2.4, anc='c', col=(.2, .4, .6), bold=True)
    v.text(40, 32.5, '(đợt sau san lấp, cần xin phép)', 1.8, anc='c', col=(.2, .4, .6))
    v.poly(LOT, edge=RED, lw=.6, dash=[6, 1.5, 1, 1.5], layer='TRUC')
    v.poly(LAND, edge=(.85, .55, .1), lw=.4, dash=[2, 1.2], layer='TRUC', close=False)
    v.text(33, 60, 'PHẦN ĐẤT CHƯA CẤP GCN (~1.200m², dò ảnh vệ tinh)', 1.8, anc='c', col=(.6, .4, .1))
    v.text(50, 73.0, 'SÔNG (phía Tây Nam)', 2.6, anc='c', bold=True, col=(.2, .4, .6))
    for i, (p, q, L) in enumerate([(LOT[0], LOT[1], '53,45m'), (LOT[1], LOT[2], '44,91m'), (LOT[2], LOT[3], '44,07m'), (LOT[3], LOT[0], '41,65m')]):
        m = ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2); ang = math.degrees(math.atan2(q[1] - p[1], q[0] - p[0]))
        if ang > 90: ang -= 180
        if ang < -90: ang += 180
        X, Y = v.P(*m); sh.text(X, Y + 1, L, 2.0, 'c', 'b', rot=ang, col=RED)
    for n, p in zip(['M2', 'M1', 'M4', 'M3'], LOT):
        X, Y = v.P(*p); sh.circle(X, Y, .8, fill=RED, edge=RED); sh.text(X + 1.5, Y + 1.5, n, 1.8, col=RED)
    v.text(30, 22, 'THỬA 320 – TỜ 51 – 2.064,2m² (GCN)', 2.4, anc='c', bold=True, col=RED)
    # cong
    for (a0, a1, t), dz in zip(GATES, (-1.4, -2.6)):
        v.line([(a0, -0.2), (a1, -0.2)], .6, (.35, .2, .1)); v.text((a0 + a1) / 2, dz, t, 1.5, anc='c')
    # nha
    v.rect(14, 2.5, 18, 18.5, fill=(.55, .55, .55), edge=BLK, lw=.4); v.text(16, 10.5, 'NHÀ CHÍNH', 1.7, anc='c', rot=90, col=(1, 1, 1), bold=True)
    v.rect(7.95, 7.75, 14, 18.5, fill=(1, 1, 1), edge=BLK, lw=.4); v.hatch(7.95, 7.75, 14, 18.5, sp=1.2)
    v.text(11, 13, 'NHÀ PHỤ', 1.7, anc='c', bold=True)
    a0, a1, b0, b1 = CARPORT; v.rect(a0, b0, a1, b1, edge=GRY, lw=.3, dash=[2, 1]); v.text((a0 + a1) / 2, 4.6, 'Nhà xe', 1.5, anc='c', col=GRY); v.text((a0 + a1) / 2, 3.6, '(đợt 2)', 1.4, anc='c', col=GRY)
    a0, a1, b0, b1 = TANK; v.rect(a0, b0, a1, b1, fill=(.7, .75, .8), edge=BLK, lw=.3)
    for (a, b) in [(8.05, 1.9), (9.95, 1.9), (8.05, 5.0), (9.95, 5.0), (9.95, 3.45)]: v.rect(a - .1, b - .1, a + .1, b + .1, fill=BLU, edge=BLU)
    v.rect(10.1, 2.3, 12.6, 7.2, edge=BLU, lw=.25, dash=[1.5, 1]); v.text(11.35, 4.6, 'Xe khách', 1.3, anc='c', rot=90, col=BLU)
    a0, a1, b0, b1 = SOAK; v.rect(a0, b0, a1, b1, fill=(.9, .87, .78), edge=GRY, lw=.25, dash=[1.5, 1]); v.text(1.65, 5.2, 'Bãi thấm', 1.3, anc='c', rot=90)
    v.circle(*WELL, .35, fill=BLU, edge=BLU); v.text(WELL[0] - .6, WELL[1] + .6, 'Giếng', 1.4, anc='r', col=BLU)
    v.circle(*WTANK, .55, fill=(1, 1, 1), edge=BLK); v.text(WTANK[0] + .9, WTANK[1], 'Bồn 1.000L', 1.4, col=BLK)
    v.line([(8.6, 21.4), (13.4, 21.4)], .3, GRY); v.text(11, 21.9, 'Dây phơi', 1.3, anc='c', col=GRY)
    v.line([(9.0, 4.85), (WELL[0], WELL[1])], .2, GRN, [1.5, 1]); v.text(11.6, 12.5, '≥15,3m', 1.6, col=GRN, rot=79)
    for a, b, s, n in TREES:
        v.circle(a, b, 3.0 * s, edge=GRN, lw=.25); v.circle(a, b, .25, fill=GRN, edge=GRN); v.text(a, b - .8, n, 1.4, anc='c', col=GRN)
    for a, b, n in TREES_L:
        v.circle(a, b, 3.0, edge=GRN, lw=.25, dash=[1.5, 1]); v.circle(a, b, .25, fill=GRN, edge=GRN)
    v.text(2.0, 18.6, 'C1–C3 tán cao', 1.3, col=GRN)
    for a, b, n in PALMS:
        v.circle(a, b, 1.0, edge=GRN, lw=.2, dash=[1, .6]); v.text(a + 1.2, b, n, 1.2, col=GRN)
    # duong vao
    v.line([(5.45, -0.2), (5.45, 3)], .2, BLK, [3, 1]); v.line([(10.25, -0.2), (10.25, 2)], .2, BLK, [3, 1])
    X, Y = v.P(10.6, 1.0); tag(sh, X + 2, Y, '12')
    north(sh, 225, 268, NORTH_PLAN)
    view_title(sh, 45, 282.5, 'TỔNG MẶT BẰNG', '1:300')
    y = notes(sh, 255, 280, 'GHI CHÚ', [
        'Ranh GCN thửa 320 tờ 51 (đỏ, theo GCN): 53,45 – 44,91 – 44,07 – 41,65m. Phần sau sát sông (~1.200m²) sử dụng ổn định, chưa cấp GCN – không xây công trình kiên cố tại đây.',
        'Toạ độ công trình: gốc tại mốc 2, trục a dọc lộ, b vào trong. Nhà chính cách ranh trái 14,0m, cách mép lộ 2,5m (hiên).',
        'Bể tự hoại 2.000L dưới sân trước bếp, cách giếng ≥15,3m. [12] Cổng chính chỉ cho người đi bộ (lối 1,2m có bậc); mọi xe, kể cả xe khách, vào cổng phụ 4,5m → không xe nào chạy gần bể, bỏ ụ chắn bánh.',
        'Bãi thấm dọc rào trái ~10m²: CHỐT SAU KHI THỬ THẤM + đo mực nước ngầm mùa mưa; chưa mua ống, vải địa trước đó.',
        'Cây: mù u, còng trên ụ đất cao +0,5 cách nhà ≥6,5–12m; cau dọc hông phải; chà là phía sau (chống nắng chiều Tây Nam, Tây Bắc).',
        'C1–C3: 3 cây tán cao bên trái nhà phụ (bàng Đài Loan hoặc mù u), trên ụ đất +0,3, cách rào 1,2m, cách bãi thấm ≥1,2m; tỉa nhánh dưới ≥2,5m. Che nắng sáng Đông Nam cho lối đi, vách bếp và khoảng sân trước hiên nhà phụ (xem KT-16).',
        'Nhà xe gỗ 5,7×7,1m làm đợt 2, vào bằng cổng phụ 4,5m.',
        'Cổng, rào: đợt 1 cổng sắt cũ lắp lại + rào kẽm gai tạm; đợt sau tường kín 2,6m.',
    ], 60, 1.85)
    sh.text(255, y - 3, 'Vị trí cây, ao, ranh phần chưa cấp lấy theo ảnh vệ tinh – sai số vài mét.', 1.7, col=GRY)


# ------------------------------------------------------------------ KT-05 MAT BANG MAI
def sheet_roof(sh):
    v = View(sh, 34, 14, 75, 5.0, 0.9)
    # nha chinh
    v.rect(14.0, 2.5, 18.0, 18.5, fill=(.93, .93, .93), edge=BLK, lw=.5, layer='MAI')
    v.rect(14.2, 2.7, 17.8, 18.3, edge=BLK, lw=.2, layer='MAI')
    v.text(16, 12, 'MÁI NHÀ CHÍNH (hiện trạng)', 1.9, anc='c', rot=90, bold=True)
    v.text(15.2, 12, 'tôn sau tường chắn mái +4.500 – kiểm tra dột, keo các mối', 1.5, anc='c', rot=90, col=GRY)
    v.rect(13.8, 2.0, 18.2, 2.5, fill=(.85, .55, .45), edge=BLK, lw=.3, layer='MAI'); v.text(16, 1.6, 'Mái hắt trang trí trước hiên', 1.5, anc='c')
    # nha phu
    v.rect(7.75, 7.6, 14.0, 18.7, fill=(1, 1, 1), edge=BLK, lw=.5, layer='MAI')
    for b in [7.7, 9.8, 11.9, 14.0, 16.1, 18.4]: v.line([(7.75, b + .03), (14.0, b + .03)], .15, (.55, .4, .25), [2, 1])
    for k in range(1, 26): v.line([(7.75 + k * .25, 7.6), (7.75 + k * .25, 18.7)], .07, LGR)
    v.rect(12.9, 18.5, 17.9, 19.7, fill=(1, 1, 1), edge=BLK, lw=.3, layer='MAI'); v.text(15.4, 19.1, 'Mái hắt tôn 1,2m (D10, D2, W3)', 1.5, anc='c')
    v.rect(9.4, 6.55, 13.95, 7.75, edge=BLU, lw=.3, dash=[2, 1], layer='DEXUAT'); v.text(11.7, 7.1, '[5] Mái hiên tôn 1,2m × 4,6m', 1.5, anc='c', col=BLU)
    for b in (10.0, 14.0):
        v.line([(13.0, b), (8.6, b)], .35, BLK); v.line([(8.9, b - .2), (8.6, b), (8.9, b + .2)], .35, BLK)
        v.text(11.0, b + .25, 'dốc ~10%', 1.6, anc='c')
    v.text(11.0, 12.0, 'MÁI TÔN CŨ NHÀ PHỤ', 2.0, anc='c', bold=True)
    v.text(11.0, 11.4, '+3.600 (đỉnh, giáp tường nhà chính) → +3.000 (mép trái)', 1.5, anc='c', col=GRY)
    v.text(11.0, 10.9, 'diềm che mưa + máng xối tôn mép trái → ống xuống Ø90', 1.5, anc='c', col=GRY)
    v.line([(7.65, 7.6), (7.65, 18.7)], .5, BLK); v.text(7.4, 13, 'Máng xối tôn mép trái', 1.5, anc='c', rot=90)
    v.circle(7.45, 17.7, .08, fill=BLK); v.text(7.3, 17.7, 'Thông hơi Ø60', 1.4, anc='r')
    v.rect(13.85, 7.6, 14.0, 18.7, fill=BLK, edge=BLK); v.text(13.7, 16.5, 'Úp nóc/diềm tôn chống thấm giáp tường', 1.4, anc='c', rot=90)
    v.circle(*WTANK, .55, fill=(1, 1, 1), edge=BLK); v.text(WTANK[0] + .7, WTANK[1], 'Bồn inox 1.000L trên bệ gạch 0,5m + bơm tăng áp', 1.5)
    v.dim_chain([7.75, 14.0, 18.0], 1.2, True, -1); v.dim_chain([7.6, 18.7, 19.9], 6.5, False, 1); v.dim_chain([2.0, 2.5, 18.5, 19.7], 19.2, False, -1)
    north(sh, 232, 268, NORTH_PLAN)
    view_title(sh, 34, 282.5, 'MẶT BẰNG MÁI', '1:75')
    notes(sh, 255, 280, 'GHI CHÚ MÁI', [
        'Mái nhà phụ: tận dụng tôn + xà gồ gỗ cũ, THAY TOÀN BỘ VÍT bằng vít có long đền cao su, tôn thủng thay tấm mới cùng sóng.',
        'Chống nóng: túi khí cách nhiệt dưới tôn (2 mặt bạc) + dải bông gió thông gió vách trước và trái; 1–2 quạt trần.',
        'Giáp tường nhà chính: diềm tôn chụp + keo Silicon/ Sika; kiểm tra sau mưa đầu tiên.',
        'Máng xối mép trái nhà phụ → ống xuống Ø90 → đợt 2 dẫn về bồn nước mưa / rãnh ra ao (không vào bể tự hoại).',
        'Mái nhà chính: chưa khảo sát kết cấu. Phương án sân thượng (PA A) hoặc lầu gỗ (PA B) chỉ làm khi có kỹ sư kiểm tra dầm, cột.',
        'Mái hắt 1,2m sau nhà: chỉ đoạn a 12,9–17,9 (che D10, D2, W3), khung sắt hộp 30×60 bắt vào tường bằng bulông nở, tôn cũ dốc ≥15% ra ngoài, đáy mái ≥ +2.600.',
    ], 60, 1.9)
    sh.text(255, 150, 'CAO ĐỘ CHÍNH', 2.6, bold=True)
    rows = [['Mặt lộ', '+0.700', 'chủ nhà đo'], ['Nền nhà chính, nhà phụ', '±0.000', 'chuẩn'], ['Sân trước', '−0.050', 'chủ nhà đo'], ['Sàn WC, chiếu nghỉ', '+0.500', ''],
            ['Triều cao nhất (ước)', '−0.300', 'hỏi dân địa phương'], ['Trần nhà chính', '+3.300', ''], ['Đỉnh tường nhà chính', '+4.500', ''],
            ['Mái nhà phụ (thấp/cao)', '+3.000/+3.600', ''], ['Đợt 2: nền nâng', '+0.450', 'cả 2 nhà'], ['Đợt 2: sân nâng', '+0.400', 'thấp hơn nền 5cm']]
    table(sh, 255, 146, [('Vị trí', 62), ('Cao độ', 30), ('Ghi chú', 55)], rows, 1.8, 4.2)


# ------------------------------------------------------------------ MAT DUNG
def carport_front(S):
    v = S.v
    for a in (2.42, 7.8): v.rect(a, .4, a + .12, 2.3, edge=GRY, lw=.25, dash=[1.5, 1])
    v.rect(2.2, 2.6, 8.05, 2.86, edge=GRY, lw=.25, dash=[1.5, 1]); v.text(5.1, 1.4, 'Nhà xe gỗ – đợt 2', 1.6, anc='c', col=GRY)


def louver(v, a0, a1, z0, z1):
    v.rect(a0, z0, a1, z1, fill=(1, 1, 1), edge=BLK, lw=.3, layer='CUA')
    for k in range(1, int((z1 - z0) / .06)): v.line([(a0, z0 + k * .06), (a1, z0 + k * .06)], .1, BLK, None, 'CUA')


def elev(sh, plane, c, look, oy, x0, title, ox=40, extra=None, lv_x=None, dimx=None):
    S = Sec(sh, plane, c, look, False, ox, oy, 75, x0)
    building(S, furn=False)
    S.draw(); v = S.v
    lo, hi = (x0, x0 + 22.5) if not v.flip else (x0 - 22.5, x0)
    if plane == 'b': lo, hi = (x0, x0 + 18.5) if not v.flip else (x0 - 18.5, x0)
    ground(S, lo, hi, road=False)
    if extra: extra(S)
    lvx = lv_x if lv_x is not None else (lo + .1 if not v.flip else hi - .1)
    levels(S, lvx, [(0, '±0.000'), (2.4, '+2.400'), (3.0, '+3.000'), (3.6, '+3.600'), (4.62, '+4.620')], 'r')
    if dimx is not None: v.dim_chain([-0.1, 0, 2.4, 3.0, 4.5, 4.62], dimx, False, -1)
    view_title(sh, ox, oy + 6.1 * 13.33, title, '1:75')
    return S


def sheet_elev_fb(sh):
    def fr(S):
        carport_front(S); v = S.v
        callout(v, 9.0, 2.65, ['Dải bông gió xi măng tận dụng', '+2.400→+2.900, lưới inox mặt trong'], 6.5, 4.6)
        callout(v, 10.2, 1.8, ['D7 cửa 2 cánh sơn xanh cổ vịt, nửa trên kính', 'trơn, ô kính phía trên tới lanh tô +2.650 [10]'], 6.5, 3.85)
        callout(v, 9.8, 2.7, 'Mái hiên tôn 1,2m × 4,6m [5]', 6.5, 3.15)
        callout(v, 16.0, 1.5, 'Cửa xếp/cuốn D1 hiện trạng', 18.8, 3.2)
        callout(v, 12.9, 1.5, 'Cửa sổ rộng W1 2.050×1.350 kính trơn, khung gỗ', 13.0, 5.1)
        louver(v, 12.6, 13.8, 2.95, 3.35); callout(v, 13.2, 3.3, 'O7 chớp hồi đầu cao mái 1.200×400 [17]', 15.0, 5.6)
        v.poly([(9.4, 2.8), (13.95, 2.8), (13.95, 2.6), (9.4, 2.6)], fill=None, edge=BLU, lw=.35, layer='DEXUAT')
        v.text(5.6, -0.6, 'Tường trắng ngà · gỗ nâu · mái xám đậm · cổng song sắt nâu (bỏ qua cổng rào khi vẽ)', 1.6, col=GRY)
    elev(sh, 'b', -1.0, +1, 85, 1.5, 'MẶT ĐỨNG TRƯỚC (nhìn từ lộ – hướng Đông Bắc)', extra=fr, dimx=19.3)
    def bk(S):
        v = S.v
        callout(v, 13.5, 1.2, ['Cửa sau nhà phụ D10 ra dây phơi,', 'lanh tô +2.650 [10]'], 11.0, 4.3)
        callout(v, 14.8, 1.4, ['Cửa sau nhà chính D2 1.000×2.700', '(đục từ cửa sổ cũ)'], 12.0, 5.0)
        louver(v, 11.8, 13.0, 2.95, 3.35); callout(v, 12.4, 3.3, 'O7 chớp hồi 1.200×400 [17]', 10.0, 5.7)
        callout(v, 17.15, 1.6, 'W3 1.200×1.200 đón gió Tây Nam [17]', 16.4, 5.45)
        callout(v, 15.9, 3.1, 'Bồn inox 1.000L trên bệ gạch 0,5m + bơm tăng áp', 8.0, 5.5)
    elev(sh, 'b', 21.5, -1, 188, 19.5, 'MẶT ĐỨNG SAU (nhìn từ vườn sau – hướng Tây Nam)', extra=bk, dimx=5.6)


def sheet_elev_side(sh):
    def lf(S):
        v = S.v
        for b in (0.6, 7.38): v.rect(b, .4, b + .12, 2.5, edge=GRY, lw=.25, dash=[1.5, 1])
        v.rect(0.35, 2.75, 7.6, 3.1, edge=GRY, lw=.25, dash=[1.5, 1]); v.text(4.0, 1.4, 'Nhà xe gỗ – đợt 2 (nét đứt)', 1.6, anc='c', col=GRY)
        v.text(13.5, 1.05, 'Lồng gas [6]', 1.5, anc='c', col=BLU)
        v.line([(6.7, 0.27), (17.4, 0.27)], .5, (.45, .3, .2)); v.text(14.0, 0.45, 'Ống thoát Ø90 đi nổi, dốc 1,5% về bể', 1.5, col=(.45, .3, .2))
        v.line([(6.7, 0.7), (18.6, 0.7)], .35, BLU); v.text(14.0, 0.85, 'Ống cấp Ø27 cao 0,7m', 1.5, col=BLU)
        v.line([(17.7, 0), (17.7, 3.6)], .4, GRY); v.text(17.85, 3.65, 'Thông hơi Ø60', 1.5)
        callout(v, 11.0, 1.5, ['Cửa sổ W2 trên mặt bếp 2.000×1.200', 'nhôm thường, 2 cánh lùa, không bệ'], 6.0, 5.0)
        callout(v, 12.0, 2.7, 'Dải bông gió + lưới inox', 9.0, 4.2)
    elev(sh, 'a', 0.5, +1, 85, 23.0, 'MẶT ĐỨNG HÔNG TRÁI (phía lối đi ra sau – hướng Đông Nam)', extra=lf, dimx=-0.8)
    def rt(S):
        v = S.v
        callout(v, 7.3, 1.7, ['3 cửa sổ S1 hiện trạng 1.200×1.400,', 'thêm lưới chống muỗi, 1 ô thoát hiểm'], 8.0, 5.4)
        callout(v, 10.0, .7, ['Dàn nóng trên chân đế 400', '+ mái che nhỏ [8]'], 12.6, 5.4)
        callout(v, 16.0, 3.0, 'Bồn nước 1.000L sau nhà', 19.5, 5.0)
        v.text(8.0, -0.6, 'Tường hông phải hướng Tây Bắc – nắng chiều tháng 5–8: hàng cau + cây tán che (xem TMB)', 1.6, col=GRY)
    elev(sh, 'a', 21.5, -1, 188, -1.0, 'MẶT ĐỨNG HÔNG PHẢI (phía ao – hướng Tây Bắc)', extra=rt, dimx=21.0)


# ------------------------------------------------------------------ KT-11 CHI TIET WC
def sheet_wc(sh):
    import copy
    v = View(sh, 32, 134, 25, 7.2, 15.05)
    names = ('Tường WC phía bếp', 'Tường WC phía khu giặt', 'Tường WC hông trái', 'Tường sau WC', 'Tường sau khu giặt', 'Vách ngăn tôn bếp–khu giặt')
    sub = copy.deepcopy([w for w in WALLS if w['name'] in names])
    hw = copy.deepcopy([w for w in WALLS if w['name'] == 'Tường hông trái nhà chính'][0]); hw['s0'] = 15.0; hw['s1'] = 18.3; hw['ops'] = [o for o in hw['ops'] if o[5] == 'D4']
    lw = copy.deepcopy([w for w in WALLS if w['name'] == 'Tường hông trái nhà phụ'][0]); lw['s0'] = 15.0; lw['ops'] = []
    for w in sub:
        w['ops'] = [(o[0], o[1], o[2], o[3], 'open', o[5], o[6]) if o[5] == 'D10' else o for o in w['ops']]
    plan_walls(v, sub + [hw, lw], tags=True, cols=[COLS[-1]])
    v.text(13.5, 18.62, 'D10 mở ra ngoài', 1.5, anc='c', col=(.1, .3, .55))
    furn_plan(v, [f for f in FURN if f[7] in ('bc', 'kt', 'gs', 'lv', 'kk')])
    steps_plan(v); future_wc2(v)
    v.rect(8.12, 16.3, 8.22, 16.6, fill=(.95, .8, .85), edge=RED, lw=.25); v.text(8.3, 16.65, 'Máy nước nóng 4,5kW (đáy +1.900)', 1.5, va='m', col=RED)
    v.line([(9.3, 15.45), (9.3, 16.55)], .5, (.3, .6, .8)); v.text(9.4, 15.6, 'Thanh treo + rèm tắm', 1.5, col=(.2, .4, .6))
    v.rect(8.67, 15.92, 8.83, 16.08, fill=BLK, edge=BLK); v.text(8.9, 15.85, 'Phễu thu', 1.5)
    v.line([(9.2, 16.3), (8.85, 16.05)], .25, BLK); v.text(9.05, 16.4, 'i=2%', 1.4)
    v.line([(9.6, 17.2), (9.0, 16.4)], .25, BLK); v.text(9.6, 17.3, 'i=1% về phễu', 1.4, anc='c')
    v.rect(8.17, 17.35, 8.21, 17.95, fill=BLU, edge=BLU); v.text(8.3, 17.98, 'Tay vịn', 1.3, col=BLU)
    v.line([(11.5, 18.05), (11.5, 18.62)], .9, (.55, .55, .55)); v.text(10.9, 18.62, 'Ø100 sấy', 1.3, anc='r', col=(.35, .35, .35))
    v.line([(12.27, 18.3), (10.05, 18.3)], .5, (.45, .3, .2), [2, 1]); v.text(11.0, 18.15, 'Ø60 đi nổi chân vách', 1.2, anc='c', col=(.45, .3, .2))
    v.circle(7.45, 17.7, .03, fill=BLK); v.text(7.4, 17.85, 'Thông hơi Ø60', 1.4, anc='r')
    v.rect(7.22, 17.32, 7.38, 17.48, fill=BLK, edge=BLK); v.text(7.4, 17.25, 'Nắp KT', 1.4)
    v.dim_chain([8.15, 8.6, 9.25, 9.3, 9.95, 10.05, 10.95, 14.0], 15.15, True, -1)
    v.dim_chain([8.05, 10.05, 11.2, 11.82, 12.0, 12.55, 13.1, 13.9, 14.0], 18.72, True, 1)
    v.dim_chain([15.4, 15.55, 16.55, 16.8, 17.5, 17.55, 18.25], 7.75, False, 1)
    v.dim_chain([15.35, 16.1, 16.4, 16.7, 17.6, 18.4], 14.4, False, -1)
    v.plan_level(9.5, 17.6, '+0.500', 1.6); v.plan_level(10.5, 17.35, '+0.500', 1.4); v.plan_level(12.3, 17.2, '±0.000', 1.6)
    v.text(9.05, 16.95, 'WC + TẮM', 2.0, anc='c', bold=True); v.text(12.6, 17.75, 'KHU GIẶT', 1.8, anc='c', bold=True)
    X, Y = v.P(11.5, 18.0); tag(sh, X, Y, '1'); X, Y = v.P(8.65, 18.65); tag(sh, X, Y, '9'); X, Y = v.P(13.1, 16.95); tag(sh, X, Y, '16')
    view_title(sh, 140, 122, 'MẶT BẰNG CHI TIẾT WC – KHU GIẶT', '1:25')
    # mat cat qua chieu nghi + bac
    S = Sec(sh, 'b', 17.1, +1, True, 32, 36, 25, 9.6, z0=0)
    ws = copy.deepcopy([w for w in WALLS if w['name'] == 'Tường WC phía khu giặt'])
    for w in ws:
        w['z1'] = 1.6
    S.walls(ws)
    S.draw(); vv = S.v
    vv.rect(9.6, -0.1, 12.4, 0, fill=CONC, edge=BLK, lw=.3)
    for (a0, a1, z) in [(10.05, 10.95, .5), (10.95, 11.25, .34), (11.25, 11.55, .17)]:
        vv.rect(a0, 0, a1, z, fill=(1, 1, 1), edge=BLK, lw=.45); vv.hatch(a0, 0, a1, z, sp=1.2, col=GRY)
        vv.rect(a0, z - .02, a1, z, fill=BLK, edge=BLK, lw=.1)
    vv.line([(10.1, 1.4), (10.95, 1.4), (11.55, 1.07), (11.65, 1.07)], .6, BLU)
    vv.dim_chain([0, .17, .34, .5], 12.1, False, 1); vv.dim_chain([10.05, 10.95, 11.25, 11.55], -0.35, True, -1)
    vv.text(10.9, 1.55, 'Tay vịn inox Ø32 cao 900', 1.5, anc='c', col=BLU)
    view_title(sh, 32, 112, 'MẶT CẮT CHI TIẾT BẬC LÊN WC (khai triển)', '1:25')
    notes(sh, 175, 100, 'QUY CÁCH BẬC', [
        'Chiếu nghỉ 900×900 cao +0.500 trước cửa lùa D9 (cửa lùa không cần chỗ quét); 2 bậc cao 170, rộng 300, đi xuống về phía bếp, song song vách WC: mặt trước máy giặt để trống ≥1,4m; mũi bậc nẹp nhôm chống trượt.',
        'Bậc xây rời, không liên kết sàn WC – đợt 2 nâng nền +0.450 thì phá bỏ.',
        'Đèn chân tường cảm biến cạnh bậc, cao 300.',
    ], 38, 1.7)
    rows = [['Bồn cầu 2 khối (INAX C-117VA)', 'tâm cách tường 450, xả sàn', 'Van + vòi xịt 400'], ['Máy nước nóng 4,5kW', 'đáy +1.900 (1,4m so sàn WC)', 'RCBO 25A 30mA riêng'],
            ['Sen tắm (của máy)', 'cài sen cao 1.000–1.900', ''], ['Quạt hút WC ≥100m³/h', 'trên ô chớp O4 vách trái', 'thổi ra ngoài'],
            ['Lavabo khu giặt', 'mặt +850, vách sau', 'van góc 550'], ['Máy giặt + sấy chồng', 'vách sau, ổ cắm cạnh máy +1.200', 'van +1.000, ống đứng Ø60 + khay hứng'],
            ['Tay vịn bồn cầu', 'cao 750 so sàn WC', 'inox Ø32'], ['Móc khăn, kệ khăn', 'cao +1.600', 'trên vách ngăn']]
    table(sh, 252, 122, [('Thiết bị', 46), ('Cao độ lắp / vị trí', 62), ('Ghi chú', 48)], rows, 1.6, 3.9)
    notes(sh, 330, 280, 'HOÀN THIỆN WC', [
        'Sàn: gạch granite mờ chống trơn R11, 300×300; dốc 1–2% về phễu.',
        'Chống thấm: 2 lớp gốc xi măng – polymer, lật tường 300 (khu tắm 1.800), thử ngâm nước 48h trước khi lát.',
        'Tường: ốp gạch men 300×600 cao 1.800 khu tắm, còn lại sơn chống ẩm.',
        'Trần: tấm nhựa PVC trên khung nhôm +2.900 (cách sàn WC 2,4m).',
        'Đợt 1 chỉ xây WC (tắm + bồn cầu). Cửa lùa D9 700, ray treo mặt ngoài, lùa về phía bếp, khoá mở được từ ngoài.',
        'Đợt 2: xây WC 2 (bồn cầu) ở chỗ chừa sẵn sát tường nhà chính, cùng lúc nâng nền +0.450 (không chung vách với WC 1, giữa là lối giặt sấy).',
        'Máy sấy thông hơi: ống Ø100 nhôm xuyên vách sau khu giặt, không dẫn vào WC, trần hay khoang mái.',
    ], 42, 1.75)


# ------------------------------------------------------------------ KT-12 CHI TIET BEP
def sheet_kitchen(sh):
    S = Sec(sh, 'a', 9.6, -1, True, 40, 200, 40, 7.4, z0=0)
    sub = [w for w in WALLS if w['name'] in ('Tường hông trái nhà phụ', 'Tường trước nhà phụ', 'Tường WC phía bếp')]
    S.walls(sub)
    for a0, a1, b0, b1, z0, z1, name, k in FURN:
        if k in ('tu', 'tl', 'mb', 'hm', 'ke', 'tk'): S.box(a0, a1, b0, b1, z0, z1, label=name, lw=.3)
    S.draw(); v = S.v
    v.rect(7.4, -0.1, 15.5, 0, fill=CONC, edge=BLK, lw=.3)
    v.rect(10.85, .8, 11.65, .85, fill=(.7, .7, .7), edge=BLK, lw=.2); v.text(11.25, .7, 'Chậu đôi', 1.5, anc='c', va='t')
    v.rect(12.55, .85, 13.28, .87, fill=BLK, edge=BLK); v.text(12.9, .95, 'Bếp từ đôi', 1.5, anc='c')
    v.rect(13.38, .85, 13.74, .93, fill=(.3, .3, .3), edge=BLK); v.text(13.56, 1.0, 'Gas', 1.4, anc='c')
    for b in (12.0, 12.3, 10.2): v.rect(b - .04, 1.08, b + .04, 1.14, fill=(1, 1, 1), edge=RED, lw=.3)
    v.text(12.15, 1.2, 'Ổ cắm đôi +1.100', 1.4, anc='c', col=RED)
    v.rect(13.5, .25, 13.6, .35, fill=(1, 1, .4), edge=BLK); v.text(13.7, .3, 'Báo rò gas sát sàn', 1.4)
    v.dim_chain([0, .85, 1.55, 2.2], 15.2, False, -1); v.dim_chain([0, 1.05, 2.0, 2.95], 7.55, False, 1)
    v.dim_chain([7.85, 8.3, 9.6, 10.3, 10.4, 10.85, 11.65, 12.55, 13.28, 13.8], -0.3, True, -1)
    view_title(sh, 40, 281, 'MẶT ĐỨNG TRIỂN KHAI BẾP (vách trái nhà phụ, nhìn từ bàn ăn)', '1:40')
    # mat bang bep 1:50
    p = View(sh, 38, 16, 50, 7.0, 7.6)
    sub2 = [w for w in WALLS if w['name'] in ('Tường hông trái nhà phụ', 'Tường trước nhà phụ', 'Tường WC phía bếp', 'Vách ngăn tôn bếp–khu giặt')]
    import copy
    hw = copy.deepcopy([w for w in WALLS if w['name'] == 'Tường hông trái nhà chính'][0]); hw['s1'] = 15.4; hw['ops'] = [o for o in hw['ops'] if o[5] == 'D3']; hw['s0'] = 7.75
    plan_walls(p, sub2 + [hw], tags=True, cols=COLS[2:4])
    furn_plan(p, [f for f in FURN if f[7] in ('tu', 'tl', 'mb', 'ban', 'tk', 'tg')])
    p.rect(6.75, 13.25, 7.25, 13.75, edge=BLU, lw=.3); p.text(7.0, 14.0, 'Gas', 1.5, anc='c', col=BLU)
    p.line([(8.75, 12.0), (8.75, 10.5), (10.4, 10.5), (10.4, 12.0)], .15, GRN, [1, .7]); p.text(9.5, 12.25, 'Lối đi ≥1.750', 1.5, anc='c', col=GRN)
    p.dim_chain([7.85, 9.6, 10.4, 13.8, 14.7, 15.3], 7.3, False, 1)
    p.dim_chain([8.05, 8.7, 10.42, 12.18, 14.0], 15.6, True, 1)
    view_title(sh, 38, 181, 'MẶT BẰNG BẾP – ĂN', '1:50')
    notes(sh, 190, 172, 'QUY CÁCH BẾP', [
        'Mặt bếp: đá granite/ đá nhân tạo dày 18–20 trên khung tủ (gỗ cũ tận dụng hoặc tủ nhựa Picomat chống ẩm), cao 850, sâu 600, len tường ốp gạch cao 600.',
        'Thứ tự: tủ lạnh → mặt để đồ 450 → chậu đôi 800 → sơ chế 900 → bếp từ đôi 730 → bếp gas đơn 520 (tổng 3.400).',
        'Bếp từ đôi: mạch R1 riêng RCBO 25A, dây 4mm² (đợt 2), ổ/hộp đấu dưới mặt bếp cao 600.',
        'Máy hút mùi mua ở đợt 2 cùng bếp từ. Đợt 1 khoan sẵn lỗ Ø150 xuyên tường trái (đáy máy sau này +1.550), bịt nắp.',
        'Bỏ kệ treo trên chậu: thay bằng cửa sổ rộng W2 (đồ khô cất tủ, kệ có sẵn [3]). Không đặt kệ trên bếp.',
        'Bình gas 12kg trong lồng thép thoáng NGOÀI tường [6], dây dẫn ≤1,5m, van điều áp ngắt tự động; báo rò gas đặt cao 300.',
        '[3] Dọc vách WC phía bếp: tủ gỗ thấp 3 cánh + 4 tủ nhựa có sẵn (cách mặt bếp ≥900); kệ sắt lớn có sẵn ở vách phải. Không đóng tủ mới.',
    ], 52, 1.75)
    notes(sh, 300, 172, 'CAO ĐỘ LẮP ĐẶT', [
        'Ổ cắm mặt bếp: +1.100, cách mép chậu ≥600.', 'Ổ tủ lạnh: +1.200 (cạnh tủ).', 'Công tắc đèn bếp: +1.250 cạnh cửa D7.',
        'Đèn LED gắn trên khung cửa sổ W2 chiếu mặt sơ chế (ban đêm).', 'Báo nhiệt trần bếp (không dùng báo khói gần bếp).', 'Bình chữa cháy 4kg cạnh cửa D7, cao 1.300.',
    ], 52, 1.75)


# ------------------------------------------------------------------ KT-13 THONG KE CUA + VAT LIEU
def sheet_schedule(sh):
    view_title(sh, 30, 280, 'BẢNG THỐNG KÊ CỬA ĐI – CỬA SỔ', '–')
    rows = [
        ['D1', 'Cửa chính nhà chính', '2.800×3.000', '1', 'Cửa xếp/cuốn hiện trạng', 'Giữ; thêm cửa lưới chống muỗi bên trong', 'Hiện trạng'],
        ['D2', 'Cửa sau hành lang', '1.000×2.700', '1', 'Cửa sắt cũ có sẵn lắp lại + lưới, mở ra ngoài', 'Đục từ cửa sổ cũ, lanh tô BTCT', 'Đợt 1 – mới'],
        ['D3', 'Khách → bếp', '900×2.200', '1', 'Gỗ hiện trạng, mở về bếp', 'Đợt 2 nâng nền: nâng lanh tô', 'Hiện trạng'],
        ['D4', 'Hành lang → khu giặt', '800×2.200', '1', 'Gỗ hiện trạng, mở về khu giặt', 'Đèn cảm biến 2 bên', 'Hiện trạng'],
        ['D5', 'Phòng ngủ 1', '800×2.200', '1', 'Gỗ đỏ ô kính mờ', 'Giữ, thay bản lề, khoá', 'Hiện trạng'],
        ['D6', 'Phòng ngủ 2/kho', '800×2.200', '1', 'Gỗ đỏ ô kính mờ', 'Giữ', 'Hiện trạng'],
        ['D7', 'Cửa nhà phụ (lối vào hằng ngày)', '2.000×2.650', '1', '2 cánh cao 2.200 khung sắt hộp mạ kẽm làm mới, sơn xanh cổ vịt, nửa trên kính trơn 5mm + ô kính trên (cửa sắt cũ duy nhất đã dùng cho D2)', 'Lanh tô +2.650 [10]', 'Đợt 1'],
        ['D8', 'Bếp → khu giặt', '800×2.100', '1', 'Cửa gỗ/nhựa, mở về phía bếp', 'Dời ra a 11,45–12,25 (ngoài dãy tủ) [2]', 'Đợt 1'],
        ['D9', 'Cửa WC 1 (tắm + bồn cầu)', '700×2.080', '1', 'Cửa lùa nhựa lõi thép, ray treo mặt ngoài, lùa về phía bếp', 'Khoá mở được từ ngoài; chiếu nghỉ 0,9×0,9 trước cửa', 'Đợt 1'],
        ['D11', 'Cửa WC 2 (bồn cầu)', '700×2.080', '1', 'Cửa lùa nhựa lõi thép', 'WC 2 chừa chỗ', 'Đợt 2'],
        ['D10', 'Cửa sau nhà phụ (ra dây phơi)', '800×2.650', '1', 'Sắt/nhôm cao 2.100 + ô lưới trên, mở ra', 'Lanh tô +2.650 [10]', 'Đợt 1'],
        ['V1', 'Vòm khách → hành lang', '1.100×2.500', '1', 'Ô trống', '', 'Hiện trạng'],
        ['S1', 'Cửa sổ hông phải', '1.200×1.400, đáy +1.000', '3', 'Sắt kính hiện trạng', 'Thêm lưới; nếu là cánh lùa thì đổi 2 cánh mở quay ra ngoài 90° làm cánh đón gió (KT-16)', 'Hiện trạng'],
        ['W3', 'Cửa sổ sau P.ngủ 2 (đón gió Tây Nam)', '1.200×1.200, đáy +1.000', '1', 'Khung nhôm/gỗ, kính trơn, 2 cánh mở quay + lưới', 'Đục mới, lanh tô BTCT; dưới mái hắt 1,2m', 'Đợt 1 – mới'],
        ['W1', 'Cửa sổ rộng trước nhà phụ', '2.050×1.350, đáy +0.900', '1', 'Nhôm hệ thường vân gỗ, kính dán an toàn 6,38 trơn (không cần cường lực 8mm), 2 cánh mở quay, không ô chia, không song; hộp ốp viền + bệ nhô 150 bằng gỗ thông sơn PU màu gỗ theo ảnh mẫu; lưới chống muỗi khung nẹp nam châm', 'Thay S2 (theo ảnh mẫu)', 'Đợt 1'],
        ['W2', 'Cửa sổ rộng hông bếp', '2.000×1.200, đáy +1.050', '1', 'Làm đơn giản cho đỡ vật liệu: nhôm hệ thường màu xám, kính trơn 5mm, 2 cánh lùa + lưới chống muỗi lùa; không hộp gỗ, không ốp viền, không bệ (bậu vữa láng dốc ra ngoài)', 'Thay S3; chỉ W1 mặt trước làm theo mẫu có bệ', 'Đợt 1'],
        ['O1', 'Ô thoáng vách khách–ngủ', '1.700×400, đáy +2.600', '1', 'Hiện trạng', '', 'Hiện trạng'],
        ['O3', 'Ô thoáng trên cửa D5, D6', '800×500, đáy +2.350', '2', 'Nan gỗ/nhôm chớp cố định + lưới', 'Gió phòng ngủ ra hành lang khi đóng cửa', 'Đợt 1 – mới'],
        ['O4', 'Cửa chớp lật WC 1 (vách trái)', '600×400, đáy +2.200', '1', 'Nhôm chớp lật + lưới + quạt hút', 'Trên khu tắm; ô chớp duy nhất của WC [9]', 'Đợt 1 – mới'],
        ['O5', 'Ô thoáng áp mái nhà chính (trước, sau)', '2.000×300, đáy +3.400', '2', 'Chớp nhôm + lưới', 'Chưa làm đợt 1: đục tường 200 cũ phải đổ lanh tô. Khảo sát mái rồi quyết; có thể thay bằng vài lỗ bông gió 200×200 không cần lanh tô', 'Đợt 2'],
        ['O6', 'Ô thoáng vách P.ngủ 1 – P.ngủ 2', '1.900×400, đáy +2.600', '1', 'Nan gỗ cố định', 'Nối luồng gió W3 → P.ngủ 1 → O1', 'Đợt 1 – mới'],
        ['O7', 'Chớp hồi mái nhà phụ (trước a12,6–13,8; sau a11,8–13,0)', '1.200×400, đáy +2.950', '2', 'Chớp tôn/nhôm + lưới', 'Ở đầu cao của mái: thoát khí nóng', 'Đợt 1 – mới'],
    ]
    cols = [('Ký hiệu', 16), ('Vị trí', 62), ('Kích thước R×C (mm)', 46), ('SL', 9), ('Vật liệu / loại', 82), ('Ghi chú', 82), ('Giai đoạn', 34)]
    y = table(sh, 30, 272, cols, rows, 1.8, 4.6)
    view_title(sh, 30, y - 8, 'BẢNG VẬT LIỆU HOÀN THIỆN', '–')
    rows2 = [
        ['Nhà chính (khách, ngủ, hành lang)', 'Giữ gạch men; đợt 2 nâng nền +0,45 lát mới', 'Xử lý chân tường ẩm: cạo, chống thấm ngược 1,2m, sơn chống kiềm + trắng ngà', 'Giữ trần thả', 'Lưới chống muỗi mọi cửa sổ'],
        ['Bếp + ăn (nhà phụ)', 'Láng vữa M75 xoa nhám (đợt 1 không lát gạch)', 'Gạch ống trát, sơn trắng ngà; len ốp gạch sau bếp cao 600', 'Túi khí cách nhiệt dưới tôn', '2 quạt trần'],
        ['WC', 'Gạch chống trơn R11 300×300 trên chống thấm 2 lớp', 'Ốp gạch 300×600 cao 1.800 khu tắm', 'Nhựa PVC +2.900', 'Xem KT-11'],
        ['Khu giặt – tắm', 'Láng vữa xoa nhám, không phễu sàn (khay hứng máy giặt)', 'Sơn chống ẩm; ốp gạch sau lavabo cao 1.200', 'Túi khí dưới tôn', 'Cảm biến rò nước (đợt 2)'],
        ['Ngoài nhà', 'Sân đá mi / xà bần lu chặt −0,05, dốc ra xa nhà về rãnh hở chân gờ, chảy ngang ra ao (KT-15)', 'Tường trắng ngà, gỗ nâu, mái xám đậm', '–', 'Ống đi nổi sơn chống nắng'],
    ]
    table(sh, 30, y - 14, [('Khu vực', 58), ('Sàn', 82), ('Tường', 100), ('Trần', 45), ('Ghi chú', 46)], rows2, 1.8, 4.6)


# ------------------------------------------------------------------ KT-14 RA SOAT
REVIEW = [
    ['1', 'Bậc lên WC', 'Chiếu nghỉ chỉ 0,5m trước cửa lùa, cao 0,5m: thai phụ đứng mở cửa dễ hụt chân.', 'Chiếu nghỉ 0,9×0,9m + 2 bậc 170/300 đi xuống về phía bếp + tay vịn; mặt trước máy giặt để trống (21/11: thu từ 0,9×1,6).', 'Cao', '+0,3–0,5tr'],
    ['2', 'Cửa D8 bếp → khu giặt', 'Cánh mở vào khu giặt quét sát góc bậc lên WC.', 'Đổi chiều mở về phía bếp, bản lề phía phải.', 'Cao', '0'],
    ['3', 'Kho chứa đồ', 'Kho chỉ có kệ sắt V ở P.ngủ 2 – sẽ thiếu chỗ khi phòng này thành phòng em bé.', 'Dùng tủ gỗ thấp 3 cánh, 4 tủ nhựa, kệ sắt lớn có sẵn dọc vách WC phía bếp; không đóng tủ kho mới (21/11).', 'Vừa', '0'],
    ['4', 'Lối vào hằng ngày', 'Ra vào thật sự qua cửa nhà phụ (sân xe) nhưng không có chỗ để giày, áo mưa, chìa khoá.', 'Kệ giày nhựa có sẵn + ghế đẩu dưới cửa sổ W1, móc treo; không đóng tủ (21/11).', 'Vừa', '~0,1tr'],
    ['5', 'Che mưa lối vào', 'Đi từ nhà xe/sân vào nhà phụ bị ướt; bệ rửa chân ngoài trời.', 'Mái hiên tôn 1,2m × 4,6m (chỉ che D7 + W1) trên khung sắt hộp, tận dụng tôn cũ.', 'Vừa', '+1,5–2tr'],
    ['6', 'Lồng bình gas', 'Lồng gas (a 7,3–7,8) đè đúng tuyến ống thoát Ø90 đi nổi chân tường (a 7,3).', 'Dời lồng ra a 6,75–7,25 trên bệ riêng; dây gas ≤1,5m xuyên ống lồng.', 'Cao', '0'],
    ['7', 'Phòng ngủ 1', 'Phòng rộng 2,3m: tủ áo sau giường làm lối bên kia chỉ còn ~0,25m; dàn lạnh thổi thẳng đầu giường.', 'Bỏ tủ áo sang P.ngủ 2; giường đầu quay vách phải; dàn lạnh lên vách trước.', 'Cao', '0'],
    ['8', 'Dàn nóng máy lạnh', 'Theo vị trí dàn lạnh mới.', 'Dàn nóng ra cạnh vách trước P.ngủ 1, ống đồng ~1m, chân đế 400 + mái che.', 'Vừa', '−0,2tr (ống ngắn)'],
    ['9', 'Thông gió WC', 'WC 5,2m² chỉ có ô thoáng 0,3×0,3 – ẩm, mốc, mùi.', '1 cửa chớp lật O4 0,6×0,4 + quạt hút (bỏ O2: 1 ô là đủ).', 'Vừa', '+0,4tr'],
    ['10', 'Chiều cao cửa sau khi nâng nền', 'Đợt 2 nâng nền +0,45: cửa cao 2,2m chỉ còn 1,75m, phải đục lại.', 'Cửa xây mới đợt 1 (D7, D10) đặt lanh tô +2,65; cửa nhà chính (D3–D6) ghi chú đục nâng ở đợt 2.', 'Cao', '+0,3tr'],
    ['11', 'Đường đêm P.ngủ → WC', 'Chưa có công tắc 2 chiều hành lang, chưa có công tắc đầu giường (thuyết minh ghi "chưa sửa").', 'Công tắc 2 chiều (D5 ↔ D4) + công tắc đầu giường + đèn chân tường cảm biến mỗi chặng.', 'Cao', '+0,5tr'],
    ['12', 'Xe khách & nắp bể', 'Cổng chính mở thẳng vào sân có bể tự hoại (nắp nhô 0,35m, cấm xe đè) – chỉ còn ~2,1m bên phải bể.', 'Cổng chính chỉ cho người đi bộ (lối 1,2m có bậc); mọi xe vào cổng phụ. Bỏ dốc xe cổng chính và ụ chắn bánh (21/11).', 'Vừa', '−2,5–3,5tr'],
    ['13', 'Phòng em bé', 'Vợ đang mang thai – chưa có phương án chỗ ngủ của bé.', 'P.ngủ 2 cạnh P.ngủ 1 chuẩn bị làm phòng em bé: dời kệ sắt, ổ cắm, rèm cản sáng.', 'Vừa', '+1tr'],
    ['14', 'Thống nhất tài liệu', 'Máy nước nóng 4.500W ghi lẫn RCBO 25A / MCB 32A; bồn nước mưa 2 vị trí (map: 6,6;8,9 – 3D: 6,9;20,5); README "cau ×4, chuối ×4" vs thuyết minh "cau ×3, chà là ×4"; sân "−0,10" vs khối xà bần +0,40 trong mô hình.', 'Chốt: RCBO 25A 30mA + dây 4mm²; bồn nước mưa sau nhà phụ (6,9;20,5); cau ×3 + chà là ×4; sân −0,05 (chủ nhà đo 19/11).', 'Thấp', '0'],
    ['15', 'Cửa sổ & thoát nước mặt', 'Cửa sổ nhỏ S2, S3 bí; lộ cao hơn nền 0,70m, nền chỉ cao hơn sân 5cm.', 'W1 dáng theo ảnh mẫu nhưng nhôm vân gỗ + kính 6,38 + hộp gỗ thông; W2 nhôm lùa đơn giản; gờ +0,80 chỉ đoạn a0–23 (làm móng tường rào đợt 2), rãnh hở chảy ngang ra ao, không bơm (KT-15).', 'Cao', '+8–11tr / +3–5tr'],
    ['16', '2 WC', 'Chỉ 1 WC chung cho tắm và đi vệ sinh: có người tắm là người khác phải chờ.', 'Đợt 1 làm tạm 1 WC (tắm + bồn cầu). Chừa chỗ WC 2 (bồn cầu) sát tường nhà chính cho đợt 2: 2 WC không chung vách, giữa là lối giặt sấy; ống chừa sẵn đầu chờ.', 'Vừa', '0 đợt 1 / ~6–9tr đợt 2'],
    ['17', 'Thông gió theo hướng', 'Phòng ngủ chỉ có cửa sổ hông phải, song song cả 2 mùa gió → đóng cửa phòng là bí; khoang mái tôn tích nhiệt.', 'W3 vách sau P.ngủ 2, O3 trên cửa D5/D6, O6 giữa 2 phòng, O7 hồi mái nhà phụ; S1 mở quay làm cánh đón gió (KT-16). O5 áp mái để đợt 2.', 'Cao', '+3–4,5tr'],
    ['18', 'Cây hông trái', 'Lối đi và vách bếp hướng Đông Nam nắng sáng gắt, khoảng sân trước hiên nhà phụ trống.', '3 cây tán cao C1–C3 cách rào 1,2m, tỉa nhánh dưới ≥2,5m: che nắng, gió vẫn lùa dưới tán.', 'Vừa', '+1–2tr'],
]


def sheet_review(sh):
    view_title(sh, 30, 280, 'RÀ SOÁT PHƯƠNG ÁN & TỐI ƯU CÔNG NĂNG SỬ DỤNG HẰNG NGÀY', '–')
    sh.text(30, 271, 'Rà soát theo tiêu chí: an toàn cho thai phụ và em bé – đường đi đêm – lối vào thật sự hằng ngày – chỗ chứa đồ – thông gió – không phải đập bỏ khi làm đợt 2.', 2.0)
    cols = [('#', 8), ('Hạng mục', 38), ('Vấn đề phát hiện', 132), ('Đề xuất (đã đưa vào bản vẽ)', 140), ('Ưu tiên', 16), ('Chi phí thêm', 46)]
    y = table(sh, 30, 266, cols, REVIEW, 1.9, 4.6)
    notes(sh, 30, y - 6, 'TỔNG HỢP', [
        'Các điểm 1, 2, 6, 7, 10, 11 nên làm ngay trong đợt 1 (chi phí thêm ~1,5–2tr, tránh sửa lại về sau). Điểm 3, 4, 5, 9, 12, 13 làm được trong đợt 1 hoặc dời đợt 2 tuỳ ngân sách (đợt 1 hiện ~145,6tr, vượt mốc 100–115tr).',
        'Giữ nguyên các quyết định đã chốt 15–17/11: vị trí WC, bếp 1 dãy, bể tự hoại sân trước bếp, điện 9 mạch, nhà xe đợt 2, mặt tiền kín đáo.',
        'Rà soát chi phí độc lập 21/11/2026 đã sửa vào bản vẽ: bỏ đóng tủ kho, tủ giày; nhà phụ không lát gạch; WC bồn cầu 2 khối, rèm tắm thay vách kính, bỏ O2; W1 vật liệu rẻ hơn giữ dáng; mái hắt sau chỉ 5m, mái hiên 4,6m; O5 dời đợt 2; cổng chính chỉ đi bộ; gờ chắn chỉ a0–23, rãnh hở thay B200; bồn nước bệ 0,5m + bơm tăng áp; cáp nguồn 2×16; bể tự hoại tấm lót chống nổi dày hơn.',
        'Chi phí thêm là ước tính sơ bộ, chưa có báo giá thợ địa phương.',
    ], 190, 1.85)


# ------------------------------------------------------------------ KT-00 BIA
def sheet_cover(sh, index_rows):
    sh.text(30, 268, PROJECT, 7, bold=True)
    sh.text(30, 258, 'HỒ SƠ BẢN VẼ THIẾT KẾ CẢI TẠO – ĐỢT 1 "DỌN VÀO Ở"', 4, bold=True, col=(.2, .2, .2))
    sh.text(30, 250, SITE + '   ·   Chủ nhà: ' + OWNER + '   ·   ' + DATE, 2.4, col=GRY)
    sh.image(30, 120, 210, 122, '/mnt/user-data/uploads/NHA_DUYEN_HAI_CAI_TAO/01_THIET_KE/3D_tong_quan.png')
    sh.text(30, 116, 'Phối cảnh tổng thể (trích mô hình 3D)', 1.9, col=GRY)
    view_title(sh, 255, 270, 'DANH MỤC BẢN VẼ', '')
    table(sh, 255, 264, [('Ký hiệu', 20), ('Tên bản vẽ', 105), ('Tỉ lệ', 28)], index_rows, 1.8, 4.3)
    notes(sh, 30, 106, 'GHI CHÚ CHUNG', [
        'Đơn vị kích thước: mm; cao độ: m. ±0.000 = mặt nền nhà chính hiện trạng (thấp hơn mặt lộ 0,70m, cao hơn sân 0,05m – chủ nhà đo 19/11/2026).',
        'Bản vẽ lập từ mô hình 3D, thuyết minh, sơ đồ điện–nước–mạng (bản 17/11/2026) và ảnh hiện trạng. Sơ đồ điện, nước, mạng chi tiết: xem phụ lục PDF kèm theo.',
        'Kích thước hiện trạng là ước tính từ mô hình – thợ/kỹ sư ĐO KIỂM TẠI CHỖ trước khi thi công, sai lệch báo lại để chỉnh bản vẽ.',
        'Hạng mục kết cấu (đục cửa D2, mái hắt, bể tự hoại, PA sân thượng/lầu) cần kỹ sư có chứng chỉ kiểm tra và ký.',
        'Ô lục giác số xanh [n]: điểm tối ưu sau rà soát 19/11/2026, sửa theo rà soát chi phí 21/11/2026 (xem KT-04, KT-14).',
    ], 110, 1.85)
    notes(sh, 255, 186, 'GIẢ ĐỊNH CẦN XÁC NHẬN', [
        'Tường nhà chính dày 200, vách trong 100; tường mới gạch ống 100.',
        'Trần thả +3,3m; đỉnh tường +4,5m; mái nhà chính là tôn sau tường chắn mái (chưa khảo sát).',
        'Mặt lộ +0,70; sân −0,05; triều cao nhất −0,30 (chủ nhà đo). Thoát nước mặt: KT-15.',
        'Móng nhà chính chưa khảo sát (vẽ nét đứt tượng trưng).',
        'Hướng: tính từ sơ đồ GCN, cạnh giáp lộ phương vị 319,67° → mặt tiền nhìn 49,7° (Đông Bắc), mặt sau 229,7° (Tây Nam). Kiểm lại bằng la bàn khi đo.',
    ], 72, 1.85)
