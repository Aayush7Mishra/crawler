"""

Extracts content exactly as modern LLMs would see it for GEO analysis
"""

from .core_crawler import GEOCrawler
from .html_parser import HTMLParser
from .data_normalizer import DataNormalizer
from .output_handler import OutputHandler
from .utils import create_output_filename, ensure_output_directory
from .api import crawl_url, crawl_url_sync, crawl_multiple_urls, extract_geo_data
from .modular_geo_crawler import GEOCrawlerOrchestrator

__version__ = "1.0.0"
__all__ = [
    "GEOCrawler",
    "HTMLParser", 
    "DataNormalizer",
    "OutputHandler",
    "GEOCrawlerOrchestrator",
    "create_output_filename",
    "ensure_output_directory",
    "crawl_url",
    "crawl_url_sync", 
    "crawl_multiple_urls",
    "extract_geo_data"
]
