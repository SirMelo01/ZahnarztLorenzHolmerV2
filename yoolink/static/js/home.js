



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

/*setTimeout(() => {
  if (cookiemapselect !== null && cookiemapselect !== "false") {
    let map = L.map("map");
    map.on("focus", function () {
      map.scrollWheelZoom.enable();
    });
    map.on("blur", function () {
      map.scrollWheelZoom.disable();
    });
  }
  
}, 500);*/

mapLoad();

});



function mapLoad() {
  if (cookiemapselect === null || cookiemapselect === "false") {
    $('#covermap').removeClass('hidden');
    $('#map').addClass('hidden');
  } else {
    $('#covermap').addClass('hidden');
    const $map = $('#map');
    const mapSrc = $map.data('mapSrc');

    if (!mapSrc) {
      $('#covermap').removeClass('hidden');
      $map.addClass('hidden');
      return;
    }

    $map.removeClass('hidden').empty();

    const iframe = document.createElement('iframe');
    iframe.className = 'w-full h-full rounded-lg shadow-lg';
    iframe.src = mapSrc;
    iframe.allowFullscreen = true;
    $map.append(iframe);
  }
}

