;非常原始的一个程序
Pro WriteMeta,Filename=filename,Title=Title,abs_str=abs_str,thumbnail=thumbnail
  xml_str0='<?xml version="1.0" encoding="gb2312"?>'+STRING(13b) + STRING(10b)+$
    '<!--<!DOCTYPE metadata SYSTEM "http://www.esri.com/metadata/esriprof80.dtd">-->'+STRING(13b) + STRING(10b)+$
    '<metadata xml:lang="zh">'+STRING(13b) + STRING(10b)+$
    ;===============ESRI元数据内容
    '<Esri>'+STRING(13b) + STRING(10b)+$
    '<MetaID>{1FA4C2D3-5F47-4809-8A3C-0C1D72709B0A}</MetaID>'+STRING(13b) + STRING(10b)+$
    '<CreaDate>20070129</CreaDate>'+STRING(13b) + STRING(10b)+$
    '<CreaTime>10192400</CreaTime>'+STRING(13b) + STRING(10b)+$
    '<SyncOnce>FALSE</SyncOnce>'+STRING(13b) + STRING(10b)+$
    '<ModDate>20070129</ModDate>'+STRING(13b) + STRING(10b)+$
    '<ModTime>10325500</ModTime>'+STRING(13b) + STRING(10b)+$
    '<SyncDate>20070129</SyncDate>'+STRING(13b) + STRING(10b)+$
    '<SyncTime>10325500</SyncTime>'+STRING(13b) + STRING(10b)+$
    '</Esri>'+STRING(13b) + STRING(10b)+$
    ;===========缩略图========================
    '<Binary>'+STRING(13b) + STRING(10b)+$
    '<Thumbnail>'+STRING(13b) + STRING(10b);+$
  ;'<Data EsriPropertyType="Picture"></Data>'+string(13b) + string(10b)+$
  xml_str1='</Thumbnail>'+STRING(13b) + STRING(10b)+$
    '</Binary>'+STRING(13b) + STRING(10b)+$
    ;===========FGDC=======================
    ;        '<metainfo>'+string(13b) + string(10b)+$
    ;        '<metd Sync="TRUE">20070129</metd>'+string(13b) + string(10b)+$
    ;        '<langmeta Sync="TRUE">zh</langmeta>'+string(13b) + string(10b)+$
    ;        '<metstdn Sync="TRUE">FGDC Content Standards for Digital Geospatial Metadata</metstdn>'+string(13b) + string(10b)+$
    ;        '<metstdv Sync="TRUE">FGDC-STD-001-1998</metstdv>'+string(13b) + string(10b)+$
    ;        '<mettc Sync="TRUE">local time</mettc>'+string(13b) + string(10b)+$
    ;        '<metc>'+string(13b) + string(10b)+$
    ;        '<cntinfo>'+string(13b) + string(10b)+$
    ;        '<cntorgp>'+string(13b) + string(10b)+$
    ;        '<cntper>REQUIRED: The person responsible for the metadata information.</cntper>'+string(13b) + string(10b)+$
    ;        '<cntorg>REQUIRED: The organization responsible for the metadata information.</cntorg>'+string(13b) + string(10b)+$
    ;        '</cntorgp>'+string(13b) + string(10b)+$
    ;        '<cntaddr>'+string(13b) + string(10b)+$
    ;        '<addrtype>REQUIRED: The mailing and/or physical address for the organization or individual.</addrtype>'+string(13b) + string(10b)+$
    ;        '<city>REQUIRED: The city of the address.</city>'+string(13b) + string(10b)+$
    ;        '<state>REQUIRED: The state or province of the address.</state>'+string(13b) + string(10b)+$
    ;        '<postal>REQUIRED: The ZIP or other postal code of the address.</postal>'+string(13b) + string(10b)+$
    ;        '</cntaddr>'+string(13b) + string(10b)+$
    ;        '<cntvoice>REQUIRED: The telephone number by which individuals can speak to the organization or individual.</cntvoice>'+string(13b) + string(10b)+$
    ;        '</cntinfo>'+string(13b) + string(10b)+$
    ;        '</metc>'+string(13b) + string(10b)+$
    ;        '<metextns>'+string(13b) + string(10b)+$
    ;        '<onlink Sync="TRUE">http://www.esri.com/metadata/esriprof80.html</onlink>'+string(13b) + string(10b)+$
    ;        '<metprof Sync="TRUE">ESRI Metadata Profile</metprof>'+string(13b) + string(10b)+$
    ;        '</metextns>'+string(13b) + string(10b)+$
    ;        '</metainfo>'+string(13b) + string(10b)+$
    '<mdDateSt Sync="TRUE">20070129</mdDateSt>'+STRING(13b) + STRING(10b)+$
    ;====================FGDC==============================================
    ;        '<idinfo>'+string(13b) + string(10b)+$
    ;        '<native Sync="TRUE">Microsoft Windows XP Version 5.1 (Build 2600) Service Pack 2; ESRI ArcCatalog 9.0.0.535</native>'+string(13b) + string(10b)+$
    ;        '<descript>'+string(13b) + string(10b)+$
    ;        '<langdata Sync="TRUE">zh</langdata>'+string(13b) + string(10b)+$
    ;        '<abstract>REQUIRED: A brief narrative summary of the data set.</abstract>'+string(13b) + string(10b)+$
    ;        '<purpose>REQUIRED: A summary of the intentions with which the data set was developed.</purpose>'+string(13b) + string(10b)+$
    ;        '</descript>'+string(13b) + string(10b)+$
    ;        '<citation>'+string(13b) + string(10b)+$
    ;        '<citeinfo>'+string(13b) + string(10b)+$
    ;        '<origin>REQUIRED: The name of an organization or individual that developed the data set.</origin>'+string(13b) + string(10b)+$
    ;        '<pubdate>REQUIRED: The date when the data set is published or otherwise made available for release.</pubdate>'+string(13b) + string(10b)+$
    ;        '<title Sync="TRUE">81aug15a.n07-VIg_data_envi.tif</title>'+string(13b) + string(10b)+$
    ;        '<ftname Sync="TRUE">81aug15a.n07-VIg_data_envi.tif</ftname>'+string(13b) + string(10b)+$
    ;        '<geoform Sync="TRUE">remote-sensing image</geoform>'+string(13b) + string(10b)+$
    ;        '<onlink Sync="TRUE">\\WORKSTATION\D$\Gimms\81aug15a.n07-VIg_data_envi.tif</onlink>'+string(13b) + string(10b)+$
    ;        '</citeinfo>'+string(13b) + string(10b)+$
    ;        '</citation>'+string(13b) + string(10b)+$
    ;        '<timeperd>'+string(13b) + string(10b)+$
    ;        '<current>REQUIRED: The basis on which the time period of content information is determined.</current>'+string(13b) + string(10b)+$
    ;        '<timeinfo>'+string(13b) + string(10b)+$
    ;        '<sngdate>'+string(13b) + string(10b)+$
    ;        '<caldate>REQUIRED: The year (and optionally month, or month and day) for which the data set corresponds to the ground.</caldate>'+string(13b) + string(10b)+$
    ;        '</sngdate>'+string(13b) + string(10b)+$
    ;        '</timeinfo>'+string(13b) + string(10b)+$
    ;        '</timeperd>'+string(13b) + string(10b)+$
    ;        '<status>'+string(13b) + string(10b)+$
    ;        '<progress>REQUIRED: The state of the data set.</progress>'+string(13b) + string(10b)+$
    ;        '<update>REQUIRED: The frequency with which changes and additions are made to the data set after the initial data set is completed.</update>'+string(13b) + string(10b)+$
    ;        '</status>'+string(13b) + string(10b)+$
    ;        '<spdom>'+string(13b) + string(10b)+$
    ;        '<bounding>'+string(13b) + string(10b)+$
    ;        '<westbc Sync="TRUE">70.046035</westbc>'+string(13b) + string(10b)+$
    ;        '<eastbc Sync="TRUE">140.082136</eastbc>'+string(13b) + string(10b)+$
    ;        '<northbc Sync="TRUE">54.981950</northbc>'+string(13b) + string(10b)+$
    ;        '<southbc Sync="TRUE">14.909373</southbc>'+string(13b) + string(10b)+$
    ;        '</bounding>'+string(13b) + string(10b)+$
    ;        '<lboundng>'+string(13b) + string(10b)+$
    ;        '<leftbc Sync="TRUE">70.046035</leftbc>'+string(13b) + string(10b)+$
    ;        '<rightbc Sync="TRUE">140.082136</rightbc>'+string(13b) + string(10b)+$
    ;        '<bottombc Sync="TRUE">14.909373</bottombc>'+string(13b) + string(10b)+$
    ;        '<topbc Sync="TRUE">54.981950</topbc>'+string(13b) + string(10b)+$
    ;        '</lboundng>'+string(13b) + string(10b)+$
    ;        '</spdom>'+string(13b) + string(10b)+$
    ;        '<keywords>'+string(13b) + string(10b)+$
    ;        '<theme>'+string(13b) + string(10b)+$
    ;        '<themekt>REQUIRED: Reference to a formally registered thesaurus or a similar authoritative source of theme keywords.</themekt>'+string(13b) + string(10b)+$
    ;        '<themekey>REQUIRED: Common-use word or phrase used to describe the subject of the data set.</themekey>'+string(13b) + string(10b)+$
    ;        '</theme>'+string(13b) + string(10b)+$
    ;        '</keywords>'+string(13b) + string(10b)+$
    ;        '<accconst>REQUIRED: Restrictions and legal prerequisites for accessing the data set.</accconst>'+string(13b) + string(10b)+$
    ;        '<useconst>REQUIRED: Restrictions and legal prerequisites for using the data set after access is granted.</useconst>'+string(13b) + string(10b)+$
    ;        '<natvform Sync="TRUE">Raster Dataset</natvform>'+string(13b) + string(10b)+$
    ;        '</idinfo>'+string(13b) + string(10b)+$
    '<dataIdInfo>'+STRING(13b) + STRING(10b)+$
    '		<envirDesc Sync="TRUE">Microsoft Windows XP Version 5.1 (Build 2600) Service Pack 2; ESRI ArcCatalog 9.0.0.535</envirDesc>'+STRING(13b) + STRING(10b)+$
  '		<dataLang>'+STRING(13b) + STRING(10b)+$
    '		<languageCode Sync="TRUE" value="zh"></languageCode>'+STRING(13b) + STRING(10b)+$
    '		</dataLang>'+STRING(13b) + STRING(10b)+$
    '		<idCitation>'+STRING(13b) + STRING(10b)
  ;******************修改标题***********************
  ;'		<resTitle Sync="TRUE">81aug15a.n07-VIg_data_envi.tif</resTitle>'+string(13b) + string(10b)+$
    
  xml_str2='		<presForm>'+STRING(13b) + STRING(10b)+$
    '		<PresFormCd Sync="TRUE" value="005"></PresFormCd>'+STRING(13b) + STRING(10b)+$
    '		</presForm>'+STRING(13b) + STRING(10b)+$
    '		<resRefDate>'+STRING(13b) + STRING(10b)+$
    '		<refDate>20070101</refDate>'+STRING(13b) + STRING(10b)+$
    '		<refDateType>'+STRING(13b) + STRING(10b)+$
    '		<DateTypCd value="001"></DateTypCd>'+STRING(13b) + STRING(10b)+$
    '</refDateType>'+STRING(13b) + STRING(10b)+$
    '</resRefDate>'+STRING(13b) + STRING(10b)+$
    '<resRefDate>'+STRING(13b) + STRING(10b)+$
    '<refDate>20070101</refDate>'+STRING(13b) + STRING(10b)+$
    '<refDateType>'+STRING(13b) + STRING(10b)+$
    '<DateTypCd value="002"></DateTypCd>'+STRING(13b) + STRING(10b)+$
    '</refDateType>'+STRING(13b) + STRING(10b)+$
    '</resRefDate>'+STRING(13b) + STRING(10b)+$
    '<citRespParty>'+STRING(13b) + STRING(10b)+$
    '<rpIndName>冉有华1</rpIndName>'+STRING(13b) + STRING(10b)+$
    '<rpOrgName>中国科学院寒区旱区环境与工程研究所</rpOrgName>'+STRING(13b) + STRING(10b)+$
    '<rpPosName>助研</rpPosName>'+STRING(13b) + STRING(10b)+$
    '<role><RoleCd value="010"></RoleCd></role>'+STRING(13b) + STRING(10b)+$
    '<rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<cntAddress>'+STRING(13b) + STRING(10b)+$
    '<delPoint>东岗西路320号</delPoint>'+STRING(13b) + STRING(10b)+$
    '<city>兰州</city>'+STRING(13b) + STRING(10b)+$
    '<adminArea>甘肃</adminArea>'+STRING(13b) + STRING(10b)+$
    '<postCode>730000</postCode>'+STRING(13b) + STRING(10b)+$
    '<eMailAdd>ranyh@lzb.ac.cn</eMailAdd>'+STRING(13b) + STRING(10b)+$
    '<country>cn</country>'+STRING(13b) + STRING(10b)+$
    '</cntAddress>'+STRING(13b) + STRING(10b)+$
    '<cntPhone>'+STRING(13b) + STRING(10b)+$
    '<voiceNum>0931-4967741</voiceNum>'+STRING(13b) + STRING(10b)+$
    '<faxNum>0931-4967741</faxNum>'+STRING(13b) + STRING(10b)+$
    '</cntPhone>'+STRING(13b) + STRING(10b)+$
    '</rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '</citRespParty>'+STRING(13b) + STRING(10b)+$
    '</idCitation>'+STRING(13b) + STRING(10b)+$
    '<spatRpType>'+STRING(13b) + STRING(10b)+$
    '<SpatRepTypCd Sync="TRUE" value="002"></SpatRepTypCd>'+STRING(13b) + STRING(10b)+$
    '</spatRpType>'+STRING(13b) + STRING(10b)+$
    '<dataExt>'+STRING(13b) + STRING(10b)+$
    '<geoEle>'+STRING(13b) + STRING(10b)+$
    '<GeoBndBox esriExtentType="native">'+STRING(13b) + STRING(10b)+$
    '<westBL Sync="TRUE">70.046035</westBL>'+STRING(13b) + STRING(10b)+$
    '<eastBL Sync="TRUE">140.082136</eastBL>'+STRING(13b) + STRING(10b)+$
    '<northBL Sync="TRUE">54.98195</northBL>'+STRING(13b) + STRING(10b)+$
    '<southBL Sync="TRUE">14.909373</southBL>'+STRING(13b) + STRING(10b)+$
    '<exTypeCode Sync="TRUE">1</exTypeCode>'+STRING(13b) + STRING(10b)+$
    '</GeoBndBox>'+STRING(13b) + STRING(10b)+$
    '</geoEle>'+STRING(13b) + STRING(10b)+$
    '</dataExt>'+STRING(13b) + STRING(10b)+$
    '<geoBox esriExtentType="decdegrees">'+STRING(13b) + STRING(10b)+$
    '<westBL Sync="TRUE">70.046035</westBL>'+STRING(13b) + STRING(10b)+$
    '<eastBL Sync="TRUE">140.082136</eastBL>'+STRING(13b) + STRING(10b)+$
    '<northBL Sync="TRUE">54.98195</northBL>'+STRING(13b) + STRING(10b)+$
    '<southBL Sync="TRUE">14.909373</southBL>'+STRING(13b) + STRING(10b)+$
    '<exTypeCode Sync="TRUE">1</exTypeCode>'+STRING(13b) + STRING(10b)+$
    '</geoBox>'+STRING(13b) + STRING(10b);+$
  ;摘要部分
  ;'<idAbs>中国GIMMS_NDVI,经纬度投影 NDVI格式(摘要部分请详细)</idAbs>'+string(13b) + string(10b)+$
  xml_str3='<tpCat>'+STRING(13b) + STRING(10b)+$
    '<TopicCatCd value="010"></TopicCatCd>'+STRING(13b) + STRING(10b)+$
    '</tpCat>'+STRING(13b) + STRING(10b)+$
    ;        '<dataScale>'+string(13b) + string(10b)+$
    ;        '<scaleDist>'+string(13b) + string(10b)+$
    ;        '<value>0.072727</value>'+string(13b) + string(10b)+$
    ;        '</scaleDist>'+string(13b) + string(10b)+$
    ;        '</dataScale>'+string(13b) + string(10b)+$
    '<resConst>'+STRING(13b) + STRING(10b)+$
    '<Consts>'+STRING(13b) + STRING(10b)+$
    '<useLimit>为保障数据作者的权益、扩展数据中心的服务、评估数据的应用潜力，'+$
    '请数据使用者在使用数据所产生的研究成果中（包括公开发表的论文、论著、数据产'+$
    '品和未公开发表的研究报告、数据产品等成果），明确注明数据来源和数据作者。对'+$
    '于转载（二次或多次发布）的数据，作者还须注明原始数据来源。'+STRING(13b) + STRING(10b)+$
    '中文发表的成果参考以下规范注明：'+STRING(13b) + STRING(10b)+$
    '数据来源于国家自然科学基金委员会“ 中国西部环境与生态科学数据中心”'+$
    '(http://westdc.westgis.ac.cn)'+STRING(13b) + STRING(10b)+$
    '英文发表的成果依据以下规范注明：'+STRING(13b) + STRING(10b)+$
    'The data set is provided by Environmental &amp; Ecological Science Data Center '+$
  'for West China,National Natural Science Foundation of China (http://westdc.westgis.ac.cn)</useLimit>'+STRING(13b) + STRING(10b)+$
    '</Consts>'+STRING(13b) + STRING(10b)+$
    '</resConst>'+STRING(13b) + STRING(10b)+$
    '</dataIdInfo>'+STRING(13b) + STRING(10b)+$
    '<mdLang>'+STRING(13b) + STRING(10b)+$
    '<languageCode Sync="TRUE" value="zh"></languageCode>'+STRING(13b) + STRING(10b)+$
    '</mdLang>'+STRING(13b) + STRING(10b)+$
    '<mdStanName Sync="TRUE">ISO 19115 Geographic Information - Metadata</mdStanName>'+STRING(13b) + STRING(10b)+$
    '<mdStanVer Sync="TRUE">DIS_ESRI1.0</mdStanVer>'+STRING(13b) + STRING(10b)+$
    '<mdChar>'+STRING(13b) + STRING(10b)+$
    '<CharSetCd Sync="TRUE" value="004"></CharSetCd>'+STRING(13b) + STRING(10b)+$
    '</mdChar>'+STRING(13b) + STRING(10b)+$
    '<mdHrLv>'+STRING(13b) + STRING(10b)+$
    '<ScopeCd Sync="TRUE" value="005"></ScopeCd>'+STRING(13b) + STRING(10b)+$
    '</mdHrLv>'+STRING(13b) + STRING(10b)+$
    '<mdHrLvName Sync="TRUE">dataset</mdHrLvName>'+STRING(13b) + STRING(10b)+$
    ;===============FGDC
    ;        '<distinfo>'+string(13b) + string(10b)+$
    ;        '<resdesc Sync="TRUE">Downloadable Data</resdesc>'+string(13b) + string(10b)+$
    ;        '<stdorder>'+string(13b) + string(10b)+$
    ;        '<digform>'+string(13b) + string(10b)+$
    ;        '<digtinfo>'+string(13b) + string(10b)+$
    ;        '<transize Sync="TRUE">0.511</transize>'+string(13b) + string(10b)+$
    ;        '<dssize Sync="TRUE">0.511</dssize>'+string(13b) + string(10b)+$
    ;        '</digtinfo>'+string(13b) + string(10b)+$
    ;        '</digform>'+string(13b) + string(10b)+$
    ;        '</stdorder>'+string(13b) + string(10b)+$
    ;        '</distinfo>'+string(13b) + string(10b)+$
    '<distInfo>'+STRING(13b) + STRING(10b)+$
    '<distributor>'+STRING(13b) + STRING(10b)+$
    '<distorTran>'+STRING(13b) + STRING(10b)+$
    '<onLineSrc>'+STRING(13b) + STRING(10b)+$
    '<orDesc Sync="TRUE">002</orDesc>'+STRING(13b) + STRING(10b)+$
    '<linkage>ftp://westdc:westdc@ftp.westgis.ac.cn/Gimms/81aug15a.n07-VIg_data_envi.rar</linkage>'+STRING(13b) + STRING(10b)+$
    '<protocol>FTP</protocol>'+STRING(13b) + STRING(10b)+$
    '<orFunct>'+STRING(13b) + STRING(10b)+$
    '<OnFunctCd value="001"></OnFunctCd>'+STRING(13b) + STRING(10b)+$
    '</orFunct>'+STRING(13b) + STRING(10b)+$
    '</onLineSrc>'+STRING(13b) + STRING(10b)+$
    '<transSize Sync="TRUE">0.511</transSize>'+STRING(13b) + STRING(10b)+$
    '<offLineMed>'+STRING(13b) + STRING(10b)+$
    '<medName>'+STRING(13b) + STRING(10b)+$
    '<MedNameCd value="002"></MedNameCd>'+STRING(13b) + STRING(10b)+$
    '</medName>'+STRING(13b) + STRING(10b)+$
    '</offLineMed>'+STRING(13b) + STRING(10b)+$
    '</distorTran>'+STRING(13b) + STRING(10b)+$
    '<distorFormat>'+STRING(13b) + STRING(10b)+$
    '<formatName>ENVI .img(栅格)</formatName>'+STRING(13b) + STRING(10b)+$
    '<formatVer>ENVI4.2</formatVer>'+STRING(13b) + STRING(10b)+$
    '</distorFormat>'+STRING(13b) + STRING(10b)+$
    '<distorCont>'+STRING(13b) + STRING(10b)+$
    '<rpIndName>马明国</rpIndName>'+STRING(13b) + STRING(10b)+$
    '<rpOrgName>中国科学院寒区旱区环境与工程研究所</rpOrgName>'+STRING(13b) + STRING(10b)+$
    '<rpPosName>副研究员</rpPosName>'+STRING(13b) + STRING(10b)+$
    '<rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<cntAddress>'+STRING(13b) + STRING(10b)+$
    '<delPoint>东岗西路320号</delPoint>'+STRING(13b) + STRING(10b)+$
    '<city>兰州</city>'+STRING(13b) + STRING(10b)+$
    '<adminArea>甘肃</adminArea>'+STRING(13b) + STRING(10b)+$
    '<postCode>730000</postCode>'+STRING(13b) + STRING(10b)+$
    '<eMailAdd>mmg@lzb.ac.cn</eMailAdd>'+STRING(13b) + STRING(10b)+$
    '<country>cn</country>'+STRING(13b) + STRING(10b)+$
    '</cntAddress>'+STRING(13b) + STRING(10b)+$
    '<cntPhone>'+STRING(13b) + STRING(10b)+$
    '<voiceNum>0931-4967741</voiceNum>'+STRING(13b) + STRING(10b)+$
    '<faxNum>0931-4967741</faxNum>'+STRING(13b) + STRING(10b)+$
    '</cntPhone>'+STRING(13b) + STRING(10b)+$
    '</rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<role>'+STRING(13b) + STRING(10b)+$
    '<RoleCd value="001"></RoleCd>'+STRING(13b) + STRING(10b)+$
    '</role>'+STRING(13b) + STRING(10b)+$
    '</distorCont>'+STRING(13b) + STRING(10b)+$
    '<distorOrdPrc>'+STRING(13b) + STRING(10b)+$
    '<ordInstr>用户在找到自己所需要的数据信息后，如果是在线数据直接下载，'+$
    '如果是离线数据，填写离线数据申请表， 签订数据共享协议， 寄至“基金委西部数据中心”数据服务组。'+$
    '申请表可在http://westdc.westgis.ac.cn/Documents/application.pdf下载。</ordInstr>'+STRING(13b) + STRING(10b)+$
    '<resFees>免费</resFees>'+STRING(13b) + STRING(10b)+$
    '<ordTurn>一周</ordTurn>'+STRING(13b) + STRING(10b)+$
    '</distorOrdPrc>'+STRING(13b) + STRING(10b)+$
    '</distributor>'+STRING(13b) + STRING(10b)+$
    '</distInfo>'+STRING(13b) + STRING(10b)+$
    '<spdoinfo>'+STRING(13b) + STRING(10b)+$
    '<direct Sync="TRUE">Raster</direct>'+STRING(13b) + STRING(10b)+$
    '<rastinfo>'+STRING(13b) + STRING(10b)+$
    '<rasttype Sync="TRUE">Pixel</rasttype>'+STRING(13b) + STRING(10b)+$
    '<rowcount Sync="TRUE">551</rowcount>'+STRING(13b) + STRING(10b)+$
    '<colcount Sync="TRUE">963</colcount>'+STRING(13b) + STRING(10b)+$
    '<rastxsz Sync="TRUE">0.072727</rastxsz>'+STRING(13b) + STRING(10b)+$
    '<rastysz Sync="TRUE">0.072727</rastysz>'+STRING(13b) + STRING(10b)+$
    '<rastbpp Sync="TRUE">8</rastbpp>'+STRING(13b) + STRING(10b)+$
    '<vrtcount Sync="TRUE">1</vrtcount>'+STRING(13b) + STRING(10b)+$
    '<rastorig Sync="TRUE">Upper Left</rastorig>'+STRING(13b) + STRING(10b)+$
    '<rastcmap Sync="TRUE">FALSE</rastcmap>'+STRING(13b) + STRING(10b)+$
    '<rastcomp Sync="TRUE">None</rastcomp>'+STRING(13b) + STRING(10b)+$
    '<rastband Sync="TRUE">1</rastband>'+STRING(13b) + STRING(10b)+$
    '<rastdtyp Sync="TRUE">pixel codes</rastdtyp>'+STRING(13b) + STRING(10b)+$
    '<rastplyr Sync="TRUE">FALSE</rastplyr>'+STRING(13b) + STRING(10b)+$
    '<rastifor Sync="TRUE">TIFF</rastifor>'+STRING(13b) + STRING(10b)+$
    '</rastinfo>'+STRING(13b) + STRING(10b)+$
    '</spdoinfo>'+STRING(13b) + STRING(10b)+$
    '<spref>'+STRING(13b) + STRING(10b)+$
    '<horizsys>'+STRING(13b) + STRING(10b)+$
    '<cordsysn>'+STRING(13b) + STRING(10b)+$
    '<geogcsn Sync="TRUE">GCS_WGS_1984</geogcsn>'+STRING(13b) + STRING(10b)+$
    '</cordsysn>'+STRING(13b) + STRING(10b)+$
    '<geograph>'+STRING(13b) + STRING(10b)+$
    '<geogunit Sync="TRUE">Decimal degrees</geogunit>'+STRING(13b) + STRING(10b)+$
    '</geograph>'+STRING(13b) + STRING(10b)+$
    '<geodetic>'+STRING(13b) + STRING(10b)+$
    '<horizdn Sync="TRUE">D_WGS_1984</horizdn>'+STRING(13b) + STRING(10b)+$
    '<ellips Sync="TRUE">WGS_1984</ellips>'+STRING(13b) + STRING(10b)+$
    '<semiaxis Sync="TRUE">6378137.000000</semiaxis>'+STRING(13b) + STRING(10b)+$
    '<denflat Sync="TRUE">298.257224</denflat>'+STRING(13b) + STRING(10b)+$
    '</geodetic>'+STRING(13b) + STRING(10b)+$
    '<planar>'+STRING(13b) + STRING(10b)+$
    '<planci>'+STRING(13b) + STRING(10b)+$
    '<plance Sync="TRUE">row and column</plance>'+STRING(13b) + STRING(10b)+$
    '<coordrep>'+STRING(13b) + STRING(10b)+$
    '<absres Sync="TRUE">0.072727</absres>'+STRING(13b) + STRING(10b)+$
    '<ordres Sync="TRUE">0.072727</ordres>'+STRING(13b) + STRING(10b)+$
    '</coordrep>'+STRING(13b) + STRING(10b)+$
    '</planci>'+STRING(13b) + STRING(10b)+$
    '</planar>'+STRING(13b) + STRING(10b)+$
    '</horizsys>'+STRING(13b) + STRING(10b)+$
    '</spref>'+STRING(13b) + STRING(10b)+$
    '<refSysInfo>'+STRING(13b) + STRING(10b)+$
    '<RefSystem>'+STRING(13b) + STRING(10b)+$
    '<refSysID>'+STRING(13b) + STRING(10b)+$
    '<identCode Sync="TRUE">GCS_WGS_1984</identCode>'+STRING(13b) + STRING(10b)+$
    '</refSysID>'+STRING(13b) + STRING(10b)+$
    '</RefSystem>'+STRING(13b) + STRING(10b)+$
    '</refSysInfo>'+STRING(13b) + STRING(10b)+$
    '<spatRepInfo>'+STRING(13b) + STRING(10b)+$
    '<GridSpatRep>'+STRING(13b) + STRING(10b)+$
    '<numDims Sync="TRUE">2</numDims>'+STRING(13b) + STRING(10b)+$
    '<cellGeo>'+STRING(13b) + STRING(10b)+$
    '<CellGeoCd Sync="TRUE" value="002"></CellGeoCd>'+STRING(13b) + STRING(10b)+$
    '</cellGeo>'+STRING(13b) + STRING(10b)+$
    '<tranParaAv Sync="TRUE">1</tranParaAv>'+STRING(13b) + STRING(10b)+$
    '<axDimProps>'+STRING(13b) + STRING(10b)+$
    '<Dimen>'+STRING(13b) + STRING(10b)+$
    '<dimName>'+STRING(13b) + STRING(10b)+$
    '<DimNameTypCd Sync="TRUE" value="002"></DimNameTypCd>'+STRING(13b) + STRING(10b)+$
    '</dimName>'+STRING(13b) + STRING(10b)+$
    '<dimSize Sync="TRUE">963</dimSize>'+STRING(13b) + STRING(10b)+$
    '<dimResol>'+STRING(13b) + STRING(10b)+$
    '<value Sync="TRUE">.072727</value>'+STRING(13b) + STRING(10b)+$
    '<uom>'+STRING(13b) + STRING(10b)+$
    '<UomLength>'+STRING(13b) + STRING(10b)+$
    '<uomName Sync="TRUE">Degree</uomName>'+STRING(13b) + STRING(10b)+$
    '</UomLength>'+STRING(13b) + STRING(10b)+$
    '</uom>'+STRING(13b) + STRING(10b)+$
    '</dimResol>'+STRING(13b) + STRING(10b)+$
    '</Dimen>'+STRING(13b) + STRING(10b)+$
    '<Dimen>'+STRING(13b) + STRING(10b)+$
    '<dimName>'+STRING(13b) + STRING(10b)+$
    '<DimNameTypCd Sync="TRUE" value="001"></DimNameTypCd>'+STRING(13b) + STRING(10b)+$
    '</dimName>'+STRING(13b) + STRING(10b)+$
    '<dimSize Sync="TRUE">551</dimSize>'+STRING(13b) + STRING(10b)+$
    '<dimResol>'+STRING(13b) + STRING(10b)+$
    '<value Sync="TRUE">.072727</value>'+STRING(13b) + STRING(10b)+$
    '<uom>'+STRING(13b) + STRING(10b)+$
    '<UomLength>'+STRING(13b) + STRING(10b)+$
    '<uomName Sync="TRUE">Degree</uomName>'+STRING(13b) + STRING(10b)+$
    '</UomLength>'+STRING(13b) + STRING(10b)+$
    '</uom>'+STRING(13b) + STRING(10b)+$
    '</dimResol>'+STRING(13b) + STRING(10b)+$
    '</Dimen>'+STRING(13b) + STRING(10b)+$
    '</axDimProps>'+STRING(13b) + STRING(10b)+$
    '</GridSpatRep>'+STRING(13b) + STRING(10b)+$
    '</spatRepInfo>'+STRING(13b) + STRING(10b)+$
    '<mdContact>'+STRING(13b) + STRING(10b)+$
    '<rpIndName>冉有华</rpIndName>'+STRING(13b) + STRING(10b)+$
    '<rpOrgName>中国科学院寒区旱区环境与工程研究所</rpOrgName>'+STRING(13b) + STRING(10b)+$
    '<rpPosName>助研</rpPosName>'+STRING(13b) + STRING(10b)+$
    '<rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<cntAddress>'+STRING(13b) + STRING(10b)+$
    '<delPoint>东岗西路320号</delPoint>'+STRING(13b) + STRING(10b)+$
    '<city>兰州</city>'+STRING(13b) + STRING(10b)+$
    '<adminArea>甘肃</adminArea>'+STRING(13b) + STRING(10b)+$
    '<postCode>730000</postCode>'+STRING(13b) + STRING(10b)+$
    '<eMailAdd>ranyh@lzb.ac.cn</eMailAdd>'+STRING(13b) + STRING(10b)+$
    '<country>cn</country>'+STRING(13b) + STRING(10b)+$
    '</cntAddress>'+STRING(13b) + STRING(10b)+$
    '<cntPhone>'+STRING(13b) + STRING(10b)+$
    '<voiceNum>0931-4967741</voiceNum>'+STRING(13b) + STRING(10b)+$
    '<faxNum>0931-4967741</faxNum>'+STRING(13b) + STRING(10b)+$
    '</cntPhone>'+STRING(13b) + STRING(10b)+$
    '</rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<role>'+STRING(13b) + STRING(10b)+$
    '<RoleCd value="010"></RoleCd>'+STRING(13b) + STRING(10b)+$
    '</role>'+STRING(13b) + STRING(10b)+$
    '</mdContact>'+STRING(13b) + STRING(10b)+$
    '</metadata>'
  xml_text=xml_str0+thumbnail+xml_str1+Title+xml_str2+abs_str+xml_str3
  OPENW,lun,filename,/get_lun
  PRINTF,lun,xml_text
  FREE_LUN,lun
End

Function CreateThumb,BMP_Filename
  ;BMP_Filename='d:\gimms\00apr15a.n14-VIg_data_envi.img.bmp'
  data = READ_BMP( BMP_Filename,R,G,B)
  img=CONGRID(data,200,133)
  image=BYTARR(200,3,133)
  image[*,0,*]=img
  image[*,1,*]=img
  image[*,2,*]=img
  ;tv,image
  header='Qk3uNwEAAAAAADYAAAAoAAAAyAAAAIUAAAABABgAAAAAALg3AQAAAAAAAAAAAAAAAAAAAAAA'
  header_byte=[66B,77B,238B,55B,1B,0B,0B,0B,0B,0B,54B,0B,0B,0B,40B,0B,0B,0B,200B,$
    0B,0B,0B,133B,0B,0B,0B,1B,0B,24B,0B,0B,0B,0B,0B,184B,55B,1B,0B,0B,$
    0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B]
  base64_data=REFORM(base64(image),200*133)
  n=N_ELEMENTS(base64_data)
  base64_img=base64(header_byte)
  ;print,'length of header_byte='+string(strlen(base64_img))
  For i=0L,n-1 Do Begin
    base64_img=base64_img+base64_data[i]
  Endfor
  thumbnail='<Data EsriPropertyType="Picture">'
  num=STRLEN(base64_img)/75
  num_mod=STRLEN(base64_img) Mod 75
  ;print,'length of data='+string(200*133*4)
  For k=0L,num-2 Do Begin
    temp_str=STRMID(base64_img,k*75,75)
    thumbnail=thumbnail+temp_str+STRING(13b) + STRING(10b)
  Endfor
  ;print,'lenght of all='+strlen(thumbnail)
  temp_str=STRMID(base64_img,(num-1)*75,num_mod)
  thumbnail=thumbnail+temp_str+STRING(13b) + STRING(10b)+'</Data>'+STRING(13b) + STRING(10b)
  RETURN,thumbnail
End

Pro CreateMeta
  ;设置工作目录
  input_path='D:\Gimms\output\'
  output_path='D:\Gimms\xml\'
  header_str='头文件信息如下：'+STRING(13b) + STRING(10b)+$
    'ENVI'+STRING(13b) + STRING(10b)+$
    'description = {'+STRING(13b) + STRING(10b)+$
    '  File Resize Result, x resize factor: 1.000000, y resize factor: 1.000000.'+STRING(13b) + STRING(10b)+$
    '  [Sat Jan 27 10:44:47 2007]}'+STRING(13b) + STRING(10b)+$
    'samples = 963'+STRING(13b) + STRING(10b)+$
    'lines   = 551'+STRING(13b) + STRING(10b)+$
    'bands   = 1'+STRING(13b) + STRING(10b)+$
    'header offset = 0'+STRING(13b) + STRING(10b)+$
    'file type = ENVI Standard'+STRING(13b) + STRING(10b)+$
    'data type = 4'+STRING(13b) + STRING(10b)+$
    'interleave = bsq'+STRING(13b) + STRING(10b)+$
    'sensor type = Unknown'+STRING(13b) + STRING(10b)+$
    'byte order = 0'+STRING(13b) + STRING(10b)+$
    'x start = 3433'+STRING(13b) + STRING(10b)+$
    'y start = 483'+STRING(13b) + STRING(10b)+$
    'map info = {Geographic Lat/Lon, 1.0000, 1.0000, 70.04603500, 54.98194960, 7.2727000000e-002, 7.2727000000e-002, WGS-84, units=Degrees}'+STRING(13b) + STRING(10b)+$
    'wavelength units = Unknown'+STRING(13b) + STRING(10b)+$
    'values = {'+STRING(13b) + STRING(10b)+$
    ' ndvi, -, -1000, 1000, -1, 1, 0, 0.001}'+STRING(13b) + STRING(10b)+$
    'year = 81'+STRING(13b) + STRING(10b)+$
    'month = aug'+STRING(13b) + STRING(10b)+$
    'date = 15a'+STRING(13b) + STRING(10b)+$
    'program = GIMMS'
  BMP_Filename='d:\gimms\00apr15a.n14-VIg_data_envi.img.bmp'
  ;搜索工作目录下的文件夹
  CD,input_path
  Foldlist=FILE_SEARCH('*',/TEST_DIRECTORY,/FULLY_QUALIFY_PATH,count=num_folder);
  For i=0L,num_folder-1 Do Begin
    CD,foldlist[i]
    filelist=FILE_SEARCH('*.img',count=n)
    ;hrdfile=file_search()
    For j=0L,n-1 Do Begin
      XML_filename=output_path+filelist[j]+'.xml'
      Title='<resTitle Sync="TRUE">'+filelist[j]+'</resTitle>'+STRING(13b) + STRING(10b)
      abs_str='<idAbs>中国GIMMS_NDVI,经纬度投影 NDVI格式(摘要部分请详细).'+header_str+'</idAbs> '
      thumbnail_img=CreateThumb(BMP_Filename)
      thumbnail='<Data EsriPropertyType="Picture">'+thumbnail_img+'</Data>'+STRING(13b) + STRING(10b);+$
      writeMeta,Filename=XML_filename,Title=Title,abs_str=abs_str,thumbnail=thumbnail
    Endfor
  Endfor
  PRINT,'end'
End