console.log('Main js is active');
console.log('home');

// Initialize animation
AOS.init({
    duration: 1000,
    once: true,
});

$(document).ready(function () {
    $('#table_id').DataTable();
    // Initialize owl carousel
    $(".owl-carousel").owlCarousel({
        loop: true,
        margin: 10,
        nav: true,
        responsive: {
            0: {
                items: 2
            },
            600: {
                items: 3
            },
            1000: {
                items: 6
            }
        },
        autoplay: true,
        autoplayTimeout: 4000,
        autoplaySpeed: 2000,
        autoplayHoverPause: false
    });

    // Scroll to contact form
    $('#contact-btn').click(() => {
        $('html, body').animate({
            scrollTop: $('#contact').offset().top - 50
        }, 1000);
    });
});

const nav = document.querySelector('#nav');
const navbar_list = document.querySelector('#navbar-list');
const sectionNav = document.querySelector('.section-nav');

// Transparent navbar only on home page
if (document.querySelector('title').innerText === 'TK') {
    console.log('home');
    nav.classList.toggle('transparent');

    window.addEventListener('scroll', function () {
        if (document.documentElement.clientWidth > 768) {
            if (pageYOffset > 100) {
                navbar_list.style.padding = '.5rem';
                if (nav.classList.contains('transparent')) {
                    nav.classList.toggle('transparent');
                }
            } else {
                navbar_list.style.padding = '2rem .5rem';
                if (!nav.classList.contains('transparent')) {
                    nav.classList.toggle('transparent');
                }
            }
        }
    });
} else {
    console.log('not home');
    sectionNav.style.position = 'static';
    navbar_list.style.padding = '.5rem';
}


