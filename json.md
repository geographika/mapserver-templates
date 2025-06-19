# Proposed JSON Structure

The proposed JSON structure is shown below. 

```json
{
  "linkset": [
    {
      "anchor": "https://demo.mapserver.org/cgi-bin/wms?",
      "meta": {
        "name": "WMS",
        "type": "WMS"
      }, 
      "service-desc": [
        {
          "href": "https://demo.mapserver.org/cgi-bin/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities",
          "title": "WMS Demo Server for MapServer",
          "type": "text/xml"
        }
      ]
    },
```

- The top-level key is `linkset`, which contains an array of linkset entries.
- Each entry has an `anchor` URL, which is the base URL for the service.
- The `meta` key contains metadata about the service, including its name and type.

## Notes

Benefits of the index page include:

- It allows sysadmins to see all accessible MapServer end-points - and help securing them or disabling them if not required
- It allows users to see all available services and their capabilities

- `anchor` - this will use the appropriate online resource URL
- `title` - this will use "wms_title" for WMS, "wfs_title" for WFS etc.
- `type` - this is the mime type the href will return

## Design Questions

- Each service type will have a linkset created for its root object. For example with WMS this
  would be `GetCapabilities`.
- Also include a link to `GetMap`?
- There are lots of different versions of WMS, WFS etc. each with their own end points. Should
  each of these be listed as a separate linkset object? For example with WMS there would be 5 linksets for WMS `1.0.0`, `1.1.0`, `1.1.1`, and `1.3.0`. 

  > MapServer supports the following WMS versions: 1.0.0, 1.0.7, 1.1.0 (a.k.a. 1.0.8), 1.1.1 and 1.3.0.
  https://mapserver.org/ogc/wms_server.html#introduction

  I wasn't even aware there was a `1.0.7` version, but that URL is available (and if not required should probably be disabled by sysadmins to reduce the attack surface).
  
  https://demo.mapserver.org/cgi-bin/wms?SERVICE=WMS&VERSION=1.0.7&REQUEST=GetCapabilities

- How should the default template group linksets? By type or Map name?


## API Catalog

I am still unclear on the difference between the API Catalog and Linkset. 

> The API Catalog (as per the IETF draft) and Linksets (defined in RFC 9264) are complementary specifications

> You can link the two: a Linkset entry can point to an API Catalog.

I have based the JSON structure on the
PyGeoAPI API Catalog approach added in https://github.com/geopython/demo.pygeoapi.io/pull/60/files. This however appears to return a linkset.

```python
@app.route('/api-catalog.json')
@app.route('/.well-known/api-catalog')
```

https://demo.pygeoapi.io/api-catalog.json

```json
{
  "linkset": [
    {
      "anchor": "https://demo.pygeoapi.io/master",
      "service-desc": [
        {
          "href": "https://demo.pygeoapi.io/master/openapi?f=json",
          "title": "pygeoapi - latest GitHub 'master' version (JSON)",
          "type": "application/vnd.oai.openapi+json"
        }
      ],
      "service-doc": [
        {
          "href": "https://demo.pygeoapi.io/master/openapi?f=html",
          "title": "pygeoapi - latest GitHub 'master' version (HTML)",
          "type": "text/html"
        }
      ]
    },
```

See [Linkset: Media Types and a Link Relation Type for Link Sets](https://www.rfc-editor.org/rfc/rfc9264.html).
See also [RFC 9264](https://datatracker.ietf.org/doc/rfc9264/). 

The API Catalog is a draft IETF specification that is still in development.It is not yet an RFC, but it is being discussed in the IETF HTTP API working group.
See [draft-ietf-httpapi-api-catalog-08](https://datatracker.ietf.org/doc/draft-ietf-httpapi-api-catalog/08/). 

## OpenLayers Links

- https://demo.mapserver.org/cgi-bin/wms_landsat?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities
- https://maps.isric.org/mapserv?map=/map/gyga.map&SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-40,-50,55,15&CRS=EPSG:4326&WIDTH=1426&HEIGHT=895&LAYERS=gyga_af_agg_erzd_crfvol__m_1km&STYLES=&FORMAT=application/openlayers
- https://demo.mapserver.org/cgi-bin/wms_landsat?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=WMS_server&STYLES=&FORMAT=application/openlayers

Not sure how to get layer names. Maybe just use the map name?

- https://demo.mapserver.org/cgi-bin/wms_landsat?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=lunenburg&STYLES=&FORMAT=application/openlayers
- https://demo.mapserver.org/cgi-bin/wms?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=WMS_server&STYLES=&FORMAT=application/openlayers


