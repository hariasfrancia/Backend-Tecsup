// yarn add express
// formas de importar js puro
const express = require("express");

class Server{
    constructor(){
        this.app = express();
        //process.env => mira en las variables de entorno de la maquina
        this.puerto = process.env.PORT || 8000;
    }
    iniciarServidor(){
        // el metodo listen sirve para levnatar un servidor en express
        this.app.listen(this.puerto, ()=>{
            console.log(`Servidor corriendo exitosamente: 127.0.0.1: ${this.puerto}`);
        });
    }
}

module.exports = {
    Server,
};