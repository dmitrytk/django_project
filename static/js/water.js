const salinityInput = document.querySelector('#salinity');
const temperatureInput = document.querySelector('#temperature');
const viscosityInput = document.querySelector('#viscosity');
const densityInput = document.querySelector('#density');

salinityInput.addEventListener('keyup', calcParameters);
temperatureInput.addEventListener('keyup', calcParameters);


function calcParameters() {
    let salinity = Number(salinityInput.value);
    let temperature = Number(temperatureInput.value);
    if (!Number.isNaN(salinity) && !Number.isNaN(temperature)) {
        if (salinity > 0 && temperature >= 4) {
            let visc = calcViscosity(salinity, temperature);
            let dens = calcDensity(salinity, temperature);
            console.log(dens);
            viscosityInput.value = visc;
            densityInput.value = dens;
            let str = visc + '\t' + dens;
            copyToClipboard(str);
        }
    }
    else {
        viscosityInput.value = '';
        densityInput.value = '';
    }

}

function calcViscosity(salin, temp) {
    let a = temp - 8.435;
    let distVisc = 100.0 / (2.1482 * (a + (8078.4 + a * a) ** 0.5) - 120.0);
    let am = 10 ** (-5) * (-2.24 * temp + 14.0 * temp ** 0.5 + 124.0);
    let viscosity = distVisc + am * salin;
    return Math.round(viscosity * 1000) / 1000;
}

function calcDensity(salin, temp) {
    let density = (1.0 - 5.9 * 10.0 ** (-6.0) * Math.pow(temp - 4.0, 1.95) + 6.5 * salin * Math.pow(10.0, -4.0)) / (1.0 - 4.2 * Math.pow(10.0, -5.0));
    return Math.round(density * 10000) / 10000;
}