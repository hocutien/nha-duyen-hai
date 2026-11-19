from common import *

CONC = (.82, .82, .82)


def zroof_annex(a): return 3.0 + (a - 7.75) / 6.25 * 0.6
def zceil_annex(a): return 2.93 + (a - 7.95) / 6.05 * 0.6


class Sec:
    """Mat cat / mat dung. plane: 'a' (mat phang a=c, truc ngang = b) hoac 'b' (b=c, truc ngang = a).
    look: +1/-1 huong nhin theo truc vuong goc. cut: True = mat cat, False = mat dung."""
    def __init__(s, sh, plane, c, look, cut, ox, oy, den, x0, flip=None, z0=0.0):
        s.plane, s.c, s.look, s.cut = plane, c, look, cut
        if flip is None:
            flip = (plane == 'a' and look > 0) or (plane == 'b' and look < 0)
        s.v = View(sh, ox, oy, den, x0, z0, flip)
        s.faces = []; s.cuts = []

    # khoang cach theo huong nhin (>=0 nghia la nam phia truoc mat nhin)
    def dist(s, lo, hi):
        if s.look > 0: return lo - s.c if lo >= s.c - 1e-9 else None
        return s.c - hi if hi <= s.c + 1e-9 else None

    def contains(s, lo, hi): return s.cut and lo - 1e-9 <= s.c <= hi + 1e-9

    def box(s, a0, a1, b0, b1, z0, z1, style='face', fill=(1, 1, 1), lw=.25, label=None, dash=None, hatch=False, layer='NOITHAT'):
        if s.plane == 'a': n0, n1, x0, x1 = a0, a1, b0, b1
        else: n0, n1, x0, x1 = b0, b1, a0, a1
        if s.contains(n0, n1):
            s.cuts.append(lambda v=s.v: (v.rect(x0, z0, x1, z1, fill=(.88, .88, .88), edge=BLK, lw=.35, layer=layer), v.hatch(x0, z0, x1, z1, sp=1.4, col=GRY) if hatch else None,
                                         v.text((x0 + x1) / 2, z1 + .08, label, 1.5, anc='c', col=GRY) if label else None))
        else:
            d = s.dist(n0, n1)
            if d is None: return
            s.faces.append((d, lambda v=s.v: (v.rect(x0, z0, x1, z1, fill=fill, edge=BLK, lw=lw, dash=dash, layer=layer),
                                               v.text((x0 + x1) / 2, (z0 + z1) / 2, label, 1.5, anc='c', va='m', col=GRY) if label else None)))

    def walls(s, walls=WALLS):
        for w in walls:
            par = (w['ax'] == 'y') == (s.plane == 'a')  # tuong song song mat phang
            if par:
                d = s.dist(w['t0'], w['t1'])
                if d is None or (s.contains(w['t0'], w['t1'])): continue
                s.faces.append((d, lambda w=w: s.wall_face(w)))
            else:
                if s.contains(w['s0'], w['s1']):
                    s.cuts.append(lambda w=w: s.wall_cut(w))
                else:
                    d = s.dist(w['s0'], w['s1'])
                    if d is None: continue
                    s.faces.append((d + .001, lambda w=w: s.v.rect(w['t0'], w['z0'], w['t1'], w['z1'], fill=(1, 1, 1), edge=BLK, lw=.3, layer='TUONG')))

    def wall_face(s, w):
        v = s.v
        v.rect(w['s0'], w['z0'], w['s1'], w['z1'], fill=(1, 1, 1), edge=BLK, lw=.35, layer='TUONG')
        for b in BANDS:
            if (b[0] == w['ax']) and abs(b[3] - (w['t0'] + w['t1']) / 2) < .1:
                s.band(b[1], b[2], b[4], b[5])
        for o in w['ops']: s.op_face(o)

    def band(s, x0, x1, z0, z1):
        v = s.v
        v.rect(x0, z0, x1, z1, fill=(.93, .93, .9), edge=BLK, lw=.2, layer='TUONG')
        n = int((x1 - x0) / .14)
        for i in range(1, n): v.line([(x0 + i * (x1 - x0) / n, z0), (x0 + i * (x1 - x0) / n, z1)], .1, GRY, None, 'TUONG')
        for j in range(1, 4): v.line([(x0, z0 + j * (z1 - z0) / 4), (x1, z0 + j * (z1 - z0) / 4)], .1, GRY, None, 'TUONG')

    def op_face(s, o):
        v = s.v; s0, s1, zb, zt, typ, code, ex = o
        L = lambda pts, lw=.2, dash=None: v.line(pts, lw, BLK, dash, 'CUA')
        v.rect(s0, zb, s1, zt, fill=(.96, .97, 1), edge=BLK, lw=.3, layer='CUA')
        if typ == 'win' and ex == 'clear':  # cua so rong kinh tron, khong chia o, khong song
            v.rect(s0 + .05, zb + .05, s1 - .05, zt - .05, edge=BLK, lw=.15, layer='CUA'); m = (s0 + s1) / 2
            L([(m, zb + .05), (m, zt - .05)], .12); L([(s0 - .1, zb - .03), (s1 + .1, zb - .03)], .5)
        elif typ == 'win':
            m = (s0 + s1) / 2
            L([(m, zb), (m, zt)], .2); v.rect(s0 + .05, zb + .05, s1 - .05, zt - .05, edge=BLK, lw=.15, layer='CUA')
            for k in range(1, 6): L([(s0 + .05, zb + k * (zt - zb) / 6), (s1 - .05, zb + k * (zt - zb) / 6)], .1)
            L([(s0 - .05, zb), (s1 + .05, zb)], .4)
        elif typ == 'door':
            leaf = ex[2] if len(ex) > 2 else zt
            v.rect(s0 + .04, zb, s1 - .04, leaf - .02, edge=BLK, lw=.2, layer='CUA')
            v.rect(s0 + .14, zb + .9 if leaf > 2 else zb + .1, s1 - .14, leaf - .15, edge=BLK, lw=.12, layer='CUA')
            hx = s1 - .12 if ex[0] == 'lo' else s0 + .12
            v.circle(hx, zb + 1.0, .03, edge=BLK, lw=.2)
            if leaf < zt - .05:
                L([(s0, leaf), (s1, leaf)], .25)
                for k in range(1, int((s1 - s0) / .12)): L([(s0 + k * .12, leaf), (s0 + k * .12, zt)], .1)
        elif typ == 'door2':
            leaf = ex if ex else zt
            m = (s0 + s1) / 2
            for a, b in ((s0, m), (m, s1)):
                v.rect(a + .03, zb, b - .03, leaf - .02, edge=BLK, lw=.2, layer='CUA')
                for k in range(1, int((b - a) / .12)): L([(a + k * .12, zb + .1), (a + k * .12, leaf - .1)], .08)
            if leaf < zt - .05:
                L([(s0, leaf), (s1, leaf)], .25)
                for k in range(1, int((s1 - s0) / .12)): L([(s0 + k * .12, leaf), (s0 + k * .12, zt)], .1)
        elif typ == 'roll':
            for k in range(1, int((zt - zb) / .1)): L([(s0, zb + k * .1), (s1, zb + k * .1)], .08)
        elif typ == 'slide':
            m = (s0 + s1) / 2
            v.rect(s0 + .03, zb, m + .05, zt - .03, edge=BLK, lw=.2, layer='CUA'); v.rect(m - .05, zb + .01, s1 - .03, zt - .04, edge=BLK, lw=.2, layer='CUA')
        elif typ == 'vent':
            for k in range(1, int((zt - zb) / .06)): L([(s0, zb + k * .06), (s1, zb + k * .06)], .1)
        elif typ == 'arch':
            pass
        if code: v.text((s0 + s1) / 2, zt + .08, code, 1.6, anc='c', col=(.1, .3, .55))

    def wall_cut(s, w):
        v = s.v; c = s.c
        ops = [o for o in w['ops'] if o[0] <= c <= o[1]]
        spans = [(w['z0'], w['z1'])]
        for o in ops:
            new = []
            for z0, z1 in spans:
                if o[3] <= z0 or o[2] >= z1: new.append((z0, z1)); continue
                if o[2] > z0: new.append((z0, o[2]))
                if o[3] < z1: new.append((o[3], z1))
            spans = new
        for z0, z1 in spans:
            if z1 - z0 < 1e-6: continue
            if w['kind'] in ('old', 'old_in'): v.rect(w['t0'], z0, w['t1'], z1, fill=(.45, .45, .45), edge=BLK, lw=.5, layer='TUONG')
            elif w['kind'] == 'new': v.rect(w['t0'], z0, w['t1'], z1, fill=(1, 1, 1), edge=BLK, lw=.5, layer='TUONG_MOI'); v.hatch(w['t0'], z0, w['t1'], z1, sp=.9)
            else: v.rect(w['t0'], z0, w['t1'], z1, fill=(1, 1, 1), edge=BLK, lw=.3, layer='TUONG')
        for o in ops:
            if o[4] == 'win': v.line([((w['t0'] + w['t1']) / 2, o[2]), ((w['t0'] + w['t1']) / 2, o[3])], .2, BLK, None, 'CUA')
            if o[4] in ('door', 'door2', 'slide', 'roll', 'win') and o[3] < w['z1']:
                pass
        # dai bong gio cat
        tm = (w['t0'] + w['t1']) / 2
        for b in BANDS:
            if b[0] == w['ax'] and b[1] <= c <= b[2] and abs(b[3] - tm) < .1:
                v.rect(w['t0'], b[4], w['t1'], b[5], fill=(.93, .93, .9), edge=BLK, lw=.3, layer='TUONG')
                v.line([(w['t0'], b[4]), (w['t1'], b[5])], .12, GRY); v.line([(w['t0'], b[5]), (w['t1'], b[4])], .12, GRY)
        # mong
        tm = (w['t0'] + w['t1']) / 2
        if w['kind'] == 'new':
            v.rect(tm - .1, -.2, tm + .1, 0, fill=CONC, edge=BLK, lw=.3, layer='TUONG_MOI')
            v.rect(tm - .2, -.6, tm + .2, -.2, edge=GRY, lw=.2, dash=[1.2, .8], layer='TUONG_MOI')
        elif w['kind'] == 'old':
            v.rect(tm - .3, -.8, tm + .3, -.1, edge=GRY, lw=.2, dash=[1.2, .8], layer='TUONG')

    def draw(s):
        for d, f in sorted(s.faces, key=lambda x: -x[0]): f()
        for f in s.cuts: f()


def building(S, furn=True, outside=True):
    """Nap toan bo nha vao Sec S (tuong, cot, san, mai, noi that)"""
    S.walls()
    for a0, b0, w, d, z1, k in COLS:
        S.box(a0, a0 + w, b0, b0 + d, 0 if k == 'old' else .4, z1, fill=(.95, .93, .9) if k == 'wood' else (1, 1, 1), layer='TUONG')
    if furn:
        for a0, a1, b0, b1, z0, z1, name, k in FURN:
            if k in ('cn', 'b1', 'b2'): S.box(a0, a1, b0, b1, 0, z1, fill=(1, 1, 1), lw=.3); continue
            if k == 'ac': S.box(a0, a1, b0, b1, z0, z1, fill=(1, 1, 1), label=None); continue
            S.box(a0, a1, b0, b1, z0, z1, label=name if (z1 - z0) > .5 and (min(a1 - a0, b1 - b0) > .3 or True) else None, lw=.2)
    if outside:
        for a0, a1, b0, b1, z0, z1, name in OUT:
            S.box(a0, a1, b0, b1, z0, z1, fill=(1, 1, 1), label=name if not S.cut else None, lw=.25, layer='THIETBI')
    # san / nen (chi mat cat)
    if S.cut:
        for a0, a1, b0, b1, z, t, name in SLABS:
            if S.plane == 'a': n0, n1, x0, x1 = a0, a1, b0, b1
            else: n0, n1, x0, x1 = b0, b1, a0, a1
            if n0 <= S.c <= n1:
                S.cuts.append(lambda x0=x0, x1=x1, z=z, t=t: (S.v.rect(x0, z - t, x1, z, fill=CONC, edge=BLK, lw=.35, layer='NEN'), S.v.hatch(x0, z - t, x1, z, sp=1.6, col=GRY)))
                if z > .2:
                    S.cuts.append(lambda x0=x0, x1=x1, z=z, t=t: (S.v.rect(x0, 0, x1, z - t, fill=(.97, .94, .85), edge=BLK, lw=.2, layer='NEN'),
                                                                  S.v.text((x0 + x1) / 2, (z - t) / 2, 'cát đầm chặt', 1.4, anc='c', va='m', col=GRY)))
        # tran tha nha chinh +3,3; tran WC +2,9
        for a0, a1, b0, b1, z, lab in [(14.2, 17.8, 5.7, 18.3, 3.3, 'Trần thả +3.300'), (8.15, 11.35, 15.4, 18.25, 2.9, 'Trần nhựa WC')]:
            n0, n1, x0, x1 = (a0, a1, b0, b1) if S.plane == 'a' else (b0, b1, a0, a1)
            if n0 <= S.c <= n1:
                S.cuts.append(lambda x0=x0, x1=x1, z=z: (S.v.rect(x0, z, x1, z + .02, fill=(1, 1, 1), edge=BLK, lw=.25, layer='NEN')))
    roofs(S)


def roofs(S):
    v = S.v; c = S.c
    # mai nha chinh (ton sau tuong chan mai; ve tuong duong san mai 4,5-4,62)
    def add(cutf, facef, n0, n1, near_d=None):
        if S.contains(n0, n1): S.cuts.append(cutf)
        else:
            d = S.dist(n0, n1)
            if d is not None: S.faces.append((d - .0005, facef))
    if S.plane == 'a':
        add(lambda: (v.rect(2.5, 4.5, 18.5, 4.62, fill=CONC, edge=BLK, lw=.4, layer='MAI'), v.hatch(2.5, 4.5, 18.5, 4.62, sp=1.4, col=GRY)),
            lambda: v.rect(2.5, 4.5, 18.5, 4.62, fill=(1, 1, 1), edge=BLK, lw=.35, layer='MAI'), 14.0, 18.0)
        add(lambda: v.poly([(2.0, 4.2), (2.5, 4.45), (2.5, 4.5), (2.0, 4.25)], fill=(.6, .3, .25), edge=BLK, lw=.3, layer='MAI'),
            lambda: v.poly([(2.0, 4.2), (2.5, 4.45), (2.5, 4.5), (2.0, 4.25)], fill=(1, 1, 1), edge=BLK, lw=.3, layer='MAI'), 13.8, 18.2)
        add(lambda: v.poly([(18.5, 2.85), (19.7, 2.62), (19.7, 2.66), (18.5, 2.89)], fill=BLK, edge=BLK, lw=.3, layer='MAI'),
            lambda: v.poly([(18.5, 2.85), (19.7, 2.62), (19.7, 2.66), (18.5, 2.89)], fill=(1, 1, 1), edge=BLK, lw=.3, layer='MAI'), 14.0, 18.0)
        # nha phu
        zr = zroof_annex(min(max(c, 7.75), 14.0)) if S.cut else 3.0
        def ann_cut():
            v.rect(7.6, zr, 18.7, zr + .03, fill=BLK, edge=BLK, lw=.3, layer='MAI')
            zc = zceil_annex(min(max(c, 7.95), 14))
            v.rect(7.85, zc, 18.45, zc + .02, fill=(1, 1, 1), edge=BLK, lw=.2, layer='MAI')
            for y in [7.7, 9.8, 11.9, 14.0, 16.1, 18.4]: v.rect(y, zr - .12, y + .06, zr, fill=(.6, .45, .3), edge=BLK, lw=.2, layer='MAI')
            v.poly([(18.7, 2.95), (19.9, 2.72), (19.9, 2.75), (18.7, 2.98)], fill=BLK, edge=BLK, lw=.3, layer='MAI')
        def ann_face():
            v.rect(7.6, 3.0, 18.7, 3.06, fill=(1, 1, 1), edge=BLK, lw=.35, layer='MAI')
            v.rect(7.7, 2.73, 18.6, 2.88, fill=(.95, .93, .9), edge=BLK, lw=.2, layer='MAI')
            v.poly([(18.7, 2.95), (19.9, 2.72), (19.9, 2.76), (18.7, 2.99)], fill=(1, 1, 1), edge=BLK, lw=.3, layer='MAI')
        add(ann_cut, ann_face, 7.75, 14.0)
    else:
        if 2.5 <= c <= 18.5 and S.cut:
            S.cuts.append(lambda: (v.rect(14.0, 4.5, 18.0, 4.62, fill=CONC, edge=BLK, lw=.4, layer='MAI'), v.hatch(14, 4.5, 18, 4.62, sp=1.4, col=GRY)))
        else:
            d = S.dist(2.5, 18.5)
            if d is not None:
                S.faces.append((d - .0005, lambda: v.rect(14.0, 4.5, 18.0, 4.62, fill=(1, 1, 1), edge=BLK, lw=.35, layer='MAI')))
                if S.look > 0: S.faces.append((max(0, 2.0 - S.c) if S.look > 0 else 0, lambda: v.rect(13.8, 4.2, 18.2, 4.45, fill=(.85, .55, .45), edge=BLK, lw=.3, layer='MAI')))
                else: S.faces.append((0, lambda: v.poly([(14, 2.62), (18, 2.62), (18, 2.85), (14, 2.85)], fill=(1, 1, 1), edge=BLK, lw=.3, layer='MAI')))
        if 7.6 <= c <= 18.7 and S.cut:
            def ac():
                v.poly([(7.75, 3.0), (14.0, 3.6), (14.0, 3.63), (7.75, 3.03)], fill=BLK, edge=BLK, lw=.3, layer='MAI')
                v.line([(7.95, 2.93), (14.0, 3.53)], .3, BLK, None, 'MAI')
                v.rect(7.95, 2.73, 8.1, 2.88, fill=(.6, .45, .3), edge=BLK, lw=.2, layer='MAI')
            S.cuts.append(ac)
        else:
            d = S.dist(7.6, 18.7)
            if d is not None:
                def af():
                    v.poly([(8.0, 2.9), (14.0, 2.9), (14.0, 3.58), (8.0, 3.02)], fill=(.92, .92, .92), edge=BLK, lw=.25, layer='MAI')
                    v.poly([(7.75, 3.0), (14.0, 3.6), (14.0, 3.65), (7.75, 3.05)], fill=(1, 1, 1), edge=BLK, lw=.35, layer='MAI')
                    if S.look < 0: v.poly([(7.75, 2.72), (14, 2.72), (14, 2.95), (7.75, 2.95)], fill=(1, 1, 1), edge=BLK, lw=.3, layer='MAI')
                S.faces.append((d - .0004, af))


def ground(S, x0, x1, road=True):
    v = S.v
    v.line([(x0, -0.1), (x1, -0.1)], .5, BLK, None, 'NEN')
    for k in range(int((x1 - x0) / .35)):
        x = x0 + k * .35
        v.line([(x, -0.1), (x + .2, -0.3)], .1, GRY)
    if road and S.plane == 'a':
        lo = min(x0, x1)
        v.rect(lo, ROAD_Z - 0.2, -0.25, ROAD_Z, fill=(.35, .35, .35), edge=BLK, lw=.3, layer='NEN')


def levels(S, x, items, side='r'):
    for z, t in items:
        S.v.level(x, z, t, 1.8, side)
