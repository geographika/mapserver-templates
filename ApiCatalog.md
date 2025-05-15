RFC 9264
https://datatracker.ietf.org/doc/rfc9264/

Linkset: Media Types and a Link Relation Type for Link Sets
https://www.rfc-editor.org/rfc/rfc9264.html

https://datatracker.ietf.org/doc/draft-ietf-httpapi-api-catalog/08/
draft-ietf-httpapi-api-catalog-08 

The API Catalog (as per the IETF draft) and Linksets (defined in RFC 9264) are complementary specifications 

You can link the two: a Linkset entry can point to an API Catalog.



@app.route('/api-catalog.json')
@app.route('/.well-known/api-catalog')

https://github.com/geopython/demo.pygeoapi.io/pull/60/files

Appears however to return a linkset.



## Notes

Allow admins to see all accessible end-points - aid in securing them


title - take from WMS/WCS title etc.


Lots of different versions of WMS etc. list all if they are available?


## OpenLayers Links

https://demo.mapserver.org/cgi-bin/wms_landsat?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities

https://maps.isric.org/mapserv?map=/map/gyga.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-40,-50,55,15&CRS=EPSG:4326&WIDTH=1426&HEIGHT=895&LAYERS=gyga_af_agg_erzd_crfvol__m_1km&STYLES=&FORMAT=application/openlayers

https://demo.mapserver.org/cgi-bin/wms_landsat?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=WMS_server&STYLES=&FORMAT=application/openlayers

# not sure how to get layer name
https://demo.mapserver.org/cgi-bin/wms_landsat?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=lunenburg&STYLES=&FORMAT=application/openlayers


https://demo.mapserver.org/cgi-bin/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=WMS_server&STYLES=&FORMAT=application/openlayers