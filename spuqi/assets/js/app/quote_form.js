$(function () {

    $('#id_search_query').select2({
        placeholder: $(this).attr('placeholder'),
        ajax: { // instead of writing the function to execute the request we use Select2's convenient helper
            url: "{% url 'api_search' %}",
            dataType: 'jsonp',
            data: function (term, page) {
                return {
                    q: term, // search term
                    page_limit: 10,
                    apikey: "ju6z9mjyajq2djue3gbvv26t" // please do not use so this example keeps working
                };
            },
            results: function (data, page) { // parse the results into the format expected by Select2.
                // since we are using custom formatting functions we do not need to alter remote JSON data
                return {results: data.movies};
            }
        }
    });

});
