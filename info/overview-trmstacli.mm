<map version="1.0.1">
<!-- To view this file, download free mind mapping software FreeMind from http://freemind.sourceforge.net -->
<node BACKGROUND_COLOR="#ffa100" CREATED="1410728528963" ID="ID_338342650" MODIFIED="1423251770168" STYLE="bubble" TEXT="trmstacli">
<font BOLD="true" NAME="SansSerif" SIZE="12"/>
<node CREATED="1410728609587" ID="ID_881067283" MODIFIED="1410737755738" POSITION="right" STYLE="bubble" TEXT="getkol(wait)">
<edge STYLE="bezier"/>
<cloud COLOR="#fff2b7"/>
<node BACKGROUND_COLOR="#ffd1ce" CREATED="1410728661672" ID="ID_1107959630" MODIFIED="1411274369641" STYLE="bubble" TEXT="[JEDNOPOKAZ]">
<cloud/>
<node CREATED="1410728993673" ID="ID_1648049992" MODIFIED="1410728998623" TEXT="for s in stacje:"/>
<node CREATED="1410728677968" ID="ID_1985863268" MODIFIED="1410728896680" STYLE="bubble" TEXT="download"/>
<node CREATED="1410728695568" ID="ID_877140011" MODIFIED="1410728896680" STYLE="bubble" TEXT="pokaz"/>
</node>
<node BACKGROUND_COLOR="#ffe0e0" CREATED="1410728835524" ID="ID_1700166341" MODIFIED="1411274429911" STYLE="bubble" TEXT="[MULTIPOKAZ]">
<cloud/>
<node CREATED="1410728700247" ID="ID_941437364" MODIFIED="1410728929794" STYLE="bubble" TEXT="for s in stacje: download"/>
<node CREATED="1410728718927" ID="ID_199597416" MODIFIED="1410728929793" STYLE="bubble" TEXT="jednoczenie">
<node CREATED="1410729333606" ID="ID_1847621573" MODIFIED="1410729340970" TEXT="multipokaz /zapisuj razem"/>
</node>
</node>
</node>
<node BACKGROUND_COLOR="#dbe1ff" COLOR="#000000" CREATED="1410728619449" ID="ID_95138420" MODIFIED="1410729647449" POSITION="left" STYLE="bubble" TEXT="getjednoczesnie">
<cloud COLOR="#9dff84"/>
<node CREATED="1410729050474" ID="ID_1993252907" MODIFIED="1410737680919" TEXT="[JEDNOPOKAZ]">
<cloud COLOR="#e4ffbd"/>
<node CREATED="1410729202996" ID="ID_1303016540" MODIFIED="1410729210288" TEXT="[wielow&#x105;tkowo] download"/>
<node BACKGROUND_COLOR="#ffffee" CREATED="1410729254913" ID="ID_1209049022" MODIFIED="1410737698115" TEXT="[WARIANT]">
<node CREATED="1410729260994" ID="ID_1716039738" MODIFIED="1410729380543" TEXT="[kolejno]">
<cloud/>
<node CREATED="1410729312047" ID="ID_1293519080" MODIFIED="1410729314008" TEXT="listuj">
<node CREATED="1410729314009" ID="ID_1934153710" MODIFIED="1410729321290" TEXT="pokaz"/>
</node>
</node>
<node CREATED="1410729273249" ID="ID_1008771715" MODIFIED="1410729383514" TEXT="[jak najszybciej, od razu po otrzymaniu danych]">
<cloud/>
<node CREATED="1410729306704" ID="ID_1580407034" MODIFIED="1410729308731" TEXT="pokaz"/>
</node>
</node>
</node>
<node CREATED="1410729152454" ID="ID_1018413617" MODIFIED="1410737734898" TEXT="[MULTIPOKAZ]">
<cloud COLOR="#dbf0d9"/>
<node CREATED="1410729160014" ID="ID_711571193" MODIFIED="1410729165845" TEXT="[wielow&#x105;tkowo] download"/>
<node CREATED="1410729177285" ID="ID_792586224" MODIFIED="1410729179944" TEXT="multipokaz"/>
</node>
</node>
<node CREATED="1423251771277" ID="ID_1050878825" MODIFIED="1423251775420" POSITION="right" TEXT="argparsing">
<node CREATED="1423251775889" ID="ID_1572818634" MODIFIED="1423251848644" TEXT="dzi&#x15b;">
<node CREATED="1423251871677" ID="ID_1803830026" MODIFIED="1423251875877" TEXT="char">
<node CREATED="1423251875878" ID="ID_1620854156" MODIFIED="1423251878040" TEXT="safe"/>
<node CREATED="1423251878901" ID="ID_1227750303" MODIFIED="1423251881001" TEXT="national"/>
</node>
<node CREATED="1423251884606" ID="ID_165327639" MODIFIED="1423251886285" TEXT="lang">
<node CREATED="1423251886286" ID="ID_1652951208" MODIFIED="1423251894721" TEXT="en"/>
<node CREATED="1423251904231" ID="ID_1063102157" MODIFIED="1423251905722" TEXT="eo"/>
<node CREATED="1423251906031" ID="ID_1218310131" MODIFIED="1423251907442" TEXT="pl"/>
<node CREATED="1423251907661" ID="ID_1225907504" MODIFIED="1423251908346" TEXT="de"/>
</node>
<node CREATED="1423251928760" ID="ID_1900819896" MODIFIED="1423251938528" TEXT="-t*">
<node CREATED="1423251911551" ID="ID_1315009044" MODIFIED="1423251926099" TEXT="-t, --waitbetweenloops"/>
<node CREATED="1423251940065" ID="ID_1847719251" MODIFIED="1423251951036" TEXT="-td, --defwaitbetweenloops"/>
<node CREATED="1423251951609" ID="ID_760705370" MODIFIED="1423251958180" TEXT="-ts, --singlecheck"/>
</node>
<node CREATED="1423251959537" ID="ID_51639137" MODIFIED="1423251962858" TEXT="-s*">
<node CREATED="1423251962858" ID="ID_1726876619" MODIFIED="1423251969861" TEXT="-sa, --allstations"/>
<node CREATED="1423251970106" ID="ID_577061163" MODIFIED="1423251977861" TEXT="-sd, --defstations"/>
<node CREATED="1423251979466" ID="ID_1637818003" MODIFIED="1423252004334" TEXT="-s 1 -s 2 -s 3 ..."/>
</node>
<node CREATED="1423252018836" ID="ID_10689553" MODIFIED="1423252023437" TEXT="-p*">
<node CREATED="1423252051686" ID="ID_1505244494" MODIFIED="1423252058081" TEXT="-pr razem"/>
<node CREATED="1423252058406" ID="ID_277920966" MODIFIED="1423252065769" TEXT="-pl long"/>
<node CREATED="1423252066190" ID="ID_1161528783" MODIFIED="1423252071570" TEXT="-pu user"/>
<node CREATED="1423252134850" ID="ID_1657978023" MODIFIED="1423252144365" TEXT="-pk komp"/>
<node CREATED="1423252144610" ID="ID_1726531808" MODIFIED="1423252149333" TEXT="-pc compressed"/>
<node CREATED="1423252149579" ID="ID_190528992" MODIFIED="1423252154950" TEXT="-pm minim"/>
<node CREATED="1423252155322" ID="ID_1187343837" MODIFIED="1423252161878" TEXT="-prk razkomp"/>
<node CREATED="1423252163675" ID="ID_1937260581" MODIFIED="1423252166214" TEXT="-pn none"/>
<node CREATED="1423252167920" ID="ID_771112490" MODIFIED="1423252171062" TEXT="-pd def"/>
<node CREATED="1423252552669" ID="ID_1364362482" MODIFIED="1423252627978" TEXT="-pf*">
<node CREATED="1423252023438" ID="ID_1726616943" MODIFIED="1423252038864" TEXT="-pfc fulladrlangchosen"/>
<node CREATED="1423252039085" ID="ID_1360062282" MODIFIED="1423252051313" TEXT="-pfl fulladrlanglocal"/>
</node>
<node CREATED="1423252574151" ID="ID_954554980" MODIFIED="1423252640244" TEXT="-pa*">
<node CREATED="1423252071910" ID="ID_912794087" MODIFIED="1423252086066" TEXT="-pac adresadrlangchosen"/>
<node CREATED="1423252081550" ID="ID_1030750786" MODIFIED="1423252099963" TEXT="-pal adresadrlandlocal"/>
</node>
<node CREATED="1423252585911" ID="ID_735481909" MODIFIED="1423252588210" TEXT="-pt*">
<node CREATED="1423252101071" ID="ID_1624303995" MODIFIED="1423252112371" TEXT="-ptc tabelaadrlangchosen"/>
<node CREATED="1423252113160" ID="ID_1362517921" MODIFIED="1423252138958" TEXT="-ptl tabelaadrlanglocal"/>
</node>
</node>
<node CREATED="1423252182355" ID="ID_1395907864" MODIFIED="1423252188084" TEXT="-b*">
<node CREATED="1423252188085" ID="ID_1999305890" MODIFIED="1423252199656" TEXT="-bf debug full"/>
<node CREATED="1423252200029" ID="ID_566676032" MODIFIED="1423252206760" TEXT="-by debusyes"/>
<node CREATED="1423252207165" ID="ID_1170707605" MODIFIED="1423252213184" TEXT="-bn debuf no"/>
<node CREATED="1423252213502" ID="ID_1565568621" MODIFIED="1423252217753" TEXT="-bd debugdef"/>
</node>
<node CREATED="1423252226726" ID="ID_492569956" MODIFIED="1423252230878" TEXT="-w*">
<node CREATED="1423252230879" ID="ID_867757083" MODIFIED="1423252244015" TEXT="-wc*">
<node CREATED="1423252244015" ID="ID_1390357769" MODIFIED="1423252252667" TEXT="-wck*">
<node CREATED="1423252289064" ID="ID_524839769" MODIFIED="1423252310853" TEXT="-wcks tocsvkolsinglefile"/>
<node CREATED="1423252314234" ID="ID_1607198394" MODIFIED="1423252349064" TEXT="-wckvt tocsvkolmultiwaitbetweenloopsvolumefile"/>
<node CREATED="1423252350076" ID="ID_1050593528" MODIFIED="1423252387107" TEXT="-wckvc tocsvkolmulticountvolumefile"/>
</node>
<node CREATED="1423252253111" ID="ID_1297743952" MODIFIED="1423252258059" TEXT="-wcr*">
<node CREATED="1423252289064" ID="ID_1146446163" MODIFIED="1423252415202" TEXT="-wcrs tocsrazlsinglefile"/>
<node CREATED="1423252314234" ID="ID_148566022" MODIFIED="1423252445700" TEXT="-wcrvt tocsvrazmultiwaitbetweenloopsvolumefile"/>
<node CREATED="1423252350076" ID="ID_616682685" MODIFIED="1423252449588" TEXT="-wcrvc tocsvrazmulticountvolumefile"/>
</node>
</node>
<node CREATED="1423252390806" ID="ID_581504351" MODIFIED="1423252393801" TEXT="-wn no"/>
</node>
<node CREATED="1423252468057" ID="ID_463255592" MODIFIED="1423252507348" TEXT="-g*">
<node CREATED="1423252471251" ID="ID_490049744" MODIFIED="1423252478813" TEXT="-gj getjednoczesnie"/>
<node CREATED="1423252479369" ID="ID_313548182" MODIFIED="1423252487037" TEXT="-gk getkolejno"/>
<node CREATED="1423252487482" ID="ID_1966982681" MODIFIED="1423252496422" TEXT="-gkw getkolejnowait"/>
<node CREATED="1423252498427" ID="ID_1029584622" MODIFIED="1423252501430" TEXT="-gd def"/>
</node>
<node CREATED="1423252508636" ID="ID_623722078" MODIFIED="1423252513452" TEXT="-i*">
<node CREATED="1423252513453" ID="ID_567025112" MODIFIED="1423252524959" TEXT="-in instantly"/>
<node CREATED="1423252525461" ID="ID_529808500" MODIFIED="1423252531064" TEXT="-iw instawrite"/>
<node CREATED="1423252531597" ID="ID_1879864671" MODIFIED="1423252536824" TEXT="-id instadisp"/>
</node>
</node>
<node CREATED="1423251778289" ID="ID_1260147066" MODIFIED="1423251858112" TEXT="w przysz&#x142;o&#x15b;ci"/>
</node>
</node>
</map>
