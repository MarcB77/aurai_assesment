# DS Project.md

<style>H2{color:lightseagreen;}</style>
## 1. EDA - Exploratory Data Analysis
Een belangrijke analyse die ik eerst heb gedaan, is het vast stellen van de '***class***' distributie.
Indien er namelijk extreme class imbalance is, moet ik gebruik maken van technieken zoals: Oversampling of undersampling. Om een betrouwbaar model te kunnen trainen. </br>
</br>
Een andere analyse is de plot waarbij alle features met ***NaN-values*** in een bar-plot worden weergegeven.
Vanuit deze plot kan ik bekijken welke features ik eventueel nog kan gebruiken in het trainen van een model.
Daarbij zoek ik naar features die maar een kleine hoeveelheid ***NaN-values*** bevatten.</br>
</br>
Ook heb ik gebruik gemaakt van boxplots, om te kijken hoe de twee klassen verschillen met elkaar in in verelijking met bepaalde features.

## 2. Feature engineering
Doormiddel van functies vanuit panda zoals: `df.info()` en `df.head()`, kan ik inzien van wat voor een type de features zijn. Het is namelijk noodzakelijk om bepaalde features die bijvoorbeeld van type '***string***' zijn te tranformeren naar type int, om het bruikbaar te maken voor een Machine learning model.
Voor deze taak heb ik veel gebruik gemaakt van sklearn: `preprocessing.LabelEncoder()`. </br>
Om de '***string***' features te transformeren in klassen.

## 3. Feature selection
Hiervoor maak ik gebruik van NaN-values distributieplot, en feature importances plot. </br>
## 4. Modeling
Gebruik gemaakt van verschillende Machine learning core algoritmen zoals: </br>
- LogisticRegression
- DecisionTreeClassifier
- RandomForestClassifier
- K-nearest Neighbor (GaussianNB)
- K-nearest Neighbor (CategoricalNB)
- K-nearest Neighbor (BernoulliNB) </br>
&</br>
- Keras Neural network / Multi layer perceptron (MLP)

## 5. Evaluation
Als evaluatie methode heb ik testset accuracy gebruikt om de modellen te beoordelen.</br>
Daarnaast heb ik de feature importances gemeten, om vervolgens features te includen of juist te excluden.</br>
## 6. Applicatie
De applicatie heeft in totaal 12 input velden. Waarvan 3 numeriek en 9 text.</br>
In de notebook (`forecasting_models.ipynb`) sla ik alle feature encoders op, die ik vervolgens in `app.py` weer gebruik.</br>
Ik gebruik het in `app.py` weer, om alle text inputs weer om te tranformeren naar classes.</br>
Daarnaast maak ik gebruik van `pickle`, om mijn model in te laden en een voorspelling uit te voeren.

## 7. Waarom zou de applicatie eventueel niet kunnen werken?
Dit zou kunnen gebeuren als er in de text inputvelden eventueel text wordt neergezet wat niet bekend is in de trainingdataset. Mocht er bijvoorbeeld een andere kleurcode zich voordoen. Dan kan de ***class encoder*** dit niet om transformeren naar een class.