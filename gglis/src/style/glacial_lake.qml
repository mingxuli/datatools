<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis version="1.5.0-Tethys" minimumScale="0" maximumScale="1e+08" minLabelScale="1" maxLabelScale="250000" hasScaleBasedVisibilityFlag="0" scaleBasedLabelVisibilityFlag="1" >
  <transparencyLevelInt>255</transparencyLevelInt>
  <classificationattribute>danger_level</classificationattribute>
  <uniquevalue>
    <classificationfield>danger_level</classificationfield>
    <symbol>
      <lowervalue></lowervalue>
      <uppervalue></uppervalue>
      <label></label>
      <pointsymbol>hard:circle</pointsymbol>
      <pointsize>2</pointsize>
      <pointsizeunits>pixels</pointsizeunits>
      <rotationclassificationfieldname></rotationclassificationfieldname>
      <scaleclassificationfieldname></scaleclassificationfieldname>
      <symbolfieldname></symbolfieldname>
      <outlinecolor red="0" blue="255" green="85" />
      <outlinestyle>SolidLine</outlinestyle>
      <outlinewidth>0.26</outlinewidth>
      <fillcolor red="85" blue="255" green="170" />
      <fillpattern>SolidPattern</fillpattern>
      <texturepath null="1" ></texturepath>
    </symbol>
    <symbol>
      <lowervalue>L1</lowervalue>
      <uppervalue>L1</uppervalue>
      <label></label>
      <pointsymbol>hard:circle</pointsymbol>
      <pointsize>2</pointsize>
      <pointsizeunits>pixels</pointsizeunits>
      <rotationclassificationfieldname></rotationclassificationfieldname>
      <scaleclassificationfieldname></scaleclassificationfieldname>
      <symbolfieldname></symbolfieldname>
      <outlinecolor red="255" blue="0" green="170" />
      <outlinestyle>SolidLine</outlinestyle>
      <outlinewidth>0.3</outlinewidth>
      <fillcolor red="180" blue="53" green="85" />
      <fillpattern>Dense4Pattern</fillpattern>
      <texturepath></texturepath>
    </symbol>
    <symbol>
      <lowervalue>L2</lowervalue>
      <uppervalue>L2</uppervalue>
      <label></label>
      <pointsymbol>hard:circle</pointsymbol>
      <pointsize>2</pointsize>
      <pointsizeunits>pixels</pointsizeunits>
      <rotationclassificationfieldname></rotationclassificationfieldname>
      <scaleclassificationfieldname></scaleclassificationfieldname>
      <symbolfieldname></symbolfieldname>
      <outlinecolor red="220" blue="30" green="30" />
      <outlinestyle>SolidLine</outlinestyle>
      <outlinewidth>0.5</outlinewidth>
      <fillcolor red="220" blue="30" green="30" />
      <fillpattern>Dense2Pattern</fillpattern>
      <texturepath></texturepath>
    </symbol>
    <symbol>
      <lowervalue>L3</lowervalue>
      <uppervalue>L3</uppervalue>
      <label></label>
      <pointsymbol>hard:circle</pointsymbol>
      <pointsize>2</pointsize>
      <pointsizeunits>pixels</pointsizeunits>
      <rotationclassificationfieldname></rotationclassificationfieldname>
      <scaleclassificationfieldname></scaleclassificationfieldname>
      <symbolfieldname></symbolfieldname>
      <outlinecolor red="255" blue="0" green="0" />
      <outlinestyle>SolidLine</outlinestyle>
      <outlinewidth>0.1</outlinewidth>
      <fillcolor red="255" blue="0" green="0" />
      <fillpattern>SolidPattern</fillpattern>
      <texturepath></texturepath>
    </symbol>
  </uniquevalue>
  <edittypes>
    <edittype type="0" name="altitude" />
    <edittype type="0" name="basin_code" />
    <edittype type="0" name="basin_name" />
    <edittype type="0" name="danger_level" />
    <edittype type="0" name="datasource" />
    <edittype type="0" name="dist2gr" />
    <edittype type="0" name="ds_date" />
    <edittype type="0" name="gid" />
    <edittype type="0" name="gl_area" />
    <edittype type="0" name="gl_class" />
    <edittype type="0" name="gl_code" />
    <edittype type="0" name="gl_length" />
    <edittype type="0" name="gl_name" />
    <edittype type="0" name="gl_orient" />
    <edittype type="0" name="latitude" />
    <edittype type="0" name="longitude" />
  </edittypes>
  <editform></editform>
  <editforminit></editforminit>
  <annotationform></annotationform>
  <displayfield>basin_name</displayfield>
  <label>1</label>
  <attributeactions/>
  <labelfield>gl_name</labelfield>
  <labelattributes>
    <label fieldname="gl_name" text="" />
    <family fieldname="" name="Arial" />
    <size fieldname="" units="pt" value="12" />
    <bold fieldname="" on="0" />
    <italic fieldname="" on="0" />
    <underline fieldname="" on="0" />
    <strikeout fieldname="" on="0" />
    <color fieldname="" red="0" blue="0" green="0" />
    <x fieldname="" />
    <y fieldname="" />
    <offset x="0" y="0" units="pt" yfieldname="" xfieldname="" />
    <angle fieldname="" value="0" auto="0" />
    <alignment fieldname="" value="center" />
    <buffercolor fieldname="" red="255" blue="255" green="255" />
    <buffersize fieldname="" units="pt" value="1" />
    <bufferenabled fieldname="" on="" />
    <multilineenabled fieldname="" on="" />
    <selectedonly on="" />
  </labelattributes>
  <overlay display="false" type="diagram" >
    <renderer item_interpretation="linear" >
      <diagramitem size="0" value="0" />
      <diagramitem size="0" value="0" />
    </renderer>
    <factory sizeUnits="MM" type="Pie" >
      <wellknownname>Pie</wellknownname>
      <classificationfield>0</classificationfield>
    </factory>
    <scalingAttribute>0</scalingAttribute>
  </overlay>
</qgis>
