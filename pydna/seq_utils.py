

def complement_codon(input_codon):
    if is_codon_correct(input_codon) is True:
        print('Everything ok')
    else:
        print('My bad')
        return None
            
    base_complements = {
            'A': 'T',
            'T': 'A',
            'C': 'G',
            'G': 'C',
            '?': '?'
    }

    first_base = input_codon[0]
    second_base = input_codon[1]
    third_base = input_codon[2]

    first_complemented_base = base_complements[first_base]
    second_complemented_base = base_complements[second_base]
    third_complemented_base = base_complements[third_base]

    complemented_codon = first_complemented_base + second_complemented_base + third_complemented_base

    return complemented_codon

def is_codon_correct(input_codon):
    if type(input_codon) == float:
        return False
    allowed_chars = ['A', 'T', 'C', 'G', '?', '-', 'N'] 
    
    for base in input_codon: # defining base here while creating a loop; could be called anything (i, item, x...)
        if base.upper() in allowed_chars:  # will fix problems with lower-case letters
            continue  # proceeds for next round, checking the next codon; stops when input_codon is finished
        else:
            print('Your codon sucks!') # can print something for the user but must also return an object for the code
            return False  # this stops the process; no need to use the "break" command
    return True
    
codon = 'TTT'
complement_codon(codon)
               
            
