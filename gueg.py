import click


class words:
    words = []
    char = ''

    def get_words(self, file):
        with open(file) as wordlist:
            content = wordlist.read()
            content = content.splitlines()
            return content
        
    def append_char(self, words, char):
        appended_words = []
        for word in words:
            word = word + char
            appended_words.append(word)
        return appended_words
        
    def __init__ (self, name):
        file, length, char = name
        words = self.get_words(file)
        short_words = []
        for word in words:
            word = word.lower()
            if len(word) > length:
                word = word[:length]
            if word not in short_words:
                short_words.append(word)
        self.words = short_words
        self.char = char
        if char != '':
            self.words = self.append_char(short_words, char)

    

def mix_words(names, surnames1):
    mixed_words = []
    for name in names:
        for surname in surnames1:
            mix = name + str(surname)
            if mix not in mixed_words:
                mixed_words.append(mix)
    return mixed_words

def add_domain(users, domain):
    addresses = []
    for user in users:
        address = user + domain
        if address not in addresses:
            addresses.append(address)
    return addresses
                


@click.command()
@click.option('-l', help="`<wordlist> <word length> <character/s to append>. Use wordlist.txt 99 '' for the whole words and nothing to append.", type=(str, int, str), multiple=True)
@click.option('-n', help='Mix numbers from 1 to X with usernames.', type = int)
@click.option('-a', default='', help='Add @domain or suffix at the end of the username.')
def main(l, n, a):
    if len(l) > 1:
        names = words(l[0])
        users = names.words
        for i in range(1, len(l)):
            to_mix = words(l[i])
            users = mix_words(users, to_mix.words)
    else:
        names = words(l[0])
        users = names.words



    if n != None:
        numbers = []
        for number in range(1, n +1):
            numbers.append(number)
        users = mix_words(users, numbers)
    
    if a != None:
        users = add_domain(users, a)

    for user in users:
        print(user)

main()

#           _____                    _____                    _____                    _____          
#          /\    \                  /\    \                  /\    \                  /\    \         
#         /::\    \                /::\____\                /::\    \                /::\    \        
#        /::::\    \              /:::/    /               /::::\    \              /::::\    \       
#       /::::::\    \            /:::/    /               /::::::\    \            /::::::\    \      
#      /:::/\:::\    \          /:::/    /               /:::/\:::\    \          /:::/\:::\    \     
#     /:::/  \:::\    \        /:::/    /               /:::/__\:::\    \        /:::/  \:::\    \    
#    /:::/    \:::\    \      /:::/    /               /::::\   \:::\    \      /:::/    \:::\    \   
#   /:::/    / \:::\    \    /:::/    /      _____    /::::::\   \:::\    \    /:::/    / \:::\    \  
#  /:::/    /   \:::\ ___\  /:::/____/      /\    \  /:::/\:::\   \:::\    \  /:::/    /   \:::\ ___\ 
# /:::/____/  ___\:::|    ||:::|    /      /::\____\/:::/__\:::\   \:::\____\/:::/____/  ___\:::|    |
# \:::\    \ /\  /:::|____||:::|____\     /:::/    /\:::\   \:::\   \::/    /\:::\    \ /\  /:::|____|
#  \:::\    /::\ \::/    /  \:::\    \   /:::/    /  \:::\   \:::\   \/____/  \:::\    /::\ \::/    / 
#   \:::\   \:::\ \/____/    \:::\    \ /:::/    /    \:::\   \:::\    \       \:::\   \:::\ \/____/  
#    \:::\   \:::\____\       \:::\    /:::/    /      \:::\   \:::\____\       \:::\   \:::\____\    
#     \:::\  /:::/    /        \:::\__/:::/    /        \:::\   \::/    /        \:::\  /:::/    /    
#      \:::\/:::/    /          \::::::::/    /          \:::\   \/____/          \:::\/:::/    /     
#       \::::::/    /            \::::::/    /            \:::\    \               \::::::/    /      
#        \::::/    /              \::::/    /              \:::\____\               \::::/    /       
#         \::/____/                \::/____/                \::/    /                \::/____/        
#                                   ~~                       \/____/                                  
# Created by Cyberspatialis

# Use: 
# python3 gueg.py -l names.txt 99 '.' -l surnames.txt 99 '' -a @example.local
