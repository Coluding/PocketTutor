# Langchain Agents

Ich habe hier ein ordner mit verschiedenen LLM Agenten basierend auf langchain. Jeder Agent ist für einen anderen 
usecase geeignet.

## ExerciseAgent
Nimmt eine Aufgabe und Lösung und eine Frage als Input und beantwortet die Frage zur der Aufgabe. 
Durch das Geben der Lösung minimieren wir Halluzinationen des Modells.
Nötige .env Variablen:
```
OPENAI_API_KEY=
OPENAI_MODEL_NAME= 
```

## CalculusAgent und CalculusChatAgent
Kann Ableitungen und Integrationen durchführen. Der CalculusChatAgent ist dann in der Lage Fragen zu der 
Ableitung oder Integral zu beantworten.
Nötige .env Variablen:
```
OPENAI_API_KEY=
```

## RecapAgent
Erstellt wahr oder falsch Fragen zu einem gegebenen Grundwissens-PDF. Die Fragen werden inklusive Antworten abgespeichert.
Der Agent wertet dann Antworten von Schülern bzgl. der Begründung und Antwort an sich aus.
Nötige .env Variablen:
```
OPENAI_API_KEY=
OPENAI_MODEL_NAME= 
```

How to: 
```
qa = RecapQuestionAgent(r"C:\Users\lbierling\Downloads\Normalverteilung.pdf",
                        "normalverteilung")
print(qa.filtered_ques_list)
print(qa.review_question(qa.filtered_ques_list[5], "wahr, sie stehen für mittelwert und modalwert"))
```