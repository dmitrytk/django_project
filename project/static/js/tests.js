describe("distance", function () {

    it("вычисляет расстояние между точкой и скважиной", function () {
        assert.equal(distance(new Well('25', 0, 0, 1), 10, 10), 200 ** 0.5);
    });
});

describe("dateToString", function () {

    it("преобразует объект Date в строку", function () {
        assert.equal(dateToString(new Date(2019, 0, 1)), '01.01.2019');
    });
});

describe("excelDatetoDate", function () {

    it("convert excel number date to Date object", function () {
        assert(excelDatetoDate(29221).getTime() === new Date(1980, 0, 1).getTime());
        assert(excelDatetoDate(69316).getTime() === new Date(2089, 9, 10).getTime());
    });
});


describe("arange", function () {

    it("create array from range", function () {
        expect(arange(1, 5, 1)).to.eql([1, 2, 3, 4, 5]);
        expect(arange(2, 5, 2)).to.eql([2, 4, 6]);

    });
});

describe("arrayToText", function () {
    it("Convert array to string with custom separator", function () {
        assert.equal(arrayToText([1, 2, 3], '\t'), '1\t2\t3');
        assert.equal(arrayToText([[1, 2, 3], [4, 5, 6]], '-'), '1-2-3\n4-5-6\n');

    });
});




