const first = document.querySelector('#first');
const last = document.querySelector('#last');
const input = document.querySelector('#inputText');
const black = document.querySelector('#black');
const color = document.querySelector('#color');
const clear = document.querySelector('#clear');


// Create array of color pages from input
function findPages(str) {
    str = str.split('\n');
    let result = [];
    for (let c of str) {
        if (c.includes(',')) {
            let row = c.split(',');
            for (let cell of row) {
                result.push(Number(cell));
            }
        }
        else if (c.includes('-')) {
            let fromTo = c.split('-');
            let arr = arange(Number(fromTo[0]), Number(fromTo[1]), 1);
            arr.forEach(e => result.push(e));

        }
        else result.push(Number(c));
    }
    return result;
}

// Print result page ranges
function calcPages() {
    let from = Number(first.value);
    let to = Number(last.value);
    let str = input.value;
    if (!Number.isNaN(from) && !Number.isNaN(to) && to > from && str.length > 0) {
        let allPages = arange(from, to, 1);
        let clr = findPages(str);
        let blck = allPages.filter(e => !clr.includes(e));
        black.value = blck.join(',');
        color.value = clr.join(',');
    }
}

first.addEventListener('keyup', calcPages);
last.addEventListener('keyup', calcPages);
input.addEventListener('keyup', calcPages);
clear.addEventListener('click', e => input.value = '')
document.querySelector('#copyBlack').addEventListener('click', e => copyToClipboard(black.value));
document.querySelector('#copyColor').addEventListener('click', e => copyToClipboard(color.value));

