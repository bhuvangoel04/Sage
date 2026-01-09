import webbrowser

KNOWN_SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
}

def open_site(site):
    webbrowser.open(
        KNOWN_SITES.get(site, f"https://www.{site}.com")
    )
