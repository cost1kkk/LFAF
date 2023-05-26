import Grammar 

class FiniteAutomata:
    def __init__(self, q0, F, sigma, delta, Q):
        self.q0 = q0
        self.F = F
        self.sigma = sigma
        self.delta = delta
        self.Q = Q

    # Define a method named "checkWord" that takes two parameters "self" and "word"
    def checkWord(self, word):
        # Check if the first character of "word" is not in the set of initial states "q0", return False if not
        if word[0] not in self.q0:
            return False

        # Check if the last character of "word" is not in the set of final states "F", return False if not
        if word[-1] not in self.F:
            return False

        # Check if all characters in "word" belong to the input alphabet "sigma", return False if not
        for letter in word:
            if letter not in self.sigma:
                return False

        # Create an empty list "transitions" to store the transitions taken by the automaton
        transitions = []
        # For each character in "word", add an empty transition to "transitions" list
        for letter in word:
            transitions.append(['', letter, ''])

        # Set the start state of the automaton to the first transition in "transitions"
        transitions[0][0] = 'S'
        # Remove the destination state of the last transition in "transitions"
        transitions[-1].pop(-1)

        # For each transition in "transitions", determine the next state by checking the delta function of the automaton
        for i in range(len(transitions) - 1):
            for state in self.delta:
                if transitions[i][0] == state[0] and transitions[i][1] == state[1]:
                    transitions[i][2] = state[2]
                    transitions[i + 1][0] = state[2]
                    break
            # If no valid transition is found for a character in "word", return False
            if transitions[i][-1] == '':
                return False

        # Print the transitions taken by the automaton for the input word
        print(f'transitions tried by the automaton{transitions}')

        # Return True if the automaton accepts the input word
        return True
    # Define a method named "convertGrammar" that takes "self" as a parameter.
    def convertGrammar(self):
        # Create an empty dictionary named "p".
        p = {}
        # Iterate through each key in the dictionary "self.Q".
        for key in self.Q:
            # Create an empty list named "finals".
            finals = []
            # Iterate through each element in the list "self.delta".
            for transition in self.delta:
                # Create an empty string named "str".
                str = ''
                # If the first element of the "transition" is equal to "key", then iterate through each element in "transition" except for the first one.
                if transition[0] == key:
                    for i in range(1, len(transition)):
                        str = str + transition[i]
                    # Add "str" to the list "finals".
                    finals.append(str)
            # Add "finals" to the dictionary "p" with the key "key".
            p[key] = finals

        # Create a new RegularGrammar object named "reg_gram" with the parameters "self.Q", "self.F", "p", and "self.sigma".
        reg_gram = Grammar.RegularGrammar(self.Q, self.F, p, self.sigma)

        # Return "reg_gram".
        return reg_gram
    # Define a method called automatonType that takes the self parameter.
    def automatonType(self):
         # Loop through each state in the Q set.
        for letter in self.Q:

             # Initialize an empty list called inputs.
            inputs = []
             # Loop through each transition in the delta set.
            for transition in self.delta:
                 # If the transition starts at the current state.
                if transition[0] == letter:
                    # If the transition symbol is already in the inputs list.
                    if transition[1] in inputs:
                        
                        # Return 'NFA' if there are multiple transitions for the same symbol.
                        return 'NFA'
                    
                    # Add the transition symbol to the inputs list.
                    inputs.append(transition[1])

            # If the set of transition symbols is not the same as the set of input symbols.
            if set(inputs) != set(self.sigma):
                # Return 'NFA' if there are missing transitions.
                return 'NFA'
        # If all states have complete and unique transitions, return 'DFA'.
        return 'DFA'

    def nfa_to_dfa(self):

        # creating the first array for conversion
        array1 = []
        for letter in self.Q:
            row = ['' for i in range(len(self.sigma))]
            for inpt in self.sigma:
                for transition in self.delta:
                    if transition[0] == letter:
                        if transition[1] == inpt:
                            if not transition[-1].islower():
                                row[self.sigma.index(inpt)] += transition[-1]
            array1.append(row)

        # creating the second array
        array2 = []
        used = []
        unused = [self.Q[0]]

        while unused:
            aux = [unused[0]]
            for i in range(0, len(self.sigma)):
                strng = ''
                for letter in unused[0]:
                    aux2 = array1[self.Q.index(letter)][i]
                    if aux2 not in strng:
                        strng += aux2
                aux.append(strng)

                if strng not in used:
                    unused.append(strng)
            array2.append(aux)

            used.append(unused[0])
            unused.remove(unused[0])

        array2_1 = []
        [array2_1.append(x) for x in array2 if x not in array2_1]
        for row in array2_1:
            for i in range(0, len(row)):
                if row[i] == '':
                    row[i] = 'dead_state'

        delta2 = []
        for row in array2_1:
            for i in range(0, len(self.sigma)):
                aux = [row[0], self.sigma[i], row[i + 1]]
                delta2.append(aux)

        Q2 = []
        for row in delta2:
            if row[0] not in Q2:
                Q2.append(row[0])

        finals = []
        for state in self.F:
            for other_state in Q2:
                if state in other_state:
                    finals.append(other_state)

        new_automaton = FiniteAutomata(self.q0[0], finals, self.sigma, delta2, Q2)
        return new_automaton








    def display(self):
        import graphviz

        f = graphviz.Digraph('finite_state_machine', filename='../Automaton Graphs/fsm.gv')
        # specifying the direction left-to-right
        f.attr(rankdir='LR', size='8,5')

        # specifying final states by double-circling them
        f.attr('node', shape='doublecircle')
        for state in self.F:
            f.node(state)

        # creating the nodes and the edges in-between
        f.attr('node', shape='circle')
        for transition in self.delta:
            if len(transition)>2:
                f.edge(transition[0],transition[2],transition[1])

        f.view()