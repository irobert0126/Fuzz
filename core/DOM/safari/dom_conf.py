
def load_dom_attr():
  return DOM_ATTR
  
def load_must_have_attr():
  return DOM_Must_Have_Attrib
  
def load_dom_css():
  return DOM_CSS

def load_dom_tags():
  return DOM_Tags
#########################################################################################################################
DOM_Tags = [
    "keygen",
    "link",
    "marquee",
    "nolayer","noscript",
    # Text-level semantics
    "a", "address","article","aside", "b", "blockquote","big",
    "caption", "center", "cite", "code", "em",
    "figure", "figcaption",
    "del","dl","dt","dd", "details", "dfn",
    "label", "layer", "legend", "listing",
    "hgroup","h1","h2","h3","h4","h5","h6","hr", "i", "mark", "nav", "pre", "p", "q",
    "samp", "small", "strong", "var", "kbd",
    "s", "section", "summary", "sub", "sup", "strike", "tt", "title", "u", "wbr", "xmp",
    "ruby", "rt", "rp",
    "ol", "li", "ul",
    "main","header","footer",
    "bdo",              #*dir=rtl*/
    "acronym", "abbr",  #*title=".."*/
    "ins",              #*datetime="" cite=""*/
    "textarea",         #*rows="4" cols="50"*/
    "br",
    "span",
    "div",
    "area",
    "img",              #*src=""*/
    "input", "output"
    "meter",            #*value="" min="" max="" | value="0.5"*/
    "button",
    "option",           #*value=""*/
    "basefont",         #* color face size */
    "font",             #* color face size */
    "progress",         #* value="" max=""*/
    "fieldset",
    "html", "head", "body", "meta",
    "canvas",
    "iframe",
]
#########################################################################################################################
DOM_ATTR = {
  "tmp_color"    : {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1},

  "abbr"        : {"def":1},
  "accept"      : {"text/h323":1,"audio/aiff":1,"audio/basic":1,"application/octet-stream":1,"text/plain":1},
  "acceptCharset" : {"UNKNOWN":1,"DOS-720":1,"windows-1257":1,"EUC-CN":1,"gb2312":1,"x-mac-chinesesimp":1},
  "accessKey"   : {"0":1,"AA":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "action"      : {"http://localhost:12345":1,"https://localhost":1,"smb://a.b.c":1,"ftp://123":1,"#1234":1},
  "activeElement" : {"?":1},
  "align"       : {"left":1,"absbottom":1,"absmiddle":1,"baseline":1,"bottom":1,"middle":1,"right":1,"texttop":1,"top":1,"center":1,"justify":1},
  "aLink"       : {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1},
  "alinkColor"  : {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1}, # a:link { color: red; }
  "alt"         : {"0":1,"AA":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "archive"     : {"http://localhost:12345":1,"https://localhost":1,"smb://a.b.c":1,"ftp://123":1,"#1234":1},
  "attributes"  : {"??":1},
  "autocomplete" : {"off":1,"on":1},
  "axis"        : {"0":1,"AABBCCDDEEFF":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "background"  : {"url(bgg.gif)":1,"yellow":1,"red":1},
  "baseURI"     : {"/external/examples/common/":1,"<html></html>":1},
  "behavior"    : {"scroll":1,"slide":1,"alternate":1},
  "bgColor"     : {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1},
  "caption"     : {"null":1,"0":1,"AABBCC":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"":1},
  "cellIndex"   : {"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},
  "cellPadding" : {"0px":1,"0.002px":1,"99px":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "cellSpacing" : {"0px":1,"0.002px":1,"99px":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "characterSet" : {"UNKNOWN":1,"DOS-720":1,"windows-1257":1,"EUC-CN":1,"gb2312":1,"x-mac-chinesesimp":1,"unicodeFFFE":1},
  "checked"     : {"false":1,"true":1},
  "cite"        : {"http://www.quotationspage.com/quotes/Benjamin_Franklin/":1,"http://localhost:12345":1},
  "className"   : {"text":1},                               #.text {color: red;}
  "clear"       : {"all":1,"left":1,"none":1,"right":1},
  "code"        : {"HelloWorld.class":1},
  "codeBase"    : {"/external/examples/common/java/":1},
  "codeType"    : {"application/x-java-applet":1,"application/x-mplayer2":1},
  "color"       : {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1},
  "cols"        : {"200, *":1,"-299, *":1,"0px":1,"0.002px":1,"99px":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "colSpan"     : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},
  "compact"     : {"false":1,"true":1},
  "compatMode"  : {"BackCompat":1,"CSS1Compat":1},           #document
  "complete"    : {"false":1,"true":1},
  "content"     : {"text/html; charset=utf-8":1,"Dottoro":1},   #meta
  "contentDocument" : {"document":1},
  "contentEditable" : {"inherit":1,"false":1,"true":1},
  "coords"      : {"1,-1,83,125":1,"234,57,30":1,"363,37,380,40,399,35,420,47,426,63,423,78,370,57":1,"0,0,0,0":1},
  "data"        : {"flash.swf":1},                               #object
  "dateTime"    : {"2999-01-33T08:00:00Z":1,"1000-01-12T08:00:00Z":1,"2001-01-07T55:22:45+06:0":1,"":1,"":1,"":1,"":1,"":1},
  "declare"     : {"false":1,"true":1},                         #applet, object
  "defaultCharset" : {"UNKNOWN":1},                       #document ??
  "defaultChecked" : {"false":1,"true":1},
  "defaultSelected" : {"false":1,"true":1},                 #option
  "defaultValue" : {"0":1,"AABB":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "dir"         : {"ltr":1,"rtl":1},
  "disabled"    : {"false":1,"true":1},
  "draggable"   : {"false":1,"true":1},
  "placeholder" : {"0":1,"AABB":1,"":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "readOnly"    : {"false":1,"true":1},
  "rows"        : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},  #textarea
  "scope"       : {"row":1,"col":1,"rowgroup":1,"colgroup":1},
  "scrolling"   : {"auto":1,"no":1,"yes":1},
  "scrollHeight" : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "scrollLeft"  : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "scrollTop"   : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "scrollWidth" : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "search"      : {"0":1,"AABB":1,"":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "selected"    : {"false":1,"true":1},                           # option
  "selectedIndex" : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},
  "selectionStart": {"0":1,"1":1,"10":1,"100":1,"5":1,"2":1,"-99999":1},
  "selectionEnd"  : {"0":1,"1":1,"10":1,"100":1,"5":1,"2":1,"-99999":1},
  "shape"       : {"circ":1,"circle":1,"poly":1,"polygon":1,"rect":1,"rectangle":1}, #a, area
  "size"        : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},
  "span"        : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},   #col, colgroup
  "start"       : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},  #ol
  "step"        : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},   #input:range
  "tabIndex"    : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1},
  "target"      : {"_self":1,"_blank":1,"_media":1,"_parent":1,"_search":1,"_top":1},
  "text"        : {"0":1,"AABB":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "textContent" : {"0":1,"AABB":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "title"       : {"0":1,"AABB":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "type"        : {"1":1,"a":1,"A":1,"i":1,"l":1,"circle":1,"disc":1,"square":1, "button":1,"reset":1,"submit":1},
  "useMap"      : {"#SampleMap":1,"#?)(!@":1},
  "vAlign"      : {"middle":1,"bottom":1,"baseline":1,"center":1,"top":1},
  "value"       : {"0":1,"AABB":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "vLink"       : {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1},
  "vlinkColor"  : {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1},
  "vspace"      : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1,"-999px":1},
  "width"       : {"0":1,"1":1,"10":1,"100":1,"9999":1,"999999":1,"-99999":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
  "colgroup_align"  : {"bottom":1,"center":1,"left":1,"middle":1,"right":1,"top":1},
  "colgroup_bgColor": {"blue":1,"red":1,"cyan":1,"white":1,"green":1,"yellow":1,"purple":1,"#9AEECC":1,"#FEDC01":1,"#01":1},
  "colgroup_span"   : {"1":1,"0":1,"10":1,"100":1,"9999":1,"999999":1,"-1":1},
  "colgroup_ch"     : {"0":1,"AABBCCDDEEFF":1,"<div></div>":1,"<body></body>":1,"!!!@@":1,"<html></html>":1,"<script />":1,"     ":1},
  "colgroup_chOff"  : {"0px":1,"0.002px":1,"99px":1,"9999px":1,"-99999px":1,"120%":1,"520%":1,"0%":1},
}

DOM_Must_Have_Attrib = {
  "iframe"  : { "src":{ "$$[next_frame_url]":1}, },
  "frame"   : { "src":{ "$$[next_frame_url]":1}, },
}

###########################################################################################

DOM_CSS = {
  "color" : {           "blue":1 ,"red":1 ,"cyan":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1 ,"inherit":1},
  "font" : {            "inherit":1},
  "fontFamily" : {      "inherit":1 ,"Sanvito":1 ,"Critter":1 ,"Courier":1 ,"Prestige":1 ,"Tahoma":1 ,"Helvetica":1 ,"Bodoni":1},
  "fontSize" : {        "12pt":1 ,"128":1 ,"15%":1 ,"xx-small":1 ,"x-small":1 ,"small":1 ,"medium":1 ,"large":1 ,"-webkit-xxx-large":1 ,"larger":1 ,"smaller":1},
  "fontStyle" : {       "inherit":1 ,"italic":1 ,"normal":1 ,"oblique":1},
  "fontVariant" : {     "inherit":1 ,"normal":1 ,"small-caps":1},
  "fontWeight" : {      "inherit":1 ,"normal":1 ,"bold":1 ,"bolder":1 ,"lighter":1 ,"100":1 ,"200":1 ,"500":1 ,"800":1 ,"900":1},
  "textDecoration" : {  "inherit":1 ,"line-through":1 ,"none":1 ,"overline":1 ,"underline":1},
  "textShadow" : {      "inherit":1 ,"none":1 ,"green 4px 4px, blue -4px -4px":1 ,"0.1em 0.1em -0.5em #333":1},
  "direction" : {      "inherit":1 ,"ltr":1 ,"rtl":1},
  "letterSpacing" : {  "inherit":1 ,"normal":1 ,"10px":1 ,"40":1},
  "lineHeight" : {     "inherit":1 ,"normal":1 ,"30px":1 ,"120%":1 ,"1.2":1 ,"1.2em":1},
  "textAlign" : {      "inherit":1 ,"-webkit-auto":1 ,"-webkit-center":1 ,"-webkit-left":1 ,"-webkit-right":1 ,"center":1 ,"end":1 ,"justify":1 ,"left":1 ,"right":1 ,"start":1},
  "textIndent" : {     "inherit":1 ,"40px":1 ,"100px":1 ,"240px":1 ,"320p":1 ,"0px":1},
  "textOverflow" : {   "clip":1 ,"ellipsis":1},
  "textTransform" : {  "inherit":1 ,"none":1 ,"capitalize":1 ,"lowercase":1 ,"uppercase":1},
  "unicodeBidi" : {    "inherit":1 ,"normal":1 ,"bidi-override":1 ,"embed":1},
  "wordSpacing" : {    "inherit":1 ,"normal":1 ,"0px":1 ,"10px":1 ,"30px":1 ,"50px":1 ,"100px":1 ,"1000px":1},
  "whiteSpace" : {   "inherit":1 ,"normal":1 ,"nowrap":1 ,"pre":1 ,"pre-line":1 ,"pre-wrap":1},
  "wordBreak" : {    "inherit":1 ,"normal":1 ,"break-all":1 ,"keep-all":1},
  "wordWrap" : {    "inherit":1 ,"normal":1 ,"break-word":1},
  "background" : {            "inherit":1 ,"transparent none repeat scroll 0% 0%":1},
  "backgroundAttachment" : {  "inherit":1 ,"scroll":1 ,"fixed":1},
  "backgroundColor" : {       "inherit":1 ,"transparent":1 ,"#FF0000":1 ,"#237765":1 ,"green":1},
  "backgroundImage" : {       "inherit":1 ,"url(http://www.markets.co/wp-content/uploads/2015/10/panw-logo_large.png)":1},
  "backgroundPosition" : {    "0% 0%":1 ,"center":1 ,"bottom":1 ,"left":1 ,"right":1 ,"top":1 ,"100% 100%":1 ,"400% 400%":1 ,"10% 10%":1 ,"600px 800px":1},
  "backgroundPositionX" : {   "inherit":1 ,"0%":1 ,"left":1 ,"center":1 ,"right":1 ,"100%":1 ,"1000%":1 ,"-30px":1 ,"300px":1},
  "backgroundPositionY" : {   "inherit":1 ,"0%":1 ,"left":1 ,"center":1 ,"right":1 ,"100%":1 ,"1000%":1 ,"-30px":1 ,"300px":1},
  "backgroundRepeat" : {      "inherit":1 ,"repeat":1 ,"no-repeat":1 ,"repeat-x":1 ,"repeat-y":1},

  "position":       {    "static":1, "relative":1, "fixed":1, "absolute":1},

  "outline" :       {    "inherit":1 ,"5px solid blue":1},
  "outlineColor" :  {    "invert":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1 ,"inherit":1},
  "outlineStyle" :  {    "none":1 ,"inherit":1 ,"dashed":1 ,"dotted":1 ,"double":1 ,"groove":1 ,"hidden":1 ,"inherit":1 ,"inset":1 ,"outset":1 ,"ridge":1 ,"solid":1},
  "outlineWidth" :  {    "medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"2px":1 ,"20px":1 ,"200px":1},
  "outlineOffset" : {    "1px":1 ,"20px":1 ,"100px":1 ,"2000px":1 ,"inherit":1},

  "padding" : {         "0":1 ,"inherit":1 ,"2px":1 ,"20px":1 ,"200px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "paddingBottom" : {   "0":1 ,"inherit":1 ,"2px":1 ,"20px":1 ,"200px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "paddingLeft" : {     "0":1 ,"inherit":1 ,"2px":1 ,"20px":1 ,"200px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "paddingRight" : {    "0":1 ,"inherit":1 ,"2px":1 ,"20px":1 ,"200px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "paddingTop" : {      "0":1 ,"inherit":1 ,"2px":1 ,"20px":1 ,"200px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "webkitPaddingStart" : {    "0":1 ,"inherit":1 ,"2px":1 ,"20px":1 ,"200px":1 ,"2000px":1 ,"1%":1 ,"100%":1},

  "margin" : {         "0":1 ,"inherit":1 ,"auto":1 ,"0px":1 ,"100px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "marginBottom" : {   "0":1 ,"inherit":1 ,"auto":1 ,"0px":1 ,"100px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "marginLeft" : {     "0":1 ,"inherit":1 ,"auto":1 ,"0px":1 ,"100px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "marginRight" : {    "0":1 ,"inherit":1 ,"auto":1 ,"0px":1 ,"100px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "marginTop" : {      "0":1 ,"inherit":1 ,"auto":1 ,"0px":1 ,"100px":1 ,"2000px":1 ,"1%":1 ,"100%":1},
  "webkitMarginCollapse" : {        "collapse collapse":1 ,"inherit":1 ,"discard":1 ,"collapse":1 ,"separate":1},
  "webkitMarginBottomCollapse" : {  "collapse":1 ,"inherit":1 ,"discard":1 ,"separate":1},
  "webkitMarginTopCollapse" : {     "collapse":1 ,"inherit":1 ,"discard":1 ,"separate":1},
  "webkitMarginStart" : {           "0":1 ,"inherit":1 ,"auto":1 ,"2px":1 ,"20px":1 ,"200px":1 ,"2000px":1},

  "webkitMarquee" : {             "inherit":1 ,"up medium 2 normal scroll":1},
  "webkitMarqueeDirection" : {    "inherit":1 ,"auto":1 ,"ahead":1 ,"backwards":1 ,"down":1 ,"forwards":1 ,"left":1 ,"reverse":1 ,"right":1 ,"up":1},
  "webkitMarqueeIncrement" : {    "inherit":1 ,"medium":1 ,"large":1 ,"small":1 ,"1px":1 ,"10px":1 ,"100px":1 ,"1000px":1 ,"1%":1 ,"100%":1},
  "webkitMarqueeRepetition" : {   "inherit":1 ,"infinite":1 ,"-1":1 ,"0":1 ,"1":1 ,"100":1},
  "webkitMarqueeSpeed" : {        "inherit":1 ,"normal":1 ,"fast":1 ,"slow":1 ,"0":1 ,"1":1 ,"10":1 ,"100":1 ,"1000":1},
  "webkitMarqueeStyle" : {        "inherit":1 ,"scroll":1 ,"none":1 ,"slide":1 ,"alternate":1},

  "webkitLineBreak" : {      "normal":1 ,"inherit":1 ,"after-white-space":1},
  "webkitNbspMode" : {       "normal":1 ,"inherit":1 ,"space":1},
  "webkitRtlOrdering" : {    "logical":1 ,"inherit":1 ,"visual":1},
  "webkitTextFillColor" : {  "black":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "webkitTextSecurity" : {   "disc":1 ,"none":1 ,"square":1 ,"circle":1},
  "webkitTextStroke" : {     "black":1 ,"inherit":1 ,"1px red":1 ,"10px green":1 ,"100px #9AEECC":1},
  "webkitTextStrokeColor" : {"black":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "webkitTextStrokeWidth" : {"medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"1px":1 ,"10px":1 ,"100px":1 ,"1000px":1},

  "webkitUserDrag" : {    "none":1 ,"inherit":1 ,"element":1 ,"auto":1},
  "webkitUserModify" : {  "read-only":1 ,"inherit":1 ,"read-write":1 ,"read-write-plaintext-only":1},
  "webkitUserSelect" : {  "text":1 ,"inherit":1 ,"all":1 ,"none":1 ,"toggle":1},

  "webkitColumnBreakAfter" : {  "auto":1 ,"inherit":1 ,"avoid":1 ,"always":1},
  "webkitColumnBreakBefore" : { "auto":1 ,"inherit":1 ,"avoid":1 ,"always":1},
  "webkitColumnBreakInside" : { "auto":1 ,"inherit":1 ,"avoid":1 ,"always":1},
  "webkitColumnCount" : {       "auto":1, "inherit":1 ,"0":1 ,"1":1 ,"2":1 ,"100":1 ,"1000":1},
  "webkitColumnGap" : {         "0":1 ,"inherit":1 ,"1em":1 ,"10em":1 ,"100em":1 ,"1000em":1},
  "webkitColumnRule" : {        "inherit":1 ,"3px solid red":1 ,"thin dashed purple":1 ,"medium groove yellow":1},
  "webkitColumnRuleColor" : {   "none":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "webkitColumnRuleStyle" : {   "none":1 ,"dashed":1 ,"dotted":1 ,"double":1 ,"groove":1 ,"hidden":1 ,"inherit":1 ,"inset":1 ,"outset":1 ,"ridge":1 ,"solid":1},
  "webkitColumnRuleWidth" : {   "medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "webkitColumnWidth" : {       "auto":1 ,"inherit":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},

  "border" : {            "inherit":1 ,"1px double #ff0f0f":1 ,"3px solid red":1 ,"thin dashed purple":1 ,"medium groove yellow":1},
  "borderColor" : {       "transparent":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "borderStyle" : {       "none":1 ,"dashed":1 ,"dotted":1 ,"double":1 ,"groove":1 ,"hidden":1 ,"inherit":1 ,"inset":1 ,"outset":1 ,"ridge":1 ,"solid":1},
  "borderWidth" : {       "medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "borderBottom" : {      "inherit":1 ,"3px solid red":1 ,"thin dashed purple":1 ,"medium groove yellow":1},
  "borderBottomColor" : { "transparent":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "borderBottomStyle" : { "none":1 ,"dashed":1 ,"dotted":1 ,"double":1 ,"groove":1 ,"hidden":1 ,"inherit":1 ,"inset":1 ,"outset":1 ,"ridge":1 ,"solid":1},
  "borderBottomWidth" : { "medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "borderLeft" : {        "inherit":1 ,"3px solid red":1 ,"thin dashed purple":1 ,"medium groove yellow":1},
  "borderLeftColor" : {   "transparent":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "borderLeftStyle" : {   "none":1 ,"dashed":1 ,"dotted":1 ,"double":1 ,"groove":1 ,"hidden":1 ,"inherit":1 ,"inset":1 ,"outset":1 ,"ridge":1 ,"solid":1},
  "borderLeftWidth" : {   "medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "borderRight" : {       "inherit":1 ,"3px solid red":1 ,"thin dashed purple":1 ,"medium groove yellow":1},
  "borderRightColor" : {  "transparent":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "borderRightStyle" : {  "none":1 ,"dashed":1 ,"dotted":1 ,"double":1 ,"groove":1 ,"hidden":1 ,"inherit":1 ,"inset":1 ,"outset":1 ,"ridge":1 ,"solid":1},
  "borderRightWidth" : {  "medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "borderTop" : {         "inherit":1 ,"3px solid red":1 ,"thin dashed purple":1 ,"medium groove yellow":1},
  "borderTopColor" : {    "transparent":1 ,"inherit":1 ,"white":1 ,"green":1 ,"yellow":1 ,"purple":1 ,"#9AEECC":1},
  "borderTopStyle" : {    "none":1 ,"dashed":1 ,"dotted":1 ,"double":1 ,"groove":1 ,"hidden":1 ,"inherit":1 ,"inset":1 ,"outset":1 ,"ridge":1 ,"solid":1},
  "borderTopWidth" : {    "medium":1 ,"inherit":1 ,"thick":1 ,"thin":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "webkitBorderRadius" : {              "40px 30px 20px 10px":1 ,"0px 100px 0px 100px":1 ,"10px 100px 0px 0px":1},
  "webkitBorderBottomLeftRadius" : {    "1px":1 ,"10px":1 ,"100px":1 ,"1000px":1 ,"1%":1 ,"100%":1},
  "webkitBorderBottomRightRadius" : {   "1px":1 ,"10px":1 ,"100px":1 ,"1000px":1 ,"1%":1 ,"100%":1},
  "webkitBorderTopRightRadius" : {      "1px":1 ,"10px":1 ,"100px":1 ,"1000px":1 ,"1%":1 ,"100%":1},
  "webkitBorderTopLeftRadius" : {       "1px":1 ,"10px":1 ,"100px":1 ,"1000px":1 ,"1%":1 ,"100%":1},
  "webkitBorderHorizontalSpacing" : {   "0":1 ,"inherit":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "webkitBorderVerticalSpacing" : {     "0":1 ,"inherit":1 ,"0px":1 ,"10px":1 ,"100px":1 ,"9999px":1},
  "webkitBorderImage" : {               "url(http://www.markets.co/wp-content/uploads/2015/10/panw-logo_large.png) thin 27 27 27 round round":1,
                                        "url(http://www.markets.co/wp-content/uploads/2015/10/panw-logo_large.png) 2 2 2 thick stretch repeat":1},

  "webkitBoxAlign" : {       "stretch":1 ,"inherit":1 ,"baseline":1 ,"center":1 ,"end":1 ,"start":1},
  "webkitBoxDirection" : {   "normal":1 ,"inherit":1 ,"reverse":1},
  "webkitBoxFlex" : {        "0":1 ,"inherit":1 ,"1":1 ,"10":1 ,"100":1 ,"9999":1},
  "webkitBoxFlexGroup" : {   "1":1 ,"inherit":1 ,"9":1 ,"99":1 ,"999":1 ,"9999":1},
  "webkitBoxLines" : {       "single":1 ,"inherit":1 ,"multiple":1},
  "webkitBoxOrdinalGroup" : {"1":1 ,"inherit":1 ,"9":1 ,"99":1 ,"999":1 ,"9999":1},
  "webkitBoxOrient" : {      "horizontal":1 ,"inherit":1 ,"block-axis":1 ,"inline-axis":1 ,"vertical":1},
  "webkitBoxPack" : {        "start":1 ,"inherit":1 ,"justify":1 ,"end":1 ,"center":1},
  "webkitBoxShadow" : {      "none":1 ,"inherit":1 ,"5px 5px 5px gray":1 ,"99px 1px 9px green":1 ,"9px 999px 9px yellow":1},
  "webkitBoxSizing" : {      "content-box":1 ,"inherit":1 ,"border-box":1 ,"margin-box":1 ,"padding-box":1},

  "webkitAppearance" : { "none":1 ,"inherit":1 ,"button":1 ,"button-bevel":1 ,"caret":1 ,"checkbox":1 ,"listbox":1 ,"push-button":1 ,"radio":1,
    "listitem":1 ,"menulist":1 ,"menulist-button":1 ,"menulist-text":1 ,"menulist-textfield":1 ,"searchfield-decoration":1,
    "scrollbarbutton-down":1 ,"scrollbarbutton-left":1 ,"scrollbarbutton-right":1 ,"scrollbarbutton-up":1,
    "scrollbargripper-horizontal":1 ,"scrollbargripper-vertical":1 ,"scrollbarthumb-horizontal":1 ,"scrollbarthumb-vertical":1,
    "scrollbartrack-horizontal":1 ,"scrollbartrack-vertical":1 ,"searchfield":1,
    "slider-horizontal":1 ,"slider-vertical":1 ,"square-button":1 ,"textarea":1 ,"textfield":1},
  "webkitTransform" : {  "none":1 ,"inherit":1 ,"rotate(45deg)":1 ,"rotate(235deg)":1 ,"scale(2, 3)":1 ,"scale(9, 1)":1,
    "matrix(0.86,0.5,-0.5,0.866,16px,10px)":1 ,"matrix(1, 0, 0, 1, 200px, 0px)":1,
    "skewY(20deg)":1 ,"skewX(200deg)":1 ,"skew(120deg, 320deg)":1,
    "translateX(200px)":1 ,"translateY(10px)":1 ,"translate(-100px, -0px)":1 ,"translate(10px, -300px)":1},
  "webkitTransformOrigin" : { "50% 50%":1 ,"inherit":1 ,"0px 0px":1 ,"408px 110px":1 ,"120px 110px":1}
}