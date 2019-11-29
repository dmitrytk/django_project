class Data {
    constructor(km, a, stat, duration) {
        this.km = km;
        this.a = a * 100000;
        this.stat = stat;
        this.duration = duration;
    }
}

class Field {
    constructor(r, Q, km, a) {
        this.r = r;
        this.Q = Q;
        this.km = km;
        this.a = a * 100000;
    }
}


class Well {
    constructor(name, x, y, r) {
        this.name = name;
        this.x = x;
        this.y = y;
        this.r = r;
        this.debts = [];
        this.S = [];
        this.qAvg = 0;
        this.qMax = 0;
        this.dS = 0;
    }
}