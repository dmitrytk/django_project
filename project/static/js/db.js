const alertArea = document.querySelector('#alert-area');
const inputArea = document.querySelector('#input-area');
const loadBtn = document.querySelector('#load-btn');
const clearBtn = document.querySelector('#clear-btn');


const list = [
    'well',
    'field',
    'location',
    'owner',
    'type',
    'alt',
    'md',
    'x',
    'y',
];


const showAlert = function (text, type) {
    alertArea.innerHTML = `
        <div id="load-alert" class="alert alert-${type} alert-dismissible">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            ${text}
        </div>
    `;
    $("#load-alert").delay(4000).slideUp(500, function () {
        $(this).alert('close');
    });
}


const getInputData = function (value) {
    if (value.includes('\n') && value.includes('\t')) {
        let val = value.replace(/\r/g, '');
        let rows = val.split('\n');
        let header = rows[0].split('\t');
        let data = [];
        for (let row of rows) {
            if (row.length > 2 && row.includes('\t')) {
                data.push(row.split('\t'))
            }
        }
        return {
            header: header,
            data: data
        }
    } else {
        return null;
    }
};

const checkData = function (data) {
    const headerLength = data.header.length;
    const equalLength = data.data.every(el => el.length === headerLength);
    const containAttr = data.header.every(el => list.includes(el));
    console.log(data.header);
    console.log(equalLength);
    console.log(containAttr);
    if (equalLength && containAttr) {
        showAlert('Data is valid', 'success');
        return true;
    } else {
        showAlert('Wrong columns names or unequal row length', 'danger');
        return false;
    }
};

inputArea.addEventListener('input', () => {
    let data = getInputData(inputArea.value);
    if (checkData(data)) {
        loadBtn.disabled = false;
        inputArea.rows = (data.data.length > 20) ? 20 : data.data.length;
    }

});

clearBtn.addEventListener('click', () => {
    inputArea.value = '';
    loadBtn.disabled = true;
    inputArea.rows = 10;
});
