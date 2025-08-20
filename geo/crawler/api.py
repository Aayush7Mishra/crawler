"""
Public API for the GEO Web Crawler
Provides simple functions for external use
"""

import asyncio
from .modular_geo_crawler import GEOCrawlerOrchestrator


async def crawl_url(url: str) -> dict:
    """
    Crawl a single URL and return the extracted data as JSON.
    
    Args:
        url (str): The URL to crawl
        
    Returns:
        dict: Complete crawled data including:
            - crawl_info: Metadata about the crawl process
            - http_info: HTTP headers and response information
            - raw_html: Original HTML content
            - rendered_html: JavaScript-rendered HTML
            - clean_text: LLM-ready text content
            - structured_data: Raw structured data (Schema.org, etc.)
            - structured_data_normalized: GEO-optimized structured data
            - meta: Meta tags and OpenGraph data
            - language: Language information
            - links: All links found on the page
            - images: All images found on the page
            - dom_diff: Changes between original and rendered HTML
            - content_stats: Content analysis statistics
            
    Example:
        >>> result = await crawl_url("https://example.com")
        >>> print(result["meta"]["title"])
        >>> print(result["structured_data_normalized"]["geo"])
    """
    orchestrator = GEOCrawlerOrchestrator()
    return await orchestrator.crawl_url(url)


def crawl_url_sync(url: str) -> dict:
    """
    Synchronous wrapper for crawl_url.
    
    Args:
        url (str): The URL to crawl
        
    Returns:
        dict: Complete crawled data (same as crawl_url)
        
    Example:
        >>> result = crawl_url_sync("https://example.com")
        >>> print(result["meta"]["title"])
    """
    return asyncio.run(crawl_url(url))


async def crawl_multiple_urls(urls: list) -> list:
    """
    Crawl multiple URLs concurrently.
    
    Args:
        urls (list): List of URLs to crawl
        
    Returns:
        list: List of crawled data dictionaries
        
    Example:
        >>> urls = ["https://example1.com", "https://example2.com"]
        >>> results = await crawl_multiple_urls(urls)
        >>> for result in results:
        ...     print(result["meta"]["title"])
    """
    orchestrator = GEOCrawlerOrchestrator()
    tasks = [orchestrator.crawl_url(url) for url in urls]
    return await asyncio.gather(*tasks, return_exceptions=True)


def extract_geo_data(crawl_result: dict) -> dict:
    """
    Extract only GEO-relevant data from a crawl result.
    
    Args:
        crawl_result (dict): Result from crawl_url()
        
    Returns:
        dict: GEO-specific data including coordinates, addresses, places
        
    Example:
        >>> result = crawl_url_sync("https://restaurant.com")
        >>> geo_data = extract_geo_data(result)
        >>> print(geo_data["coordinates"])
    """
    normalized_data = crawl_result.get("structured_data_normalized", {})
    
    return {
        "coordinates": normalized_data.get("geo"),
        "address": normalized_data.get("address"),
        "place": normalized_data.get("place"),
        "contact": normalized_data.get("contact"),
        "breadcrumbs": normalized_data.get("breadcrumbs", []),
        "language": crawl_result.get("language", {}),
        "meta_title": crawl_result.get("meta", {}).get("title"),
        "meta_description": crawl_result.get("meta", {}).get("description")
    }
