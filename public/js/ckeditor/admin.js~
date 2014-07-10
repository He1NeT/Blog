/**
 * @author lihuan
 */
$(document).ready(function() {
    if (typeof CKEDITOR == 'undefined') {
        alert('加载CKEditor失败');
    }else {
        var texts = $('textarea');
        $.each(texts,function(i){
            if (texts[i].id != 'id_summary') {
                var editor = CKEDITOR.replace(texts[i].id, {customConfig:"http://static.eya.cc/js/ckeditor/base.js"});
                CKFinder.SetupCKEditor(editor, '/ckfinder/');
            }            
        });
    }
});
