import moviepy.editor
def trailer(janela,teclado):
    if (teclado.key_pressed("ESC")):
        quit()
    video = moviepy.editor.VideoFileClip("imagens/test2.mp4")
    video.preview()