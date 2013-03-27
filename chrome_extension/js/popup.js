// "url": "http://local.host:8000/v1/quotes/1/",
// "privacy_state": 1,
// "quote": "Lorem ipsum",
// "owner": "serkan.sokmen",
// "source": "http://local.host:8000/v1/sources/1/"

$(function () {
    // model
    var QuoteModel = Backbone.Model.extend({ urlRoot: 'http://local.host:8000/v1/quotes' });
    var model = new QuoteModel({ id: 1 });
    model.fetch();

    // viewmodel
    var QuoteViewModel = function (quote) {
        this.url = kb.observable(quote, 'url');
        this.privacy_state = kb.observable(quote, 'privacy_state');
        this.quote = kb.observable(quote, 'quote');
        this.owner = kb.observable(quote, 'owner');
        this.source = kb.observable(quote, 'source');
    };
    var quoteViewModel = new QuoteViewModel(model);

    // binding
    ko.applyBindings(quoteViewModel, $('#kb_observable')[0]);


    // model
    var QuotesModel = Backbone.Collection.extend({ model: QuoteModel, url: 'http://local.host:8000/v1/quotes' });
    var quotesModel = new QuotesModel();
    quotesModel.fetch();

    // viewmodel
    var QuotesViewModel = function (quotes) {
        this.quotes = kb.collectionObservable(quotes);
    };
    var quotesViewModel = new QuotesViewModel(quotesModel);

    // binding
    ko.applyBindings(quotesViewModel, $('#kb_collection_observable')[0]);
});


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
