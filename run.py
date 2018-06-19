from fake_person_creator import scraper

soup = scraper.get_page_data()
print(soup.prettify())
