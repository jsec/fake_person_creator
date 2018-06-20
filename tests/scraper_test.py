

def test_get_page_data():
    data = fake_person_creator.scraper.get_page_data()
    assert data == 'lul'
