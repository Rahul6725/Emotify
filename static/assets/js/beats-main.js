jQuery(document).ready(function ($) {
	"use strict";
	$( ".post-edit-link, .vc_inline-link" ).addClass( "musica-button" );
	$( ".single_add_to_cart_button" ).removeClass("button").addClass( "musica-button-two button-gradient-bg small-button" );
 
	/*** =====================================
    * Main Menu
    * =====================================***/
	$('#primary-menu').smartmenus({
		subMenusSubOffsetX: 1,
		subMenusSubOffsetY: 0
	});
    /*** =====================================
    * Main Menu Fixed
    * =====================================***/
    jQuery(window).on('scroll', function (){
	  	if ($(window).scrollTop() > 1){
	    	$('.menu-area').addClass('menu-fixed-top');
			$('.audio-player-area').addClass('background-overlay');
	  	} else {
	    	$('.menu-area').removeClass('menu-fixed-top');
			$('.audio-player-area').removeClass('background-overlay');
	  	}
	});
	/*** =====================================
    * Mobile Menu
    * =====================================***/
	$('.mobile-background-nav .menu-item-has-children > a').click(function(e) {
	  	e.preventDefault();
	    var $this = $(this);

	    if ($this.next().hasClass('menu-show')) {
	        $this.next().removeClass('menu-show');
	        $this.next().slideUp(350);
	    } else {
	        $this.parent().parent().find('li .dropdown-menu').removeClass('menu-show');
	        $this.parent().parent().find('li .dropdown-menu').slideUp(350);
	        $this.next().toggleClass('menu-show');
	        $this.next().slideToggle(350);
	    }
	});

	$('.mobile-menu-close i').on('click',function(){
	     $('.mobile-background-nav').removeClass('in');
	});

	$('.mobile-menu .humbarger-button i').on('click',function(){
	     $('.mobile-background-nav').toggleClass('in');
	});

	var windowHeight = $(window).height();
	$(".mobile-background-nav .mobile-inner").css({"height": windowHeight});
	$(window).on('resize',function(){
	    var windowHeight = $(window).height();
		var windowWidth = $(window).width();
	    if (windowWidth < 991) {
	        $(".mobile-background-nav .mobile-inner").css({"height": windowHeight});
	    }
	});
	/*** =====================================
    * Musica Events Counter
    * =====================================***/
	function musicaEvents() {
        var musicaEvent = $('.musica-counter-active');
        var len = musicaEvent.length;
        for (var i = 0; i < len; i++) {
            var musicaEventId = '#' + musicaEvent[i].id,
            dataValueYear	= $(musicaEventId).attr('data-year'),
			dataValueMonth   = $(musicaEventId).attr('data-month'),
			dataValueDay 	 = $(musicaEventId).attr('data-day'),
			dataValueHour    = $(musicaEventId).attr('data-hour'),
			dataValueMinute  = $(musicaEventId).attr('data-minute'),
			dataValueZone 	= $(musicaEventId).attr('data-zone');
			dataValueMonth -= 1;

            $(musicaEventId).countdown({
				
				labels: [localize_data.Years, localize_data.Months, localize_data.Weeks, localize_data.Days, localize_data.Hours, localize_data.Mins, 				 localize_data.Secs], 
				labels1: [localize_data.Year, localize_data.Month, localize_data.Week, localize_data.Day, localize_data.Hour, localize_data.Min, localize_data.Sec],
				
        		// The expanded texts for the counters 
			    //labels1: ['Year', 'Month', 'Week', 'Day', 'Hour', 'Minute', 'Second'], 
				
		        until: $.countdown.UTCDate(dataValueZone, dataValueYear, dataValueMonth, dataValueDay, dataValueHour ,dataValueMinute),
				format: 'dHMS',
		        padZeroes: true
		    });
        }
    }

    if ($('.musica-counter-active').length) {
        musicaEvents();
    }
	/*** =====================================
    * Gallery Filter
    * ==================================== ***/
	$(window).on('load', function(){
		$('.beats-loader').fadeOut();
		if($('.gallery-grid').length){
			var $grid = $('.gallery-grid').isotope({
		        itemSelector: '.grid-item',
		        percentPosition: true,
		        masonry: {
		            columnWidth: '.grid-item',
		        }
		    });
			$('.gallery-grid .zoom-button').simpleLightbox();
		}
		$('.gallery-filter ul li a').on('click', function() {
	        var filterValue = $(this).attr('data-filter');
	        $grid.isotope({
		            filter: filterValue
		    });
	    });
	});
	/** =====================================
	*  Popup Video
	* ===================================== **/
	if($('.video-play-icon').length) {
		var video_url = $('#video-play-icon').attr('data-video-url');
		$('.video-play-icon a').magnificPopup({
			items: {
		 		src: video_url
			},
			type: 'iframe', // this is default type
		});
	}
	
	/** =====================================
	*  Shop Item Cart
	* ===================================== **/
	$(document).on('click', '.value-increment-decrement .increment-button', function(){
		var pqty = $(this).parents('.value-increment-decrement').find('.product-quantity').val();
		pqty++;

		$(this).parents('.value-increment-decrement').find('.product-quantity').val(pqty);
		$( '.shop_table.cart' ).closest( 'form' ).find( 'input[name=\"update_cart\"]' ).removeProp( 'disabled' );
	});
	$(document).on('click','.value-increment-decrement .decrement-button', function(){
		var pqty = $(this).parents('.value-increment-decrement').find('.product-quantity').val();
		if(pqty>1){
			pqty--;
		}
		$(this).parents('.value-increment-decrement').find('.product-quantity').val(pqty);
		$( '.shop_table.cart' ).closest( 'form' ).find( 'input[name=\"update_cart\"]' ).removeProp( 'disabled' );
	});

	/** =====================================
	*  Nice Scroll
	* ===================================== **/
	if($('.nicescroll-active').length){
		$(".nicescroll-active").niceScroll({
			cursorborder:"",
			cursorcolor:"#00F",
			cursorwidth:0,
			boxzoom:false,
			scrollspeed:500,
			horizrailenabled:false
		});
	}
	/** =====================================
	*  Audio Player Plylist and Sound Control
	* ===================================== **/
	$('.musica-audio-player .audio-playlist').on('click',function(){
		$('.musica-audio-player .audio-playlist-wrapper').toggleClass('playlist-show');
	});
	$('.jp-volume-controls .jp-mute').on('click',function(){
		$(this).toggleClass('toggle-mute');
	});

	/**
     * =====================================
     * Back to Top Button
     * =====================================
     */
	var showoffset = 70,
	offset_opacity = 1200,
	scroll_top_duration = 700,
	$back_to_top = $('.cd-top');
	$(window).on('scroll', function() {
		($(this).scrollTop() > showoffset) ? $back_to_top.addClass('cd-is-visible'): $back_to_top.removeClass('cd-is-visible cd-fade-out');
		if ($(this).scrollTop() > offset_opacity) {
			$back_to_top.addClass('cd-fade-out');
		}
	});

    $back_to_top.on('click', function(event) {
        event.preventDefault();
        $('body,html').animate({
            scrollTop: 0,
        }, scroll_top_duration);
    });
	
	/** =====================================
	*  Gallery Post
	* ===================================== **/
	$(".blog-gallery-post").owlCarousel({
		'items':1,
		'loop':true,
		'nav':true,
		'dots':false,
		'navText': [
			"<i class='fa fa-angle-left'></i>",
			"<i class='fa fa-angle-right'></i>"
		],
	});
});
