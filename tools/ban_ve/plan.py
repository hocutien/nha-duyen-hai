from common import *

CUT = 1.2
WALL_FILL = {'old': (.55, .55, .55), 'old_in': (.62, .62, .62)}


def wrect(w, s0, s1):
    """hinh chu nhat (a0,b0,a1,b1) cua doan tuong s0..s1"""
    if w['ax'] == 'x': return (s0, w['t0'], s1, w['t1'])
    return (w['t0'], s0, w['t1'], s1)


def plan_walls(v, walls=WALLS, tags=True, cols=COLS, demo=False):
    sh = v.sh
    for w in walls:
        gaps = sorted([(o[0], o[1]) for o in w['ops'] if o[2] < CUT < o[3]])
        segs, cur = [], w['s0']
        for g0, g1 in gaps: segs.append((cur, g0)); cur = g1
        segs.append((cur, w['s1']))
        for s0, s1 in segs:
            if s1 - s0 < 1e-6: continue
            a0, b0, a1, b1 = wrect(w, s0, s1)
            k = w['kind']
            if k in WALL_FILL:
                v.rect(a0, b0, a1, b1, fill=WALL_FILL[k], edge=BLK, lw=.45, layer='TUONG')
            elif k == 'new':
                v.rect(a0, b0, a1, b1, fill=(1, 1, 1), edge=BLK, lw=.45, layer='TUONG_MOI'); v.hatch(a0, b0, a1, b1, sp=.9)
            elif k == 'light':
                v.rect(a0, b0, a1, b1, fill=(1, 1, 1), edge=BLK, lw=.3, layer='TUONG')
            elif k == 'demo':
                v.rect(a0, b0, a1, b1, edge=GRY, lw=.25, dash=[1.5, 1], layer='TUONG')
        for o in w['ops']: opening(v, w, o, tags)
    for a0, b0, ww, dd, z1, k in cols:
        if k == 'wood': v.rect(a0, b0, a0 + ww, b0 + dd, fill=(.55, .4, .25), edge=BLK, lw=.3, layer='TUONG')
        else: v.rect(a0, b0, a0 + ww, b0 + dd, fill=(.55, .55, .55), edge=BLK, lw=.45, layer='TUONG')


def P2(w, s, t):  # (s doc tuong, t ngang tuong) -> (a,b)
    return (s, t) if w['ax'] == 'x' else (t, s)


def opening(v, w, o, tags=True):
    s0, s1, zb, zt, typ, code, ex = o
    t0, t1 = w['t0'], w['t1']; tm = (t0 + t1) / 2
    L = lambda pts, lw=.2, dash=None, col=BLK: v.line([P2(w, *p) for p in pts], lw, col, dash, 'CUA')
    cut = zb < CUT < zt
    if not cut:
        if typ == 'vent' or zb >= CUT:
            L([(s0, t0), (s1, t0), (s1, t1), (s0, t1), (s0, t0)], .15, [1.2, .8])
        return
    L([(s0, t0), (s0, t1)], .3); L([(s1, t0), (s1, t1)], .3)
    if typ == 'win':
        for t in (t0, t1): L([(s0, t), (s1, t)], .18)
        L([(s0, tm - .015), (s1, tm - .015)], .13); L([(s0, tm + .015), (s1, tm + .015)], .13)
    elif typ in ('door', 'door2'):
        if typ == 'door':
            hinge, sw = ex[0], ex[1]
            leaves = [(s0 if hinge == 'lo' else s1, s1 - s0, 1 if hinge == 'lo' else -1)]
        else:
            sw = +1; ww = (s1 - s0) / 2
            leaves = [(s0, ww, 1), (s1, ww, -1)]
        tf = t1 if sw > 0 else t0
        for hs, wd, dirn in leaves:
            # canh cua mo vuong goc
            L([(hs, tf), (hs, tf + sw * wd)], .3)
            # cung quet
            n = 12; pts = []
            for i in range(n + 1):
                th = math.pi / 2 * i / n
                pts.append((hs + dirn * wd * math.cos(th), tf + sw * wd * math.sin(th)))
            L(pts, .13, [1, .7])
    elif typ == 'slide':
        L([(s0, tm - .02), (s0 + (s1 - s0) * .55, tm - .02)], .35); L([(s0 + (s1 - s0) * .45, tm + .02), (s1, tm + .02)], .35)
    elif typ == 'roll':
        L([(s0, tm), (s1, tm)], .2, [2, 1]); L([(s0, t0), (s1, t0)], .13); L([(s0, t1), (s1, t1)], .13)
    elif typ == 'arch':
        L([(s0, t0), (s1, t0)], .13, [1.5, 1]); L([(s0, t1), (s1, t1)], .13, [1.5, 1])
    if tags and code:
        sm = (s0 + s1) / 2
        side = -1 if w['ax'] == 'x' else -1
        off = .42
        if typ in ('door', 'door2'):
            sw = ex[1] if typ == 'door' else 1
            off_t = t0 - off if sw > 0 else t1 + off
        else:
            off_t = t1 + off if w['ax'] == 'y' and w['t0'] > 17 else t0 - off
        a, b = P2(w, sm, off_t)
        X, Y = v.P(a, b)
        v.sh.text(X, Y, code, 1.9, 'c', 'm', bold=True, col=(.1, .3, .55), layer='CUA')


def furn_plan(v, items=FURN, skip=(), col=GRY):
    sh = v.sh
    for a0, a1, b0, b1, z0, z1, name, k in items:
        if k in skip: continue
        dash = [1.2, .8] if z0 >= 1.3 else None
        if k == 'g' or k == 'g2':
            v.rect(a0, b0, a1, b1, fill=(1, 1, 1), edge=col, lw=.25, layer='NOITHAT')
            # goi o dau giuong (phia a lon)
            for bb in ((b0 + .1, (b0 + b1) / 2 - .05), ((b0 + b1) / 2 + .05, b1 - .1)):
                v.rect(a1 - .45, bb[0], a1 - .1, bb[1], edge=col, lw=.18, layer='NOITHAT')
            v.line([(a0 + .05, b0), (a0 + .6, b1)], .13, col, None, 'NOITHAT')
        elif k == 'ban':
            v.rect(a0, b0, a1, b1, fill=(1, 1, 1), edge=col, lw=.25, layer='NOITHAT')
            for (ca, cb) in [(a0 - .48, b0 + .15), (a0 - .48, b0 + .65), (a1 + .08, b0 + .15), (a1 + .08, b0 + .65)]:
                v.rect(ca, cb, ca + .4, cb + .4, edge=col, lw=.18, layer='NOITHAT')
        elif k == 'btr':  # ban tron inox + 4 ghe (toa do theo 3D)
            ca, cb, r = (a0 + a1) / 2, (b0 + b1) / 2, (a1 - a0) / 2
            v.circle(ca, cb, r, fill=(1, 1, 1), edge=col, lw=.25, layer='NOITHAT'); v.circle(ca, cb, .3, edge=col, lw=.12, dash=[.8, .6], layer='NOITHAT')
            for (da, db) in [(-r - .2, 0), (r + .2, 0), (0, -r - .2), (0, r + .2)]:
                v.rect(ca + da - .2, cb + db - .2, ca + da + .2, cb + db + .2, edge=col, lw=.18, layer='NOITHAT')
            X, Y = v.P(ca, cb); sh.text(X, Y, name, 1.4, 'c', 'm', col=(.3, .3, .3), layer='NOITHAT')
        elif k == 'don':
            v.circle((a0 + a1) / 2, (b0 + b1) / 2, (a1 - a0) / 2, fill=(1, 1, 1), edge=col, lw=.18, layer='NOITHAT')
        elif k == 'mb':
            v.rect(a0, b0, a1, b1, fill=(1, 1, 1), edge=col, lw=.25, layer='NOITHAT')
            v.rect(a0 + .08, 10.85, a1 - .1, 11.25, edge=col, lw=.18, layer='NOITHAT'); v.rect(a0 + .08, 11.27, a1 - .1, 11.65, edge=col, lw=.18, layer='NOITHAT')
            v.circle(8.37, 12.73, .09, edge=col, lw=.18, layer='NOITHAT'); v.circle(8.37, 13.1, .11, edge=col, lw=.18, layer='NOITHAT')
            v.rect(8.15, 12.55, 8.6, 13.28, edge=col, lw=.18, layer='NOITHAT')
            v.circle(8.38, 13.56, .1, edge=col, lw=.18, layer='NOITHAT')
        elif k == 'bc':
            v.rect(a0 + .05, b1 - .18, a1 - .05, b1, edge=col, lw=.2, layer='NOITHAT')
            pts = [((a0 + a1) / 2 + .19 * math.cos(t), b1 - .18 - .25 + .28 * math.sin(t)) for t in [i * math.pi / 10 for i in range(-10, 11)]]
            pts = [((a0 + a1) / 2 + .18 * math.cos(math.radians(d)), (b1 - .42) + .26 * math.sin(math.radians(d))) for d in range(0, 361, 15)]
            v.line(pts, .2, col, None, 'NOITHAT')
        elif k == 'bcw':  # bon cau quay mat ve phia a nho, ket nuoc sat tuong a1
            v.rect(a1 - .18, b0 + .05, a1, b1 - .05, edge=col, lw=.2, layer='NOITHAT')
            pts = [((a1 - .42) + .26 * math.cos(math.radians(d)), (b0 + b1) / 2 + .18 * math.sin(math.radians(d))) for d in range(0, 361, 15)]
            v.line(pts, .2, col, None, 'NOITHAT')
        elif k == 'kt':
            v.rect(a0, b0, a1, b1, edge=col, lw=.2, layer='NOITHAT'); v.line([(a0, b0), (a1, b1)], .1, col); v.line([(a0, b1), (a1, b0)], .1, col)
        elif k == 'gs':
            v.rect(a0, b0, a1, b1, fill=(1, 1, 1), edge=col, lw=.25, layer='NOITHAT'); v.circle((a0 + a1) / 2, (b0 + b1) / 2, .22, edge=col, lw=.18, layer='NOITHAT')
        elif k == 'lv':
            v.rect(a0, b0, a1, b1, fill=(1, 1, 1), edge=col, lw=.25, layer='NOITHAT')
            pts = [((a0 + a1) / 2 + .2 * math.cos(math.radians(d)), (b0 + b1) / 2 - .02 + .13 * math.sin(math.radians(d))) for d in range(0, 361, 20)]
            v.line(pts, .18, col, None, 'NOITHAT')
        elif k in ('cn', 'b1', 'b2'):
            continue
        elif k == 'ac':
            v.rect(a0, b0, a1, b1, edge=BLU, lw=.25, dash=[1.2, .8], layer='DEXUAT')
        else:
            v.rect(a0, b0, a1, b1, fill=None if dash else (1, 1, 1), edge=col, lw=.22, dash=dash, layer='NOITHAT')
            if k in ('tu', 'ta', 'ta2', 'tk', 'tl', 'tm'):
                v.line([(a0, b0), (a1, b1)], .1, col, None, 'NOITHAT')
        if k not in ('mb', 'bc', 'bcw', 'kt', 'lv', 'gs', 'ac', 'ban', 'btr', 'don', 'cn', 'b1', 'b2') and z0 < 1.3:
            X, Y = v.P((a0 + a1) / 2, (b0 + b1) / 2)
            hgt = min(1.6, 1.6)
            if (b1 - b0) > (a1 - a0) * 1.6 and (b1 - b0) * v.k > 18:
                sh.text(X, Y, name, hgt, 'c', 'm', rot=90, col=(.3, .3, .3), layer='NOITHAT')
            else:
                sh.text(X, Y, name, hgt, 'c', 'm', col=(.3, .3, .3), layer='NOITHAT')


def steps_plan(v):
    # dot 1: chieu nghi 0,9x1,6 (+0,5) truoc cua lua D9 + 2 bac cao 170 rong 300; tay vin 2 ben
    # 21/11 ra soat: chieu nghi 0,9x0,9 (cua lua khong can cho quet), 2 bac xuong ve phia bep -> trong mat truoc may giat
    v.rect(10.05, 16.7, 10.95, 17.6, fill=(1, 1, 1), edge=BLK, lw=.3, layer='NOITHAT')
    v.rect(10.05, 16.4, 10.95, 16.7, fill=(1, 1, 1), edge=BLK, lw=.3, layer='NOITHAT'); v.rect(10.05, 16.1, 10.95, 16.4, fill=(1, 1, 1), edge=BLK, lw=.3, layer='NOITHAT')
    v.line([(10.5, 16.15), (10.5, 17.2)], .2, BLK); v.line([(10.4, 17.05), (10.5, 17.2), (10.6, 17.05)], .2, BLK); v.text(10.5, 15.85, 'LÊN', 1.4, anc='c', va='m')
    v.line([(10.99, 16.1), (10.99, 16.7), (10.99, 17.6)], .35, BLU, None, 'DEXUAT')


def future_wc2(v):
    a0, a1, b0, b1 = FUTURE_WC2
    v.rect(a0, b0, a1, b1, edge=BLU, lw=.3, dash=[2, 1], layer='DEXUAT'); v.text((a0 + a1) / 2, (b0 + b1) / 2 + .1, 'WC 2 – đợt 2', 1.5, anc='c', col=BLU)
    v.text((a0 + a1) / 2, (b0 + b1) / 2 - .25, '(chừa chỗ)', 1.3, anc='c', col=BLU)


def grid(v, a_lines, b_lines, a_rng, b_rng, r=3.2):
    sh = v.sh
    for name, a in a_lines:
        p0 = v.P(a, b_rng[0]); p1 = v.P(a, b_rng[1])
        sh.line([p0, p1], .13, (.4, .4, .4), [6, 1.2, 1, 1.2], 'TRUC')
        for P in (p0,):
            sh.circle(P[0], P[1] - r, r, fill=(1, 1, 1), edge=BLK, lw=.25, layer='TRUC'); sh.text(P[0], P[1] - r, name, 2.6, 'c', 'm', layer='TRUC')
    for name, b in b_lines:
        p0 = v.P(a_rng[0], b); p1 = v.P(a_rng[1], b)
        sh.line([p0, p1], .13, (.4, .4, .4), [6, 1.2, 1, 1.2], 'TRUC')
        sh.circle(p0[0] - r, p0[1], r, fill=(1, 1, 1), edge=BLK, lw=.25, layer='TRUC'); sh.text(p0[0] - r, p0[1], name, 2.6, 'c', 'm', layer='TRUC')


A_GRID = [('1', 8.0), ('2', 14.1), ('3', 17.9)]
B_GRID = [('A', 2.5), ('B', 5.6), ('C', 7.8), ('D', 10.05), ('E', 14.15), ('F', 15.33), ('G', 18.4)]


def section_mark(v, name, p0, p1, look):
    """ky hieu mat cat tren mat bang: duong cat + mui ten huong nhin. look: (da,db) huong nhin"""
    sh = v.sh
    for p in (p0, p1):
        X, Y = v.P(*p)
        dx, dy = look
        sh.line([(X - 0 * dx, Y), (X + dx * 5, Y + dy * 5)], .5, BLK, None, 'TRUC')
        sh.poly([(X + dx * 6.5, Y + dy * 6.5), (X + dx * 4 + dy * 1.4, Y + dy * 4 + dx * 1.4), (X + dx * 4 - dy * 1.4, Y + dy * 4 - dx * 1.4)], fill=BLK, edge=BLK, lw=.2, layer='TRUC')
        sh.text(X + dx * 3 - (3 if dx == 0 else 0) + (0), Y + dy * 3 + (2.5 if dy == 0 else 0), name, 3.2, 'c', 'm', bold=True, layer='TRUC')
    A = v.P(*p0); B = v.P(*p1)
    sh.line([A, B], .25, BLK, [8, 1.5, 1.5, 1.5], 'TRUC')
