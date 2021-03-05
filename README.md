# tires-optimizer-baseline
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Setup del proyecto 
Este trabajo se desarrollará en dos ramas
-  main: rama de cara al cliente 
-  develop: rama de desarrollo en las cuales se comenzarán los desarrollos

Por lo tanto, todas las personas que contribuyan en el desarrollo del repo, deben hacer chechout a la rama de develop y trabjar única y exclusivamente en esta rama.
La rama main, no se tocará y solo se harán las transferencias vía Pull Request (PR), en el cual los owners del repo deberán aprobar. La idea es a corto plazo tener una instancia de CI/CD a través de github actions para hacer el deploy de los stacks, en donde el proceso de deploy esta totalmente automatizado y separado por ambientes de desarrollo.

Pasos a seguir para hacer ambiente de trabajo del producto

```sh
$ echo Es estrictamente necesario usar python 3.7 para hacer los deploys de stacks
git clone git@github.com:alaya-digital-solutions/tires-optimizer
$ cd tires-optimizer
$ echo instalar los requirements
$ pip install -r requirements.txt
```

## Introducción
Este será un software mantenimiento predictivo de neumaticos mineros, los objetivos son:
 - Alargar la vida útil de los neumáticos de un 4 a un 10 %
 - Mejora en planificación de mantenimiento 
 - Mejora en continuidad operacional asegurando control en condiciones límite
 - Aporte en excelencia operacional contribuyendo con seguimiento de conducción de operadores

## Modulos
 - Modulo Base: Tabla de mantenimiento de neumáticos, ordenados por vida remanente del activo y por caex
 - Modulo Alertas: Alertas personalizadas vía e-mail, con recomendaciones de futuras entradas a mantenimiento de los neumáticos. Alertas a tiempo real (baja de presión, aumento
   excesivo de temperatura, desbalance de carga, recorrido del neumático mayor al permitido u otra que pueda impactar el rendimiento o seguridad de los activos mina    
   involucrados)
 - Modulo Seguimiento de KPI’s: Curvas de evolución de uso del neumático en función de la actividad minera (distancia recorrida, inclinación de caminos, desgaste por fricción, tonelaje de mineral transportado, etc)
 - Modulo Control Operacional de Desgaste: Cuantificación del desgaste en neumáticos por conducción de operadores, seguimiento de mejora operacional (ejemplo: control de
   frenado)
   
 ## ¿Qué se necesita para trabajar? 
 
 -  Consola unix o emulador de consola unix, para windows (Ej: Cmder instalando el path de anaconda)
 
## ¿Cómo configuro el espacio de trabajo? 

 ```sh
Una vez instalado aws-cli y aws-sam en un ambiente (digase conda), se debe configurar la terminal para que pueda ejectutar comandos de aws-cli (command line interface)
--> conda activate del ambiente
$ conda activate ambiente 
--> configurar credenciales
$ aws configure --profile tires-opt-{minera en la que se trabaja}
--> poner las crendeciales que se te fueron enviadas por mail, si no pedir al administrador de la cuenta que te entregue credenciales programaticas
```

## ¿Cómo levantar un stack de CloudFormation AWS (Infrastructura como código)? 

```sh
Hacer el template.yaml y samconfig.toml del stack, ver ejemplos en src/cleaning-process/template.yaml y src/cleaning-process/samconfig.toml
--> Contruye la base para levantar la arquitectura
$ sam build --profile tiresopt-anglo 
--> Saca un estado de la arquitectura, foto que será guardada y sale en el archivo packaged.yaml, de lo que será levantado
$ sam package --template-file template.yaml --output-template-file packaged.yaml --s3-bucket tiresopt-deploy-anglo --profile tiresopt-anglo
--> Levanta la infraestrucura en la cuenta que definiste
$ sam deploy --profile tiresopt-anglo
--> Todo esto se puede evitar ejecutando el deploy.sh en una consola unix
$ bash deploy.sh
```

 
 
