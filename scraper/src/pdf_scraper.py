import scrapy
import os
from dotenv import load_dotenv
from scrapy.crawler import CrawlerProcess
import scrapy
from scrapy.pipelines.files import FilesPipeline


class PdfPipeline(FilesPipeline):
    # to save with the name of the pdf from the website instead of hash
    def file_path(self, request, response=None, info=None):
        file_name = request.url.split('/')[-1]
        return file_name


class PdfScraper(scrapy.Spider):
    name = 'pdf_scraper'
    start_urls = ["http://www.strobl-f.de/m12.html"]
    load_dotenv("../../.env")
    custom_settings = {
        "ITEM_PIPELINES": {
            PdfPipeline: 100
        },
        "FILES_STORE": os.getenv("SCRAPED_PDFS_DIR")
    }

    def parse(self, response):
        links = response.xpath("//a[contains(text(), 'pdf')]/@href").getall()
        links = [response.urljoin(link) for link in links] # to make them absolute urls
        links = links[:-2]
        yield {
            "file_urls": links
        }


def main():
    process = CrawlerProcess()
    process.crawl(PdfScraper)
    process.start()


if __name__ == "__main__":
    main()