import geoip2.database

async def iplookup(ip):
    with geoip2.database.Reader('moduley/ipdb/GeoLite2-City.mmdb') as reader:
        response = reader.city(ip)
        return {
            'ip' : ip,
            'network' : response.traits.network,
            'country_code' : response.country.iso_code,
            'country_name' : response.country.name,
            #'country_name_cn' : response.country.names['zh-CN'],
            'specific_name' : response.subdivisions.most_specific.name,
            'specific_code' : response.subdivisions.most_specific.iso_code,
            'cite_name' : response.city.name,
            #'cite_name_cn' : response.city.names['zh-CN'],
            'country_code' : response.postal.code,
            'latitude' : response.location.latitude,
            'longitude' : response.location.longitude,
        }
