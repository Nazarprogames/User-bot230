from bs4 import BeautifulSoup
from markdown import markdown
from  .paste import pastetext

def md_to_text(md):
    html = markdown(md)
    soup = BeautifulSoup(html, features="html.parser")
    return soup.get_text()


async def paste_message(text, pastetype="p", extension=None, markdown=True):
    if markdown:
        text = md_to_text(text)
    response = await pastetext(text, pastetype, extension)
    if "url" in response:
        return response["url"]
    return "Error while pasting text to site"