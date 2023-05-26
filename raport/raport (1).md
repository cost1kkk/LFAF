
# Determinism in Finite Automata. Conversion from NDFA 2 DFA. Chomsky Hierarchy.
### Course: Formal Languages & Finite Automata
### Author: Baxanean Constantin
### Variant: 4
## Theory
Def:
**Language** - a means of communicating information, by using visual or audio interpretations of words.
**Formal language** - a set of strings based on an alphabet that are generated with the help of a grammar.
**String** - a combination of symbols generated with the help of rules from the production set.
**Grammar** - an entity defined by four elements: the set of non-terminal symbols, the set of terminal symbols, the start symbol, and the set of production rules.
**Automation** - an abstract computational device. It contains the states, an alphabet, transition functions for each state, the initial and final states.
**Finite automaton** - an automaton with finite amounts of states and transitions.
Finite Automata and Regular Grammars are two strongly related concepts. They can be converted from one to another. 

**There are 4 types of grammars, called Chomsky Types, which describe the limitations they have:**

**Type 0**
Any form of string conversion.
**Type 1**
The condition string can have more than one character. Can't convert to empty string.
**Type 2**
The condition string has only one non-terminal character. Can convert into any configuration of strings made from non-terminals and terminals.
**Type 3**
The condition string has only one non-terminal character. Can convert to strings of form T, TN or T, NT, where T are terminals and N are non-terminals.

Only a grammar of type 3 can be converted to a Finite Automaton and vice-versa.
Finite Automata can be deterministic or non-deterministic. If from a state, using one character, we can transition to two or more different states, then the finite automaton is regarded as non-deterministic. It is possible to convert a non-deterministic finite automaton to a deterministic through the use of an algorithm.
## **Objectives**

1. Understand what an automaton is and what it can be used for.
2. Continuing the work in the same repository and the same project, the following need to be added:
    a. Provide a function in your grammar type/class that could classify the grammar based on Chomsky hierarchy.
    b. For this you can use the variant from the previous lab.
3. According to your variant number (by universal convention it is register ID), get the finite automaton definition and do the following tasks:
    a. Implement conversion of a finite automaton to a regular grammar.
    b. Determine whether your FA is deterministic or non-deterministic.
    c. Implement some functionality that would convert an NDFA to a DFA.
    d. Represent the finite automaton graphically (Optional, and can be considered as a __*bonus point*__):      
    - You can use external libraries, tools or APIs to generate the figures/diagrams.
    - Your program needs to gather and send the data about the automaton and the lib/tool/API return the visual representation.
   
## Implementation description
**Variant 4**
```
VN={S, D, R},
VT={a, b, c, d, f},
P={
S → aS
S → bD
S → fR
D → cD
D → dR
R → bR
R → f
D → d
}
Q = {q0,q1,q2,q3},
∑ = {a,b},
F = {q3},
δ(q0,a) = q1,
δ(q0,a) = q2,
δ(q1,b) = q1,
δ(q1,a) = q2,
δ(q2,a) = q1,
δ(q2,b) = q3.
```

This program defines a class called  `FiniteAutomata`. It provides the methods to check if a given word is accepted by the automaton, convert the automaton to a regular grammar, determine if the automaton is a DFA or a NFA, convert a NFA to a DFA, and display the finite state machine.

The  `__init__`  method initializes the instance variables, including  `q0`,  `F`,  `sigma`,  `delta`, and  `Q`.  `q0`  is the initial state,  `F`  is the set of final states,  `sigma`  is the input alphabet,  `delta`  is the transition function, and  `Q`  is the set of states.

The  `checkWord`  method takes a word as input and returns  `True`  if the word is accepted by the automaton,  `False`  otherwise. It checks if the first state of the word is in the initial state, if the last state of the word is in the final state, and if all the letters of the word are in the alphabet. It computes the transitions made by the automaton for the given word and prints them.

The  `convertGrammar`  method converts the automaton to a regular grammar. It initializes a dictionary to store the productions of the grammar, creates the regular grammar from the dictionary of productions, and returns the regular grammar.

The  `automatonType`  method determines if the automaton is a DFA or a NFA. It iterates over each state of the automaton and checks if the inputs for that state are unique and cover the entire input alphabet. If they are, the automaton is a DFA, otherwise it is a NFA.

The  `nfa_to_dfa`  method converts a NFA to a DFA. It creates two arrays to store the transitions and states of the DFA. It iterates over each state of the NFA and generates the corresponding row for the DFA. It then generates the remaining rows of the DFA until no new states are generated. It initializes a list of final states and generates the transition function for the DFA. Finally, it returns the new DFA.

The  `display`  method displays the finite state machine using the  `graphviz`  library. It creates a new graph with the specified filename and direction, and specifies final states by double-circling them.

## Results
```
test a string (y/n)abdf
S -> ['aS', 'bD', 'fR']
D -> ['cD', 'dR', 'd']
R -> ['bR', 'f']
---------------------
grammar type :  3
---------------------
Q = ['S', 'A', 'dead_state', 'AB', 'ABAC']
---------------------
start state: S
---------------------
final states: ['ABAC']
---------------------
sigma: ['a', 'b']
---------------------
delta:
['S', 'a', 'A']
['S', 'b', 'dead_state']
['A', 'a', 'AB']
['A', 'b', 'A']
['dead_state', 'a', 'dead_state']
['dead_state', 'b', 'dead_state']
['AB', 'a', 'ABAC']
['AB', 'b', 'A']
['ABAC', 'a', 'ABAC']
['ABAC', 'b', 'A']
---------------------
---------------------
```

## Conclusion
In this laboratory work I understand what an automaton is and what it can be used for. I had some problems with the tasks but I managed to finish this laboratory work, also I was helped by my colegues.
