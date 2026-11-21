# KT-16 THONG GIO TU NHIEN – tinh theo huong thua dat (GCN) va mua gio
import math
from sheets_rest import *
from sheets_level import arrow

BRG_A = 319.67          # phuong +a (doc lo, moc 2 -> moc 1) theo so do GCN (map.html BRG0)
BRG_B = BRG_A - 90      # phuong +b (vao trong dat, ve phia song) = 229,67
FACES = [('Mặt tiền (lộ, nhà phụ D7/W1, nhà chính D1)', (BRG_B + 180) % 360), ('Mặt sau (sông: W3, D2, D10, O2)', BRG_B),
         ('Hông trái (W2, dải bông gió, O4)', (BRG_A + 180) % 360), ('Hông phải (S1 ×3)', BRG_A)]
WINDS = [('Đông Bắc (T12–T4)', 45.0), ('Tây Nam (T5–T11)', 225.0), ('Đông Nam – gió chướng*', 135.0)]


def inc(face, wind):  # goc giua phap tuyen mat ngoai va huong gio thoi toi (0 = truc dien)
    d = abs((face - wind + 180) % 360 - 180); return d


def role(d):
    if d <= 45: return 'đón gió'
    if d < 135: return 'song song (hút)'
    return 'khuất gió (hút)'


def wdir(brg):  # vec to don vi (a,b) cua phuong co goc phuong vi brg
    d = math.radians(BRG_A - brg); return (math.cos(d), math.sin(d))


def op(code, nth=0):
    hits = [(w, o) for w in WALLS for o in w['ops'] if o[5] == code]
    w, o = hits[nth]; h = o[3] - o[2]
    if o[4] == 'door2' and o[6]: h = o[6] - o[2]
    if o[4] == 'door' and len(o[6]) > 2: h = o[6][2] - o[2]
    return (o[1] - o[0]) * h


K = {'cua': 1.0, 'quay': 0.9, 'lua': 0.5, 'chop': 0.5, 'bong': 0.4}  # he so dien tich thoang (gia dinh)
BAND = {'front': sum(s1 - s0 for ax, s0, s1, t, z0, z1 in BANDS if ax == 'x') * 0.5, 'left': sum(s1 - s0 for ax, s0, s1, t, z0, z1 in BANDS if ax == 'y') * 0.55}


def A(items):
    return sum(K[k] * (op(c) if isinstance(c, str) else c) * n for c, k, n in items)


def series(a1, a2): return 1 / math.sqrt(1 / a1 ** 2 + 1 / a2 ** 2)


V_WIND = 1.0  # m/s gia dinh gio nhe tai cao do cua – ket qua ti le thuan voi v
VOL = {'kh': (3.6 * 4.3 + 1.2 * 8.2) * 3.3, 'ng': (2.3 * 4.0 + 2.3 * 4.1) * 3.3, 'bep': 5.95 * 7.45 * 3.23}
O7 = 1.2 * 0.4
SCEN = [  # (khu, kich ban, cua vao, cua ra, Cv, the tich)
    ('Khách + hành lang', 'Ngày · Đông Bắc', [('D1', 'cua', 1)], [('D2', 'cua', 1)], .5, 'kh'),
    ('Khách + hành lang', 'Ngày · Tây Nam', [('D2', 'cua', 1)], [('D1', 'cua', 1)], .5, 'kh'),
    ('P.ngủ 1 + 2 (cửa đóng)', 'Đêm · Đông Bắc', [('S1', 'quay', 2)], [('W3', 'quay', 1), ('O3', 'chop', 2)], .3, 'ng'),
    ('P.ngủ 1 + 2 (cửa đóng)', 'Đêm · Tây Nam', [('W3', 'quay', 1)], [('S1', 'quay', 2), ('O3', 'chop', 2)], .5, 'ng'),
    ('Bếp + ăn (nhà phụ)', 'Ngày · Đông Bắc', [('D7', 'cua', 1), ('W1', 'quay', 1), (BAND['front'], 'bong', 1)], [('W2', 'lua', 1), (BAND['left'], 'bong', 1), (O7, 'chop', 1), (series(op('D8'), op('D10')), 'cua', 1)], .5, 'bep'),
    ('Bếp + ăn (nhà phụ)', 'Ngày · Tây Nam', [(series(op('D8'), op('D10')), 'cua', 1), (O7, 'chop', 1)], [('D7', 'cua', 1), ('W1', 'quay', 1), (BAND['front'], 'bong', 1), ('W2', 'lua', 1), (BAND['left'], 'bong', 1)], .5, 'bep'),
    ('Bếp + ăn (nhà phụ)', 'Ngày · Đông Nam*', [('W2', 'lua', 1), (BAND['left'], 'bong', 1)], [('D7', 'cua', 1), ('W1', 'quay', 1), (BAND['front'], 'bong', 1), (O7, 'chop', 1)], .5, 'bep'),
]


def calc():
    out = []
    for zone, sc, ins, outs, cv, vk in SCEN:
        ai, ao = A(ins), A(outs); ae = series(ai, ao); q = cv * ae * V_WIND; ach = q * 3600 / VOL[vk]
        out.append((zone, sc, ai, ao, ae, cv, q, ach))
    return out


def _selfcheck():
    assert abs(FACES[0][1] - 49.67) < .01 and abs(FACES[1][1] - 229.67) < .01 and abs(FACES[2][1] - 139.67) < .01
    assert inc(FACES[0][1], 45) < 5 and inc(FACES[1][1], 225) < 5 and inc(FACES[2][1], 135) < 5 and inc(FACES[3][1], 45) > 85
    b = wdir(BRG_B); assert abs(b[0]) < 1e-9 and abs(b[1] - 1) < 1e-9
    assert abs(op('D1') - 8.4) < 1e-9 and abs(op('W3') - 1.44) < 1e-9 and abs(op('D7') - 4.4) < 1e-9
    assert abs(series(3, 4) - 2.4) < 1e-9


_selfcheck()
f2 = lambda x: f'{x:.2f}'.replace('.', ',')
f1 = lambda x: f'{x:.1f}'.replace('.', ',')


def sheet_vent(sh):
    v = View(sh, 22, 40, 100, 2.0, 2.0)
    plan_walls(v, tags=True)
    for a, b, n in TREES_L:
        v.circle(a, b, 3.0, edge=GRN, lw=.25, dash=[1.5, 1]); v.circle(a, b, .15, fill=GRN, edge=GRN); v.text(a, b - .7, n, 1.4, anc='c', col=GRN)
    v.line([(0.5, 2.0), (5.44, 22.0)], .2, RED, [4, 1, 1, 1]); v.text(1.3, 4.5, 'ranh trái', 1.4, col=RED, rot=76)
    v.line([(2.0, -0.3), (20.5, -0.3)], .35); v.text(11, -1.2, 'LỘ (mặt tiền nhìn 49,7° – Đông Bắc)', 1.8, anc='c', bold=True)
    # gio mua: mui ten lon theo dung goc phuong vi (gio thoi TOI huong nguoc)
    C_NE, C_SW, C_SE = (.1, .35, .75), (.75, .3, .1), (.35, .55, .25)
    for (brg, col, lab, c0) in [(45, C_NE, 'GIÓ ĐÔNG BẮC 45° (T12–T4)', (19.0, 4.2)), (225, C_SW, 'GIÓ TÂY NAM 225° (T5–T11)', (19.3, 20.5)), (135, C_SE, 'GIÓ ĐÔNG NAM* 135°', (6.6, 7.0))]:
        d = wdir((brg + 180) % 360)  # huong gio di toi
        p = (c0[0] - d[0] * 3.2, c0[1] - d[1] * 3.2); arrow(v, p, c0, col, .9); v.text(p[0] - .3, p[1] + .3, lab, 1.7, anc='r', bold=True, col=col) if brg == 225 else v.text(p[0], p[1] + (.4 if brg != 45 else -.9), lab, 1.7, anc='l' if brg == 135 else 'c', bold=True, col=col)
    # luong gio qua nha
    path = lambda pts, col: [arrow(v, pts[i], pts[i + 1], col, .35) for i in range(len(pts) - 1)]
    path([(16.0, 4.6), (16.0, 8.2), (14.9, 10.6), (14.9, 17.6), (14.8, 19.2)], C_NE)
    path([(17.3, 19.4), (17.3, 17.6), (16.6, 14.6), (16.6, 13.2), (16.9, 10.4), (16.5, 9.0), (18.6, 7.3)], C_SW)
    path([(11.0, 6.2), (11.0, 12.6), (12.85, 15.0), (13.5, 18.2), (13.5, 19.4)], C_NE)
    path([(10.0, 9.0), (8.4, 11.4), (7.2, 11.9)], C_NE)
    path([(5.6, 11.2), (8.6, 12.0), (12.4, 9.5), (12.9, 7.0)], C_SE)
    v.text(14.6, 13.6, 'O3', 1.4, col=BLU); v.text(16.9, 14.35, 'O6', 1.4, col=BLU); v.text(16.6, 10.25, 'O1', 1.4, col=BLU)
    north(sh, 36, 258, NORTH_PLAN)
    view_title(sh, 26, 282.5, 'SƠ ĐỒ HƯỚNG GIÓ – LUỒNG GIÓ XUYÊN PHÒNG', '1:100')
    sh.text(26, 276, 'Xanh: gió Đông Bắc · Cam: gió Tây Nam · Lục: gió Đông Nam (gió chướng). Mũi tên vẽ đúng góc phương vị so với trục nhà.', 1.7, col=GRY)
    # bang 1: huong mat nha
    X = 205
    view_title(sh, X, 282.5, '1. HƯỚNG CÁC MẶT NHÀ (tính từ sơ đồ GCN)', '–', 2.8)
    rows = []
    for n, f in FACES:
        r = [n, f1(f) + '°']
        for _, wb in WINDS:
            d = inc(f, wb); r.append(f'{d:.0f}° {role(d)}')
        rows.append(r)
    y = table(sh, X, 277, [('Mặt nhà', 62), ('Hướng nhìn ra', 21), ('Gió Đông Bắc 45°', 34), ('Gió Tây Nam 225°', 34), ('Gió Đông Nam 135°', 34)], rows, 1.55, 3.9)
    sh.text(X, y - 3, 'Cạnh giáp lộ (mốc 2 → mốc 1) phương vị 319,67° theo sơ đồ GCN; trục nhà song song cạnh này. Góc = lệch giữa hướng gió thổi tới và pháp tuyến mặt.', 1.45, col=GRY)
    sh.text(X, y - 6, 'Gió mùa thực tế dao động ±22,5° quanh hướng chính → mặt tiền và mặt sau vẫn lệch ≤27°, luôn ở vùng đón gió trực diện.', 1.45, col=GRY)
    # bang 2: luu luong
    y -= 13
    view_title(sh, X, y, '2. LƯU LƯỢNG GIÓ XUYÊN PHÒNG (gió nhẹ v = 1 m/s)', '–', 2.8)
    rows = []
    for zone, sc, ai, ao, ae, cv, q, ach in calc():
        rows.append([zone, sc, f2(ai), f2(ao), f2(ae), f2(cv).rstrip('0'), f2(q), f'{ach:.0f}'])
    y = table(sh, X, y - 5, [('Khu', 40), ('Kịch bản', 27), ('A vào m²', 17), ('A ra m²', 17), ('A hiệu dụng', 19), ('Cv', 10), ('Q m³/s', 16), ('Lần/giờ', 16)], rows, 1.5, 3.8)
    y = notes(sh, X, y - 3, 'CÁCH TÍNH', [
        'Q = Cv · A · v (ASHRAE Fundamentals, thông gió do gió). Cv = 0,5 khi gió vuông góc cửa vào, 0,3 khi gió chạy song song mặt có cửa (S1 hông phải).',
        'A hiệu dụng cửa vào – cửa ra nối tiếp: 1/A² = 1/A vào² + 1/A ra². Diện tích lấy tự động từ mô hình bản vẽ (KT-03, KT-13) nhân hệ số thoáng: cửa đi mở 1,0 · cửa sổ mở quay 0,9 · cửa lùa 0,5 · chớp/ô thoáng có lưới 0,5 · bông gió có lưới 0,4.',
        'v = 1 m/s là giả định gió nhẹ ở độ cao cửa (chưa có số liệu trạm gần nhất). Gió 2 m/s thì Q và số lần/giờ gấp đôi. Đêm: D1, D2, D7, D10 đóng; cửa phòng ngủ đóng, gió đi qua ô thoáng O3, O6, O1.',
    ], 95, 1.45, 1.35, 2.2)
    y = notes(sh, X, y - 2, 'KẾT LUẬN & GIẢI PHÁP ĐÃ ĐƯA VÀO BẢN VẼ', [
        'Trục nhà gần như trùng hai mùa gió (lệch 4,7°): gió xuyên phòng TRƯỚC ↔ SAU là chủ đạo cả năm. Không chắn mặt tiền và mặt sau bằng tường kín, bồn nước hay cây tán thấp.',
        'Hông phải (S1) song song cả hai mùa gió: đổi S1 thành 2 cánh mở quay ra ngoài 90° – cánh bản lề phía lộ đón gió Tây Nam, cánh bản lề phía sông đón gió Đông Bắc.',
        'W3 (1.200×1.200) mới ở vách sau P.ngủ 2 lệch khỏi bóng bồn nước 1.000L (a 15,35–16,45) + O6 vách giữa 2 phòng ngủ + O3 trên cửa D5, D6: phòng ngủ đóng cửa ban đêm vẫn có gió qua (dòng 3–4 bảng 2).',
        'O5 áp mái trước/sau nhà chính: gió thổi xuyên khoang mái theo đúng trục Đông Bắc – Tây Nam, xả nhiệt dưới tôn trước khi xuống trần.',
        'O7 ở đầu cao mái nhà phụ (trước + sau): khí nóng bếp dồn lên đầu cao rồi thoát ra, cả khi lặng gió. Mỗi WC 1 ô chớp + quạt hút ra ngoài trời.',
        'Máy sấy thông hơi xả ra vách sau khu giặt, chụp lật hướng xuống, cách ô chớp WC 2 ~2,9m.',
        'Cây bên trái nhà phụ: tán cao, tỉa nhánh dưới ≥2,5m để gió Đông Nam lùa dưới tán vào W2 và dải bông gió, tán che nắng sáng.',
    ], 95, 1.45, 1.35, 2.2)
    sh.text(X, y - 2, '* Gió mùa Đông Bắc T12–đầu T4 và Tây Nam T5–T11: Tạp chí KTTV số 717 (09/2020), "Nghiên cứu đặc điểm khí hậu tỉnh Trà Vinh".', 1.4, col=GRY)
    sh.text(X, y - 4.6, '  Gió chướng Đông – Đông Nam mùa khô là kinh nghiệm ven biển miền Tây, chưa có số liệu trạm: kiểm chứng tại chỗ (cờ gió / cảm nhận) trước khi chốt.', 1.4, col=GRY)
