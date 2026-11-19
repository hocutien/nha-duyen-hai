# Bo ve 2 dau ra: PDF (reportlab, vector) + DXF (ezdxf). Toa do giay = mm, goc duoi-trai.
import math, ezdxf
from ezdxf.enums import TextEntityAlignment as TA
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import stringWidth
MM = 72 / 25.4
pdfmetrics.registerFont(TTFont('F', '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'))
pdfmetrics.registerFont(TTFont('FB', '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'))
PW, PH = 420, 297  # A3 ngang

BLK = (0, 0, 0); GRY = (.45, .45, .45); LGR = (.75, .75, .75); RED = (.75, .12, .12); BLU = (0, .33, .78); GRN = (.1, .5, .2)
LAYER_COL = {'KHUNG': 7, 'TUONG': 7, 'TUONG_MOI': 1, 'HATCH': 8, 'CUA': 4, 'NOITHAT': 8, 'KICHTHUOC': 3, 'CHU': 7, 'TRUC': 6, 'DEXUAT': 5, 'MAI': 30, 'NEN': 8, 'COTE': 2, 'THIETBI': 9, 'DOT2': 9}


def fs(h):  # chieu cao chu (mm) -> co chu (pt)
    return h * MM / 0.72


class Sheet:
    def __init__(s, no, title, scale, D):
        s.no, s.title, s.scale, s.D = no, title, scale, D
        s.it = []

    def line(s, pts, lw=.25, col=BLK, dash=None, layer='0'):
        s.it.append(('L', pts, lw, col, dash, layer))

    def poly(s, pts, fill=None, edge=BLK, lw=.25, dash=None, layer='0', close=True):
        s.it.append(('P', pts, fill, edge, lw, dash, layer, close))

    def rect(s, x0, y0, x1, y1, **k):
        s.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], **k)

    def text(s, x, y, t, h=2.5, anc='l', va='b', rot=0, bold=False, col=BLK, layer='CHU'):
        s.it.append(('T', x, y, str(t), h, anc, va, rot, bold, col, layer))

    def image(s, x, y, w, h, path):
        s.it.append(('I', x, y, w, h, path))

    def circle(s, x, y, r, fill=None, edge=BLK, lw=.25, dash=None, layer='0'):
        s.it.append(('C', x, y, r, fill, edge, lw, dash, layer))

    def arc(s, x, y, r, a0, a1, lw=.18, col=BLK, dash=None, layer='0'):
        n = max(6, int(abs(a1 - a0) / 6))
        pts = [(x + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)), y + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
        s.line(pts, lw, col, dash, layer)

    def hatch_rect(s, x0, y0, x1, y1, sp=1.2, lw=.13, col=RED, layer='HATCH', ang=45):
        # duong gach cheo 45 do cat trong hinh chu nhat
        if x1 < x0: x0, x1 = x1, x0
        if y1 < y0: y0, y1 = y1, y0
        c = math.floor((x0 - y1) / sp) * sp
        while c < x1 - y0:
            # duong y = x - c (ang 45)
            p = []
            for (xa, ya) in [(x0, x0 - c), (x1, x1 - c), (y0 + c, y0), (y1 + c, y1)]:
                if x0 - 1e-9 <= xa <= x1 + 1e-9 and y0 - 1e-9 <= ya <= y1 + 1e-9: p.append((xa, ya))
            p = sorted(set((round(a, 4), round(b, 4)) for a, b in p))
            if len(p) >= 2 and math.dist(p[0], p[-1]) > 1e-3:
                s.line([p[0], p[-1]], lw, col, None, layer)
            c += sp


def _dash(c, d):
    if d: c.setDash([x * MM for x in d])
    else: c.setDash([])


def render_pdf(sheets, path):
    c = canvas.Canvas(path, pagesize=(PW * MM, PH * MM))
    c.setTitle('Bo ban ve cai tao nha Duyen Hai'); c.setAuthor('Nguyen Manh Tien')
    for sh in sheets:
        c.setLineJoin(1); c.setLineCap(1)
        for it in sh.it:
            k = it[0]
            if k == 'L':
                _, pts, lw, col, dash, _l = it
                c.setStrokeColorRGB(*col); c.setLineWidth(lw * MM); _dash(c, dash)
                p = c.beginPath(); p.moveTo(pts[0][0] * MM, pts[0][1] * MM)
                for x, y in pts[1:]: p.lineTo(x * MM, y * MM)
                c.drawPath(p, stroke=1, fill=0)
            elif k == 'P':
                _, pts, fill, edge, lw, dash, _l, close = it
                p = c.beginPath(); p.moveTo(pts[0][0] * MM, pts[0][1] * MM)
                for x, y in pts[1:]: p.lineTo(x * MM, y * MM)
                if close: p.close()
                if fill: c.setFillColorRGB(*fill)
                if edge: c.setStrokeColorRGB(*edge); c.setLineWidth(lw * MM); _dash(c, dash)
                c.drawPath(p, stroke=1 if edge else 0, fill=1 if fill else 0)
            elif k == 'C':
                _, x, y, r, fill, edge, lw, dash, _l = it
                if fill: c.setFillColorRGB(*fill)
                if edge: c.setStrokeColorRGB(*edge); c.setLineWidth(lw * MM); _dash(c, dash)
                c.circle(x * MM, y * MM, r * MM, stroke=1 if edge else 0, fill=1 if fill else 0)
            elif k == 'I':
                _, x, y, w, h, path = it
                c.drawImage(path, x * MM, y * MM, w * MM, h * MM, preserveAspectRatio=True, anchor='c')
            elif k == 'T':
                _, x, y, t, h, anc, va, rot, bold, col, _l = it
                f = 'FB' if bold else 'F'; z = fs(h)
                w = stringWidth(t, f, z) / MM
                dx = {'l': 0, 'c': -w / 2, 'r': -w}[anc]; dy = {'b': 0, 'm': -h / 2, 't': -h}[va]
                c.saveState(); c.translate(x * MM, y * MM); c.rotate(rot)
                c.setFillColorRGB(*col); c.setFont(f, z); c.drawString(dx * MM, dy * MM, t); c.restoreState()
        c.showPage()
    c.save()


def _aci(col):
    if col == RED: return 1
    if col == BLU: return 5
    if col == GRN: return 3
    if col in (GRY, LGR): return 8
    return 256


def render_dxf(sh, path):
    D = sh.D
    doc = ezdxf.new('R2013', setup=True); doc.units = ezdxf.units.MM
    st = doc.styles.get('Standard') if 'Standard' in doc.styles else doc.styles.new('Standard')
    st.dxf.font = 'arial.ttf'
    for n, c in LAYER_COL.items():
        if n not in doc.layers: doc.layers.add(n, color=c)
    msp = doc.modelspace()
    T = lambda p: (p[0] * D, p[1] * D)
    for it in sh.it:
        k = it[0]
        if k == 'L':
            _, pts, lw, col, dash, lay = it
            a = {'layer': lay if lay in LAYER_COL else '0', 'color': _aci(col), 'lineweight': int(min(211, max(0, round(lw * 100))))}
            if dash: a['linetype'] = 'DASHED'; a['ltscale'] = D / 50
            msp.add_lwpolyline([T(p) for p in pts], dxfattribs=a)
        elif k == 'P':
            _, pts, fill, edge, lw, dash, lay, close = it
            lay = lay if lay in LAYER_COL else '0'
            if fill and fill not in ((1, 1, 1),):
                h = msp.add_hatch(color=8 if fill != BLK else 7, dxfattribs={'layer': 'HATCH' if lay in ('TUONG', 'TUONG_MOI') else lay})
                h.paths.add_polyline_path([T(p) for p in pts], is_closed=True)
                if fill not in (BLK,):
                    g = sum(fill) / 3; h.set_solid_fill(color=8 if g < .7 else 9)
            if edge:
                a = {'layer': lay, 'color': _aci(edge), 'lineweight': int(min(211, max(0, round(lw * 100))))}
                if dash: a['linetype'] = 'DASHED'; a['ltscale'] = D / 50
                msp.add_lwpolyline([T(p) for p in pts], close=close, dxfattribs=a)
        elif k == 'C':
            _, x, y, r, fill, edge, lw, dash, lay = it
            a = {'layer': lay if lay in LAYER_COL else '0', 'color': _aci(edge or BLK)}
            if dash: a['linetype'] = 'DASHED'; a['ltscale'] = D / 50
            msp.add_circle(T((x, y)), r * D, dxfattribs=a)
        elif k == 'T':
            _, x, y, t, h, anc, va, rot, bold, col, lay = it
            al = {('l', 'b'): TA.BOTTOM_LEFT, ('c', 'b'): TA.BOTTOM_CENTER, ('r', 'b'): TA.BOTTOM_RIGHT,
                  ('l', 'm'): TA.MIDDLE_LEFT, ('c', 'm'): TA.MIDDLE_CENTER, ('r', 'm'): TA.MIDDLE_RIGHT,
                  ('l', 't'): TA.TOP_LEFT, ('c', 't'): TA.TOP_CENTER, ('r', 't'): TA.TOP_RIGHT}[(anc, va)]
            msp.add_text(t, height=h * D, rotation=rot, dxfattribs={'layer': lay if lay in LAYER_COL else 'CHU', 'color': _aci(col), 'style': 'Standard'}).set_placement(T((x, y)), align=al)
    doc.saveas(path)


class View:
    """Anh xa toa do the gioi (m) -> giay (mm). X=f(a,b), Y=z hoac b."""
    def __init__(s, sh, ox, oy, den, wx0=0, wy0=0, flip=False):
        s.sh, s.ox, s.oy, s.den, s.wx0, s.wy0, s.flip = sh, ox, oy, den, wx0, wy0, flip
        s.k = 1000 / den

    def P(s, x, y):
        xx = (s.wx0 - x) if s.flip else (x - s.wx0)
        return (s.ox + xx * s.k, s.oy + (y - s.wy0) * s.k)

    def line(s, pts, lw=.25, col=BLK, dash=None, layer='0'):
        s.sh.line([s.P(*p) for p in pts], lw, col, dash, layer)

    def poly(s, pts, **kw):
        s.sh.poly([s.P(*p) for p in pts], **kw)

    def rect(s, x0, y0, x1, y1, **kw):
        s.poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], **kw)

    def text(s, x, y, t, h=2.2, **kw):
        X, Y = s.P(x, y); s.sh.text(X, Y, t, h, **kw)

    def circle(s, x, y, r, **kw):
        X, Y = s.P(x, y); s.sh.circle(X, Y, r * s.k, **kw)

    def arc(s, x, y, r, a0, a1, **kw):
        X, Y = s.P(x, y)
        if s.flip: a0, a1 = 180 - a0, 180 - a1
        s.sh.arc(X, Y, r * s.k, a0, a1, **kw)

    def hatch(s, x0, y0, x1, y1, **kw):
        X0, Y0 = s.P(x0, y0); X1, Y1 = s.P(x1, y1); s.sh.hatch_rect(X0, Y0, X1, Y1, **kw)

    # ---- kich thuoc ----
    def dim_chain(s, vals, at, horiz=True, txt_side=1, ext_from=None, h=2.0, layer='KICHTHUOC', fmt=None):
        """vals: toa do the gioi lien tiep; at: vi tri duong kich thuoc (the gioi). horiz: kich thuoc theo X."""
        sh = s.sh; vals = list(vals)
        for i, v in enumerate(vals):
            if horiz:
                A = s.P(v, at); B = s.P(v, ext_from) if ext_from is not None else (A[0], A[1] - 2 * txt_side)
                sh.line([(A[0], B[1] + (1 if B[1] < A[1] else -1) * 1.0), (A[0], A[1] + 1.2 * txt_side)], .13, BLK, None, layer)
                sh.line([(A[0] - .9, A[1] - .9), (A[0] + .9, A[1] + .9)], .35, BLK, None, layer)
            else:
                A = s.P(at, v); B = s.P(ext_from, v) if ext_from is not None else (A[0] - 2 * txt_side, A[1])
                sh.line([(B[0] + (1 if B[0] < A[0] else -1) * 1.0, A[1]), (A[0] + 1.2 * txt_side, A[1])], .13, BLK, None, layer)
                sh.line([(A[0] - .9, A[1] - .9), (A[0] + .9, A[1] + .9)], .35, BLK, None, layer)
        if horiz:
            a, b = s.P(min(vals), at), s.P(max(vals), at); sh.line([(a[0] - 1.5, a[1]), (b[0] + 1.5, b[1])], .13, BLK, None, layer)
        else:
            a, b = s.P(at, min(vals)), s.P(at, max(vals)); sh.line([(a[0], a[1] - 1.5), (b[0], b[1] + 1.5)], .13, BLK, None, layer)
        for v0, v1 in zip(vals, vals[1:]):
            L = round(abs(v1 - v0) * 1000)
            t = fmt(L) if fmt else f'{L}'
            if horiz:
                X = (s.P(v0, at)[0] + s.P(v1, at)[0]) / 2; Y = s.P(v0, at)[1]
                small = abs(s.P(v1, at)[0] - s.P(v0, at)[0]) < len(t) * h * .62
                sh.text(X, Y + (0.8 if txt_side > 0 else -0.8 - h), t, h * (.85 if small else 1), 'c', 'b', layer=layer)
            else:
                X = s.P(at, v0)[0]; Y = (s.P(at, v0)[1] + s.P(at, v1)[1]) / 2
                small = abs(s.P(at, v1)[1] - s.P(at, v0)[1]) < len(t) * h * .62
                sh.text(X + (-0.8 if txt_side > 0 else 0.8 + h), Y, t, h * (.85 if small else 1), 'c', 'b', rot=90, layer=layer)

    def level(s, x, y, t, h=2.0, side='r', col=BLK):
        """Ky hieu cao do trong mat dung/cat: tam giac + chu"""
        X, Y = s.P(x, y); sh = s.sh
        sh.poly([(X, Y), (X - 1.5, Y + 2.2), (X + 1.5, Y + 2.2)], fill=None, edge=col, lw=.2, layer='COTE')
        sh.line([(X - 1.5, Y + 2.2), (X + (14 if side == 'r' else -14), Y + 2.2)], .15, col, None, 'COTE')
        sh.text(X + (2 if side == 'r' else -2), Y + 2.8, t, h, 'l' if side == 'r' else 'r', 'b', col=col, layer='COTE')

    def plan_level(s, x, y, t, h=2.0, col=BLK):
        X, Y = s.P(x, y); w = len(t) * h * .62 + 2
        s.sh.rect(X - w / 2, Y - h / 2 - 1, X + w / 2, Y + h / 2 + 1, fill=(1, 1, 1), edge=col, lw=.18, layer='COTE')
        s.sh.text(X, Y, t, h, 'c', 'm', col=col, layer='COTE')


def tag(sh, X, Y, t, col=BLU, r=2.4, h=2.2):
    # the de xuat (luc giac) tren giay
    pts = [(X + r * math.cos(math.radians(30 + 60 * i)), Y + r * math.sin(math.radians(30 + 60 * i))) for i in range(6)]
    sh.poly(pts, fill=(1, 1, 1), edge=col, lw=.3, layer='DEXUAT'); sh.text(X, Y, t, h, 'c', 'm', bold=True, col=col, layer='DEXUAT')


def wrap(t, n):
    out, cur = [], ''
    for w in t.split(' '):
        if len(cur) + len(w) + 1 > n and cur: out.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    if cur: out.append(cur)
    return out
