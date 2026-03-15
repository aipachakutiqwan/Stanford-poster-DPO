with open("beamercolorthemestanford.sty", "r") as f:
    text = f.read()

text = text.replace(r"\setbeamertemplate{bibliography item}[text]",
                    r"\setbeamertemplate{bibliography item}[text]" + "\n" + r"\setbeamercolor{bibliography item}{fg=black}")

with open("beamercolorthemestanford.sty", "w") as f:
    f.write(text)

with open("main.tex", "r") as f:
    text = f.read()

text = text.replace(r"\footnotesize{\bibliographystyle{plain}\bibliography{poster}}",
                    r"\bibliographystyle{plain}\bibliography{poster}")

text = text.replace(r"\nocite{*}", r"\nocite{*}" + "\n" + r"    Here is some text before the bibliography to ensure block is visible.")

with open("main.tex", "w") as f:
    f.write(text)
