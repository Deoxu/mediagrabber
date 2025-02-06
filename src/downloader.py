import re

class MediaDownloader:
    def __init__(self):
        self.patterns = {
            'youtube': r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com|youtu\.be)',
            'x': r'(?:https?:\/\/)?(?:www\.)?(?:twitter\.com|x\.com)',
            'facebook': r'(?:https?:\/\/)?(?:www\.)?facebook\.com',
            'tiktok': r'(?:https?:\/\/)?(?:www\.)?(?:tiktok\.com|vm\.tiktok\.com)',
            'twitch': r'(?:https?:\/\/)?(?:www\.)?twitch\.tv'
        }

    def identify_platform(self, url: str) -> str | None:
        """
        Identifica de qual plataforma o link pertence
        Args:
            url: String contendo a URL do vídeo
        Returns:
            String com o nome da plataforma ou None se não reconhecida
        """
        if not url:
            return None
            
        for platform, pattern in self.patterns.items():
            if re.search(pattern, url, re.IGNORECASE):
                return platform
        return None

    def validate_url(self, url: str) -> bool:
        """
        Verifica se a URL é válida e pertence a uma plataforma suportada
        Args:
            url: String contendo a URL do vídeo
        Returns:
            Boolean indicando se a URL é válida
        """
        return self.identify_platform(url) is not None
