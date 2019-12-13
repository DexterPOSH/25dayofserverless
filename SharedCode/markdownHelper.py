from markdown2 import Markdown

def convertMDToHTML(contentString: str):
    markdowner = Markdown()
    return markdowner.convert(contentString)