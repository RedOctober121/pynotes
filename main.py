run = True


while run is True:
    query = input("\n You: ")
    if query in ['new note', 'newnote', 'new record', 'newrecord', 'newnote()', 'newrecord()']:
        import newnote

    if query in ['records()', 'records', 'my records', 'notes()', 'notes', 'my notes']:
        file1 = open('savdata.txt', 'r')
        print(file1.read())
        print()
        file1.close()

    if 'quit()' in query:
        quit()
