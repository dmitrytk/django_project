const drop_zone = document.querySelector('#drop_zone');

var FILES = [];

// Well inclinometry class
class WellInc {
    constructor(name) {
        this.name = name;
        this.md = [];
        this.inc = [];
        this.azim = [];
    }
}

function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
}

function handleFileSelect(evt) {
    evt.stopPropagation();
    evt.preventDefault();

    FILES = [];

    var files = evt.dataTransfer.files;
    if (files.length > 0) {
        for (let i = 0; i < files.length; i++) {
            let file = files[i];
            loadFile(file, FILES);
        }
    }
    calculate();
}

// process loaded files
function calculate() {
    setTimeout(() => {
        for (let file of FILES) {
            if (file.name === 'incline.xlsx') {
                calcInclinometry(file.content);
            }
        }
    },
        300)
}

// load file and store it content in array
function loadFile(file, array) {
    if (file.name.includes('xlsx')) {
        let reader = new FileReader();
        reader.readAsArrayBuffer(file);
        reader.onload = function (e) {
            let data = new Uint8Array(reader.result);
            let wb = XLSX.read(data, { type: 'array' });
            let arr = XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]], { header: 1 });
            let obj = { name: file.name, content: arr };
            array.push(obj);
        }
    }
    else {
        let reader = new FileReader();
        reader.readAsText(file);
        reader.onload = function (event) {
            let obj = { name: file.name, content: event.target.result };
            array.push(obj);
        };
    }
}

// Setup the dnd listeners.
drop_zone.addEventListener('dragover', handleDragOver, false);
drop_zone.addEventListener('drop', handleFileSelect, false);


// Calculate inclinometry and store it in LAS files
function calcInclinometry(array) {
    let wells = [];
    wells.push(new WellInc(array[1][0]));
    wells[wells.length - 1].md.push(array[1][1]);
    wells[wells.length - 1].inc.push(array[1][2]);
    wells[wells.length - 1].azim.push(array[1][3]);

    for (let row of array.slice(2)) {
        if (row[0] === '' || row[0] === undefined) break;
        if (wells[wells.length - 1].name === row[0]) {
            wells[wells.length - 1].md.push(row[1]);
            wells[wells.length - 1].inc.push(row[2]);
            wells[wells.length - 1].azim.push(row[3]);
        }
        else {
            wells.push(new WellInc(row[0]));
            wells[wells.length - 1].md.push(row[1]);
            wells[wells.length - 1].inc.push(row[2]);
            wells[wells.length - 1].azim.push(row[3]);
        }
    }
    console.log(wells);
    for (let well of wells) {
        let txt = 'MD\tINC\tAZIM\n';
        for (let i = 0; i < well.md.length; i++) {
            txt += well.md[i] + '\t' + well.inc[i] + '\t' + well.azim[i] + '\n';
        }
        txt = txt.replace(/undefined/g, '');
        saveToFile(txt, well.name + '.inc');
    }
}
