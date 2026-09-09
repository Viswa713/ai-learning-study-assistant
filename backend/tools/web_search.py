import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def web_search(query: str, max_results: int = 5):
    """
    Perform a simple web search using DuckDuckGo's HTML endpoint.
    """

    if not query.strip():
        return {
            "success": False,
            "error": "Search query cannot be empty."
        }

    try:
        url = (
            "https://html.duckduckgo.com/html/"
            f"?q={quote(query)}"
        )

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/120.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=15
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        results = []

        for result in soup.select(".result")[:max_results]:
            title_element = result.select_one(".result__title")
            link_element = result.select_one(".result__a")
            snippet_element = result.select_one(".result__snippet")

            if not title_element or not link_element:
                continue

            results.append({
                "title": title_element.get_text(
                    " ",
                    strip=True
                ),
                "url": link_element.get("href", ""),
                "snippet": (
                    snippet_element.get_text(
                        " ",
                        strip=True
                    )
                    if snippet_element
                    else ""
                )
            })

        return {
            "success": True,
            "query": query,
            "results": results
        }

    except requests.exceptions.RequestException as error:
        return {
            "success": False,
            "error": f"Search request failed: {error}"
        }

    except Exception as error:
        return {
            "success": False,
            "error": f"Search failed: {error}"
        }