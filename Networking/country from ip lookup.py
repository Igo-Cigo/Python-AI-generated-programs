import geoip2.database

# Enter the IP address to look up
IP_ADDRESS = "49.86.191.231"

# Open the GeoIP database
reader = geoip2.database.Reader('GeoLite2-Country.mmdb')

# Look up the country for the IP address
response = reader.country(IP_ADDRESS)

# Print the country code and name
print(response.country.iso_code)
print(response.country.name)
