bob = new Backbone.Model({
    name: 'Bob'
    friends: new Backbone.Collection([
        new Backbone.Model({ name: 'Fred' })
        new Backbone.Model({ name: 'John' })
    ])
})

view_model = kb.viewModel(bob)

ko.applyBindings(view_model, $('#quotes-app')[0])
