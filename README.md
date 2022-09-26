# MLE Assessment
Voor dit assessment ga je een simpel prototype voor een data science project opzetten. Wij letten hierbij op de volgende vaardigheden:
- Python
- Coding guidelines
- Computer skills: kunnen installeren en leren van onbekende tool/package
- Data science project kunnen structureren
- Data lokaal kunnen inladen
- Kennis van basis machine learning algoritmes
- Keuze maken in te gebruiken machine learning algoritme
- Kunnen implementeren van basis machine learning algoritmes
- Getraind model kunnen aanroepen

Het eindproduct van deze assessment is een getraind machine learning model dat benaderd kan worden voor voorspellingen via een lokaal draaiende API.
Gebruik [de dataset](Data/) waarbij het doel is paddenstoelen te classificeren in de klassen eetbaar en giftig. Je zoekt hier zelf modellen voor uit die kandidaat zijn om uiteindelijk te gebruiken.

De opdracht is vrij in te gebruiken tools en packages, tenzij het in de opdracht aangegeven staat. Wij werken veel met Python. Het is daarom ook de bedoeling om deze opdracht in een Python omgeving te maken. Je kunt bijvoorbeeld Pandas en sklearn gebruiken als tooling voor dit probleem. Keuzes kun je eventueel verantwoorden via comments in de code.

Neem maximaal 5 uur voor dit assessment. Dit is weinig tijd voor een project van zo’n omvang. Wij snappen dat de code die jij aflevert van een andere kwaliteit zal zijn dan een project waar je langer aan kan werken. Laat vooral bij elk onderdeel zien wat je wel en niet weet. Mocht een onderdeel niet afkomen, laat dan via comments weten hoe je het probleem zou aanpakken met meer tijd en ga eventueel verder met een dummy variabele.
Besteed niet al te veel tijd aan het optimaliseren van jouw model. Het is belangrijker om te laten zien dat je werkwijzes beheerst of kan verklaren waarom iets niet goed werkt en hoe je dat met meer tijd zou aanpakken, dan een hoge model performance te hebben.

## Stappen
- Laad de data in een Pandas dataframe.
- Schoon de data op.
- Op welke manier moet de data opgeschoond worden? Welke randgevallen zijn er, of kun je zelf bedenken, waardoor jouw applicatie niet meer zal werken? Hoe handel je deze randgevallen af?
- Probeer een paar machine learning algoritmes uit.
- Verklaar de voorkeur voor een specifiek algoritme uit deze selectie.
- Train model en schrijf getraind model weg als .pickle.
- Implementeer simpele frontend applicatie voor voorspellingen.
    - Gebruik bijvoorbeeld FastAPI of Flask. Open getraind .pickle bestand in frontend applicatie. Aan de API moet je input parameters mee kunnen geven, waarna het gekoppelde model een voorspelling terugstuurt. Je hoeft geen grafische front end te maken (mag wel).
- Gebruik de frontend applicatie om een voorspelling te doen met het model.
- Kijk of de applicatie werkt voor verschillende input parameters. Noteer eventueel opvallende resultaten.
- Vul [Instructies.md](Instructies.md) met gebruiksinstructies.
- Vul [requirements.txt](requirements.txt) aan met de python libraries die je hebt gebruikt. 
- Beschrijf een data science project waar jij aan gewerkt hebt in het bestand [DS_Project.md](DS_Project.md).
- Leg het algemene doel uit en de verschillende onderdelen van het project in [Project.md](Project.md). Welke tooling heb je hierbij gebruikt? Een antwoord van ongeveer tien zinnen is voldoende. Tijdens een interview kunnen wij hier dieper op ingaan.
- Git push de gehele repo weer naar Github (Je mag maar 1x pushen naar onze github. Wij zullen je eerste push beschouwen als je inzending)
    - Na het pushen van de repo zal iemand jouw assessment nakijken. Als het nakijken afgerond is, bespreken wij het assessment tijdens een interview.