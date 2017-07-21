# $$[dom_attr_name


def load_js_cmd():
  return DOM_Commands

##########################################################################################

##==--==####==--==####==--==####==--==####==--==####==--==####==--==####==--==####==--==##
DOM_Commands = {
      #'contentReadOnly'     :{"status":0, "value":{"status":0, "value":"$$[bool],null"},
      'cut'                 :{"status":1, "value":"$$[bool],null"},
      'copy'                :{"status":1, "value":"$$[bool],null"},
      'paste'               :{"status":1, "value":"$$[bool],null"},
      'delete'              :{"status":1, "value":"$$[bool],null"},
      'redo'                :{"status":1, "value":"$$[bool],null"},
      'undo'                :{"status":1, "value":"$$[bool],null"},
      #'print'               :{"status":-1,"value":"$$[bool],null"},
      'selectall'           :{"status":1, "value":"$$[bool],null"},
      'unselect'            :{"status":1, "value":"$$[bool],null"},
      'bold'                :{"status":1, "value":"$$[bool],null"},
      'italic'              :{"status":1, "value":"$$[bool],null"},
      'underline'           :{"status":1, "value":"$$[bool],null"},
      'strikethrough'       :{"status":1, "value":"$$[bool],null"},
      'createlink'          :{"status":1, "value":"$$[bool],'$$[RandUrl]'"},
      'unlink'              :{"status":1, "value":"$$[bool],null"},
      'inserthtml'          :{"status":1, "value":"$$[bool],'$$[Rand_Html]'"},
      'insertimage'         :{"status":1, "value":"$$[bool],'$$[RandUrl??type==img]'"},
      'inserthorizontalrule':{"status":1, "value":"$$[bool],null"},
      'insertorderedlist'   :{"status":1, "value":"$$[bool],null"},
      'insertunorderedlist' :{"status":1, "value":"$$[bool],null"},
      'insertparagraph'     :{"status":1, "value":"$$[bool],null"},
      'decreasefontsize'    :{"status":-1,"value":"$$[bool],null"},
      'increasefontsize'    :{"status":-1,"value":"$$[bool],null"},
      'subscript'           :{"status":1, "value":"$$[bool],null"},
      'superscript'         :{"status":1, "value":"$$[bool],null"},
      'backcolor'           :{"status":1, "value":"$$[bool],'$$[color]'"},
      'forecolor'           :{"status":1, "value":"$$[bool],'$$[color]'"},
      'hilitecolor'         :{"status":1, "value":"$$[bool],'$$[color]'"},
      'justifycenter'       :{"status":1, "value":"$$[bool],null"},
      'justifyfull'         :{"status":1, "value":"$$[bool],null"},
      'justifyleft'         :{"status":1, "value":"$$[bool],null"},
      'justifyright'        :{"status":1, "value":"$$[bool],null"},
      'indent'              :{"status":1, "value":"$$[bool],null"},
      'outdent'             :{"status":1, "value":"$$[bool],null"},
      'fontname'            :{"status":1, "value":"$$[bool],'Arial'"},
      'fontSize'            :{"status":1, "value":"$$[bool],$$[int??max==20]"},
      'formatblock'         :{"status":1, "value":"$$[bool],'$$[dom_tag_name]'"},
      'removeformat'        :{"status":1, "value":"$$[bool],null"},
      'styleWithCSS'        :{"status":1, "value":"$$[bool],null"},
    }