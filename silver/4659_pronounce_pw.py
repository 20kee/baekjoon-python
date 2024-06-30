vowels = ['a', 'e', 'i', 'o', 'u']
while True:
    word = input()
    if word == 'end':
        break

    rule1 = False
    rule2 = True
    rule3 = True
    
    word_list = list(word)
    v_count = 0
    n_count = 0
    for i, alpha in enumerate(word_list):
        if alpha in vowels:
            rule1 = True
            n_count = 0
            v_count += 1
        else:
            v_count = 0
            n_count += 1
        
        if v_count >= 3 or n_count >= 3:
            rule3 = False
        
        if i >= 1 and word_list[i-1] == word_list[i] and word_list[i] != 'e' and word_list[i] != 'o':
            rule2 = False
    
    if rule1 and rule2 and rule3:
        print('<{word}> is acceptable.'.format(word=word))
    else:
        print('<{word}> is not acceptable.'.format(word=word))
        
