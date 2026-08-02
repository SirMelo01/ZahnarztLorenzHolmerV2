$(document).ready(function() {
  var $form = $("form");
  var $cookieslider = $("#cookie");
  var $mapslider = $("#map");
  var $fontslider = $("#font");

  function cookiereload2() {
    document.cookie =
      "Cookie-Consent=" + ($cookieslider.is(":checked") ? "true" : "false") +
      "; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";

    document.cookie =
      "Cookie-Map=" + ($mapslider.is(":checked") ? "true" : "false") +
      "; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";

    document.cookie =
      "Cookie-Font=" + ($fontslider.is(":checked") ? "true" : "false") +
      "; expires=" + new Date(9999, 0, 1).toUTCString() + "; path=/";
  }

  // Onload functionality
  if (cookieselect === "true") {
    $cookieslider.prop("checked", true);
  }
  if (cookiemapselect === "true") {
    $mapslider.prop("checked", true);
  }
  if (cookiefontselect === "true") {
    $fontslider.prop("checked", true);
  }

  $cookieslider.on("change", function() {
    if ($cookieslider.is(":checked")) {
      $mapslider.prop("checked", true);
      $fontslider.prop("checked", true);
    } else {
      $mapslider.prop("checked", false);
      $fontslider.prop("checked", false);
    }
    cookiereload2();
  });

  $mapslider.on("change", function() {
    if ($mapslider.is(":checked")) {
      if ($fontslider.is(":checked")) {
        $cookieslider.prop("checked", true);
      }
    } else {
      $cookieslider.prop("checked", false);
    }
    cookiereload2();
  });

  $fontslider.on("change", function() {
    if ($fontslider.is(":checked")) {
      if ($mapslider.is(":checked")) {
        $cookieslider.prop("checked", true);
      }
    } else {
      $cookieslider.prop("checked", false);
    }
    cookiereload2();
  });
});
