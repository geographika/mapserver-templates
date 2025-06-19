## Mapfile Setup

```ps1
conda activate gdal
pip install -e D:\GitHub\mappyfile-templates

cd D:\GitHub\mapserver-templates\mapfiles
gdal vector info ./data/ne_110m_land.fgb | python D:\GitHub\mappyfile-templates\scripts\gdal_map.py wms.map
map2img -m wms.map -o wms.png -all_debug 5 -l ne_110m_land


gdal raster info ./data/crop_4326_ocs_0-30cm_mean_subset.tif | python D:\GitHub\mappyfile-templates\scripts\gdal_map.py wcs.map
map2img -m wcs.map -o wcs.png -all_debug 5 -l crop_4326_ocs

```

## Docker Setup

```
start "C:\Program Files\Docker\Docker\Docker Desktop.exe"
cd D:\GitHub\mapserver-templates\mapfiles

docker run -it --rm `
  -v ${PWD}:/etc/mapserver/:ro `
  -p 8080:80 `
  compass/compass-mapserver:8.4.0-full

```

## WMS Services

http://localhost:8080/wms/?version=1.0.0&request=GetCapabilities&service=WMS
http://localhost:8080/wms/?version=1.0.7&request=GetCapabilities&service=WMS
http://localhost:8080/wms/?version=1.1.0&request=GetCapabilities&service=WMS # incorrect mimetype? force browser to download
http://localhost:8080/wms/?version=1.1.1&request=GetCapabilities&service=WMS
http://localhost:8080/wms/?version=1.3.0&request=GetCapabilities&service=WMS

### GetMap Services

Use default OUTPUTFORMAT to construct URL
http://localhost:8080/wms/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=WMS%20Demo&STYLES=&FORMAT=image/png

### OpenLayers Services

- Require WMS GetMap request to be allowed
- Requires wms_srs to be set in WEB METADATA
- Requires wms_onlineresource to be set

http://localhost:8080/wms/?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetMap&BBOX=-90,-180,90,180&CRS=EPSG:4326&WIDTH=4096&HEIGHT=4096&LAYERS=WMS Demo&STYLES=&FORMAT=application/openlayers


Or OpenLayers is enough?

## WFS Services

http://localhost:8080/wfs/?version=1.0.0&request=GetCapabilities&service=WFS
http://localhost:8080/wfs/?version=1.1.0&request=GetCapabilities&service=WFS
http://localhost:8080/wfs/?version=2.0.0&request=GetCapabilities&service=WFS


## WCS Services

http://localhost:8080/wcs/?SERVICE=WCS&VERSION=1.0.0&REQUEST=GetCapabilities
http://localhost:8080/wcs/?SERVICE=WCS&VERSION=1.1.0&REQUEST=GetCapabilities # needs SRS for LAYER
http://localhost:8080/wcs/?SERVICE=WCS&VERSION=2.0.0&REQUEST=GetCapabilities

## SOS Services

http://localhost:8080/wfs/?version=1.0.0&request=GetCapabilities&service=WFS

msOWSDispatch(): SOS server error. SERVICE=SOS requested, but SOS support not configured in MapServer.

## CGI Services

http://localhost:8080/wms/?mode=map&layer=WMS Demo # no output
# Version 4.4 and above: passing ‘LAYERS=all’ will automatically turn on all layers.
http://localhost:8080/wms/?mode=map&layers=all # would need a layer name

http://localhost:8080/wms/?mode=legend # note classes need a name to display
http://localhost:8080/wms/?mode=legend&layers=all