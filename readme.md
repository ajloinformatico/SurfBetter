# SURF-BETTER
Aplicación Web para mi proyecto final de **CFGS DESARROLLO DE APLICACIONES WEB**. Es una aplicación de **SURF** destinada a los/as surferos/as y surfistas de la bahía de cádiz que no tienen una buena herramienta donde consultar sus playas y conectar con otros usuarios/as.

## Developed with

Api Rest codificada con **React** y **Flask** en el cliente y servidor respectivamente.

### Tools and technologies: 🛠

* ***[Python](https://www.python.org/)*** - Back language.
* ***[Flask](https://flask.palletsprojects.com/en/2.0.x/)*** - Python framework.
* ***[Flask Praetorian](https://flask-praetorian.readthedocs.io/en/latest/index.html)*** -  JWT Python Module.
* ***[SQLite](https://www.sqlite.org/)*** - Database.
* ***[React](https://es.reactjs.org/)*** - JavaScript front Framework.
* ***[SASS](https://sass-lang.com/)*** - CSS3 CSS preprocessor.

### Ide: 🚀

* ***Visual Studio:***
  * Fase inicial de desarrollo y fixes del final del desarrollo
* ***WebStorm :***
  * Desarrollo del cliente en las fases más complejas del desarrollo.
* ***Pycharm:***
  * Desarrollo de la Api en flask durante la modularización .

### Structure: 🧱

* ***API:***
  
  En el directorio **_'/api'_** se encuentran los archivos de la api. Esta se divide en **seeders**, **models** **modules**, **servicies**, **extensions**, **run**. La documentación es el único recurso que se incluye como **template**. Este se ubica en http://localhost:5000/docs

  * **Extensions**

    Incluyen las dependencisa que se van a utilizar en el resto de la aplicaciòn: **db** (sqlAlchemy) **guard** (praetorian)).
    
  * **Models** 
    
    Incluye todos las entidades de la aplicación.

  * **Seeders**
  
    Seeders de la aplicación. Estos se inyectan de manera autonmática si no existiesen datos previos.

  * **Modules**

    Módulos BluePrint con todas las rutas, estos módulos se dividen por funcionalidad.

  * **Services**
  
    Servicios de subida de imágenes y correo electrónico.

  * **Run**
    
    Incluye **_main.py_** y **_wsgy.py_** el primero de ellos hace de punto de unión de toda la API y como **run** en el modo desarrollo. El segundo instancia **_app()_** y se utiliza junto con **_Gunicorn_** para arrancar la aplicación

* ***Front:***
    
    El código a compilar se encuentra en ***'/front/src'*** Este incluye **_App.jsx_** Unión de los componentes y rutas. **_Utils.js_** con métodos comunes a varios módulos de la aplicación. 

    **Componentes**

    Los comentes se ubican en **/front/components**.
    
    A quí se ubican todos los componentes de la aplicación divididos por paquetes.
    
  * **Componentes específicos**
    
    Dada la función específica dentro de la aplicación estos no se han empaquetado. Lo conforman: 
    <br/>**Contact.jsx** ➡️ (Información de contacto con la empresa, enlace a web personal, formulario de envío de correo elecrtónico).
    <br/>**Footer.jsx** ➡️ Acceso a la información legal, contacto, y rutas de la aplicación.
    <br/>**HeaderMenu.jsx** ➡️ Menú común de la aplicación. Junto con **_App.jsx_** conforman las rutas de la aplicación.
    <br/>**LegalNotices.jsx** ➡️ Información legal.
    
  * **Auth**
    
    Componente para gestionar la autenticación por JWT. Junto con Praetorian en la Api. Conforman la seguridad de la aplicación. El token se genera de manera automática en cada inico de sesión. Este queda asociadop a cada usuariario durante su vida en la aplicación, es necesario para cargar cualquier ruta fuera de login y para hacer cualquier petición de datos personales a la api.
  * **beaches**
  
    Empaqueta los componentes encargados de gestionar la visualización de las playas y su contenido: **Beaches.jsx**, **BeacheHost.jsx**, **BeachCardjsx**, **BeachInfo.jsx**, **StarComponent**.

  * **loginsign**
  
    Empaqueta los componentes nencesarios para gestionar el login y el registro de usuarios en la aplicación: **LoginRegister.jsx**, **HeaderLoginRegister**, **LoginModal.jsx**, ***SignInModal.jsx**. 

  * **map**
    
    Componentes para mostrar el mapa de playas: **MapHost.jsx**, **Map.jsx**.

  * **Profile**

    Contiene los componentes necesarios para gestionar el perfil de los usuarios de SurfBetter: **Profile.jsx**, **OptionsModal.jsx**, **PasswordModal.jsx**, **UserInfoUpdateModal.jsx**

  * **Widgets**
  
    Widgets que se isntancian en App comunes para el resto de vistas.

---

## What can you do with it 😄

En primera tendrás una vista de lo que te puede **ofrecer la aplicación** junto a un slider. En esta vista encontrarás dos botones en el header para **Iniciar sesión o registrarte**.

Una vez iniciado sesión tendrás una vista de la **información personal*** del usuario de SurfBetter y de las playas favoritas y comentadas. Desde las playas el usuario puede comentar o acceder a la información de detalle de las playas. Desde aquí el usuario puede acceder a la vista **beaches**.

Desde **Beaches** el usuario tiene una vista de todas las playas de la bahía de cadiz. Tiene una barra de búsqueda donde filtrar por nombre. Puede consultar directamente en la tarjeta la información de la playa así como sus comentarios desde el detalle. Si lo desease podría guardar la playa en su perfil dandole a like o comentando en una de ellas. Además de esta vista puede acceder a **map**.

En la vista **Map** tiene un fragmento de google Maps donde puede navegar entre las playas, viendo la media de cada una y pulsar sobre una de ellas para acceder al detalle. Gracias a la api de google maps puede usar **street view** y ver como si estuviese allí la playa.

En la vista de **Contact** puede acceder a la web de **infolojo** ver los desarrolladores de la aplicación. Acceder al github de infolojo o a los enlaces de interés de los distintos desarrolladores. Además contiene un footer personalizado desde el cual puede enviar un correo electrónico a los desarrolladores, para informar de incidencias o simplemente para comunicarse con ellos-

La aplicación dispone de dos temas **Modos light & dark** y porsupuesto es totalmente responsiva

---

## Doplyment and Install 🚀

_Clona el repositorio o descarga su .zip_.

Se da la opción de dos modos **Desarrollo & Deploy** mediante **React y Flask** en el primer caso y **Docker**

### Desarrollo 🔧

#### Prerequisitos 📦
* node
* python

#### Preparación
* **Preparación de la Api**
  
  Se requiere de la instalación de un entorno virtual para python y la instalación de _api/apirequirements_.txt
  ```
  cd /api
  python3 -m venv env
  source /env/bin/activate
  python3 apirequirements.txt
  ```

* **Preparación de React**
  
  React viene preparado para arrancar con sus comandos tanto el cliente como el servidor. Por lo tanto una vez listo este paso no habrá que volver a **/api**. Se requiere instalar las dependencias que se utilizan en el cliente
  ```
  cd ../front
  npm install
  /**
  Hay veces que este comando falla al instalar 
  la dependencia de seguridad en ese caso
  /*
  npm install --save react-token-auth
  ```
#### Ejecución ⚙️
  
  Desde **/front**
  Se arranca la **api** introducciendo
  ```
  npm run start-api
  ```
  Se arranca el **cliente** introduciendo
  ```
  npm run start
  ```
  Accede desde http://localhost:3000

  La api se encuentra en http://localhost:5000

### Deploy docker 📋
#### Prerequisitos 📦
* docker

#### Ejecución ⚙️
La aplicación monta dos contenedores. El primero de ellos con **Node** y **Nginx** y el segundo con **Python** y **Gunicorn**

Estos se montan y se ejecuntan desde la **raiz** introudciendo
```
docker-compose build
docker-compose up
```
Accede desde http://localhost:80

La api se encuentra en http://localhost:5000
## New Versions Control 📌
La aplicación se encuentra actualmente en su versión 1.0
Se incorporaran nuevas features en futuras versiones
## Contributing 🖇️
Puedes [Fork my work](https://github.com/ajloinformatico) y usarlo de base o lanzar un merge request.
## Web Site 🌐
Visita mi web personal y conoce un poco más sobre mi.
[infolojo.es](https://www.infolojo.es)
## Author ✒️
_Esta aplicación web ha sido desarollada por:_

* **Antonio José Lojo Ojeda** [ajloinformatico](https://github.com/ajloinformatico).

## License 📄
_I'm open source (CC BY-NC) [INFOLOJO](https://www.infolojo.es)._

Use my work if you want, imporove it but mention and ask me before deploy.
## Thanks 🎁

* Comment with your friends about my work 📢.
* Enjouy it 🍺  ☕ . 
* mention this job in your social networks🤓.
* etc.
---
⌨️ with ❤️ by [INFOLOJO](https://www.infolojo.es) 🧑‍💻.


