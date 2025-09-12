# Debugging

```
mapserv "PATH_INFO=/oapifdemo/ogcapi/" "QUERY_STRING=f=json" -conf "D:\GitHub\mapserver-templates\mapfiles\mapserver-windows.conf"
```

## TODO

- add env option to turn on
- add by requests headers
- prototype using mappyfile and Python


  // if f= query parameter is not specified, use HTTP Accept header if available
  if (p == nullptr) {
    const char *accept = getenv("HTTP_ACCEPT");


// use A first

  switch (chNamespace) {
  case 'O':
    return "ows";
  case 'A':
    return "oga"; /* oga_... (OGC Geospatial API) */
  case 'M':
    return "wms";
  case 'F':
    return "wfs";
  case 'C':
    return "wcs";
  case 'G':
    return "gml";
  case 'S':
    return "sos";
  default:

    // extend the JSON with a few things that we need for templating
    j["template"] = {{"path", json::array()},
                     {"params", json::object()},
                     {"api_root", getApiRootUrl(map)},
                     {"title", getTitle(map)},
                     {"tags", json::object()}};

