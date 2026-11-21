import os, sys
from sheets_rest import *
from sheets_level import sheet_level
from sheets_vent import sheet_vent
OUT = sys.argv[1]
os.makedirs(OUT + '/DXF', exist_ok=True)
SPEC = [
    ('KT-00', 'Bìa – danh mục – ghi chú chung', '–', 100, None),
    ('KT-01', 'Tổng mặt bằng', '1:300', 300, sheet_site),
    ('KT-02', 'Mặt bằng hiện trạng & phá dỡ', '1:75', 75, sheet_existing),
    ('KT-03', 'Mặt bằng kích thước – định vị tường, cửa', '1:75', 75, sheet_dim_plan),
    ('KT-04', 'Mặt bằng bố trí công năng – nội thất (sau tối ưu)', '1:75', 75, sheet_furn_plan),
    ('KT-05', 'Mặt bằng mái – cao độ chính', '1:75', 75, sheet_roof),
    ('KT-06', 'Mặt đứng trước – mặt đứng sau', '1:75', 75, sheet_elev_fb),
    ('KT-07', 'Mặt đứng hông trái – hông phải', '1:75', 75, sheet_elev_side),
    ('KT-08', 'Mặt cắt dọc A-A, B-B', '1:75', 75, sheet_long_sections),
    ('KT-09', 'Mặt cắt ngang C-C', '1:50', 50, sheet_sec_C),
    ('KT-10', 'Mặt cắt ngang D-D', '1:50', 50, sheet_sec_D),
    ('KT-11', 'Chi tiết WC – khu giặt – bậc lên WC', '1:25', 25, sheet_wc),
    ('KT-12', 'Chi tiết bếp – mặt đứng triển khai', '1:40 · 1:50', 40, sheet_kitchen),
    ('KT-13', 'Thống kê cửa – vật liệu hoàn thiện', '–', 100, sheet_schedule),
    ('KT-14', 'Rà soát phương án & tối ưu công năng', '–', 100, sheet_review),
    ('KT-15', 'Cao độ lộ – sân – nền, thoát nước mặt', '1:50', 50, sheet_level),
    ('KT-16', 'Thông gió tự nhiên theo hướng thửa đất', '1:100', 100, sheet_vent),
]
S = []
for i, (no, title, sc, D, fn) in enumerate(SPEC):
    sh = Sheet(no, title, sc, D); sh.idx = i + 1
    if fn: fn(sh)
    else: sheet_cover(sh, [[a, b, c] for a, b, c, _, _ in SPEC])
    S.append(sh)
for sh in S: frame(sh, len(S))
render_pdf(S, OUT + '/BAN_VE_CAI_TAO_NHA_DUYEN_HAI_v1.pdf')
for sh in S:
    if sh.no in ('KT-00', 'KT-13', 'KT-14'): continue
    render_dxf(sh, f'{OUT}/DXF/{sh.no}.dxf')
print('ok', len(S))
