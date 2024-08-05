import importlib

from senpwai.common.scraper import ListMetadata, AnimeMetadata


def search(source: str, search_term: str) -> ListMetadata:
    try:
        src = importlib.import_module(f"senpwai.scrapers.{source}.main")
    except ModuleNotFoundError:
        # TODO: raise error in logging library
        raise ModuleNotFoundError
    return src.search(search_term)
