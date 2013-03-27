if (!window.App) {
    App = {};
}

App.Selector = {};
App.Selector.getSelected = function(){
    var t = '';
    if(window.getSelection) {
        t = window.getSelection();
    } else if(document.getSelection) {
        t = document.getSelection();
    } else if(document.selection) {
        t = document.selection.createRange().text;
    }
    return t;
};

App.Selector.mouseup = function(){
    var st = App.Selector.getSelected();
    if (st !== '') {
        alert('You selected:\n'+st);
    }
};

$(document).ready(function(){
    $(document).bind('mouseup', App.Selector.mouseup);
});
