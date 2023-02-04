$(function () {
  $("#openHairs").click(function () {
    $("#openHairs").addClass("active");
    $("#openNails").removeClass("active");
    $("#hairs").addClass("active");
    $("#nails").removeClass("active");
    $(".price").css("background-size", "70rem");
  });
  $("#openNails").click(function () {
    $("#openHairs").removeClass("active");
    $("#openNails").addClass("active");
    $("#hairs").removeClass("active");
    $("#nails").addClass("active");
    $(".price").css("background-size", "90rem");
  });

  $("#datetime").focus(function () {
    $(this).attr({ type: "datetime-local" });
  });
  $("form").submit(function (e) {
    e.preventDefault;
    if (e.result == true) {
      $("#formsend").hide();
      $("#thanks").show();
    }
  });
  $(".close-btn").click(function () {
    $("#thanks").hide();
  });
});

$(document).ready(function () {
  //hide both tables and dropdown on page-load
  $("table, .dropdown-content").hide();

  //to make dropdown work
  $(".dropbtn").click(function () {
    //changes show/hide state
    $("#moreImg").toggleClass("up");
    $(".dropdown-content").toggle();
  });

  //fires when <a> in dropdown is clicked
  $(".dropdown-content a").click(function (event) {
    //prevents page refresh
    event.preventDefault();
    //hides both tables
    
    $(".dropdown-content").hide();
    //shows only desired
    $($(this).attr("href")).show();
    //modifies text in button
    $(".dropbtn").text($(this).text());
    var target = $(event.target);
    if (target.is("#mobileNails")) {
      $("#hairs").removeClass("active");
      $("#nails").addClass("active");
      $("#moreImg").removeClass("up");
    }
    if (target.is("#mobileHair")) {
      $("#hairs").addClass("active");
      $("#nails").removeClass("active");
      $("#moreImg").removeClass("up");
    }
  });
});
