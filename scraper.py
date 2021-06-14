from daftlistings import Daft, Location, SearchType

daft = Daft()
daft.set_location(Location.COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN)
daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)
daft.set_min_price(400)
daft.set_max_price(700)

listings = daft.search(max_pages=1)
COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords = [53.34611743880528, -6.258371046939863]
listings.sort(key=lambda x: x.distance_to(COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords))

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print(f'{listing.distance_to(COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords):.3}km')

