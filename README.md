# PaperWritingTools
Some tools for latex-based paper.

## CleanBib.py
Read reference in bib and tex files to find redundent reference. 

`python3 CleanBib.py -d [tex folders] -b [bib txt file]`

## ToParagraph.py
Remove "-\n" to construct paragraph text.
1. copy text from pdf, add a empty line to split paragraphs.
2. `python3 CleanBib.py -r [txt file for content copy from pdf] -w [output file]`
3. copy paragraph content to Grammarly for syntax check.
eg:
input:
"I am stu-"
"dying."
""
"icecat2012."

output:
"I am studying."
"icecat2012."
