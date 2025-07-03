import wikipedia

def get_wikipedia(breed):
    try:
        # Searching for the dog breed
        search_results = wikipedia.search(breed + " dog")
        if not search_results:
            return None

        # Getting the first result that matches
        page_title = search_results[0]
        page = wikipedia.page(page_title)

        return page.url
    except wikipedia.exceptions.DisambiguationError as e:
        # Trying the first non-ambiguous result if there's a disambiguation
        for option in e.options:
            if "dog" in option.lower():
                try:
                    return wikipedia.page(option).url
                except Exception:
                    continue
        return None
    except Exception as e:
        return None