$(window).load(function(){
  // SETUP
  $('#page-title-suggestion').hide();
  $('#page-title-good-length').hide();

  $('.seo-item').hide();

  var modalTitle = $('#cms_toolbar .cms_modal .cms_modal-title', window.parent.document);

  setTimeout(function(){
    modalTitle.html('SEO-Check');
    $('.cms_modal', parent.document).find('.cms_modal-body').removeClass('cms_loader');
    $('.cms_modal', parent.document).find('.cms_btn').text('Schließen');
  }, 100);

  // TITLE
  var title = window.parent.document.title;
  if (title){
    var titleLength = title.length;
    $('.page-title-yes').show();
    $('#page-title-length').text(titleLength);
    if (titleLength < 40 || titleLength > 70) {
      $('#page-title-length-icon').removeClass('fa-check-circle');
      $('#page-title-length-icon').addClass('fa-exclamation-triangle');
      $('#page-title-suggestion').show();
    }
    else{
      $('#page-title-good-length').show();
    }
  }
  else{
    $('#page-title-no').show();
  }

  // DESCRIPTION
  var metaDescription = $('meta[name="description"]', parent.document);
  if (metaDescription) {metaDescription = metaDescription.attr("content");}

  if (metaDescription) {
    $('.meta-description-yes').show();
    $('#meta-length').text(metaDescription.length);
  }
  else{
    $('#meta-description-no').show();
  }
  
  // H1
  var ageOne =  $('h1', parent.document);

  if (ageOne.length === 0) {
   $('.h1-no').show(); 
  }
  else if (ageOne.length === 1){
    $('#one-h1').show();
  }
  else {
    $('#multiple-h1').show();
  }

  // H2
  var ageTwo =  $('h2,h3,h4,h5,h6', parent.document);

  if (ageTwo.length === 0) {
   $('.h2-no').show(); 
  }
  else {
    $('.h2-yes').show();
  }

  // TEXT
  var wordCount = 0;
  var text = $('p:visible', parent.document);
  if (text.length !== 0) {
    $('.text-yes').show();
    text.each(
      function(){
        var content = $(this).text();
        var contentLength = content.split(' ').length;
        wordCount += contentLength;
      }
    ) 
    $('#word-count').text(wordCount);
  }
  else{
    $('.text-no').show();
  }

});
