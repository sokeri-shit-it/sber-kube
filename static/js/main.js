function disp(div) {
    if (div.style.display == "none") {
        div.style.display = "block";
    } else {
        div.style.display = "none";
    }
}

function buttons() {
    var input1 = $('#input1').val();
    var input2 = $('#input2').val();
    var input3 = $('#input3').val();
    var input4 = $('#input4').val();
    var input5 = $('#input5').val();
    var input6 = $('#input6').val();
    var input7 = $('#input7').val();
    var input8 = $('#input8').val();
    var input9 = $('#input9').val();
    var input10 = $('#input10').val();
    var input11 = $('#input11').val();
    var input12 = $('#input12').val();
    var input13 = $('#input13').val();
    if  (input1 && input2 && input3 && input4 && input5 && input6 && input7 && input8 && input9 && input10 && input11 && input12 && input13) {
                $('#submitButton').attr('disabled', false);
            } else {
                $('#submitButton').attr('disabled', true);
            }
}
