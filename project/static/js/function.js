// #region classes
class Data {
    constructor() {
        this.km = 0;
        this.a = 0;
        this.years = [];
        this.dates = [];
        this.wells = [];
        this.dist = [];
    }
}

class Grid {
    constructor() {
        this.XX = [];
        this.YY = [];
        this.X = 0;
        this.Y = 0;
        this.Z = 0;
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
    }
}

// #endregion classes


function dateToString(date) {
    var yyyy = date.getFullYear();
    var mm = date.getMonth() < 9 ? "0" + (date.getMonth() + 1) : (date.getMonth() + 1); // getMonth() is zero-based
    var dd = date.getDate() < 10 ? "0" + date.getDate() : date.getDate();
    return dd + "." + mm + '.' + yyyy;
}

function excelDatetoDate(day) {
    let startDate = new Date(1900, 0, 1);
    startDate.setDate(startDate.getDate() + day - 2);
    return startDate;
}

function arange(start, stop, step) {
    let step_count = Math.ceil((stop - start) / step);
    let counter = start;
    let result = new Array(step_count + 1);
    for (let i = 0; i < result.length; i++) {
        result[i] = counter;
        counter += step;
    }
    return result;
}

function distance(well, x, y) {
    return ((well.x - x) ** 2 + (well.y - y) ** 2) ** 0.5;
}

function calcDistances(wells) {
    let array = [];
    for (let well of wells) {
        let row = [];
        for (let other_well of wells) {
            if (well === other_well) {
                row.push(well.r)
            } else {
                row.push(distance(well, other_well.x, other_well.y))
            }
        }
        array.push(row);
    }
    return array;
}

// delete undefined from array
function deleteUndefined(array) {
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array[i].length; j++) {
            if (array[i][j] === undefined) array[i][j] = '';
        }
    }
}

// Create HTML table string from 2d Array
function arrayToTable(arr) {
    let table = '<table class="table table-sm" id="tbl"><thead class="thead-dark"><tr>'
    for (let el of arr[0]) {
        table += `<th>${el}</th>`
    }
    table += '</tr></thead><tbody>';
    for (let i = 1; i < arr.length; i++) {
        table += '<tr>';
        for (let j = 0; j < arr[i].length; j++) {
            table += `<td contenteditable='true'>${arr[i][j]}</td>`;
        }
        table += '</tr>';
    }
    table += '</tbody></table>';
    return table;
}

// copy string to clipboard
function copyToClipboard(text) {
    navigator.clipboard.writeText(text).then(function () {
    }, function (err) {
        console.error('Async: Could not copy text: ', err);
    });
}

// save string to file
function saveToFile(content, fileName) {
    let blob = new Blob([content],
        { type: "text/plain;charset=utf-8" });
    saveAs(blob, fileName);
}

// Load data from 2D array to Data variable
function loadExcelFile(array) {
    let data = new Data();
    data.km = toNumber(array[1][0]);
    data.a = toNumber(array[1][1]);

    let startDate = array[4][4];

    let lastCell = 0;
    console.log(array[4]);
    for (let i = 0; i < array[4].length; i++) {
        let element = array[4][i];
        if (element === '' || element === undefined) {
            lastCell = i - 1;
            break;
        } else lastCell = array[4].length - 1;
    }
    console.log(lastCell);


    for (let cell of array[4].slice(4, lastCell + 1)) {
        data.dates.push(cell - startDate);
        data.years.push(excelDatetoDate(cell));
    }

    for (let row of array.slice(5)) {
        if (row[0] === "" || row[0] === undefined) {
            break;
        } else {
            let well = new Well(String(row[0]), toNumber(row[1]), toNumber(row[2]), toNumber(row[3]));
            for (let cell of row.slice(4, lastCell + 1)) {
                well.debts.push(toNumber(cell));
            }
            well.debts[0] = 0;
            data.wells.push(well);
        }
    }
    data.dist = calcDistances(data.wells);
    return data;
}

// Calculate Sub table => 2d array
function calculateSubTable(data) {
    let arr = [['WELL', 'X', 'Y', 'R']];
    for (let year of data.years) {
        arr[0].push(dateToString(year))
    }
    for (let i = 0; i < data.dates.length; i++) {
        let date = data.dates[i];
        for (let j = 0; j < data.wells.length; j++) {
            let well = data.wells[j];
            let SUM = 0;
            for (let k = 1; k < i + 1; k++) {
                for (let l = 0; l < data.wells.length; l++) {
                    let otherWell = data.wells[l];
                    let R = data.dist[j][l];
                    let Q = otherWell.debts[k] - otherWell.debts[k - 1];
                    let T = data.dates[i] - data.dates[k - 1];
                    let arg = -1 * R * R / 4 / data.a / T / 100000;
                    SUM += Q * EI(arg);
                }
            }
            well.S.push(Math.round((-1 / 4 / 3.14 / data.km * SUM) * 100) / 100)
        }
    }
    for (let well of data.wells) {
        let row = [well.name, well.x, well.y, well.r];
        for (let s of well.S) {
            row.push(s);
        }
        arr.push(row);
    }
    return arr;
}

// Convert array to string with custom separator
function arrayToText(array, separator) {
    let result = '';
    if (array[0][0]) {
        for (let row of array) {
            result += row.join(separator) + '\n';
        }
    } else result = array.join(separator);
    return result;
}

const toNumber = el => (typeof el === 'string') ? Number(el.replace(',', '.').replace(/ /g, '')) : Number(el);

// function toNumber(e) {
//     let result = (typeof e === 'string') ? Number(e.replace(',', '.').replace(/ /g, '')) : Number(e);
//     return result;
// }

function scrollToElement(selector) {
    // $('html, body').animate({
    //     scrollTop: $(selector).offset().top
    // }, 700);
}