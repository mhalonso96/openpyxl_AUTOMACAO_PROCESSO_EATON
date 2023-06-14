from services.teste_service import TestScrapingService

service = TestScrapingService()
service.start_scraping(
            url="https://www.youtube.com/"
            
        )
# except Exception as error: 8