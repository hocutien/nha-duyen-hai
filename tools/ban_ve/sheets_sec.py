from section import *


def callout(v, x, z, t, tx, tz, h=1.7, col=BLK):
    X, Y = v.P(x, z); TX, TY = v.P(tx, tz)
    sh = v.sh
    sh.circle(X, Y, .5, fill=col, edge=col, lw=.1)
    sh.line([(X, Y), (TX, TY)], .15, col, None, 'CHU')
    lines = t if isinstance(t, list) else [t]
    right = TX >= X
    w = max(stringWidth(l, 'F', fs(h)) / MM for l in lines)
    sh.line([(TX, TY), (TX + (w + 1) * (1 if right else -1), TY)], .15, col, None, 'CHU')
    for i, l in enumerate(lines):
        sh.text(TX + (0.5 if right else -0.5), TY + .6 - i * h * 1.4 if i == 0 else TY - .9 - i * h * 1.35 + h * .1, l, h, 'l' if right else 'r', 'b' if i == 0 else 't', col=col)


def septic(S):
    v = S.v
    if S.plane == 'a' and S.cut and TANK[0] <= S.c <= TANK[1]:
        def f():
            v.poly([(1.9, -0.1), (2.3, .35), (4.6, .35), (5.1, -0.1)], fill=(.9, .85, .75), edge=BLK, lw=.2, layer='NEN')
            v.rect(2.15, -1.03, 4.75, -0.93, fill=CONC, edge=BLK, lw=.3, layer='NEN')
            pts = [(2.3 + .6 - .6 * math.cos(math.radians(a)), -0.33 + .6 * math.sin(math.radians(a))) for a in range(-90, 91, 15)][::-1]
            pts = [(2.9 - .6 * math.cos(math.radians(a)), -0.33 + .6 * math.sin(math.radians(a))) for a in range(-90, 91, 15)]
            pts2 = [(4.0 + .6 * math.cos(math.radians(a)), -0.33 + .6 * math.sin(math.radians(a))) for a in range(90, -91, -15)]
            v.poly(pts[::-1][::-1] + pts2, fill=(.75, .8, .82), edge=BLK, lw=.4, layer='THIETBI')
            for b in (2.75, 4.15): v.rect(b - .3, .27, b + .3, .4, fill=(.55, .6, .65), edge=BLK, lw=.3, layer='THIETBI')
            v.text(3.45, -0.35, 'BỂ TỰ HOẠI NHỰA 2.000L', 1.5, anc='c', va='m', bold=True)
            v.text(3.45, -0.6, 'có ngăn lọc · neo chống nổi', 1.3, anc='c', va='m')
        S.cuts.append(f)


def sec_long(sh, name, c, oy, title, calls):
    S = Sec(sh, 'a', c, -1, True, 40, oy, 75, -3.0)
    building(S); septic(S); S.draw(); ground(S, -3.0, 21.0)
    v = S.v
    levels(S, -2.9, [(0, '±0.000 nền nhà'), (0.5, '+0.500 sàn WC / mặt lộ'), (3.3, '+3.300 trần'), (4.5, '+4.500')], 'r')
    v.dim_chain([0, 2.2, 3.3, 4.5], 20.6, False, -1)
    for args in calls: callout(v, *args)
    view_title(sh, 40, oy + 5.9 * 13.33, title, '1:75')


def sheet_long_sections(sh):
    sec_long(sh, 'A', 14.8, 190, 'MẶT CẮT A-A (dọc qua hành lang nhà chính, nhìn về hông trái)', [
        (4.0, 4.56, ['Mái hiện trạng: tôn sau tường chắn mái +4.500', '(giả định – khảo sát lại, chống dột trước khi vào ở)'], 5.5, 5.25),
        (12.0, 3.31, 'Trần thả nhựa hiện trạng +3.300', 12.5, 3.9),
        (18.4, 2.0, ['Cửa sau D2 1.000×2.700 đục mới', 'lanh tô BTCT 200×150, gối 200'], 19.5, 1.2),
        (19.2, 2.7, 'Mái hắt tôn 1,2m', 20.0, 3.3),
        (9.0, -0.05, 'Nền BT hiện trạng + gạch men; đợt 2 nâng +0.450', 9.5, -0.6),
    ])
    sec_long(sh, 'B', 9.0, 84, 'MẶT CẮT B-B (dọc qua bể tự hoại – bếp – WC, nhìn về hông trái)', [
        (16.5, 0.45, ['Sàn WC +0.500: gạch chống trơn 300×300 / vữa / chống thấm', '2 lớp lật tường 300 (khu tắm 1.800) / BT lót 80 / cát đầm'], 17.5, -0.65),
        (12.0, zroof_annex(9.0) + .02, ['Mái tôn cũ dốc ~10% về hông trái, xà gồ gỗ cũ,', 'cách nhiệt túi khí dưới tôn'], 12.5, 3.85),
        (7.8, 2.6, ['Tường gạch ống 100 trát 2 mặt (mới)', 'trên đà kiềng BTCT 200×200'], 5.0, 3.6),
        (3.4, 0.35, ['Nắp bể nhô ~0,35, đắp đất phủ', 'CẤM XE ĐÈ – ụ chắn bánh ([12])'], 0.0, 2.3),
        (17.0, 2.9, 'Trần nhựa WC +2.900', 19.5, 3.4),
    ])


def sec_cross(sh, c, title, calls, extra=None):
    S = Sec(sh, 'b', c, +1, True, 30, 110, 50, 5.0, z0=-0.9)
    building(S); S.draw(); ground(S, 5.0, 20.0, road=False)
    v = S.v
    levels(S, 5.1, [(0, '±0.000'), (0.5, '+0.500'), (2.9, '+2.900'), (3.3, '+3.300'), (4.5, '+4.500')], 'r')
    v.dim_chain([-0.1, 0, 1.0, 2.4, 3.3, 4.5, 4.62], 19.6, False, -1)
    v.dim_chain([7.95, 8.05, 14.0, 14.2, 15.4, 15.5, 17.8, 18.0], -0.75, True, -1)
    for args in calls: callout(v, *args)
    if extra: extra(S)
    view_title(sh, 33, 283, title, '1:50')


def sheet_sec_C(sh):
    sec_cross(sh, 11.2, 'MẶT CẮT C-C (ngang qua bếp – bàn ăn – hành lang – phòng ngủ 1)', [
        (8.4, 0.85, ['Mặt bếp đá/gạch cao 850, sâu 600', 'chậu đôi dưới cửa sổ S3'], 9.3, 1.9),
        (8.0, 1.5, ['Cửa sổ S3', '1.000×950, đáy +1.050'], 7.4, 2.1),
        (8.0, 2.65, ['Dải bông gió xi măng tận dụng +2.400→+2.950,', 'mặt trong căng lưới inox chống muỗi'], 9.0, 4.4),
        (11.0, zroof_annex(11.0) + .02, ['Mái tôn cũ dốc ~10%, xà gồ gỗ cũ,', 'cách nhiệt túi khí dưới tôn'], 10.0, 5.0),
        (17.9, 1.7, ['Cửa sổ S1 hiện trạng 1.200×1.400', 'thêm lưới chống muỗi; 1 ô mở khoá thoát hiểm'], 18.3, 4.25),
        (11.3, 0.75, 'Bàn ăn 4 người 800×1.200', 12.0, 1.4),
    ])
    notes(sh, 330, 280, 'GHI CHÚ C-C', [
        'Nhà phụ: nền ±0.000 giữ nền nhà tạm cũ, láng vữa + gạch chống trơn.',
        'Mái nhà phụ gác cột gỗ cũ, tường xây mới không đỡ mái; khe giữa đỉnh tường và mái để thoáng hoặc bịt lưới.',
        'Lối đi bếp – bàn ăn ≥1,75m (chuẩn NKBA ≥1,07).',
        'Máy hút mùi đáy +1.550 (cách mặt bếp 700), ống thải xuyên tường trái.',
        'Đợt 2: nâng nền nhà chính + nhà phụ +0.450 → trần nhà chính còn 2,85m; cửa nhà phụ lanh tô +2.650 còn 2,2m.',
    ], 36, 1.75)


def sheet_sec_D(sh):
    sec_cross(sh, 16.2, 'MẶT CẮT D-D (ngang qua WC – chiếu nghỉ – khu giặt – hành lang – phòng ngủ 2)', [
        (11.9, 0.5, ['Chiếu nghỉ 1.000×900 cao +0.500 ([1])', 'mặt gạch chống trơn, mũi bậc nẹp chống trượt'], 12.6, 1.6),
        (12.9, 0.17, '2 bậc: cao 170, rộng 300', 14.6, 0.75),
        (11.4, 1.6, ['Cửa lùa WC D9 800×2.080', 'ray treo, không ray sàn'], 12.0, 3.2),
        (8.75, 0.55, ['Khay tắm, phễu thu', 'có bẫy mùi'], 7.4, 1.3),
        (10.0, zroof_annex(10.0) + .02, ['Mái tôn cũ dốc ~10%, xà gồ gỗ cũ,', 'cách nhiệt túi khí dưới tôn'], 9.0, 4.6),
        (16.8, 0.45, 'Giường phụ / nôi em bé ([13])', 18.2, 1.0),
    ], extra=lambda S: (S.v.line([(11.5, 1.4), (12.45, 1.4), (13.05, 1.07), (13.05, 0.17)], .5, BLU), S.v.text(13.1, 1.15, 'Tay vịn inox Ø32 cao 900', 1.5, col=BLU)))
    notes(sh, 330, 280, 'GHI CHÚ D-D', [
        'Đường đêm P.ngủ → WC: hành lang 1,2m → cửa D4 → khu giặt → 2 bậc → chiếu nghỉ → cửa lùa. Đèn cảm biến chân tường mỗi chặng.',
        'Bậc xây gạch đặc trên nền cũ, không liên kết sàn WC: đợt 2 nâng nền +0.450 thì đập bỏ dễ, WC chỉ còn cao hơn 5cm.',
        'Ống thoát chính Ø90 chạy dưới sàn WC (+0.300) ra hông trái; nắp kiểm tra ở góc.',
        'Máy nước nóng trực tiếp 4,5kW treo đáy cao 1,4m so sàn WC, ngoài tia nước.',
    ], 36, 1.75)
