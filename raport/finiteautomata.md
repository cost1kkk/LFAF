
# Intro to formal languages. Regular grammars. Finite Automata.

### Course: Formal Languages & Finite Automata
### Author: Baxanean Constantin

----

## Theory

In automata theory, a formal language is a set of strings of symbols drawn from a finite alphabet. A formal language can be specified either by a set of rules (such as regular expressions or a context-free grammar) that generates the language, or by a formal machine that accepts (recognizes) the language. A regular grammar is a mathematical object, G, with four components, G = (N, Σ, P, S), where. N is a nonempty, finite set of nonterminal symbols, Σ is a finite set of terminal symbols , or alphabet, symbols, P is a set of grammar rules, each of one having one of the forms. A → aB. A finite automaton (FA) is a simple idealized machine used to recognize patterns within input taken from some character set (or alphabet) C. The job of an FA is to accept or reject an input depending on whether the pattern defined by the FA occurs in the input.

## Objectives:

1. Understand what a language is and what it needs to have in order to be considered a formal one.

2. Provide the initial setup for the evolving project that you will work on during this semester. I said project because usually at lab works, I encourage/impose students to treat all the labs like stages of development of a whole project. Basically you need to do the following:

    a. Create a local && remote repository of a VCS hosting service (let us all use Github to avoid unnecessary headaches);

    b. Choose a programming language, and my suggestion would be to choose one that supports all the main paradigms;

    c. Create a separate folder where you will be keeping the report. This semester I wish I won't see reports alongside source code files, fingers crossed;

3. According to your variant number (by universal convention it is register ID), get the grammar definition and do the following tasks:

    a. Implement a type/class for your grammar;

    b. Add one function that would generate 5 valid strings from the language expressed by your given grammar;

    c. Implement some functionality that would convert and object of type Grammar to one of type Finite Automaton;

    d. For the Finite Automaton, please add a method that checks if an input string can be obtained via the state transition from it.


## Implementation description

The grammar was implemented under this format. Vn and Vt represent the non-terminal and terminal set of characters respectively. The transition set P contains a list of pairs. A pair consists of two strings where the first string shows what combination of terminal and non-terminal characters should convert into the second string. The first non-terminal character in the set is used as the starting character, whereas by convention, the starting character is 'S'.

```
Vn = ['S', 'B', 'D', 'Q']
Vt = ['a', 'b', 'c', 'd']
P = [
    ['S', 'aB'],
    ['S', 'bB'],
    ['B', 'cD'],
    ['D', 'dQ'],
    ['Q', 'bB'],
    ['D', 'a'],
    ['Q', 'dQ']
]
```

The FA was implemented under this format. Q is the set of all states, Sigma is the alphabet, q0 is the initial state and F is the set of final states possible. Delta is the transition set, it contains lists of 3 strings. The first string is the state the FA is in, the second string is the character the FA is checking, and the third string is the state the FA will transition to.

```
Q = ['S', 'B', 'D', 'Q', 'Final']
Sigma = ['a', 'b', 'c', 'd']
Delta = [
['S', 'a', 'B']
['S', 'b', 'B']
['B', 'c', 'D']
['D', 'd', 'Q']
['Q', 'b', 'B']
['D', 'a', 'Final']
['Q', 'd', 'Q']
]
q0 = 'S'
F = 'Final'
```

In the method below, using a while loop, I'm replacing the non-terminals with their respective strings until there are no more non-terminal characters. The replaced strings are chosen randomly given there are multiple ways for a non-terminal to transition.

```
while switch:
    switch = 0
    for char in self.non_terminal_chars:
        if char in iterated_string:
            choice_index = choice(index_return(self.transition_set,char))
            iterated_string = iterated_string.replace(char, self.transition_set[choice_index][1])
            switch = 1
```

The index_return function iterates through the transition set and adds all the indices where the passed non-terminal is present.

```
for i in range(len(list)):
    if list[i][0] == a:
    temp.append(i)
```

In order to convert the grammar to a finite automaton, I implemented a Convertor class with the respective method. By using a for loop, I iterated through the transition set of the grammar, extracting the necessary non-terminal and terminal characters for the finite automaton. However, there is a special case where the result string from the transition set is only a character long, that is when there no any non-terminal characters in string, meaning we should use a unconventionally chosen 'Final' state for the FA.

```
for non_terminal, result in grammar.transition_set:
    if len(result) > 1:
        delta_function.append([non_terminal, result[0], result[1:]])
    else:
        delta_function.append([non_terminal, result[0], 'Final'])
```

For the construction of the FA, we use the non-terminal characters and the 'Final' state as the set of all states in the FA. The alphabet of the grammar is used for the set of terminal characters. The initial state is chosen as the first non-terminal character of the Grammar.

```
FiniteAutomaton(
    grammar.non_terminal_chars + ['Final'],
    grammar.terminal_chars,
    delta_function,
    grammar.non_terminal_chars[0],
    'Final'
)
```

The method below, by using a for loop, I iterated through each character of the passed string. I then identified the index of each state/character pair in the delta function, if the pair is not contained in the delta function, then the function returns -1, which by an if statement, will return False. The current state is changed to the respective state from the delta function. The process is repeated until the end of the string, where it will be checked whether the current state is a final state. Note that this method won't work in case the FA is non-deterministic.

```
current_state = self.initial_state
for char in string:
    a = index_return(current_state, char, self.delta_function)
    if a == -1:
        return False
    current_state = self.delta_function[a][2]
if current_state == self.final_states:  
    return True
return False
```

The index_return function here is different than the previous one, though it functions in a similar way. It looks for the matching state/character pair in the passed delta function.

```
for i in range(len(list)):
    if a == list[i][0] and b == list[i][1]:
        return i
return -1
```

## Results

The following strings are generated by my grammar given the variant. The FA immediately checks if they belong to the language.

```
Generated strings:
bcddbcdbcdbcdbcddddbca
The string belongs to the finite automata
aca
The string belongs to the finite automata
aca
The string belongs to the finite automata
acdbca
The string belongs to the finite automata
bcddbca
The string belongs to the finite automata
```

If instead I input "stranger" strings into the finite automaton, it will return the following message.

```
Stranger strings:
abc
The string does not belong to the finite automata
aaa
The string does not belong to the finite automata
adadada
The string does not belong to the finite automata
bbbb
The string does not belong to the finite automata
adddddaaa
The string does not belong to the finite automata
costik
The string does not belong to the finite automata
```

## Conclusion

In this laboratory work I implemented the concept of regular grammar and finite automaton. I learned how they work and undestand how  to convert a regular grammar to a finite automaton and check the strings through it.
