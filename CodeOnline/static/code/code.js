var textarea = document.getElementsByTagName('textarea');
var count = textarea.length;
for(var i=0;i<count;i++){
    textarea[i].onkeydown = function(e){
        if(e.keyCode==9 || e.which==9){
            e.preventDefault();
            var s = this.selectionStart;
            this.value = this.value.substring(0,this.selectionStart) + "\t" + this.value.substring(this.selectionEnd);
            this.selectionEnd = s+1; 
        }
        else if (e.keyCode == 13 && e.shiftKey) {
            console.log("Shift+Enter")
            e.preventDefault();
            document.forms[0].submit();
        }
        else{}
    }
}

$(window).ready(function(){
    var t =$(textarea);
    t.focus().val(t.val());
 });