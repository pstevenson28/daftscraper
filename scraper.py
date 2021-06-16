import time
# from daftlistings import Daft, Location, SearchType

from daftlistings import Daft, Location, SearchType, PropertyType

daft = Daft()
daft.set_location(Location.DUBLIN)
daft.set_search_type(SearchType.RESIDENTIAL_SALE)
daft.set_property_type(PropertyType.HOUSE)
daft.set_min_price(400000)
daft.set_max_price(500000)

listings = daft.search()

for listing in listings:
    print(listing.title)
    print(listing.price)
    print(listing.daft_link)

# daft = Daft()
# daft.set_location(Location.COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN) #Search for student accomodation near Dundalk IT.
# daft.set_search_type(SearchType.STUDENT_ACCOMMODATION)
# daft.set_min_price(400)
# daft.set_max_price(700)

# #lists only 1 page from daft
# listings = daft.search(max_pages=1)
# #inputting the coordinates from google maps and using the lambda function gives us accommodation nearest CCT
# COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords = [53.34611743880528, -6.258371046939863]
# listings.sort(key=lambda x: x.distance_to(COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords))

# for listing in listings:
#   print(listing.title)
#   print(listing.price)
#   print(listing.daft_link)
#   #Search properties according to criteria then sort by nearness to Dublin Castle
#   print(f'{listing.distance_to(COLLEGE_OF_COMPUTING_TECHNOLOGY_DUBLIN_coords):.3}km')

   
def algo1(n):
    product = 1
    for i in range(n):
        product = product / (i+1)
    return product

print (algo1(5))

def algo2(n):
    if n == 0:
        return 1
    else:
        return n / algo2(n-1)

print (algo2(5))

  # STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = algo1(100)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)

# STEP 1: Get start time
start_time = time.time()
# Step 2: Run your code you want to time
result = algo2(100)
# Step 3: Calculate total time elapsed
end_time = time.time() - start_time

print(end_time)