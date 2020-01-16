"""
Innkapsling skal hindre direkte tilgang til tilstanden til et objekt fra
objekter av andre klasser.
Grunnen til å bruke innkapsling er for å sikre at objektene har en tilstand som
er gyldig. endringene i tilstanden burde skje Ved å kalle på metodene til
objektet, og ikke endre på tingene direkte.

Et grensesnitt definerer et sett med metoder (eller meldinger) som kommer
 av en klasse som har det grensesnittet kan svare på.
Grensesnittet til et objekt består altså av det som er åpent tilgjengelig, og
ved beskrivelse av oppførselen ønsker en å unngå å trekke inn en evt. intern
tilstand, siden denne uansett er ment å være skjult. Det er det som skiller det
fra implementasjonen.

Hvert objekt har instansvariabler og de defineres og intialiseres ved
opprettelsen av et nytt objekt. Det har sine egne variabler som har verdier som
er forskjellig fra andre eksempel objekter av samme klasse og dens
instansmetodene kun påvirke sine egne variabler.Instansvariablene er private:
Brukes kun av klassens metode.
"""
