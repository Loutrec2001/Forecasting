# Forecasting
Prueba Técnica Forecasting

El archivo contiene las bases de datos:

 * dataset_demand_acumulate.csv  Este archivo contiene la información de la demanda entre el 2017-01 hasta el 2022-04 siendo (año-mes).

 * dataset_alpha_betha.csv Este archivo contiene la información de todas las variables involucradas para realizar la clasificación de si un registro es Alpha o Betha, este cuenta con más de 7000 registros. * to_predict.csv  Cuenta con 3 registros los cuales ya tienen toda la información completa, excepto la demanda y la clase. Este archivo esta completado con ayuda del modelo de clasificación Gradient Boosting.

 * Para con sultar la Api para probar el modelo de machine learning (Clasificación, puede ingresar a http://127.0.0.1:8000/docs#/default/predict_predict__post)

 ![FastApi](/Screen%20Shot%202024-07-26%20at%208.23.17%20PM.png)
 

 * El archivo  [Serie de Tiempo](/Serie%20de%20Tiempo.ipynb) contiene la predicción de la demanda a través del modelo ARIMA. 

 * El archivo  [Clasifición](/Clasificaci%C3%B3n.ipynb) contiene el modelo de clasificación Gradient Boosting con sus respectivas métricas.

 * El archivo [teoría_](/teoria_.pdf) Teoría posee las respuestas a tres preguntas teóricas aplicando el conocimiento sobre ML. Estas preguntas son:

 1. En la empresa GA, en el área de compras necesitan CLASIFICAR y organizar los correos que llegan a la bandeja de entrada entre 4 tipos de correos (Compras cementos, Compras energía, Compras concretos y correos generales o de otra índole). Esta tarea se le encomienda a usted, como es el Gestor SR en temas de analítica e IA puede solicitar al área interesada los recursos humanos que necesite para llevar a cabo este proyecto, también puede solicitar en tecnología todo lo que necesite, además tiene las bandejas de entrada de correos históricos de los analistas que reciben estas solicitudes con aproximadamente: 5500 correos de compras cementos, 2700 correos de compras de energía, 1100 correos de compras concretos y 12876 correos generales o de otra índole.

 2. Seis meses después de haber desplegado un modelo de regresión en producción, los usuarios se dan cuenta que las predicciones que este está dando no son tan acertadas, se le encarga a usted como Gestor SR en temas de IA que revise que puede estar sucediendo.
 * ¿Cree que el modelo esté sufriendo Drift?
 * ¿Cómo puede validarlo?
 * ¿De ser así, que haría usted para corregir esto?

 3. Su equipo de trabajo está trabajando en un chatbot con generación de texto utilizando el modelo GPT-3.5, según cómo funciona este modelo, ¿cómo haría usted para hacer que las respuestas del chatbot estén siempre relacionadas a conseguir cierta información particular del usuario y no empiece a generar texto aleatorio sobre cualquier tema?
 
