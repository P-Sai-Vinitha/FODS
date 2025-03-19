import pandas as pd
property_data = pd.DataFrame({
    'property_id': [1, 2, 3, 4, 5],
    'location': ['NYC', 'LA', 'NYC', 'SF', 'LA'],
    'bedrooms': [3, 5, 4, 2, 6],
    'area_sqft': [1500, 2500, 1800, 1200, 3000],
    'listing_price': [500000, 750000, 600000, 450000, 950000]
})
avg_price_per_location = property_data.groupby('location')['listing_price'].mean()
print("Average Listing Price per Location:\n", avg_price_per_location)
num_large_properties = (property_data['bedrooms'] > 4).sum()
print("\nNumber of properties with more than four bedrooms:", num_large_properties)
largest_property = property_data.loc[property_data['area_sqft'].idxmax()]
print("\nProperty with the largest area:\n", largest_property)
