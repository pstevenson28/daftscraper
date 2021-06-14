from daftlistings import Daft

 daft = Daft()
 listings = daft.search()

 daft = Daft()
 daft.set_location(Location.COLLEGE_OF_COMPUTING_AND_TECHNOLOGU_DUBLIN)
 daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)

 listings = daft.search()
 daft.search(max_pages=1)

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)