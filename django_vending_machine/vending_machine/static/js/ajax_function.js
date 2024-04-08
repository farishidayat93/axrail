
function buy_item(id) {
    let wo_number = id.getAttribute('data-workorder')

    let text = `Are sure you want to change job [${wo_number}] status to run now?`

    if (confirm(text) == true) {
        var data_s = {};

        data_s.type = id.getAttribute('data-type')
        data_s.job_id = id.getAttribute('data-id')

        row_id =  data_s.type + '_' +  data_s.job_id
        $.ajax({
            type: 'POST',
            url: 'run_now',
            data: data_s,
            headers: {
                'X-CSRFToken': getCookie('csrftoken')  // Fetch CSRF token from cookie
            },
            success: function(response) {
                $('#t_' + row_id +' .job_status').html('run_now');
                $('#t_' + row_id).css("color", "green");
                $('#run_' + row_id).attr("disabled", true);
                $('#result').html(response);
            }
        });
    }
}