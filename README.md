# gueg
gueg(Great Username and Email Generator) is a python utility for generating user and email address worlists based on naming patterns.

Use case:
Say you found an email address `jdoe@example.local` for the user John Doe, you know that the pattern is First Name Letter + Surname + @example.local. The command used to generate  a wordlist with a similar pattern would be:
```
python3 gueg.py -l names.txt 1 '' -l surnames.txt 99 '' -a @example.net
```
The wordlist generated would be something like:
```
nleon@example.net
trivera@example.net
bmendoza@example.net
```

## Usage
```
python3 gueg.py -l names.txt 1 '' -l surnames.txt 99 '' -n 8 -a @example.net
```
- `-l <wordlist> <word length> <character/s to append>` Use `wordlist.txt 99 ''` For the whole words and nothing to append.
- `-n <max>` Mix numbers from 1 to max with usernames.
- `-a @example.net` Add @domain or suffix at the end of the username.

### Examples
**`name.surname@domain.local`**:
```
python3 gueg.py -l names.txt 99 '.' -l surnames.txt 99 '' -a @example.net
```
Output:
```
michael.rogers@example.net
david.stewart@example.net
diane.alexander@example.net
```

**`surname.nameNUMBER@domain.local`** With name having 3 letters and numbers from 1 to 10:
```
python3 gueg.py -l surnames.txt 99 '.' -l names.txt 3 '' -n 10 -a @example.net 
```
Output:
```
rogers.mic8@example.net
stewart.dav2@example.net
alexander.dia10@example.net
```
