;ver 1.0
;Author:wulizong
;E-mail:wulizong@lzb.ac.cn
;�й���ѧԺ�������������빤���о���
;����ʡ�����ж�����·320�� �ʱࣺ730000
;�绰��0931-4967298
;�����������и�ȫ��Χ��GIMMS���ݣ��Բ����й��Ӽ����ݣ����γ�����ͼ��ISO��׼��Ԫ����
;����Ŀ¼�ṹ���������Ŀ¼��ͬ������������޷�����ִ��
;����Ŀ¼/
;        1981/
;        1982/
;        1983/
;        1984/
;        1985/
;        1986/
;         ��/
;        output/
;        output/1981/
;        output/1982/
;        output/1983/
;        output/1984/
;        output/��./
;��������������������Ҫ��IDL+ENVI�Ļ�����ִ��


;****************����Ԫ���ݵĳ���**********************************************
Pro WriteMeta,Filename=filename,Title=Title,abs_str=abs_str,$
    thumbnail=thumbnail,thumb_linkage=thumb_linkage,$
    download=download
  xml_str0='<?xml version="1.0" encoding="gb2312"?>'+STRING(13b) + STRING(10b)+$
    '<!--<!DOCTYPE metadata SYSTEM "http://www.esri.com/metadata/esriprof80.dtd">-->'+STRING(13b) + STRING(10b)+$
    '<metadata xml:lang="zh">'+STRING(13b) + STRING(10b)+$
    ;===============ESRIԪ��������
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
    
    '<mdDateSt Sync="TRUE">20070129</mdDateSt>'+STRING(13b) + STRING(10b)+$
   
    '<dataIdInfo>'+STRING(13b) + STRING(10b)+$
    '		<envirDesc Sync="TRUE">Microsoft Windows XP Version 5.1 (Build 2600) Service Pack 2; ESRI ArcCatalog 9.0.0.535</envirDesc>'+STRING(13b) + STRING(10b)+$
  '		<dataLang>'+STRING(13b) + STRING(10b)+$
    '		<languageCode Sync="TRUE" value="zh"></languageCode>'+STRING(13b) + STRING(10b)+$
    '		</dataLang>'+STRING(13b) + STRING(10b)+$
    '		<idCitation>'+STRING(13b) + STRING(10b)
  ;******************�޸ı���***********************
  ;'		<resTitle Sync="TRUE">81aug15a.n07-VIg_data_envi.tif</resTitle>'+string(13b) + string(10b)+$
    
  xml_str1='		<presForm>'+STRING(13b) + STRING(10b)+$
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
    '<rpIndName>������</rpIndName>'+STRING(13b) + STRING(10b)+$
    '<rpOrgName>�й���ѧԺ�������������빤���о���</rpOrgName>'+STRING(13b) + STRING(10b)+$
    '<rpPosName>����</rpPosName>'+STRING(13b) + STRING(10b)+$
    '<role><RoleCd value="010"></RoleCd></role>'+STRING(13b) + STRING(10b)+$
    '<rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<cntAddress>'+STRING(13b) + STRING(10b)+$
    '<delPoint>������·320��</delPoint>'+STRING(13b) + STRING(10b)+$
    '<city>����</city>'+STRING(13b) + STRING(10b)+$
    '<adminArea>����</adminArea>'+STRING(13b) + STRING(10b)+$
    '<postCode>730000</postCode>'+STRING(13b) + STRING(10b)+$
    '<eMailAdd>wulizong@lzb.ac.cn</eMailAdd>'+STRING(13b) + STRING(10b)+$
    '<country>cn</country>'+STRING(13b) + STRING(10b)+$
    '</cntAddress>'+STRING(13b) + STRING(10b)+$
    '<cntPhone>'+STRING(13b) + STRING(10b)+$
    '<voiceNum>0931-4967298</voiceNum>'+STRING(13b) + STRING(10b)+$
    '<faxNum>0931-4967298</faxNum>'+STRING(13b) + STRING(10b)+$
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
  ;ժҪ����
  ;'<idAbs>�й�GIMMS_NDVI,��γ��ͶӰ NDVI��ʽ(ժҪ��������ϸ)</idAbs>'+string(13b) + string(10b)+$
  xml_str2='<tpCat>'+STRING(13b) + STRING(10b)+$
    '<TopicCatCd value="010"></TopicCatCd>'+STRING(13b) + STRING(10b)+$
    '</tpCat>'+STRING(13b) + STRING(10b)+$
    ;        '<dataScale>'+string(13b) + string(10b)+$
    ;        '<scaleDist>'+string(13b) + string(10b)+$
    ;        '<value>0.072727</value>'+string(13b) + string(10b)+$
    ;        '</scaleDist>'+string(13b) + string(10b)+$
    ;        '</dataScale>'+string(13b) + string(10b)+$
    '<resConst>'+STRING(13b) + STRING(10b)+$
    '<Consts>'+STRING(13b) + STRING(10b)+$
    '<useLimit>Ϊ�����������ߵ�Ȩ�桢��չ�������ĵķ����������ݵ�Ӧ��Ǳ����'+$
    '������ʹ������ʹ���������������о��ɹ��У�����������������ġ����������ݲ�Ʒ'+$
    '��δ����������о����桢���ݲ�Ʒ�ȳɹ�������ȷע��������Դ���������ߡ�'+$
    '����ת�أ����λ��η����������ݣ����߻���ע��ԭʼ������Դ��'+STRING(13b) + STRING(10b)+$
    '���ķ���ĳɹ��ο����¹淶ע����'+STRING(13b) + STRING(10b)+$
    '������Դ�ڹ�����Ȼ��ѧ����ίԱ��" �й�������������̬��ѧ��������"'+$
    '(http://westdc.westgis.ac.cn)'+STRING(13b) + STRING(10b)+$
    'Ӣ�ķ���ĳɹ��������¹淶ע����'+STRING(13b) + STRING(10b)+$
    'The data set is provided by Environmental &amp; Ecological Science Data Center '+$
  'for West China,National Natural Science Foundation of China (http://westdc.westgis.ac.cn)'+STRING(13b) + STRING(10b)+$
    '</useLimit>'+STRING(13b) + STRING(10b)+$
    '</Consts>'+STRING(13b) + STRING(10b)+$
    '</resConst>'+STRING(13b) + STRING(10b)+$
    '</dataIdInfo>'+STRING(13b) + STRING(10b)+$
    '<dqInfo>'+STRING(13b) + STRING(10b)+$
    '<dataLineage>'+STRING(13b) + STRING(10b)+$
    '<statement>������Ȼ��ѧ����ίԱ�ᡰ�й�������������̬��ѧ�������ġ�����ơ������������ġ���'+STRING(13b) + STRING(10b)+$
    '�ǹ�����Ȼ��ѧ����ίԱ���ѧ�����й�������������̬��ѧ�ƻ���(���¼�ơ������ƻ���) '+STRING(13b) + STRING(10b)+$
    '�����½��������ݹ���ƽ̨�����������ռ������������ƻ�����Ŀ���ݲ�����'+STRING(13b) + STRING(10b)+$
    '������������ر��ǻ�����Ŀ�й���Ա�ṩ��ѧ���ݷ��񡣡������������ġ��ܻ���ί��ѧ���쵼��'+STRING(13b) + STRING(10b)+$
    '���й���ѧԺ�������������빤���о������й���ѧԺ�����ѧ����Դ�о����н������С�'+STRING(13b) + STRING(10b)+$
    '</statement> '+STRING(13b) + STRING(10b)+$
    '</dataLineage>'+STRING(13b) + STRING(10b)+$
    '<dqScope>'+STRING(13b) + STRING(10b)+$
    '<scpLvl>'+STRING(13b) + STRING(10b)+$
    '<ScopeCd value="005" /> '+STRING(13b) + STRING(10b)+$
    '</scpLvl>'+STRING(13b) + STRING(10b)+$
    '</dqScope>'+STRING(13b) + STRING(10b)+$
    '</dqInfo>'+STRING(13b) + STRING(10b)+$
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
    
    '<distInfo>'+STRING(13b) + STRING(10b)+$
    '<distributor>'+STRING(13b) + STRING(10b)+$
    '<distorTran>'+STRING(13b) + STRING(10b)+$
    '<onLineSrc>'+STRING(13b) + STRING(10b)+$
    '<orDesc Sync="TRUE">002</orDesc>'+STRING(13b) + STRING(10b);+$
  ;���ص�ַ
  ;        '<linkage>ftp://westdc:westdc@ftp.westgis.ac.cn/Gimms/81aug15a.n07-VIg_data_envi.rar</linkage>'+string(13b) + string(10b)+$
  xml_str3='<protocol>FTP</protocol>'+STRING(13b) + STRING(10b)+$
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
    '<formatName>ENVI .img(դ��)</formatName>'+STRING(13b) + STRING(10b)+$
    '<formatVer>ENVI4.2</formatVer>'+STRING(13b) + STRING(10b)+$
    '</distorFormat>'+STRING(13b) + STRING(10b)+$
    '<distorCont>'+STRING(13b) + STRING(10b)+$
    '<rpIndName>������</rpIndName>'+STRING(13b) + STRING(10b)+$
    '<rpOrgName>�й���ѧԺ�������������빤���о���</rpOrgName>'+STRING(13b) + STRING(10b)+$
    '<rpPosName>���о�Ա</rpPosName>'+STRING(13b) + STRING(10b)+$
    '<rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<cntAddress>'+STRING(13b) + STRING(10b)+$
    '<delPoint>������·320��</delPoint>'+STRING(13b) + STRING(10b)+$
    '<city>����</city>'+STRING(13b) + STRING(10b)+$
    '<adminArea>����</adminArea>'+STRING(13b) + STRING(10b)+$
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
    '<ordInstr>�û����ҵ��Լ�����Ҫ��������Ϣ���������������ֱ�����أ�������������ݣ�'+STRING(13b) + STRING(10b)+$
    '��д������������� ǩ�����ݹ���Э�飬 ����"����ί������������"���ݷ����顣'+STRING(13b) + STRING(10b)+$
    '��������http://westdc.westgis.ac.cn/Documents/application.pdf���ء�'+STRING(13b) + STRING(10b)+$
    '��ϵ��ʽ:'+STRING(13b) + STRING(10b)+$
    '�й���ѧԺ�������������빤���о���'+STRING(13b) + STRING(10b)+$
    'ң���������Ϣ��ѧ�о���'+STRING(13b) + STRING(10b)+$
    '�й�������������̬��ѧ��������'+STRING(13b) + STRING(10b)+$
    '���ݷ�����'+STRING(13b) + STRING(10b)+$
    '��ַ������ʡ�����ж�����·320 �� �ʱࣺ730000'+STRING(13b) + STRING(10b)+$
    '���ݷ�����ϵ�ˣ��� ����Ƚ�л����� ��'+STRING(13b) + STRING(10b)+$
    '�绰��0931-4967741��Ƚ�л������̣���4967234����������4967298�������ڡ����Σ�'+STRING(13b) + STRING(10b)+$
    '���棺0931-8279161��4967235'+STRING(13b) + STRING(10b)+$
    '���䣺ranyh@lzb.ac.cn , leung@lzb.ac.cn , wjian@lzb.ac.cn'+STRING(13b) + STRING(10b)+$
    '��ַ��http://westdc.westgis.ac.cn'+STRING(13b) + STRING(10b)+$
    '</ordInstr>'+STRING(13b) + STRING(10b)+$
    '<resFees>���</resFees>'+STRING(13b) + STRING(10b)+$
    '<ordTurn>һ��</ordTurn>'+STRING(13b) + STRING(10b)+$
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
    '<rpIndName>Ƚ�л�</rpIndName>'+STRING(13b) + STRING(10b)+$
    '<rpOrgName>�й���ѧԺ�������������빤���о���</rpOrgName>'+STRING(13b) + STRING(10b)+$
    '<rpPosName>����</rpPosName>'+STRING(13b) + STRING(10b)+$
    '<rpCntInfo>'+STRING(13b) + STRING(10b)+$
    '<cntAddress>'+STRING(13b) + STRING(10b)+$
    '<delPoint>������·320��</delPoint>'+STRING(13b) + STRING(10b)+$
    '<city>����</city>'+STRING(13b) + STRING(10b)+$
    '<adminArea>����</adminArea>'+STRING(13b) + STRING(10b)+$
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
    ;===========����ͼ========================
    '<Binary>'+STRING(13b) + STRING(10b)+$
    '<Thumbnail>'+STRING(13b) + STRING(10b);+$
  ;'<Data EsriPropertyType="Picture"></Data>'+string(13b) + string(10b)+$
  xml_str4='</Thumbnail>'+STRING(13b) + STRING(10b)+$
    '</Binary>'+STRING(13b) + STRING(10b)+$
    '</metadata>'
  xml_text=xml_str0+Title+xml_str1+abs_str+xml_str2+download+xml_str3+thumbnail+thumb_linkage+xml_str4
  OPENW,lun,filename,/get_lun
  PRINTF,lun,xml_text
  FREE_LUN,lun
End
;*********************����Base64��������ͼ�ĳ���***************************
Function CreateThumb,Data_byte
  image=BYTARR(3,200,133)
  image[0,*,*]=Data_byte
  image[1,*,*]=Data_byte
  image[2,*,*]=Data_byte
  ;header='Qk3uNwEAAAAAADYAAAAoAAAAyAAAAIUAAAABABgAAAAAALg3AQAAAAAAAAAAAAAAAAAAAAAA'
  header_byte=[66B,77B,238B,55B,1B,0B,0B,0B,0B,0B,54B,0B,0B,0B,40B,0B,0B,0B,200B,$
    0B,0B,0B,133B,0B,0B,0B,1B,0B,24B,0B,0B,0B,0B,0B,184B,55B,1B,0B,0B,$
    0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B,0B]   ;size=54byte
  base64_data=base64(image)
  base64_img='Qk3uNwEAAAAAADYAAAAoAAAAyAAAAIUAAAABABgAAAAAALo3AQASCwAAEgsAAAAAAAAAAAAA'
  
  For j=0L,133-1 Do Begin
    For i=0L,200-1 Do Begin
      base64_img=base64_img+base64_data[i,j]
    Endfor
  Endfor
  ;	FOR i=0L,n-1 DO BEGIN
  ;		base64_img=base64_img+base64_data[i]
  ;	ENDFOR
  thumbnail_meta=''
  num=STRLEN(base64_img)/76                                   ;����ж�����
  num_mod=STRLEN(base64_img) Mod 76                           ;���һ�е��ַ���
  For k=0L,num-1 Do Begin
    temp_str=STRMID(base64_img,k*76,76)
    thumbnail_meta=thumbnail_meta+temp_str+STRING(13b) + STRING(10b)
  Endfor
  
  thumbnail_meta=thumbnail_meta+STRMID(base64_img,num*76,num_mod)+'AAA='
  RETURN,thumbnail_meta
End

;******************************************������**********************************************

Pro Gimms_Tool                                  ;�ļ����������������ͬ�������޷�����
  Compile_opt strictarr                       ;�ɱ������������ʶ��ENVI����
  ;!except=2                                  ;�����ѧ����
  ;===============���ó������(Start)===============================================
  ;=====���ù���Ŀ¼·��=====
  Inpath='d:\gimms\data'                   ;�޸Ĵ˴��ı乤��·��
  ;=====��������ļ�·��=====
  Outpath='d:\Gimms\output\'               ;��Ҫ�ֹ�������Ŀ¼
  ;=====��������ͼ���·��===
  Thumbnail_Path='d:\Gimms\thumbnail\'
  ;=====����Ԫ���ݴ��·��=====            ;��Ҫ�ֹ�������Ŀ¼
  Meta_Path='d:\Gimms\XML\'
  ;=====�����������ͼ���Ϻ����ͼ��λ��====================
  Nanhaifile='D:\DataTools\GLIMMS\nanhai.img'
  ;=====����ENVI���ݵ�ͷ�ļ�==================================
  ;��ͷ�ļ���Ϣ��ͳһд�뵽Ԫ���ݵ�ժҪ��
  header_str='����ͷ�ļ���Ϣ���£�'+STRING(13b) + STRING(10b)+$
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
    'values = {ndvi, -, -1000, 1000, -1, 1, 0, 0.001}'+STRING(13b) + STRING(10b)+$
    ;						'year = 81'+string(13b) + string(10b)+$
    ;						'month = aug'+string(13b) + string(10b)+$
    ;						'date = 15a'+string(13b) + string(10b)+$
    'program = GIMMS'
  ;===============���ó������(END)===============================================
  envi, /restore_base_save_files           ;�ָ�ENVI sav�ļ�
  envi_batch_init, log_file='batch.txt'    ;��ʼ������ģʽ
  ;����GIMMS����
  CD,Inpath                                ;���빤��Ŀ¼
  Foldlist=FILE_SEARCH('*',/TEST_DIRECTORY,/FULLY_QUALIFY_PATH,count=num_folder);�����ļ���
  For i=0,num_folder-1 Do Begin
    ;������ļ����д�����Ŀ¼
    CD,Outpath                               ;��������ļ���Ŀ¼
    pathpos=STRPOS(foldlist[i],'\',/REVERSE_SEARCH)
    Subdir=STRMID(foldlist[i],pathpos+1,4)
    FILE_MKDIR, Subdir    									 ;������ļ����д�����Ŀ¼
    ;
    CD,Foldlist[i]
    filelist=FILE_SEARCH('*.img',count=n)    ;��ȡͼ���ļ�����
    For j=0,n-1 Do Begin
      filename=foldlist[i]+'\'+filelist[j]
      envi_open_file, filename, r_fid=fid
      If (fid Eq -1) Then Begin
        envi_batch_exit
        RETURN
      Endif
      envi_file_query, fid, ns=ns, nl=nl, nb=nb
      dims = [-1, 0, ns-1, 0, nl-1]
      pos  = LINDGEN(nb)
      out_name = outpath+STRMID(foldlist[i],pathpos+1,4)+'\'+filelist[j]
      ;=================�޸Ĵ˴�����Լ�����Ȥ������====================
      west_x=70           ;����     ��λ����
      south_y=15          ;����
      east_x=140          ;����
      north_y=55          ;����
      ;============���и�������Ϣ====================
      ;������Ϣ��ͷ�ļ��ж�ȡ,ע����ʼ��ľ�γ�Ȳ���-180�Ⱥ�-90��
      resolution=0.07272                     ;�ֱ���,��λ:��
      start_x=-179.55302900                  ;����     ��λ����
      start_y=90.03636360                    ;����
      ;ENVI/IDL��ʼ���Ǵ����Ͻǿ�ʼ��
      start_sample=ROUND((west_x-start_x)/resolution)
      end_sample=ROUND((east_x-start_x)/resolution)
      start_line=ROUND((start_y-north_y)/resolution)
      end_line=ROUND((start_y-south_y)/resolution)
      ;ִ���и����,�˴�����ENVI����
      envi_doit, 'resize_doit',$
        fid=fid, pos=pos, dims=[-1,start_sample,end_sample,start_line,end_line],$
        interp=0, rfact=[1,1],out_name=out_name, r_fid=r_fid
      ;======�������ͼ=============
      ;��ȡͼ������
      envi_file_query, r_fid, ns=ns, nl=nl, nb=nb
      dims = [-1, 0, ns-1, 0, nl-1]
      pos  = LINDGEN(nb)
      data = ENVI_GET_DATA(fid=r_fid,dims=dims,pos=pos)
      thumbnail_filename=thumbnail_path+filelist[j]+'.jpg'
      ;��ͼ���豸'Z'�л�ͼ
      current_device=!D.NAME
      SET_PLOT, 'Z'
      DEVICE,SET_RESOLUTION=[ns,nl],Z_BUFFERING=0,SET_FONT='Times Bold',SET_CHARACTER_SIZE=[10,15]
      
      ERASE,color=255
      MAP_SET,limit=[15,70,55,140],title=filelist[j]+'!C',$
        xmargin=[3,3],ymargin=[3,5] ;������ʾ��Χ
      image=MAP_IMAGE(data,x0,y0,xsize,ysize,latmin=15,lonmin=70,latmax=55,lonmax=140,compress=1)
      TV,image,x0,y0,xsize=xsize,ysize=ysize,order=1
      MAP_CONTINENTS,/countries        ;�����磨�޺����ߣ�
      MAP_GRID,/BOX_AXES               ;����γ������
      ;�Ϻ����λ���Ѿ���ǰ������
      ;nanhaifile='D:\DataTools\GLIMMS\nanhai.img'
      ;��ȡ�Ϻ�������ݲ�������豸'Z'��
      envi_open_file, nanhaifile, r_fid=fid
      envi_file_query,fid, ns=ns, nl=nl, nb=nb
      dims = [-1, 0, ns-1, 0, nl-1]
      pos  = LINDGEN(nb)
      nanhai_data = ENVI_GET_DATA(fid=fid,dims=dims,pos=pos)
      nanhai_image=MAP_IMAGE(nanhai_data,x0,y0,xsize,ysize,latmin=15,lonmin=140-(15*0.8),latmax=30,lonmax=140,compress=1)
      TV,nanhai_image,x0,y0,xsize=xsize,ysize=ysize,order=1
      XYOUTS,70,11,'Environmental and Ecological Science Data Center For West China      (http://westdc.westgis.ac.cn)';,color=1,charsize=1;,CHARTHICK=2
      ;������豸�ж�ȡ����
      TVImage=TVRD()
      ;�ر�ͼ������豸
      DEVICE, /CLOSE
      SET_PLOT, current_device
      ;�������ͼ��JPG��ʽ
      WRITE_JPEG, thumbnail_filename, TVImage, ORDER=0
      ;=========����Ԫ����============================
      ;Ԫ���ݵ����·����Ԫ�����ļ���
      XML_filename=Meta_Path+STRMID(filelist[j],0,(STRLEN(filelist[j])-3))+'xml'
      ;������.�ĵ�һ��λ��
      ;��gallery.westgis.ac.cn��"."��"_"������
      point_pos=STRPOS(filelist[j],'.')
      year=STRMID(filelist[j],0,2)
      If year Lt 80 Then Begin
        year='20'+year+'��'
      Endif Else Begin
        year='19'+year+'��'
      Endelse
      month=STRMID(filelist[j],2,3)
      Case month Of
        'jan': month='1'+'��'
        'feb': month='2'+'��'
        'mar': month='3'+'��'
        'apr': month='4'+'��'
        'may': month='5'+'��'
        'jun': month='6'+'��'
        'jul': month='7'+'��'
        'aug': month='8'+'��'
        'sep': month='9'+'��'
        'oct': month='10'+'��'
        'nov': month='11'+'��'
        'dec': month='12'+'��'
      Endcase
      day=STRMID(filelist[j],5,2)+'�� '
      band_name=STRMID(filelist[j],7,1)+'����'
      ;Ԫ���ݱ���
      Gimms_Name=STRMID(filelist[j],0,point_pos)
      Title='<resTitle Sync="TRUE">GIMMS NDVI����('+year+month+day+band_name+')</resTitle>'+STRING(13b) + STRING(10b)
      ;Ԫ����ժҪ
      abs_str='<idAbs>�й�GIMMS NDVI����.�����ݿ�����ENVI����򿪲�ת��������Ҫ�ĸ�ʽ.(ժҪ��������ϸ).'+$
        STRING(13b) + STRING(10b)+header_str+'</idAbs>'
      ;Ԫ��������ͼ��Base64����
      Data_Byte=ROTATE(CONGRID(data,200,133),7)                       ;�������ͼ�Ĵ�СΪ200*133
      ;			window,0,xsize=200,ysize=133
      ;			tv,data_byte;,/order
      Thumbnail_img=CreateThumb(Data_Byte)
      Thumbnail='<Data EsriPropertyType="Picture">'+thumbnail_img+'</Data>'+STRING(13b) + STRING(10b)
      
      thumb_Linkage='<Linkage>http://gallery.westgis.ac.cn/view/westdc/Thumbnail/RSImage/GIMMS/'+$
        STRMID(filelist[j],0,point_pos)+'_'+$
        STRMID(filelist[j],point_pos+1,(STRLEN(filelist[j])-5-point_pos))+$
        '_img.jpg.html</Linkage>'
      download='<linkage>ftp://westdc:westdc@ftp.westgis.ac.cn/RSData/Gimms/'+$
        STRMID(filelist[j],0,(STRLEN(filelist[j])-4))+'.rar'+$
        '</linkage> '
      WriteMeta,Filename=XML_filename,Title=Title,abs_str=abs_str,$
        thumbnail=thumbnail,thumb_linkage=thumb_linkage,download=download
        
    Endfor
  Endfor
  
  Envi_batch_exit     ;�˳�������ģʽ
  PRINT,'The Programe is End'
End

