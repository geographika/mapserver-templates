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