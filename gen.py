import pyttsx3
from colorama import Fore, Style
from time import sleep

style_reset = Style.RESET_ALL

def generate_chapter(chapter: str) -> None:
    engine = pyttsx3.init()
    chapter_name = chapter.split("\n")[0]
    print(f"[{Fore.BLUE}i{style_reset}] Generando capítulo {Fore.GREEN}{chapter_name}{style_reset}")
    engine.save_to_file(chapter, f"{chapter_name}.mp3")
    engine.runAndWait()

with open("book.txt", encoding="utf8") as book:
    chapters = book.read().split("::")
    for chapter in chapters: 
        try:
            generate_chapter(chapter=chapter)
        except Exception as e: 
            print(f"[{Fore.RED}!{style_reset}] Ha ocurrido un error.")
            print(f'"{e}"')
            
