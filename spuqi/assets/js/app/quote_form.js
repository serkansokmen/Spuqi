$(function () {

    $('#id_search_query').select2({

        placeholder: $(this).attr('placeholder'),

        ajax: { // instead of writing the function to execute the request we use Select2's convenient helper

            url: Spuqi.API_URL + 'search/',
            dataType: 'json',

            data: function (term, page) {
                return {
                    title: term // search term
                    // apikey: "ju6z9mjyajq2djue3gbvv26t" // please do not use so this example keeps working
                };
            },

            results: function (data, page) { // parse the results into the format expected by Select2.
                // since we are using custom formatting functions we do not need to alter remote JSON data
                return {
                    results: data.results.sources.spuqi
                };
            }
        }
    });

    // initialize if we have existing source
    /*
    $.ajax({
        dataType: 'json',
        url: '/v1/sources/' + 1,
        success: function (data) {
            console.log(data);
        }
    });
    */
});
