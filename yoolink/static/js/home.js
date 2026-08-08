



// JQuery functions
$(document).ready(function() {
  var csrfTokenInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
  var csrfToken = csrfTokenInput ? csrfTokenInput.value : undefined;
  /**
   * Email Form submit Function (index page)
   * How to use: Compare wukschweiss project
   */
  $('#emailForm').submit(function (event) {
    event.preventDefault(); // Prevent the default form submission
    $('#bSendMail').prop('disabled', true);
    console.log("Sende email...")
    // Send form data to the server using AJAX
    setTimeout(() => {
      $.ajax({
        type: 'POST',
        url: '/cms/email/request/',
        data: $("#emailForm").serialize(),
        success: function (response) {
          // Handle successful response here
          if (response.success) {
            sendNotif("Ihre Nachricht wurde erfolgreich gesendet", "success")
          }
          $('#emailForm')[0].reset();
        },
        error: function (error) {
          // Handle error response here
          console.error('Form submission failed');
          sendNotif("Etwas ist schief gelaufen. Versuchen Sie es bitte später nochmal.", "error")
        },
        complete: function() {
            // Wird ausgeführt, egal ob Erfolg oder Fehler
            $('#bSendMail').prop('disabled', false); // Button wieder aktivieren
        }
      });
    }, 500)
    
  });

// Die Google-Maps-Karte wird nicht mehr hier gebaut: Das <iframe> steht mit
// data-cookie-src im Template und wird zentral von loadinit.js ein-/ausgeblendet
// (gleiches Muster wie auf allen anderen Seiten mit externen Embeds).

});

