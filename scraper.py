from daftlistings import Daft, Location, SearchType

daft = Daft()
daft.set_location(Location.COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN) #Search for student accomodation near Dundalk IT.
daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)
daft.set_min_price(400)
daft.set_max_price(700)

#lists only 1 page from daft
listings = daft.search(max_pages=1)
#inputting the coordinates from google maps and using the lambda function gives us accommodation nearest CCT
COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords = [53.34611743880528, -6.258371046939863]
listings.sort(key=lambda x: x.distance_to(COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords))

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)
    print(f'{listing.distance_to(COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords):.3}km') #Search properties according to criteria then sort by nearness to Dublin Castle

