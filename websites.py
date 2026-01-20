import webbrowser

KNOWN_SITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "github": "https://github.com",
}

def normalize_site(site):
    return (
        site.replace(" dot ", ".")
            .replace(" ", "")
    )
    
def open_site(site):
    site = site.lower().strip()
    # Known sites
    if site in KNOWN_SITES:
        webbrowser.open(KNOWN_SITES[site])
        return

    # fallback (normalize and construct URL)
    normalized = normalize_site(site)

    if "." in normalized:
        url = "https://" + normalized
    else:
        url = f"https://www.{normalized}.com"

    webbrowser.open(url)

def google_search(query):
    query = query.replace(" ", "+")
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)