# Projecto API Server

## Objetivo: programar un API Server utilizando Django. Django es un framework escrito en Python para desarrollar aplicaciones web

## API endpoints

### api/v1/devices/

Descripción: retorna los dispositvos almacenados en la DB  
Métodos:
GET  

### api/v1/{device}/interfaces/

Descripción: agrega, elimina, modifica y retorna las interfaces de un {dispositivo} almacenaodo en la DB  

Métodos:  
GET  
POST  
&nbsp;&nbsp;Body:  
&nbsp;&nbsp;{  
&nbsp;&nbsp;&nbsp;&nbsp;"type": "Giga" o "Fast",  
&nbsp;&nbsp;&nbsp;&nbsp;"slot": 0 o 1,  
&nbsp;&nbsp;&nbsp;&nbsp;"port": 0 o 1,  
&nbsp;&nbsp;&nbsp;&nbsp;"ip_address": "X.X.X.X" o "none",  
&nbsp;&nbsp;&nbsp;&nbsp;"status": "u" o "d"  
&nbsp;&nbsp;}  

### api/v1/{device}/interfaces/{status}/

Descripción: retorna las interfaces de un {dispositivo} almecenado en la DB según su estado {Up o Down}  

Métodos:  
GET  

## Base de datos

SQLite  

## Tablas DB

Devices  
Interfaces  
Usuarios  

### Ed Scrimaglia, Año 2022
