def f(sentence):
    sent = ''
    for i in sentence:
        if i == " ":
            i = ""
        sent = sent + i
    print(sent)
f("A programming language is a system of notation for writing computer programs")
    