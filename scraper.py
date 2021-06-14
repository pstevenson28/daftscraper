from daftlistings import Daft, Location, SearchType

daft = Daft()
daft.set_location(Location.COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN)
daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)

listings = daft.search()
daft.search(max_pages=1)

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)