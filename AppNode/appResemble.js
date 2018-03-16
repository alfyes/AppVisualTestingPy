const compareImages = require('resemblejs/compareImages');
const fs = require("mz/fs");

async function getDiff(imgIni, imgFinal, resultado){
    const options = {
        output: {
            errorColor: {
                red: 255,
                green: 0,
                blue: 255
            },
            errorType: 'movement',
            transparency: 1,
            largeImageThreshold: 1200,
            useCrossOrigin: false,
            outputDiff: true
        },
        scaleToSameSize: true,
        ignore: ['less'],
    };
    const data = await compareImages(
        await fs.readFile(imgIni),
        await fs.readFile(imgFinal),
        options
    );

    console.log(data);

    await fs.writeFile(resultado, data.getBuffer());
}

getDiff('./AppNode/screenshots/CrearExistenteInicio.png',
        './AppNode/screenshots/CrearExistenteFin.png',
        './AppNode/salidas/CrearExistenteRS.png');

getDiff('./AppNode/screenshots/FiltroMateriasInicio.png',
        './AppNode/screenshots/FiltroMateriasFin.png',
        './AppNode/salidas/FiltroMateriasRS.png');

getDiff('./AppNode/screenshots/LoginOkInicio.png',
        './AppNode/screenshots/LoginOkFin.png',
        './AppNode/salidas/LoginOkRS.png');
