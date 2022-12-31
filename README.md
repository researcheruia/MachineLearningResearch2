<h1 style="text-align:center;">EVALUACIÓN DEL MODELO ALGORÍTMICO DE REGRESIÓN LOGÍSTICA, EN LA PREDICCIÓN DE EFECTOS ADVERSOS DE FÁRMACOS UTILIZADOS PARA TRATAR LAS PATOLOGÍAS SUBYACENTES ASOCIADAS CON EL TRASTORNO DEL ESPECTRO AUTISTA, A PARTIR DEL INVENTARIO DE LOS GRUPOS FUNCIONALES PRESENTES EN LAS ESTRUCTURA MOLECULAR Y LA MASA MOLAR"</h1>
<br/>
<div>
  <p style="text-align:justify;">Este repositorio corresponde al repositorio final de un proyecto de investigación que trabajado en la Universidad de las Américas, por el siguiente equipo de investigación:</p>
  <dl>
  <dt>Lic. Marcus Vinicio Mora Salas</dt>
  <dd>Profesor de Química para las Escuelas de Farmacia y Medicina.</dd>
  <dt>Paola Jiménez Méndez</dt>
  <dd>Estudiante de Medicina.</dd>
  <dt>Iván Rodríguez Orozco</dt>
  <dd>Estudiante de Farmacia.</dd>
  <dt>Lic. Kristel Gómez Oviedo</dt>
  <dd>Coordinadora Académica de  Investigación y Extensión, Escuela de Farmacia.</dd>
  <dt>Lic. Marianela Soto Arias</dt>
  <dd>Coordinadora Académica de Investigación y Extensión, Escuela de Medicina.</dd>
  </dl>
</div>
<br/>
<div>
<h2 style="text-align:center;">Sobre el contenido de este repositorio.</h2>
<p style="text-align:justify;">Aunque, debido al uso de <a href="https://www.djangoproject.com/">django</a> a primera vista el proyecto pareciera el repositorio para el "backend" de un sitio web, realmente se ha decidido usar este paquete principalmente con el objetivo de tener un medio interactivo a través del cual, una vez que culmine el proyecto, se puedan presentar los resultados de manera elegante. Lo que realmente se busca con el proyecto, es probar modelos algorítmicos de "Machine Learning", buscando encontrar uno que permita predecir si cabe esperar que el activo de un fármaco nuevo produzca o no un determinado efecto adverso. Se reducirá el grupo de fármacos del modelo a aquellos utilizados para tratar patologías subyacentes del TEA.</p>
<p style="text-align:justify;">De momento lo que se ha hecho es crear un paquete llamado drugbank2, que se encarga de descargar los datos necesarios para construir los modelos. Cabe destacar que no es la pretensión, al menos de momento, que el paquete sea utilizado fuera de este proyecto, pues aún se pueden y se deben hacer muchas mejorías en este paquete. Sin embargo, la optimización del código de este paquete puede posponerse para futuros proyectos, pues de momento lo único que se buscaba era un medio para realizar la descarga masiva de los datos de los fármacos, lo cual, al momento de escribir este README, ya se consiguió. Sólo se realizarían mejoras inmediatas en caso de que haya algún error grave en los datos descargados.</p>
<p style="text-align:justify;">Lo que sigue por hacer, una vez completada la descarga, es realizar una limpieza de la base de datos y llevar a cabo un análisis exploratorio</p>
</div>
<br/>
<div>
<h2 style="text-align:center;">Justificación sobre el estilo de la documentación del código</h2>
<p style="text-align:justify;">La documentación que usualmente se escribe para un paquete de Python va a orientada a guiar a los desarrolladores sobre el uso de dicho paquete. Es por eso que existen ciertas normativas estilísticas que suelen seguirse al escribir el código. Más sobre estás convenciones de estilo pueden encontrarse en el siguiente <a href="https://peps.python.org/pep-0257/">enlace</a>.Sin embargo, en el presente caso, la documentación estará dirigida a quienes asesoran y financian este proyecto, así como otros miembros rectores y docentes de la Universidad de las Américas, muchos de los cuales, debido a que orientaron sus estudios a ramas del saber no relacionadas con las Ciencias de la Computación, carecen de la formación básica necesaria para leer código de Python, por lo cuak no se busca que lleguen a utilizar el código o implementarlo en sus proyectos, si no simplemente justificarles y explicarles para que sirve cada pieza y cómo resultan trascendentales para lograr los objetivos del proyecto. De este modo, por los fines del medio, el equipo de investigación se excusa de no seguir, en la mayoría de los casos, las convenciones establecidas en el PEP 257.</p>


