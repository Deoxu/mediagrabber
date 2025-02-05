import customtkinter as ctk
import webbrowser
from PIL import Image
import os

# Definir o caminho para a pasta images (coloque isso logo após os imports)
import os
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
images_dir = os.path.join(current_dir, "images")

# Definir o caminho para as fontes de forma mais explícita
fonts_dir = os.path.join(current_dir, "fonts")

# Configurações da interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Media Grabber")
app.geometry("800x500")
app.resizable(False, False)
app._set_appearance_mode("dark")  # Garantir modo escuro
app.configure(fg_color="#000000")  # Configurar cor de fundo da janela principal para preto

# Cores para os botões
DEFAULT_FG = "#333"
ACTIVE_FG = "white"
DEFAULT_HOVER = "#555"

# Criar fontes personalizadas com caminhos absolutos
roboto_regular = os.path.join(fonts_dir, "Roboto-Regular.ttf")
roboto_bold = os.path.join(fonts_dir, "Roboto-Bold.ttf")
roboto_light = os.path.join(fonts_dir, "Roboto-Light.ttf")

# Registrar as fontes no sistema
from tkinter import font
import tkinter as tk

def load_custom_font(font_path, family_name):
    try:
        tk.font.families()  # Inicializa o sistema de fontes
        custom_font = tk.font.Font(font=font_path)
        print(f"Fonte carregada: {font_path}")
        return True
    except Exception as e:
        print(f"Erro ao carregar fonte {font_path}: {e}")
        return False

# Tentar carregar cada fonte
load_custom_font(roboto_regular, "Roboto")
load_custom_font(roboto_bold, "Roboto Bold")
load_custom_font(roboto_light, "Roboto Light")

# Definir as fontes após o carregamento
emoji_font = ("Arial", 20)  # Mantendo Arial para emojis
small_font = ("Roboto Light", 10)  # Para textos pequenos como os da barra lateral
title_font = ("Roboto Bold", 24)   # Para títulos
text_font = ("Roboto", 14)         # Para texto geral

# --- FRAME LATERAL ---
side_frame = ctk.CTkFrame(app, width=100, height=500, fg_color="#101010")
side_frame.pack(side="left", fill="y")

# Espaço para a logo acima do botão Save
logo_frame = ctk.CTkFrame(side_frame, width=80, height=40, fg_color="#101010")
logo_frame.pack(side="top", fill="x", pady=5)

# Calcular o tamanho proporcional da logo
original_image = Image.open("images/logo.png")
original_width, original_height = original_image.size
max_width = 80
max_height = 40

# Calcular as proporções para largura e altura
width_ratio = max_width / original_width
height_ratio = max_height / original_height

# Usar o menor ratio para garantir que a imagem caiba completamente
scale_ratio = min(width_ratio, height_ratio)
new_width = int(original_width * scale_ratio)
new_height = int(original_height * scale_ratio)

# Adicionar a logo
logo_image = ctk.CTkImage(light_image=original_image,
                         dark_image=original_image,
                         size=(new_width, new_height))
logo_label = ctk.CTkLabel(logo_frame, image=logo_image, text="")
logo_label.pack(expand=True, fill="both")

# Frame inferior para botões About e Settings
bottom_frame = ctk.CTkFrame(side_frame, fg_color="#101010")
bottom_frame.pack(side="bottom", fill="x")

# Frame para o botão Save
download_frame = ctk.CTkFrame(side_frame, width=80, height=50, fg_color=DEFAULT_FG, corner_radius=0)
download_frame.pack(side="top", fill="x", pady=(0, 10))
download_frame.pack_propagate(False)

download_emoji = ctk.CTkLabel(download_frame, text="⬇", font=emoji_font)
download_emoji.pack(pady=(5, 0))
download_text = ctk.CTkLabel(download_frame, text="Save", font=small_font)
download_text.pack(pady=(0, 5))

# Frame para o botão About
about_frame = ctk.CTkFrame(bottom_frame, width=80, height=50, fg_color=DEFAULT_FG, corner_radius=0)
about_frame.pack(fill="x")
about_frame.pack_propagate(False)

about_emoji = ctk.CTkLabel(about_frame, text="ℹ", font=emoji_font)
about_emoji.pack(pady=(5, 0))
about_text = ctk.CTkLabel(about_frame, text="About", font=small_font)
about_text.pack(pady=(0, 5))

# Frame para o botão Settings
settings_frame = ctk.CTkFrame(bottom_frame, width=80, height=50, fg_color=DEFAULT_FG, corner_radius=0)
settings_frame.pack(fill="x")
settings_frame.pack_propagate(False)

settings_emoji = ctk.CTkLabel(settings_frame, text="⚙", font=emoji_font)
settings_emoji.pack(pady=(5, 0))
settings_text = ctk.CTkLabel(settings_frame, text="Settings", font=small_font)
settings_text.pack(pady=(0, 5))

# Função para simular hover nos frames
def on_enter(e, frame):
    frame.configure(fg_color=DEFAULT_HOVER)

def on_leave(e, frame):
    frame.configure(fg_color=DEFAULT_FG)

# Função para lidar com cliques
def on_click(e, command):
    command()

# Adicionar eventos de hover e clique
download_frame.bind('<Enter>', lambda e: on_enter(e, download_frame))
download_frame.bind('<Leave>', lambda e: on_leave(e, download_frame))
download_frame.bind('<Button-1>', lambda e: on_click(e, show_download))

about_frame.bind('<Enter>', lambda e: on_enter(e, about_frame))
about_frame.bind('<Leave>', lambda e: on_leave(e, about_frame))
about_frame.bind('<Button-1>', lambda e: on_click(e, show_about))

settings_frame.bind('<Enter>', lambda e: on_enter(e, settings_frame))
settings_frame.bind('<Leave>', lambda e: on_leave(e, settings_frame))
settings_frame.bind('<Button-1>', lambda e: on_click(e, show_settings))

# Adicionar eventos de clique também às labels
download_emoji.bind('<Button-1>', lambda e: on_click(e, show_download))
download_text.bind('<Button-1>', lambda e: on_click(e, show_download))

about_emoji.bind('<Button-1>', lambda e: on_click(e, show_about))
about_text.bind('<Button-1>', lambda e: on_click(e, show_about))

settings_emoji.bind('<Button-1>', lambda e: on_click(e, show_settings))
settings_text.bind('<Button-1>', lambda e: on_click(e, show_settings))

# --- CONTAINER PRINCIPAL ---
container = ctk.CTkFrame(app, fg_color="#000000")
container.pack(expand=True, fill="both", padx=20, pady=20)

# --- TELA "SAVE" ---
frame_download = ctk.CTkFrame(container, fg_color="#000000")

# Wrapper centralizado
wrapper = ctk.CTkFrame(frame_download, fg_color="#000000")
wrapper.pack(expand=True)

# Carregar e redimensionar a logo principal
main_logo_original = Image.open(os.path.join(images_dir, "biglogo.png"))
original_width, original_height = main_logo_original.size
desired_width = 345  # Aumentado em 15% (300 * 1.15)
scale_ratio = desired_width / original_width
new_height = int(original_height * scale_ratio)

# Criar a imagem para a logo principal
main_logo = ctk.CTkImage(
    light_image=main_logo_original,
    dark_image=main_logo_original,
    size=(desired_width, new_height)
)

# Substituir o emoji pela logo
main_logo_label = ctk.CTkLabel(wrapper, image=main_logo, text="")
main_logo_label.pack(pady=20)

# Campo de entrada
link_entry = ctk.CTkEntry(wrapper, 
                         placeholder_text="paste the link here", 
                         width=400, 
                         fg_color="#000000",
                         text_color="white",
                         border_color="#FFFFFF",
                         placeholder_text_color="gray",
                         corner_radius=10)
link_entry.pack(pady=10)

# Frame dos botões de opção
format_frame = ctk.CTkFrame(wrapper, fg_color="#000000")
format_frame.pack(pady=10)

audio_button = ctk.CTkButton(format_frame, text="Audio", width=80, fg_color="#333", hover_color="#555")
video_button = ctk.CTkButton(format_frame, text="Video", width=80, fg_color="#333", hover_color="#555")
info_button  = ctk.CTkButton(format_frame, text="Info", width=80, fg_color="#333", hover_color="#555")

audio_button.grid(row=0, column=2, padx=5)
video_button.grid(row=0, column=1, padx=5)
info_button.grid(row=0, column=0, padx=5)

# Ajustar tamanho dos ícones para 25x25 pixels
icon_size = (25, 25)

# Carregar ícones (versões escuras e claras)
download_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(images_dir, "download.png")),
    dark_image=Image.open(os.path.join(images_dir, "download.png")),
    size=icon_size
)

download_icon_white = ctk.CTkImage(
    light_image=Image.open(os.path.join(images_dir, "download.png")).convert("L"),
    dark_image=Image.open(os.path.join(images_dir, "download.png")).convert("L"),
    size=icon_size
)

info_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(images_dir, "info.png")),
    dark_image=Image.open(os.path.join(images_dir, "info.png")),
    size=icon_size
)

info_icon_white = ctk.CTkImage(
    light_image=Image.open(os.path.join(images_dir, "info.png")).convert("L"),
    dark_image=Image.open(os.path.join(images_dir, "info.png")).convert("L"),
    size=icon_size
)

settings_icon = ctk.CTkImage(
    light_image=Image.open(os.path.join(images_dir, "settings.png")),
    dark_image=Image.open(os.path.join(images_dir, "settings.png")),
    size=icon_size
)

settings_icon_white = ctk.CTkImage(
    light_image=Image.open(os.path.join(images_dir, "settings.png")).convert("L"),
    dark_image=Image.open(os.path.join(images_dir, "settings.png")).convert("L"),
    size=icon_size
)

# --- TELA "ABOUT" ---
frame_about = ctk.CTkFrame(container, fg_color="#000000")

# Wrapper centralizado para About
about_wrapper = ctk.CTkFrame(frame_about, fg_color="#000000")
about_wrapper.pack(expand=True)

about_title = ctk.CTkLabel(about_wrapper, text="Sobre", font=title_font, text_color="white")
about_title.pack(pady=(20, 10))

about_description = ("Estou desenvolvendo essa aplicação para aprender mais sobre Python e ajudar pessoas "
              "que necessitam de um aplicativo para baixar músicas ou vídeos, sem a inconveniência de "
              "múltiplos pop-ups.\n\n"
              "Opções de download: MP3 (audio) e MP4 (video)\n"
              "Aplicações suportadas: YouTube, Twitter, Twitch, Facebook\n\n"
              "A funcionalidade de salvamento simplifica o download de conteúdo da internet e não assume "
              "responsabilidade sobre o uso do conteúdo salvo.")

about_label = ctk.CTkLabel(about_wrapper, text=about_description, font=text_font, text_color="white", justify="left", wraplength=600)
about_label.pack(padx=20, pady=10)

# Calcular dimensões proporcionais para a logo do GitHub
github_original = Image.open(os.path.join(images_dir, "github.png"))
original_width, original_height = github_original.size
desired_width = 200  # Largura desejada
scale_ratio = desired_width / original_width
new_height = int(original_height * scale_ratio)

# Função para lidar com o clique no link do GitHub
def open_github_link(event):
    webbrowser.open("https://github.com/Deoxu")

# Criar e configurar a imagem do GitHub
github_image = ctk.CTkImage(
    light_image=github_original,
    dark_image=github_original,
    size=(desired_width, new_height)
)

github_button = ctk.CTkLabel(
    about_wrapper,
    image=github_image,
    text="",
    cursor="hand2"
)
github_button.pack(pady=(10, 20))
github_button.bind("<Button-1>", open_github_link)

# Função para atualizar a aparência dos botões
def update_buttons(active_button):
    # Resetar todos os botões para o estado padrão
    download_frame.configure(fg_color=DEFAULT_FG)
    about_frame.configure(fg_color=DEFAULT_FG)
    settings_frame.configure(fg_color=DEFAULT_FG)
    
    # Resetar todas as cores de texto para branco
    download_emoji.configure(text_color="white")
    download_text.configure(text_color="white")
    about_emoji.configure(text_color="white")
    about_text.configure(text_color="white")
    settings_emoji.configure(text_color="white")
    settings_text.configure(text_color="white")
    
    # Configurar o botão ativo para branco e texto preto
    if active_button == "download":
        download_frame.configure(fg_color="white")
        download_emoji.configure(text_color="black")
        download_text.configure(text_color="black")
        download_frame.unbind('<Enter>')
        download_frame.unbind('<Leave>')
    else:
        download_frame.bind('<Enter>', lambda e: on_enter(e, download_frame))
        download_frame.bind('<Leave>', lambda e: on_leave(e, download_frame))
        
    if active_button == "about":
        about_frame.configure(fg_color="white")
        about_emoji.configure(text_color="black")
        about_text.configure(text_color="black")
        about_frame.unbind('<Enter>')
        about_frame.unbind('<Leave>')
    else:
        about_frame.bind('<Enter>', lambda e: on_enter(e, about_frame))
        about_frame.bind('<Leave>', lambda e: on_leave(e, about_frame))
        
    if active_button == "settings":
        settings_frame.configure(fg_color="white")
        settings_emoji.configure(text_color="black")
        settings_text.configure(text_color="black")
        settings_frame.unbind('<Enter>')
        settings_frame.unbind('<Leave>')
    else:
        settings_frame.bind('<Enter>', lambda e: on_enter(e, settings_frame))
        settings_frame.bind('<Leave>', lambda e: on_leave(e, settings_frame))

# Funções de navegação atualizadas
def show_download():
    hide_frames()
    frame_download.pack(expand=True, fill="both")
    update_buttons("download")

def show_about():
    hide_frames()
    frame_about.pack(expand=True, fill="both")
    update_buttons("about")

def show_settings():
    hide_frames()
    frame_settings.pack(expand=True, fill="both")
    update_buttons("settings")

# Função para esconder todos os frames
def hide_frames():
    frame_download.pack_forget()
    frame_about.pack_forget()
    frame_settings.pack_forget()

# --- TELA "SETTINGS" ---
frame_settings = ctk.CTkFrame(container, fg_color="#000000")

# Wrapper centralizado para Settings
settings_wrapper = ctk.CTkFrame(frame_settings, fg_color="#000000")
settings_wrapper.pack(expand=True)

settings_title = ctk.CTkLabel(settings_wrapper, text="Configurações", font=title_font, text_color="white")
settings_title.pack(pady=(20, 10))

directory_frame = ctk.CTkFrame(settings_wrapper, fg_color="#000000")
directory_frame.pack(pady=10)

directory_button = ctk.CTkButton(directory_frame, 
                               text="Selecionar Diretório", 
                               width=200, 
                               fg_color="#333", 
                               hover_color="#555", 
                               font=text_font)
directory_button.pack(side="left", padx=5)

directory_label = ctk.CTkLabel(directory_frame, 
                             text="Nenhum diretório selecionado", 
                             text_color="white", 
                             font=text_font)
directory_label.pack(side="left")

auto_format_var = ctk.StringVar(value="off")
auto_format_checkbox = ctk.CTkCheckBox(settings_wrapper, 
                                     text="Formatar nomes automaticamente", 
                                     variable=auto_format_var, 
                                     onvalue="on", 
                                     offvalue="off", 
                                     font=text_font)
auto_format_checkbox.pack(pady=10)

# Funções de navegação
def hide_frames():
    frame_download.pack_forget()
    frame_about.pack_forget()
    frame_settings.pack_forget()

def show_download():
    hide_frames()
    frame_download.pack(expand=True, fill="both")
    update_buttons("download")

def show_about():
    hide_frames()
    frame_about.pack(expand=True, fill="both")
    update_buttons("about")

def show_settings():
    hide_frames()
    frame_settings.pack(expand=True, fill="both")
    update_buttons("settings")

# Tela inicial
show_download()

app.mainloop()