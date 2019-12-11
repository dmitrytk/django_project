// DATA
var DATA = 0;

// CONTROLS
const drop = document.querySelector('#drop_zone');
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
            var wb = XLSX.read(data, { type: 'array' });
            var workBook = {
                data: deleteBlankRows(XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[0]], { header: 1 })),
                wellAvg: deleteBlankRows(XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[1]], { header: 1 })),
                wellMax: deleteBlankRows(XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[2]], { header: 1 })),
                fields: deleteBlankRows(XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[3]], { header: 1 })),
                imperfection: deleteBlankRows(XLSX.utils.sheet_to_json(wb.Sheets[wb.SheetNames[4]], { header: 1 }))
            };
            console.log(workBook);
            // DATA = loadExcelFile(arr);
            // showFileContent();
            // checkControls();
        }
    }
}

function handleDragOver(evt) {
    evt.stopPropagation();
    evt.preventDefault();
    evt.dataTransfer.dropEffect = 'copy'; // Explicitly show this is a copy.
}

// Setup the dnd listeners.
drop.addEventListener('dragover', handleDragOver, false);
drop.addEventListener('drop', handleFileSelect, false);
//  #endregion drop functions



function deleteBlankRows(arr) {
    let result = []
    for (let row of arr) {
        if (row.length !== 0) result.push(row);
    }
    return result;
}