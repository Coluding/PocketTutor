from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from ExerciseAgent import ExerciseAgent
from CalculusAgent import *

def main():
    aufgabe = """Gegeben ist die Funktion f: 
x↦ln(x−3) mit maximaler Definitionsmenge 
D und Ableitungsfunktion 
f 
′
 .

Geben Sie 
D sowie die Nullstelle von 
f an."""

    loesung ="""Das Argument 
(x−3) der 
ln-Funktion muss größer 0 sein.

Also muss gelten:

x−3>0
Somit muss 
x>3 sein.

Zur Nullstelle: Die 
ln-Funktion hat den Wert 0, wenn das Argument 
x−3=1 ist.

Also 
f(x)=0, genau dann, wenn 
x−3=1. Damit ist die Nullstelle (nach Umstellen) 
x=4."""
    load_dotenv("../../.env")
    e = ExerciseAgent(ChatOpenAI())
    c = CalculusAgent()
    c.set_variable("x", "y")
    c.set_expression(SingleExpressionMapper("square"), SingleExpressionMapper("initial"), "x")
    c.set_binary_outer_func_to_current_expression(DoubleExpressionMapper("mul"), -1/8)
    c.set_outer_func_to_current_expression(SingleExpressionMapper("exp"))
    c.set_binary_outer_func_to_current_expression(DoubleExpressionMapper("mul"), 2)
    chat = CalculusChatAgent(ChatOpenAI())
    print(c.expression)
    print(c.differentiate("x"))
    #print(chat.run(c.expression, c.differentiate("x"), "Wie kommt man auf die -0.5 in der Ableitung?"))
    print(e.run(aufgabe, loesung, "Warum muss x größer als 3 sein? Erkläre es mir in einfachen Worten"))
    #print(e.run(aufgabe, loesung, "Warum ist es wichtig ob sie größer als 0 ist?"))


if __name__ == "__main__":
    main()