const txtArea = document.querySelector('#txt-area');
const tableDiv = document.querySelector('#table-div');
const clear = document.querySelector('#clear');


clear.addEventListener('click', del);
txtArea.addEventListener('keyup', calculateAndShow);
txtArea.addEventListener('input', calculateAndShow);

txtArea.placeholder = 'Вставьте данные в формате:\nWELL\tX\t\t   Y\n1WZ    4564000\t789121\n2WZ    4564000\t789121';

// Calculate distance betweens to well (points)
function distance(well, x, y) {
    return ((well.x - x) ** 2 + (well.y - y) ** 2) ** 0.5;
}

// Value from text area to string 2d array
function getTextValue(textArea) {
    let value = textArea.value;
    let flat = value.split('\n');
    let arr = [];
    for (let row of flat) {
        arr.push(row.split('\t'))
    }
    return arr;
}

// Text array to well array
function textToWellArray(arr) {
    let wells = [];
    for (let row of arr) {
        let well = {
            name: row[0],
            x: toNumber(row[1]),
            y: toNumber(row[2])
        }
        wells.push(well);
    }
    wells = wells.filter(el => !Number.isNaN(el.x) && el.x !== undefined);
    return wells;
}

// Calculate well distances and store them in 2D array
function calcWellsDistances(wells) {
    let arr = [['WELL', 'X', 'Y']];
    wells.forEach(el => arr[0].push(el.name));
    for (let well of wells) {
        let row = [well.name, well.x, well.y];
        for (let other_well of wells) {
            row.push(Math.round(distance(well, other_well.x, other_well.y)))
        }
        arr.push(row)
    }
    return (arr);
}


// Result function to calculate distances and show html table
function calculateAndShow() {
    let inputArr = getTextValue(txtArea);
    let wells = textToWellArray(inputArr);
    if (wells.length > 0) {
        let resultArr = calcWellsDistances(wells);
        tableDiv.innerHTML = arrayToTable(resultArr);
        // tableDiv.scrollIntoView({ behavior: 'smooth', block: 'center' });
        scrollToElement('#table-div');
        copyToClipboard(arrayToText(resultArr, '\t'));
    }
}

// Delete table and alert
function del() {
    tableDiv.innerHTML = '';
    txtArea.value = '';
}

function showAlert() {
    if (document.body.children[1].id != 'ALRT') {
        var alertNode = document.createElement("div");
        alertNode.id = 'ALRT';
        alertNode.innerHTML = '<div class="alert alert-success alert-dismissible container" id="alrt"><button type="button" class="close" data-dismiss="alert">&times;</button>Данные скопированы в буфер обмена.</div>';
        var navBar = document.body.children[0];
        navBar.parentNode.insertBefore(alertNode, navBar.nextSibling);
    }
}