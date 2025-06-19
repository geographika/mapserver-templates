<StyledLayerDescriptor xmlns="http://www.opengis.net/sld" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:ogc="http://www.opengis.net/ogc" xmlns:gml="http://www.opengis.net/gml" xsi:schemaLocation="http://www.opengis.net/sld StyledLayerDescriptor.xsd" version="1.0.0">
  <NamedLayer>
    <Name>ocs</Name>
    <UserStyle>
      <Title>ocs</Title>
      <FeatureTypeStyle>
        <Rule>
          <RasterSymbolizer>
           <Geometry>
              <PropertyName>Organic carbon stocks (t/ha)</PropertyName>
              <Opacity>1</Opacity>
            </Geometry>
            <ColorMap type="intervals">
            <ColorMapEntry color="#FFFFFF" label="NODATA" quantity="-32768" opacity="0.7"/>
              <ColorMapEntry color="#ffffbe" label="0" quantity="0"/>
              <ColorMapEntry color="#ffffbe" label="5" quantity="5"/>
              <ColorMapEntry color="#ffffbe" label="11" quantity="11"/>
              <ColorMapEntry color="#ffefa7" label="18" quantity="18"/>
              <ColorMapEntry color="#ffefa7" label="25" quantity="25"/>
              <ColorMapEntry color="#ffe091" label="31" quantity="31"/>
              <ColorMapEntry color="#fad27c" label="38" quantity="38"/>
              <ColorMapEntry color="#fad27c" label="45" quantity="45"/>
              <ColorMapEntry color="#dbcc6d" label="51" quantity="51"/>
              <ColorMapEntry color="#b8bc5d" label="58" quantity="58"/>
              <ColorMapEntry color="#b8bc5d" label="65" quantity="65"/>
              <ColorMapEntry color="#8b9d4e" label="71" quantity="71"/>
              <ColorMapEntry color="#688941" label="78" quantity="78"/>
              <ColorMapEntry color="#688941" label="85" quantity="85"/>
              <ColorMapEntry color="#498939" label="91" quantity="91"/>
              <ColorMapEntry color="#32893f" label="98" quantity="98"/>
              <ColorMapEntry color="#32893f" label="105" quantity="105"/>
              <ColorMapEntry color="#2a895a" label="111" quantity="111"/>
              <ColorMapEntry color="#2a895a" label="118" quantity="118"/>
              <ColorMapEntry color="#218772" label="125" quantity="125"/>
              <ColorMapEntry color="#16817c" label="131" quantity="131"/>
              <ColorMapEntry color="#16817c" label="138" quantity="138"/>
              <ColorMapEntry color="#0c6e7b" label="145" quantity="145"/>
              <ColorMapEntry color="#035675" label="151" quantity="151"/>
              <ColorMapEntry color="#035675" label="158" quantity="158"/>
              <ColorMapEntry color="#094273" label="165" quantity="165"/>
              <ColorMapEntry color="#1a3273" label="171" quantity="171"/>
              <ColorMapEntry color="#1a3273" label="178" quantity="178"/>
              <ColorMapEntry color="#2a2173" label="185" quantity="185"/>
              <ColorMapEntry color="#3b1073" label="191" quantity="191"/>
              <ColorMapEntry color="#3b1073" label="198" quantity="198"/>
              <ColorMapEntry color="#4c0073" label="205" quantity="205"/>
             <ColorMapEntry color="#4c0073" label="212" quantity="212"/>
            </ColorMap>
          </RasterSymbolizer>
        </Rule>
      </FeatureTypeStyle>
    </UserStyle>
  </NamedLayer>
</StyledLayerDescriptor>
