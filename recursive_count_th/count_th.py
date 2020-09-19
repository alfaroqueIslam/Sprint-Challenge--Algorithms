'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word, n=0, x=0):
    if word == '':
        return x
    
    if word[n]+word[n+1] == 'th' and n < len(word) - 1:
        x = x + 1
        n = n + 1
        print(x)
        if n == len(word) - 1:
            return x
        return count_th(word,n,x)
    n = n + 1
    if n == len(word) - 1:
        print(x)
        return x
    else:
        return count_th(word,n,x)
    

