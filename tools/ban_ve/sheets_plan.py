from plan import *

PROPOSALS = [
    ('1', 12.85, 17.05, 'Bậc lên WC: chiếu nghỉ chung 1,0×2,0m trước 2 cửa WC + 2 bậc cao 170, rộng 300 + tay vịn inox + lan can mép chiếu nghỉ. Thai phụ đứng mở cửa an toàn.'),
    ('16', 9.75, 16.45, '2 WC thay 1 WC 9m²: WC 1 (tắm + bồn cầu, cửa lùa D9) và WC 2 (bồn cầu, cửa D11 mở vào trong). Một người tắm, người khác vẫn đi vệ sinh được.'),
    ('17', 16.6, 18.95, 'Thông gió theo hướng thửa (mặt tiền 49,7° Đông Bắc – sau 229,7° Tây Nam): thêm W3 sau P.ngủ 2, ô thoáng trên cửa D5, D6 (O3), vách 2 phòng ngủ (O6), áp mái (O5), hồi mái nhà phụ (O7). Xem KT-16.'),
    ('18', 6.9, 10.0, '3 cây tán cao bên trái nhà phụ, cách rào 1,2m: che nắng sáng hướng Đông Nam, gió vẫn lùa dưới tán vào W2 và dải bông gió.'),
    ('2', 12.85, 14.55, 'Cửa D8 (bếp → khu giặt) đổi chiều mở về phía bếp, bản lề phía phải: không quét vào chiếu nghỉ/bậc.'),
    ('3', 9.7, 14.25, 'Tủ kho cao 2,2m dọc vách WC phía bếp (3,2m × sâu 0,6m): gạo, đồ khô, đồ gia dụng; thay kệ sắt V ở P.ngủ 2.'),
    ('4', 12.6, 8.55, 'Cửa nhà phụ là lối vào hằng ngày (sân xe): tủ giày thấp + ghế ngồi + móc chìa khoá/áo mưa, dưới cửa sổ rộng W1.'),
    ('5', 8.75, 7.15, 'Mái hiên tôn 1,2m trước cửa nhà phụ (dài 4,1m, cao +2,8 sát tường, trên lanh tô +2,65 → +2,6 mép ngoài): đi từ nhà xe vào không ướt, che bệ rửa chân.'),
    ('6', 6.45, 12.75, 'Lồng bình gas dời ra 0,55m (bệ riêng a 6,75–7,25): bản cũ đè lên ống thoát Ø90 đi nổi chân tường.'),
    ('7', 16.25, 11.45, 'P.ngủ 1: bỏ tủ áo (dời sang P.ngủ 2), giường đầu quay vách phải, 2 bên đều lên xuống được; dàn lạnh lên vách trước, không thổi thẳng đầu giường.'),
    ('8', 19.15, 10.9, 'Dàn nóng dời ra cạnh vách trước P.ngủ 1 (b 9,6–10,4): ống đồng ~1m, ít uốn, dễ vệ sinh.'),
    ('9', 8.65, 18.85, 'WC chỉ có ô thoáng 0,3×0,3: mỗi WC 1 cửa chớp lật 0,6×0,4 (O2, O4) + quạt hút, chống ẩm mốc.'),
    ('10', 13.5, 19.05, 'Lanh tô cửa đi nhà phụ (D7, D10) đặt +2,65, cánh cao 2,1–2,2 + ô lưới phía trên: sau này nâng nền +0,45 vẫn đủ cao 2,2m.'),
    ('11', 14.8, 12.3, 'Đường đêm P.ngủ → WC (~8m): đèn hành lang công tắc 2 chiều (cửa D5 ↔ cửa D4) + đèn chân tường cảm biến + công tắc đầu giường.'),
    ('13', 17.25, 16.95, 'P.ngủ 2 chuẩn bị làm phòng em bé (cạnh P.ngủ 1): dời kệ sắt ra tủ kho bếp, thêm ổ cắm 1,0m, rèm cản sáng.'),
]


def plan_base(sh, v, tags=True):
    plan_walls(v, tags=tags)
    # mai hien de xuat (net dut, tren cao)
    for (a0, b0, a1, b1, lab) in [(7.9, 6.55, 14.05, 7.75, 'Mái hiên tôn 1,2m (đề xuất)'), (14.0, 18.5, 18.0, 19.7, 'Mái hắt 1,2m'), (7.75, 18.7, 14.0, 19.9, 'Mái hắt 1,2m')]:
        v.rect(a0, b0, a1, b1, edge=BLU if 'đề xuất' in lab else GRY, lw=.2, dash=[2, 1], layer='MAI')
        v.text((a0 + a1) / 2, b0 + .15, lab, 1.5, anc='c', col=BLU if 'đề xuất' in lab else GRY)
    # hien, bac tam cap
    v.rect(14.0, 2.5, 18.0, 5.5, edge=BLK, lw=.2, layer='NEN')


def sheet_dim_plan(sh):
    v = View(sh, 34, 14, 75, 5.0, 0.9)
    plan_base(sh, v)
    grid(v, A_GRID, B_GRID, (5.4, 19.2), (1.5, 20.6))
    v.dim_chain([7.95, 9.5, 11.5, 12.3, 13.5, 14.0, 14.6, 17.4, 18.0], 1.95, True, -1)
    v.dim_chain([7.95, 14.0, 18.0], 1.15, True, -1)
    v.dim_chain([8.05, 8.35, 8.95, 11.35, 13.1, 13.9, 14.0, 14.3, 15.3, 16.55, 17.75, 18.0], 20.0, True, 1)
    v.dim_chain([7.75, 10.45, 11.45, 15.3, 18.35], 6.55, False, 1)
    v.dim_chain([7.75, 18.5], 5.85, False, 1)
    v.dim_chain([2.5, 5.5, 6.7, 7.9, 10.7, 11.9, 14.7, 15.9, 18.5], 18.75, False, -1)
    v.dim_chain([2.5, 5.5, 10.05, 14.15, 18.5], 19.5, False, -1)
    v.dim_chain([2.5, 18.5], 20.25, False, -1)
    # trong nha
    v.dim_chain([14.2, 15.4, 17.8], 9.3, True, 1); v.dim_chain([14.2, 17.8], 6.0, True, 1)
    v.dim_chain([10.1, 10.7, 11.5, 14.1, 14.8, 15.6, 18.3], 15.72, False, -1)
    v.dim_chain([5.7, 10.0], 17.35, False, -1); v.dim_chain([10.1, 14.1, 18.3], 16.9, False, -1)
    v.dim_chain([8.05, 8.7, 10.9, 11.7, 14.0], 9.0, True, 1)
    v.dim_chain([7.85, 9.6, 10.4, 13.8, 14.7, 15.3], 9.95, False, -1)
    v.dim_chain([8.15, 11.35], 17.75, True, 1); v.dim_chain([15.4, 18.25], 10.6, False, -1)
    v.dim_chain([11.45, 12.45, 13.05, 14.0], 15.55, True, 1)
    v.dim_chain([15.35, 15.7, 16.6, 18.4], 13.6, False, -1)
    # cao do
    for (a, b, t) in [(16.0, 4.4, '±0.000'), (16.6, 7.0, '±0.000'), (12.8, 8.4, '±0.000'), (9.2, 16.6, '+0.500'), (11.95, 16.3, '+0.500'), (13.6, 17.3, '±0.000'), (11.0, 4.8, '−0.100'), (5.0, 4.4, '−0.100')]:
        v.plan_level(a, b, t, 1.7)
    for name, a, b, S in ROOMS:
        v.text(a, b, name, 2.0, anc='c', bold=True); v.text(a, b - .38, f'S = {S:.1f} m²'.replace('.', ','), 1.6, anc='c', col=GRY)
    section_mark(v, 'A', (14.8, 2.3), (14.8, 19.6), (-1, 0))
    section_mark(v, 'B', (9.0, 2.3), (9.0, 19.6), (-1, 0))
    section_mark(v, 'C', (6.0, 11.2), (19.3, 11.2), (0, 1))
    section_mark(v, 'D', (6.0, 16.2), (19.3, 16.2), (0, 1))
    north(sh, 232, 268, NORTH_PLAN)
    view_title(sh, 34, 282.5, 'MẶT BẰNG KÍCH THƯỚC – ĐỊNH VỊ TƯỜNG, CỬA', '1:75')
    y = notes(sh, 255, 280, 'GHI CHÚ', [
        '1. Kích thước ghi bằng mm, tính tới mặt tường thô (chưa trát). Cao độ ±0.000 = mặt nền nhà chính hiện trạng.',
        '2. Tường xám đặc: tường hiện trạng giữ lại (nhà chính dày 200, vách trong 100).',
        '3. Tường gạch chéo đỏ: xây mới đợt 1 – gạch ống 8×8×18 dày 100, vữa M75, trát 2 mặt, trên đà kiềng BTCT 200×200 (xem mặt cắt).',
        '4. Vách ngăn bếp – khu giặt: tôn cũ trên khung gỗ (giữ), có thể thay tấm xi măng sau.',
        '5. Cột gỗ cũ 150×150 nhà phụ giữ lại đỡ mái; tường mới không đỡ mái.',
        '6. Sàn WC +0.500 (cát đầm + BT lót + chống thấm 2 lớp, lật chân tường 300; khu tắm lật 1.800).',
        '7. Ký hiệu cửa: xem bảng thống kê cửa (tờ KT-13).',
        '8. Số trong ô lục giác xanh: điểm điều chỉnh sau rà soát – xem tờ KT-04 và KT-14.',
        '9. GIẢ ĐỊNH CẦN ĐO LẠI: chiều dày tường, cao độ nền so với mặt lộ (chủ nhà đo 0,70m), vị trí giếng, hầm cũ, cột điện; cao trần thả 3,3m.',
    ], 58, 1.9)
    legend_walls(sh, 255, y - 4)


def legend_walls(sh, x, y):
    sh.text(x, y, 'KÝ HIỆU', 2.6, bold=True); y -= 6
    sh.rect(x, y, x + 10, y + 2.5, fill=(.55, .55, .55), edge=BLK, lw=.4); sh.text(x + 13, y + .4, 'Tường hiện trạng giữ lại', 1.9); y -= 5
    sh.rect(x, y, x + 10, y + 2.5, fill=(1, 1, 1), edge=BLK, lw=.4); sh.hatch_rect(x, y, x + 10, y + 2.5, sp=.9); sh.text(x + 13, y + .4, 'Tường xây mới đợt 1', 1.9); y -= 5
    sh.rect(x, y, x + 10, y + 2.5, edge=BLK, lw=.3); sh.text(x + 13, y + .4, 'Vách tôn/nhẹ', 1.9); y -= 5
    sh.line([(x, y + 1.2), (x + 10, y + 1.2)], .2, BLU, [2, 1]); sh.text(x + 13, y + .4, 'Mái/vật thể trên cao (nét đứt)', 1.9); y -= 5
    tag(sh, x + 5, y + 1.2, '1'); sh.text(x + 13, y + .4, 'Điểm tối ưu sau rà soát', 1.9); y -= 5
    sh.circle(x + 5, y + 1.2, 2.2, edge=BLK); sh.text(x + 5, y + 1.2, 'A', 2.2, 'c', 'm'); sh.text(x + 13, y + .4, 'Trục định vị', 1.9); y -= 5
    return y


def sheet_furn_plan(sh):
    v = View(sh, 34, 14, 75, 5.0, 0.9)
    plan_base(sh, v)
    furn_plan(v)
    steps_plan(v)
    # long gas, de nong, be rua chan
    v.rect(6.75, 13.25, 7.25, 13.75, edge=BLU, lw=.3, layer='DEXUAT'); v.line([(6.75, 13.25), (7.25, 13.75)], .15, BLU); v.text(7.0, 13.95, 'Lồng gas', 1.5, anc='c', col=BLU)
    v.rect(7.3, 13.25, 7.8, 13.7, edge=RED, lw=.2, dash=[1, .8]); v.text(7.55, 13.0, 'vị trí cũ', 1.3, anc='c', col=RED)
    v.line([(7.3, 17.4), (7.3, 6.7), (8.6, 5.2)], .5, (.45, .3, .2), [3, 1]); v.text(7.15, 9.0, 'Ống thoát Ø90 đi nổi chân tường', 1.5, rot=90, col=(.45, .3, .2), anc='c')
    v.rect(18.0, 9.6, 18.9, 10.4, edge=BLU, lw=.3, layer='DEXUAT'); v.text(18.45, 10.0, 'DN', 1.5, anc='c', va='m', col=BLU)
    v.rect(18.05, 12.45, 18.35, 13.25, edge=RED, lw=.2, dash=[1, .8]); v.text(18.5, 12.85, 'DN cũ', 1.3, col=RED)
    v.rect(7.95, 6.1, 8.75, 6.7, edge=GRY, lw=.25); v.text(8.35, 5.85, 'Bệ rửa chân', 1.4, anc='c', col=GRY)
    # be tu hoai
    a0, a1, b0, b1 = TANK; v.rect(a0, b0, a1, b1, edge=(.3, .3, .3), lw=.25, dash=[2, 1]); v.text((a0 + a1) / 2, (b0 + b1) / 2, 'Bể tự hoại 2.000L', 1.5, anc='c', va='m', rot=90, col=GRY)
    # quat tran
    for (a, b) in [(11.3, 11.2), (12.0, 9.0)]:
        v.circle(a, b, .6, edge=GRY, lw=.15, dash=[1, .8]); v.text(a, b - .85, 'Quạt trần', 1.3, anc='c', col=GRY)
    for name, a, b, S in ROOMS:
        v.text(a, b, name, 2.0, anc='c', bold=True); v.text(a, b - .38, f'{S:.1f} m²'.replace('.', ','), 1.6, anc='c', col=GRY)
    for n, a, b, _ in PROPOSALS:
        X, Y = v.P(a, b); tag(sh, X, Y, n)
    north(sh, 232, 268, NORTH_PLAN)
    view_title(sh, 34, 282.5, 'MẶT BẰNG BỐ TRÍ CÔNG NĂNG – NỘI THẤT (SAU TỐI ƯU)', '1:75')
    y = notes(sh, 255, 280, 'ĐIỀU CHỈNH SAU RÀ SOÁT ', [f'{n}. {t}' for n, _, _, t in PROPOSALS], 62, 1.75, 1.4)
    y = notes(sh, 255, y - 3, 'GIỮ NGUYÊN (đã chốt 15–17/11)', [
        'Bếp 1 dãy 3,4m: tủ lạnh → chậu đôi → sơ chế 0,9m → bếp từ đôi → bếp gas đơn; cao 850, sâu 600; ổ cắm cách chậu ≥0,6m.',
        'WC tại chỗ WC cũ, cửa lùa quay vào khu giặt (không nhìn ra bàn ăn); máy giặt + sấy chồng; lavabo ngoài.',
    ], 62, 1.75, 1.4)


def sheet_existing(sh):
    v = View(sh, 34, 14, 75, 5.0, 0.9)
    old = [w for w in WALLS if w['kind'] in ('old', 'old_in')]
    import copy
    ex = copy.deepcopy(old)
    for w in ex:
        if w['name'] == 'Tường sau nhà chính': w['ops'] = [(14.3, 15.3, 1.0, 2.4, 'win', 'cs', None)]
    plan_walls(v, ex, tags=False, cols=COLS)
    # nen nha tam cu + vach ton cu
    v.rect(8.0, 7.8, 14.0, 18.5, edge=GRY, lw=.3, dash=[2, 1.2]); v.text(11.0, 13.2, 'NỀN NHÀ TẠM CŨ 6,0 × 10,7m', 2.2, anc='c', bold=True, col=GRY)
    v.text(11.0, 12.6, '(mái tôn + cột gỗ cũ giữ lại; vách tôn cũ tháo bỏ)', 1.7, anc='c', col=GRY)
    v.rect(8.05, 15.3, 11.45, 18.45, edge=RED, lw=.3, dash=[1.5, 1]); v.text(9.75, 16.9, 'WC CŨ – phá dỡ, xây lại tại chỗ', 1.8, anc='c', col=RED)
    v.circle(OLD_PIT[0], OLD_PIT[1], .7, edge=RED, lw=.3, dash=[1.5, 1]); v.text(OLD_PIT[0] + .9, OLD_PIT[1], 'Hầm cầu cũ: hút sạch, rắc vôi, lấp cát, đậy BT', 1.7, col=RED)
    v.circle(WELL[0], WELL[1], .25, edge=BLU, lw=.3); v.text(WELL[0] - .4, WELL[1] + .4, 'Giếng khoan (giữ)', 1.7, anc='r', col=BLU)
    v.text(14.8, 18.8, 'Cửa sổ cuối hành lang → đục thành cửa sau D2 (đợt 1)', 1.7, col=RED)
    v.text(16.0, 4.0, 'HIÊN', 2.0, anc='c', bold=True)
    for name, a, b, S in ROOMS[1:5]:
        v.text(a, b, name, 2.0, anc='c', bold=True)
    v.text(16.65, 15.2, '(kho + thay đồ)', 1.6, anc='c', col=GRY)
    v.dim_chain([14.0, 18.0], 1.6, True, -1); v.dim_chain([2.5, 18.5], 19.3, False, -1); v.dim_chain([8.0, 14.0], 19.3, True, 1); v.dim_chain([7.8, 18.5], 6.6, False, 1)
    v.plan_level(16.0, 7.0, '±0.000', 1.7); v.plan_level(11.0, 9.0, '≈ ±0.000', 1.7); v.plan_level(11.0, 4.5, '−0.100', 1.7)
    north(sh, 232, 268, NORTH_PLAN)
    view_title(sh, 34, 282.5, 'MẶT BẰNG HIỆN TRẠNG & PHÁ DỠ', '1:75')
    notes(sh, 255, 280, 'HIỆN TRẠNG (theo ảnh 11/2026 + đo sơ bộ)', [
        'Nhà kiên cố 4,0 × 16,0m (cả hiên 3,0m): tường gạch 200 sơn, nền gạch men, trần thả nhựa ~3,3m, chân tường ẩm, bong sơn (ảnh 52–56).',
        'Phòng khách 3,6×4,3m, vòm ra hành lang 1,2m bên trái, 2 phòng 2,3×4,0 và 2,3×4,1 bên phải; cửa đi gỗ đỏ có ô kính mờ.',
        'Nền nhà tạm 6,0×10,7m sát hông trái: cột gỗ, mái + vách tôn cũ. WC cũ phía sau, hầm cầu cũ sau WC.',
        'Nền nhà thấp hơn mặt lộ 0,70m, cao hơn sân 5cm – đợt 1 gờ chắn + rãnh tự chảy ra ao (KT-15); đợt 2 nâng nền +0,45, sân +0,40.',
    ], 60, 1.9)
    notes(sh, 255, 200, 'PHÁ DỠ / THÁO (đợt 1)', [
        'Tháo vách tôn cũ nhà tạm (giữ mái, cột gỗ, thay vít có long đền cao su).',
        'Phá dỡ WC cũ; hút sạch, khử trùng, lấp hầm cũ.',
        'Đục mở rộng cửa sổ cuối hành lang thành cửa đi 1,0 × 2,7m (D2) – làm lanh tô BTCT đổ tại chỗ hoặc thép hộp, chống đỡ tạm trước khi đục.',
        'Không đục tường chịu lực khác. Mọi lỗ xuyên tường (ống, máy lạnh) khoan rút lõi.',
    ], 60, 1.9, col=RED)
