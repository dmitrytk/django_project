// DATA
var DATA = 0;
var GRID = 0;
var CONTENT = false;

// CONTROLS
const drop = document.querySelector('#drop_zone');
const stepInput = document.querySelector('#step');
const marginInput = document.querySelector('#margin');
const fieldInput = document.querySelector('#field');

const tableBox = document.querySelector('#tableCheckBox');
const imageBox = document.querySelector('#imageCheckBox');
const gridBox = document.querySelector('#gridCheckBox');

const calculateBtn = document.querySelector('#calculate');
const clearBtn = document.querySelector('#del');

const progress = document.querySelector('#progress');
const progress_div = document.querySelector('#progress_div');

//  #region event listeners
stepInput.addEventListener('change', checkControls);
stepInput.addEventListener('keyup', checkControls);
marginInput.addEventListener('change', checkControls);
marginInput.addEventListener('keyup', checkControls);

tableBox.addEventListener('change', checkControls);
imageBox.addEventListener('change', checkControls);
gridBox.addEventListener('change', checkControls);

calculateBtn.addEventListener('click', calculate);
clearBtn.addEventListener('click', clearContent);
//  #endregion event listeners


// FUNCTIONS
//  #region drop functions
function handleFileSelect(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    var files = evt.dataTransfer.files; // FileList object.
    // files is a FileList of File objects. List some properties.

    let f = files[0];
    if (f.name.includes('xlsx')) {
        var reader = new FileReader();
        reader.readAsArrayBuffer(f);
        reader.onload = function (e) {
            var data = new Uint8Array(reader.result);
            var wb = XLSX.read(data, {type: 'array'});
            let arr = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]], {header: 1});
            DATA = loadExcelFile(arr);
            showFileContent();
            checkControls();
        }
    }
}

function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    drop.classList.add('border-primary', 'text-primary');
    evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
}

// Setup the dnd listeners.
drop.addEventListener('drop', handleFileSelect, false);
drop.addEventListener('dragover', handleDragOver, false);
drop.addEventListener('dragleave', () => {
    drop.classList.remove('border-primary', 'text-primary');
});
//  #endregion drop functions


// #region UI function
function checkControls() {
    if (CONTENT || DATA !== 0) {
        clearBtn.disabled = false;
    } else {
        clearBtn.disabled = true;
    }
    if (checkInput() && checkBoxState() && DATA !== 0) {
        calculateBtn.disabled = false;
        return true;
    } else {
        calculateBtn.disabled = true;
        return true;
    }
}

function checkInput() {
    let step = stepInput.value;
    let margin = marginInput.value;
    if (!Number.isNaN(step) && !Number.isNaN(margin) && step > 0 && margin > 0) {
        return true;
    } else {
        return false;
    }
}

function clearContent() {
    document.querySelector('#table').innerHTML = '';
    document.querySelector('#chart').innerHTML = '';
    drop.innerHTML = 'Перетащите файл excel сюда';
    drop.style.color = '#bbb';
    drop.classList.remove('border-primary', 'text-primary');
    DATA = 0;
    GRID = 0;
    CONTENT = false;
    checkControls();
}

function checkBoxState() {
    let boxes = getCheckBoxes();
    return Object.values(boxes).some(el => el === true);
}

function getCheckBoxes() {
    return {
        table: tableBox.checked,
        image: imageBox.checked,
        grid: gridBox.checked,
    }
}

function showFileContent() {
    drop.innerHTML = `Km=${DATA.km} &nbsp; a=${DATA.a}*10<sup>5</sup> &nbsp; ${DATA.wells.length} скважин`;
    drop.style.color = 'green';
}

// #endregion UI function

// #region calculate function
function calculate() {
    let boxes = getCheckBoxes();
    if (boxes.table) {
        drawTable();
        scrollToElement('#table');
    }
    if (boxes.grid || boxes.image) {
        let promise = new Promise(function (resolve, reject) {
            calculateGrid(DATA, resolve);
        });
        if (boxes.grid) {
            promise.then(
                result => {
                    writeGrid(GRID);
                },
            );
        }
        if (boxes.image) {
            promise.then(
                result => {
                    drawPlot(GRID, DATA);
                },
            );
        }
    }
}

function drawTable() {
    let tableArr = calculateSubTable(DATA);
    copyToClipboard(arrayToText(tableArr, '\t'));
    document.querySelector('.table-responsive').innerHTML = arrayToTable(tableArr);
}

function calculateGrid(data, resolve) {
    let t0 = performance.now();
    GRID = new Grid();
    let step = Number(stepInput.value);
    let margin = Number(marginInput.value);
    let field = Number(fieldInput.value);
    if (checkInput()) {
        for (let well of data.wells) {
            GRID.XX.push(well.x);
            GRID.YY.push(well.y);
        }
        let min_x = Math.floor((Math.min(...GRID.XX) - margin) / 1000) * 1000;
        let min_y = Math.floor((Math.min(...GRID.YY) - margin) / 1000) * 1000;
        let max_x = Math.ceil((Math.max(...GRID.XX) + margin) / 1000) * 1000;
        let max_y = Math.ceil((Math.max(...GRID.YY) + margin) / 1000) * 1000;


        GRID.X = arange(min_x, max_x, step);
        GRID.Y = arange(min_y, max_y, step);
        GRID.Z = []

        let points = GRID.Y.length * GRID.X.length;
        let tenPercent = Math.round(points / 10);
        let counter = 0;
        let percent = 0;
        progress_div.style.display = 'block';
        for (let i = 0; i < GRID.Y.length; i++) {
            setTimeout(() => {
                GRID.Z[i] = [];
                for (let j = 0; j < GRID.X.length; j++) {
                    let SUM = 0;
                    for (let well of data.wells) {
                        let R = distance(well, GRID.X[j], GRID.Y[i]);
                        for (let k = 0; k < data.dates.length; k++) {
                            if (k > 0) {
                                let Q = well.debts[k] - well.debts[k - 1];
                                let T = data.dates[data.dates.length - 1] - data.dates[k - 1];
                                let arg = -1 * R * R / 4 / data.a / T / 100000;
                                SUM += Q * EI(arg);
                            }
                        }
                    }
                    let temp_S = -1 / 4 / 3.14 / data.km * SUM;
                    GRID.Z[i][j] = (Math.round(temp_S * 100)) / 100 + field;
                    counter++;
                    if (counter % tenPercent === 0) {
                        progress.style.width = `${counter / tenPercent * 10}%`;
                    }
                    if (i === GRID.Y.length - 1 && j === GRID.X.length - 1) {
                        progress_div.style.display = 'none';
                        console.log("Grid generating took " + (performance.now() - t0) / 1000 + " seconds.");
                        resolve();
                    }
                }
            }, 20);
        }
    }
}

function writeGrid(grid) {
    let grd = 'DSAA\n';
    grd += grid.X.length + ' ' + grid.Y.length + ' \n';
    grd += grid.X[0] + ' ' + grid.X[grid.X.length - 1] + ' \n';
    grd += grid.Y[0] + ' ' + grid.Y[grid.Y.length - 1] + ' \n';

    let max = -Infinity;
    let min = Infinity;
    for (let i = 0; i < grid.Z.length; i++) {
        let mx = Math.max(...grid.Z[i]);
        let mn = Math.min(...grid.Z[i]);
        max = max < mx ? mx : max;
        min = min > mn ? mn : min;

    }
    grd += max + ' ' + min + ' \n';

    let counter = 0;
    for (let i = 0; i < grid.Y.length; i++) {
        for (let j = 0; j < grid.X.length; j++) {
            grd += grid.Z[i][j] + ' ';
            counter++;
            if (counter % 10 === 0) {
                grd += '\n'
            }
        }
    }
    saveToFile(grd, 'RESULT.grd');
}

function drawPlot(grid, dt) {
    let data = [{
        x: grid.X,
        y: grid.Y,
        z: grid.Z,
        type: 'contour',
        contours: {
            coloring: 'heatmap',
            showlabels: true,
            labelfont: {
                family: 'Arial',
                size: 12,
                color: 'black',
            }
        }
    }];

    let layout = {
        showlegend: true,
        annotations: []
    };
    for (let well of dt.wells) {
        layout.annotations.push({
            x: well.x,
            y: well.y,
            xref: 'x',
            yref: 'y',
            text: String(well.name),
            showarrow: false,
            arrowhead: 2,
            ax: 2000,
            ay: 1000
        })
    }
    Plotly.newPlot('chart', data, layout);
}

// #endregion calculate function
