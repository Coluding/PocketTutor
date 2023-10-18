from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from ExerciseAgent import ExerciseAgent
from CalculusAgent import *

def main():
    aufgabe = """2x 
    2
     +16=12x"""

    loesung = """2x 
    2
     +16	
    =	
    12x	
    −12x
    0	
    =	
    2x 
    2
     −12x+16	
    ↓
    Diskriminante berechnen

    D	
    =	
    (−12) 
    2
     −4⋅2⋅16	
    =	
    144−128	
    =	
    16	
    ⇒16	
    >	
    0	
    ↓
    daher 2 Lösungen

    2x 
    2
     +16	
    =	
    2x	
    ↓
    In die Mitternachtsformel einsetzen dabei die berechnete Diskriminante einsetzen

    x 
    1,2
    ​

    =	
    2⋅2
    12± 
    16
    ​

    ​

    ↓
    x 
    1
    ​
      berechnen

    x 
    1
    ​

    =	
    4
    12+4
    ​

    =	
    4
    16
    ​
     =4	
    x 
    2
    ​

    =	
    4
    12−4
    ​

    =	
    4
    8
    ​
     =2	
    L	
    =	
    {4;2}"""
    load_dotenv("../../.env")
    e = ExerciseAgent(ChatOpenAI())
    c = CalculusAgent()
    c.set_variable("x", "y")
    c.set_expression(SingleExpressionMapper("sin"), SingleExpressionMapper("initial"), "x")
    c.set_expression(SingleExpressionMapper("sin"), DoubleExpressionMapper("div"), "y")
    chat = CalculusChatAgent(ChatOpenAI())
    print(c.differentiate("x"))
    print(chat.run(c.expression, c.differentiate("x"), "Warum ist das die Lösung?"))
    #print(e.run(aufgabe, loesung, "warum nutzen wir die diskriminate hier?"))
    #print(e.run(aufgabe, loesung, "Warum ist es wichtig ob sie größer als 0 ist?"))


if __name__ == "__main__":
    main()